import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor

import boto3
from botocore.config import Config
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_aws.models.sts import (
    AssumeRoleRequest,
    AssumedRoleResponse,
)
from werkflow_system import System
from werkflow_aws.types import STSClient

import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    """
    Lambda function that assumes a proxy role, then uses it to assume a role
    in another account and list S3 buckets.
    """

    # Define role ARNs
    proxy_role_arn = "arn:aws:iam::339712954262:role/delegate-admin-finops-metadata-collector"
    target_role_arn = "arn:aws:iam::654654312378:role/finops-metadata-collector-role"

    try:
        # Step 1: Assume the proxy role in the same account
        sts_client = boto3.client('sts')

        print(f"Assuming proxy role: {proxy_role_arn}")
        proxy_assumed_role = sts_client.assume_role(
            RoleArn=proxy_role_arn,
            RoleSessionName='LambdaProxyRoleSession'
        )

        # Extract credentials from the proxy role
        proxy_credentials = proxy_assumed_role['Credentials']

        # Step 2: Create new STS client using proxy role credentials
        proxy_sts_client = boto3.client(
            'sts',
            aws_access_key_id=proxy_credentials['AccessKeyId'],
            aws_secret_access_key=proxy_credentials['SecretAccessKey'],
            aws_session_token=proxy_credentials['SessionToken']
        )

        # Step 3: Use proxy role to assume the target role in the remote account
        print(f"Using proxy role to assume target role: {target_role_arn}")
        target_assumed_role = proxy_sts_client.assume_role(
            RoleArn=target_role_arn,
            RoleSessionName='LambdaTargetRoleSession'
        )

        # Extract credentials from the target role
        target_credentials = target_assumed_role['Credentials']

        # Step 4: Create S3 client using target role credentials
        s3_client = boto3.client(
            's3',
            aws_access_key_id=target_credentials['AccessKeyId'],
            aws_secret_access_key=target_credentials['SecretAccessKey'],
            aws_session_token=target_credentials['SessionToken']
        )

        # Step 5: List S3 buckets in the target account
        print("Listing S3 buckets in target account...")
        response = s3_client.list_buckets()

        buckets = response.get('Buckets', [])
        bucket_names = [bucket['Name'] for bucket in buckets]

        result = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully listed S3 buckets',
                'target_account': '654654312378',
                'bucket_count': len(buckets),
                'buckets': bucket_names
            }, indent=2)
        }

        print(f"Found {len(buckets)} buckets: {bucket_names}")
        return result

    except ClientError as e:
        error_message = f"AWS Error: {e.response['Error']['Code']} - {e.response['Error']['Message']}"
        print(error_message)

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_message,
                'error_type': e.response['Error']['Code']
            })
        }

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_message,
                'error_type': 'UnexpectedError'
            })
        }

class AWSSTS:

    def __init__(self):
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client: STSClient | None = None
        self._proxy_client: STSClient | None = None


        self.service_name = 'STS'

        self._regions = AWSRegionMap()

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()       

        self._client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def connect_unauthorized(
        self,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def assume_role_by_proxy(
        self,
        assume_role_request: AssumeRoleRequest,
        assume_proxy_role_request: AssumeRoleRequest,
        region: RegionName,

    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        aws_region = self._regions.get(region)
        
        self._proxy_client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                config=Config(
                    region_name=aws_region.value
                )
            )
        )
        
        proxy_response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.assume_role,
                **assume_proxy_role_request.model_dump(exclude_none=True)
            )
        )

        assumed_proxy_response = AssumedRoleResponse(**proxy_response)

        self._client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                aws_access_key_id=assumed_proxy_response.Credentials.AccessKeyId,
                aws_secret_access_key=assumed_proxy_response.Credentials.SecretAccessKey,
                aws_session_token=assumed_proxy_response.Credentials.SessionToken,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

        assume_response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.assume_role,
                **assume_role_request.model_dump(exclude_none=True)
            )
        )

        return AssumedRoleResponse(**assume_response)

    async def assume_role(
        self,
        assume_role_request: AssumeRoleRequest
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.assume_role,
                **assume_role_request.model_dump(exclude_none=True)
            )
        )

        return AssumedRoleResponse(**response)
    
    async def close(self):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()     

        if self._client:
            await self._loop.run_in_executor(
                None,
                self._client.close
            )

        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._client.close()
        self._system.abort()
        self._executor.shutdown()