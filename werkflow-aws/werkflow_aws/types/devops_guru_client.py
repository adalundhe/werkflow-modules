from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class DevOpsGuruClient(ABC):

    @abstractmethod
    def add_notification_channel(
        self,
        *,
        Config: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_insight(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_health(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_overview(
        self,
        *,
        FromTime: datetime.datetime | str,
        ToTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_anomaly(
        self,
        *,
        Id: str,
        AccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_sources_config(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_feedback(
        self,
        *,
        InsightId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_insight(
        self,
        *,
        Id: str,
        AccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_health(
        self,
        *,
        AccountIds: list[str] | None = None,
        OrganizationalUnitIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_overview(
        self,
        *,
        FromTime: datetime.datetime | str,
        ToTime: datetime.datetime | str | None = None,
        AccountIds: list[str] | None = None,
        OrganizationalUnitIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_resource_collection_health(
        self,
        *,
        OrganizationResourceCollectionType: str,
        AccountIds: list[str] | None = None,
        OrganizationalUnitIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_collection_health(
        self,
        *,
        ResourceCollectionType: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_integration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_estimation(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_collection(
        self,
        *,
        ResourceCollectionType: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_anomalies_for_insight(
        self,
        *,
        InsightId: str,
        StartTimeRange: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        AccountId: str | None = None,
        Filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_anomalous_log_groups(
        self,
        *,
        InsightId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_events(
        self,
        *,
        Filters: dict[str, Any],
        MaxResults: int | None = None,
        NextToken: str | None = None,
        AccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_insights(
        self,
        *,
        StatusFilter: dict[str, Any],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_monitored_resources(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notification_channels(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_insights(
        self,
        *,
        StatusFilter: dict[str, Any],
        MaxResults: int | None = None,
        AccountIds: list[str] | None = None,
        OrganizationalUnitIds: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommendations(
        self,
        *,
        InsightId: str,
        NextToken: str | None = None,
        Locale: str | None = None,
        AccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_feedback(
        self,
        *,
        InsightFeedback: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_notification_channel(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_insights(
        self,
        *,
        StartTimeRange: dict[str, Any],
        Type: str,
        Filters: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_organization_insights(
        self,
        *,
        AccountIds: list[str],
        StartTimeRange: dict[str, Any],
        Type: str,
        Filters: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_cost_estimation(
        self,
        *,
        ResourceCollection: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_event_sources_config(
        self,
        *,
        EventSources: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_collection(
        self,
        *,
        Action: str,
        ResourceCollection: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_integration(
        self,
        *,
        ServiceIntegration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
