from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class WorkSpacesThinClientClient(ABC):

    @abstractmethod
    def create_environment(
        self,
        *,
        desktopArn: str,
        name: str | None = None,
        desktopEndpoint: str | None = None,
        softwareSetUpdateSchedule: str | None = None,
        maintenanceWindow: dict[str, Any] | None = None,
        softwareSetUpdateMode: str | None = None,
        desiredSoftwareSetId: str | None = None,
        kmsKeyArn: str | None = None,
        clientToken: str | None = None,
        tags: dict[str, str] | None = None,
        deviceCreationTags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_device(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_device(
        self,
        *,
        id: str,
        targetDeviceStatus: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_software_set(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_devices(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environments(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_software_sets(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
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
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device(
        self,
        *,
        id: str,
        name: str | None = None,
        desiredSoftwareSetId: str | None = None,
        softwareSetUpdateSchedule: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment(
        self,
        *,
        id: str,
        name: str | None = None,
        desktopArn: str | None = None,
        desktopEndpoint: str | None = None,
        softwareSetUpdateSchedule: str | None = None,
        maintenanceWindow: dict[str, Any] | None = None,
        softwareSetUpdateMode: str | None = None,
        desiredSoftwareSetId: str | None = None,
        deviceCreationTags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_software_set(
        self,
        *,
        id: str,
        validationStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
