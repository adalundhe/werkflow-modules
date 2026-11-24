from werkflow_aws.models.personalize import (
    PersonalizeCreateBatchInferenceJobRequest,
    PersonalizeCreateBatchInferenceJobResponse,
    PersonalizeCreateBatchSegmentJobRequest,
    PersonalizeCreateBatchSegmentJobResponse,
    PersonalizeCreateCampaignRequest,
    PersonalizeCreateCampaignResponse,
    PersonalizeCreateDataDeletionJobRequest,
    PersonalizeCreateDataDeletionJobResponse,
    PersonalizeCreateDatasetExportJobRequest,
    PersonalizeCreateDatasetExportJobResponse,
    PersonalizeCreateDatasetGroupRequest,
    PersonalizeCreateDatasetGroupResponse,
    PersonalizeCreateDatasetImportJobRequest,
    PersonalizeCreateDatasetImportJobResponse,
    PersonalizeCreateDatasetRequest,
    PersonalizeCreateDatasetResponse,
    PersonalizeCreateEventTrackerRequest,
    PersonalizeCreateEventTrackerResponse,
    PersonalizeCreateFilterRequest,
    PersonalizeCreateFilterResponse,
    PersonalizeCreateMetricAttributionRequest,
    PersonalizeCreateMetricAttributionResponse,
    PersonalizeCreateRecommenderRequest,
    PersonalizeCreateRecommenderResponse,
    PersonalizeCreateSchemaRequest,
    PersonalizeCreateSchemaResponse,
    PersonalizeCreateSolutionRequest,
    PersonalizeCreateSolutionResponse,
    PersonalizeCreateSolutionVersionRequest,
    PersonalizeCreateSolutionVersionResponse,
    PersonalizeDeleteCampaignRequest,
    PersonalizeDeleteCampaignResponse,
    PersonalizeDeleteDatasetGroupRequest,
    PersonalizeDeleteDatasetGroupResponse,
    PersonalizeDeleteDatasetRequest,
    PersonalizeDeleteDatasetResponse,
    PersonalizeDeleteEventTrackerRequest,
    PersonalizeDeleteEventTrackerResponse,
    PersonalizeDeleteFilterRequest,
    PersonalizeDeleteFilterResponse,
    PersonalizeDeleteMetricAttributionRequest,
    PersonalizeDeleteMetricAttributionResponse,
    PersonalizeDeleteRecommenderRequest,
    PersonalizeDeleteRecommenderResponse,
    PersonalizeDeleteSchemaRequest,
    PersonalizeDeleteSchemaResponse,
    PersonalizeDeleteSolutionRequest,
    PersonalizeDeleteSolutionResponse,
    PersonalizeDescribeAlgorithmRequest,
    PersonalizeDescribeAlgorithmResponse,
    PersonalizeDescribeBatchInferenceJobRequest,
    PersonalizeDescribeBatchInferenceJobResponse,
    PersonalizeDescribeBatchSegmentJobRequest,
    PersonalizeDescribeBatchSegmentJobResponse,
    PersonalizeDescribeCampaignRequest,
    PersonalizeDescribeCampaignResponse,
    PersonalizeDescribeDataDeletionJobRequest,
    PersonalizeDescribeDataDeletionJobResponse,
    PersonalizeDescribeDatasetExportJobRequest,
    PersonalizeDescribeDatasetExportJobResponse,
    PersonalizeDescribeDatasetGroupRequest,
    PersonalizeDescribeDatasetGroupResponse,
    PersonalizeDescribeDatasetImportJobRequest,
    PersonalizeDescribeDatasetImportJobResponse,
    PersonalizeDescribeDatasetRequest,
    PersonalizeDescribeDatasetResponse,
    PersonalizeDescribeEventTrackerRequest,
    PersonalizeDescribeEventTrackerResponse,
    PersonalizeDescribeFeatureTransformationRequest,
    PersonalizeDescribeFeatureTransformationResponse,
    PersonalizeDescribeFilterRequest,
    PersonalizeDescribeFilterResponse,
    PersonalizeDescribeMetricAttributionRequest,
    PersonalizeDescribeMetricAttributionResponse,
    PersonalizeDescribeRecipeRequest,
    PersonalizeDescribeRecipeResponse,
    PersonalizeDescribeRecommenderRequest,
    PersonalizeDescribeRecommenderResponse,
    PersonalizeDescribeSchemaRequest,
    PersonalizeDescribeSchemaResponse,
    PersonalizeDescribeSolutionRequest,
    PersonalizeDescribeSolutionResponse,
    PersonalizeDescribeSolutionVersionRequest,
    PersonalizeDescribeSolutionVersionResponse,
    PersonalizeGetSolutionMetricsRequest,
    PersonalizeGetSolutionMetricsResponse,
    PersonalizeListBatchInferenceJobsRequest,
    PersonalizeListBatchInferenceJobsResponse,
    PersonalizeListBatchSegmentJobsRequest,
    PersonalizeListBatchSegmentJobsResponse,
    PersonalizeListCampaignsRequest,
    PersonalizeListCampaignsResponse,
    PersonalizeListDataDeletionJobsRequest,
    PersonalizeListDataDeletionJobsResponse,
    PersonalizeListDatasetExportJobsRequest,
    PersonalizeListDatasetExportJobsResponse,
    PersonalizeListDatasetGroupsRequest,
    PersonalizeListDatasetGroupsResponse,
    PersonalizeListDatasetImportJobsRequest,
    PersonalizeListDatasetImportJobsResponse,
    PersonalizeListDatasetsRequest,
    PersonalizeListDatasetsResponse,
    PersonalizeListEventTrackersRequest,
    PersonalizeListEventTrackersResponse,
    PersonalizeListFiltersRequest,
    PersonalizeListFiltersResponse,
    PersonalizeListMetricAttributionMetricsRequest,
    PersonalizeListMetricAttributionMetricsResponse,
    PersonalizeListMetricAttributionsRequest,
    PersonalizeListMetricAttributionsResponse,
    PersonalizeListRecipesRequest,
    PersonalizeListRecipesResponse,
    PersonalizeListRecommendersRequest,
    PersonalizeListRecommendersResponse,
    PersonalizeListSchemasRequest,
    PersonalizeListSchemasResponse,
    PersonalizeListSolutionVersionsRequest,
    PersonalizeListSolutionVersionsResponse,
    PersonalizeListSolutionsRequest,
    PersonalizeListSolutionsResponse,
    PersonalizeListTagsForResourceRequest,
    PersonalizeListTagsForResourceResponse,
    PersonalizeStartRecommenderRequest,
    PersonalizeStartRecommenderResponse,
    PersonalizeStopRecommenderRequest,
    PersonalizeStopRecommenderResponse,
    PersonalizeStopSolutionVersionCreationRequest,
    PersonalizeStopSolutionVersionCreationResponse,
    PersonalizeTagResourceRequest,
    PersonalizeTagResourceResponse,
    PersonalizeUntagResourceRequest,
    PersonalizeUntagResourceResponse,
    PersonalizeUpdateCampaignRequest,
    PersonalizeUpdateCampaignResponse,
    PersonalizeUpdateDatasetRequest,
    PersonalizeUpdateDatasetResponse,
    PersonalizeUpdateMetricAttributionRequest,
    PersonalizeUpdateMetricAttributionResponse,
    PersonalizeUpdateRecommenderRequest,
    PersonalizeUpdateRecommenderResponse,
    PersonalizeUpdateSolutionRequest,
    PersonalizeUpdateSolutionResponse,
)
from werkflow_aws.types.personalize_client import PersonalizeClient
from .base import AWSBaseService


class AWSPersonalize(AWSBaseService[PersonalizeClient]):
    service_name = 'personalize'
    boto3_service_name = 'personalize'

    def __init__(self) -> None:
        super().__init__(service_name='personalize', boto3_service_name='personalize')

    async def create_batch_inference_job(
        self,
        request: PersonalizeCreateBatchInferenceJobRequest,
    ) -> PersonalizeCreateBatchInferenceJobResponse:
        client = self._require_client()
        return await self._execute(client.create_batch_inference_job, request, PersonalizeCreateBatchInferenceJobResponse)

    async def create_batch_segment_job(
        self,
        request: PersonalizeCreateBatchSegmentJobRequest,
    ) -> PersonalizeCreateBatchSegmentJobResponse:
        client = self._require_client()
        return await self._execute(client.create_batch_segment_job, request, PersonalizeCreateBatchSegmentJobResponse)

    async def create_campaign(
        self,
        request: PersonalizeCreateCampaignRequest,
    ) -> PersonalizeCreateCampaignResponse:
        client = self._require_client()
        return await self._execute(client.create_campaign, request, PersonalizeCreateCampaignResponse)

    async def create_data_deletion_job(
        self,
        request: PersonalizeCreateDataDeletionJobRequest,
    ) -> PersonalizeCreateDataDeletionJobResponse:
        client = self._require_client()
        return await self._execute(client.create_data_deletion_job, request, PersonalizeCreateDataDeletionJobResponse)

    async def create_dataset(
        self,
        request: PersonalizeCreateDatasetRequest,
    ) -> PersonalizeCreateDatasetResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset, request, PersonalizeCreateDatasetResponse)

    async def create_dataset_export_job(
        self,
        request: PersonalizeCreateDatasetExportJobRequest,
    ) -> PersonalizeCreateDatasetExportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset_export_job, request, PersonalizeCreateDatasetExportJobResponse)

    async def create_dataset_group(
        self,
        request: PersonalizeCreateDatasetGroupRequest,
    ) -> PersonalizeCreateDatasetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset_group, request, PersonalizeCreateDatasetGroupResponse)

    async def create_dataset_import_job(
        self,
        request: PersonalizeCreateDatasetImportJobRequest,
    ) -> PersonalizeCreateDatasetImportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset_import_job, request, PersonalizeCreateDatasetImportJobResponse)

    async def create_event_tracker(
        self,
        request: PersonalizeCreateEventTrackerRequest,
    ) -> PersonalizeCreateEventTrackerResponse:
        client = self._require_client()
        return await self._execute(client.create_event_tracker, request, PersonalizeCreateEventTrackerResponse)

    async def create_filter(
        self,
        request: PersonalizeCreateFilterRequest,
    ) -> PersonalizeCreateFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_filter, request, PersonalizeCreateFilterResponse)

    async def create_metric_attribution(
        self,
        request: PersonalizeCreateMetricAttributionRequest,
    ) -> PersonalizeCreateMetricAttributionResponse:
        client = self._require_client()
        return await self._execute(client.create_metric_attribution, request, PersonalizeCreateMetricAttributionResponse)

    async def create_recommender(
        self,
        request: PersonalizeCreateRecommenderRequest,
    ) -> PersonalizeCreateRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.create_recommender, request, PersonalizeCreateRecommenderResponse)

    async def create_schema(
        self,
        request: PersonalizeCreateSchemaRequest,
    ) -> PersonalizeCreateSchemaResponse:
        client = self._require_client()
        return await self._execute(client.create_schema, request, PersonalizeCreateSchemaResponse)

    async def create_solution(
        self,
        request: PersonalizeCreateSolutionRequest,
    ) -> PersonalizeCreateSolutionResponse:
        client = self._require_client()
        return await self._execute(client.create_solution, request, PersonalizeCreateSolutionResponse)

    async def create_solution_version(
        self,
        request: PersonalizeCreateSolutionVersionRequest,
    ) -> PersonalizeCreateSolutionVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_solution_version, request, PersonalizeCreateSolutionVersionResponse)

    async def delete_campaign(
        self,
        request: PersonalizeDeleteCampaignRequest,
    ) -> PersonalizeDeleteCampaignResponse:
        client = self._require_client()
        return await self._execute(client.delete_campaign, request, PersonalizeDeleteCampaignResponse)

    async def delete_dataset(
        self,
        request: PersonalizeDeleteDatasetRequest,
    ) -> PersonalizeDeleteDatasetResponse:
        client = self._require_client()
        return await self._execute(client.delete_dataset, request, PersonalizeDeleteDatasetResponse)

    async def delete_dataset_group(
        self,
        request: PersonalizeDeleteDatasetGroupRequest,
    ) -> PersonalizeDeleteDatasetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_dataset_group, request, PersonalizeDeleteDatasetGroupResponse)

    async def delete_event_tracker(
        self,
        request: PersonalizeDeleteEventTrackerRequest,
    ) -> PersonalizeDeleteEventTrackerResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_tracker, request, PersonalizeDeleteEventTrackerResponse)

    async def delete_filter(
        self,
        request: PersonalizeDeleteFilterRequest,
    ) -> PersonalizeDeleteFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_filter, request, PersonalizeDeleteFilterResponse)

    async def delete_metric_attribution(
        self,
        request: PersonalizeDeleteMetricAttributionRequest,
    ) -> PersonalizeDeleteMetricAttributionResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_attribution, request, PersonalizeDeleteMetricAttributionResponse)

    async def delete_recommender(
        self,
        request: PersonalizeDeleteRecommenderRequest,
    ) -> PersonalizeDeleteRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.delete_recommender, request, PersonalizeDeleteRecommenderResponse)

    async def delete_schema(
        self,
        request: PersonalizeDeleteSchemaRequest,
    ) -> PersonalizeDeleteSchemaResponse:
        client = self._require_client()
        return await self._execute(client.delete_schema, request, PersonalizeDeleteSchemaResponse)

    async def delete_solution(
        self,
        request: PersonalizeDeleteSolutionRequest,
    ) -> PersonalizeDeleteSolutionResponse:
        client = self._require_client()
        return await self._execute(client.delete_solution, request, PersonalizeDeleteSolutionResponse)

    async def describe_algorithm(
        self,
        request: PersonalizeDescribeAlgorithmRequest,
    ) -> PersonalizeDescribeAlgorithmResponse:
        client = self._require_client()
        return await self._execute(client.describe_algorithm, request, PersonalizeDescribeAlgorithmResponse)

    async def describe_batch_inference_job(
        self,
        request: PersonalizeDescribeBatchInferenceJobRequest,
    ) -> PersonalizeDescribeBatchInferenceJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_batch_inference_job, request, PersonalizeDescribeBatchInferenceJobResponse)

    async def describe_batch_segment_job(
        self,
        request: PersonalizeDescribeBatchSegmentJobRequest,
    ) -> PersonalizeDescribeBatchSegmentJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_batch_segment_job, request, PersonalizeDescribeBatchSegmentJobResponse)

    async def describe_campaign(
        self,
        request: PersonalizeDescribeCampaignRequest,
    ) -> PersonalizeDescribeCampaignResponse:
        client = self._require_client()
        return await self._execute(client.describe_campaign, request, PersonalizeDescribeCampaignResponse)

    async def describe_data_deletion_job(
        self,
        request: PersonalizeDescribeDataDeletionJobRequest,
    ) -> PersonalizeDescribeDataDeletionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_deletion_job, request, PersonalizeDescribeDataDeletionJobResponse)

    async def describe_dataset(
        self,
        request: PersonalizeDescribeDatasetRequest,
    ) -> PersonalizeDescribeDatasetResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset, request, PersonalizeDescribeDatasetResponse)

    async def describe_dataset_export_job(
        self,
        request: PersonalizeDescribeDatasetExportJobRequest,
    ) -> PersonalizeDescribeDatasetExportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset_export_job, request, PersonalizeDescribeDatasetExportJobResponse)

    async def describe_dataset_group(
        self,
        request: PersonalizeDescribeDatasetGroupRequest,
    ) -> PersonalizeDescribeDatasetGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset_group, request, PersonalizeDescribeDatasetGroupResponse)

    async def describe_dataset_import_job(
        self,
        request: PersonalizeDescribeDatasetImportJobRequest,
    ) -> PersonalizeDescribeDatasetImportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset_import_job, request, PersonalizeDescribeDatasetImportJobResponse)

    async def describe_event_tracker(
        self,
        request: PersonalizeDescribeEventTrackerRequest,
    ) -> PersonalizeDescribeEventTrackerResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_tracker, request, PersonalizeDescribeEventTrackerResponse)

    async def describe_feature_transformation(
        self,
        request: PersonalizeDescribeFeatureTransformationRequest,
    ) -> PersonalizeDescribeFeatureTransformationResponse:
        client = self._require_client()
        return await self._execute(client.describe_feature_transformation, request, PersonalizeDescribeFeatureTransformationResponse)

    async def describe_filter(
        self,
        request: PersonalizeDescribeFilterRequest,
    ) -> PersonalizeDescribeFilterResponse:
        client = self._require_client()
        return await self._execute(client.describe_filter, request, PersonalizeDescribeFilterResponse)

    async def describe_metric_attribution(
        self,
        request: PersonalizeDescribeMetricAttributionRequest,
    ) -> PersonalizeDescribeMetricAttributionResponse:
        client = self._require_client()
        return await self._execute(client.describe_metric_attribution, request, PersonalizeDescribeMetricAttributionResponse)

    async def describe_recipe(
        self,
        request: PersonalizeDescribeRecipeRequest,
    ) -> PersonalizeDescribeRecipeResponse:
        client = self._require_client()
        return await self._execute(client.describe_recipe, request, PersonalizeDescribeRecipeResponse)

    async def describe_recommender(
        self,
        request: PersonalizeDescribeRecommenderRequest,
    ) -> PersonalizeDescribeRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.describe_recommender, request, PersonalizeDescribeRecommenderResponse)

    async def describe_schema(
        self,
        request: PersonalizeDescribeSchemaRequest,
    ) -> PersonalizeDescribeSchemaResponse:
        client = self._require_client()
        return await self._execute(client.describe_schema, request, PersonalizeDescribeSchemaResponse)

    async def describe_solution(
        self,
        request: PersonalizeDescribeSolutionRequest,
    ) -> PersonalizeDescribeSolutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_solution, request, PersonalizeDescribeSolutionResponse)

    async def describe_solution_version(
        self,
        request: PersonalizeDescribeSolutionVersionRequest,
    ) -> PersonalizeDescribeSolutionVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_solution_version, request, PersonalizeDescribeSolutionVersionResponse)

    async def get_solution_metrics(
        self,
        request: PersonalizeGetSolutionMetricsRequest,
    ) -> PersonalizeGetSolutionMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_solution_metrics, request, PersonalizeGetSolutionMetricsResponse)

    async def list_batch_inference_jobs(
        self,
        request: PersonalizeListBatchInferenceJobsRequest | None = None,
    ) -> PersonalizeListBatchInferenceJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_batch_inference_jobs, request, PersonalizeListBatchInferenceJobsResponse)

    async def list_batch_inference_jobs_paginated(
        self,
        request: PersonalizeListBatchInferenceJobsRequest | None = None,
    ) -> list[PersonalizeListBatchInferenceJobsResponse]:
        return await self._paginate('list_batch_inference_jobs', request, PersonalizeListBatchInferenceJobsResponse)

    async def list_batch_segment_jobs(
        self,
        request: PersonalizeListBatchSegmentJobsRequest | None = None,
    ) -> PersonalizeListBatchSegmentJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_batch_segment_jobs, request, PersonalizeListBatchSegmentJobsResponse)

    async def list_batch_segment_jobs_paginated(
        self,
        request: PersonalizeListBatchSegmentJobsRequest | None = None,
    ) -> list[PersonalizeListBatchSegmentJobsResponse]:
        return await self._paginate('list_batch_segment_jobs', request, PersonalizeListBatchSegmentJobsResponse)

    async def list_campaigns(
        self,
        request: PersonalizeListCampaignsRequest | None = None,
    ) -> PersonalizeListCampaignsResponse:
        client = self._require_client()
        return await self._execute(client.list_campaigns, request, PersonalizeListCampaignsResponse)

    async def list_campaigns_paginated(
        self,
        request: PersonalizeListCampaignsRequest | None = None,
    ) -> list[PersonalizeListCampaignsResponse]:
        return await self._paginate('list_campaigns', request, PersonalizeListCampaignsResponse)

    async def list_data_deletion_jobs(
        self,
        request: PersonalizeListDataDeletionJobsRequest | None = None,
    ) -> PersonalizeListDataDeletionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_deletion_jobs, request, PersonalizeListDataDeletionJobsResponse)

    async def list_dataset_export_jobs(
        self,
        request: PersonalizeListDatasetExportJobsRequest | None = None,
    ) -> PersonalizeListDatasetExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_dataset_export_jobs, request, PersonalizeListDatasetExportJobsResponse)

    async def list_dataset_export_jobs_paginated(
        self,
        request: PersonalizeListDatasetExportJobsRequest | None = None,
    ) -> list[PersonalizeListDatasetExportJobsResponse]:
        return await self._paginate('list_dataset_export_jobs', request, PersonalizeListDatasetExportJobsResponse)

    async def list_dataset_groups(
        self,
        request: PersonalizeListDatasetGroupsRequest | None = None,
    ) -> PersonalizeListDatasetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_dataset_groups, request, PersonalizeListDatasetGroupsResponse)

    async def list_dataset_groups_paginated(
        self,
        request: PersonalizeListDatasetGroupsRequest | None = None,
    ) -> list[PersonalizeListDatasetGroupsResponse]:
        return await self._paginate('list_dataset_groups', request, PersonalizeListDatasetGroupsResponse)

    async def list_dataset_import_jobs(
        self,
        request: PersonalizeListDatasetImportJobsRequest | None = None,
    ) -> PersonalizeListDatasetImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_dataset_import_jobs, request, PersonalizeListDatasetImportJobsResponse)

    async def list_dataset_import_jobs_paginated(
        self,
        request: PersonalizeListDatasetImportJobsRequest | None = None,
    ) -> list[PersonalizeListDatasetImportJobsResponse]:
        return await self._paginate('list_dataset_import_jobs', request, PersonalizeListDatasetImportJobsResponse)

    async def list_datasets(
        self,
        request: PersonalizeListDatasetsRequest | None = None,
    ) -> PersonalizeListDatasetsResponse:
        client = self._require_client()
        return await self._execute(client.list_datasets, request, PersonalizeListDatasetsResponse)

    async def list_datasets_paginated(
        self,
        request: PersonalizeListDatasetsRequest | None = None,
    ) -> list[PersonalizeListDatasetsResponse]:
        return await self._paginate('list_datasets', request, PersonalizeListDatasetsResponse)

    async def list_event_trackers(
        self,
        request: PersonalizeListEventTrackersRequest | None = None,
    ) -> PersonalizeListEventTrackersResponse:
        client = self._require_client()
        return await self._execute(client.list_event_trackers, request, PersonalizeListEventTrackersResponse)

    async def list_event_trackers_paginated(
        self,
        request: PersonalizeListEventTrackersRequest | None = None,
    ) -> list[PersonalizeListEventTrackersResponse]:
        return await self._paginate('list_event_trackers', request, PersonalizeListEventTrackersResponse)

    async def list_filters(
        self,
        request: PersonalizeListFiltersRequest | None = None,
    ) -> PersonalizeListFiltersResponse:
        client = self._require_client()
        return await self._execute(client.list_filters, request, PersonalizeListFiltersResponse)

    async def list_filters_paginated(
        self,
        request: PersonalizeListFiltersRequest | None = None,
    ) -> list[PersonalizeListFiltersResponse]:
        return await self._paginate('list_filters', request, PersonalizeListFiltersResponse)

    async def list_metric_attribution_metrics(
        self,
        request: PersonalizeListMetricAttributionMetricsRequest | None = None,
    ) -> PersonalizeListMetricAttributionMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_metric_attribution_metrics, request, PersonalizeListMetricAttributionMetricsResponse)

    async def list_metric_attribution_metrics_paginated(
        self,
        request: PersonalizeListMetricAttributionMetricsRequest | None = None,
    ) -> list[PersonalizeListMetricAttributionMetricsResponse]:
        return await self._paginate('list_metric_attribution_metrics', request, PersonalizeListMetricAttributionMetricsResponse)

    async def list_metric_attributions(
        self,
        request: PersonalizeListMetricAttributionsRequest | None = None,
    ) -> PersonalizeListMetricAttributionsResponse:
        client = self._require_client()
        return await self._execute(client.list_metric_attributions, request, PersonalizeListMetricAttributionsResponse)

    async def list_metric_attributions_paginated(
        self,
        request: PersonalizeListMetricAttributionsRequest | None = None,
    ) -> list[PersonalizeListMetricAttributionsResponse]:
        return await self._paginate('list_metric_attributions', request, PersonalizeListMetricAttributionsResponse)

    async def list_recipes(
        self,
        request: PersonalizeListRecipesRequest | None = None,
    ) -> PersonalizeListRecipesResponse:
        client = self._require_client()
        return await self._execute(client.list_recipes, request, PersonalizeListRecipesResponse)

    async def list_recipes_paginated(
        self,
        request: PersonalizeListRecipesRequest | None = None,
    ) -> list[PersonalizeListRecipesResponse]:
        return await self._paginate('list_recipes', request, PersonalizeListRecipesResponse)

    async def list_recommenders(
        self,
        request: PersonalizeListRecommendersRequest | None = None,
    ) -> PersonalizeListRecommendersResponse:
        client = self._require_client()
        return await self._execute(client.list_recommenders, request, PersonalizeListRecommendersResponse)

    async def list_recommenders_paginated(
        self,
        request: PersonalizeListRecommendersRequest | None = None,
    ) -> list[PersonalizeListRecommendersResponse]:
        return await self._paginate('list_recommenders', request, PersonalizeListRecommendersResponse)

    async def list_schemas(
        self,
        request: PersonalizeListSchemasRequest | None = None,
    ) -> PersonalizeListSchemasResponse:
        client = self._require_client()
        return await self._execute(client.list_schemas, request, PersonalizeListSchemasResponse)

    async def list_schemas_paginated(
        self,
        request: PersonalizeListSchemasRequest | None = None,
    ) -> list[PersonalizeListSchemasResponse]:
        return await self._paginate('list_schemas', request, PersonalizeListSchemasResponse)

    async def list_solution_versions(
        self,
        request: PersonalizeListSolutionVersionsRequest | None = None,
    ) -> PersonalizeListSolutionVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_solution_versions, request, PersonalizeListSolutionVersionsResponse)

    async def list_solution_versions_paginated(
        self,
        request: PersonalizeListSolutionVersionsRequest | None = None,
    ) -> list[PersonalizeListSolutionVersionsResponse]:
        return await self._paginate('list_solution_versions', request, PersonalizeListSolutionVersionsResponse)

    async def list_solutions(
        self,
        request: PersonalizeListSolutionsRequest | None = None,
    ) -> PersonalizeListSolutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_solutions, request, PersonalizeListSolutionsResponse)

    async def list_solutions_paginated(
        self,
        request: PersonalizeListSolutionsRequest | None = None,
    ) -> list[PersonalizeListSolutionsResponse]:
        return await self._paginate('list_solutions', request, PersonalizeListSolutionsResponse)

    async def list_tags_for_resource(
        self,
        request: PersonalizeListTagsForResourceRequest,
    ) -> PersonalizeListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, PersonalizeListTagsForResourceResponse)

    async def start_recommender(
        self,
        request: PersonalizeStartRecommenderRequest,
    ) -> PersonalizeStartRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.start_recommender, request, PersonalizeStartRecommenderResponse)

    async def stop_recommender(
        self,
        request: PersonalizeStopRecommenderRequest,
    ) -> PersonalizeStopRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.stop_recommender, request, PersonalizeStopRecommenderResponse)

    async def stop_solution_version_creation(
        self,
        request: PersonalizeStopSolutionVersionCreationRequest,
    ) -> PersonalizeStopSolutionVersionCreationResponse:
        client = self._require_client()
        return await self._execute(client.stop_solution_version_creation, request, PersonalizeStopSolutionVersionCreationResponse)

    async def tag_resource(
        self,
        request: PersonalizeTagResourceRequest,
    ) -> PersonalizeTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, PersonalizeTagResourceResponse)

    async def untag_resource(
        self,
        request: PersonalizeUntagResourceRequest,
    ) -> PersonalizeUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, PersonalizeUntagResourceResponse)

    async def update_campaign(
        self,
        request: PersonalizeUpdateCampaignRequest,
    ) -> PersonalizeUpdateCampaignResponse:
        client = self._require_client()
        return await self._execute(client.update_campaign, request, PersonalizeUpdateCampaignResponse)

    async def update_dataset(
        self,
        request: PersonalizeUpdateDatasetRequest,
    ) -> PersonalizeUpdateDatasetResponse:
        client = self._require_client()
        return await self._execute(client.update_dataset, request, PersonalizeUpdateDatasetResponse)

    async def update_metric_attribution(
        self,
        request: PersonalizeUpdateMetricAttributionRequest | None = None,
    ) -> PersonalizeUpdateMetricAttributionResponse:
        client = self._require_client()
        return await self._execute(client.update_metric_attribution, request, PersonalizeUpdateMetricAttributionResponse)

    async def update_recommender(
        self,
        request: PersonalizeUpdateRecommenderRequest,
    ) -> PersonalizeUpdateRecommenderResponse:
        client = self._require_client()
        return await self._execute(client.update_recommender, request, PersonalizeUpdateRecommenderResponse)

    async def update_solution(
        self,
        request: PersonalizeUpdateSolutionRequest,
    ) -> PersonalizeUpdateSolutionResponse:
        client = self._require_client()
        return await self._execute(client.update_solution, request, PersonalizeUpdateSolutionResponse)
