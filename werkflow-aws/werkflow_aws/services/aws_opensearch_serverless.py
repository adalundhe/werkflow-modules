from werkflow_aws.models.opensearch_serverless import (
    OpenSearchServerlessBatchGetCollectionGroupRequest,
    OpenSearchServerlessBatchGetCollectionGroupResponse,
    OpenSearchServerlessBatchGetCollectionRequest,
    OpenSearchServerlessBatchGetCollectionResponse,
    OpenSearchServerlessBatchGetEffectiveLifecyclePolicyRequest,
    OpenSearchServerlessBatchGetEffectiveLifecyclePolicyResponse,
    OpenSearchServerlessBatchGetLifecyclePolicyRequest,
    OpenSearchServerlessBatchGetLifecyclePolicyResponse,
    OpenSearchServerlessBatchGetVpcEndpointRequest,
    OpenSearchServerlessBatchGetVpcEndpointResponse,
    OpenSearchServerlessCancelIngestionJobRequest,
    OpenSearchServerlessCancelIngestionJobResponse,
    OpenSearchServerlessCreateAccessPolicyRequest,
    OpenSearchServerlessCreateAccessPolicyResponse,
    OpenSearchServerlessCreateCollectionGroupRequest,
    OpenSearchServerlessCreateCollectionGroupResponse,
    OpenSearchServerlessCreateCollectionRequest,
    OpenSearchServerlessCreateCollectionResponse,
    OpenSearchServerlessCreateIndexRequest,
    OpenSearchServerlessCreateIndexResponse,
    OpenSearchServerlessCreateIngestionJobRequest,
    OpenSearchServerlessCreateIngestionJobResponse,
    OpenSearchServerlessCreateIngestionStreamRequest,
    OpenSearchServerlessCreateIngestionStreamResponse,
    OpenSearchServerlessCreateLifecyclePolicyRequest,
    OpenSearchServerlessCreateLifecyclePolicyResponse,
    OpenSearchServerlessCreateSecurityConfigRequest,
    OpenSearchServerlessCreateSecurityConfigResponse,
    OpenSearchServerlessCreateSecurityPolicyRequest,
    OpenSearchServerlessCreateSecurityPolicyResponse,
    OpenSearchServerlessCreateVpcEndpointRequest,
    OpenSearchServerlessCreateVpcEndpointResponse,
    OpenSearchServerlessDeleteAccessPolicyRequest,
    OpenSearchServerlessDeleteAccessPolicyResponse,
    OpenSearchServerlessDeleteCollectionGroupRequest,
    OpenSearchServerlessDeleteCollectionGroupResponse,
    OpenSearchServerlessDeleteCollectionRequest,
    OpenSearchServerlessDeleteCollectionResponse,
    OpenSearchServerlessDeleteIndexRequest,
    OpenSearchServerlessDeleteIndexResponse,
    OpenSearchServerlessDeleteIngestionStreamRequest,
    OpenSearchServerlessDeleteIngestionStreamResponse,
    OpenSearchServerlessDeleteLifecyclePolicyRequest,
    OpenSearchServerlessDeleteLifecyclePolicyResponse,
    OpenSearchServerlessDeleteSecurityConfigRequest,
    OpenSearchServerlessDeleteSecurityConfigResponse,
    OpenSearchServerlessDeleteSecurityPolicyRequest,
    OpenSearchServerlessDeleteSecurityPolicyResponse,
    OpenSearchServerlessDeleteVpcEndpointRequest,
    OpenSearchServerlessDeleteVpcEndpointResponse,
    OpenSearchServerlessGetAccessPolicyRequest,
    OpenSearchServerlessGetAccessPolicyResponse,
    OpenSearchServerlessGetAccountSettingsRequest,
    OpenSearchServerlessGetAccountSettingsResponse,
    OpenSearchServerlessGetIndexRequest,
    OpenSearchServerlessGetIndexResponse,
    OpenSearchServerlessGetIngestionJobRequest,
    OpenSearchServerlessGetIngestionJobResponse,
    OpenSearchServerlessGetIngestionStreamRequest,
    OpenSearchServerlessGetIngestionStreamResponse,
    OpenSearchServerlessGetPoliciesStatsRequest,
    OpenSearchServerlessGetPoliciesStatsResponse,
    OpenSearchServerlessGetSecurityConfigRequest,
    OpenSearchServerlessGetSecurityConfigResponse,
    OpenSearchServerlessGetSecurityPolicyRequest,
    OpenSearchServerlessGetSecurityPolicyResponse,
    OpenSearchServerlessListAccessPoliciesRequest,
    OpenSearchServerlessListAccessPoliciesResponse,
    OpenSearchServerlessListCollectionGroupsRequest,
    OpenSearchServerlessListCollectionGroupsResponse,
    OpenSearchServerlessListCollectionsRequest,
    OpenSearchServerlessListCollectionsResponse,
    OpenSearchServerlessListIngestionJobsRequest,
    OpenSearchServerlessListIngestionJobsResponse,
    OpenSearchServerlessListIngestionStreamsRequest,
    OpenSearchServerlessListIngestionStreamsResponse,
    OpenSearchServerlessListLifecyclePoliciesRequest,
    OpenSearchServerlessListLifecyclePoliciesResponse,
    OpenSearchServerlessListSecurityConfigsRequest,
    OpenSearchServerlessListSecurityConfigsResponse,
    OpenSearchServerlessListSecurityPoliciesRequest,
    OpenSearchServerlessListSecurityPoliciesResponse,
    OpenSearchServerlessListTagsForResourceRequest,
    OpenSearchServerlessListTagsForResourceResponse,
    OpenSearchServerlessListVpcEndpointsRequest,
    OpenSearchServerlessListVpcEndpointsResponse,
    OpenSearchServerlessTagResourceRequest,
    OpenSearchServerlessTagResourceResponse,
    OpenSearchServerlessUntagResourceRequest,
    OpenSearchServerlessUntagResourceResponse,
    OpenSearchServerlessUpdateAccessPolicyRequest,
    OpenSearchServerlessUpdateAccessPolicyResponse,
    OpenSearchServerlessUpdateAccountSettingsRequest,
    OpenSearchServerlessUpdateAccountSettingsResponse,
    OpenSearchServerlessUpdateCollectionGroupRequest,
    OpenSearchServerlessUpdateCollectionGroupResponse,
    OpenSearchServerlessUpdateCollectionRequest,
    OpenSearchServerlessUpdateCollectionResponse,
    OpenSearchServerlessUpdateIndexRequest,
    OpenSearchServerlessUpdateIndexResponse,
    OpenSearchServerlessUpdateLifecyclePolicyRequest,
    OpenSearchServerlessUpdateLifecyclePolicyResponse,
    OpenSearchServerlessUpdateSecurityConfigRequest,
    OpenSearchServerlessUpdateSecurityConfigResponse,
    OpenSearchServerlessUpdateSecurityPolicyRequest,
    OpenSearchServerlessUpdateSecurityPolicyResponse,
    OpenSearchServerlessUpdateVpcEndpointRequest,
    OpenSearchServerlessUpdateVpcEndpointResponse,
)
from werkflow_aws.types.opensearch_serverless_client import OpenSearchServerlessClient
from .base import AWSBaseService


class AWSOpenSearchServerless(AWSBaseService[OpenSearchServerlessClient]):
    service_name = 'opensearch-serverless'
    boto3_service_name = 'opensearchserverless'

    def __init__(self) -> None:
        super().__init__(service_name='opensearch-serverless', boto3_service_name='opensearchserverless')

    async def batch_get_collection(
        self,
        request: OpenSearchServerlessBatchGetCollectionRequest | None = None,
    ) -> OpenSearchServerlessBatchGetCollectionResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_collection, request, OpenSearchServerlessBatchGetCollectionResponse)

    async def batch_get_collection_group(
        self,
        request: OpenSearchServerlessBatchGetCollectionGroupRequest | None = None,
    ) -> OpenSearchServerlessBatchGetCollectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_collection_group, request, OpenSearchServerlessBatchGetCollectionGroupResponse)

    async def batch_get_effective_lifecycle_policy(
        self,
        request: OpenSearchServerlessBatchGetEffectiveLifecyclePolicyRequest,
    ) -> OpenSearchServerlessBatchGetEffectiveLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_effective_lifecycle_policy, request, OpenSearchServerlessBatchGetEffectiveLifecyclePolicyResponse)

    async def batch_get_lifecycle_policy(
        self,
        request: OpenSearchServerlessBatchGetLifecyclePolicyRequest,
    ) -> OpenSearchServerlessBatchGetLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_lifecycle_policy, request, OpenSearchServerlessBatchGetLifecyclePolicyResponse)

    async def batch_get_vpc_endpoint(
        self,
        request: OpenSearchServerlessBatchGetVpcEndpointRequest,
    ) -> OpenSearchServerlessBatchGetVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_vpc_endpoint, request, OpenSearchServerlessBatchGetVpcEndpointResponse)

    async def cancel_ingestion_job(
        self,
        request: OpenSearchServerlessCancelIngestionJobRequest,
    ) -> OpenSearchServerlessCancelIngestionJobResponse:
        client = self._require_client()
        return await self._execute(client.cancel_ingestion_job, request, OpenSearchServerlessCancelIngestionJobResponse)

    async def create_access_policy(
        self,
        request: OpenSearchServerlessCreateAccessPolicyRequest,
    ) -> OpenSearchServerlessCreateAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_access_policy, request, OpenSearchServerlessCreateAccessPolicyResponse)

    async def create_collection(
        self,
        request: OpenSearchServerlessCreateCollectionRequest,
    ) -> OpenSearchServerlessCreateCollectionResponse:
        client = self._require_client()
        return await self._execute(client.create_collection, request, OpenSearchServerlessCreateCollectionResponse)

    async def create_collection_group(
        self,
        request: OpenSearchServerlessCreateCollectionGroupRequest,
    ) -> OpenSearchServerlessCreateCollectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_collection_group, request, OpenSearchServerlessCreateCollectionGroupResponse)

    async def create_index(
        self,
        request: OpenSearchServerlessCreateIndexRequest,
    ) -> OpenSearchServerlessCreateIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_index, request, OpenSearchServerlessCreateIndexResponse)

    async def create_ingestion_job(
        self,
        request: OpenSearchServerlessCreateIngestionJobRequest,
    ) -> OpenSearchServerlessCreateIngestionJobResponse:
        client = self._require_client()
        return await self._execute(client.create_ingestion_job, request, OpenSearchServerlessCreateIngestionJobResponse)

    async def create_ingestion_stream(
        self,
        request: OpenSearchServerlessCreateIngestionStreamRequest,
    ) -> OpenSearchServerlessCreateIngestionStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_ingestion_stream, request, OpenSearchServerlessCreateIngestionStreamResponse)

    async def create_lifecycle_policy(
        self,
        request: OpenSearchServerlessCreateLifecyclePolicyRequest,
    ) -> OpenSearchServerlessCreateLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_lifecycle_policy, request, OpenSearchServerlessCreateLifecyclePolicyResponse)

    async def create_security_config(
        self,
        request: OpenSearchServerlessCreateSecurityConfigRequest,
    ) -> OpenSearchServerlessCreateSecurityConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_security_config, request, OpenSearchServerlessCreateSecurityConfigResponse)

    async def create_security_policy(
        self,
        request: OpenSearchServerlessCreateSecurityPolicyRequest,
    ) -> OpenSearchServerlessCreateSecurityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_security_policy, request, OpenSearchServerlessCreateSecurityPolicyResponse)

    async def create_vpc_endpoint(
        self,
        request: OpenSearchServerlessCreateVpcEndpointRequest,
    ) -> OpenSearchServerlessCreateVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_endpoint, request, OpenSearchServerlessCreateVpcEndpointResponse)

    async def delete_access_policy(
        self,
        request: OpenSearchServerlessDeleteAccessPolicyRequest,
    ) -> OpenSearchServerlessDeleteAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_policy, request, OpenSearchServerlessDeleteAccessPolicyResponse)

    async def delete_collection(
        self,
        request: OpenSearchServerlessDeleteCollectionRequest,
    ) -> OpenSearchServerlessDeleteCollectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_collection, request, OpenSearchServerlessDeleteCollectionResponse)

    async def delete_collection_group(
        self,
        request: OpenSearchServerlessDeleteCollectionGroupRequest,
    ) -> OpenSearchServerlessDeleteCollectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_collection_group, request, OpenSearchServerlessDeleteCollectionGroupResponse)

    async def delete_index(
        self,
        request: OpenSearchServerlessDeleteIndexRequest,
    ) -> OpenSearchServerlessDeleteIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_index, request, OpenSearchServerlessDeleteIndexResponse)

    async def delete_ingestion_stream(
        self,
        request: OpenSearchServerlessDeleteIngestionStreamRequest,
    ) -> OpenSearchServerlessDeleteIngestionStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_ingestion_stream, request, OpenSearchServerlessDeleteIngestionStreamResponse)

    async def delete_lifecycle_policy(
        self,
        request: OpenSearchServerlessDeleteLifecyclePolicyRequest,
    ) -> OpenSearchServerlessDeleteLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_lifecycle_policy, request, OpenSearchServerlessDeleteLifecyclePolicyResponse)

    async def delete_security_config(
        self,
        request: OpenSearchServerlessDeleteSecurityConfigRequest,
    ) -> OpenSearchServerlessDeleteSecurityConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_config, request, OpenSearchServerlessDeleteSecurityConfigResponse)

    async def delete_security_policy(
        self,
        request: OpenSearchServerlessDeleteSecurityPolicyRequest,
    ) -> OpenSearchServerlessDeleteSecurityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_policy, request, OpenSearchServerlessDeleteSecurityPolicyResponse)

    async def delete_vpc_endpoint(
        self,
        request: OpenSearchServerlessDeleteVpcEndpointRequest,
    ) -> OpenSearchServerlessDeleteVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_endpoint, request, OpenSearchServerlessDeleteVpcEndpointResponse)

    async def get_access_policy(
        self,
        request: OpenSearchServerlessGetAccessPolicyRequest,
    ) -> OpenSearchServerlessGetAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_access_policy, request, OpenSearchServerlessGetAccessPolicyResponse)

    async def get_account_settings(
        self,
        request: OpenSearchServerlessGetAccountSettingsRequest | None = None,
    ) -> OpenSearchServerlessGetAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_account_settings, request, OpenSearchServerlessGetAccountSettingsResponse)

    async def get_index(
        self,
        request: OpenSearchServerlessGetIndexRequest,
    ) -> OpenSearchServerlessGetIndexResponse:
        client = self._require_client()
        return await self._execute(client.get_index, request, OpenSearchServerlessGetIndexResponse)

    async def get_ingestion_job(
        self,
        request: OpenSearchServerlessGetIngestionJobRequest,
    ) -> OpenSearchServerlessGetIngestionJobResponse:
        client = self._require_client()
        return await self._execute(client.get_ingestion_job, request, OpenSearchServerlessGetIngestionJobResponse)

    async def get_ingestion_stream(
        self,
        request: OpenSearchServerlessGetIngestionStreamRequest,
    ) -> OpenSearchServerlessGetIngestionStreamResponse:
        client = self._require_client()
        return await self._execute(client.get_ingestion_stream, request, OpenSearchServerlessGetIngestionStreamResponse)

    async def get_policies_stats(
        self,
        request: OpenSearchServerlessGetPoliciesStatsRequest | None = None,
    ) -> OpenSearchServerlessGetPoliciesStatsResponse:
        client = self._require_client()
        return await self._execute(client.get_policies_stats, request, OpenSearchServerlessGetPoliciesStatsResponse)

    async def get_security_config(
        self,
        request: OpenSearchServerlessGetSecurityConfigRequest,
    ) -> OpenSearchServerlessGetSecurityConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_security_config, request, OpenSearchServerlessGetSecurityConfigResponse)

    async def get_security_policy(
        self,
        request: OpenSearchServerlessGetSecurityPolicyRequest,
    ) -> OpenSearchServerlessGetSecurityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_security_policy, request, OpenSearchServerlessGetSecurityPolicyResponse)

    async def list_access_policies(
        self,
        request: OpenSearchServerlessListAccessPoliciesRequest,
    ) -> OpenSearchServerlessListAccessPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_access_policies, request, OpenSearchServerlessListAccessPoliciesResponse)

    async def list_collection_groups(
        self,
        request: OpenSearchServerlessListCollectionGroupsRequest | None = None,
    ) -> OpenSearchServerlessListCollectionGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_collection_groups, request, OpenSearchServerlessListCollectionGroupsResponse)

    async def list_collections(
        self,
        request: OpenSearchServerlessListCollectionsRequest | None = None,
    ) -> OpenSearchServerlessListCollectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_collections, request, OpenSearchServerlessListCollectionsResponse)

    async def list_ingestion_jobs(
        self,
        request: OpenSearchServerlessListIngestionJobsRequest,
    ) -> OpenSearchServerlessListIngestionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_ingestion_jobs, request, OpenSearchServerlessListIngestionJobsResponse)

    async def list_ingestion_jobs_paginated(
        self,
        request: OpenSearchServerlessListIngestionJobsRequest,
    ) -> list[OpenSearchServerlessListIngestionJobsResponse]:
        return await self._paginate('list_ingestion_jobs', request, OpenSearchServerlessListIngestionJobsResponse)

    async def list_ingestion_streams(
        self,
        request: OpenSearchServerlessListIngestionStreamsRequest,
    ) -> OpenSearchServerlessListIngestionStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_ingestion_streams, request, OpenSearchServerlessListIngestionStreamsResponse)

    async def list_ingestion_streams_paginated(
        self,
        request: OpenSearchServerlessListIngestionStreamsRequest,
    ) -> list[OpenSearchServerlessListIngestionStreamsResponse]:
        return await self._paginate('list_ingestion_streams', request, OpenSearchServerlessListIngestionStreamsResponse)

    async def list_lifecycle_policies(
        self,
        request: OpenSearchServerlessListLifecyclePoliciesRequest,
    ) -> OpenSearchServerlessListLifecyclePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_lifecycle_policies, request, OpenSearchServerlessListLifecyclePoliciesResponse)

    async def list_security_configs(
        self,
        request: OpenSearchServerlessListSecurityConfigsRequest,
    ) -> OpenSearchServerlessListSecurityConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_configs, request, OpenSearchServerlessListSecurityConfigsResponse)

    async def list_security_policies(
        self,
        request: OpenSearchServerlessListSecurityPoliciesRequest,
    ) -> OpenSearchServerlessListSecurityPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_security_policies, request, OpenSearchServerlessListSecurityPoliciesResponse)

    async def list_tags_for_resource(
        self,
        request: OpenSearchServerlessListTagsForResourceRequest,
    ) -> OpenSearchServerlessListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, OpenSearchServerlessListTagsForResourceResponse)

    async def list_vpc_endpoints(
        self,
        request: OpenSearchServerlessListVpcEndpointsRequest | None = None,
    ) -> OpenSearchServerlessListVpcEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_endpoints, request, OpenSearchServerlessListVpcEndpointsResponse)

    async def tag_resource(
        self,
        request: OpenSearchServerlessTagResourceRequest,
    ) -> OpenSearchServerlessTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, OpenSearchServerlessTagResourceResponse)

    async def untag_resource(
        self,
        request: OpenSearchServerlessUntagResourceRequest,
    ) -> OpenSearchServerlessUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, OpenSearchServerlessUntagResourceResponse)

    async def update_access_policy(
        self,
        request: OpenSearchServerlessUpdateAccessPolicyRequest,
    ) -> OpenSearchServerlessUpdateAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_access_policy, request, OpenSearchServerlessUpdateAccessPolicyResponse)

    async def update_account_settings(
        self,
        request: OpenSearchServerlessUpdateAccountSettingsRequest | None = None,
    ) -> OpenSearchServerlessUpdateAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_account_settings, request, OpenSearchServerlessUpdateAccountSettingsResponse)

    async def update_collection(
        self,
        request: OpenSearchServerlessUpdateCollectionRequest,
    ) -> OpenSearchServerlessUpdateCollectionResponse:
        client = self._require_client()
        return await self._execute(client.update_collection, request, OpenSearchServerlessUpdateCollectionResponse)

    async def update_collection_group(
        self,
        request: OpenSearchServerlessUpdateCollectionGroupRequest,
    ) -> OpenSearchServerlessUpdateCollectionGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_collection_group, request, OpenSearchServerlessUpdateCollectionGroupResponse)

    async def update_index(
        self,
        request: OpenSearchServerlessUpdateIndexRequest,
    ) -> OpenSearchServerlessUpdateIndexResponse:
        client = self._require_client()
        return await self._execute(client.update_index, request, OpenSearchServerlessUpdateIndexResponse)

    async def update_lifecycle_policy(
        self,
        request: OpenSearchServerlessUpdateLifecyclePolicyRequest,
    ) -> OpenSearchServerlessUpdateLifecyclePolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_lifecycle_policy, request, OpenSearchServerlessUpdateLifecyclePolicyResponse)

    async def update_security_config(
        self,
        request: OpenSearchServerlessUpdateSecurityConfigRequest,
    ) -> OpenSearchServerlessUpdateSecurityConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_security_config, request, OpenSearchServerlessUpdateSecurityConfigResponse)

    async def update_security_policy(
        self,
        request: OpenSearchServerlessUpdateSecurityPolicyRequest,
    ) -> OpenSearchServerlessUpdateSecurityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_security_policy, request, OpenSearchServerlessUpdateSecurityPolicyResponse)

    async def update_vpc_endpoint(
        self,
        request: OpenSearchServerlessUpdateVpcEndpointRequest,
    ) -> OpenSearchServerlessUpdateVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_endpoint, request, OpenSearchServerlessUpdateVpcEndpointResponse)
