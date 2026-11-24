from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class DataSyncClient(ABC):

    @abstractmethod
    def cancel_task_execution(
        self,
        *,
        TaskExecutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_agent(
        self,
        *,
        ActivationKey: str,
        AgentName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VpcEndpointId: str | None = None,
        SubnetArns: list[str] | None = None,
        SecurityGroupArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_azure_blob(
        self,
        *,
        ContainerUrl: str,
        AuthenticationType: str,
        SasConfiguration: dict[str, Any] | None = None,
        FederatedIdentity: dict[str, Any] | None = None,
        BlobType: str | None = None,
        AccessTier: str | None = None,
        Subdirectory: str | None = None,
        AgentArns: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_efs(
        self,
        *,
        EfsFilesystemArn: str,
        Ec2Config: dict[str, Any],
        Subdirectory: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AccessPointArn: str | None = None,
        FileSystemAccessRoleArn: str | None = None,
        InTransitEncryption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_fsx_lustre(
        self,
        *,
        FsxFilesystemArn: str,
        SecurityGroupArns: list[str],
        Subdirectory: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_fsx_ontap(
        self,
        *,
        Protocol: dict[str, Any],
        SecurityGroupArns: list[str],
        StorageVirtualMachineArn: str,
        Subdirectory: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_fsx_open_zfs(
        self,
        *,
        FsxFilesystemArn: str,
        Protocol: dict[str, Any],
        SecurityGroupArns: list[str],
        Subdirectory: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_fsx_windows(
        self,
        *,
        FsxFilesystemArn: str,
        SecurityGroupArns: list[str],
        User: str,
        Subdirectory: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Domain: str | None = None,
        Password: str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_hdfs(
        self,
        *,
        NameNodes: list[dict[str, Any]],
        AuthenticationType: str,
        AgentArns: list[str],
        Subdirectory: str | None = None,
        BlockSize: int | None = None,
        ReplicationFactor: int | None = None,
        KmsKeyProviderUri: str | None = None,
        QopConfiguration: dict[str, Any] | None = None,
        SimpleUser: str | None = None,
        KerberosPrincipal: str | None = None,
        KerberosKeytab: bytes | BinaryIO | str | None = None,
        KerberosKrb5Conf: bytes | BinaryIO | str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_nfs(
        self,
        *,
        Subdirectory: str,
        ServerHostname: str,
        OnPremConfig: dict[str, Any],
        MountOptions: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_object_storage(
        self,
        *,
        ServerHostname: str,
        BucketName: str,
        ServerPort: int | None = None,
        ServerProtocol: str | None = None,
        Subdirectory: str | None = None,
        AccessKey: str | None = None,
        SecretKey: str | None = None,
        FederatedIdentity: dict[str, Any] | None = None,
        AgentArns: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ServerCertificate: bytes | BinaryIO | str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_s3(
        self,
        *,
        S3BucketArn: str,
        S3Config: dict[str, Any],
        Subdirectory: str | None = None,
        S3StorageClass: str | None = None,
        AgentArns: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_location_smb(
        self,
        *,
        Subdirectory: str,
        ServerHostname: str,
        AgentArns: list[str],
        User: str | None = None,
        Domain: str | None = None,
        Password: str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
        MountOptions: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AuthenticationType: str | None = None,
        DnsIpAddresses: list[str] | None = None,
        KerberosPrincipal: str | None = None,
        KerberosKeytab: bytes | BinaryIO | str | None = None,
        KerberosKrb5Conf: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_task(
        self,
        *,
        SourceLocationArn: str,
        DestinationLocationArn: str,
        CloudWatchLogGroupArn: str | None = None,
        Name: str | None = None,
        Options: dict[str, Any] | None = None,
        Excludes: list[dict[str, Any]] | None = None,
        Schedule: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Includes: list[dict[str, Any]] | None = None,
        ManifestConfig: dict[str, Any] | None = None,
        TaskReportConfig: dict[str, Any] | None = None,
        TaskMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_agent(
        self,
        *,
        AgentArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_location(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_task(
        self,
        *,
        TaskArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_agent(
        self,
        *,
        AgentArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_azure_blob(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_efs(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_fsx_lustre(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_fsx_ontap(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_fsx_open_zfs(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_fsx_windows(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_hdfs(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_nfs(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_object_storage(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_s3(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_location_smb(
        self,
        *,
        LocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_task(
        self,
        *,
        TaskArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_task_execution(
        self,
        *,
        TaskExecutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_agents(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_locations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_task_executions(
        self,
        *,
        TaskArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tasks(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_task_execution(
        self,
        *,
        TaskArn: str,
        OverrideOptions: dict[str, Any] | None = None,
        Includes: list[dict[str, Any]] | None = None,
        Excludes: list[dict[str, Any]] | None = None,
        ManifestConfig: dict[str, Any] | None = None,
        TaskReportConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        Keys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_agent(
        self,
        *,
        AgentArn: str,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_azure_blob(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        AuthenticationType: str | None = None,
        SasConfiguration: dict[str, Any] | None = None,
        FederatedIdentity: dict[str, Any] | None = None,
        BlobType: str | None = None,
        AccessTier: str | None = None,
        AgentArns: list[str] | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_efs(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        AccessPointArn: str | None = None,
        FileSystemAccessRoleArn: str | None = None,
        InTransitEncryption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_fsx_lustre(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_fsx_ontap(
        self,
        *,
        LocationArn: str,
        Protocol: dict[str, Any] | None = None,
        Subdirectory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_fsx_open_zfs(
        self,
        *,
        LocationArn: str,
        Protocol: dict[str, Any] | None = None,
        Subdirectory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_fsx_windows(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        Domain: str | None = None,
        User: str | None = None,
        Password: str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_hdfs(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        NameNodes: list[dict[str, Any]] | None = None,
        BlockSize: int | None = None,
        ReplicationFactor: int | None = None,
        KmsKeyProviderUri: str | None = None,
        QopConfiguration: dict[str, Any] | None = None,
        AuthenticationType: str | None = None,
        SimpleUser: str | None = None,
        KerberosPrincipal: str | None = None,
        KerberosKeytab: bytes | BinaryIO | str | None = None,
        KerberosKrb5Conf: bytes | BinaryIO | str | None = None,
        AgentArns: list[str] | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_nfs(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        ServerHostname: str | None = None,
        OnPremConfig: dict[str, Any] | None = None,
        MountOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_object_storage(
        self,
        *,
        LocationArn: str,
        ServerPort: int | None = None,
        ServerProtocol: str | None = None,
        Subdirectory: str | None = None,
        ServerHostname: str | None = None,
        AccessKey: str | None = None,
        SecretKey: str | None = None,
        FederatedIdentity: dict[str, Any] | None = None,
        AgentArns: list[str] | None = None,
        ServerCertificate: bytes | BinaryIO | str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_s3(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        S3StorageClass: str | None = None,
        S3Config: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_location_smb(
        self,
        *,
        LocationArn: str,
        Subdirectory: str | None = None,
        ServerHostname: str | None = None,
        User: str | None = None,
        Domain: str | None = None,
        Password: str | None = None,
        CmkSecretConfig: dict[str, Any] | None = None,
        CustomSecretConfig: dict[str, Any] | None = None,
        AgentArns: list[str] | None = None,
        MountOptions: dict[str, Any] | None = None,
        AuthenticationType: str | None = None,
        DnsIpAddresses: list[str] | None = None,
        KerberosPrincipal: str | None = None,
        KerberosKeytab: bytes | BinaryIO | str | None = None,
        KerberosKrb5Conf: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_task(
        self,
        *,
        TaskArn: str,
        Options: dict[str, Any] | None = None,
        Excludes: list[dict[str, Any]] | None = None,
        Schedule: dict[str, Any] | None = None,
        Name: str | None = None,
        CloudWatchLogGroupArn: str | None = None,
        Includes: list[dict[str, Any]] | None = None,
        ManifestConfig: dict[str, Any] | None = None,
        TaskReportConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_task_execution(
        self,
        *,
        TaskExecutionArn: str,
        Options: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
