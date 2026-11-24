from werkflow_aws.models.ecr import (
    ECRBatchCheckLayerAvailabilityRequest,
    ECRBatchCheckLayerAvailabilityResponse,
    ECRBatchDeleteImageRequest,
    ECRBatchDeleteImageResponse,
    ECRBatchGetImageRequest,
    ECRBatchGetImageResponse,
    ECRBatchGetRepositoryScanningConfigurationRequest,
    ECRBatchGetRepositoryScanningConfigurationResponse,
    ECRCompleteLayerUploadRequest,
    ECRCompleteLayerUploadResponse,
    ECRCreatePullThroughCacheRuleRequest,
    ECRCreatePullThroughCacheRuleResponse,
    ECRCreateRepositoryCreationTemplateRequest,
    ECRCreateRepositoryCreationTemplateResponse,
    ECRCreateRepositoryRequest,
    ECRCreateRepositoryResponse,
    ECRDeleteLifecyclePolicyRequest,
    ECRDeleteLifecyclePolicyResponse,
    ECRDeletePullThroughCacheRuleRequest,
    ECRDeletePullThroughCacheRuleResponse,
    ECRDeleteRegistryPolicyRequest,
    ECRDeleteRegistryPolicyResponse,
    ECRDeleteRepositoryCreationTemplateRequest,
    ECRDeleteRepositoryCreationTemplateResponse,
    ECRDeleteRepositoryPolicyRequest,
    ECRDeleteRepositoryPolicyResponse,
    ECRDeleteRepositoryRequest,
    ECRDeleteRepositoryResponse,
    ECRDeleteSigningConfigurationRequest,
    ECRDeleteSigningConfigurationResponse,
    ECRDeregisterPullTimeUpdateExclusionRequest,
    ECRDeregisterPullTimeUpdateExclusionResponse,
    ECRDescribeImageReplicationStatusRequest,
    ECRDescribeImageReplicationStatusResponse,
    ECRDescribeImageScanFindingsRequest,
    ECRDescribeImageScanFindingsResponse,
    ECRDescribeImageSigningStatusRequest,
    ECRDescribeImageSigningStatusResponse,
    ECRDescribeImagesRequest,
    ECRDescribeImagesResponse,
    ECRDescribePullThroughCacheRulesRequest,
    ECRDescribePullThroughCacheRulesResponse,
    ECRDescribeRegistryRequest,
    ECRDescribeRegistryResponse,
    ECRDescribeReplicationBackfillResultsRequest,
    ECRDescribeReplicationBackfillResultsResponse,
    ECRDescribeRepositoriesRequest,
    ECRDescribeRepositoriesResponse,
    ECRDescribeRepositoryCreationTemplatesRequest,
    ECRDescribeRepositoryCreationTemplatesResponse,
    ECRGetAccountSettingRequest,
    ECRGetAccountSettingResponse,
    ECRGetAuthorizationTokenRequest,
    ECRGetAuthorizationTokenResponse,
    ECRGetDownloadUrlForLayerRequest,
    ECRGetDownloadUrlForLayerResponse,
    ECRGetLifecyclePolicyPreviewRequest,
    ECRGetLifecyclePolicyPreviewResponse,
    ECRGetLifecyclePolicyRequest,
    ECRGetLifecyclePolicyResponse,
    ECRGetRegistryPolicyRequest,
    ECRGetRegistryPolicyResponse,
    ECRGetRegistryScanningConfigurationRequest,
    ECRGetRegistryScanningConfigurationResponse,
    ECRGetRepositoryPolicyRequest,
    ECRGetRepositoryPolicyResponse,
    ECRGetSigningConfigurationRequest,
    ECRGetSigningConfigurationResponse,
    ECRInitiateLayerUploadRequest,
    ECRInitiateLayerUploadResponse,
    ECRListImageReferrersRequest,
    ECRListImageReferrersResponse,
    ECRListImagesRequest,
    ECRListImagesResponse,
    ECRListPullTimeUpdateExclusionsRequest,
    ECRListPullTimeUpdateExclusionsResponse,
    ECRListReplicationBackfillsRequest,
    ECRListReplicationBackfillsResponse,
    ECRListTagsForResourceRequest,
    ECRListTagsForResourceResponse,
    ECRPutAccountSettingRequest,
    ECRPutAccountSettingResponse,
    ECRPutImageRequest,
    ECRPutImageResponse,
    ECRPutImageScanningConfigurationRequest,
    ECRPutImageScanningConfigurationResponse,
    ECRPutImageTagMutabilityRequest,
    ECRPutImageTagMutabilityResponse,
    ECRPutLifecyclePolicyRequest,
    ECRPutLifecyclePolicyResponse,
    ECRPutRegistryPolicyRequest,
    ECRPutRegistryPolicyResponse,
    ECRPutRegistryScanningConfigurationRequest,
    ECRPutRegistryScanningConfigurationResponse,
    ECRPutReplicationConfigurationRequest,
    ECRPutReplicationConfigurationResponse,
    ECRPutSigningConfigurationRequest,
    ECRPutSigningConfigurationResponse,
    ECRRegisterPullTimeUpdateExclusionRequest,
    ECRRegisterPullTimeUpdateExclusionResponse,
    ECRSetRepositoryPolicyRequest,
    ECRSetRepositoryPolicyResponse,
    ECRStartImageScanRequest,
    ECRStartImageScanResponse,
    ECRStartLifecyclePolicyPreviewRequest,
    ECRStartLifecyclePolicyPreviewResponse,
    ECRStartReplicationBackfillRequest,
    ECRStartReplicationBackfillResponse,
    ECRStopReplicationBackfillRequest,
    ECRStopReplicationBackfillResponse,
    ECRTagResourceRequest,
    ECRTagResourceResponse,
    ECRUntagResourceRequest,
    ECRUntagResourceResponse,
    ECRUpdateImageStorageClassRequest,
    ECRUpdateImageStorageClassResponse,
    ECRUpdatePullThroughCacheRuleRequest,
    ECRUpdatePullThroughCacheRuleResponse,
    ECRUpdateRepositoryCreationTemplateRequest,
    ECRUpdateRepositoryCreationTemplateResponse,
    ECRUploadLayerPartRequest,
    ECRUploadLayerPartResponse,
    ECRValidatePullThroughCacheRuleRequest,
    ECRValidatePullThroughCacheRuleResponse,
)
from werkflow_aws.types.ecr_client import ECRClient
from .base import AWSBaseService


class AWSECR(AWSBaseService[ECRClient]):
    service_name = 'ecr'
    boto3_service_name = 'ecr'

    def __init__(self) -> None:
        super().__init__(service_name='ecr', boto3_service_name='ecr')

    async def batch_check_layer_availability(
        self,
        request: ECRBatchCheckLayerAvailabilityRequest,
    ) -> ECRBatchCheckLayerAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.batch_check_layer_availability, request, ECRBatchCheckLayerAvailabilityResponse)

    async def batch_delete_image(
        self,
        request: ECRBatchDeleteImageRequest,
    ) -> ECRBatchDeleteImageResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_image, request, ECRBatchDeleteImageResponse)

    async def batch_get_image(
        self,
        request: ECRBatchGetImageRequest,
    ) -> ECRBatchGetImageResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_image, request, ECRBatchGetImageResponse)

    async def batch_get_repository_scanning_configuration(
        self,
        request: ECRBatchGetRepositoryScanningConfigurationRequest,
    ) -> ECRBatchGetRepositoryScanningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_repository_scanning_configuration, request, ECRBatchGetRepositoryScanningConfigurationResponse)

    async def complete_layer_upload(
        self,
        request: ECRCompleteLayerUploadRequest,
    ) -> ECRCompleteLayerUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_layer_upload, request, ECRCompleteLayerUploadResponse)

    async def create_pull_through_cache_rule(
        self,
        request: ECRCreatePullThroughCacheRuleRequest,
    ) -> ECRCreatePullThroughCacheRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_pull_through_cache_rule, request, ECRCreatePullThroughCacheRuleResponse)

    async def create_repository(
        self,
        request: ECRCreateRepositoryRequest,
    ) -> ECRCreateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.create_repository, request, ECRCreateRepositoryResponse)

    async def create_repository_creation_template(
        self,
        request: ECRCreateRepositoryCreationTemplateRequest,
    ) -> ECRCreateRepositoryCreationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_repository_creation_template, request, ECRCreateRepositoryCreationTemplateResponse)

    async def delete_lifecycle_policy(
        self,
        request: ECRDeleteLifecyclePolicyRequest,
    ) -> ECRDeleteLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_lifecycle_policy, request, ECRDeleteLifecyclePolicyResponse)

    async def delete_pull_through_cache_rule(
        self,
        request: ECRDeletePullThroughCacheRuleRequest,
    ) -> ECRDeletePullThroughCacheRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_pull_through_cache_rule, request, ECRDeletePullThroughCacheRuleResponse)

    async def delete_registry_policy(
        self,
        request: ECRDeleteRegistryPolicyRequest | None = None,
    ) -> ECRDeleteRegistryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_registry_policy, request, ECRDeleteRegistryPolicyResponse)

    async def delete_repository(
        self,
        request: ECRDeleteRepositoryRequest,
    ) -> ECRDeleteRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository, request, ECRDeleteRepositoryResponse)

    async def delete_repository_creation_template(
        self,
        request: ECRDeleteRepositoryCreationTemplateRequest,
    ) -> ECRDeleteRepositoryCreationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository_creation_template, request, ECRDeleteRepositoryCreationTemplateResponse)

    async def delete_repository_policy(
        self,
        request: ECRDeleteRepositoryPolicyRequest,
    ) -> ECRDeleteRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository_policy, request, ECRDeleteRepositoryPolicyResponse)

    async def delete_signing_configuration(
        self,
        request: ECRDeleteSigningConfigurationRequest | None = None,
    ) -> ECRDeleteSigningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_signing_configuration, request, ECRDeleteSigningConfigurationResponse)

    async def deregister_pull_time_update_exclusion(
        self,
        request: ECRDeregisterPullTimeUpdateExclusionRequest,
    ) -> ECRDeregisterPullTimeUpdateExclusionResponse:
        client = self._require_client()
        return await self._execute(client.deregister_pull_time_update_exclusion, request, ECRDeregisterPullTimeUpdateExclusionResponse)

    async def describe_image_replication_status(
        self,
        request: ECRDescribeImageReplicationStatusRequest,
    ) -> ECRDescribeImageReplicationStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_replication_status, request, ECRDescribeImageReplicationStatusResponse)

    async def describe_image_scan_findings(
        self,
        request: ECRDescribeImageScanFindingsRequest,
    ) -> ECRDescribeImageScanFindingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_scan_findings, request, ECRDescribeImageScanFindingsResponse)

    async def describe_image_scan_findings_paginated(
        self,
        request: ECRDescribeImageScanFindingsRequest,
    ) -> list[ECRDescribeImageScanFindingsResponse]:
        return await self._paginate('describe_image_scan_findings', request, ECRDescribeImageScanFindingsResponse)

    async def describe_image_signing_status(
        self,
        request: ECRDescribeImageSigningStatusRequest,
    ) -> ECRDescribeImageSigningStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_signing_status, request, ECRDescribeImageSigningStatusResponse)

    async def describe_images(
        self,
        request: ECRDescribeImagesRequest,
    ) -> ECRDescribeImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_images, request, ECRDescribeImagesResponse)

    async def describe_images_paginated(
        self,
        request: ECRDescribeImagesRequest,
    ) -> list[ECRDescribeImagesResponse]:
        return await self._paginate('describe_images', request, ECRDescribeImagesResponse)

    async def describe_pull_through_cache_rules(
        self,
        request: ECRDescribePullThroughCacheRulesRequest | None = None,
    ) -> ECRDescribePullThroughCacheRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_pull_through_cache_rules, request, ECRDescribePullThroughCacheRulesResponse)

    async def describe_pull_through_cache_rules_paginated(
        self,
        request: ECRDescribePullThroughCacheRulesRequest | None = None,
    ) -> list[ECRDescribePullThroughCacheRulesResponse]:
        return await self._paginate('describe_pull_through_cache_rules', request, ECRDescribePullThroughCacheRulesResponse)

    async def describe_registry(
        self,
        request: ECRDescribeRegistryRequest | None = None,
    ) -> ECRDescribeRegistryResponse:
        client = self._require_client()
        return await self._execute(client.describe_registry, request, ECRDescribeRegistryResponse)

    async def describe_replication_backfill_results(
        self,
        request: ECRDescribeReplicationBackfillResultsRequest,
    ) -> ECRDescribeReplicationBackfillResultsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_backfill_results, request, ECRDescribeReplicationBackfillResultsResponse)

    async def describe_replication_backfill_results_paginated(
        self,
        request: ECRDescribeReplicationBackfillResultsRequest,
    ) -> list[ECRDescribeReplicationBackfillResultsResponse]:
        return await self._paginate('describe_replication_backfill_results', request, ECRDescribeReplicationBackfillResultsResponse)

    async def describe_repositories(
        self,
        request: ECRDescribeRepositoriesRequest | None = None,
    ) -> ECRDescribeRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_repositories, request, ECRDescribeRepositoriesResponse)

    async def describe_repositories_paginated(
        self,
        request: ECRDescribeRepositoriesRequest | None = None,
    ) -> list[ECRDescribeRepositoriesResponse]:
        return await self._paginate('describe_repositories', request, ECRDescribeRepositoriesResponse)

    async def describe_repository_creation_templates(
        self,
        request: ECRDescribeRepositoryCreationTemplatesRequest | None = None,
    ) -> ECRDescribeRepositoryCreationTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_repository_creation_templates, request, ECRDescribeRepositoryCreationTemplatesResponse)

    async def describe_repository_creation_templates_paginated(
        self,
        request: ECRDescribeRepositoryCreationTemplatesRequest | None = None,
    ) -> list[ECRDescribeRepositoryCreationTemplatesResponse]:
        return await self._paginate('describe_repository_creation_templates', request, ECRDescribeRepositoryCreationTemplatesResponse)

    async def get_account_setting(
        self,
        request: ECRGetAccountSettingRequest,
    ) -> ECRGetAccountSettingResponse:
        client = self._require_client()
        return await self._execute(client.get_account_setting, request, ECRGetAccountSettingResponse)

    async def get_authorization_token(
        self,
        request: ECRGetAuthorizationTokenRequest | None = None,
    ) -> ECRGetAuthorizationTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_authorization_token, request, ECRGetAuthorizationTokenResponse)

    async def get_download_url_for_layer(
        self,
        request: ECRGetDownloadUrlForLayerRequest,
    ) -> ECRGetDownloadUrlForLayerResponse:
        client = self._require_client()
        return await self._execute(client.get_download_url_for_layer, request, ECRGetDownloadUrlForLayerResponse)

    async def get_lifecycle_policy(
        self,
        request: ECRGetLifecyclePolicyRequest,
    ) -> ECRGetLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_lifecycle_policy, request, ECRGetLifecyclePolicyResponse)

    async def get_lifecycle_policy_preview(
        self,
        request: ECRGetLifecyclePolicyPreviewRequest,
    ) -> ECRGetLifecyclePolicyPreviewResponse:
        client = self._require_client()
        return await self._execute(client.get_lifecycle_policy_preview, request, ECRGetLifecyclePolicyPreviewResponse)

    async def get_lifecycle_policy_preview_paginated(
        self,
        request: ECRGetLifecyclePolicyPreviewRequest,
    ) -> list[ECRGetLifecyclePolicyPreviewResponse]:
        return await self._paginate('get_lifecycle_policy_preview', request, ECRGetLifecyclePolicyPreviewResponse)

    async def get_registry_policy(
        self,
        request: ECRGetRegistryPolicyRequest | None = None,
    ) -> ECRGetRegistryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_registry_policy, request, ECRGetRegistryPolicyResponse)

    async def get_registry_scanning_configuration(
        self,
        request: ECRGetRegistryScanningConfigurationRequest | None = None,
    ) -> ECRGetRegistryScanningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_registry_scanning_configuration, request, ECRGetRegistryScanningConfigurationResponse)

    async def get_repository_policy(
        self,
        request: ECRGetRepositoryPolicyRequest,
    ) -> ECRGetRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_repository_policy, request, ECRGetRepositoryPolicyResponse)

    async def get_signing_configuration(
        self,
        request: ECRGetSigningConfigurationRequest | None = None,
    ) -> ECRGetSigningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_signing_configuration, request, ECRGetSigningConfigurationResponse)

    async def initiate_layer_upload(
        self,
        request: ECRInitiateLayerUploadRequest,
    ) -> ECRInitiateLayerUploadResponse:
        client = self._require_client()
        return await self._execute(client.initiate_layer_upload, request, ECRInitiateLayerUploadResponse)

    async def list_image_referrers(
        self,
        request: ECRListImageReferrersRequest,
    ) -> ECRListImageReferrersResponse:
        client = self._require_client()
        return await self._execute(client.list_image_referrers, request, ECRListImageReferrersResponse)

    async def list_images(
        self,
        request: ECRListImagesRequest,
    ) -> ECRListImagesResponse:
        client = self._require_client()
        return await self._execute(client.list_images, request, ECRListImagesResponse)

    async def list_images_paginated(
        self,
        request: ECRListImagesRequest,
    ) -> list[ECRListImagesResponse]:
        return await self._paginate('list_images', request, ECRListImagesResponse)

    async def list_pull_time_update_exclusions(
        self,
        request: ECRListPullTimeUpdateExclusionsRequest | None = None,
    ) -> ECRListPullTimeUpdateExclusionsResponse:
        client = self._require_client()
        return await self._execute(client.list_pull_time_update_exclusions, request, ECRListPullTimeUpdateExclusionsResponse)

    async def list_replication_backfills(
        self,
        request: ECRListReplicationBackfillsRequest | None = None,
    ) -> ECRListReplicationBackfillsResponse:
        client = self._require_client()
        return await self._execute(client.list_replication_backfills, request, ECRListReplicationBackfillsResponse)

    async def list_replication_backfills_paginated(
        self,
        request: ECRListReplicationBackfillsRequest | None = None,
    ) -> list[ECRListReplicationBackfillsResponse]:
        return await self._paginate('list_replication_backfills', request, ECRListReplicationBackfillsResponse)

    async def list_tags_for_resource(
        self,
        request: ECRListTagsForResourceRequest,
    ) -> ECRListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ECRListTagsForResourceResponse)

    async def put_account_setting(
        self,
        request: ECRPutAccountSettingRequest,
    ) -> ECRPutAccountSettingResponse:
        client = self._require_client()
        return await self._execute(client.put_account_setting, request, ECRPutAccountSettingResponse)

    async def put_image(
        self,
        request: ECRPutImageRequest,
    ) -> ECRPutImageResponse:
        client = self._require_client()
        return await self._execute(client.put_image, request, ECRPutImageResponse)

    async def put_image_scanning_configuration(
        self,
        request: ECRPutImageScanningConfigurationRequest,
    ) -> ECRPutImageScanningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_image_scanning_configuration, request, ECRPutImageScanningConfigurationResponse)

    async def put_image_tag_mutability(
        self,
        request: ECRPutImageTagMutabilityRequest,
    ) -> ECRPutImageTagMutabilityResponse:
        client = self._require_client()
        return await self._execute(client.put_image_tag_mutability, request, ECRPutImageTagMutabilityResponse)

    async def put_lifecycle_policy(
        self,
        request: ECRPutLifecyclePolicyRequest,
    ) -> ECRPutLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_lifecycle_policy, request, ECRPutLifecyclePolicyResponse)

    async def put_registry_policy(
        self,
        request: ECRPutRegistryPolicyRequest,
    ) -> ECRPutRegistryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_registry_policy, request, ECRPutRegistryPolicyResponse)

    async def put_registry_scanning_configuration(
        self,
        request: ECRPutRegistryScanningConfigurationRequest | None = None,
    ) -> ECRPutRegistryScanningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_registry_scanning_configuration, request, ECRPutRegistryScanningConfigurationResponse)

    async def put_replication_configuration(
        self,
        request: ECRPutReplicationConfigurationRequest,
    ) -> ECRPutReplicationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_replication_configuration, request, ECRPutReplicationConfigurationResponse)

    async def put_signing_configuration(
        self,
        request: ECRPutSigningConfigurationRequest,
    ) -> ECRPutSigningConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_signing_configuration, request, ECRPutSigningConfigurationResponse)

    async def register_pull_time_update_exclusion(
        self,
        request: ECRRegisterPullTimeUpdateExclusionRequest,
    ) -> ECRRegisterPullTimeUpdateExclusionResponse:
        client = self._require_client()
        return await self._execute(client.register_pull_time_update_exclusion, request, ECRRegisterPullTimeUpdateExclusionResponse)

    async def set_repository_policy(
        self,
        request: ECRSetRepositoryPolicyRequest,
    ) -> ECRSetRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.set_repository_policy, request, ECRSetRepositoryPolicyResponse)

    async def start_image_scan(
        self,
        request: ECRStartImageScanRequest,
    ) -> ECRStartImageScanResponse:
        client = self._require_client()
        return await self._execute(client.start_image_scan, request, ECRStartImageScanResponse)

    async def start_lifecycle_policy_preview(
        self,
        request: ECRStartLifecyclePolicyPreviewRequest,
    ) -> ECRStartLifecyclePolicyPreviewResponse:
        client = self._require_client()
        return await self._execute(client.start_lifecycle_policy_preview, request, ECRStartLifecyclePolicyPreviewResponse)

    async def start_replication_backfill(
        self,
        request: ECRStartReplicationBackfillRequest,
    ) -> ECRStartReplicationBackfillResponse:
        client = self._require_client()
        return await self._execute(client.start_replication_backfill, request, ECRStartReplicationBackfillResponse)

    async def stop_replication_backfill(
        self,
        request: ECRStopReplicationBackfillRequest,
    ) -> ECRStopReplicationBackfillResponse:
        client = self._require_client()
        return await self._execute(client.stop_replication_backfill, request, ECRStopReplicationBackfillResponse)

    async def tag_resource(
        self,
        request: ECRTagResourceRequest,
    ) -> ECRTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ECRTagResourceResponse)

    async def untag_resource(
        self,
        request: ECRUntagResourceRequest,
    ) -> ECRUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ECRUntagResourceResponse)

    async def update_image_storage_class(
        self,
        request: ECRUpdateImageStorageClassRequest,
    ) -> ECRUpdateImageStorageClassResponse:
        client = self._require_client()
        return await self._execute(client.update_image_storage_class, request, ECRUpdateImageStorageClassResponse)

    async def update_pull_through_cache_rule(
        self,
        request: ECRUpdatePullThroughCacheRuleRequest,
    ) -> ECRUpdatePullThroughCacheRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_through_cache_rule, request, ECRUpdatePullThroughCacheRuleResponse)

    async def update_repository_creation_template(
        self,
        request: ECRUpdateRepositoryCreationTemplateRequest,
    ) -> ECRUpdateRepositoryCreationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_repository_creation_template, request, ECRUpdateRepositoryCreationTemplateResponse)

    async def upload_layer_part(
        self,
        request: ECRUploadLayerPartRequest,
    ) -> ECRUploadLayerPartResponse:
        client = self._require_client()
        return await self._execute(client.upload_layer_part, request, ECRUploadLayerPartResponse)

    async def validate_pull_through_cache_rule(
        self,
        request: ECRValidatePullThroughCacheRuleRequest,
    ) -> ECRValidatePullThroughCacheRuleResponse:
        client = self._require_client()
        return await self._execute(client.validate_pull_through_cache_rule, request, ECRValidatePullThroughCacheRuleResponse)
