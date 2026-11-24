from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class XRayClient(ABC):

    @abstractmethod
    def batch_get_traces(
        self,
        *,
        TraceIds: list[str],
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_trace_retrieval(
        self,
        *,
        RetrievalToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group(
        self,
        *,
        GroupName: str,
        FilterExpression: str | None = None,
        InsightsConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_sampling_rule(
        self,
        *,
        SamplingRule: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        GroupName: str | None = None,
        GroupARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        PolicyName: str,
        PolicyRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_sampling_rule(
        self,
        *,
        RuleName: str | None = None,
        RuleARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_encryption_config(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group(
        self,
        *,
        GroupName: str | None = None,
        GroupARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_groups(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_indexing_rules(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight(
        self,
        *,
        InsightId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_events(
        self,
        *,
        InsightId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_impact_graph(
        self,
        *,
        InsightId: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_summaries(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        States: list[str] | None = None,
        GroupARN: str | None = None,
        GroupName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_retrieved_traces_graph(
        self,
        *,
        RetrievalToken: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sampling_rules(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sampling_statistic_summaries(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sampling_targets(
        self,
        *,
        SamplingStatisticsDocuments: list[dict[str, Any]],
        SamplingBoostStatisticsDocuments: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service_graph(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        GroupName: str | None = None,
        GroupARN: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_time_series_service_statistics(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        GroupName: str | None = None,
        GroupARN: str | None = None,
        EntitySelectorExpression: str | None = None,
        Period: int | None = None,
        ForecastStatistics: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trace_graph(
        self,
        *,
        TraceIds: list[str],
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trace_segment_destination(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trace_summaries(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        TimeRangeType: str | None = None,
        Sampling: bool | None = None,
        SamplingStrategy: dict[str, Any] | None = None,
        FilterExpression: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_policies(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_retrieved_traces(
        self,
        *,
        RetrievalToken: str,
        TraceFormat: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_encryption_config(
        self,
        *,
        Type: str,
        KeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        PolicyName: str,
        PolicyDocument: str,
        PolicyRevisionId: str | None = None,
        BypassPolicyLockoutCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_telemetry_records(
        self,
        *,
        TelemetryRecords: list[dict[str, Any]],
        EC2InstanceId: str | None = None,
        Hostname: str | None = None,
        ResourceARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_trace_segments(
        self,
        *,
        TraceSegmentDocuments: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_trace_retrieval(
        self,
        *,
        TraceIds: list[str],
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
    ) -> dict[str, Any]:
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
    def update_group(
        self,
        *,
        GroupName: str | None = None,
        GroupARN: str | None = None,
        FilterExpression: str | None = None,
        InsightsConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_indexing_rule(
        self,
        *,
        Name: str,
        Rule: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_sampling_rule(
        self,
        *,
        SamplingRuleUpdate: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trace_segment_destination(
        self,
        *,
        Destination: str | None = None,
        CloudWatchLogsConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
