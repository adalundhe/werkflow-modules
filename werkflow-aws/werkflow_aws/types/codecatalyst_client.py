from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class CodeCatalystClient(ABC):

    @abstractmethod
    def create_access_token(
        self,
        *,
        name: str,
        expiresTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        instanceType: str,
        persistentStorage: dict[str, Any],
        repositories: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
        alias: str | None = None,
        ides: list[dict[str, Any]] | None = None,
        inactivityTimeoutMinutes: int | None = None,
        vpcConnectionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        spaceName: str,
        displayName: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_source_repository(
        self,
        *,
        spaceName: str,
        projectName: str,
        name: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_source_repository_branch(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        name: str,
        headCommitId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_token(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        spaceName: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_source_repository(
        self,
        *,
        spaceName: str,
        projectName: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_space(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project(
        self,
        *,
        spaceName: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_source_repository(
        self,
        *,
        spaceName: str,
        projectName: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_source_repository_clone_urls(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_space(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription(
        self,
        *,
        spaceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_details(
        self,
        *,
        id: str | None = None,
        userName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow(
        self,
        *,
        spaceName: str,
        id: str,
        projectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow_run(
        self,
        *,
        spaceName: str,
        id: str,
        projectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_tokens(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dev_environment_sessions(
        self,
        *,
        spaceName: str,
        projectName: str,
        devEnvironmentId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dev_environments(
        self,
        *,
        spaceName: str,
        projectName: str | None = None,
        filters: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_logs(
        self,
        *,
        spaceName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        eventName: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        spaceName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_source_repositories(
        self,
        *,
        spaceName: str,
        projectName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_source_repository_branches(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_spaces(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workflow_runs(
        self,
        *,
        spaceName: str,
        projectName: str,
        workflowId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        sortBy: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workflows(
        self,
        *,
        spaceName: str,
        projectName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        sortBy: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        ides: list[dict[str, Any]] | None = None,
        instanceType: str | None = None,
        inactivityTimeoutMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dev_environment_session(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        sessionConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_workflow_run(
        self,
        *,
        spaceName: str,
        projectName: str,
        workflowId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_dev_environment_session(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        sessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        alias: str | None = None,
        ides: list[dict[str, Any]] | None = None,
        instanceType: str | None = None,
        inactivityTimeoutMinutes: int | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        spaceName: str,
        name: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_space(
        self,
        *,
        name: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_session(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
