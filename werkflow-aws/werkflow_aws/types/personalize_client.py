from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class PersonalizeClient(ABC):

    @abstractmethod
    def create_batch_inference_job(
        self,
        *,
        jobName: str,
        solutionVersionArn: str,
        jobInput: dict[str, Any],
        jobOutput: dict[str, Any],
        roleArn: str,
        filterArn: str | None = None,
        numResults: int | None = None,
        batchInferenceJobConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        batchInferenceJobMode: str | None = None,
        themeGenerationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_batch_segment_job(
        self,
        *,
        jobName: str,
        solutionVersionArn: str,
        jobInput: dict[str, Any],
        jobOutput: dict[str, Any],
        roleArn: str,
        filterArn: str | None = None,
        numResults: int | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_campaign(
        self,
        *,
        name: str,
        solutionVersionArn: str,
        minProvisionedTPS: int | None = None,
        campaignConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_deletion_job(
        self,
        *,
        jobName: str,
        datasetGroupArn: str,
        dataSource: dict[str, Any],
        roleArn: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset(
        self,
        *,
        name: str,
        schemaArn: str,
        datasetGroupArn: str,
        datasetType: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset_export_job(
        self,
        *,
        jobName: str,
        datasetArn: str,
        roleArn: str,
        jobOutput: dict[str, Any],
        ingestionMode: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset_group(
        self,
        *,
        name: str,
        roleArn: str | None = None,
        kmsKeyArn: str | None = None,
        domain: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset_import_job(
        self,
        *,
        jobName: str,
        datasetArn: str,
        dataSource: dict[str, Any],
        roleArn: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        importMode: str | None = None,
        publishAttributionMetricsToS3: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_tracker(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_filter(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        filterExpression: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_metric_attribution(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        metrics: list[dict[str, Any]],
        metricsOutputConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_recommender(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        recipeArn: str,
        recommenderConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_schema(
        self,
        *,
        name: str,
        schema: str,
        domain: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_solution(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        performHPO: bool | None = None,
        performAutoML: bool | None = None,
        performAutoTraining: bool | None = None,
        performIncrementalUpdate: bool | None = None,
        recipeArn: str | None = None,
        eventType: str | None = None,
        solutionConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_solution_version(
        self,
        *,
        solutionArn: str,
        name: str | None = None,
        trainingMode: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_campaign(
        self,
        *,
        campaignArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dataset(
        self,
        *,
        datasetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dataset_group(
        self,
        *,
        datasetGroupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_tracker(
        self,
        *,
        eventTrackerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_filter(
        self,
        *,
        filterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_attribution(
        self,
        *,
        metricAttributionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_recommender(
        self,
        *,
        recommenderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_schema(
        self,
        *,
        schemaArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_solution(
        self,
        *,
        solutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_algorithm(
        self,
        *,
        algorithmArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_batch_inference_job(
        self,
        *,
        batchInferenceJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_batch_segment_job(
        self,
        *,
        batchSegmentJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_campaign(
        self,
        *,
        campaignArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_deletion_job(
        self,
        *,
        dataDeletionJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset(
        self,
        *,
        datasetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset_export_job(
        self,
        *,
        datasetExportJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset_group(
        self,
        *,
        datasetGroupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset_import_job(
        self,
        *,
        datasetImportJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_tracker(
        self,
        *,
        eventTrackerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_feature_transformation(
        self,
        *,
        featureTransformationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_filter(
        self,
        *,
        filterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metric_attribution(
        self,
        *,
        metricAttributionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recipe(
        self,
        *,
        recipeArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recommender(
        self,
        *,
        recommenderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_schema(
        self,
        *,
        schemaArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_solution(
        self,
        *,
        solutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_solution_version(
        self,
        *,
        solutionVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_solution_metrics(
        self,
        *,
        solutionVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_batch_inference_jobs(
        self,
        *,
        solutionVersionArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_batch_segment_jobs(
        self,
        *,
        solutionVersionArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_campaigns(
        self,
        *,
        solutionArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_deletion_jobs(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dataset_export_jobs(
        self,
        *,
        datasetArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dataset_groups(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dataset_import_jobs(
        self,
        *,
        datasetArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_datasets(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_trackers(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_filters(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metric_attribution_metrics(
        self,
        *,
        metricAttributionArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metric_attributions(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recipes(
        self,
        *,
        recipeProvider: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        domain: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommenders(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schemas(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_solution_versions(
        self,
        *,
        solutionArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_solutions(
        self,
        *,
        datasetGroupArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_recommender(
        self,
        *,
        recommenderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_recommender(
        self,
        *,
        recommenderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_solution_version_creation(
        self,
        *,
        solutionVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_campaign(
        self,
        *,
        campaignArn: str,
        solutionVersionArn: str | None = None,
        minProvisionedTPS: int | None = None,
        campaignConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dataset(
        self,
        *,
        datasetArn: str,
        schemaArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_metric_attribution(
        self,
        *,
        addMetrics: list[dict[str, Any]] | None = None,
        removeMetrics: list[str] | None = None,
        metricsOutputConfig: dict[str, Any] | None = None,
        metricAttributionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_recommender(
        self,
        *,
        recommenderArn: str,
        recommenderConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_solution(
        self,
        *,
        solutionArn: str,
        performAutoTraining: bool | None = None,
        performIncrementalUpdate: bool | None = None,
        solutionUpdateConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
