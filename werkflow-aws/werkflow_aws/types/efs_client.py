from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class EFSClient(ABC):

    @abstractmethod
    def create_access_point(
        self,
        *,
        ClientToken: str,
        FileSystemId: str,
        Tags: list[dict[str, Any]] | None = None,
        PosixUser: dict[str, Any] | None = None,
        RootDirectory: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_file_system(
        self,
        *,
        CreationToken: str,
        PerformanceMode: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
        ThroughputMode: str | None = None,
        ProvisionedThroughputInMibps: float | int | None = None,
        AvailabilityZoneName: str | None = None,
        Backup: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_mount_target(
        self,
        *,
        FileSystemId: str,
        SubnetId: str,
        IpAddress: str | None = None,
        Ipv6Address: str | None = None,
        IpAddressType: str | None = None,
        SecurityGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_configuration(
        self,
        *,
        SourceFileSystemId: str,
        Destinations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tags(
        self,
        *,
        FileSystemId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_point(
        self,
        *,
        AccessPointId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file_system(
        self,
        *,
        FileSystemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file_system_policy(
        self,
        *,
        FileSystemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_mount_target(
        self,
        *,
        MountTargetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_configuration(
        self,
        *,
        SourceFileSystemId: str,
        DeletionMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        FileSystemId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_access_points(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        AccessPointId: str | None = None,
        FileSystemId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_preferences(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backup_policy(
        self,
        *,
        FileSystemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_system_policy(
        self,
        *,
        FileSystemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_systems(
        self,
        *,
        MaxItems: int | None = None,
        Marker: str | None = None,
        CreationToken: str | None = None,
        FileSystemId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lifecycle_configuration(
        self,
        *,
        FileSystemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mount_target_security_groups(
        self,
        *,
        MountTargetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mount_targets(
        self,
        *,
        MaxItems: int | None = None,
        Marker: str | None = None,
        FileSystemId: str | None = None,
        MountTargetId: str | None = None,
        AccessPointId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_configurations(
        self,
        *,
        FileSystemId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        FileSystemId: str,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_mount_target_security_groups(
        self,
        *,
        MountTargetId: str,
        SecurityGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_preferences(
        self,
        *,
        ResourceIdType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_backup_policy(
        self,
        *,
        FileSystemId: str,
        BackupPolicy: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_file_system_policy(
        self,
        *,
        FileSystemId: str,
        Policy: str,
        BypassPolicyLockoutSafetyCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_lifecycle_configuration(
        self,
        *,
        FileSystemId: str,
        LifecyclePolicies: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ThroughputMode: str | None = None,
        ProvisionedThroughputInMibps: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_file_system_protection(
        self,
        *,
        FileSystemId: str,
        ReplicationOverwriteProtection: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
