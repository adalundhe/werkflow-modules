import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from io import FileIO
from werkflow_aws.exceptions import (
    EmptyResponseException,
    UnsetAWSConnectionException
)
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegion
)
from werkflow_aws.models.s3 import (
    AWSs3AbortMultipartUploadOptions,
    AWSs3AbortMultipartUploadResponse,
    AWSs3CreateMultipartUploadOptions,
    AWSs3CreateMultipartUploadResponse,
    AWSs3CompleteMultipartUploadOptions,
    AWSs3CompleteMultipartUploadResponse,
    AWSs3DeleteBucketOptions,
    AWSs3DeleteBucketReponse,
    AWSs3DeleteObjectOptions,
    AWSs3DeleteObjectResponse,
    AWSs3GetObjectOptions,
    AWSs3GetObjectResponse,
    AWSs3ListBucketsResponse,
    AWSs3ListObjectsOptions,
    AWSs3ListObjectsResponse,
    AWSs3ListMultipartUploadsOptions,
    AWSs3ListMultipartUploadsResponse,
    AWSs3ListPartsOptions,
    AWSs3ListPartsResponse,
    AWSs3MultipartUpload,
    AWSs3PutObjectOptions,
    AWSs3PutObjectResponse,
    AWSs3StreamingBody,
    AWSs3UploadPartCopyOptions,
    AWSs3UploadPartCopyResponse,
    AWSs3UploadPartOptions,
    AWSs3UploadPartResponse
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

        listed_buckets = await self._loop.run_in_executor(
            self._executor,
            self._client.list_buckets
        )
        
        return AWSs3ListBucketsResponse(**listed_buckets)

    async def list_objects(
        self,
        bucket: str,
        options: Optional[AWSs3ListObjectsOptions]=None
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        
        if options is None:
            options = AWSs3ListObjectsOptions()

        listed_objects = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_objects_v2,
                Bucket=bucket,
                **options.to_options()
            )
        )

        return AWSs3ListObjectsResponse(**listed_objects)

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

        retrieved_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_object,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

        return AWSs3GetObjectResponse(
            **retrieved_object,
            Body=AWSs3StreamingBody(
                retrieved_object['Body']
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

        updated_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_object,
                Bucket=bucket,
                Key=key,
                Body=body,
                **options.to_options()
            )
        )

        return AWSs3PutObjectResponse(**updated_object)

    async def delete_bucket(
            self,
            bucket: str,
            options: Optional[AWSs3DeleteBucketOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3DeleteBucketOptions()

        deleted_bucket = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                **options.to_options()
            )
        )

        return AWSs3DeleteBucketReponse(**deleted_bucket)
    
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

        deleted_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )
        
        return AWSs3DeleteObjectResponse(**deleted_object)

    async def list_multipart_uploads(
        self,
        bucket: str,
        options: Optional[AWSs3ListMultipartUploadsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3ListMultipartUploadsOptions()

        multipart_uploads = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_multipart_uploads,
                Bucket=bucket,
                **options.to_options()
            )
        )

        return AWSs3ListMultipartUploadsResponse(**multipart_uploads)

    async def list_multipart_upload_parts(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3ListPartsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3ListPartsOptions()

        parts = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_parts,
                Bucket=bucket,
                **options.to_options()
            )
        )

        return AWSs3ListPartsResponse(**parts)

    async def complete_multipart_upload(
        self,
        bucket: str,
        key: str,
        upload_parts: AWSs3MultipartUpload,
        options: Optional[AWSs3CompleteMultipartUploadOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3CompleteMultipartUploadOptions()

        completed_multipart_upload = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.complete_multipart_upload,
                Bucket=bucket,
                Key=key,
                MultipartUpload=upload_parts.to_options(),
                **options.to_options()
            )
        )

        return AWSs3CompleteMultipartUploadResponse(**completed_multipart_upload)

    async def abort_multipart_upload(
        self,
        bucket: str,
        key: str,
        upload_id: str,
        options: Optional[AWSs3AbortMultipartUploadOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3AbortMultipartUploadOptions()
        
        aborted_uploads = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.abort_multipart_upload,
                Bucket=bucket,
                Key=key,
                UploadId=upload_id,
                **options.to_options()
            )
        )

        return AWSs3AbortMultipartUploadResponse(**aborted_uploads)

    async def create_multipart_upload(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3CreateMultipartUploadOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3CreateMultipartUploadOptions()

        created_multipart_upload = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.create_multipart_upload,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

        return AWSs3CreateMultipartUploadResponse(**created_multipart_upload)

    async def upload_multiupload_part(
        self,
        bucket: str,
        key: str,
        part_number: str,
        upload_id: str
    ): 
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3UploadPartOptions()

        uploaded_part = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_part,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

        return AWSs3UploadPartResponse(**uploaded_part)

    async def upload_multiupload_part_copy(
        self,
        bucket: str,
        key: str,
        part_number: str,
        upload_id: str
    ): 
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if options is None:
            options = AWSs3UploadPartCopyOptions()

        copied_upload_part = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_part_copy,
                Bucket=bucket,
                Key=key,
                **options.to_options()
            )
        )

        return AWSs3UploadPartCopyResponse(**copied_upload_part)
    
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