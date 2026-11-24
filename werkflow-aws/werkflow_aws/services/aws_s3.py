import functools
from typing import Any, BinaryIO, Optional
from pydantic import AnyHttpUrl

from werkflow_aws.models.s3 import (
    AWSS3CopyObjectRequest,
    AWSS3CreateBucketRequest,
    AWSS3CreateBucketResponse,
    AWSS3DeleteBucketCorsRequest,
    AWSS3DeleteBucketCorsResponse,
    AWSS3DeleteBucketEncryptionRequest,
    AWSS3DeleteBucketEncryptionResponse,
    AWSS3DeleteBucketLifecycleRequest,
    AWSS3DeleteBucketLifecycleResponse,
    AWSS3DeleteBucketOwnershipControlsRequest,
    AWSS3DeleteBucketOwnershipControlsResponse,
    AWSS3DeleteBucketPolicyRequest,
    AWSS3DeleteBucketPolicyResponse,
    AWSS3DeleteBucketRequest,
    AWSS3DeleteBucketResponse,
    AWSS3DeleteBucketTaggingRequest,
    AWSS3DeleteBucketWebsiteRequest,
    AWSS3DeleteBucketWebsiteResponse,
    AWSS3DeleteObjectRequest,
    AWSS3DeleteObjectResponse,
    AWSS3DeleteObjectTaggingRequest,
    AWSS3DeleteObjectsRequest,
    AWSS3DeletePublicAccessBlockRequest,
    AWSS3DeletePublicAccessBlockResponse,
    AWSS3GeneratePresignedPostRequest,
    AWSS3GeneratePresignedURLRequest,
    AWSS3GetBucketAccelerateConfigurationRequest,
    AWSS3GetBucketAccelerateConfigurationResponse,
    AWSS3GetBucketAclRequest,
    AWSS3GetBucketAclResponse,
    AWSS3GetBucketCorsRequest,
    AWSS3GetBucketCorsResponse,
    AWSS3GetBucketEncryptionRequest,
    AWSS3GetBucketEncryptionResponse,
    AWSS3GetBucketLifecycleConfigurationRequest,
    AWSS3GetBucketLifecycleConfigurationResponse,
    AWSS3GetBucketLocationRequest,
    AWSS3GetBucketLocationResponse,
    AWSS3GetBucketLoggingRequest,
    AWSS3GetBucketLoggingResponse,
    AWSS3GetBucketNotificationConfigurationRequest,
    AWSS3GetBucketNotificationConfigurationResponse,
    AWSS3GetBucketOwnershipControlsRequest,
    AWSS3GetBucketOwnershipControlsResponse,
    AWSS3GetBucketPolicyRequest,
    AWSS3GetBucketPolicyResponse,
    AWSS3GetBucketPolicyStatusRequest,
    AWSS3GetBucketPolicyStatusResponse,
    AWSS3GetBucketRequestPaymentRequest,
    AWSS3GetBucketRequestPaymentResponse,
    AWSS3GetBucketTaggingRequest,
    AWSS3GetBucketVersioningRequest,
    AWSS3GetBucketVersioningResponse,
    AWSS3GetBucketWebsiteRequest,
    AWSS3GetBucketWebsiteResponse,
    AWSS3GetObjectAclRequest,
    AWSS3GetObjectAclResponse,
    AWSS3GetObjectAttributesRequest,
    AWSS3GetObjectAttributesResponse,
    AWSS3GetObjectLegalHoldRequest,
    AWSS3GetObjectLegalHoldResponse,
    AWSS3GetObjectLockConfigurationRequest,
    AWSS3GetObjectLockConfigurationResponse,
    AWSS3GetObjectRequest,
    AWSS3GetObjectResponse,
    AWSS3GetObjectRetentionRequest,
    AWSS3GetObjectRetentionResponse,
    AWSS3GetObjectTaggingRequest,
    AWSS3GetPublicAccessBlockRequest,
    AWSS3GetPublicAccessBlockResponse,
    AWSS3HeadBucketRequest,
    AWSS3HeadBucketResponse,
    AWSS3HeadObjectRequest,
    AWSS3HeadObjectResponse,
    AWSS3ListBucketsRequest,
    AWSS3ListDirectoryBucketsRequest,
    AWSS3ListObjectVersionsRequest,
    AWSS3ListObjectsRequest,
    AWSS3ListObjectsResponse,
    AWSS3PutBucketAccelerateConfigurationRequest,
    AWSS3PutBucketAccelerateConfigurationResponse,
    AWSS3PutBucketAclRequest,
    AWSS3PutBucketAclResponse,
    AWSS3PutBucketCorsRequest,
    AWSS3PutBucketCorsResponse,
    AWSS3PutBucketEncryptionRequest,
    AWSS3PutBucketEncryptionResponse,
    AWSS3PutBucketLifecycleConfigurationRequest,
    AWSS3PutBucketLifecycleConfigurationResponse,
    AWSS3PutBucketLoggingRequest,
    AWSS3PutBucketLoggingResponse,
    AWSS3PutBucketNotificationConfigurationRequest,
    AWSS3PutBucketNotificationConfigurationResponse,
    AWSS3PutBucketOwnershipControlsRequest,
    AWSS3PutBucketOwnershipControlsResponse,
    AWSS3PutBucketPolicyRequest,
    AWSS3PutBucketPolicyResponse,
    AWSS3PutBucketRequestPaymentRequest,
    AWSS3PutBucketRequestPaymentResponse,
    AWSS3PutBucketTaggingRequest,
    AWSS3PutBucketVersioningRequest,
    AWSS3PutBucketWebsiteRequest,
    AWSS3PutBucketWebsiteResponse,
    AWSS3PutObjectAclRequest,
    AWSS3PutObjectAclResponse,
    AWSS3PutObjectLegalHoldRequest,
    AWSS3PutObjectLegalHoldResponse,
    AWSS3PutObjectLockConfigurationRequest,
    AWSS3PutObjectLockConfigurationResponse,
    AWSS3PutObjectRequest,
    AWSS3PutObjectResponse,
    AWSS3PutObjectRetentionRequest,
    AWSS3PutObjectRetentionResponse,
    AWSS3PutObjectTaggingRequest,
    AWSS3PutPublicAccessBlockRequest,
    AWSS3PutPublicAccessBlockResponse,
    AWSS3RestoreObjectRequest,
    AWSS3RestoreObjectResponse,
    AWSS3StreamingBody,
    AWSs3AbortMultipartUploadRequest,
    AWSs3AbortMultipartUploadResponse,
    AWSs3CompleteMultipartUploadRequest,
    AWSs3CompleteMultipartUploadResponse,
    AWSs3CopyObjectResponse,
    AWSs3CopySource,
    AWSs3CreateMultipartUploadRequest,
    AWSs3CreateMultipartUploadResponse,
    AWSs3DeleteBucketTaggingResponse,
    AWSs3DeleteObjectTaggingResponse,
    AWSs3DeleteObjectsResponse,
    AWSs3GeneratePresignedPostResponse,
    AWSs3GeneratePresignedURLResponse,
    AWSs3GetBucketTaggingResponse,
    AWSs3GetObjectTaggingResponse,
    AWSs3ListBucketsResponse,
    AWSs3ListDirectoryBucketsResponse,
    AWSs3ListMultipartUploadsRequest,
    AWSs3ListMultipartUploadsResponse,
    AWSs3ListObjectVersionsResponse,
    AWSs3ListPartsRequest,
    AWSs3ListPartsResponse,
    AWSs3PutBucketTaggingResponse,
    AWSs3PutBucketVersioningResponse,
    AWSs3PutObjectTaggingResponse,
    AWSs3TransferAllowedDownloadArgs,
    AWSs3TransferAllowedUploadArgs,
    AWSs3TransferConfigOptions,
    AWSs3UploadPartCopyRequest,
    AWSs3UploadPartCopyResponse,
    AWSs3UploadPartRequest,
    AWSs3UploadPartResponse,
)
from werkflow_aws.types import s3Client
from .base import AWSBaseService
from werkflow_aws.models.s3 import (
    AWSS3CreateBucketMetadataConfigurationRequest,
    AWSS3CreateBucketMetadataConfigurationResponse,
    AWSS3CreateBucketMetadataTableConfigurationRequest,
    AWSS3CreateBucketMetadataTableConfigurationResponse,
    AWSS3CreateSessionRequest,
    AWSS3CreateSessionResponse,
    AWSS3DeleteBucketAnalyticsConfigurationRequest,
    AWSS3DeleteBucketAnalyticsConfigurationResponse,
    AWSS3DeleteBucketIntelligentTieringConfigurationRequest,
    AWSS3DeleteBucketIntelligentTieringConfigurationResponse,
    AWSS3DeleteBucketInventoryConfigurationRequest,
    AWSS3DeleteBucketInventoryConfigurationResponse,
    AWSS3DeleteBucketMetadataConfigurationRequest,
    AWSS3DeleteBucketMetadataConfigurationResponse,
    AWSS3DeleteBucketMetadataTableConfigurationRequest,
    AWSS3DeleteBucketMetadataTableConfigurationResponse,
    AWSS3DeleteBucketMetricsConfigurationRequest,
    AWSS3DeleteBucketMetricsConfigurationResponse,
    AWSS3DeleteBucketReplicationRequest,
    AWSS3DeleteBucketReplicationResponse,
    AWSS3DeleteObjectAnnotationRequest,
    AWSS3DeleteObjectAnnotationResponse,
    AWSS3GetBucketAbacRequest,
    AWSS3GetBucketAbacResponse,
    AWSS3GetBucketAnalyticsConfigurationRequest,
    AWSS3GetBucketAnalyticsConfigurationResponse,
    AWSS3GetBucketIntelligentTieringConfigurationRequest,
    AWSS3GetBucketIntelligentTieringConfigurationResponse,
    AWSS3GetBucketInventoryConfigurationRequest,
    AWSS3GetBucketInventoryConfigurationResponse,
    AWSS3GetBucketLifecycleRequest,
    AWSS3GetBucketLifecycleResponse,
    AWSS3GetBucketMetadataConfigurationRequest,
    AWSS3GetBucketMetadataConfigurationResponse,
    AWSS3GetBucketMetadataTableConfigurationRequest,
    AWSS3GetBucketMetadataTableConfigurationResponse,
    AWSS3GetBucketMetricsConfigurationRequest,
    AWSS3GetBucketMetricsConfigurationResponse,
    AWSS3GetBucketNotificationRequest,
    AWSS3GetBucketNotificationResponse,
    AWSS3GetBucketReplicationRequest,
    AWSS3GetBucketReplicationResponse,
    AWSS3GetObjectAnnotationRequest,
    AWSS3GetObjectAnnotationResponse,
    AWSS3GetObjectTorrentRequest,
    AWSS3GetObjectTorrentResponse,
    AWSS3ListBucketAnalyticsConfigurationsRequest,
    AWSS3ListBucketAnalyticsConfigurationsResponse,
    AWSS3ListBucketIntelligentTieringConfigurationsRequest,
    AWSS3ListBucketIntelligentTieringConfigurationsResponse,
    AWSS3ListBucketInventoryConfigurationsRequest,
    AWSS3ListBucketInventoryConfigurationsResponse,
    AWSS3ListBucketMetricsConfigurationsRequest,
    AWSS3ListBucketMetricsConfigurationsResponse,
    AWSS3ListObjectAnnotationsRequest,
    AWSS3ListObjectAnnotationsResponse,
    AWSS3ListObjectsRequestModel,
    AWSS3ListObjectsResponseModel,
    AWSS3PutBucketAbacRequest,
    AWSS3PutBucketAbacResponse,
    AWSS3PutBucketAnalyticsConfigurationRequest,
    AWSS3PutBucketAnalyticsConfigurationResponse,
    AWSS3PutBucketIntelligentTieringConfigurationRequest,
    AWSS3PutBucketIntelligentTieringConfigurationResponse,
    AWSS3PutBucketInventoryConfigurationRequest,
    AWSS3PutBucketInventoryConfigurationResponse,
    AWSS3PutBucketLifecycleRequest,
    AWSS3PutBucketLifecycleResponse,
    AWSS3PutBucketMetricsConfigurationRequest,
    AWSS3PutBucketMetricsConfigurationResponse,
    AWSS3PutBucketNotificationRequest,
    AWSS3PutBucketNotificationResponse,
    AWSS3PutBucketReplicationRequest,
    AWSS3PutBucketReplicationResponse,
    AWSS3PutObjectAnnotationRequest,
    AWSS3PutObjectAnnotationResponse,
    AWSS3RenameObjectRequest,
    AWSS3RenameObjectResponse,
    AWSS3SelectObjectContentRequest,
    AWSS3SelectObjectContentResponse,
    AWSS3UpdateBucketMetadataAnnotationTableConfigurationRequest,
    AWSS3UpdateBucketMetadataAnnotationTableConfigurationResponse,
    AWSS3UpdateBucketMetadataInventoryTableConfigurationRequest,
    AWSS3UpdateBucketMetadataInventoryTableConfigurationResponse,
    AWSS3UpdateBucketMetadataJournalTableConfigurationRequest,
    AWSS3UpdateBucketMetadataJournalTableConfigurationResponse,
    AWSS3UpdateObjectEncryptionRequest,
    AWSS3UpdateObjectEncryptionResponse,
    AWSS3WriteGetObjectResponseRequest,
    AWSS3WriteGetObjectResponseResponse,
)


class AWSs3(AWSBaseService[s3Client]):
    service_name = 's3'
    boto3_service_name = 's3'

    def __init__(self) -> None:
        super().__init__(service_name='s3', boto3_service_name='s3')

    async def get_object(
        self,
        request: AWSS3GetObjectRequest,
    ) -> AWSS3GetObjectResponse:
        client = self._require_client()
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True)

        response = await loop.run_in_executor(
            self._executor,
            functools.partial(client.get_object, **dumped),
        )
        response_data: dict[str, Any] = dict(response)
        if response_data.get('Body') is not None:
            response_data['Body'] = AWSS3StreamingBody(response_data['Body'])
        return AWSS3GetObjectResponse(**response_data)

    async def list_buckets(
        self,
        request: AWSS3ListBucketsRequest | None = None,
    ) -> AWSs3ListBucketsResponse:
        client = self._require_client()
        return await self._execute(client.list_buckets, request, AWSs3ListBucketsResponse)

    async def list_buckets_paginated(
        self,
        request: AWSS3ListBucketsRequest | None = None,
    ) -> list[AWSs3ListBucketsResponse]:
        return await self._paginate('list_buckets', request, AWSs3ListBucketsResponse)

    async def list_directory_buckets(
        self,
        request: AWSS3ListDirectoryBucketsRequest | None = None,
    ) -> AWSs3ListDirectoryBucketsResponse:
        client = self._require_client()
        return await self._execute(client.list_directory_buckets, request, AWSs3ListDirectoryBucketsResponse)

    async def list_directory_buckets_paginated(
        self,
        request: AWSS3ListDirectoryBucketsRequest | None = None,
    ) -> list[AWSs3ListDirectoryBucketsResponse]:
        return await self._paginate('list_directory_buckets', request, AWSs3ListDirectoryBucketsResponse)

    async def create_bucket(
        self,
        request: AWSS3CreateBucketRequest,
    ) -> AWSS3CreateBucketResponse:
        client = self._require_client()
        return await self._execute(client.create_bucket, request, AWSS3CreateBucketResponse)

    async def head_bucket(
        self,
        request: AWSS3HeadBucketRequest,
    ) -> AWSS3HeadBucketResponse:
        client = self._require_client()
        return await self._execute(client.head_bucket, request, AWSS3HeadBucketResponse)

    async def delete_bucket(
        self,
        request: AWSS3DeleteBucketRequest,
    ) -> AWSS3DeleteBucketResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket, request, AWSS3DeleteBucketResponse)

    async def get_bucket_versioning(
        self,
        request: AWSS3GetBucketVersioningRequest,
    ) -> AWSS3GetBucketVersioningResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_versioning, request, AWSS3GetBucketVersioningResponse)

    async def put_bucket_versioning(
        self,
        request: AWSS3PutBucketVersioningRequest,
    ) -> AWSs3PutBucketVersioningResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_versioning, request, AWSs3PutBucketVersioningResponse)

    async def get_bucket_tagging(
        self,
        request: AWSS3GetBucketTaggingRequest,
    ) -> AWSs3GetBucketTaggingResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_tagging, request, AWSs3GetBucketTaggingResponse)

    async def put_bucket_tagging(
        self,
        request: AWSS3PutBucketTaggingRequest,
    ) -> AWSs3PutBucketTaggingResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_tagging, request, AWSs3PutBucketTaggingResponse)

    async def delete_bucket_tagging(
        self,
        request: AWSS3DeleteBucketTaggingRequest,
    ) -> AWSs3DeleteBucketTaggingResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_tagging, request, AWSs3DeleteBucketTaggingResponse)

    async def list_objects(
        self,
        request: AWSS3ListObjectsRequest,
    ) -> AWSS3ListObjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_objects_v2, request, AWSS3ListObjectsResponse)

    async def list_objects_paginated(
        self,
        request: AWSS3ListObjectsRequest,
    ) -> list[AWSS3ListObjectsResponse]:
        return await self._paginate('list_objects_v2', request, AWSS3ListObjectsResponse)

    async def list_object_versions(
        self,
        request: AWSS3ListObjectVersionsRequest,
    ) -> AWSs3ListObjectVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_object_versions, request, AWSs3ListObjectVersionsResponse)

    async def list_object_versions_paginated(
        self,
        request: AWSS3ListObjectVersionsRequest,
    ) -> list[AWSs3ListObjectVersionsResponse]:
        return await self._paginate('list_object_versions', request, AWSs3ListObjectVersionsResponse)

    async def head_object(
        self,
        request: AWSS3HeadObjectRequest,
    ) -> AWSS3HeadObjectResponse:
        client = self._require_client()
        return await self._execute(client.head_object, request, AWSS3HeadObjectResponse)

    async def put_object(
        self,
        request: AWSS3PutObjectRequest,
    ) -> AWSS3PutObjectResponse:
        client = self._require_client()
        return await self._execute(client.put_object, request, AWSS3PutObjectResponse)

    async def copy_object(
        self,
        request: AWSS3CopyObjectRequest,
    ) -> AWSs3CopyObjectResponse:
        client = self._require_client()
        return await self._execute(client.copy_object, request, AWSs3CopyObjectResponse)

    async def delete_object(
        self,
        request: AWSS3DeleteObjectRequest,
    ) -> AWSS3DeleteObjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_object, request, AWSS3DeleteObjectResponse)

    async def delete_objects(
        self,
        request: AWSS3DeleteObjectsRequest,
    ) -> AWSs3DeleteObjectsResponse:
        client = self._require_client()
        return await self._execute(client.delete_objects, request, AWSs3DeleteObjectsResponse)

    async def get_object_tagging(
        self,
        request: AWSS3GetObjectTaggingRequest,
    ) -> AWSs3GetObjectTaggingResponse:
        client = self._require_client()
        return await self._execute(client.get_object_tagging, request, AWSs3GetObjectTaggingResponse)

    async def put_object_tagging(
        self,
        request: AWSS3PutObjectTaggingRequest,
    ) -> AWSs3PutObjectTaggingResponse:
        client = self._require_client()
        return await self._execute(client.put_object_tagging, request, AWSs3PutObjectTaggingResponse)

    async def delete_object_tagging(
        self,
        request: AWSS3DeleteObjectTaggingRequest,
    ) -> AWSs3DeleteObjectTaggingResponse:
        client = self._require_client()
        return await self._execute(client.delete_object_tagging, request, AWSs3DeleteObjectTaggingResponse)

    async def create_multipart_upload(
        self,
        request: AWSs3CreateMultipartUploadRequest,
    ) -> AWSs3CreateMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.create_multipart_upload, request, AWSs3CreateMultipartUploadResponse)

    async def upload_part(
        self,
        request: AWSs3UploadPartRequest,
    ) -> AWSs3UploadPartResponse:
        client = self._require_client()
        return await self._execute(client.upload_part, request, AWSs3UploadPartResponse)

    async def upload_part_copy(
        self,
        request: AWSs3UploadPartCopyRequest,
    ) -> AWSs3UploadPartCopyResponse:
        client = self._require_client()
        return await self._execute(client.upload_part_copy, request, AWSs3UploadPartCopyResponse)

    async def complete_multipart_upload(
        self,
        request: AWSs3CompleteMultipartUploadRequest,
    ) -> AWSs3CompleteMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_multipart_upload, request, AWSs3CompleteMultipartUploadResponse)

    async def abort_multipart_upload(
        self,
        request: AWSs3AbortMultipartUploadRequest,
    ) -> AWSs3AbortMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.abort_multipart_upload, request, AWSs3AbortMultipartUploadResponse)

    async def list_multipart_uploads(
        self,
        request: AWSs3ListMultipartUploadsRequest,
    ) -> AWSs3ListMultipartUploadsResponse:
        client = self._require_client()
        return await self._execute(client.list_multipart_uploads, request, AWSs3ListMultipartUploadsResponse)

    async def list_multipart_uploads_paginated(
        self,
        request: AWSs3ListMultipartUploadsRequest,
    ) -> list[AWSs3ListMultipartUploadsResponse]:
        return await self._paginate('list_multipart_uploads', request, AWSs3ListMultipartUploadsResponse)

    async def list_parts(
        self,
        request: AWSs3ListPartsRequest,
    ) -> AWSs3ListPartsResponse:
        client = self._require_client()
        return await self._execute(client.list_parts, request, AWSs3ListPartsResponse)

    async def list_parts_paginated(
        self,
        request: AWSs3ListPartsRequest,
    ) -> list[AWSs3ListPartsResponse]:
        return await self._paginate('list_parts', request, AWSs3ListPartsResponse)

    async def get_bucket_location(
        self,
        request: AWSS3GetBucketLocationRequest,
    ) -> AWSS3GetBucketLocationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_location, request, AWSS3GetBucketLocationResponse)

    async def get_bucket_policy(
        self,
        request: AWSS3GetBucketPolicyRequest,
    ) -> AWSS3GetBucketPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_policy, request, AWSS3GetBucketPolicyResponse)

    async def put_bucket_policy(
        self,
        request: AWSS3PutBucketPolicyRequest,
    ) -> AWSS3PutBucketPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_policy, request, AWSS3PutBucketPolicyResponse)

    async def delete_bucket_policy(
        self,
        request: AWSS3DeleteBucketPolicyRequest,
    ) -> AWSS3DeleteBucketPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_policy, request, AWSS3DeleteBucketPolicyResponse)

    async def get_bucket_policy_status(
        self,
        request: AWSS3GetBucketPolicyStatusRequest,
    ) -> AWSS3GetBucketPolicyStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_policy_status, request, AWSS3GetBucketPolicyStatusResponse)

    async def get_bucket_encryption(
        self,
        request: AWSS3GetBucketEncryptionRequest,
    ) -> AWSS3GetBucketEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_encryption, request, AWSS3GetBucketEncryptionResponse)

    async def put_bucket_encryption(
        self,
        request: AWSS3PutBucketEncryptionRequest,
    ) -> AWSS3PutBucketEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_encryption, request, AWSS3PutBucketEncryptionResponse)

    async def delete_bucket_encryption(
        self,
        request: AWSS3DeleteBucketEncryptionRequest,
    ) -> AWSS3DeleteBucketEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_encryption, request, AWSS3DeleteBucketEncryptionResponse)

    async def get_public_access_block(
        self,
        request: AWSS3GetPublicAccessBlockRequest,
    ) -> AWSS3GetPublicAccessBlockResponse:
        client = self._require_client()
        return await self._execute(client.get_public_access_block, request, AWSS3GetPublicAccessBlockResponse)

    async def put_public_access_block(
        self,
        request: AWSS3PutPublicAccessBlockRequest,
    ) -> AWSS3PutPublicAccessBlockResponse:
        client = self._require_client()
        return await self._execute(client.put_public_access_block, request, AWSS3PutPublicAccessBlockResponse)

    async def delete_public_access_block(
        self,
        request: AWSS3DeletePublicAccessBlockRequest,
    ) -> AWSS3DeletePublicAccessBlockResponse:
        client = self._require_client()
        return await self._execute(client.delete_public_access_block, request, AWSS3DeletePublicAccessBlockResponse)

    async def get_bucket_lifecycle_configuration(
        self,
        request: AWSS3GetBucketLifecycleConfigurationRequest,
    ) -> AWSS3GetBucketLifecycleConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_lifecycle_configuration, request, AWSS3GetBucketLifecycleConfigurationResponse)

    async def put_bucket_lifecycle_configuration(
        self,
        request: AWSS3PutBucketLifecycleConfigurationRequest,
    ) -> AWSS3PutBucketLifecycleConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_lifecycle_configuration, request, AWSS3PutBucketLifecycleConfigurationResponse)

    async def delete_bucket_lifecycle(
        self,
        request: AWSS3DeleteBucketLifecycleRequest,
    ) -> AWSS3DeleteBucketLifecycleResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_lifecycle, request, AWSS3DeleteBucketLifecycleResponse)

    async def get_bucket_cors(
        self,
        request: AWSS3GetBucketCorsRequest,
    ) -> AWSS3GetBucketCorsResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_cors, request, AWSS3GetBucketCorsResponse)

    async def put_bucket_cors(
        self,
        request: AWSS3PutBucketCorsRequest,
    ) -> AWSS3PutBucketCorsResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_cors, request, AWSS3PutBucketCorsResponse)

    async def delete_bucket_cors(
        self,
        request: AWSS3DeleteBucketCorsRequest,
    ) -> AWSS3DeleteBucketCorsResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_cors, request, AWSS3DeleteBucketCorsResponse)

    async def get_bucket_ownership_controls(
        self,
        request: AWSS3GetBucketOwnershipControlsRequest,
    ) -> AWSS3GetBucketOwnershipControlsResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_ownership_controls, request, AWSS3GetBucketOwnershipControlsResponse)

    async def put_bucket_ownership_controls(
        self,
        request: AWSS3PutBucketOwnershipControlsRequest,
    ) -> AWSS3PutBucketOwnershipControlsResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_ownership_controls, request, AWSS3PutBucketOwnershipControlsResponse)

    async def delete_bucket_ownership_controls(
        self,
        request: AWSS3DeleteBucketOwnershipControlsRequest,
    ) -> AWSS3DeleteBucketOwnershipControlsResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_ownership_controls, request, AWSS3DeleteBucketOwnershipControlsResponse)

    async def get_bucket_acl(
        self,
        request: AWSS3GetBucketAclRequest,
    ) -> AWSS3GetBucketAclResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_acl, request, AWSS3GetBucketAclResponse)

    async def put_bucket_acl(
        self,
        request: AWSS3PutBucketAclRequest,
    ) -> AWSS3PutBucketAclResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_acl, request, AWSS3PutBucketAclResponse)

    async def get_bucket_logging(
        self,
        request: AWSS3GetBucketLoggingRequest,
    ) -> AWSS3GetBucketLoggingResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_logging, request, AWSS3GetBucketLoggingResponse)

    async def put_bucket_logging(
        self,
        request: AWSS3PutBucketLoggingRequest,
    ) -> AWSS3PutBucketLoggingResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_logging, request, AWSS3PutBucketLoggingResponse)

    async def get_bucket_notification_configuration(
        self,
        request: AWSS3GetBucketNotificationConfigurationRequest,
    ) -> AWSS3GetBucketNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_notification_configuration, request, AWSS3GetBucketNotificationConfigurationResponse)

    async def put_bucket_notification_configuration(
        self,
        request: AWSS3PutBucketNotificationConfigurationRequest,
    ) -> AWSS3PutBucketNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_notification_configuration, request, AWSS3PutBucketNotificationConfigurationResponse)

    async def get_bucket_accelerate_configuration(
        self,
        request: AWSS3GetBucketAccelerateConfigurationRequest,
    ) -> AWSS3GetBucketAccelerateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_accelerate_configuration, request, AWSS3GetBucketAccelerateConfigurationResponse)

    async def put_bucket_accelerate_configuration(
        self,
        request: AWSS3PutBucketAccelerateConfigurationRequest,
    ) -> AWSS3PutBucketAccelerateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_accelerate_configuration, request, AWSS3PutBucketAccelerateConfigurationResponse)

    async def get_bucket_website(
        self,
        request: AWSS3GetBucketWebsiteRequest,
    ) -> AWSS3GetBucketWebsiteResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_website, request, AWSS3GetBucketWebsiteResponse)

    async def put_bucket_website(
        self,
        request: AWSS3PutBucketWebsiteRequest,
    ) -> AWSS3PutBucketWebsiteResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_website, request, AWSS3PutBucketWebsiteResponse)

    async def delete_bucket_website(
        self,
        request: AWSS3DeleteBucketWebsiteRequest,
    ) -> AWSS3DeleteBucketWebsiteResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_website, request, AWSS3DeleteBucketWebsiteResponse)

    async def get_bucket_request_payment(
        self,
        request: AWSS3GetBucketRequestPaymentRequest,
    ) -> AWSS3GetBucketRequestPaymentResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_request_payment, request, AWSS3GetBucketRequestPaymentResponse)

    async def put_bucket_request_payment(
        self,
        request: AWSS3PutBucketRequestPaymentRequest,
    ) -> AWSS3PutBucketRequestPaymentResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_request_payment, request, AWSS3PutBucketRequestPaymentResponse)

    async def get_object_acl(
        self,
        request: AWSS3GetObjectAclRequest,
    ) -> AWSS3GetObjectAclResponse:
        client = self._require_client()
        return await self._execute(client.get_object_acl, request, AWSS3GetObjectAclResponse)

    async def put_object_acl(
        self,
        request: AWSS3PutObjectAclRequest,
    ) -> AWSS3PutObjectAclResponse:
        client = self._require_client()
        return await self._execute(client.put_object_acl, request, AWSS3PutObjectAclResponse)

    async def get_object_attributes(
        self,
        request: AWSS3GetObjectAttributesRequest,
    ) -> AWSS3GetObjectAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_object_attributes, request, AWSS3GetObjectAttributesResponse)

    async def get_object_legal_hold(
        self,
        request: AWSS3GetObjectLegalHoldRequest,
    ) -> AWSS3GetObjectLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.get_object_legal_hold, request, AWSS3GetObjectLegalHoldResponse)

    async def put_object_legal_hold(
        self,
        request: AWSS3PutObjectLegalHoldRequest,
    ) -> AWSS3PutObjectLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.put_object_legal_hold, request, AWSS3PutObjectLegalHoldResponse)

    async def get_object_retention(
        self,
        request: AWSS3GetObjectRetentionRequest,
    ) -> AWSS3GetObjectRetentionResponse:
        client = self._require_client()
        return await self._execute(client.get_object_retention, request, AWSS3GetObjectRetentionResponse)

    async def put_object_retention(
        self,
        request: AWSS3PutObjectRetentionRequest,
    ) -> AWSS3PutObjectRetentionResponse:
        client = self._require_client()
        return await self._execute(client.put_object_retention, request, AWSS3PutObjectRetentionResponse)

    async def get_object_lock_configuration(
        self,
        request: AWSS3GetObjectLockConfigurationRequest,
    ) -> AWSS3GetObjectLockConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_object_lock_configuration, request, AWSS3GetObjectLockConfigurationResponse)

    async def put_object_lock_configuration(
        self,
        request: AWSS3PutObjectLockConfigurationRequest,
    ) -> AWSS3PutObjectLockConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_object_lock_configuration, request, AWSS3PutObjectLockConfigurationResponse)

    async def restore_object(
        self,
        request: AWSS3RestoreObjectRequest,
    ) -> AWSS3RestoreObjectResponse:
        client = self._require_client()
        return await self._execute(client.restore_object, request, AWSS3RestoreObjectResponse)

    async def generate_presigned_url(
        self,
        request: AWSS3GeneratePresignedURLRequest,
    ) -> AWSs3GeneratePresignedURLResponse:
        client = self._require_client()
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True)
        client_method = dumped.pop('ClientMethod')

        presigned_url = await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.generate_presigned_url,
                client_method,
                **dumped,
            ),
        )
        return AWSs3GeneratePresignedURLResponse(URL=AnyHttpUrl(presigned_url))

    async def generate_presigned_post(
        self,
        request: AWSS3GeneratePresignedPostRequest,
    ) -> AWSs3GeneratePresignedPostResponse:
        client = self._require_client()
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True)

        presigned_post = await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.generate_presigned_post,
                **dumped,
            ),
        )
        return AWSs3GeneratePresignedPostResponse(**presigned_post)

    async def upload_file_object(
        self,
        file_object: BinaryIO,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs] = None,
        config: Optional[AWSs3TransferConfigOptions] = None,
    ) -> None:
        client = self._require_client()
        loop = self._get_loop()

        extra_args = options.to_data() if options is not None else None
        transfer_config = config.to_transfer_config() if config is not None else None

        try:
            await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.upload_fileobj,
                    file_object,
                    bucket,
                    key,
                    ExtraArgs=extra_args or None,
                    Config=transfer_config,
                ),
            )
        finally:
            await loop.run_in_executor(self._executor, file_object.close)

    async def upload_file(
        self,
        path: str,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedUploadArgs] = None,
        config: Optional[AWSs3TransferConfigOptions] = None,
    ) -> None:
        client = self._require_client()
        loop = self._get_loop()

        extra_args = options.to_data() if options is not None else None
        transfer_config = config.to_transfer_config() if config is not None else None

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.upload_file,
                path,
                bucket,
                key,
                ExtraArgs=extra_args or None,
                Config=transfer_config,
            ),
        )

    async def download_file_object(
        self,
        file_object: BinaryIO,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedDownloadArgs] = None,
        config: Optional[AWSs3TransferConfigOptions] = None,
    ) -> None:
        client = self._require_client()
        loop = self._get_loop()

        extra_args = options.to_data() if options is not None else None
        transfer_config = config.to_transfer_config() if config is not None else None

        try:
            await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.download_fileobj,
                    bucket,
                    key,
                    file_object,
                    ExtraArgs=extra_args or None,
                    Config=transfer_config,
                ),
            )
        finally:
            await loop.run_in_executor(self._executor, file_object.close)

    async def download_file(
        self,
        path: str,
        bucket: str,
        key: str,
        options: Optional[AWSs3TransferAllowedDownloadArgs] = None,
        config: Optional[AWSs3TransferConfigOptions] = None,
    ) -> None:
        client = self._require_client()
        loop = self._get_loop()

        extra_args = options.to_data() if options is not None else None
        transfer_config = config.to_transfer_config() if config is not None else None

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.download_file,
                bucket,
                key,
                path,
                ExtraArgs=extra_args or None,
                Config=transfer_config,
            ),
        )

    async def copy(
        self,
        copy_source: AWSs3CopySource,
        bucket: str,
        key: str,
        config: Optional[AWSs3TransferConfigOptions] = None,
        options: AWSs3TransferAllowedUploadArgs | None = None,
    ) -> None:
        client = self._require_client()
        loop = self._get_loop()

        extra_args = options.to_data() if options is not None else None
        transfer_config = config.to_transfer_config() if config is not None else None

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.copy,
                copy_source.to_data(),
                bucket,
                key,
                ExtraArgs=extra_args or None,
                Callback=None,
                SourceClient=None,
                Config=transfer_config,
            ),
        )

    async def create_bucket_metadata_configuration(
        self,
        request: AWSS3CreateBucketMetadataConfigurationRequest,
    ) -> AWSS3CreateBucketMetadataConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_bucket_metadata_configuration, request, AWSS3CreateBucketMetadataConfigurationResponse)

    async def create_bucket_metadata_table_configuration(
        self,
        request: AWSS3CreateBucketMetadataTableConfigurationRequest,
    ) -> AWSS3CreateBucketMetadataTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_bucket_metadata_table_configuration, request, AWSS3CreateBucketMetadataTableConfigurationResponse)

    async def create_session(
        self,
        request: AWSS3CreateSessionRequest,
    ) -> AWSS3CreateSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_session, request, AWSS3CreateSessionResponse)

    async def delete_bucket_analytics_configuration(
        self,
        request: AWSS3DeleteBucketAnalyticsConfigurationRequest,
    ) -> AWSS3DeleteBucketAnalyticsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_analytics_configuration, request, AWSS3DeleteBucketAnalyticsConfigurationResponse)

    async def delete_bucket_intelligent_tiering_configuration(
        self,
        request: AWSS3DeleteBucketIntelligentTieringConfigurationRequest,
    ) -> AWSS3DeleteBucketIntelligentTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_intelligent_tiering_configuration, request, AWSS3DeleteBucketIntelligentTieringConfigurationResponse)

    async def delete_bucket_inventory_configuration(
        self,
        request: AWSS3DeleteBucketInventoryConfigurationRequest,
    ) -> AWSS3DeleteBucketInventoryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_inventory_configuration, request, AWSS3DeleteBucketInventoryConfigurationResponse)

    async def delete_bucket_metadata_configuration(
        self,
        request: AWSS3DeleteBucketMetadataConfigurationRequest,
    ) -> AWSS3DeleteBucketMetadataConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_metadata_configuration, request, AWSS3DeleteBucketMetadataConfigurationResponse)

    async def delete_bucket_metadata_table_configuration(
        self,
        request: AWSS3DeleteBucketMetadataTableConfigurationRequest,
    ) -> AWSS3DeleteBucketMetadataTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_metadata_table_configuration, request, AWSS3DeleteBucketMetadataTableConfigurationResponse)

    async def delete_bucket_metrics_configuration(
        self,
        request: AWSS3DeleteBucketMetricsConfigurationRequest,
    ) -> AWSS3DeleteBucketMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_metrics_configuration, request, AWSS3DeleteBucketMetricsConfigurationResponse)

    async def delete_bucket_replication(
        self,
        request: AWSS3DeleteBucketReplicationRequest,
    ) -> AWSS3DeleteBucketReplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_replication, request, AWSS3DeleteBucketReplicationResponse)

    async def delete_object_annotation(
        self,
        request: AWSS3DeleteObjectAnnotationRequest,
    ) -> AWSS3DeleteObjectAnnotationResponse:
        client = self._require_client()
        return await self._execute(client.delete_object_annotation, request, AWSS3DeleteObjectAnnotationResponse)

    async def get_bucket_abac(
        self,
        request: AWSS3GetBucketAbacRequest,
    ) -> AWSS3GetBucketAbacResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_abac, request, AWSS3GetBucketAbacResponse)

    async def get_bucket_analytics_configuration(
        self,
        request: AWSS3GetBucketAnalyticsConfigurationRequest,
    ) -> AWSS3GetBucketAnalyticsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_analytics_configuration, request, AWSS3GetBucketAnalyticsConfigurationResponse)

    async def get_bucket_intelligent_tiering_configuration(
        self,
        request: AWSS3GetBucketIntelligentTieringConfigurationRequest,
    ) -> AWSS3GetBucketIntelligentTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_intelligent_tiering_configuration, request, AWSS3GetBucketIntelligentTieringConfigurationResponse)

    async def get_bucket_inventory_configuration(
        self,
        request: AWSS3GetBucketInventoryConfigurationRequest,
    ) -> AWSS3GetBucketInventoryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_inventory_configuration, request, AWSS3GetBucketInventoryConfigurationResponse)

    async def get_bucket_lifecycle(
        self,
        request: AWSS3GetBucketLifecycleRequest,
    ) -> AWSS3GetBucketLifecycleResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_lifecycle, request, AWSS3GetBucketLifecycleResponse)

    async def get_bucket_metadata_configuration(
        self,
        request: AWSS3GetBucketMetadataConfigurationRequest,
    ) -> AWSS3GetBucketMetadataConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_metadata_configuration, request, AWSS3GetBucketMetadataConfigurationResponse)

    async def get_bucket_metadata_table_configuration(
        self,
        request: AWSS3GetBucketMetadataTableConfigurationRequest,
    ) -> AWSS3GetBucketMetadataTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_metadata_table_configuration, request, AWSS3GetBucketMetadataTableConfigurationResponse)

    async def get_bucket_metrics_configuration(
        self,
        request: AWSS3GetBucketMetricsConfigurationRequest,
    ) -> AWSS3GetBucketMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_metrics_configuration, request, AWSS3GetBucketMetricsConfigurationResponse)

    async def get_bucket_notification(
        self,
        request: AWSS3GetBucketNotificationRequest,
    ) -> AWSS3GetBucketNotificationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_notification, request, AWSS3GetBucketNotificationResponse)

    async def get_bucket_replication(
        self,
        request: AWSS3GetBucketReplicationRequest,
    ) -> AWSS3GetBucketReplicationResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_replication, request, AWSS3GetBucketReplicationResponse)

    async def get_object_annotation(
        self,
        request: AWSS3GetObjectAnnotationRequest,
    ) -> AWSS3GetObjectAnnotationResponse:
        client = self._require_client()
        return await self._execute(client.get_object_annotation, request, AWSS3GetObjectAnnotationResponse)

    async def get_object_torrent(
        self,
        request: AWSS3GetObjectTorrentRequest,
    ) -> AWSS3GetObjectTorrentResponse:
        client = self._require_client()
        return await self._execute(client.get_object_torrent, request, AWSS3GetObjectTorrentResponse)

    async def list_bucket_analytics_configurations(
        self,
        request: AWSS3ListBucketAnalyticsConfigurationsRequest,
    ) -> AWSS3ListBucketAnalyticsConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bucket_analytics_configurations, request, AWSS3ListBucketAnalyticsConfigurationsResponse)

    async def list_bucket_intelligent_tiering_configurations(
        self,
        request: AWSS3ListBucketIntelligentTieringConfigurationsRequest,
    ) -> AWSS3ListBucketIntelligentTieringConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bucket_intelligent_tiering_configurations, request, AWSS3ListBucketIntelligentTieringConfigurationsResponse)

    async def list_bucket_inventory_configurations(
        self,
        request: AWSS3ListBucketInventoryConfigurationsRequest,
    ) -> AWSS3ListBucketInventoryConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bucket_inventory_configurations, request, AWSS3ListBucketInventoryConfigurationsResponse)

    async def list_bucket_metrics_configurations(
        self,
        request: AWSS3ListBucketMetricsConfigurationsRequest,
    ) -> AWSS3ListBucketMetricsConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bucket_metrics_configurations, request, AWSS3ListBucketMetricsConfigurationsResponse)

    async def list_object_annotations(
        self,
        request: AWSS3ListObjectAnnotationsRequest,
    ) -> AWSS3ListObjectAnnotationsResponse:
        client = self._require_client()
        return await self._execute(client.list_object_annotations, request, AWSS3ListObjectAnnotationsResponse)

    async def list_object_annotations_paginated(
        self,
        request: AWSS3ListObjectAnnotationsRequest,
    ) -> list[AWSS3ListObjectAnnotationsResponse]:
        return await self._paginate('list_object_annotations', request, AWSS3ListObjectAnnotationsResponse)

    async def list_objects_v1(
        self,
        request: AWSS3ListObjectsRequestModel,
    ) -> AWSS3ListObjectsResponseModel:
        client = self._require_client()
        return await self._execute(client.list_objects, request, AWSS3ListObjectsResponseModel)

    async def list_objects_v1_paginated(
        self,
        request: AWSS3ListObjectsRequestModel,
    ) -> list[AWSS3ListObjectsResponseModel]:
        return await self._paginate('list_objects', request, AWSS3ListObjectsResponseModel)

    async def list_objects_v2_paginated(
        self,
        request: AWSS3ListObjectsRequest,
    ) -> list[AWSS3ListObjectsResponse]:
        return await self._paginate('list_objects_v2', request, AWSS3ListObjectsResponse)

    async def put_bucket_abac(
        self,
        request: AWSS3PutBucketAbacRequest,
    ) -> AWSS3PutBucketAbacResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_abac, request, AWSS3PutBucketAbacResponse)

    async def put_bucket_analytics_configuration(
        self,
        request: AWSS3PutBucketAnalyticsConfigurationRequest,
    ) -> AWSS3PutBucketAnalyticsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_analytics_configuration, request, AWSS3PutBucketAnalyticsConfigurationResponse)

    async def put_bucket_intelligent_tiering_configuration(
        self,
        request: AWSS3PutBucketIntelligentTieringConfigurationRequest,
    ) -> AWSS3PutBucketIntelligentTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_intelligent_tiering_configuration, request, AWSS3PutBucketIntelligentTieringConfigurationResponse)

    async def put_bucket_inventory_configuration(
        self,
        request: AWSS3PutBucketInventoryConfigurationRequest,
    ) -> AWSS3PutBucketInventoryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_inventory_configuration, request, AWSS3PutBucketInventoryConfigurationResponse)

    async def put_bucket_lifecycle(
        self,
        request: AWSS3PutBucketLifecycleRequest,
    ) -> AWSS3PutBucketLifecycleResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_lifecycle, request, AWSS3PutBucketLifecycleResponse)

    async def put_bucket_metrics_configuration(
        self,
        request: AWSS3PutBucketMetricsConfigurationRequest,
    ) -> AWSS3PutBucketMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_metrics_configuration, request, AWSS3PutBucketMetricsConfigurationResponse)

    async def put_bucket_notification(
        self,
        request: AWSS3PutBucketNotificationRequest,
    ) -> AWSS3PutBucketNotificationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_notification, request, AWSS3PutBucketNotificationResponse)

    async def put_bucket_replication(
        self,
        request: AWSS3PutBucketReplicationRequest,
    ) -> AWSS3PutBucketReplicationResponse:
        client = self._require_client()
        return await self._execute(client.put_bucket_replication, request, AWSS3PutBucketReplicationResponse)

    async def put_object_annotation(
        self,
        request: AWSS3PutObjectAnnotationRequest,
    ) -> AWSS3PutObjectAnnotationResponse:
        client = self._require_client()
        return await self._execute(client.put_object_annotation, request, AWSS3PutObjectAnnotationResponse)

    async def rename_object(
        self,
        request: AWSS3RenameObjectRequest,
    ) -> AWSS3RenameObjectResponse:
        client = self._require_client()
        return await self._execute(client.rename_object, request, AWSS3RenameObjectResponse)

    async def select_object_content(
        self,
        request: AWSS3SelectObjectContentRequest,
    ) -> AWSS3SelectObjectContentResponse:
        client = self._require_client()
        return await self._execute(client.select_object_content, request, AWSS3SelectObjectContentResponse)

    async def update_bucket_metadata_annotation_table_configuration(
        self,
        request: AWSS3UpdateBucketMetadataAnnotationTableConfigurationRequest,
    ) -> AWSS3UpdateBucketMetadataAnnotationTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_bucket_metadata_annotation_table_configuration, request, AWSS3UpdateBucketMetadataAnnotationTableConfigurationResponse)

    async def update_bucket_metadata_inventory_table_configuration(
        self,
        request: AWSS3UpdateBucketMetadataInventoryTableConfigurationRequest,
    ) -> AWSS3UpdateBucketMetadataInventoryTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_bucket_metadata_inventory_table_configuration, request, AWSS3UpdateBucketMetadataInventoryTableConfigurationResponse)

    async def update_bucket_metadata_journal_table_configuration(
        self,
        request: AWSS3UpdateBucketMetadataJournalTableConfigurationRequest,
    ) -> AWSS3UpdateBucketMetadataJournalTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_bucket_metadata_journal_table_configuration, request, AWSS3UpdateBucketMetadataJournalTableConfigurationResponse)

    async def update_object_encryption(
        self,
        request: AWSS3UpdateObjectEncryptionRequest,
    ) -> AWSS3UpdateObjectEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.update_object_encryption, request, AWSS3UpdateObjectEncryptionResponse)

    async def write_get_object_response(
        self,
        request: AWSS3WriteGetObjectResponseRequest,
    ) -> AWSS3WriteGetObjectResponseResponse:
        client = self._require_client()
        return await self._execute(client.write_get_object_response, request, AWSS3WriteGetObjectResponseResponse)

