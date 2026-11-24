from werkflow_aws.models.ecr_public import (
    ECRPublicBatchCheckLayerAvailabilityRequest,
    ECRPublicBatchCheckLayerAvailabilityResponse,
    ECRPublicBatchDeleteImageRequest,
    ECRPublicBatchDeleteImageResponse,
    ECRPublicCompleteLayerUploadRequest,
    ECRPublicCompleteLayerUploadResponse,
    ECRPublicCreateRepositoryRequest,
    ECRPublicCreateRepositoryResponse,
    ECRPublicDeleteRepositoryPolicyRequest,
    ECRPublicDeleteRepositoryPolicyResponse,
    ECRPublicDeleteRepositoryRequest,
    ECRPublicDeleteRepositoryResponse,
    ECRPublicDescribeImageTagsRequest,
    ECRPublicDescribeImageTagsResponse,
    ECRPublicDescribeImagesRequest,
    ECRPublicDescribeImagesResponse,
    ECRPublicDescribeRegistriesRequest,
    ECRPublicDescribeRegistriesResponse,
    ECRPublicDescribeRepositoriesRequest,
    ECRPublicDescribeRepositoriesResponse,
    ECRPublicGetAuthorizationTokenRequest,
    ECRPublicGetAuthorizationTokenResponse,
    ECRPublicGetRegistryCatalogDataRequest,
    ECRPublicGetRegistryCatalogDataResponse,
    ECRPublicGetRepositoryCatalogDataRequest,
    ECRPublicGetRepositoryCatalogDataResponse,
    ECRPublicGetRepositoryPolicyRequest,
    ECRPublicGetRepositoryPolicyResponse,
    ECRPublicInitiateLayerUploadRequest,
    ECRPublicInitiateLayerUploadResponse,
    ECRPublicListTagsForResourceRequest,
    ECRPublicListTagsForResourceResponse,
    ECRPublicPutImageRequest,
    ECRPublicPutImageResponse,
    ECRPublicPutRegistryCatalogDataRequest,
    ECRPublicPutRegistryCatalogDataResponse,
    ECRPublicPutRepositoryCatalogDataRequest,
    ECRPublicPutRepositoryCatalogDataResponse,
    ECRPublicSetRepositoryPolicyRequest,
    ECRPublicSetRepositoryPolicyResponse,
    ECRPublicTagResourceRequest,
    ECRPublicTagResourceResponse,
    ECRPublicUntagResourceRequest,
    ECRPublicUntagResourceResponse,
    ECRPublicUploadLayerPartRequest,
    ECRPublicUploadLayerPartResponse,
)
from werkflow_aws.types.ecr_public_client import ECRPublicClient
from .base import AWSBaseService


class AWSECRPublic(AWSBaseService[ECRPublicClient]):
    service_name = 'ecr-public'
    boto3_service_name = 'ecr-public'

    def __init__(self) -> None:
        super().__init__(service_name='ecr-public', boto3_service_name='ecr-public')

    async def batch_check_layer_availability(
        self,
        request: ECRPublicBatchCheckLayerAvailabilityRequest,
    ) -> ECRPublicBatchCheckLayerAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.batch_check_layer_availability, request, ECRPublicBatchCheckLayerAvailabilityResponse)

    async def batch_delete_image(
        self,
        request: ECRPublicBatchDeleteImageRequest,
    ) -> ECRPublicBatchDeleteImageResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_image, request, ECRPublicBatchDeleteImageResponse)

    async def complete_layer_upload(
        self,
        request: ECRPublicCompleteLayerUploadRequest,
    ) -> ECRPublicCompleteLayerUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_layer_upload, request, ECRPublicCompleteLayerUploadResponse)

    async def create_repository(
        self,
        request: ECRPublicCreateRepositoryRequest,
    ) -> ECRPublicCreateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.create_repository, request, ECRPublicCreateRepositoryResponse)

    async def delete_repository(
        self,
        request: ECRPublicDeleteRepositoryRequest,
    ) -> ECRPublicDeleteRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository, request, ECRPublicDeleteRepositoryResponse)

    async def delete_repository_policy(
        self,
        request: ECRPublicDeleteRepositoryPolicyRequest,
    ) -> ECRPublicDeleteRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository_policy, request, ECRPublicDeleteRepositoryPolicyResponse)

    async def describe_image_tags(
        self,
        request: ECRPublicDescribeImageTagsRequest,
    ) -> ECRPublicDescribeImageTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_tags, request, ECRPublicDescribeImageTagsResponse)

    async def describe_image_tags_paginated(
        self,
        request: ECRPublicDescribeImageTagsRequest,
    ) -> list[ECRPublicDescribeImageTagsResponse]:
        return await self._paginate('describe_image_tags', request, ECRPublicDescribeImageTagsResponse)

    async def describe_images(
        self,
        request: ECRPublicDescribeImagesRequest,
    ) -> ECRPublicDescribeImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_images, request, ECRPublicDescribeImagesResponse)

    async def describe_images_paginated(
        self,
        request: ECRPublicDescribeImagesRequest,
    ) -> list[ECRPublicDescribeImagesResponse]:
        return await self._paginate('describe_images', request, ECRPublicDescribeImagesResponse)

    async def describe_registries(
        self,
        request: ECRPublicDescribeRegistriesRequest | None = None,
    ) -> ECRPublicDescribeRegistriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_registries, request, ECRPublicDescribeRegistriesResponse)

    async def describe_registries_paginated(
        self,
        request: ECRPublicDescribeRegistriesRequest | None = None,
    ) -> list[ECRPublicDescribeRegistriesResponse]:
        return await self._paginate('describe_registries', request, ECRPublicDescribeRegistriesResponse)

    async def describe_repositories(
        self,
        request: ECRPublicDescribeRepositoriesRequest | None = None,
    ) -> ECRPublicDescribeRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_repositories, request, ECRPublicDescribeRepositoriesResponse)

    async def describe_repositories_paginated(
        self,
        request: ECRPublicDescribeRepositoriesRequest | None = None,
    ) -> list[ECRPublicDescribeRepositoriesResponse]:
        return await self._paginate('describe_repositories', request, ECRPublicDescribeRepositoriesResponse)

    async def get_authorization_token(
        self,
        request: ECRPublicGetAuthorizationTokenRequest | None = None,
    ) -> ECRPublicGetAuthorizationTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_authorization_token, request, ECRPublicGetAuthorizationTokenResponse)

    async def get_registry_catalog_data(
        self,
        request: ECRPublicGetRegistryCatalogDataRequest | None = None,
    ) -> ECRPublicGetRegistryCatalogDataResponse:
        client = self._require_client()
        return await self._execute(client.get_registry_catalog_data, request, ECRPublicGetRegistryCatalogDataResponse)

    async def get_repository_catalog_data(
        self,
        request: ECRPublicGetRepositoryCatalogDataRequest,
    ) -> ECRPublicGetRepositoryCatalogDataResponse:
        client = self._require_client()
        return await self._execute(client.get_repository_catalog_data, request, ECRPublicGetRepositoryCatalogDataResponse)

    async def get_repository_policy(
        self,
        request: ECRPublicGetRepositoryPolicyRequest,
    ) -> ECRPublicGetRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_repository_policy, request, ECRPublicGetRepositoryPolicyResponse)

    async def initiate_layer_upload(
        self,
        request: ECRPublicInitiateLayerUploadRequest,
    ) -> ECRPublicInitiateLayerUploadResponse:
        client = self._require_client()
        return await self._execute(client.initiate_layer_upload, request, ECRPublicInitiateLayerUploadResponse)

    async def list_tags_for_resource(
        self,
        request: ECRPublicListTagsForResourceRequest,
    ) -> ECRPublicListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ECRPublicListTagsForResourceResponse)

    async def put_image(
        self,
        request: ECRPublicPutImageRequest,
    ) -> ECRPublicPutImageResponse:
        client = self._require_client()
        return await self._execute(client.put_image, request, ECRPublicPutImageResponse)

    async def put_registry_catalog_data(
        self,
        request: ECRPublicPutRegistryCatalogDataRequest | None = None,
    ) -> ECRPublicPutRegistryCatalogDataResponse:
        client = self._require_client()
        return await self._execute(client.put_registry_catalog_data, request, ECRPublicPutRegistryCatalogDataResponse)

    async def put_repository_catalog_data(
        self,
        request: ECRPublicPutRepositoryCatalogDataRequest,
    ) -> ECRPublicPutRepositoryCatalogDataResponse:
        client = self._require_client()
        return await self._execute(client.put_repository_catalog_data, request, ECRPublicPutRepositoryCatalogDataResponse)

    async def set_repository_policy(
        self,
        request: ECRPublicSetRepositoryPolicyRequest,
    ) -> ECRPublicSetRepositoryPolicyResponse:
        client = self._require_client()
        return await self._execute(client.set_repository_policy, request, ECRPublicSetRepositoryPolicyResponse)

    async def tag_resource(
        self,
        request: ECRPublicTagResourceRequest,
    ) -> ECRPublicTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ECRPublicTagResourceResponse)

    async def untag_resource(
        self,
        request: ECRPublicUntagResourceRequest,
    ) -> ECRPublicUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ECRPublicUntagResourceResponse)

    async def upload_layer_part(
        self,
        request: ECRPublicUploadLayerPartRequest,
    ) -> ECRPublicUploadLayerPartResponse:
        client = self._require_client()
        return await self._execute(client.upload_layer_part, request, ECRPublicUploadLayerPartResponse)
