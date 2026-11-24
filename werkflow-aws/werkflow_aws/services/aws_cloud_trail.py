from werkflow_aws.models.cloud_trail import (
    CloudTrailAddTagsRequest,
    CloudTrailAddTagsResponse,
    CloudTrailCancelQueryRequest,
    CloudTrailCancelQueryResponse,
    CloudTrailCreateChannelRequest,
    CloudTrailCreateChannelResponse,
    CloudTrailCreateDashboardRequest,
    CloudTrailCreateDashboardResponse,
    CloudTrailCreateEventDataStoreRequest,
    CloudTrailCreateEventDataStoreResponse,
    CloudTrailCreateTrailRequest,
    CloudTrailCreateTrailResponse,
    CloudTrailDeleteChannelRequest,
    CloudTrailDeleteChannelResponse,
    CloudTrailDeleteDashboardRequest,
    CloudTrailDeleteDashboardResponse,
    CloudTrailDeleteEventDataStoreRequest,
    CloudTrailDeleteEventDataStoreResponse,
    CloudTrailDeleteResourcePolicyRequest,
    CloudTrailDeleteResourcePolicyResponse,
    CloudTrailDeleteTrailRequest,
    CloudTrailDeleteTrailResponse,
    CloudTrailDeregisterOrganizationDelegatedAdminRequest,
    CloudTrailDeregisterOrganizationDelegatedAdminResponse,
    CloudTrailDescribeQueryRequest,
    CloudTrailDescribeQueryResponse,
    CloudTrailDescribeTrailsRequest,
    CloudTrailDescribeTrailsResponse,
    CloudTrailDisableFederationRequest,
    CloudTrailDisableFederationResponse,
    CloudTrailEnableFederationRequest,
    CloudTrailEnableFederationResponse,
    CloudTrailGenerateQueryRequest,
    CloudTrailGenerateQueryResponse,
    CloudTrailGetChannelRequest,
    CloudTrailGetChannelResponse,
    CloudTrailGetDashboardRequest,
    CloudTrailGetDashboardResponse,
    CloudTrailGetEventConfigurationRequest,
    CloudTrailGetEventConfigurationResponse,
    CloudTrailGetEventDataStoreRequest,
    CloudTrailGetEventDataStoreResponse,
    CloudTrailGetEventSelectorsRequest,
    CloudTrailGetEventSelectorsResponse,
    CloudTrailGetImportRequest,
    CloudTrailGetImportResponse,
    CloudTrailGetInsightSelectorsRequest,
    CloudTrailGetInsightSelectorsResponse,
    CloudTrailGetQueryResultsRequest,
    CloudTrailGetQueryResultsResponse,
    CloudTrailGetResourcePolicyRequest,
    CloudTrailGetResourcePolicyResponse,
    CloudTrailGetTrailRequest,
    CloudTrailGetTrailResponse,
    CloudTrailGetTrailStatusRequest,
    CloudTrailGetTrailStatusResponse,
    CloudTrailListChannelsRequest,
    CloudTrailListChannelsResponse,
    CloudTrailListDashboardsRequest,
    CloudTrailListDashboardsResponse,
    CloudTrailListEventDataStoresRequest,
    CloudTrailListEventDataStoresResponse,
    CloudTrailListImportFailuresRequest,
    CloudTrailListImportFailuresResponse,
    CloudTrailListImportsRequest,
    CloudTrailListImportsResponse,
    CloudTrailListInsightsDataRequest,
    CloudTrailListInsightsDataResponse,
    CloudTrailListInsightsMetricDataRequest,
    CloudTrailListInsightsMetricDataResponse,
    CloudTrailListPublicKeysRequest,
    CloudTrailListPublicKeysResponse,
    CloudTrailListQueriesRequest,
    CloudTrailListQueriesResponse,
    CloudTrailListTagsRequest,
    CloudTrailListTagsResponse,
    CloudTrailListTrailsRequest,
    CloudTrailListTrailsResponse,
    CloudTrailLookupEventsRequest,
    CloudTrailLookupEventsResponse,
    CloudTrailPutEventConfigurationRequest,
    CloudTrailPutEventConfigurationResponse,
    CloudTrailPutEventSelectorsRequest,
    CloudTrailPutEventSelectorsResponse,
    CloudTrailPutInsightSelectorsRequest,
    CloudTrailPutInsightSelectorsResponse,
    CloudTrailPutResourcePolicyRequest,
    CloudTrailPutResourcePolicyResponse,
    CloudTrailRegisterOrganizationDelegatedAdminRequest,
    CloudTrailRegisterOrganizationDelegatedAdminResponse,
    CloudTrailRemoveTagsRequest,
    CloudTrailRemoveTagsResponse,
    CloudTrailRestoreEventDataStoreRequest,
    CloudTrailRestoreEventDataStoreResponse,
    CloudTrailSearchSampleQueriesRequest,
    CloudTrailSearchSampleQueriesResponse,
    CloudTrailStartDashboardRefreshRequest,
    CloudTrailStartDashboardRefreshResponse,
    CloudTrailStartEventDataStoreIngestionRequest,
    CloudTrailStartEventDataStoreIngestionResponse,
    CloudTrailStartImportRequest,
    CloudTrailStartImportResponse,
    CloudTrailStartLoggingRequest,
    CloudTrailStartLoggingResponse,
    CloudTrailStartQueryRequest,
    CloudTrailStartQueryResponse,
    CloudTrailStopEventDataStoreIngestionRequest,
    CloudTrailStopEventDataStoreIngestionResponse,
    CloudTrailStopImportRequest,
    CloudTrailStopImportResponse,
    CloudTrailStopLoggingRequest,
    CloudTrailStopLoggingResponse,
    CloudTrailUpdateChannelRequest,
    CloudTrailUpdateChannelResponse,
    CloudTrailUpdateDashboardRequest,
    CloudTrailUpdateDashboardResponse,
    CloudTrailUpdateEventDataStoreRequest,
    CloudTrailUpdateEventDataStoreResponse,
    CloudTrailUpdateTrailRequest,
    CloudTrailUpdateTrailResponse,
)
from werkflow_aws.types.cloud_trail_client import CloudTrailClient
from .base import AWSBaseService


class AWSCloudTrail(AWSBaseService[CloudTrailClient]):
    service_name = 'cloud-trail'
    boto3_service_name = 'cloudtrail'

    def __init__(self) -> None:
        super().__init__(service_name='cloud-trail', boto3_service_name='cloudtrail')

    async def add_tags(
        self,
        request: CloudTrailAddTagsRequest,
    ) -> CloudTrailAddTagsResponse:
        client = self._require_client()
        return await self._execute(client.add_tags, request, CloudTrailAddTagsResponse)

    async def cancel_query(
        self,
        request: CloudTrailCancelQueryRequest,
    ) -> CloudTrailCancelQueryResponse:
        client = self._require_client()
        return await self._execute(client.cancel_query, request, CloudTrailCancelQueryResponse)

    async def create_channel(
        self,
        request: CloudTrailCreateChannelRequest,
    ) -> CloudTrailCreateChannelResponse:
        client = self._require_client()
        return await self._execute(client.create_channel, request, CloudTrailCreateChannelResponse)

    async def create_dashboard(
        self,
        request: CloudTrailCreateDashboardRequest,
    ) -> CloudTrailCreateDashboardResponse:
        client = self._require_client()
        return await self._execute(client.create_dashboard, request, CloudTrailCreateDashboardResponse)

    async def create_event_data_store(
        self,
        request: CloudTrailCreateEventDataStoreRequest,
    ) -> CloudTrailCreateEventDataStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_event_data_store, request, CloudTrailCreateEventDataStoreResponse)

    async def create_trail(
        self,
        request: CloudTrailCreateTrailRequest,
    ) -> CloudTrailCreateTrailResponse:
        client = self._require_client()
        return await self._execute(client.create_trail, request, CloudTrailCreateTrailResponse)

    async def delete_channel(
        self,
        request: CloudTrailDeleteChannelRequest,
    ) -> CloudTrailDeleteChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_channel, request, CloudTrailDeleteChannelResponse)

    async def delete_dashboard(
        self,
        request: CloudTrailDeleteDashboardRequest,
    ) -> CloudTrailDeleteDashboardResponse:
        client = self._require_client()
        return await self._execute(client.delete_dashboard, request, CloudTrailDeleteDashboardResponse)

    async def delete_event_data_store(
        self,
        request: CloudTrailDeleteEventDataStoreRequest,
    ) -> CloudTrailDeleteEventDataStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_data_store, request, CloudTrailDeleteEventDataStoreResponse)

    async def delete_resource_policy(
        self,
        request: CloudTrailDeleteResourcePolicyRequest,
    ) -> CloudTrailDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, CloudTrailDeleteResourcePolicyResponse)

    async def delete_trail(
        self,
        request: CloudTrailDeleteTrailRequest,
    ) -> CloudTrailDeleteTrailResponse:
        client = self._require_client()
        return await self._execute(client.delete_trail, request, CloudTrailDeleteTrailResponse)

    async def deregister_organization_delegated_admin(
        self,
        request: CloudTrailDeregisterOrganizationDelegatedAdminRequest,
    ) -> CloudTrailDeregisterOrganizationDelegatedAdminResponse:
        client = self._require_client()
        return await self._execute(client.deregister_organization_delegated_admin, request, CloudTrailDeregisterOrganizationDelegatedAdminResponse)

    async def describe_query(
        self,
        request: CloudTrailDescribeQueryRequest | None = None,
    ) -> CloudTrailDescribeQueryResponse:
        client = self._require_client()
        return await self._execute(client.describe_query, request, CloudTrailDescribeQueryResponse)

    async def describe_trails(
        self,
        request: CloudTrailDescribeTrailsRequest | None = None,
    ) -> CloudTrailDescribeTrailsResponse:
        client = self._require_client()
        return await self._execute(client.describe_trails, request, CloudTrailDescribeTrailsResponse)

    async def disable_federation(
        self,
        request: CloudTrailDisableFederationRequest,
    ) -> CloudTrailDisableFederationResponse:
        client = self._require_client()
        return await self._execute(client.disable_federation, request, CloudTrailDisableFederationResponse)

    async def enable_federation(
        self,
        request: CloudTrailEnableFederationRequest,
    ) -> CloudTrailEnableFederationResponse:
        client = self._require_client()
        return await self._execute(client.enable_federation, request, CloudTrailEnableFederationResponse)

    async def generate_query(
        self,
        request: CloudTrailGenerateQueryRequest,
    ) -> CloudTrailGenerateQueryResponse:
        client = self._require_client()
        return await self._execute(client.generate_query, request, CloudTrailGenerateQueryResponse)

    async def get_channel(
        self,
        request: CloudTrailGetChannelRequest,
    ) -> CloudTrailGetChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_channel, request, CloudTrailGetChannelResponse)

    async def get_dashboard(
        self,
        request: CloudTrailGetDashboardRequest,
    ) -> CloudTrailGetDashboardResponse:
        client = self._require_client()
        return await self._execute(client.get_dashboard, request, CloudTrailGetDashboardResponse)

    async def get_event_configuration(
        self,
        request: CloudTrailGetEventConfigurationRequest | None = None,
    ) -> CloudTrailGetEventConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_event_configuration, request, CloudTrailGetEventConfigurationResponse)

    async def get_event_data_store(
        self,
        request: CloudTrailGetEventDataStoreRequest,
    ) -> CloudTrailGetEventDataStoreResponse:
        client = self._require_client()
        return await self._execute(client.get_event_data_store, request, CloudTrailGetEventDataStoreResponse)

    async def get_event_selectors(
        self,
        request: CloudTrailGetEventSelectorsRequest,
    ) -> CloudTrailGetEventSelectorsResponse:
        client = self._require_client()
        return await self._execute(client.get_event_selectors, request, CloudTrailGetEventSelectorsResponse)

    async def get_import(
        self,
        request: CloudTrailGetImportRequest,
    ) -> CloudTrailGetImportResponse:
        client = self._require_client()
        return await self._execute(client.get_import, request, CloudTrailGetImportResponse)

    async def get_insight_selectors(
        self,
        request: CloudTrailGetInsightSelectorsRequest | None = None,
    ) -> CloudTrailGetInsightSelectorsResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_selectors, request, CloudTrailGetInsightSelectorsResponse)

    async def get_query_results(
        self,
        request: CloudTrailGetQueryResultsRequest,
    ) -> CloudTrailGetQueryResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_query_results, request, CloudTrailGetQueryResultsResponse)

    async def get_resource_policy(
        self,
        request: CloudTrailGetResourcePolicyRequest,
    ) -> CloudTrailGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, CloudTrailGetResourcePolicyResponse)

    async def get_trail(
        self,
        request: CloudTrailGetTrailRequest,
    ) -> CloudTrailGetTrailResponse:
        client = self._require_client()
        return await self._execute(client.get_trail, request, CloudTrailGetTrailResponse)

    async def get_trail_status(
        self,
        request: CloudTrailGetTrailStatusRequest,
    ) -> CloudTrailGetTrailStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_trail_status, request, CloudTrailGetTrailStatusResponse)

    async def list_channels(
        self,
        request: CloudTrailListChannelsRequest | None = None,
    ) -> CloudTrailListChannelsResponse:
        client = self._require_client()
        return await self._execute(client.list_channels, request, CloudTrailListChannelsResponse)

    async def list_dashboards(
        self,
        request: CloudTrailListDashboardsRequest | None = None,
    ) -> CloudTrailListDashboardsResponse:
        client = self._require_client()
        return await self._execute(client.list_dashboards, request, CloudTrailListDashboardsResponse)

    async def list_event_data_stores(
        self,
        request: CloudTrailListEventDataStoresRequest | None = None,
    ) -> CloudTrailListEventDataStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_event_data_stores, request, CloudTrailListEventDataStoresResponse)

    async def list_import_failures(
        self,
        request: CloudTrailListImportFailuresRequest,
    ) -> CloudTrailListImportFailuresResponse:
        client = self._require_client()
        return await self._execute(client.list_import_failures, request, CloudTrailListImportFailuresResponse)

    async def list_import_failures_paginated(
        self,
        request: CloudTrailListImportFailuresRequest,
    ) -> list[CloudTrailListImportFailuresResponse]:
        return await self._paginate('list_import_failures', request, CloudTrailListImportFailuresResponse)

    async def list_imports(
        self,
        request: CloudTrailListImportsRequest | None = None,
    ) -> CloudTrailListImportsResponse:
        client = self._require_client()
        return await self._execute(client.list_imports, request, CloudTrailListImportsResponse)

    async def list_imports_paginated(
        self,
        request: CloudTrailListImportsRequest | None = None,
    ) -> list[CloudTrailListImportsResponse]:
        return await self._paginate('list_imports', request, CloudTrailListImportsResponse)

    async def list_insights_data(
        self,
        request: CloudTrailListInsightsDataRequest,
    ) -> CloudTrailListInsightsDataResponse:
        client = self._require_client()
        return await self._execute(client.list_insights_data, request, CloudTrailListInsightsDataResponse)

    async def list_insights_data_paginated(
        self,
        request: CloudTrailListInsightsDataRequest,
    ) -> list[CloudTrailListInsightsDataResponse]:
        return await self._paginate('list_insights_data', request, CloudTrailListInsightsDataResponse)

    async def list_insights_metric_data(
        self,
        request: CloudTrailListInsightsMetricDataRequest,
    ) -> CloudTrailListInsightsMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.list_insights_metric_data, request, CloudTrailListInsightsMetricDataResponse)

    async def list_public_keys(
        self,
        request: CloudTrailListPublicKeysRequest | None = None,
    ) -> CloudTrailListPublicKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_public_keys, request, CloudTrailListPublicKeysResponse)

    async def list_public_keys_paginated(
        self,
        request: CloudTrailListPublicKeysRequest | None = None,
    ) -> list[CloudTrailListPublicKeysResponse]:
        return await self._paginate('list_public_keys', request, CloudTrailListPublicKeysResponse)

    async def list_queries(
        self,
        request: CloudTrailListQueriesRequest,
    ) -> CloudTrailListQueriesResponse:
        client = self._require_client()
        return await self._execute(client.list_queries, request, CloudTrailListQueriesResponse)

    async def list_tags(
        self,
        request: CloudTrailListTagsRequest,
    ) -> CloudTrailListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, CloudTrailListTagsResponse)

    async def list_tags_paginated(
        self,
        request: CloudTrailListTagsRequest,
    ) -> list[CloudTrailListTagsResponse]:
        return await self._paginate('list_tags', request, CloudTrailListTagsResponse)

    async def list_trails(
        self,
        request: CloudTrailListTrailsRequest | None = None,
    ) -> CloudTrailListTrailsResponse:
        client = self._require_client()
        return await self._execute(client.list_trails, request, CloudTrailListTrailsResponse)

    async def list_trails_paginated(
        self,
        request: CloudTrailListTrailsRequest | None = None,
    ) -> list[CloudTrailListTrailsResponse]:
        return await self._paginate('list_trails', request, CloudTrailListTrailsResponse)

    async def lookup_events(
        self,
        request: CloudTrailLookupEventsRequest | None = None,
    ) -> CloudTrailLookupEventsResponse:
        client = self._require_client()
        return await self._execute(client.lookup_events, request, CloudTrailLookupEventsResponse)

    async def lookup_events_paginated(
        self,
        request: CloudTrailLookupEventsRequest | None = None,
    ) -> list[CloudTrailLookupEventsResponse]:
        return await self._paginate('lookup_events', request, CloudTrailLookupEventsResponse)

    async def put_event_configuration(
        self,
        request: CloudTrailPutEventConfigurationRequest | None = None,
    ) -> CloudTrailPutEventConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_event_configuration, request, CloudTrailPutEventConfigurationResponse)

    async def put_event_selectors(
        self,
        request: CloudTrailPutEventSelectorsRequest,
    ) -> CloudTrailPutEventSelectorsResponse:
        client = self._require_client()
        return await self._execute(client.put_event_selectors, request, CloudTrailPutEventSelectorsResponse)

    async def put_insight_selectors(
        self,
        request: CloudTrailPutInsightSelectorsRequest,
    ) -> CloudTrailPutInsightSelectorsResponse:
        client = self._require_client()
        return await self._execute(client.put_insight_selectors, request, CloudTrailPutInsightSelectorsResponse)

    async def put_resource_policy(
        self,
        request: CloudTrailPutResourcePolicyRequest,
    ) -> CloudTrailPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, CloudTrailPutResourcePolicyResponse)

    async def register_organization_delegated_admin(
        self,
        request: CloudTrailRegisterOrganizationDelegatedAdminRequest,
    ) -> CloudTrailRegisterOrganizationDelegatedAdminResponse:
        client = self._require_client()
        return await self._execute(client.register_organization_delegated_admin, request, CloudTrailRegisterOrganizationDelegatedAdminResponse)

    async def remove_tags(
        self,
        request: CloudTrailRemoveTagsRequest,
    ) -> CloudTrailRemoveTagsResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags, request, CloudTrailRemoveTagsResponse)

    async def restore_event_data_store(
        self,
        request: CloudTrailRestoreEventDataStoreRequest,
    ) -> CloudTrailRestoreEventDataStoreResponse:
        client = self._require_client()
        return await self._execute(client.restore_event_data_store, request, CloudTrailRestoreEventDataStoreResponse)

    async def search_sample_queries(
        self,
        request: CloudTrailSearchSampleQueriesRequest,
    ) -> CloudTrailSearchSampleQueriesResponse:
        client = self._require_client()
        return await self._execute(client.search_sample_queries, request, CloudTrailSearchSampleQueriesResponse)

    async def start_dashboard_refresh(
        self,
        request: CloudTrailStartDashboardRefreshRequest,
    ) -> CloudTrailStartDashboardRefreshResponse:
        client = self._require_client()
        return await self._execute(client.start_dashboard_refresh, request, CloudTrailStartDashboardRefreshResponse)

    async def start_event_data_store_ingestion(
        self,
        request: CloudTrailStartEventDataStoreIngestionRequest,
    ) -> CloudTrailStartEventDataStoreIngestionResponse:
        client = self._require_client()
        return await self._execute(client.start_event_data_store_ingestion, request, CloudTrailStartEventDataStoreIngestionResponse)

    async def start_import(
        self,
        request: CloudTrailStartImportRequest | None = None,
    ) -> CloudTrailStartImportResponse:
        client = self._require_client()
        return await self._execute(client.start_import, request, CloudTrailStartImportResponse)

    async def start_logging(
        self,
        request: CloudTrailStartLoggingRequest,
    ) -> CloudTrailStartLoggingResponse:
        client = self._require_client()
        return await self._execute(client.start_logging, request, CloudTrailStartLoggingResponse)

    async def start_query(
        self,
        request: CloudTrailStartQueryRequest | None = None,
    ) -> CloudTrailStartQueryResponse:
        client = self._require_client()
        return await self._execute(client.start_query, request, CloudTrailStartQueryResponse)

    async def stop_event_data_store_ingestion(
        self,
        request: CloudTrailStopEventDataStoreIngestionRequest,
    ) -> CloudTrailStopEventDataStoreIngestionResponse:
        client = self._require_client()
        return await self._execute(client.stop_event_data_store_ingestion, request, CloudTrailStopEventDataStoreIngestionResponse)

    async def stop_import(
        self,
        request: CloudTrailStopImportRequest,
    ) -> CloudTrailStopImportResponse:
        client = self._require_client()
        return await self._execute(client.stop_import, request, CloudTrailStopImportResponse)

    async def stop_logging(
        self,
        request: CloudTrailStopLoggingRequest,
    ) -> CloudTrailStopLoggingResponse:
        client = self._require_client()
        return await self._execute(client.stop_logging, request, CloudTrailStopLoggingResponse)

    async def update_channel(
        self,
        request: CloudTrailUpdateChannelRequest,
    ) -> CloudTrailUpdateChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_channel, request, CloudTrailUpdateChannelResponse)

    async def update_dashboard(
        self,
        request: CloudTrailUpdateDashboardRequest,
    ) -> CloudTrailUpdateDashboardResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboard, request, CloudTrailUpdateDashboardResponse)

    async def update_event_data_store(
        self,
        request: CloudTrailUpdateEventDataStoreRequest,
    ) -> CloudTrailUpdateEventDataStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_event_data_store, request, CloudTrailUpdateEventDataStoreResponse)

    async def update_trail(
        self,
        request: CloudTrailUpdateTrailRequest,
    ) -> CloudTrailUpdateTrailResponse:
        client = self._require_client()
        return await self._execute(client.update_trail, request, CloudTrailUpdateTrailResponse)
