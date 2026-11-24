from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class SchedulerClient(ABC):

    @abstractmethod
    def create_schedule(
        self,
        *,
        Name: str,
        ScheduleExpression: str,
        Target: dict[str, Any],
        FlexibleTimeWindow: dict[str, Any],
        GroupName: str | None = None,
        StartDate: datetime.datetime | str | None = None,
        EndDate: datetime.datetime | str | None = None,
        Description: str | None = None,
        ScheduleExpressionTimezone: str | None = None,
        State: str | None = None,
        KmsKeyArn: str | None = None,
        ClientToken: str | None = None,
        ActionAfterCompletion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_schedule_group(
        self,
        *,
        Name: str,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_schedule(
        self,
        *,
        Name: str,
        GroupName: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_schedule_group(
        self,
        *,
        Name: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schedule(
        self,
        *,
        Name: str,
        GroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schedule_group(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schedule_groups(
        self,
        *,
        NamePrefix: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schedules(
        self,
        *,
        GroupName: str | None = None,
        NamePrefix: str | None = None,
        State: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
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
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_schedule(
        self,
        *,
        Name: str,
        ScheduleExpression: str,
        Target: dict[str, Any],
        FlexibleTimeWindow: dict[str, Any],
        GroupName: str | None = None,
        StartDate: datetime.datetime | str | None = None,
        EndDate: datetime.datetime | str | None = None,
        Description: str | None = None,
        ScheduleExpressionTimezone: str | None = None,
        State: str | None = None,
        KmsKeyArn: str | None = None,
        ClientToken: str | None = None,
        ActionAfterCompletion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
