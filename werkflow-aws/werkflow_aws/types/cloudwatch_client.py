from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class CloudWatchClient(ABC):

    @abstractmethod
    def get_metric_data(
        self,
        *,
        MetricDataQueries: list[dict[str, Any]],
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        NextToken: str | None = None,
        ScanBy: str | None = None,
        MaxDatapoints: int | None = None,
        LabelOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_statistics(
        self,
        *,
        Namespace: str,
        MetricName: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Period: int,
        Dimensions: list[dict[str, Any]] | None = None,
        Statistics: list[str] | None = None,
        ExtendedStatistics: list[str] | None = None,
        Unit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metrics(
        self,
        *,
        Namespace: str | None = None,
        MetricName: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        RecentlyActive: str | None = None,
        IncludeLinkedAccounts: bool | None = None,
        OwningAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_data(
        self,
        *,
        Namespace: str,
        MetricData: list[dict[str, Any]] | None = None,
        EntityMetricData: list[dict[str, Any]] | None = None,
        StrictEntityValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_alarms(
        self,
        *,
        AlarmNames: list[str] | None = None,
        AlarmNamePrefix: str | None = None,
        AlarmTypes: list[str] | None = None,
        ChildrenOfAlarmName: str | None = None,
        ParentsOfAlarmName: str | None = None,
        StateValue: str | None = None,
        ActionPrefix: str | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_alarm(
        self,
        *,
        AlarmName: str,
        AlarmDescription: str | None = None,
        ActionsEnabled: bool | None = None,
        OKActions: list[str] | None = None,
        AlarmActions: list[str] | None = None,
        InsufficientDataActions: list[str] | None = None,
        MetricName: str | None = None,
        Namespace: str | None = None,
        Statistic: str | None = None,
        ExtendedStatistic: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        Period: int | None = None,
        Unit: str | None = None,
        EvaluationPeriods: int | None = None,
        DatapointsToAlarm: int | None = None,
        Threshold: float | int | None = None,
        ComparisonOperator: str | None = None,
        TreatMissingData: str | None = None,
        EvaluateLowSampleCountPercentile: str | None = None,
        Metrics: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ThresholdMetricId: str | None = None,
        EvaluationWindow: dict[str, Any] | None = None,
        WarmUpConfiguration: dict[str, Any] | None = None,
        EvaluationCriteria: dict[str, Any] | None = None,
        EvaluationInterval: int | None = None,
        ActionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_alarms(
        self,
        *,
        AlarmNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_dataset_kms_key(
        self,
        *,
        DatasetIdentifier: str,
        KmsKeyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_metrics_configuration(
        self,
        *,
        ResourceArn: str,
        MetricSelections: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_alarm_mute_rule(
        self,
        *,
        AlarmMuteRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_anomaly_detector(
        self,
        *,
        AnomalyDetectorId: str | None = None,
        Namespace: str | None = None,
        MetricName: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        Stat: str | None = None,
        SingleMetricAnomalyDetector: dict[str, Any] | None = None,
        MetricMathAnomalyDetector: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dashboards(
        self,
        *,
        DashboardNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_insight_rules(
        self,
        *,
        RuleNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_data_query_definition(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_stream(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_metrics_configuration(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_alarm_contributors(
        self,
        *,
        AlarmName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_alarm_history(
        self,
        *,
        AlarmName: str | None = None,
        AlarmContributorId: str | None = None,
        AlarmTypes: list[str] | None = None,
        HistoryItemType: str | None = None,
        StartDate: datetime.datetime | str | None = None,
        EndDate: datetime.datetime | str | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
        ScanBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_alarms_for_metric(
        self,
        *,
        MetricName: str,
        Namespace: str,
        Statistic: str | None = None,
        ExtendedStatistic: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        Period: int | None = None,
        Unit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_anomaly_detectors(
        self,
        *,
        AnomalyDetectorIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Namespace: str | None = None,
        MetricName: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        AnomalyDetectorTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_insight_rules(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_alarm_actions(
        self,
        *,
        AlarmNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_insight_rules(
        self,
        *,
        RuleNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_dataset_kms_key(
        self,
        *,
        DatasetIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_alarm_actions(
        self,
        *,
        AlarmNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_insight_rules(
        self,
        *,
        RuleNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_alarm_mute_rule(
        self,
        *,
        AlarmMuteRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dashboard(
        self,
        *,
        DashboardName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dataset(
        self,
        *,
        DatasetIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_rule_report(
        self,
        *,
        RuleName: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Period: int,
        MaxContributorCount: int | None = None,
        Metrics: list[str] | None = None,
        OrderBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_data_query_definition(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_stream(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_widget_image(
        self,
        *,
        MetricWidget: str,
        OutputFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_otel_enrichment(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_metrics_configuration(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_alarm_mute_rules(
        self,
        *,
        AlarmName: str | None = None,
        Statuses: list[str] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dashboards(
        self,
        *,
        DashboardNamePrefix: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_managed_insight_rules(
        self,
        *,
        ResourceARN: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metric_data_query_definitions(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metric_streams(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_alarm_mute_rule(
        self,
        *,
        Name: str,
        Rule: dict[str, Any],
        Description: str | None = None,
        MuteTargets: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StartDate: datetime.datetime | str | None = None,
        ExpireDate: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_anomaly_detector(
        self,
        *,
        Namespace: str | None = None,
        MetricName: str | None = None,
        Dimensions: list[dict[str, Any]] | None = None,
        Stat: str | None = None,
        Configuration: dict[str, Any] | None = None,
        MetricCharacteristics: dict[str, Any] | None = None,
        SingleMetricAnomalyDetector: dict[str, Any] | None = None,
        MetricMathAnomalyDetector: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_composite_alarm(
        self,
        *,
        AlarmName: str,
        AlarmRule: str,
        ActionsEnabled: bool | None = None,
        AlarmActions: list[str] | None = None,
        AlarmDescription: str | None = None,
        InsufficientDataActions: list[str] | None = None,
        OKActions: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ActionsSuppressor: str | None = None,
        ActionsSuppressorWaitPeriod: int | None = None,
        ActionsSuppressorExtensionPeriod: int | None = None,
        ActionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_dashboard(
        self,
        *,
        DashboardName: str,
        DashboardBody: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_insight_rule(
        self,
        *,
        RuleName: str,
        RuleDefinition: str,
        RuleState: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ApplyOnTransformedLogs: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_log_alarm(
        self,
        *,
        AlarmName: str,
        ScheduledQueryConfiguration: dict[str, Any],
        QueryResultsToEvaluate: int,
        QueryResultsToAlarm: int,
        Threshold: float | int,
        ComparisonOperator: str,
        AlarmDescription: str | None = None,
        ActionLogLineCount: int | None = None,
        ActionLogLineRoleArn: str | None = None,
        ActionsEnabled: bool | None = None,
        OKActions: list[str] | None = None,
        AlarmActions: list[str] | None = None,
        InsufficientDataActions: list[str] | None = None,
        TreatMissingData: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WarmUpConfiguration: dict[str, Any] | None = None,
        ActionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_managed_insight_rules(
        self,
        *,
        ManagedRules: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_data_query_definition(
        self,
        *,
        Path: str,
        Expression: str,
        Type: str,
        Id: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_stream(
        self,
        *,
        Name: str,
        FirehoseArn: str,
        RoleArn: str,
        OutputFormat: str,
        IncludeFilters: list[dict[str, Any]] | None = None,
        ExcludeFilters: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StatisticsConfigurations: list[dict[str, Any]] | None = None,
        IncludeLinkedAccountsMetrics: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_alarm_state(
        self,
        *,
        AlarmName: str,
        StateValue: str,
        StateReason: str,
        StateReasonData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metric_streams(
        self,
        *,
        Names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_otel_enrichment(
        self,
        *,
        IncludeFilters: list[dict[str, Any]] | None = None,
        ExcludeFilters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_metric_streams(
        self,
        *,
        Names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_otel_enrichment(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_otel_enrichment(
        self,
        *,
        IncludeFilters: list[dict[str, Any]] | None = None,
        ExcludeFilters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_metrics_configuration(
        self,
        *,
        ResourceArn: str,
        MetricSelections: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
