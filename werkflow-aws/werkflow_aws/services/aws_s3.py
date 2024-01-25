import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.exceptions import (
    EmptyResponseException,
    UnsetAWSConnectionException
)
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegion
)
from werkflow_aws.models.s3 import (
    AWSs3ListBucketOptions,
    AWSs3GetObjectOptions,
    AWSs3PutObjectOptions,
    AWSs3DeleteBucketOptions,
    AWSs3DeleteObjectOptions,
    AWSs3ListMultipartUploadOptions,
    AWSs3ListPartsOptions
)


from werkflow_aws.types import (
    s3Client
)
from werkflow.modules.system import System
from typing import (
    Union, 
    Optional,
    BinaryIO,
    TextIO
)


class AWSs3:
    
    def __init__(self) -> None:
        
        self._system = System()

        self._loop: Union[asyncio.AbstractEventLoop, None] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 's3'

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: AWSRegion
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: s3Client = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                's3',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region=region.value
                )
            )
        )

    async def list_buckets(self):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        buckets = await self._loop.run_in_executor(
            self._executor,
            self._client.list_buckets
        )

    async def list_objects(
        self,
        bucket: str,
        options: Optional[AWSs3ListBucketOptions]=None
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        
        if options is None:
            options = AWSs3ListBucketOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_objects_v2(),
                Bucket=bucket,
                **options.to_options()
            )
        )

    async def get_object(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3GetObjectOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        
        if options is None:
            options = AWSs3GetObjectOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_object,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

    async def put_object(
        self,
        bucket: str,
        key: str,
        body: Union[bytes, BinaryIO, TextIO],
        options: Optional[AWSs3PutObjectOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        
        if options is None:
            options = AWSs3PutObjectOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_object,
                Bucket=bucket,
                Key=key,
                Body=body,
                **options.to_options()
            )
        )

    async def delete_bucket(
            self,
            bucket: str,
            options: Optional[AWSs3DeleteBucketOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3DeleteBucketOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                **options.to_options()
            )
        )

    async def delete_object(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3DeleteObjectOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3DeleteObjectOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

    async def list_multipart_uploads(
        self,
        bucket: str,
        options: Optional[AWSs3ListMultipartUploadOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3ListMultipartUploadOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_multipart_uploads,
                Bucket=bucket,
                **options.to_options()
            )
        )

    async def list_parts(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3ListPartsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3ListPartsOptions()

        buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_multipart_uploads,
                Bucket=bucket,
                **options.to_options()
            )
        )

    async def complete_multipart_upload(
        self,
        bucket: str,
        key: str
    ):
        pass
    
    async def close(self):
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