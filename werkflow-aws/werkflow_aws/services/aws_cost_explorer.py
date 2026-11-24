import functools
from typing import Any

from werkflow_aws.models.cost_explorer import (
    CostExplorerGetCostForecastRequest,
    CostExplorerGetCostForecastResponse,
    CostExplorerGetDimensionValuesRequest,
    CostExplorerGetDimensionValuesResponse,
    CostExplorerGetTagsRequest,
    CostExplorerGetTagsResponse,
    CostExplorerListCostCategoryDefinitionsRequest,
    CostExplorerListCostCategoryDefinitionsResponse,
    CostExplorerQuery,
    CostExplorerResponse,
)
from werkflow_aws.types import CostExplorerClient
from .base import AWSBaseService
from werkflow_aws.models.cost_explorer import (
    CostExplorerCreateAnomalyMonitorRequest,
    CostExplorerCreateAnomalyMonitorResponse,
    CostExplorerCreateAnomalySubscriptionRequest,
    CostExplorerCreateAnomalySubscriptionResponse,
    CostExplorerCreateCostCategoryDefinitionRequest,
    CostExplorerCreateCostCategoryDefinitionResponse,
    CostExplorerDeleteAnomalyMonitorRequest,
    CostExplorerDeleteAnomalyMonitorResponse,
    CostExplorerDeleteAnomalySubscriptionRequest,
    CostExplorerDeleteAnomalySubscriptionResponse,
    CostExplorerDeleteCostCategoryDefinitionRequest,
    CostExplorerDeleteCostCategoryDefinitionResponse,
    CostExplorerDescribeCostCategoryDefinitionRequest,
    CostExplorerDescribeCostCategoryDefinitionResponse,
    CostExplorerGetAnomaliesRequest,
    CostExplorerGetAnomaliesResponse,
    CostExplorerGetAnomalyMonitorsRequest,
    CostExplorerGetAnomalyMonitorsResponse,
    CostExplorerGetAnomalySubscriptionsRequest,
    CostExplorerGetAnomalySubscriptionsResponse,
    CostExplorerGetApproximateUsageRecordsRequest,
    CostExplorerGetApproximateUsageRecordsResponse,
    CostExplorerGetCommitmentPurchaseAnalysisRequest,
    CostExplorerGetCommitmentPurchaseAnalysisResponse,
    CostExplorerGetCostAndUsageComparisonsRequest,
    CostExplorerGetCostAndUsageComparisonsResponse,
    CostExplorerGetCostAndUsageWithResourcesRequest,
    CostExplorerGetCostAndUsageWithResourcesResponse,
    CostExplorerGetCostCategoriesRequest,
    CostExplorerGetCostCategoriesResponse,
    CostExplorerGetCostComparisonDriversRequest,
    CostExplorerGetCostComparisonDriversResponse,
    CostExplorerGetReservationCoverageRequest,
    CostExplorerGetReservationCoverageResponse,
    CostExplorerGetReservationPurchaseRecommendationRequest,
    CostExplorerGetReservationPurchaseRecommendationResponse,
    CostExplorerGetReservationUtilizationRequest,
    CostExplorerGetReservationUtilizationResponse,
    CostExplorerGetRightsizingRecommendationRequest,
    CostExplorerGetRightsizingRecommendationResponse,
    CostExplorerGetSavingsPlanPurchaseRecommendationDetailsRequest,
    CostExplorerGetSavingsPlanPurchaseRecommendationDetailsResponse,
    CostExplorerGetSavingsPlansCoverageRequest,
    CostExplorerGetSavingsPlansCoverageResponse,
    CostExplorerGetSavingsPlansPurchaseRecommendationRequest,
    CostExplorerGetSavingsPlansPurchaseRecommendationResponse,
    CostExplorerGetSavingsPlansUtilizationDetailsRequest,
    CostExplorerGetSavingsPlansUtilizationDetailsResponse,
    CostExplorerGetSavingsPlansUtilizationRequest,
    CostExplorerGetSavingsPlansUtilizationResponse,
    CostExplorerGetUsageForecastRequest,
    CostExplorerGetUsageForecastResponse,
    CostExplorerListCommitmentPurchaseAnalysesRequest,
    CostExplorerListCommitmentPurchaseAnalysesResponse,
    CostExplorerListCostAllocationTagBackfillHistoryRequest,
    CostExplorerListCostAllocationTagBackfillHistoryResponse,
    CostExplorerListCostAllocationTagsRequest,
    CostExplorerListCostAllocationTagsResponse,
    CostExplorerListCostCategoryResourceAssociationsRequest,
    CostExplorerListCostCategoryResourceAssociationsResponse,
    CostExplorerListSavingsPlansPurchaseRecommendationGenerationRequest,
    CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse,
    CostExplorerListTagsForResourceRequest,
    CostExplorerListTagsForResourceResponse,
    CostExplorerProvideAnomalyFeedbackRequest,
    CostExplorerProvideAnomalyFeedbackResponse,
    CostExplorerStartCommitmentPurchaseAnalysisRequest,
    CostExplorerStartCommitmentPurchaseAnalysisResponse,
    CostExplorerStartCostAllocationTagBackfillRequest,
    CostExplorerStartCostAllocationTagBackfillResponse,
    CostExplorerStartSavingsPlansPurchaseRecommendationGenerationRequest,
    CostExplorerStartSavingsPlansPurchaseRecommendationGenerationResponse,
    CostExplorerTagResourceRequest,
    CostExplorerTagResourceResponse,
    CostExplorerUntagResourceRequest,
    CostExplorerUntagResourceResponse,
    CostExplorerUpdateAnomalyMonitorRequest,
    CostExplorerUpdateAnomalyMonitorResponse,
    CostExplorerUpdateAnomalySubscriptionRequest,
    CostExplorerUpdateAnomalySubscriptionResponse,
    CostExplorerUpdateCostAllocationTagsStatusRequest,
    CostExplorerUpdateCostAllocationTagsStatusResponse,
    CostExplorerUpdateCostCategoryDefinitionRequest,
    CostExplorerUpdateCostCategoryDefinitionResponse,
)


class AWSCostExplorer(AWSBaseService[CostExplorerClient]):
    service_name = 'CostExplorer'
    boto3_service_name = 'ce'

    def __init__(self) -> None:
        super().__init__(
            service_name='CostExplorer',
            boto3_service_name='ce',
        )

    async def get_cost_and_usage(
        self,
        query: CostExplorerQuery,
    ) -> CostExplorerResponse:
        client = self._require_client()
        loop = self._get_loop()
        dumped = query.dump()

        result = await loop.run_in_executor(
            self._executor,
            functools.partial(client.get_cost_and_usage, **dumped),
        )
        return CostExplorerResponse(**result)

    async def get_cost_and_usage_paginated(
        self,
        query: CostExplorerQuery,
    ) -> list[CostExplorerResponse]:
        client = self._require_client()
        loop = self._get_loop()
        base_params: dict[str, Any] = dict(query.dump())

        responses: list[CostExplorerResponse] = []
        next_page_token: str | None = base_params.pop('NextPageToken', None)

        while True:
            params = dict(base_params)
            if next_page_token is not None:
                params['NextPageToken'] = next_page_token

            result = await loop.run_in_executor(
                self._executor,
                functools.partial(client.get_cost_and_usage, **params),
            )
            page = CostExplorerResponse(**result)
            responses.append(page)

            if not page.NextPageToken:
                break
            next_page_token = page.NextPageToken

        return responses

    async def get_cost_forecast(
        self,
        request: CostExplorerGetCostForecastRequest,
    ) -> CostExplorerGetCostForecastResponse:
        client = self._require_client()
        return await self._execute(
            client.get_cost_forecast,
            request,
            CostExplorerGetCostForecastResponse,
        )

    async def get_dimension_values(
        self,
        request: CostExplorerGetDimensionValuesRequest,
    ) -> CostExplorerGetDimensionValuesResponse:
        client = self._require_client()
        return await self._execute(
            client.get_dimension_values,
            request,
            CostExplorerGetDimensionValuesResponse,
        )

    async def get_tags(
        self,
        request: CostExplorerGetTagsRequest,
    ) -> CostExplorerGetTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.get_tags,
            request,
            CostExplorerGetTagsResponse,
        )

    async def list_cost_category_definitions(
        self,
        request: CostExplorerListCostCategoryDefinitionsRequest | None = None,
    ) -> CostExplorerListCostCategoryDefinitionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_cost_category_definitions,
            request or CostExplorerListCostCategoryDefinitionsRequest(),
            CostExplorerListCostCategoryDefinitionsResponse,
        )

    async def list_cost_category_definitions_paginated(
        self,
        request: CostExplorerListCostCategoryDefinitionsRequest | None = None,
    ) -> list[CostExplorerListCostCategoryDefinitionsResponse]:
        return await self._paginate(
            'list_cost_category_definitions',
            request or CostExplorerListCostCategoryDefinitionsRequest(),
            CostExplorerListCostCategoryDefinitionsResponse,
        )

    async def create_anomaly_monitor(
        self,
        request: CostExplorerCreateAnomalyMonitorRequest,
    ) -> CostExplorerCreateAnomalyMonitorResponse:
        client = self._require_client()
        return await self._execute(client.create_anomaly_monitor, request, CostExplorerCreateAnomalyMonitorResponse)

    async def create_anomaly_subscription(
        self,
        request: CostExplorerCreateAnomalySubscriptionRequest,
    ) -> CostExplorerCreateAnomalySubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_anomaly_subscription, request, CostExplorerCreateAnomalySubscriptionResponse)

    async def create_cost_category_definition(
        self,
        request: CostExplorerCreateCostCategoryDefinitionRequest,
    ) -> CostExplorerCreateCostCategoryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_cost_category_definition, request, CostExplorerCreateCostCategoryDefinitionResponse)

    async def delete_anomaly_monitor(
        self,
        request: CostExplorerDeleteAnomalyMonitorRequest,
    ) -> CostExplorerDeleteAnomalyMonitorResponse:
        client = self._require_client()
        return await self._execute(client.delete_anomaly_monitor, request, CostExplorerDeleteAnomalyMonitorResponse)

    async def delete_anomaly_subscription(
        self,
        request: CostExplorerDeleteAnomalySubscriptionRequest,
    ) -> CostExplorerDeleteAnomalySubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_anomaly_subscription, request, CostExplorerDeleteAnomalySubscriptionResponse)

    async def delete_cost_category_definition(
        self,
        request: CostExplorerDeleteCostCategoryDefinitionRequest,
    ) -> CostExplorerDeleteCostCategoryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_cost_category_definition, request, CostExplorerDeleteCostCategoryDefinitionResponse)

    async def describe_cost_category_definition(
        self,
        request: CostExplorerDescribeCostCategoryDefinitionRequest,
    ) -> CostExplorerDescribeCostCategoryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_cost_category_definition, request, CostExplorerDescribeCostCategoryDefinitionResponse)

    async def get_anomalies(
        self,
        request: CostExplorerGetAnomaliesRequest,
    ) -> CostExplorerGetAnomaliesResponse:
        client = self._require_client()
        return await self._execute(client.get_anomalies, request, CostExplorerGetAnomaliesResponse)

    async def get_anomalies_paginated(
        self,
        request: CostExplorerGetAnomaliesRequest,
    ) -> list[CostExplorerGetAnomaliesResponse]:
        return await self._paginate('get_anomalies', request, CostExplorerGetAnomaliesResponse)

    async def get_anomaly_monitors(
        self,
        request: CostExplorerGetAnomalyMonitorsRequest | None = None,
    ) -> CostExplorerGetAnomalyMonitorsResponse:
        client = self._require_client()
        return await self._execute(client.get_anomaly_monitors, request, CostExplorerGetAnomalyMonitorsResponse)

    async def get_anomaly_monitors_paginated(
        self,
        request: CostExplorerGetAnomalyMonitorsRequest | None = None,
    ) -> list[CostExplorerGetAnomalyMonitorsResponse]:
        return await self._paginate('get_anomaly_monitors', request, CostExplorerGetAnomalyMonitorsResponse)

    async def get_anomaly_subscriptions(
        self,
        request: CostExplorerGetAnomalySubscriptionsRequest | None = None,
    ) -> CostExplorerGetAnomalySubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_anomaly_subscriptions, request, CostExplorerGetAnomalySubscriptionsResponse)

    async def get_anomaly_subscriptions_paginated(
        self,
        request: CostExplorerGetAnomalySubscriptionsRequest | None = None,
    ) -> list[CostExplorerGetAnomalySubscriptionsResponse]:
        return await self._paginate('get_anomaly_subscriptions', request, CostExplorerGetAnomalySubscriptionsResponse)

    async def get_approximate_usage_records(
        self,
        request: CostExplorerGetApproximateUsageRecordsRequest,
    ) -> CostExplorerGetApproximateUsageRecordsResponse:
        client = self._require_client()
        return await self._execute(client.get_approximate_usage_records, request, CostExplorerGetApproximateUsageRecordsResponse)

    async def get_commitment_purchase_analysis(
        self,
        request: CostExplorerGetCommitmentPurchaseAnalysisRequest,
    ) -> CostExplorerGetCommitmentPurchaseAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_commitment_purchase_analysis, request, CostExplorerGetCommitmentPurchaseAnalysisResponse)

    async def get_cost_and_usage_comparisons(
        self,
        request: CostExplorerGetCostAndUsageComparisonsRequest,
    ) -> CostExplorerGetCostAndUsageComparisonsResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_and_usage_comparisons, request, CostExplorerGetCostAndUsageComparisonsResponse)

    async def get_cost_and_usage_comparisons_paginated(
        self,
        request: CostExplorerGetCostAndUsageComparisonsRequest,
    ) -> list[CostExplorerGetCostAndUsageComparisonsResponse]:
        return await self._paginate('get_cost_and_usage_comparisons', request, CostExplorerGetCostAndUsageComparisonsResponse)

    async def get_cost_and_usage_with_resources(
        self,
        request: CostExplorerGetCostAndUsageWithResourcesRequest,
    ) -> CostExplorerGetCostAndUsageWithResourcesResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_and_usage_with_resources, request, CostExplorerGetCostAndUsageWithResourcesResponse)

    async def get_cost_categories(
        self,
        request: CostExplorerGetCostCategoriesRequest,
    ) -> CostExplorerGetCostCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_categories, request, CostExplorerGetCostCategoriesResponse)

    async def get_cost_comparison_drivers(
        self,
        request: CostExplorerGetCostComparisonDriversRequest,
    ) -> CostExplorerGetCostComparisonDriversResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_comparison_drivers, request, CostExplorerGetCostComparisonDriversResponse)

    async def get_cost_comparison_drivers_paginated(
        self,
        request: CostExplorerGetCostComparisonDriversRequest,
    ) -> list[CostExplorerGetCostComparisonDriversResponse]:
        return await self._paginate('get_cost_comparison_drivers', request, CostExplorerGetCostComparisonDriversResponse)

    async def get_reservation_coverage(
        self,
        request: CostExplorerGetReservationCoverageRequest,
    ) -> CostExplorerGetReservationCoverageResponse:
        client = self._require_client()
        return await self._execute(client.get_reservation_coverage, request, CostExplorerGetReservationCoverageResponse)

    async def get_reservation_purchase_recommendation(
        self,
        request: CostExplorerGetReservationPurchaseRecommendationRequest,
    ) -> CostExplorerGetReservationPurchaseRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.get_reservation_purchase_recommendation, request, CostExplorerGetReservationPurchaseRecommendationResponse)

    async def get_reservation_purchase_recommendation_paginated(
        self,
        request: CostExplorerGetReservationPurchaseRecommendationRequest,
    ) -> list[CostExplorerGetReservationPurchaseRecommendationResponse]:
        return await self._paginate('get_reservation_purchase_recommendation', request, CostExplorerGetReservationPurchaseRecommendationResponse)

    async def get_reservation_utilization(
        self,
        request: CostExplorerGetReservationUtilizationRequest,
    ) -> CostExplorerGetReservationUtilizationResponse:
        client = self._require_client()
        return await self._execute(client.get_reservation_utilization, request, CostExplorerGetReservationUtilizationResponse)

    async def get_rightsizing_recommendation(
        self,
        request: CostExplorerGetRightsizingRecommendationRequest,
    ) -> CostExplorerGetRightsizingRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.get_rightsizing_recommendation, request, CostExplorerGetRightsizingRecommendationResponse)

    async def get_rightsizing_recommendation_paginated(
        self,
        request: CostExplorerGetRightsizingRecommendationRequest,
    ) -> list[CostExplorerGetRightsizingRecommendationResponse]:
        return await self._paginate('get_rightsizing_recommendation', request, CostExplorerGetRightsizingRecommendationResponse)

    async def get_savings_plan_purchase_recommendation_details(
        self,
        request: CostExplorerGetSavingsPlanPurchaseRecommendationDetailsRequest,
    ) -> CostExplorerGetSavingsPlanPurchaseRecommendationDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_savings_plan_purchase_recommendation_details, request, CostExplorerGetSavingsPlanPurchaseRecommendationDetailsResponse)

    async def get_savings_plans_coverage(
        self,
        request: CostExplorerGetSavingsPlansCoverageRequest,
    ) -> CostExplorerGetSavingsPlansCoverageResponse:
        client = self._require_client()
        return await self._execute(client.get_savings_plans_coverage, request, CostExplorerGetSavingsPlansCoverageResponse)

    async def get_savings_plans_purchase_recommendation(
        self,
        request: CostExplorerGetSavingsPlansPurchaseRecommendationRequest,
    ) -> CostExplorerGetSavingsPlansPurchaseRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.get_savings_plans_purchase_recommendation, request, CostExplorerGetSavingsPlansPurchaseRecommendationResponse)

    async def get_savings_plans_utilization(
        self,
        request: CostExplorerGetSavingsPlansUtilizationRequest,
    ) -> CostExplorerGetSavingsPlansUtilizationResponse:
        client = self._require_client()
        return await self._execute(client.get_savings_plans_utilization, request, CostExplorerGetSavingsPlansUtilizationResponse)

    async def get_savings_plans_utilization_details(
        self,
        request: CostExplorerGetSavingsPlansUtilizationDetailsRequest,
    ) -> CostExplorerGetSavingsPlansUtilizationDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_savings_plans_utilization_details, request, CostExplorerGetSavingsPlansUtilizationDetailsResponse)

    async def get_usage_forecast(
        self,
        request: CostExplorerGetUsageForecastRequest,
    ) -> CostExplorerGetUsageForecastResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_forecast, request, CostExplorerGetUsageForecastResponse)

    async def list_commitment_purchase_analyses(
        self,
        request: CostExplorerListCommitmentPurchaseAnalysesRequest | None = None,
    ) -> CostExplorerListCommitmentPurchaseAnalysesResponse:
        client = self._require_client()
        return await self._execute(client.list_commitment_purchase_analyses, request, CostExplorerListCommitmentPurchaseAnalysesResponse)

    async def list_commitment_purchase_analyses_paginated(
        self,
        request: CostExplorerListCommitmentPurchaseAnalysesRequest | None = None,
    ) -> list[CostExplorerListCommitmentPurchaseAnalysesResponse]:
        return await self._paginate('list_commitment_purchase_analyses', request, CostExplorerListCommitmentPurchaseAnalysesResponse)

    async def list_cost_allocation_tag_backfill_history(
        self,
        request: CostExplorerListCostAllocationTagBackfillHistoryRequest | None = None,
    ) -> CostExplorerListCostAllocationTagBackfillHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_cost_allocation_tag_backfill_history, request, CostExplorerListCostAllocationTagBackfillHistoryResponse)

    async def list_cost_allocation_tag_backfill_history_paginated(
        self,
        request: CostExplorerListCostAllocationTagBackfillHistoryRequest | None = None,
    ) -> list[CostExplorerListCostAllocationTagBackfillHistoryResponse]:
        return await self._paginate('list_cost_allocation_tag_backfill_history', request, CostExplorerListCostAllocationTagBackfillHistoryResponse)

    async def list_cost_allocation_tags(
        self,
        request: CostExplorerListCostAllocationTagsRequest | None = None,
    ) -> CostExplorerListCostAllocationTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_cost_allocation_tags, request, CostExplorerListCostAllocationTagsResponse)

    async def list_cost_allocation_tags_paginated(
        self,
        request: CostExplorerListCostAllocationTagsRequest | None = None,
    ) -> list[CostExplorerListCostAllocationTagsResponse]:
        return await self._paginate('list_cost_allocation_tags', request, CostExplorerListCostAllocationTagsResponse)

    async def list_cost_category_resource_associations(
        self,
        request: CostExplorerListCostCategoryResourceAssociationsRequest | None = None,
    ) -> CostExplorerListCostCategoryResourceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_cost_category_resource_associations, request, CostExplorerListCostCategoryResourceAssociationsResponse)

    async def list_cost_category_resource_associations_paginated(
        self,
        request: CostExplorerListCostCategoryResourceAssociationsRequest | None = None,
    ) -> list[CostExplorerListCostCategoryResourceAssociationsResponse]:
        return await self._paginate('list_cost_category_resource_associations', request, CostExplorerListCostCategoryResourceAssociationsResponse)

    async def list_savings_plans_purchase_recommendation_generation(
        self,
        request: CostExplorerListSavingsPlansPurchaseRecommendationGenerationRequest | None = None,
    ) -> CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse:
        client = self._require_client()
        return await self._execute(client.list_savings_plans_purchase_recommendation_generation, request, CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse)

    async def list_savings_plans_purchase_recommendation_generation_paginated(
        self,
        request: CostExplorerListSavingsPlansPurchaseRecommendationGenerationRequest | None = None,
    ) -> list[CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse]:
        return await self._paginate('list_savings_plans_purchase_recommendation_generation', request, CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse)

    async def list_tags_for_resource(
        self,
        request: CostExplorerListTagsForResourceRequest,
    ) -> CostExplorerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CostExplorerListTagsForResourceResponse)

    async def provide_anomaly_feedback(
        self,
        request: CostExplorerProvideAnomalyFeedbackRequest,
    ) -> CostExplorerProvideAnomalyFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.provide_anomaly_feedback, request, CostExplorerProvideAnomalyFeedbackResponse)

    async def start_commitment_purchase_analysis(
        self,
        request: CostExplorerStartCommitmentPurchaseAnalysisRequest,
    ) -> CostExplorerStartCommitmentPurchaseAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_commitment_purchase_analysis, request, CostExplorerStartCommitmentPurchaseAnalysisResponse)

    async def start_cost_allocation_tag_backfill(
        self,
        request: CostExplorerStartCostAllocationTagBackfillRequest,
    ) -> CostExplorerStartCostAllocationTagBackfillResponse:
        client = self._require_client()
        return await self._execute(client.start_cost_allocation_tag_backfill, request, CostExplorerStartCostAllocationTagBackfillResponse)

    async def start_savings_plans_purchase_recommendation_generation(
        self,
        request: CostExplorerStartSavingsPlansPurchaseRecommendationGenerationRequest | None = None,
    ) -> CostExplorerStartSavingsPlansPurchaseRecommendationGenerationResponse:
        client = self._require_client()
        return await self._execute(client.start_savings_plans_purchase_recommendation_generation, request, CostExplorerStartSavingsPlansPurchaseRecommendationGenerationResponse)

    async def tag_resource(
        self,
        request: CostExplorerTagResourceRequest,
    ) -> CostExplorerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CostExplorerTagResourceResponse)

    async def untag_resource(
        self,
        request: CostExplorerUntagResourceRequest,
    ) -> CostExplorerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CostExplorerUntagResourceResponse)

    async def update_anomaly_monitor(
        self,
        request: CostExplorerUpdateAnomalyMonitorRequest,
    ) -> CostExplorerUpdateAnomalyMonitorResponse:
        client = self._require_client()
        return await self._execute(client.update_anomaly_monitor, request, CostExplorerUpdateAnomalyMonitorResponse)

    async def update_anomaly_subscription(
        self,
        request: CostExplorerUpdateAnomalySubscriptionRequest,
    ) -> CostExplorerUpdateAnomalySubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_anomaly_subscription, request, CostExplorerUpdateAnomalySubscriptionResponse)

    async def update_cost_allocation_tags_status(
        self,
        request: CostExplorerUpdateCostAllocationTagsStatusRequest,
    ) -> CostExplorerUpdateCostAllocationTagsStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_cost_allocation_tags_status, request, CostExplorerUpdateCostAllocationTagsStatusResponse)

    async def update_cost_category_definition(
        self,
        request: CostExplorerUpdateCostCategoryDefinitionRequest,
    ) -> CostExplorerUpdateCostCategoryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.update_cost_category_definition, request, CostExplorerUpdateCostCategoryDefinitionResponse)

