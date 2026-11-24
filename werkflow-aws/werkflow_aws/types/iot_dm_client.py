from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class IoTJobsDataClient(ABC):

    @abstractmethod
    def describe_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        includeJobDocument: bool | None = None,
        executionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pending_job_executions(
        self,
        *,
        thingName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_command_execution(
        self,
        *,
        targetArn: str,
        commandArn: str,
        parameters: dict[str, dict[str, Any]] | None = None,
        executionTimeoutSeconds: int | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_next_pending_job_execution(
        self,
        *,
        thingName: str,
        statusDetails: dict[str, str] | None = None,
        stepTimeoutInMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        status: str,
        statusDetails: dict[str, str] | None = None,
        stepTimeoutInMinutes: int | None = None,
        expectedVersion: int | None = None,
        includeJobExecutionState: bool | None = None,
        includeJobDocument: bool | None = None,
        executionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
