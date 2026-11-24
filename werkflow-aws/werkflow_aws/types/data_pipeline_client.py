from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class DataPipelineClient(ABC):

    @abstractmethod
    def activate_pipeline(
        self,
        *,
        pipelineId: str,
        parameterValues: list[dict[str, Any]] | None = None,
        startTimestamp: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags(
        self,
        *,
        pipelineId: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pipeline(
        self,
        *,
        name: str,
        uniqueId: str,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_pipeline(
        self,
        *,
        pipelineId: str,
        cancelActive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pipeline(
        self,
        *,
        pipelineId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_objects(
        self,
        *,
        pipelineId: str,
        objectIds: list[str],
        evaluateExpressions: bool | None = None,
        marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pipelines(
        self,
        *,
        pipelineIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evaluate_expression(
        self,
        *,
        pipelineId: str,
        objectId: str,
        expression: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pipeline_definition(
        self,
        *,
        pipelineId: str,
        version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipelines(
        self,
        *,
        marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def poll_for_task(
        self,
        *,
        workerGroup: str,
        hostname: str | None = None,
        instanceIdentity: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_pipeline_definition(
        self,
        *,
        pipelineId: str,
        pipelineObjects: list[dict[str, Any]],
        parameterObjects: list[dict[str, Any]] | None = None,
        parameterValues: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query_objects(
        self,
        *,
        pipelineId: str,
        sphere: str,
        query: dict[str, Any] | None = None,
        marker: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags(
        self,
        *,
        pipelineId: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def report_task_progress(
        self,
        *,
        taskId: str,
        fields: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def report_task_runner_heartbeat(
        self,
        *,
        taskrunnerId: str,
        workerGroup: str | None = None,
        hostname: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_status(
        self,
        *,
        pipelineId: str,
        objectIds: list[str],
        status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_task_status(
        self,
        *,
        taskId: str,
        taskStatus: str,
        errorId: str | None = None,
        errorMessage: str | None = None,
        errorStackTrace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_pipeline_definition(
        self,
        *,
        pipelineId: str,
        pipelineObjects: list[dict[str, Any]],
        parameterObjects: list[dict[str, Any]] | None = None,
        parameterValues: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
