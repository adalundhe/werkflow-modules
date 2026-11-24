from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CloudHSMClient(ABC):

    @abstractmethod
    def copy_backup_to_region(
        self,
        *,
        DestinationRegion: str,
        BackupId: str,
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        HsmType: str,
        SubnetIds: list[str],
        BackupRetentionPolicy: dict[str, Any] | None = None,
        SourceBackupId: str | None = None,
        NetworkType: str | None = None,
        TagList: list[dict[str, Any]] | None = None,
        Mode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hsm(
        self,
        *,
        ClusterId: str,
        AvailabilityZone: str,
        IpAddress: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup(
        self,
        *,
        BackupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hsm(
        self,
        *,
        ClusterId: str,
        HsmId: str | None = None,
        EniId: str | None = None,
        EniIp: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backups(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: dict[str, list[str]] | None = None,
        Shared: bool | None = None,
        SortAscending: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_clusters(
        self,
        *,
        Filters: dict[str, list[str]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initialize_cluster(
        self,
        *,
        ClusterId: str,
        SignedCert: str,
        TrustAnchor: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_backup_attributes(
        self,
        *,
        BackupId: str,
        NeverExpires: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster(
        self,
        *,
        ClusterId: str,
        HsmType: str | None = None,
        BackupRetentionPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str | None = None,
        Policy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_backup(
        self,
        *,
        BackupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceId: str,
        TagList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceId: str,
        TagKeyList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
