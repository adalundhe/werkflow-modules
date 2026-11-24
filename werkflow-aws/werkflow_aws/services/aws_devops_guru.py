from werkflow_aws.models.devops_guru import (
    DevOpsGuruAddNotificationChannelRequest,
    DevOpsGuruAddNotificationChannelResponse,
    DevOpsGuruDeleteInsightRequest,
    DevOpsGuruDeleteInsightResponse,
    DevOpsGuruDescribeAccountHealthRequest,
    DevOpsGuruDescribeAccountHealthResponse,
    DevOpsGuruDescribeAccountOverviewRequest,
    DevOpsGuruDescribeAccountOverviewResponse,
    DevOpsGuruDescribeAnomalyRequest,
    DevOpsGuruDescribeAnomalyResponse,
    DevOpsGuruDescribeEventSourcesConfigRequest,
    DevOpsGuruDescribeEventSourcesConfigResponse,
    DevOpsGuruDescribeFeedbackRequest,
    DevOpsGuruDescribeFeedbackResponse,
    DevOpsGuruDescribeInsightRequest,
    DevOpsGuruDescribeInsightResponse,
    DevOpsGuruDescribeOrganizationHealthRequest,
    DevOpsGuruDescribeOrganizationHealthResponse,
    DevOpsGuruDescribeOrganizationOverviewRequest,
    DevOpsGuruDescribeOrganizationOverviewResponse,
    DevOpsGuruDescribeOrganizationResourceCollectionHealthRequest,
    DevOpsGuruDescribeOrganizationResourceCollectionHealthResponse,
    DevOpsGuruDescribeResourceCollectionHealthRequest,
    DevOpsGuruDescribeResourceCollectionHealthResponse,
    DevOpsGuruDescribeServiceIntegrationRequest,
    DevOpsGuruDescribeServiceIntegrationResponse,
    DevOpsGuruGetCostEstimationRequest,
    DevOpsGuruGetCostEstimationResponse,
    DevOpsGuruGetResourceCollectionRequest,
    DevOpsGuruGetResourceCollectionResponse,
    DevOpsGuruListAnomaliesForInsightRequest,
    DevOpsGuruListAnomaliesForInsightResponse,
    DevOpsGuruListAnomalousLogGroupsRequest,
    DevOpsGuruListAnomalousLogGroupsResponse,
    DevOpsGuruListEventsRequest,
    DevOpsGuruListEventsResponse,
    DevOpsGuruListInsightsRequest,
    DevOpsGuruListInsightsResponse,
    DevOpsGuruListMonitoredResourcesRequest,
    DevOpsGuruListMonitoredResourcesResponse,
    DevOpsGuruListNotificationChannelsRequest,
    DevOpsGuruListNotificationChannelsResponse,
    DevOpsGuruListOrganizationInsightsRequest,
    DevOpsGuruListOrganizationInsightsResponse,
    DevOpsGuruListRecommendationsRequest,
    DevOpsGuruListRecommendationsResponse,
    DevOpsGuruPutFeedbackRequest,
    DevOpsGuruPutFeedbackResponse,
    DevOpsGuruRemoveNotificationChannelRequest,
    DevOpsGuruRemoveNotificationChannelResponse,
    DevOpsGuruSearchInsightsRequest,
    DevOpsGuruSearchInsightsResponse,
    DevOpsGuruSearchOrganizationInsightsRequest,
    DevOpsGuruSearchOrganizationInsightsResponse,
    DevOpsGuruStartCostEstimationRequest,
    DevOpsGuruStartCostEstimationResponse,
    DevOpsGuruUpdateEventSourcesConfigRequest,
    DevOpsGuruUpdateEventSourcesConfigResponse,
    DevOpsGuruUpdateResourceCollectionRequest,
    DevOpsGuruUpdateResourceCollectionResponse,
    DevOpsGuruUpdateServiceIntegrationRequest,
    DevOpsGuruUpdateServiceIntegrationResponse,
)
from werkflow_aws.types.devops_guru_client import DevOpsGuruClient
from .base import AWSBaseService


class AWSDevOpsGuru(AWSBaseService[DevOpsGuruClient]):
    service_name = 'devops-guru'
    boto3_service_name = 'devops-guru'

    def __init__(self) -> None:
        super().__init__(service_name='devops-guru', boto3_service_name='devops-guru')

    async def add_notification_channel(
        self,
        request: DevOpsGuruAddNotificationChannelRequest,
    ) -> DevOpsGuruAddNotificationChannelResponse:
        client = self._require_client()
        return await self._execute(client.add_notification_channel, request, DevOpsGuruAddNotificationChannelResponse)

    async def delete_insight(
        self,
        request: DevOpsGuruDeleteInsightRequest,
    ) -> DevOpsGuruDeleteInsightResponse:
        client = self._require_client()
        return await self._execute(client.delete_insight, request, DevOpsGuruDeleteInsightResponse)

    async def describe_account_health(
        self,
        request: DevOpsGuruDescribeAccountHealthRequest | None = None,
    ) -> DevOpsGuruDescribeAccountHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_health, request, DevOpsGuruDescribeAccountHealthResponse)

    async def describe_account_overview(
        self,
        request: DevOpsGuruDescribeAccountOverviewRequest,
    ) -> DevOpsGuruDescribeAccountOverviewResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_overview, request, DevOpsGuruDescribeAccountOverviewResponse)

    async def describe_anomaly(
        self,
        request: DevOpsGuruDescribeAnomalyRequest,
    ) -> DevOpsGuruDescribeAnomalyResponse:
        client = self._require_client()
        return await self._execute(client.describe_anomaly, request, DevOpsGuruDescribeAnomalyResponse)

    async def describe_event_sources_config(
        self,
        request: DevOpsGuruDescribeEventSourcesConfigRequest | None = None,
    ) -> DevOpsGuruDescribeEventSourcesConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_sources_config, request, DevOpsGuruDescribeEventSourcesConfigResponse)

    async def describe_feedback(
        self,
        request: DevOpsGuruDescribeFeedbackRequest | None = None,
    ) -> DevOpsGuruDescribeFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.describe_feedback, request, DevOpsGuruDescribeFeedbackResponse)

    async def describe_insight(
        self,
        request: DevOpsGuruDescribeInsightRequest,
    ) -> DevOpsGuruDescribeInsightResponse:
        client = self._require_client()
        return await self._execute(client.describe_insight, request, DevOpsGuruDescribeInsightResponse)

    async def describe_organization_health(
        self,
        request: DevOpsGuruDescribeOrganizationHealthRequest | None = None,
    ) -> DevOpsGuruDescribeOrganizationHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_health, request, DevOpsGuruDescribeOrganizationHealthResponse)

    async def describe_organization_overview(
        self,
        request: DevOpsGuruDescribeOrganizationOverviewRequest,
    ) -> DevOpsGuruDescribeOrganizationOverviewResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_overview, request, DevOpsGuruDescribeOrganizationOverviewResponse)

    async def describe_organization_resource_collection_health(
        self,
        request: DevOpsGuruDescribeOrganizationResourceCollectionHealthRequest,
    ) -> DevOpsGuruDescribeOrganizationResourceCollectionHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_resource_collection_health, request, DevOpsGuruDescribeOrganizationResourceCollectionHealthResponse)

    async def describe_organization_resource_collection_health_paginated(
        self,
        request: DevOpsGuruDescribeOrganizationResourceCollectionHealthRequest,
    ) -> list[DevOpsGuruDescribeOrganizationResourceCollectionHealthResponse]:
        return await self._paginate('describe_organization_resource_collection_health', request, DevOpsGuruDescribeOrganizationResourceCollectionHealthResponse)

    async def describe_resource_collection_health(
        self,
        request: DevOpsGuruDescribeResourceCollectionHealthRequest,
    ) -> DevOpsGuruDescribeResourceCollectionHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_collection_health, request, DevOpsGuruDescribeResourceCollectionHealthResponse)

    async def describe_resource_collection_health_paginated(
        self,
        request: DevOpsGuruDescribeResourceCollectionHealthRequest,
    ) -> list[DevOpsGuruDescribeResourceCollectionHealthResponse]:
        return await self._paginate('describe_resource_collection_health', request, DevOpsGuruDescribeResourceCollectionHealthResponse)

    async def describe_service_integration(
        self,
        request: DevOpsGuruDescribeServiceIntegrationRequest | None = None,
    ) -> DevOpsGuruDescribeServiceIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_integration, request, DevOpsGuruDescribeServiceIntegrationResponse)

    async def get_cost_estimation(
        self,
        request: DevOpsGuruGetCostEstimationRequest | None = None,
    ) -> DevOpsGuruGetCostEstimationResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_estimation, request, DevOpsGuruGetCostEstimationResponse)

    async def get_cost_estimation_paginated(
        self,
        request: DevOpsGuruGetCostEstimationRequest | None = None,
    ) -> list[DevOpsGuruGetCostEstimationResponse]:
        return await self._paginate('get_cost_estimation', request, DevOpsGuruGetCostEstimationResponse)

    async def get_resource_collection(
        self,
        request: DevOpsGuruGetResourceCollectionRequest,
    ) -> DevOpsGuruGetResourceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_collection, request, DevOpsGuruGetResourceCollectionResponse)

    async def get_resource_collection_paginated(
        self,
        request: DevOpsGuruGetResourceCollectionRequest,
    ) -> list[DevOpsGuruGetResourceCollectionResponse]:
        return await self._paginate('get_resource_collection', request, DevOpsGuruGetResourceCollectionResponse)

    async def list_anomalies_for_insight(
        self,
        request: DevOpsGuruListAnomaliesForInsightRequest,
    ) -> DevOpsGuruListAnomaliesForInsightResponse:
        client = self._require_client()
        return await self._execute(client.list_anomalies_for_insight, request, DevOpsGuruListAnomaliesForInsightResponse)

    async def list_anomalies_for_insight_paginated(
        self,
        request: DevOpsGuruListAnomaliesForInsightRequest,
    ) -> list[DevOpsGuruListAnomaliesForInsightResponse]:
        return await self._paginate('list_anomalies_for_insight', request, DevOpsGuruListAnomaliesForInsightResponse)

    async def list_anomalous_log_groups(
        self,
        request: DevOpsGuruListAnomalousLogGroupsRequest,
    ) -> DevOpsGuruListAnomalousLogGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_anomalous_log_groups, request, DevOpsGuruListAnomalousLogGroupsResponse)

    async def list_anomalous_log_groups_paginated(
        self,
        request: DevOpsGuruListAnomalousLogGroupsRequest,
    ) -> list[DevOpsGuruListAnomalousLogGroupsResponse]:
        return await self._paginate('list_anomalous_log_groups', request, DevOpsGuruListAnomalousLogGroupsResponse)

    async def list_events(
        self,
        request: DevOpsGuruListEventsRequest,
    ) -> DevOpsGuruListEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_events, request, DevOpsGuruListEventsResponse)

    async def list_events_paginated(
        self,
        request: DevOpsGuruListEventsRequest,
    ) -> list[DevOpsGuruListEventsResponse]:
        return await self._paginate('list_events', request, DevOpsGuruListEventsResponse)

    async def list_insights(
        self,
        request: DevOpsGuruListInsightsRequest,
    ) -> DevOpsGuruListInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_insights, request, DevOpsGuruListInsightsResponse)

    async def list_insights_paginated(
        self,
        request: DevOpsGuruListInsightsRequest,
    ) -> list[DevOpsGuruListInsightsResponse]:
        return await self._paginate('list_insights', request, DevOpsGuruListInsightsResponse)

    async def list_monitored_resources(
        self,
        request: DevOpsGuruListMonitoredResourcesRequest | None = None,
    ) -> DevOpsGuruListMonitoredResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_monitored_resources, request, DevOpsGuruListMonitoredResourcesResponse)

    async def list_monitored_resources_paginated(
        self,
        request: DevOpsGuruListMonitoredResourcesRequest | None = None,
    ) -> list[DevOpsGuruListMonitoredResourcesResponse]:
        return await self._paginate('list_monitored_resources', request, DevOpsGuruListMonitoredResourcesResponse)

    async def list_notification_channels(
        self,
        request: DevOpsGuruListNotificationChannelsRequest | None = None,
    ) -> DevOpsGuruListNotificationChannelsResponse:
        client = self._require_client()
        return await self._execute(client.list_notification_channels, request, DevOpsGuruListNotificationChannelsResponse)

    async def list_notification_channels_paginated(
        self,
        request: DevOpsGuruListNotificationChannelsRequest | None = None,
    ) -> list[DevOpsGuruListNotificationChannelsResponse]:
        return await self._paginate('list_notification_channels', request, DevOpsGuruListNotificationChannelsResponse)

    async def list_organization_insights(
        self,
        request: DevOpsGuruListOrganizationInsightsRequest,
    ) -> DevOpsGuruListOrganizationInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_insights, request, DevOpsGuruListOrganizationInsightsResponse)

    async def list_organization_insights_paginated(
        self,
        request: DevOpsGuruListOrganizationInsightsRequest,
    ) -> list[DevOpsGuruListOrganizationInsightsResponse]:
        return await self._paginate('list_organization_insights', request, DevOpsGuruListOrganizationInsightsResponse)

    async def list_recommendations(
        self,
        request: DevOpsGuruListRecommendationsRequest,
    ) -> DevOpsGuruListRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendations, request, DevOpsGuruListRecommendationsResponse)

    async def list_recommendations_paginated(
        self,
        request: DevOpsGuruListRecommendationsRequest,
    ) -> list[DevOpsGuruListRecommendationsResponse]:
        return await self._paginate('list_recommendations', request, DevOpsGuruListRecommendationsResponse)

    async def put_feedback(
        self,
        request: DevOpsGuruPutFeedbackRequest | None = None,
    ) -> DevOpsGuruPutFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.put_feedback, request, DevOpsGuruPutFeedbackResponse)

    async def remove_notification_channel(
        self,
        request: DevOpsGuruRemoveNotificationChannelRequest,
    ) -> DevOpsGuruRemoveNotificationChannelResponse:
        client = self._require_client()
        return await self._execute(client.remove_notification_channel, request, DevOpsGuruRemoveNotificationChannelResponse)

    async def search_insights(
        self,
        request: DevOpsGuruSearchInsightsRequest,
    ) -> DevOpsGuruSearchInsightsResponse:
        client = self._require_client()
        return await self._execute(client.search_insights, request, DevOpsGuruSearchInsightsResponse)

    async def search_insights_paginated(
        self,
        request: DevOpsGuruSearchInsightsRequest,
    ) -> list[DevOpsGuruSearchInsightsResponse]:
        return await self._paginate('search_insights', request, DevOpsGuruSearchInsightsResponse)

    async def search_organization_insights(
        self,
        request: DevOpsGuruSearchOrganizationInsightsRequest,
    ) -> DevOpsGuruSearchOrganizationInsightsResponse:
        client = self._require_client()
        return await self._execute(client.search_organization_insights, request, DevOpsGuruSearchOrganizationInsightsResponse)

    async def search_organization_insights_paginated(
        self,
        request: DevOpsGuruSearchOrganizationInsightsRequest,
    ) -> list[DevOpsGuruSearchOrganizationInsightsResponse]:
        return await self._paginate('search_organization_insights', request, DevOpsGuruSearchOrganizationInsightsResponse)

    async def start_cost_estimation(
        self,
        request: DevOpsGuruStartCostEstimationRequest,
    ) -> DevOpsGuruStartCostEstimationResponse:
        client = self._require_client()
        return await self._execute(client.start_cost_estimation, request, DevOpsGuruStartCostEstimationResponse)

    async def update_event_sources_config(
        self,
        request: DevOpsGuruUpdateEventSourcesConfigRequest | None = None,
    ) -> DevOpsGuruUpdateEventSourcesConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_event_sources_config, request, DevOpsGuruUpdateEventSourcesConfigResponse)

    async def update_resource_collection(
        self,
        request: DevOpsGuruUpdateResourceCollectionRequest,
    ) -> DevOpsGuruUpdateResourceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_collection, request, DevOpsGuruUpdateResourceCollectionResponse)

    async def update_service_integration(
        self,
        request: DevOpsGuruUpdateServiceIntegrationRequest,
    ) -> DevOpsGuruUpdateServiceIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.update_service_integration, request, DevOpsGuruUpdateServiceIntegrationResponse)
