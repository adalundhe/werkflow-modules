from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AppFlowClient(ABC):

    @abstractmethod
    def cancel_flow_executions(
        self,
        *,
        flowName: str,
        executionIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectorType: str,
        connectionMode: str,
        connectorProfileConfig: dict[str, Any],
        kmsArn: str | None = None,
        connectorLabel: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_flow(
        self,
        *,
        flowName: str,
        triggerConfig: dict[str, Any],
        sourceFlowConfig: dict[str, Any],
        destinationFlowConfigList: list[dict[str, Any]],
        tasks: list[dict[str, Any]],
        description: str | None = None,
        kmsArn: str | None = None,
        tags: dict[str, str] | None = None,
        metadataCatalogConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connector_profile(
        self,
        *,
        connectorProfileName: str,
        forceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_flow(
        self,
        *,
        flowName: str,
        forceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connector(
        self,
        *,
        connectorType: str,
        connectorLabel: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connector_entity(
        self,
        *,
        connectorEntityName: str,
        connectorType: str | None = None,
        connectorProfileName: str | None = None,
        apiVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connector_profiles(
        self,
        *,
        connectorProfileNames: list[str] | None = None,
        connectorType: str | None = None,
        connectorLabel: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connectors(
        self,
        *,
        connectorTypes: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flow(
        self,
        *,
        flowName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flow_execution_records(
        self,
        *,
        flowName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connector_entities(
        self,
        *,
        connectorProfileName: str | None = None,
        connectorType: str | None = None,
        entitiesPath: str | None = None,
        apiVersion: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connectors(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flows(
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
    def register_connector(
        self,
        *,
        connectorLabel: str | None = None,
        description: str | None = None,
        connectorProvisioningType: str | None = None,
        connectorProvisioningConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_connector_metadata_cache(
        self,
        *,
        connectorProfileName: str | None = None,
        connectorType: str | None = None,
        connectorEntityName: str | None = None,
        entitiesPath: str | None = None,
        apiVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_flow(
        self,
        *,
        flowName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_flow(
        self,
        *,
        flowName: str,
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
    def unregister_connector(
        self,
        *,
        connectorLabel: str,
        forceDelete: bool | None = None,
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
    def update_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectionMode: str,
        connectorProfileConfig: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connector_registration(
        self,
        *,
        connectorLabel: str,
        description: str | None = None,
        connectorProvisioningConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_flow(
        self,
        *,
        flowName: str,
        triggerConfig: dict[str, Any],
        sourceFlowConfig: dict[str, Any],
        destinationFlowConfigList: list[dict[str, Any]],
        tasks: list[dict[str, Any]],
        description: str | None = None,
        metadataCatalogConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
