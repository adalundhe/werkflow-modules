from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class CloudTrailClient(ABC):

    @abstractmethod
    def add_tags(
        self,
        *,
        ResourceId: str,
        TagsList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_query(
        self,
        *,
        QueryId: str,
        EventDataStore: str | None = None,
        EventDataStoreOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_channel(
        self,
        *,
        Name: str,
        Source: str,
        Destinations: list[dict[str, Any]],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dashboard(
        self,
        *,
        Name: str,
        RefreshSchedule: dict[str, Any] | None = None,
        TagsList: list[dict[str, Any]] | None = None,
        TerminationProtectionEnabled: bool | None = None,
        Widgets: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_data_store(
        self,
        *,
        Name: str,
        AdvancedEventSelectors: list[dict[str, Any]] | None = None,
        MultiRegionEnabled: bool | None = None,
        OrganizationEnabled: bool | None = None,
        RetentionPeriod: int | None = None,
        TerminationProtectionEnabled: bool | None = None,
        TagsList: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        StartIngestion: bool | None = None,
        BillingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trail(
        self,
        *,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: str | None = None,
        SnsTopicName: str | None = None,
        IncludeGlobalServiceEvents: bool | None = None,
        IsMultiRegionTrail: bool | None = None,
        EnableLogFileValidation: bool | None = None,
        CloudWatchLogsLogGroupArn: str | None = None,
        CloudWatchLogsRoleArn: str | None = None,
        KmsKeyId: str | None = None,
        IsOrganizationTrail: bool | None = None,
        TagsList: list[dict[str, Any]] | None = None,
        RecursiveLogging: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_channel(
        self,
        *,
        Channel: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dashboard(
        self,
        *,
        DashboardId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_data_store(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trail(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_organization_delegated_admin(
        self,
        *,
        DelegatedAdminAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_query(
        self,
        *,
        EventDataStore: str | None = None,
        QueryId: str | None = None,
        QueryAlias: str | None = None,
        RefreshId: str | None = None,
        EventDataStoreOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trails(
        self,
        *,
        trailNameList: list[str] | None = None,
        includeShadowTrails: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_federation(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_federation(
        self,
        *,
        EventDataStore: str,
        FederationRoleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_query(
        self,
        *,
        EventDataStores: list[str],
        Prompt: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_channel(
        self,
        *,
        Channel: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dashboard(
        self,
        *,
        DashboardId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_configuration(
        self,
        *,
        TrailName: str | None = None,
        EventDataStore: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_data_store(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_selectors(
        self,
        *,
        TrailName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_import(
        self,
        *,
        ImportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_selectors(
        self,
        *,
        TrailName: str | None = None,
        EventDataStore: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_results(
        self,
        *,
        QueryId: str,
        EventDataStore: str | None = None,
        NextToken: str | None = None,
        MaxQueryResults: int | None = None,
        EventDataStoreOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trail(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trail_status(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_channels(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dashboards(
        self,
        *,
        NamePrefix: str | None = None,
        Type: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_data_stores(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_import_failures(
        self,
        *,
        ImportId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_imports(
        self,
        *,
        MaxResults: int | None = None,
        Destination: str | None = None,
        ImportStatus: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_insights_data(
        self,
        *,
        InsightSource: str,
        DataType: str,
        Dimensions: dict[str, str] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_insights_metric_data(
        self,
        *,
        EventSource: str,
        EventName: str,
        InsightType: str,
        TrailName: str | None = None,
        ErrorCode: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Period: int | None = None,
        DataType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_public_keys(
        self,
        *,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queries(
        self,
        *,
        EventDataStore: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        QueryStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceIdList: list[str],
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trails(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def lookup_events(
        self,
        *,
        LookupAttributes: list[dict[str, Any]] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        EventCategory: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_event_configuration(
        self,
        *,
        TrailName: str | None = None,
        EventDataStore: str | None = None,
        MaxEventSize: str | None = None,
        ContextKeySelectors: list[dict[str, Any]] | None = None,
        AggregationConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_event_selectors(
        self,
        *,
        TrailName: str,
        EventSelectors: list[dict[str, Any]] | None = None,
        AdvancedEventSelectors: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_insight_selectors(
        self,
        *,
        InsightSelectors: list[dict[str, Any]],
        TrailName: str | None = None,
        EventDataStore: str | None = None,
        InsightsDestination: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        ResourcePolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_organization_delegated_admin(
        self,
        *,
        MemberAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags(
        self,
        *,
        ResourceId: str,
        TagsList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_event_data_store(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_sample_queries(
        self,
        *,
        SearchPhrase: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dashboard_refresh(
        self,
        *,
        DashboardId: str,
        QueryParameterValues: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_event_data_store_ingestion(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_import(
        self,
        *,
        Destinations: list[str] | None = None,
        ImportSource: dict[str, Any] | None = None,
        StartEventTime: datetime.datetime | str | None = None,
        EndEventTime: datetime.datetime | str | None = None,
        ImportId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_logging(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_query(
        self,
        *,
        QueryStatement: str | None = None,
        DeliveryS3Uri: str | None = None,
        QueryAlias: str | None = None,
        QueryParameters: list[str] | None = None,
        EventDataStoreOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_event_data_store_ingestion(
        self,
        *,
        EventDataStore: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_import(
        self,
        *,
        ImportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_logging(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_channel(
        self,
        *,
        Channel: str,
        Destinations: list[dict[str, Any]] | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboard(
        self,
        *,
        DashboardId: str,
        Widgets: list[dict[str, Any]] | None = None,
        RefreshSchedule: dict[str, Any] | None = None,
        TerminationProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_event_data_store(
        self,
        *,
        EventDataStore: str,
        Name: str | None = None,
        AdvancedEventSelectors: list[dict[str, Any]] | None = None,
        MultiRegionEnabled: bool | None = None,
        OrganizationEnabled: bool | None = None,
        RetentionPeriod: int | None = None,
        TerminationProtectionEnabled: bool | None = None,
        KmsKeyId: str | None = None,
        BillingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trail(
        self,
        *,
        Name: str,
        S3BucketName: str | None = None,
        S3KeyPrefix: str | None = None,
        SnsTopicName: str | None = None,
        IncludeGlobalServiceEvents: bool | None = None,
        IsMultiRegionTrail: bool | None = None,
        EnableLogFileValidation: bool | None = None,
        CloudWatchLogsLogGroupArn: str | None = None,
        CloudWatchLogsRoleArn: str | None = None,
        KmsKeyId: str | None = None,
        IsOrganizationTrail: bool | None = None,
        RecursiveLogging: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
