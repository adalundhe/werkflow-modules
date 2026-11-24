from werkflow_aws.models.glacier import (
    GlacierAbortMultipartUploadRequest,
    GlacierAbortMultipartUploadResponse,
    GlacierAbortVaultLockRequest,
    GlacierAbortVaultLockResponse,
    GlacierAddTagsToVaultRequest,
    GlacierAddTagsToVaultResponse,
    GlacierCompleteMultipartUploadRequest,
    GlacierCompleteMultipartUploadResponse,
    GlacierCompleteVaultLockRequest,
    GlacierCompleteVaultLockResponse,
    GlacierCreateVaultRequest,
    GlacierCreateVaultResponse,
    GlacierDeleteArchiveRequest,
    GlacierDeleteArchiveResponse,
    GlacierDeleteVaultAccessPolicyRequest,
    GlacierDeleteVaultAccessPolicyResponse,
    GlacierDeleteVaultNotificationsRequest,
    GlacierDeleteVaultNotificationsResponse,
    GlacierDeleteVaultRequest,
    GlacierDeleteVaultResponse,
    GlacierDescribeJobRequest,
    GlacierDescribeJobResponse,
    GlacierDescribeVaultRequest,
    GlacierDescribeVaultResponse,
    GlacierGetDataRetrievalPolicyRequest,
    GlacierGetDataRetrievalPolicyResponse,
    GlacierGetJobOutputRequest,
    GlacierGetJobOutputResponse,
    GlacierGetVaultAccessPolicyRequest,
    GlacierGetVaultAccessPolicyResponse,
    GlacierGetVaultLockRequest,
    GlacierGetVaultLockResponse,
    GlacierGetVaultNotificationsRequest,
    GlacierGetVaultNotificationsResponse,
    GlacierInitiateJobRequest,
    GlacierInitiateJobResponse,
    GlacierInitiateMultipartUploadRequest,
    GlacierInitiateMultipartUploadResponse,
    GlacierInitiateVaultLockRequest,
    GlacierInitiateVaultLockResponse,
    GlacierListJobsRequest,
    GlacierListJobsResponse,
    GlacierListMultipartUploadsRequest,
    GlacierListMultipartUploadsResponse,
    GlacierListPartsRequest,
    GlacierListPartsResponse,
    GlacierListProvisionedCapacityRequest,
    GlacierListProvisionedCapacityResponse,
    GlacierListTagsForVaultRequest,
    GlacierListTagsForVaultResponse,
    GlacierListVaultsRequest,
    GlacierListVaultsResponse,
    GlacierPurchaseProvisionedCapacityRequest,
    GlacierPurchaseProvisionedCapacityResponse,
    GlacierRemoveTagsFromVaultRequest,
    GlacierRemoveTagsFromVaultResponse,
    GlacierSetDataRetrievalPolicyRequest,
    GlacierSetDataRetrievalPolicyResponse,
    GlacierSetVaultAccessPolicyRequest,
    GlacierSetVaultAccessPolicyResponse,
    GlacierSetVaultNotificationsRequest,
    GlacierSetVaultNotificationsResponse,
    GlacierUploadArchiveRequest,
    GlacierUploadArchiveResponse,
    GlacierUploadMultipartPartRequest,
    GlacierUploadMultipartPartResponse,
)
from werkflow_aws.types.glacier_client import GlacierClient
from .base import AWSBaseService


class AWSGlacier(AWSBaseService[GlacierClient]):
    service_name = 'glacier'
    boto3_service_name = 'glacier'

    def __init__(self) -> None:
        super().__init__(service_name='glacier', boto3_service_name='glacier')

    async def abort_multipart_upload(
        self,
        request: GlacierAbortMultipartUploadRequest,
    ) -> GlacierAbortMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.abort_multipart_upload, request, GlacierAbortMultipartUploadResponse)

    async def abort_vault_lock(
        self,
        request: GlacierAbortVaultLockRequest,
    ) -> GlacierAbortVaultLockResponse:
        client = self._require_client()
        return await self._execute(client.abort_vault_lock, request, GlacierAbortVaultLockResponse)

    async def add_tags_to_vault(
        self,
        request: GlacierAddTagsToVaultRequest,
    ) -> GlacierAddTagsToVaultResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_vault, request, GlacierAddTagsToVaultResponse)

    async def complete_multipart_upload(
        self,
        request: GlacierCompleteMultipartUploadRequest,
    ) -> GlacierCompleteMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_multipart_upload, request, GlacierCompleteMultipartUploadResponse)

    async def complete_vault_lock(
        self,
        request: GlacierCompleteVaultLockRequest,
    ) -> GlacierCompleteVaultLockResponse:
        client = self._require_client()
        return await self._execute(client.complete_vault_lock, request, GlacierCompleteVaultLockResponse)

    async def create_vault(
        self,
        request: GlacierCreateVaultRequest,
    ) -> GlacierCreateVaultResponse:
        client = self._require_client()
        return await self._execute(client.create_vault, request, GlacierCreateVaultResponse)

    async def delete_archive(
        self,
        request: GlacierDeleteArchiveRequest,
    ) -> GlacierDeleteArchiveResponse:
        client = self._require_client()
        return await self._execute(client.delete_archive, request, GlacierDeleteArchiveResponse)

    async def delete_vault(
        self,
        request: GlacierDeleteVaultRequest,
    ) -> GlacierDeleteVaultResponse:
        client = self._require_client()
        return await self._execute(client.delete_vault, request, GlacierDeleteVaultResponse)

    async def delete_vault_access_policy(
        self,
        request: GlacierDeleteVaultAccessPolicyRequest,
    ) -> GlacierDeleteVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_vault_access_policy, request, GlacierDeleteVaultAccessPolicyResponse)

    async def delete_vault_notifications(
        self,
        request: GlacierDeleteVaultNotificationsRequest,
    ) -> GlacierDeleteVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_vault_notifications, request, GlacierDeleteVaultNotificationsResponse)

    async def describe_job(
        self,
        request: GlacierDescribeJobRequest,
    ) -> GlacierDescribeJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_job, request, GlacierDescribeJobResponse)

    async def describe_vault(
        self,
        request: GlacierDescribeVaultRequest,
    ) -> GlacierDescribeVaultResponse:
        client = self._require_client()
        return await self._execute(client.describe_vault, request, GlacierDescribeVaultResponse)

    async def get_data_retrieval_policy(
        self,
        request: GlacierGetDataRetrievalPolicyRequest,
    ) -> GlacierGetDataRetrievalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_data_retrieval_policy, request, GlacierGetDataRetrievalPolicyResponse)

    async def get_job_output(
        self,
        request: GlacierGetJobOutputRequest,
    ) -> GlacierGetJobOutputResponse:
        client = self._require_client()
        return await self._execute(client.get_job_output, request, GlacierGetJobOutputResponse)

    async def get_vault_access_policy(
        self,
        request: GlacierGetVaultAccessPolicyRequest,
    ) -> GlacierGetVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_vault_access_policy, request, GlacierGetVaultAccessPolicyResponse)

    async def get_vault_lock(
        self,
        request: GlacierGetVaultLockRequest,
    ) -> GlacierGetVaultLockResponse:
        client = self._require_client()
        return await self._execute(client.get_vault_lock, request, GlacierGetVaultLockResponse)

    async def get_vault_notifications(
        self,
        request: GlacierGetVaultNotificationsRequest,
    ) -> GlacierGetVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.get_vault_notifications, request, GlacierGetVaultNotificationsResponse)

    async def initiate_job(
        self,
        request: GlacierInitiateJobRequest,
    ) -> GlacierInitiateJobResponse:
        client = self._require_client()
        return await self._execute(client.initiate_job, request, GlacierInitiateJobResponse)

    async def initiate_multipart_upload(
        self,
        request: GlacierInitiateMultipartUploadRequest,
    ) -> GlacierInitiateMultipartUploadResponse:
        client = self._require_client()
        return await self._execute(client.initiate_multipart_upload, request, GlacierInitiateMultipartUploadResponse)

    async def initiate_vault_lock(
        self,
        request: GlacierInitiateVaultLockRequest,
    ) -> GlacierInitiateVaultLockResponse:
        client = self._require_client()
        return await self._execute(client.initiate_vault_lock, request, GlacierInitiateVaultLockResponse)

    async def list_jobs(
        self,
        request: GlacierListJobsRequest,
    ) -> GlacierListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, GlacierListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: GlacierListJobsRequest,
    ) -> list[GlacierListJobsResponse]:
        return await self._paginate('list_jobs', request, GlacierListJobsResponse)

    async def list_multipart_uploads(
        self,
        request: GlacierListMultipartUploadsRequest,
    ) -> GlacierListMultipartUploadsResponse:
        client = self._require_client()
        return await self._execute(client.list_multipart_uploads, request, GlacierListMultipartUploadsResponse)

    async def list_multipart_uploads_paginated(
        self,
        request: GlacierListMultipartUploadsRequest,
    ) -> list[GlacierListMultipartUploadsResponse]:
        return await self._paginate('list_multipart_uploads', request, GlacierListMultipartUploadsResponse)

    async def list_parts(
        self,
        request: GlacierListPartsRequest,
    ) -> GlacierListPartsResponse:
        client = self._require_client()
        return await self._execute(client.list_parts, request, GlacierListPartsResponse)

    async def list_parts_paginated(
        self,
        request: GlacierListPartsRequest,
    ) -> list[GlacierListPartsResponse]:
        return await self._paginate('list_parts', request, GlacierListPartsResponse)

    async def list_provisioned_capacity(
        self,
        request: GlacierListProvisionedCapacityRequest,
    ) -> GlacierListProvisionedCapacityResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioned_capacity, request, GlacierListProvisionedCapacityResponse)

    async def list_tags_for_vault(
        self,
        request: GlacierListTagsForVaultRequest,
    ) -> GlacierListTagsForVaultResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_vault, request, GlacierListTagsForVaultResponse)

    async def list_vaults(
        self,
        request: GlacierListVaultsRequest,
    ) -> GlacierListVaultsResponse:
        client = self._require_client()
        return await self._execute(client.list_vaults, request, GlacierListVaultsResponse)

    async def list_vaults_paginated(
        self,
        request: GlacierListVaultsRequest,
    ) -> list[GlacierListVaultsResponse]:
        return await self._paginate('list_vaults', request, GlacierListVaultsResponse)

    async def purchase_provisioned_capacity(
        self,
        request: GlacierPurchaseProvisionedCapacityRequest,
    ) -> GlacierPurchaseProvisionedCapacityResponse:
        client = self._require_client()
        return await self._execute(client.purchase_provisioned_capacity, request, GlacierPurchaseProvisionedCapacityResponse)

    async def remove_tags_from_vault(
        self,
        request: GlacierRemoveTagsFromVaultRequest,
    ) -> GlacierRemoveTagsFromVaultResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_vault, request, GlacierRemoveTagsFromVaultResponse)

    async def set_data_retrieval_policy(
        self,
        request: GlacierSetDataRetrievalPolicyRequest,
    ) -> GlacierSetDataRetrievalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.set_data_retrieval_policy, request, GlacierSetDataRetrievalPolicyResponse)

    async def set_vault_access_policy(
        self,
        request: GlacierSetVaultAccessPolicyRequest,
    ) -> GlacierSetVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.set_vault_access_policy, request, GlacierSetVaultAccessPolicyResponse)

    async def set_vault_notifications(
        self,
        request: GlacierSetVaultNotificationsRequest,
    ) -> GlacierSetVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.set_vault_notifications, request, GlacierSetVaultNotificationsResponse)

    async def upload_archive(
        self,
        request: GlacierUploadArchiveRequest,
    ) -> GlacierUploadArchiveResponse:
        client = self._require_client()
        return await self._execute(client.upload_archive, request, GlacierUploadArchiveResponse)

    async def upload_multipart_part(
        self,
        request: GlacierUploadMultipartPartRequest,
    ) -> GlacierUploadMultipartPartResponse:
        client = self._require_client()
        return await self._execute(client.upload_multipart_part, request, GlacierUploadMultipartPartResponse)
