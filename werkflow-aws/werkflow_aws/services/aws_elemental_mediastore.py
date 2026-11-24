from werkflow_aws.models.elemental_mediastore import (
    MediaStoreCreateContainerRequest,
    MediaStoreCreateContainerResponse,
    MediaStoreDeleteContainerPolicyRequest,
    MediaStoreDeleteContainerPolicyResponse,
    MediaStoreDeleteContainerRequest,
    MediaStoreDeleteContainerResponse,
    MediaStoreDeleteCorsPolicyRequest,
    MediaStoreDeleteCorsPolicyResponse,
    MediaStoreDeleteLifecyclePolicyRequest,
    MediaStoreDeleteLifecyclePolicyResponse,
    MediaStoreDeleteMetricPolicyRequest,
    MediaStoreDeleteMetricPolicyResponse,
    MediaStoreDescribeContainerRequest,
    MediaStoreDescribeContainerResponse,
    MediaStoreGetContainerPolicyRequest,
    MediaStoreGetContainerPolicyResponse,
    MediaStoreGetCorsPolicyRequest,
    MediaStoreGetCorsPolicyResponse,
    MediaStoreGetLifecyclePolicyRequest,
    MediaStoreGetLifecyclePolicyResponse,
    MediaStoreGetMetricPolicyRequest,
    MediaStoreGetMetricPolicyResponse,
    MediaStoreListContainersRequest,
    MediaStoreListContainersResponse,
    MediaStoreListTagsForResourceRequest,
    MediaStoreListTagsForResourceResponse,
    MediaStorePutContainerPolicyRequest,
    MediaStorePutContainerPolicyResponse,
    MediaStorePutCorsPolicyRequest,
    MediaStorePutCorsPolicyResponse,
    MediaStorePutLifecyclePolicyRequest,
    MediaStorePutLifecyclePolicyResponse,
    MediaStorePutMetricPolicyRequest,
    MediaStorePutMetricPolicyResponse,
    MediaStoreStartAccessLoggingRequest,
    MediaStoreStartAccessLoggingResponse,
    MediaStoreStopAccessLoggingRequest,
    MediaStoreStopAccessLoggingResponse,
    MediaStoreTagResourceRequest,
    MediaStoreTagResourceResponse,
    MediaStoreUntagResourceRequest,
    MediaStoreUntagResourceResponse,
)
from werkflow_aws.types.elemental_mediastore_client import MediaStoreClient
from .base import AWSBaseService


class AWSMediaStore(AWSBaseService[MediaStoreClient]):
    service_name = 'elemental-mediastore'
    boto3_service_name = 'mediastore'

    def __init__(self) -> None:
        super().__init__(service_name='elemental-mediastore', boto3_service_name='mediastore')

    async def create_container(
        self,
        request: MediaStoreCreateContainerRequest,
    ) -> MediaStoreCreateContainerResponse:
        client = self._require_client()
        return await self._execute(client.create_container, request, MediaStoreCreateContainerResponse)

    async def delete_container(
        self,
        request: MediaStoreDeleteContainerRequest,
    ) -> MediaStoreDeleteContainerResponse:
        client = self._require_client()
        return await self._execute(client.delete_container, request, MediaStoreDeleteContainerResponse)

    async def delete_container_policy(
        self,
        request: MediaStoreDeleteContainerPolicyRequest,
    ) -> MediaStoreDeleteContainerPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_container_policy, request, MediaStoreDeleteContainerPolicyResponse)

    async def delete_cors_policy(
        self,
        request: MediaStoreDeleteCorsPolicyRequest,
    ) -> MediaStoreDeleteCorsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_cors_policy, request, MediaStoreDeleteCorsPolicyResponse)

    async def delete_lifecycle_policy(
        self,
        request: MediaStoreDeleteLifecyclePolicyRequest,
    ) -> MediaStoreDeleteLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_lifecycle_policy, request, MediaStoreDeleteLifecyclePolicyResponse)

    async def delete_metric_policy(
        self,
        request: MediaStoreDeleteMetricPolicyRequest,
    ) -> MediaStoreDeleteMetricPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_policy, request, MediaStoreDeleteMetricPolicyResponse)

    async def describe_container(
        self,
        request: MediaStoreDescribeContainerRequest | None = None,
    ) -> MediaStoreDescribeContainerResponse:
        client = self._require_client()
        return await self._execute(client.describe_container, request, MediaStoreDescribeContainerResponse)

    async def get_container_policy(
        self,
        request: MediaStoreGetContainerPolicyRequest,
    ) -> MediaStoreGetContainerPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_container_policy, request, MediaStoreGetContainerPolicyResponse)

    async def get_cors_policy(
        self,
        request: MediaStoreGetCorsPolicyRequest,
    ) -> MediaStoreGetCorsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_cors_policy, request, MediaStoreGetCorsPolicyResponse)

    async def get_lifecycle_policy(
        self,
        request: MediaStoreGetLifecyclePolicyRequest,
    ) -> MediaStoreGetLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_lifecycle_policy, request, MediaStoreGetLifecyclePolicyResponse)

    async def get_metric_policy(
        self,
        request: MediaStoreGetMetricPolicyRequest,
    ) -> MediaStoreGetMetricPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_metric_policy, request, MediaStoreGetMetricPolicyResponse)

    async def list_containers(
        self,
        request: MediaStoreListContainersRequest | None = None,
    ) -> MediaStoreListContainersResponse:
        client = self._require_client()
        return await self._execute(client.list_containers, request, MediaStoreListContainersResponse)

    async def list_containers_paginated(
        self,
        request: MediaStoreListContainersRequest | None = None,
    ) -> list[MediaStoreListContainersResponse]:
        return await self._paginate('list_containers', request, MediaStoreListContainersResponse)

    async def list_tags_for_resource(
        self,
        request: MediaStoreListTagsForResourceRequest,
    ) -> MediaStoreListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, MediaStoreListTagsForResourceResponse)

    async def put_container_policy(
        self,
        request: MediaStorePutContainerPolicyRequest,
    ) -> MediaStorePutContainerPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_container_policy, request, MediaStorePutContainerPolicyResponse)

    async def put_cors_policy(
        self,
        request: MediaStorePutCorsPolicyRequest,
    ) -> MediaStorePutCorsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_cors_policy, request, MediaStorePutCorsPolicyResponse)

    async def put_lifecycle_policy(
        self,
        request: MediaStorePutLifecyclePolicyRequest,
    ) -> MediaStorePutLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_lifecycle_policy, request, MediaStorePutLifecyclePolicyResponse)

    async def put_metric_policy(
        self,
        request: MediaStorePutMetricPolicyRequest,
    ) -> MediaStorePutMetricPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_metric_policy, request, MediaStorePutMetricPolicyResponse)

    async def start_access_logging(
        self,
        request: MediaStoreStartAccessLoggingRequest,
    ) -> MediaStoreStartAccessLoggingResponse:
        client = self._require_client()
        return await self._execute(client.start_access_logging, request, MediaStoreStartAccessLoggingResponse)

    async def stop_access_logging(
        self,
        request: MediaStoreStopAccessLoggingRequest,
    ) -> MediaStoreStopAccessLoggingResponse:
        client = self._require_client()
        return await self._execute(client.stop_access_logging, request, MediaStoreStopAccessLoggingResponse)

    async def tag_resource(
        self,
        request: MediaStoreTagResourceRequest,
    ) -> MediaStoreTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, MediaStoreTagResourceResponse)

    async def untag_resource(
        self,
        request: MediaStoreUntagResourceRequest,
    ) -> MediaStoreUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, MediaStoreUntagResourceResponse)
