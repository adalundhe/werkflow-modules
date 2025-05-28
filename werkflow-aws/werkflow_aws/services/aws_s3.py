import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from io import FileIO
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_aws.models.s3 import (
    AWSs3AbortMultipartUploadOptions,
    AWSs3AbortMultipartUploadResponse,
    AWSs3CreateMultipartUploadOptions,
    AWSs3CreateMultipartUploadResponse,
    AWSs3CompleteMultipartUploadOptions,
    AWSs3CompleteMultipartUploadResponse,
    AWSs3CopySource,
    AWSs3CopyObjectOptions,
    AWSs3CopyObjectResponse,
    AWSs3DeleteBucketOptions,
    AWSs3DeleteBucketReponse,
    AWSs3DeleteBucketTaggingOptions,
    AWSs3DeleteObjectTaggingResponse,
    AWSs3DeleteObjectOptions,
    AWSs3DeleteObjectResponse,
    AWSs3DeleteObjectTaggingOptions,
    AWSs3DeleteBucketTaggingResponse,
    AWSs3DeleteObjectsOptions,
    AWSs3DeleteObjectsResponse,
    AWSs3GeneratePresignedURLOptions,
    AWSs3GeneratePresignedURLResponse,
    AWSs3GetBucketTaggingOptions,
    AWSs3GetBucketTaggingResponse,
    AWSs3GetObjectOptions,
    AWSs3GetObjectResponse,
    AWSs3GetObjectTaggingOptions,
    AWSs3GetObjectTaggingResponse,
    AWSs3ListBucketsResponse,
    AWSs3GeneratePresignedPostOptions,
    AWSs3GeneratePresignedPostResponse,
    AWSs3ListDirectoryBucketsOptions,
    AWSs3ListDirectoryBucketsResponse,
    AWSs3ListObjectsOptions,
    AWSs3ListObjectsResponse,
    AWSs3ListObjectVersionsOptions,
    AWSs3ListObjectVersionsResponse,
    AWSs3ListMultipartUploadsOptions,
    AWSs3ListMultipartUploadsResponse,
    AWSs3ListPartsOptions,
    AWSs3ListPartsResponse,
    AWSs3MultipartUpload,
    AWSs3Object,
    AWSs3PutBucketTaggingOptions,
    AWSs3PutBucketTaggingResponse,
    AWSs3PutBucketVersioningOptions,
    AWSs3PutBucketVersioningResponse,
    AWSs3PutObjectOptions,
    AWSs3PutObjectResponse,
    AWSs3PutObjectTaggingOptions,
    AWSs3PutObjectTaggingResponse,
    AWSs3StreamingBody,
    AWSs3Tag,
    AWSs3TransferConfigOptions,
    AWSs3TransferAllowedUploadArgs,
    AWSs3UploadPartCopyOptions,
    AWSs3UploadPartCopyResponse,
    AWSs3UploadPartOptions,
    AWSs3UploadPartResponse
)
from typing import List


from werkflow_aws.types import (
    s3Client
)
from werkflow_system import System
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
        self._regions = AWSRegionMap()
    
    async def sso(
        self,
        profile_name: str,
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            None,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name
            )
        )

        self._client: s3Client = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                's3',
            )
        )

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: RegionName,
    ):

        aws_region = self._regions.get(region)

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
                    region_name=aws_region.value
                )
            )
        )

    async def list_buckets(self):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        
        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        listed_buckets = await self._loop.run_in_executor(
            self._executor,
            self._client.list_buckets
        )
        
        return AWSs3ListBucketsResponse(**listed_buckets)

    async def list_objects(
        self,
        bucket: str,
        options: AWSs3ListObjectsOptions | None=None
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        if options is None:
            options = AWSs3ListObjectsOptions()

        listed_objects = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_objects_v2,
                Bucket=bucket,
                **options.to_data()
            )
        )

        return AWSs3ListObjectsResponse(**listed_objects)

    async def get_object(
        self,
        bucket: str,
        key: str,
        options: AWSs3GetObjectOptions | None=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        if options is None:
            options = AWSs3GetObjectOptions()

        retrieved_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_object,
                Bucket=bucket,
                Key=key,
                **options.to_data()
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
        body: bytes | BinaryIO | TextIO,
        options: AWSs3PutObjectOptions | None=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        if options is None:
            options = AWSs3PutObjectOptions()

        updated_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_object,
                Bucket=bucket,
                Key=key,
                Body=body,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3DeleteBucketOptions()

        deleted_bucket = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        if options is None:
            options = AWSs3DeleteObjectOptions()

        deleted_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket,
                Bucket=bucket,
                Key=key,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        if options is None:
            options = AWSs3ListMultipartUploadsOptions()

        multipart_uploads = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_multipart_uploads,
                Bucket=bucket,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3ListPartsOptions()

        parts = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_parts,
                Bucket=bucket,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3CompleteMultipartUploadOptions()

        completed_multipart_upload = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.complete_multipart_upload,
                Bucket=bucket,
                Key=key,
                MultipartUpload=upload_parts.to_data(),
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3AbortMultipartUploadOptions()
        
        aborted_uploads = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.abort_multipart_upload,
                Bucket=bucket,
                Key=key,
                UploadId=upload_id,
                **options.to_data()
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

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3CreateMultipartUploadOptions()

        created_multipart_upload = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.create_multipart_upload,
                Bucket=bucket,
                Key=key,
                **options.to_data()
            )
        )

        return AWSs3CreateMultipartUploadResponse(**created_multipart_upload)

    async def upload_multiupload_part(
        self,
        bucket: str,
        key: str,
        part_number: str,
        upload_id: str,
        options: AWSs3UploadPartOptions | None = None
    ): 
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3UploadPartOptions()

        uploaded_part = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_part,
                Bucket=bucket,
                Key=key,
                PartNumber=part_number,
                UploadId=upload_id,
                **options.to_data()
            )
        )

        return AWSs3UploadPartResponse(**uploaded_part)

    async def upload_multiupload_part_copy(
        self,
        bucket: str,
        key: str,
        part_number: str,
        upload_id: str,
        options: AWSs3UploadPartCopyOptions | None = None,
    ): 
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3UploadPartCopyOptions()

        copied_upload_part = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_part_copy,
                Bucket=bucket,
                Key=key,
                PartNumber=part_number,
                UploadId=upload_id,
                **options.to_data()
            )
        )

        return AWSs3UploadPartCopyResponse(**copied_upload_part)
    
    async def upload_file_object(
        self,
        file_object: FileIO,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs]=None,
        config: Optional[AWSs3TransferConfigOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3TransferAllowedUploadArgs()

        if config is None:
            config = AWSs3TransferConfigOptions()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_fileobj,
                file_object,
                bucket,
                key,
                options,
                None,
                config
            )
        )

        await self._loop.run_in_executor(
            self._executor,
            file_object.close
        )

    async def upload_file(
        self,
        path: str,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs]=None,
        config: Optional[AWSs3TransferConfigOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3TransferAllowedUploadArgs()

        if config is None:
            config = AWSs3TransferConfigOptions()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.upload_file,
                path,
                bucket,
                key,
                options,
                None,
                config
            )
        )

    async def list_directory_buckets(
        self,
        options: Optional[AWSs3ListDirectoryBucketsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3ListDirectoryBucketsOptions()

        directory_buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_directory_buckets,
                **options.to_data()
            )
        )

        return AWSs3ListDirectoryBucketsResponse(**directory_buckets)
    
    async def list_object_versions(
        self,
        bucket: str=None,
        options: Optional[AWSs3ListObjectVersionsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3ListObjectVersionsOptions()

        directory_buckets = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_object_versions,
                Bucket=bucket,
                **options.to_data()
            )
        )

        return AWSs3ListObjectVersionsResponse(**directory_buckets)
    
    async def delete_objects(
        self,
        bucket: str,
        objects: List[AWSs3Object],
        quiet: bool=False,
        options: Optional[AWSs3DeleteObjectsOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3DeleteObjectsOptions()

        delete_request = {
            'Delete': [
                s3_object.model_dump() for s3_object in objects
            ],
            'Quiet': quiet
        }

        deleted_objects = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_object_versions,
                Bucket=bucket,
                Delete=delete_request,
                **options.to_data()
            )
        )

        return AWSs3DeleteObjectsResponse(**deleted_objects)
    
    async def download_file_object(
        self,
        file_object: FileIO,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs]=None,
        config: Optional[AWSs3TransferConfigOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3TransferAllowedUploadArgs()

        if config is None:
            config = AWSs3TransferConfigOptions()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.download_fileobj,
                file_object,
                bucket,
                key,
                options,
                None,
                config
            )
        )

        await self._loop.run_in_executor(
            self._executor,
            file_object.close
        )

    async def download_file(
        self,
        path: str,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs]=None,
        config: Optional[AWSs3TransferConfigOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3TransferAllowedUploadArgs()

        if config is None:
            config = AWSs3TransferConfigOptions()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.download_file,
                path,
                bucket,
                key,
                options,
                None,
                config
            )
        )
    
    async def generate_presigned_url(
        self,
        client_method: str,
        options: Optional[AWSs3GeneratePresignedURLOptions]=None
    ) -> str:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3GeneratePresignedURLOptions()

        presigned_url = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.generate_presigned_url,
                client_method,
                **options.to_data()
            )
        )

        return AWSs3GeneratePresignedURLResponse(
            URL=presigned_url
        )
    
    async def geneate_presigned_post(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3GeneratePresignedPostOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3GeneratePresignedPostOptions()

        presigned_post = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.generate_presigned_post,
                Bucket=bucket,
                Key=key,
                **options.to_data()
            )
        )

        return AWSs3GeneratePresignedPostResponse(**presigned_post)
    
    async def copy_object(
        self,
        bucket: str,
        copy_source: str | AWSs3CopySource,
        key: str,
        options: Optional[AWSs3CopyObjectOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3CopyObjectOptions()

        if isinstance(copy_source, AWSs3CopySource):
            copy_source = copy_source.to_data()

        copied_object = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.copy_object,
                Bucket=bucket,
                CopySource=copy_source,
                Key=key,
                **options.to_data()
            )
        )

        return AWSs3CopyObjectResponse(**copied_object)
    
    async def copy(
        self,
        copy_source: AWSs3CopySource,
        bucket: str,
        key: str,
        config: Optional[AWSs3TransferConfigOptions]=None,
        options: AWSs3TransferAllowedUploadArgs | None = None,
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3TransferAllowedUploadArgs()

        if config is None:
            config = AWSs3TransferConfigOptions()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.copy,
                copy_source.to_data(),
                bucket,
                key,
                ExtraArgs=options,
                Callback=None,
                SourceClient=None,
                Config=config
            )
        )

    async def put_bucket_versioning(
        self,
        bucket: str,
        options: Optional[AWSs3PutBucketVersioningOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3PutBucketVersioningOptions()

        bucket_versioning = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_bucket_versioning,
                Bucket=bucket,
                **options.to_data()
            )
        )

        return AWSs3PutBucketVersioningResponse(**bucket_versioning)
    
    async def get_bucket_tagging(
        self,
        bucket: str,
        options: Optional[AWSs3GetBucketTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3GetBucketTaggingOptions()

        bucket_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_bucket_tagging,
                Bucket=bucket,
                **options.to_data()
            )
        )

        return AWSs3GetBucketTaggingOptions(**bucket_tagging)
    
    async def get_object_tagging(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3GetObjectTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3GetObjectTaggingOptions()

        bucket_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_bucket_tagging,
                Bucket=bucket,
                Key=key,
                **options.to_data()
            )
        )

        return AWSs3GetObjectTaggingResponse(**bucket_tagging)
    
    async def put_bucket_tagging(
        self,
        bucket: str,
        tags: List[AWSs3Tag],
        options: Optional[AWSs3PutBucketTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3PutBucketTaggingOptions()

        bucket_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_bucket_tagging,
                Bucket=bucket,
                Tagging={
                    'TagSet': [
                        tag.to_data() for tag in tags
                    ]
                },
                **options.to_data()
            )
        )

        return AWSs3PutBucketTaggingResponse(**bucket_tagging)
    
    async def put_bucket_tagging(
        self,
        bucket: str,
        key: str,
        tags: List[AWSs3Tag],
        options: Optional[AWSs3PutObjectTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3PutObjectTaggingOptions()

        object_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.put_object_tagging,
                Bucket=bucket,
                Key=key,
                Tagging={
                    'TagSet': [
                        tag.to_data() for tag in tags
                    ]
                },
                **options.to_data()
            )
        )

        return AWSs3PutObjectTaggingResponse(**object_tagging)
    
    async def delete_bucket_tagging(
        self,
        bucket: str,
        options: Optional[AWSs3DeleteBucketTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3PutObjectTaggingOptions()

        deleted_bucket_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_bucket_tagging,
                Bucket=bucket,
                **options.to_data()
            )
        )

        return AWSs3DeleteBucketTaggingResponse(**deleted_bucket_tagging)
    
    async def delete_object_tagging(
        self,
        bucket: str,
        key: str,
        options: Optional[AWSs3DeleteObjectTaggingOptions]=None
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 

        if options is None:
            options = AWSs3DeleteObjectTaggingOptions()

        deleted_object_tagging = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.delete_object_tagging,
                Bucket=bucket,
                Key=key,
                **options.to_data()
            )
        )

        return AWSs3DeleteObjectTaggingResponse(**deleted_object_tagging)

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