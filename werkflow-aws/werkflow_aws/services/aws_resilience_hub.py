from werkflow_aws.models.resilience_hub import (
    ResilienceHubAcceptResourceGroupingRecommendationsRequest,
    ResilienceHubAcceptResourceGroupingRecommendationsResponse,
    ResilienceHubAddDraftAppVersionResourceMappingsRequest,
    ResilienceHubAddDraftAppVersionResourceMappingsResponse,
    ResilienceHubBatchUpdateRecommendationStatusRequest,
    ResilienceHubBatchUpdateRecommendationStatusResponse,
    ResilienceHubCreateAppRequest,
    ResilienceHubCreateAppResponse,
    ResilienceHubCreateAppVersionAppComponentRequest,
    ResilienceHubCreateAppVersionAppComponentResponse,
    ResilienceHubCreateAppVersionResourceRequest,
    ResilienceHubCreateAppVersionResourceResponse,
    ResilienceHubCreateRecommendationTemplateRequest,
    ResilienceHubCreateRecommendationTemplateResponse,
    ResilienceHubCreateResiliencyPolicyRequest,
    ResilienceHubCreateResiliencyPolicyResponse,
    ResilienceHubDeleteAppAssessmentRequest,
    ResilienceHubDeleteAppAssessmentResponse,
    ResilienceHubDeleteAppInputSourceRequest,
    ResilienceHubDeleteAppInputSourceResponse,
    ResilienceHubDeleteAppRequest,
    ResilienceHubDeleteAppResponse,
    ResilienceHubDeleteAppVersionAppComponentRequest,
    ResilienceHubDeleteAppVersionAppComponentResponse,
    ResilienceHubDeleteAppVersionResourceRequest,
    ResilienceHubDeleteAppVersionResourceResponse,
    ResilienceHubDeleteRecommendationTemplateRequest,
    ResilienceHubDeleteRecommendationTemplateResponse,
    ResilienceHubDeleteResiliencyPolicyRequest,
    ResilienceHubDeleteResiliencyPolicyResponse,
    ResilienceHubDescribeAppAssessmentRequest,
    ResilienceHubDescribeAppAssessmentResponse,
    ResilienceHubDescribeAppRequest,
    ResilienceHubDescribeAppResponse,
    ResilienceHubDescribeAppVersionAppComponentRequest,
    ResilienceHubDescribeAppVersionAppComponentResponse,
    ResilienceHubDescribeAppVersionRequest,
    ResilienceHubDescribeAppVersionResourceRequest,
    ResilienceHubDescribeAppVersionResourceResponse,
    ResilienceHubDescribeAppVersionResourcesResolutionStatusRequest,
    ResilienceHubDescribeAppVersionResourcesResolutionStatusResponse,
    ResilienceHubDescribeAppVersionResponse,
    ResilienceHubDescribeAppVersionTemplateRequest,
    ResilienceHubDescribeAppVersionTemplateResponse,
    ResilienceHubDescribeDraftAppVersionResourcesImportStatusRequest,
    ResilienceHubDescribeDraftAppVersionResourcesImportStatusResponse,
    ResilienceHubDescribeMetricsExportRequest,
    ResilienceHubDescribeMetricsExportResponse,
    ResilienceHubDescribeResiliencyPolicyRequest,
    ResilienceHubDescribeResiliencyPolicyResponse,
    ResilienceHubDescribeResourceGroupingRecommendationTaskRequest,
    ResilienceHubDescribeResourceGroupingRecommendationTaskResponse,
    ResilienceHubImportResourcesToDraftAppVersionRequest,
    ResilienceHubImportResourcesToDraftAppVersionResponse,
    ResilienceHubListAlarmRecommendationsRequest,
    ResilienceHubListAlarmRecommendationsResponse,
    ResilienceHubListAppAssessmentComplianceDriftsRequest,
    ResilienceHubListAppAssessmentComplianceDriftsResponse,
    ResilienceHubListAppAssessmentResourceDriftsRequest,
    ResilienceHubListAppAssessmentResourceDriftsResponse,
    ResilienceHubListAppAssessmentsRequest,
    ResilienceHubListAppAssessmentsResponse,
    ResilienceHubListAppComponentCompliancesRequest,
    ResilienceHubListAppComponentCompliancesResponse,
    ResilienceHubListAppComponentRecommendationsRequest,
    ResilienceHubListAppComponentRecommendationsResponse,
    ResilienceHubListAppInputSourcesRequest,
    ResilienceHubListAppInputSourcesResponse,
    ResilienceHubListAppVersionAppComponentsRequest,
    ResilienceHubListAppVersionAppComponentsResponse,
    ResilienceHubListAppVersionResourceMappingsRequest,
    ResilienceHubListAppVersionResourceMappingsResponse,
    ResilienceHubListAppVersionResourcesRequest,
    ResilienceHubListAppVersionResourcesResponse,
    ResilienceHubListAppVersionsRequest,
    ResilienceHubListAppVersionsResponse,
    ResilienceHubListAppsRequest,
    ResilienceHubListAppsResponse,
    ResilienceHubListMetricsRequest,
    ResilienceHubListMetricsResponse,
    ResilienceHubListRecommendationTemplatesRequest,
    ResilienceHubListRecommendationTemplatesResponse,
    ResilienceHubListResiliencyPoliciesRequest,
    ResilienceHubListResiliencyPoliciesResponse,
    ResilienceHubListResourceGroupingRecommendationsRequest,
    ResilienceHubListResourceGroupingRecommendationsResponse,
    ResilienceHubListSopRecommendationsRequest,
    ResilienceHubListSopRecommendationsResponse,
    ResilienceHubListSuggestedResiliencyPoliciesRequest,
    ResilienceHubListSuggestedResiliencyPoliciesResponse,
    ResilienceHubListTagsForResourceRequest,
    ResilienceHubListTagsForResourceResponse,
    ResilienceHubListTestRecommendationsRequest,
    ResilienceHubListTestRecommendationsResponse,
    ResilienceHubListUnsupportedAppVersionResourcesRequest,
    ResilienceHubListUnsupportedAppVersionResourcesResponse,
    ResilienceHubPublishAppVersionRequest,
    ResilienceHubPublishAppVersionResponse,
    ResilienceHubPutDraftAppVersionTemplateRequest,
    ResilienceHubPutDraftAppVersionTemplateResponse,
    ResilienceHubRejectResourceGroupingRecommendationsRequest,
    ResilienceHubRejectResourceGroupingRecommendationsResponse,
    ResilienceHubRemoveDraftAppVersionResourceMappingsRequest,
    ResilienceHubRemoveDraftAppVersionResourceMappingsResponse,
    ResilienceHubResolveAppVersionResourcesRequest,
    ResilienceHubResolveAppVersionResourcesResponse,
    ResilienceHubStartAppAssessmentRequest,
    ResilienceHubStartAppAssessmentResponse,
    ResilienceHubStartMetricsExportRequest,
    ResilienceHubStartMetricsExportResponse,
    ResilienceHubStartResourceGroupingRecommendationTaskRequest,
    ResilienceHubStartResourceGroupingRecommendationTaskResponse,
    ResilienceHubTagResourceRequest,
    ResilienceHubTagResourceResponse,
    ResilienceHubUntagResourceRequest,
    ResilienceHubUntagResourceResponse,
    ResilienceHubUpdateAppRequest,
    ResilienceHubUpdateAppResponse,
    ResilienceHubUpdateAppVersionAppComponentRequest,
    ResilienceHubUpdateAppVersionAppComponentResponse,
    ResilienceHubUpdateAppVersionRequest,
    ResilienceHubUpdateAppVersionResourceRequest,
    ResilienceHubUpdateAppVersionResourceResponse,
    ResilienceHubUpdateAppVersionResponse,
    ResilienceHubUpdateResiliencyPolicyRequest,
    ResilienceHubUpdateResiliencyPolicyResponse,
)
from werkflow_aws.types.resilience_hub_client import ResilienceHubClient
from .base import AWSBaseService


class AWSResilienceHub(AWSBaseService[ResilienceHubClient]):
    service_name = 'resilience-hub'
    boto3_service_name = 'resiliencehub'

    def __init__(self) -> None:
        super().__init__(service_name='resilience-hub', boto3_service_name='resiliencehub')

    async def accept_resource_grouping_recommendations(
        self,
        request: ResilienceHubAcceptResourceGroupingRecommendationsRequest,
    ) -> ResilienceHubAcceptResourceGroupingRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.accept_resource_grouping_recommendations, request, ResilienceHubAcceptResourceGroupingRecommendationsResponse)

    async def add_draft_app_version_resource_mappings(
        self,
        request: ResilienceHubAddDraftAppVersionResourceMappingsRequest,
    ) -> ResilienceHubAddDraftAppVersionResourceMappingsResponse:
        client = self._require_client()
        return await self._execute(client.add_draft_app_version_resource_mappings, request, ResilienceHubAddDraftAppVersionResourceMappingsResponse)

    async def batch_update_recommendation_status(
        self,
        request: ResilienceHubBatchUpdateRecommendationStatusRequest,
    ) -> ResilienceHubBatchUpdateRecommendationStatusResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_recommendation_status, request, ResilienceHubBatchUpdateRecommendationStatusResponse)

    async def create_app(
        self,
        request: ResilienceHubCreateAppRequest,
    ) -> ResilienceHubCreateAppResponse:
        client = self._require_client()
        return await self._execute(client.create_app, request, ResilienceHubCreateAppResponse)

    async def create_app_version_app_component(
        self,
        request: ResilienceHubCreateAppVersionAppComponentRequest,
    ) -> ResilienceHubCreateAppVersionAppComponentResponse:
        client = self._require_client()
        return await self._execute(client.create_app_version_app_component, request, ResilienceHubCreateAppVersionAppComponentResponse)

    async def create_app_version_resource(
        self,
        request: ResilienceHubCreateAppVersionResourceRequest,
    ) -> ResilienceHubCreateAppVersionResourceResponse:
        client = self._require_client()
        return await self._execute(client.create_app_version_resource, request, ResilienceHubCreateAppVersionResourceResponse)

    async def create_recommendation_template(
        self,
        request: ResilienceHubCreateRecommendationTemplateRequest,
    ) -> ResilienceHubCreateRecommendationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_recommendation_template, request, ResilienceHubCreateRecommendationTemplateResponse)

    async def create_resiliency_policy(
        self,
        request: ResilienceHubCreateResiliencyPolicyRequest,
    ) -> ResilienceHubCreateResiliencyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_resiliency_policy, request, ResilienceHubCreateResiliencyPolicyResponse)

    async def delete_app(
        self,
        request: ResilienceHubDeleteAppRequest,
    ) -> ResilienceHubDeleteAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_app, request, ResilienceHubDeleteAppResponse)

    async def delete_app_assessment(
        self,
        request: ResilienceHubDeleteAppAssessmentRequest,
    ) -> ResilienceHubDeleteAppAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_assessment, request, ResilienceHubDeleteAppAssessmentResponse)

    async def delete_app_input_source(
        self,
        request: ResilienceHubDeleteAppInputSourceRequest,
    ) -> ResilienceHubDeleteAppInputSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_input_source, request, ResilienceHubDeleteAppInputSourceResponse)

    async def delete_app_version_app_component(
        self,
        request: ResilienceHubDeleteAppVersionAppComponentRequest,
    ) -> ResilienceHubDeleteAppVersionAppComponentResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_version_app_component, request, ResilienceHubDeleteAppVersionAppComponentResponse)

    async def delete_app_version_resource(
        self,
        request: ResilienceHubDeleteAppVersionResourceRequest,
    ) -> ResilienceHubDeleteAppVersionResourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_version_resource, request, ResilienceHubDeleteAppVersionResourceResponse)

    async def delete_recommendation_template(
        self,
        request: ResilienceHubDeleteRecommendationTemplateRequest,
    ) -> ResilienceHubDeleteRecommendationTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_recommendation_template, request, ResilienceHubDeleteRecommendationTemplateResponse)

    async def delete_resiliency_policy(
        self,
        request: ResilienceHubDeleteResiliencyPolicyRequest,
    ) -> ResilienceHubDeleteResiliencyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resiliency_policy, request, ResilienceHubDeleteResiliencyPolicyResponse)

    async def describe_app(
        self,
        request: ResilienceHubDescribeAppRequest,
    ) -> ResilienceHubDescribeAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_app, request, ResilienceHubDescribeAppResponse)

    async def describe_app_assessment(
        self,
        request: ResilienceHubDescribeAppAssessmentRequest,
    ) -> ResilienceHubDescribeAppAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_assessment, request, ResilienceHubDescribeAppAssessmentResponse)

    async def describe_app_version(
        self,
        request: ResilienceHubDescribeAppVersionRequest,
    ) -> ResilienceHubDescribeAppVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_version, request, ResilienceHubDescribeAppVersionResponse)

    async def describe_app_version_app_component(
        self,
        request: ResilienceHubDescribeAppVersionAppComponentRequest,
    ) -> ResilienceHubDescribeAppVersionAppComponentResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_version_app_component, request, ResilienceHubDescribeAppVersionAppComponentResponse)

    async def describe_app_version_resource(
        self,
        request: ResilienceHubDescribeAppVersionResourceRequest,
    ) -> ResilienceHubDescribeAppVersionResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_version_resource, request, ResilienceHubDescribeAppVersionResourceResponse)

    async def describe_app_version_resources_resolution_status(
        self,
        request: ResilienceHubDescribeAppVersionResourcesResolutionStatusRequest,
    ) -> ResilienceHubDescribeAppVersionResourcesResolutionStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_version_resources_resolution_status, request, ResilienceHubDescribeAppVersionResourcesResolutionStatusResponse)

    async def describe_app_version_template(
        self,
        request: ResilienceHubDescribeAppVersionTemplateRequest,
    ) -> ResilienceHubDescribeAppVersionTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_version_template, request, ResilienceHubDescribeAppVersionTemplateResponse)

    async def describe_draft_app_version_resources_import_status(
        self,
        request: ResilienceHubDescribeDraftAppVersionResourcesImportStatusRequest,
    ) -> ResilienceHubDescribeDraftAppVersionResourcesImportStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_draft_app_version_resources_import_status, request, ResilienceHubDescribeDraftAppVersionResourcesImportStatusResponse)

    async def describe_metrics_export(
        self,
        request: ResilienceHubDescribeMetricsExportRequest,
    ) -> ResilienceHubDescribeMetricsExportResponse:
        client = self._require_client()
        return await self._execute(client.describe_metrics_export, request, ResilienceHubDescribeMetricsExportResponse)

    async def describe_resiliency_policy(
        self,
        request: ResilienceHubDescribeResiliencyPolicyRequest,
    ) -> ResilienceHubDescribeResiliencyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_resiliency_policy, request, ResilienceHubDescribeResiliencyPolicyResponse)

    async def describe_resource_grouping_recommendation_task(
        self,
        request: ResilienceHubDescribeResourceGroupingRecommendationTaskRequest,
    ) -> ResilienceHubDescribeResourceGroupingRecommendationTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_grouping_recommendation_task, request, ResilienceHubDescribeResourceGroupingRecommendationTaskResponse)

    async def import_resources_to_draft_app_version(
        self,
        request: ResilienceHubImportResourcesToDraftAppVersionRequest,
    ) -> ResilienceHubImportResourcesToDraftAppVersionResponse:
        client = self._require_client()
        return await self._execute(client.import_resources_to_draft_app_version, request, ResilienceHubImportResourcesToDraftAppVersionResponse)

    async def list_alarm_recommendations(
        self,
        request: ResilienceHubListAlarmRecommendationsRequest,
    ) -> ResilienceHubListAlarmRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_alarm_recommendations, request, ResilienceHubListAlarmRecommendationsResponse)

    async def list_app_assessment_compliance_drifts(
        self,
        request: ResilienceHubListAppAssessmentComplianceDriftsRequest,
    ) -> ResilienceHubListAppAssessmentComplianceDriftsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_assessment_compliance_drifts, request, ResilienceHubListAppAssessmentComplianceDriftsResponse)

    async def list_app_assessment_resource_drifts(
        self,
        request: ResilienceHubListAppAssessmentResourceDriftsRequest,
    ) -> ResilienceHubListAppAssessmentResourceDriftsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_assessment_resource_drifts, request, ResilienceHubListAppAssessmentResourceDriftsResponse)

    async def list_app_assessment_resource_drifts_paginated(
        self,
        request: ResilienceHubListAppAssessmentResourceDriftsRequest,
    ) -> list[ResilienceHubListAppAssessmentResourceDriftsResponse]:
        return await self._paginate('list_app_assessment_resource_drifts', request, ResilienceHubListAppAssessmentResourceDriftsResponse)

    async def list_app_assessments(
        self,
        request: ResilienceHubListAppAssessmentsRequest | None = None,
    ) -> ResilienceHubListAppAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_assessments, request, ResilienceHubListAppAssessmentsResponse)

    async def list_app_component_compliances(
        self,
        request: ResilienceHubListAppComponentCompliancesRequest,
    ) -> ResilienceHubListAppComponentCompliancesResponse:
        client = self._require_client()
        return await self._execute(client.list_app_component_compliances, request, ResilienceHubListAppComponentCompliancesResponse)

    async def list_app_component_recommendations(
        self,
        request: ResilienceHubListAppComponentRecommendationsRequest,
    ) -> ResilienceHubListAppComponentRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_component_recommendations, request, ResilienceHubListAppComponentRecommendationsResponse)

    async def list_app_input_sources(
        self,
        request: ResilienceHubListAppInputSourcesRequest,
    ) -> ResilienceHubListAppInputSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_app_input_sources, request, ResilienceHubListAppInputSourcesResponse)

    async def list_app_version_app_components(
        self,
        request: ResilienceHubListAppVersionAppComponentsRequest,
    ) -> ResilienceHubListAppVersionAppComponentsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_version_app_components, request, ResilienceHubListAppVersionAppComponentsResponse)

    async def list_app_version_resource_mappings(
        self,
        request: ResilienceHubListAppVersionResourceMappingsRequest,
    ) -> ResilienceHubListAppVersionResourceMappingsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_version_resource_mappings, request, ResilienceHubListAppVersionResourceMappingsResponse)

    async def list_app_version_resources(
        self,
        request: ResilienceHubListAppVersionResourcesRequest,
    ) -> ResilienceHubListAppVersionResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_app_version_resources, request, ResilienceHubListAppVersionResourcesResponse)

    async def list_app_versions(
        self,
        request: ResilienceHubListAppVersionsRequest,
    ) -> ResilienceHubListAppVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_versions, request, ResilienceHubListAppVersionsResponse)

    async def list_apps(
        self,
        request: ResilienceHubListAppsRequest | None = None,
    ) -> ResilienceHubListAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_apps, request, ResilienceHubListAppsResponse)

    async def list_metrics(
        self,
        request: ResilienceHubListMetricsRequest | None = None,
    ) -> ResilienceHubListMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_metrics, request, ResilienceHubListMetricsResponse)

    async def list_metrics_paginated(
        self,
        request: ResilienceHubListMetricsRequest | None = None,
    ) -> list[ResilienceHubListMetricsResponse]:
        return await self._paginate('list_metrics', request, ResilienceHubListMetricsResponse)

    async def list_recommendation_templates(
        self,
        request: ResilienceHubListRecommendationTemplatesRequest | None = None,
    ) -> ResilienceHubListRecommendationTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendation_templates, request, ResilienceHubListRecommendationTemplatesResponse)

    async def list_resiliency_policies(
        self,
        request: ResilienceHubListResiliencyPoliciesRequest | None = None,
    ) -> ResilienceHubListResiliencyPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_resiliency_policies, request, ResilienceHubListResiliencyPoliciesResponse)

    async def list_resource_grouping_recommendations(
        self,
        request: ResilienceHubListResourceGroupingRecommendationsRequest | None = None,
    ) -> ResilienceHubListResourceGroupingRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_grouping_recommendations, request, ResilienceHubListResourceGroupingRecommendationsResponse)

    async def list_resource_grouping_recommendations_paginated(
        self,
        request: ResilienceHubListResourceGroupingRecommendationsRequest | None = None,
    ) -> list[ResilienceHubListResourceGroupingRecommendationsResponse]:
        return await self._paginate('list_resource_grouping_recommendations', request, ResilienceHubListResourceGroupingRecommendationsResponse)

    async def list_sop_recommendations(
        self,
        request: ResilienceHubListSopRecommendationsRequest,
    ) -> ResilienceHubListSopRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_sop_recommendations, request, ResilienceHubListSopRecommendationsResponse)

    async def list_suggested_resiliency_policies(
        self,
        request: ResilienceHubListSuggestedResiliencyPoliciesRequest | None = None,
    ) -> ResilienceHubListSuggestedResiliencyPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_suggested_resiliency_policies, request, ResilienceHubListSuggestedResiliencyPoliciesResponse)

    async def list_tags_for_resource(
        self,
        request: ResilienceHubListTagsForResourceRequest,
    ) -> ResilienceHubListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ResilienceHubListTagsForResourceResponse)

    async def list_test_recommendations(
        self,
        request: ResilienceHubListTestRecommendationsRequest,
    ) -> ResilienceHubListTestRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_recommendations, request, ResilienceHubListTestRecommendationsResponse)

    async def list_unsupported_app_version_resources(
        self,
        request: ResilienceHubListUnsupportedAppVersionResourcesRequest,
    ) -> ResilienceHubListUnsupportedAppVersionResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_unsupported_app_version_resources, request, ResilienceHubListUnsupportedAppVersionResourcesResponse)

    async def publish_app_version(
        self,
        request: ResilienceHubPublishAppVersionRequest,
    ) -> ResilienceHubPublishAppVersionResponse:
        client = self._require_client()
        return await self._execute(client.publish_app_version, request, ResilienceHubPublishAppVersionResponse)

    async def put_draft_app_version_template(
        self,
        request: ResilienceHubPutDraftAppVersionTemplateRequest,
    ) -> ResilienceHubPutDraftAppVersionTemplateResponse:
        client = self._require_client()
        return await self._execute(client.put_draft_app_version_template, request, ResilienceHubPutDraftAppVersionTemplateResponse)

    async def reject_resource_grouping_recommendations(
        self,
        request: ResilienceHubRejectResourceGroupingRecommendationsRequest,
    ) -> ResilienceHubRejectResourceGroupingRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.reject_resource_grouping_recommendations, request, ResilienceHubRejectResourceGroupingRecommendationsResponse)

    async def remove_draft_app_version_resource_mappings(
        self,
        request: ResilienceHubRemoveDraftAppVersionResourceMappingsRequest,
    ) -> ResilienceHubRemoveDraftAppVersionResourceMappingsResponse:
        client = self._require_client()
        return await self._execute(client.remove_draft_app_version_resource_mappings, request, ResilienceHubRemoveDraftAppVersionResourceMappingsResponse)

    async def resolve_app_version_resources(
        self,
        request: ResilienceHubResolveAppVersionResourcesRequest,
    ) -> ResilienceHubResolveAppVersionResourcesResponse:
        client = self._require_client()
        return await self._execute(client.resolve_app_version_resources, request, ResilienceHubResolveAppVersionResourcesResponse)

    async def start_app_assessment(
        self,
        request: ResilienceHubStartAppAssessmentRequest,
    ) -> ResilienceHubStartAppAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.start_app_assessment, request, ResilienceHubStartAppAssessmentResponse)

    async def start_metrics_export(
        self,
        request: ResilienceHubStartMetricsExportRequest | None = None,
    ) -> ResilienceHubStartMetricsExportResponse:
        client = self._require_client()
        return await self._execute(client.start_metrics_export, request, ResilienceHubStartMetricsExportResponse)

    async def start_resource_grouping_recommendation_task(
        self,
        request: ResilienceHubStartResourceGroupingRecommendationTaskRequest,
    ) -> ResilienceHubStartResourceGroupingRecommendationTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_resource_grouping_recommendation_task, request, ResilienceHubStartResourceGroupingRecommendationTaskResponse)

    async def tag_resource(
        self,
        request: ResilienceHubTagResourceRequest,
    ) -> ResilienceHubTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ResilienceHubTagResourceResponse)

    async def untag_resource(
        self,
        request: ResilienceHubUntagResourceRequest,
    ) -> ResilienceHubUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ResilienceHubUntagResourceResponse)

    async def update_app(
        self,
        request: ResilienceHubUpdateAppRequest,
    ) -> ResilienceHubUpdateAppResponse:
        client = self._require_client()
        return await self._execute(client.update_app, request, ResilienceHubUpdateAppResponse)

    async def update_app_version(
        self,
        request: ResilienceHubUpdateAppVersionRequest,
    ) -> ResilienceHubUpdateAppVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_app_version, request, ResilienceHubUpdateAppVersionResponse)

    async def update_app_version_app_component(
        self,
        request: ResilienceHubUpdateAppVersionAppComponentRequest,
    ) -> ResilienceHubUpdateAppVersionAppComponentResponse:
        client = self._require_client()
        return await self._execute(client.update_app_version_app_component, request, ResilienceHubUpdateAppVersionAppComponentResponse)

    async def update_app_version_resource(
        self,
        request: ResilienceHubUpdateAppVersionResourceRequest,
    ) -> ResilienceHubUpdateAppVersionResourceResponse:
        client = self._require_client()
        return await self._execute(client.update_app_version_resource, request, ResilienceHubUpdateAppVersionResourceResponse)

    async def update_resiliency_policy(
        self,
        request: ResilienceHubUpdateResiliencyPolicyRequest,
    ) -> ResilienceHubUpdateResiliencyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_resiliency_policy, request, ResilienceHubUpdateResiliencyPolicyResponse)
