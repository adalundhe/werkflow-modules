from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class TimestreamQueryClient(ABC):

    @abstractmethod
    def cancel_query(
        self,
        *,
        QueryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_scheduled_query(
        self,
        *,
        Name: str,
        QueryString: str,
        ScheduleConfiguration: dict[str, Any],
        NotificationConfiguration: dict[str, Any],
        ScheduledQueryExecutionRoleArn: str,
        ErrorReportConfiguration: dict[str, Any],
        TargetConfiguration: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduled_query(
        self,
        *,
        ScheduledQueryArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoints(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_query(
        self,
        *,
        ScheduledQueryArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_scheduled_query(
        self,
        *,
        ScheduledQueryArn: str,
        InvocationTime: datetime.datetime | str,
        ClientToken: str | None = None,
        QueryInsights: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scheduled_queries(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def prepare_query(
        self,
        *,
        QueryString: str,
        ValidateOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query(
        self,
        *,
        QueryString: str,
        ClientToken: str | None = None,
        NextToken: str | None = None,
        MaxRows: int | None = None,
        QueryInsights: dict[str, Any] | None = None,
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
    def update_account_settings(
        self,
        *,
        MaxQueryTCU: int | None = None,
        QueryPricingModel: str | None = None,
        QueryCompute: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scheduled_query(
        self,
        *,
        ScheduledQueryArn: str,
        State: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
