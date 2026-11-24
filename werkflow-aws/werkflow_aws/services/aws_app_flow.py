from werkflow_aws.models.app_flow import (
    AppFlowCancelFlowExecutionsRequest,
    AppFlowCancelFlowExecutionsResponse,
    AppFlowCreateConnectorProfileRequest,
    AppFlowCreateConnectorProfileResponse,
    AppFlowCreateFlowRequest,
    AppFlowCreateFlowResponse,
    AppFlowDeleteConnectorProfileRequest,
    AppFlowDeleteConnectorProfileResponse,
    AppFlowDeleteFlowRequest,
    AppFlowDeleteFlowResponse,
    AppFlowDescribeConnectorEntityRequest,
    AppFlowDescribeConnectorEntityResponse,
    AppFlowDescribeConnectorProfilesRequest,
    AppFlowDescribeConnectorProfilesResponse,
    AppFlowDescribeConnectorRequest,
    AppFlowDescribeConnectorResponse,
    AppFlowDescribeConnectorsRequest,
    AppFlowDescribeConnectorsResponse,
    AppFlowDescribeFlowExecutionRecordsRequest,
    AppFlowDescribeFlowExecutionRecordsResponse,
    AppFlowDescribeFlowRequest,
    AppFlowDescribeFlowResponse,
    AppFlowListConnectorEntitiesRequest,
    AppFlowListConnectorEntitiesResponse,
    AppFlowListConnectorsRequest,
    AppFlowListConnectorsResponse,
    AppFlowListFlowsRequest,
    AppFlowListFlowsResponse,
    AppFlowListTagsForResourceRequest,
    AppFlowListTagsForResourceResponse,
    AppFlowRegisterConnectorRequest,
    AppFlowRegisterConnectorResponse,
    AppFlowResetConnectorMetadataCacheRequest,
    AppFlowResetConnectorMetadataCacheResponse,
    AppFlowStartFlowRequest,
    AppFlowStartFlowResponse,
    AppFlowStopFlowRequest,
    AppFlowStopFlowResponse,
    AppFlowTagResourceRequest,
    AppFlowTagResourceResponse,
    AppFlowUnregisterConnectorRequest,
    AppFlowUnregisterConnectorResponse,
    AppFlowUntagResourceRequest,
    AppFlowUntagResourceResponse,
    AppFlowUpdateConnectorProfileRequest,
    AppFlowUpdateConnectorProfileResponse,
    AppFlowUpdateConnectorRegistrationRequest,
    AppFlowUpdateConnectorRegistrationResponse,
    AppFlowUpdateFlowRequest,
    AppFlowUpdateFlowResponse,
)
from werkflow_aws.types.app_flow_client import AppFlowClient
from .base import AWSBaseService


class AWSAppFlow(AWSBaseService[AppFlowClient]):
    service_name = 'app-flow'
    boto3_service_name = 'appflow'

    def __init__(self) -> None:
        super().__init__(service_name='app-flow', boto3_service_name='appflow')

    async def cancel_flow_executions(
        self,
        request: AppFlowCancelFlowExecutionsRequest,
    ) -> AppFlowCancelFlowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_flow_executions, request, AppFlowCancelFlowExecutionsResponse)

    async def create_connector_profile(
        self,
        request: AppFlowCreateConnectorProfileRequest,
    ) -> AppFlowCreateConnectorProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_connector_profile, request, AppFlowCreateConnectorProfileResponse)

    async def create_flow(
        self,
        request: AppFlowCreateFlowRequest,
    ) -> AppFlowCreateFlowResponse:
        client = self._require_client()
        return await self._execute(client.create_flow, request, AppFlowCreateFlowResponse)

    async def delete_connector_profile(
        self,
        request: AppFlowDeleteConnectorProfileRequest,
    ) -> AppFlowDeleteConnectorProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_connector_profile, request, AppFlowDeleteConnectorProfileResponse)

    async def delete_flow(
        self,
        request: AppFlowDeleteFlowRequest,
    ) -> AppFlowDeleteFlowResponse:
        client = self._require_client()
        return await self._execute(client.delete_flow, request, AppFlowDeleteFlowResponse)

    async def describe_connector(
        self,
        request: AppFlowDescribeConnectorRequest,
    ) -> AppFlowDescribeConnectorResponse:
        client = self._require_client()
        return await self._execute(client.describe_connector, request, AppFlowDescribeConnectorResponse)

    async def describe_connector_entity(
        self,
        request: AppFlowDescribeConnectorEntityRequest,
    ) -> AppFlowDescribeConnectorEntityResponse:
        client = self._require_client()
        return await self._execute(client.describe_connector_entity, request, AppFlowDescribeConnectorEntityResponse)

    async def describe_connector_profiles(
        self,
        request: AppFlowDescribeConnectorProfilesRequest | None = None,
    ) -> AppFlowDescribeConnectorProfilesResponse:
        client = self._require_client()
        return await self._execute(client.describe_connector_profiles, request, AppFlowDescribeConnectorProfilesResponse)

    async def describe_connectors(
        self,
        request: AppFlowDescribeConnectorsRequest | None = None,
    ) -> AppFlowDescribeConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_connectors, request, AppFlowDescribeConnectorsResponse)

    async def describe_flow(
        self,
        request: AppFlowDescribeFlowRequest,
    ) -> AppFlowDescribeFlowResponse:
        client = self._require_client()
        return await self._execute(client.describe_flow, request, AppFlowDescribeFlowResponse)

    async def describe_flow_execution_records(
        self,
        request: AppFlowDescribeFlowExecutionRecordsRequest,
    ) -> AppFlowDescribeFlowExecutionRecordsResponse:
        client = self._require_client()
        return await self._execute(client.describe_flow_execution_records, request, AppFlowDescribeFlowExecutionRecordsResponse)

    async def list_connector_entities(
        self,
        request: AppFlowListConnectorEntitiesRequest | None = None,
    ) -> AppFlowListConnectorEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_connector_entities, request, AppFlowListConnectorEntitiesResponse)

    async def list_connectors(
        self,
        request: AppFlowListConnectorsRequest | None = None,
    ) -> AppFlowListConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_connectors, request, AppFlowListConnectorsResponse)

    async def list_flows(
        self,
        request: AppFlowListFlowsRequest | None = None,
    ) -> AppFlowListFlowsResponse:
        client = self._require_client()
        return await self._execute(client.list_flows, request, AppFlowListFlowsResponse)

    async def list_tags_for_resource(
        self,
        request: AppFlowListTagsForResourceRequest,
    ) -> AppFlowListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AppFlowListTagsForResourceResponse)

    async def register_connector(
        self,
        request: AppFlowRegisterConnectorRequest | None = None,
    ) -> AppFlowRegisterConnectorResponse:
        client = self._require_client()
        return await self._execute(client.register_connector, request, AppFlowRegisterConnectorResponse)

    async def reset_connector_metadata_cache(
        self,
        request: AppFlowResetConnectorMetadataCacheRequest | None = None,
    ) -> AppFlowResetConnectorMetadataCacheResponse:
        client = self._require_client()
        return await self._execute(client.reset_connector_metadata_cache, request, AppFlowResetConnectorMetadataCacheResponse)

    async def start_flow(
        self,
        request: AppFlowStartFlowRequest,
    ) -> AppFlowStartFlowResponse:
        client = self._require_client()
        return await self._execute(client.start_flow, request, AppFlowStartFlowResponse)

    async def stop_flow(
        self,
        request: AppFlowStopFlowRequest,
    ) -> AppFlowStopFlowResponse:
        client = self._require_client()
        return await self._execute(client.stop_flow, request, AppFlowStopFlowResponse)

    async def tag_resource(
        self,
        request: AppFlowTagResourceRequest,
    ) -> AppFlowTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AppFlowTagResourceResponse)

    async def unregister_connector(
        self,
        request: AppFlowUnregisterConnectorRequest,
    ) -> AppFlowUnregisterConnectorResponse:
        client = self._require_client()
        return await self._execute(client.unregister_connector, request, AppFlowUnregisterConnectorResponse)

    async def untag_resource(
        self,
        request: AppFlowUntagResourceRequest,
    ) -> AppFlowUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AppFlowUntagResourceResponse)

    async def update_connector_profile(
        self,
        request: AppFlowUpdateConnectorProfileRequest,
    ) -> AppFlowUpdateConnectorProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_connector_profile, request, AppFlowUpdateConnectorProfileResponse)

    async def update_connector_registration(
        self,
        request: AppFlowUpdateConnectorRegistrationRequest,
    ) -> AppFlowUpdateConnectorRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.update_connector_registration, request, AppFlowUpdateConnectorRegistrationResponse)

    async def update_flow(
        self,
        request: AppFlowUpdateFlowRequest,
    ) -> AppFlowUpdateFlowResponse:
        client = self._require_client()
        return await self._execute(client.update_flow, request, AppFlowUpdateFlowResponse)
