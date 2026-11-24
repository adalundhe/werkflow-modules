from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class TransferClient(ABC):

    @abstractmethod
    def create_access(
        self,
        *,
        Role: str,
        ServerId: str,
        ExternalId: str,
        HomeDirectory: str | None = None,
        HomeDirectoryType: str | None = None,
        HomeDirectoryMappings: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        PosixProfile: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_agreement(
        self,
        *,
        ServerId: str,
        LocalProfileId: str,
        PartnerProfileId: str,
        AccessRole: str,
        Description: str | None = None,
        BaseDirectory: str | None = None,
        Status: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        PreserveFilename: str | None = None,
        EnforceMessageSigning: str | None = None,
        CustomDirectories: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connector(
        self,
        *,
        AccessRole: str,
        Url: str | None = None,
        As2Config: dict[str, Any] | None = None,
        LoggingRole: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SftpConfig: dict[str, Any] | None = None,
        SecurityPolicyName: str | None = None,
        EgressConfig: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_profile(
        self,
        *,
        As2Id: str,
        ProfileType: str,
        CertificateIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_server(
        self,
        *,
        Certificate: str | None = None,
        Domain: str | None = None,
        EndpointDetails: dict[str, Any] | None = None,
        EndpointType: str | None = None,
        HostKey: str | None = None,
        IdentityProviderDetails: dict[str, Any] | None = None,
        IdentityProviderType: str | None = None,
        LoggingRole: str | None = None,
        PostAuthenticationLoginBanner: str | None = None,
        PreAuthenticationLoginBanner: str | None = None,
        Protocols: list[str] | None = None,
        ProtocolDetails: dict[str, Any] | None = None,
        SecurityPolicyName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WorkflowDetails: dict[str, Any] | None = None,
        StructuredLogDestinations: list[str] | None = None,
        S3StorageOptions: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
        HostKeyStorageType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str | None = None,
        HomeDirectoryType: str | None = None,
        HomeDirectoryMappings: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        PosixProfile: dict[str, Any] | None = None,
        SshPublicKeyBody: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_web_app(
        self,
        *,
        IdentityProviderDetails: dict[str, Any],
        AccessEndpoint: str | None = None,
        WebAppUnits: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WebAppEndpointPolicy: str | None = None,
        EndpointDetails: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workflow(
        self,
        *,
        Steps: list[dict[str, Any]],
        Description: str | None = None,
        OnExceptionSteps: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StructuredLogDestinations: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access(
        self,
        *,
        ServerId: str,
        ExternalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_agreement(
        self,
        *,
        AgreementId: str,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate(
        self,
        *,
        CertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connector(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_host_key(
        self,
        *,
        ServerId: str,
        HostKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_profile(
        self,
        *,
        ProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_server(
        self,
        *,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ssh_public_key(
        self,
        *,
        ServerId: str,
        SshPublicKeyId: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        ServerId: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_web_app(
        self,
        *,
        WebAppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_web_app_customization(
        self,
        *,
        WebAppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workflow(
        self,
        *,
        WorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_access(
        self,
        *,
        ServerId: str,
        ExternalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_agreement(
        self,
        *,
        AgreementId: str,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate(
        self,
        *,
        CertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connector(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_execution(
        self,
        *,
        ExecutionId: str,
        WorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_host_key(
        self,
        *,
        ServerId: str,
        HostKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_profile(
        self,
        *,
        ProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_policy(
        self,
        *,
        SecurityPolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_server(
        self,
        *,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user(
        self,
        *,
        ServerId: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_web_app(
        self,
        *,
        WebAppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_web_app_customization(
        self,
        *,
        WebAppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workflow(
        self,
        *,
        WorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_certificate(
        self,
        *,
        Usage: str,
        Certificate: str,
        CertificateChain: str | None = None,
        PrivateKey: str | None = None,
        ActiveDate: datetime.datetime | str | None = None,
        InactiveDate: datetime.datetime | str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_host_key(
        self,
        *,
        ServerId: str,
        HostKeyBody: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageType: str | None = None,
        KmsKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_ssh_public_key(
        self,
        *,
        ServerId: str,
        SshPublicKeyBody: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accesses(
        self,
        *,
        ServerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_agreements(
        self,
        *,
        ServerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificates(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connectors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_executions(
        self,
        *,
        WorkflowId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_file_transfer_results(
        self,
        *,
        ConnectorId: str,
        TransferId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_host_keys(
        self,
        *,
        ServerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_profiles(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ProfileType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_policies(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_servers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        Arn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        ServerId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_web_apps(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workflows(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_workflow_step_state(
        self,
        *,
        WorkflowId: str,
        ExecutionId: str,
        Token: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_directory_listing(
        self,
        *,
        ConnectorId: str,
        RemoteDirectoryPath: str,
        OutputDirectoryPath: str,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_file_transfer(
        self,
        *,
        ConnectorId: str,
        SendFilePaths: list[str] | None = None,
        RetrieveFilePaths: list[str] | None = None,
        LocalDirectoryPath: str | None = None,
        RemoteDirectoryPath: str | None = None,
        CustomHttpHeaders: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_remote_delete(
        self,
        *,
        ConnectorId: str,
        DeletePath: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_remote_move(
        self,
        *,
        ConnectorId: str,
        SourcePath: str,
        TargetPath: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_server(
        self,
        *,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_server(
        self,
        *,
        ServerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        Arn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_connection(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_identity_provider(
        self,
        *,
        ServerId: str,
        UserName: str,
        ServerProtocol: str | None = None,
        SourceIp: str | None = None,
        UserPassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        Arn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_access(
        self,
        *,
        ServerId: str,
        ExternalId: str,
        HomeDirectory: str | None = None,
        HomeDirectoryType: str | None = None,
        HomeDirectoryMappings: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        PosixProfile: dict[str, Any] | None = None,
        Role: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_agreement(
        self,
        *,
        AgreementId: str,
        ServerId: str,
        Description: str | None = None,
        Status: str | None = None,
        LocalProfileId: str | None = None,
        PartnerProfileId: str | None = None,
        BaseDirectory: str | None = None,
        AccessRole: str | None = None,
        PreserveFilename: str | None = None,
        EnforceMessageSigning: str | None = None,
        CustomDirectories: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_certificate(
        self,
        *,
        CertificateId: str,
        ActiveDate: datetime.datetime | str | None = None,
        InactiveDate: datetime.datetime | str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connector(
        self,
        *,
        ConnectorId: str,
        Url: str | None = None,
        As2Config: dict[str, Any] | None = None,
        AccessRole: str | None = None,
        LoggingRole: str | None = None,
        SftpConfig: dict[str, Any] | None = None,
        SecurityPolicyName: str | None = None,
        EgressConfig: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_host_key(
        self,
        *,
        ServerId: str,
        HostKeyId: str,
        Description: str | None = None,
        StorageType: str | None = None,
        KmsKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_profile(
        self,
        *,
        ProfileId: str,
        CertificateIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_server(
        self,
        *,
        ServerId: str,
        Certificate: str | None = None,
        ProtocolDetails: dict[str, Any] | None = None,
        EndpointDetails: dict[str, Any] | None = None,
        EndpointType: str | None = None,
        HostKey: str | None = None,
        IdentityProviderDetails: dict[str, Any] | None = None,
        LoggingRole: str | None = None,
        PostAuthenticationLoginBanner: str | None = None,
        PreAuthenticationLoginBanner: str | None = None,
        Protocols: list[str] | None = None,
        SecurityPolicyName: str | None = None,
        WorkflowDetails: dict[str, Any] | None = None,
        StructuredLogDestinations: list[str] | None = None,
        S3StorageOptions: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
        IdentityProviderType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        ServerId: str,
        UserName: str,
        HomeDirectory: str | None = None,
        HomeDirectoryType: str | None = None,
        HomeDirectoryMappings: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        PosixProfile: dict[str, Any] | None = None,
        Role: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_web_app(
        self,
        *,
        WebAppId: str,
        IdentityProviderDetails: dict[str, Any] | None = None,
        AccessEndpoint: str | None = None,
        WebAppUnits: dict[str, Any] | None = None,
        EndpointDetails: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_web_app_customization(
        self,
        *,
        WebAppId: str,
        Title: str | None = None,
        LogoFile: bytes | BinaryIO | str | None = None,
        FaviconFile: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
