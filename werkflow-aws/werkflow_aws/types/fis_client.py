from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class FISClient(ABC):

    @abstractmethod
    def create_experiment_template(
        self,
        *,
        clientToken: str,
        description: str,
        stopConditions: list[dict[str, Any]],
        actions: dict[str, dict[str, Any]],
        roleArn: str,
        targets: dict[str, dict[str, Any]] | None = None,
        tags: dict[str, str] | None = None,
        logConfiguration: dict[str, Any] | None = None,
        experimentOptions: dict[str, Any] | None = None,
        experimentReportConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str,
        clientToken: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_experiment_template(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_action(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_experiment(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_experiment_target_account_configuration(
        self,
        *,
        experimentId: str,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_experiment_template(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_safety_lever(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_target_resource_type(
        self,
        *,
        resourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_actions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiment_resolved_targets(
        self,
        *,
        experimentId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        targetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiment_target_account_configurations(
        self,
        *,
        experimentId: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiment_templates(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiments(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        experimentTemplateId: str | None = None,
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
    def list_target_account_configurations(
        self,
        *,
        experimentTemplateId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_target_resource_types(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_experiment(
        self,
        *,
        clientToken: str,
        experimentTemplateId: str,
        experimentOptions: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_experiment(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_experiment_template(
        self,
        *,
        id: str,
        description: str | None = None,
        stopConditions: list[dict[str, Any]] | None = None,
        targets: dict[str, dict[str, Any]] | None = None,
        actions: dict[str, dict[str, Any]] | None = None,
        roleArn: str | None = None,
        logConfiguration: dict[str, Any] | None = None,
        experimentOptions: dict[str, Any] | None = None,
        experimentReportConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_safety_lever_state(
        self,
        *,
        id: str,
        state: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
