from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class StepFunctionsClient(ABC):

    @abstractmethod
    def create_activity(
        self,
        *,
        name: str,
        tags: list[dict[str, Any]] | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_state_machine(
        self,
        *,
        name: str,
        definition: str,
        roleArn: str,
        type: str | None = None,
        loggingConfiguration: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        tracingConfiguration: dict[str, Any] | None = None,
        publish: bool | None = None,
        versionDescription: str | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_state_machine_alias(
        self,
        *,
        name: str,
        routingConfiguration: list[dict[str, Any]],
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_activity(
        self,
        *,
        activityArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_state_machine(
        self,
        *,
        stateMachineArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_state_machine_alias(
        self,
        *,
        stateMachineAliasArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_state_machine_version(
        self,
        *,
        stateMachineVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_activity(
        self,
        *,
        activityArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_execution(
        self,
        *,
        executionArn: str,
        includedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_map_run(
        self,
        *,
        mapRunArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_state_machine(
        self,
        *,
        stateMachineArn: str,
        includedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_state_machine_alias(
        self,
        *,
        stateMachineAliasArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_state_machine_for_execution(
        self,
        *,
        executionArn: str,
        includedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_activity_task(
        self,
        *,
        activityArn: str,
        workerName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_execution_history(
        self,
        *,
        executionArn: str,
        maxResults: int | None = None,
        reverseOrder: bool | None = None,
        nextToken: str | None = None,
        includeExecutionData: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_activities(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_executions(
        self,
        *,
        stateMachineArn: str | None = None,
        statusFilter: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        mapRunArn: str | None = None,
        redriveFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_map_runs(
        self,
        *,
        executionArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_state_machine_aliases(
        self,
        *,
        stateMachineArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_state_machine_versions(
        self,
        *,
        stateMachineArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_state_machines(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
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
    def publish_state_machine_version(
        self,
        *,
        stateMachineArn: str,
        revisionId: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def redrive_execution(
        self,
        *,
        executionArn: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_task_failure(
        self,
        *,
        taskToken: str,
        error: str | None = None,
        cause: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_task_heartbeat(
        self,
        *,
        taskToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_task_success(
        self,
        *,
        taskToken: str,
        output: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_execution(
        self,
        *,
        stateMachineArn: str,
        name: str | None = None,
        input: str | None = None,
        traceHeader: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_sync_execution(
        self,
        *,
        stateMachineArn: str,
        name: str | None = None,
        input: str | None = None,
        traceHeader: str | None = None,
        includedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_execution(
        self,
        *,
        executionArn: str,
        error: str | None = None,
        cause: str | None = None,
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
    def test_state(
        self,
        *,
        definition: str,
        roleArn: str | None = None,
        input: str | None = None,
        inspectionLevel: str | None = None,
        revealSecrets: bool | None = None,
        variables: str | None = None,
        stateName: str | None = None,
        mock: dict[str, Any] | None = None,
        context: str | None = None,
        stateConfiguration: dict[str, Any] | None = None,
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
    def update_map_run(
        self,
        *,
        mapRunArn: str,
        maxConcurrency: int | None = None,
        toleratedFailurePercentage: float | int | None = None,
        toleratedFailureCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_state_machine(
        self,
        *,
        stateMachineArn: str,
        definition: str | None = None,
        roleArn: str | None = None,
        loggingConfiguration: dict[str, Any] | None = None,
        tracingConfiguration: dict[str, Any] | None = None,
        publish: bool | None = None,
        versionDescription: str | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_state_machine_alias(
        self,
        *,
        stateMachineAliasArn: str,
        description: str | None = None,
        routingConfiguration: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_state_machine_definition(
        self,
        *,
        definition: str,
        type: str | None = None,
        severity: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
