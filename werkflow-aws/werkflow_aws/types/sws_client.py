from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SWFClient(ABC):

    @abstractmethod
    def count_closed_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: dict[str, Any] | None = None,
        closeTimeFilter: dict[str, Any] | None = None,
        executionFilter: dict[str, Any] | None = None,
        typeFilter: dict[str, Any] | None = None,
        tagFilter: dict[str, Any] | None = None,
        closeStatusFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def count_open_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: dict[str, Any],
        typeFilter: dict[str, Any] | None = None,
        tagFilter: dict[str, Any] | None = None,
        executionFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def count_pending_activity_tasks(
        self,
        *,
        domain: str,
        taskList: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def count_pending_decision_tasks(
        self,
        *,
        domain: str,
        taskList: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_activity_type(
        self,
        *,
        domain: str,
        activityType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workflow_type(
        self,
        *,
        domain: str,
        workflowType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprecate_activity_type(
        self,
        *,
        domain: str,
        activityType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprecate_domain(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprecate_workflow_type(
        self,
        *,
        domain: str,
        workflowType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_activity_type(
        self,
        *,
        domain: str,
        activityType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workflow_execution(
        self,
        *,
        domain: str,
        execution: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workflow_type(
        self,
        *,
        domain: str,
        workflowType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow_execution_history(
        self,
        *,
        domain: str,
        execution: dict[str, Any],
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_activity_types(
        self,
        *,
        domain: str,
        registrationStatus: str,
        name: str | None = None,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_closed_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: dict[str, Any] | None = None,
        closeTimeFilter: dict[str, Any] | None = None,
        executionFilter: dict[str, Any] | None = None,
        closeStatusFilter: dict[str, Any] | None = None,
        typeFilter: dict[str, Any] | None = None,
        tagFilter: dict[str, Any] | None = None,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        registrationStatus: str,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_open_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: dict[str, Any],
        typeFilter: dict[str, Any] | None = None,
        tagFilter: dict[str, Any] | None = None,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
        executionFilter: dict[str, Any] | None = None,
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
    def list_workflow_types(
        self,
        *,
        domain: str,
        registrationStatus: str,
        name: str | None = None,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def poll_for_activity_task(
        self,
        *,
        domain: str,
        taskList: dict[str, Any],
        identity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def poll_for_decision_task(
        self,
        *,
        domain: str,
        taskList: dict[str, Any],
        identity: str | None = None,
        nextPageToken: str | None = None,
        maximumPageSize: int | None = None,
        reverseOrder: bool | None = None,
        startAtPreviousStartedEvent: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def record_activity_task_heartbeat(
        self,
        *,
        taskToken: str,
        details: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_activity_type(
        self,
        *,
        domain: str,
        name: str,
        version: str,
        description: str | None = None,
        defaultTaskStartToCloseTimeout: str | None = None,
        defaultTaskHeartbeatTimeout: str | None = None,
        defaultTaskList: dict[str, Any] | None = None,
        defaultTaskPriority: str | None = None,
        defaultTaskScheduleToStartTimeout: str | None = None,
        defaultTaskScheduleToCloseTimeout: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_domain(
        self,
        *,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_workflow_type(
        self,
        *,
        domain: str,
        name: str,
        version: str,
        description: str | None = None,
        defaultTaskStartToCloseTimeout: str | None = None,
        defaultExecutionStartToCloseTimeout: str | None = None,
        defaultTaskList: dict[str, Any] | None = None,
        defaultTaskPriority: str | None = None,
        defaultChildPolicy: str | None = None,
        defaultLambdaRole: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_cancel_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        runId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def respond_activity_task_canceled(
        self,
        *,
        taskToken: str,
        details: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def respond_activity_task_completed(
        self,
        *,
        taskToken: str,
        result: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def respond_activity_task_failed(
        self,
        *,
        taskToken: str,
        reason: str | None = None,
        details: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def respond_decision_task_completed(
        self,
        *,
        taskToken: str,
        decisions: list[dict[str, Any]] | None = None,
        executionContext: str | None = None,
        taskList: dict[str, Any] | None = None,
        taskListScheduleToStartTimeout: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def signal_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        signalName: str,
        runId: str | None = None,
        input: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        workflowType: dict[str, Any],
        taskList: dict[str, Any] | None = None,
        taskPriority: str | None = None,
        input: str | None = None,
        executionStartToCloseTimeout: str | None = None,
        tagList: list[str] | None = None,
        taskStartToCloseTimeout: str | None = None,
        childPolicy: str | None = None,
        lambdaRole: str | None = None,
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
    def terminate_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        runId: str | None = None,
        reason: str | None = None,
        details: str | None = None,
        childPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def undeprecate_activity_type(
        self,
        *,
        domain: str,
        activityType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def undeprecate_domain(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def undeprecate_workflow_type(
        self,
        *,
        domain: str,
        workflowType: dict[str, Any],
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
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
