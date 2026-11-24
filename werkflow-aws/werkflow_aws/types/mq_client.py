from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class MQClient(ABC):

    @abstractmethod
    def create_broker(
        self,
        *,
        BrokerName: str,
        DeploymentMode: str,
        EngineType: str,
        HostInstanceType: str,
        PubliclyAccessible: bool,
        AuthenticationStrategy: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        Configuration: dict[str, Any] | None = None,
        CreatorRequestId: str | None = None,
        EncryptionOptions: dict[str, Any] | None = None,
        EngineVersion: str | None = None,
        LdapServerMetadata: dict[str, Any] | None = None,
        Logs: dict[str, Any] | None = None,
        MaintenanceWindowStartTime: dict[str, Any] | None = None,
        SecurityGroups: list[str] | None = None,
        StorageSize: int | None = None,
        StorageType: str | None = None,
        SubnetIds: list[str] | None = None,
        Tags: dict[str, str] | None = None,
        Users: list[dict[str, Any]] | None = None,
        DataReplicationMode: str | None = None,
        DataReplicationPrimaryBrokerArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration(
        self,
        *,
        EngineType: str,
        Name: str,
        AuthenticationStrategy: str | None = None,
        EngineVersion: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tags(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        BrokerId: str,
        Password: str,
        Username: str,
        ConsoleAccess: bool | None = None,
        Groups: list[str] | None = None,
        ReplicationUser: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_broker(
        self,
        *,
        BrokerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration(
        self,
        *,
        ConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        BrokerId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_broker(
        self,
        *,
        BrokerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_broker_engine_types(
        self,
        *,
        EngineType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_broker_instance_options(
        self,
        *,
        EngineType: str | None = None,
        HostInstanceType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        StorageType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration(
        self,
        *,
        ConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_revision(
        self,
        *,
        ConfigurationId: str,
        ConfigurationRevision: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_shared_resources(
        self,
        *,
        BrokerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user(
        self,
        *,
        BrokerId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_brokers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_revisions(
        self,
        *,
        ConfigurationId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configurations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        BrokerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def promote(
        self,
        *,
        BrokerId: str,
        Mode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_broker(
        self,
        *,
        BrokerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_broker(
        self,
        *,
        BrokerId: str,
        AuthenticationStrategy: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        Configuration: dict[str, Any] | None = None,
        EngineVersion: str | None = None,
        HostInstanceType: str | None = None,
        LdapServerMetadata: dict[str, Any] | None = None,
        Logs: dict[str, Any] | None = None,
        MaintenanceWindowStartTime: dict[str, Any] | None = None,
        ResourceShareArns: list[str] | None = None,
        SecurityGroups: list[str] | None = None,
        StorageSize: int | None = None,
        DataReplicationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_configuration(
        self,
        *,
        ConfigurationId: str,
        Data: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool | None = None,
        Groups: list[str] | None = None,
        Password: str | None = None,
        ReplicationUser: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
