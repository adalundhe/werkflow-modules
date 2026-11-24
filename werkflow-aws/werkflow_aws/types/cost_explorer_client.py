from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CostExplorerClient(ABC):

    @abstractmethod
    def get_cost_and_usage(
        self,
        *,
        TimePeriod: dict[str, Any],
        Granularity: str,
        Metrics: list[str],
        Filter: dict[str, Any] | None = None,
        GroupBy: list[dict[str, Any]] | None = None,
        BillingViewArn: str | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_forecast(
        self,
        *,
        TimePeriod: dict[str, Any],
        Metric: str,
        Granularity: str,
        Filter: dict[str, Any] | None = None,
        BillingViewArn: str | None = None,
        PredictionIntervalLevel: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dimension_values(
        self,
        *,
        TimePeriod: dict[str, Any],
        Dimension: str,
        SearchString: str | None = None,
        DimensionKey: str | None = None,
        Context: str | None = None,
        Filter: dict[str, Any] | None = None,
        SortBy: list[dict[str, Any]] | None = None,
        BillingViewArn: str | None = None,
        MaxResults: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tags(
        self,
        *,
        TimePeriod: dict[str, Any],
        SearchString: str | None = None,
        TagKey: str | None = None,
        Filter: dict[str, Any] | None = None,
        SortBy: list[dict[str, Any]] | None = None,
        BillingViewArn: str | None = None,
        MaxResults: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cost_category_definitions(
        self,
        *,
        EffectiveOn: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SupportedResourceTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_anomaly_monitor(
        self,
        *,
        AnomalyMonitor: dict[str, Any],
        ResourceTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_anomaly_subscription(
        self,
        *,
        AnomalySubscription: dict[str, Any],
        ResourceTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cost_category_definition(
        self,
        *,
        Name: str,
        RuleVersion: str,
        Rules: list[dict[str, Any]],
        EffectiveStart: str | None = None,
        DefaultValue: str | None = None,
        SplitChargeRules: list[dict[str, Any]] | None = None,
        ResourceTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_anomaly_monitor(
        self,
        *,
        MonitorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_anomaly_subscription(
        self,
        *,
        SubscriptionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cost_category_definition(
        self,
        *,
        CostCategoryArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cost_category_definition(
        self,
        *,
        CostCategoryArn: str,
        EffectiveOn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_anomalies(
        self,
        *,
        DateInterval: dict[str, Any],
        MonitorArn: str | None = None,
        Feedback: str | None = None,
        TotalImpact: dict[str, Any] | None = None,
        NextPageToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_anomaly_monitors(
        self,
        *,
        MonitorArnList: list[str] | None = None,
        NextPageToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_anomaly_subscriptions(
        self,
        *,
        SubscriptionArnList: list[str] | None = None,
        MonitorArn: str | None = None,
        NextPageToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_approximate_usage_records(
        self,
        *,
        Granularity: str,
        ApproximationDimension: str,
        Services: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_commitment_purchase_analysis(
        self,
        *,
        AnalysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_and_usage_comparisons(
        self,
        *,
        BaselineTimePeriod: dict[str, Any],
        ComparisonTimePeriod: dict[str, Any],
        MetricForComparison: str,
        BillingViewArn: str | None = None,
        Filter: dict[str, Any] | None = None,
        GroupBy: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_and_usage_with_resources(
        self,
        *,
        TimePeriod: dict[str, Any],
        Granularity: str,
        Filter: dict[str, Any],
        Metrics: list[str] | None = None,
        GroupBy: list[dict[str, Any]] | None = None,
        BillingViewArn: str | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_categories(
        self,
        *,
        TimePeriod: dict[str, Any],
        SearchString: str | None = None,
        CostCategoryName: str | None = None,
        Filter: dict[str, Any] | None = None,
        SortBy: list[dict[str, Any]] | None = None,
        BillingViewArn: str | None = None,
        MaxResults: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_comparison_drivers(
        self,
        *,
        BaselineTimePeriod: dict[str, Any],
        ComparisonTimePeriod: dict[str, Any],
        MetricForComparison: str,
        BillingViewArn: str | None = None,
        Filter: dict[str, Any] | None = None,
        GroupBy: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reservation_coverage(
        self,
        *,
        TimePeriod: dict[str, Any],
        GroupBy: list[dict[str, Any]] | None = None,
        Granularity: str | None = None,
        Filter: dict[str, Any] | None = None,
        Metrics: list[str] | None = None,
        NextPageToken: str | None = None,
        SortBy: dict[str, Any] | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reservation_purchase_recommendation(
        self,
        *,
        Service: str,
        AccountId: str | None = None,
        Filter: dict[str, Any] | None = None,
        AccountScope: str | None = None,
        LookbackPeriodInDays: str | None = None,
        TermInYears: str | None = None,
        PaymentOption: str | None = None,
        ServiceSpecification: dict[str, Any] | None = None,
        PageSize: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reservation_utilization(
        self,
        *,
        TimePeriod: dict[str, Any],
        GroupBy: list[dict[str, Any]] | None = None,
        Granularity: str | None = None,
        Filter: dict[str, Any] | None = None,
        SortBy: dict[str, Any] | None = None,
        NextPageToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rightsizing_recommendation(
        self,
        *,
        Service: str,
        Filter: dict[str, Any] | None = None,
        Configuration: dict[str, Any] | None = None,
        PageSize: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_savings_plan_purchase_recommendation_details(
        self,
        *,
        RecommendationDetailId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_savings_plans_coverage(
        self,
        *,
        TimePeriod: dict[str, Any],
        GroupBy: list[dict[str, Any]] | None = None,
        Granularity: str | None = None,
        Filter: dict[str, Any] | None = None,
        Metrics: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_savings_plans_purchase_recommendation(
        self,
        *,
        SavingsPlansType: str,
        TermInYears: str,
        PaymentOption: str,
        LookbackPeriodInDays: str,
        AccountScope: str | None = None,
        NextPageToken: str | None = None,
        PageSize: int | None = None,
        Filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_savings_plans_utilization(
        self,
        *,
        TimePeriod: dict[str, Any],
        Granularity: str | None = None,
        Filter: dict[str, Any] | None = None,
        SortBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_savings_plans_utilization_details(
        self,
        *,
        TimePeriod: dict[str, Any],
        Filter: dict[str, Any] | None = None,
        DataType: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_forecast(
        self,
        *,
        TimePeriod: dict[str, Any],
        Metric: str,
        Granularity: str,
        Filter: dict[str, Any] | None = None,
        BillingViewArn: str | None = None,
        PredictionIntervalLevel: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_commitment_purchase_analyses(
        self,
        *,
        AnalysisStatus: str | None = None,
        NextPageToken: str | None = None,
        PageSize: int | None = None,
        AnalysisIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cost_allocation_tag_backfill_history(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cost_allocation_tags(
        self,
        *,
        Status: str | None = None,
        TagKeys: list[str] | None = None,
        Type: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cost_category_resource_associations(
        self,
        *,
        CostCategoryArn: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_savings_plans_purchase_recommendation_generation(
        self,
        *,
        GenerationStatus: str | None = None,
        RecommendationIds: list[str] | None = None,
        PageSize: int | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provide_anomaly_feedback(
        self,
        *,
        AnomalyId: str,
        Feedback: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_commitment_purchase_analysis(
        self,
        *,
        CommitmentPurchaseAnalysisConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_cost_allocation_tag_backfill(
        self,
        *,
        BackfillFrom: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_savings_plans_purchase_recommendation_generation(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        ResourceTags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        ResourceTagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_anomaly_monitor(
        self,
        *,
        MonitorArn: str,
        MonitorName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_anomaly_subscription(
        self,
        *,
        SubscriptionArn: str,
        Threshold: float | int | None = None,
        Frequency: str | None = None,
        MonitorArnList: list[str] | None = None,
        Subscribers: list[dict[str, Any]] | None = None,
        SubscriptionName: str | None = None,
        ThresholdExpression: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cost_allocation_tags_status(
        self,
        *,
        CostAllocationTagsStatus: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cost_category_definition(
        self,
        *,
        CostCategoryArn: str,
        RuleVersion: str,
        Rules: list[dict[str, Any]],
        EffectiveStart: str | None = None,
        DefaultValue: str | None = None,
        SplitChargeRules: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
