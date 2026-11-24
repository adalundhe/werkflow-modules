from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class DirectoryServiceClient(ABC):

    @abstractmethod
    def accept_shared_directory(
        self,
        *,
        SharedDirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_ip_routes(
        self,
        *,
        DirectoryId: str,
        IpRoutes: list[dict[str, Any]],
        UpdateSecurityGroupForDirectoryControllers: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_region(
        self,
        *,
        DirectoryId: str,
        RegionName: str,
        VPCSettings: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags_to_resource(
        self,
        *,
        ResourceId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_schema_extension(
        self,
        *,
        DirectoryId: str,
        SchemaExtensionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def connect_directory(
        self,
        *,
        Name: str,
        Password: str,
        Size: str,
        ConnectSettings: dict[str, Any],
        ShortName: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_alias(
        self,
        *,
        DirectoryId: str,
        Alias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_computer(
        self,
        *,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str | None = None,
        ComputerAttributes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_conditional_forwarder(
        self,
        *,
        DirectoryId: str,
        RemoteDomainName: str,
        DnsIpAddrs: list[str] | None = None,
        DnsIpv6Addrs: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_directory(
        self,
        *,
        Name: str,
        Password: str,
        Size: str,
        ShortName: str | None = None,
        Description: str | None = None,
        VpcSettings: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hybrid_ad(
        self,
        *,
        SecretArn: str,
        AssessmentId: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_log_subscription(
        self,
        *,
        DirectoryId: str,
        LogGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_microsoft_ad(
        self,
        *,
        Name: str,
        Password: str,
        VpcSettings: dict[str, Any],
        ShortName: str | None = None,
        Description: str | None = None,
        Edition: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        DirectoryId: str,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trust(
        self,
        *,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: str,
        TrustType: str | None = None,
        ConditionalForwarderIpAddrs: list[str] | None = None,
        ConditionalForwarderIpv6Addrs: list[str] | None = None,
        SelectiveAuth: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ad_assessment(
        self,
        *,
        AssessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_conditional_forwarder(
        self,
        *,
        DirectoryId: str,
        RemoteDomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_directory(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_log_subscription(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot(
        self,
        *,
        SnapshotId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trust(
        self,
        *,
        TrustId: str,
        DeleteAssociatedConditionalForwarder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_certificate(
        self,
        *,
        DirectoryId: str,
        CertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_event_topic(
        self,
        *,
        DirectoryId: str,
        TopicName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ad_assessment(
        self,
        *,
        AssessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ca_enrollment_policy(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate(
        self,
        *,
        DirectoryId: str,
        CertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_authentication_settings(
        self,
        *,
        DirectoryId: str,
        Type: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conditional_forwarders(
        self,
        *,
        DirectoryId: str,
        RemoteDomainNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_directories(
        self,
        *,
        DirectoryIds: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_directory_data_access(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_controllers(
        self,
        *,
        DirectoryId: str,
        DomainControllerIds: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_topics(
        self,
        *,
        DirectoryId: str | None = None,
        TopicNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hybrid_ad_update(
        self,
        *,
        DirectoryId: str,
        UpdateType: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ldaps_settings(
        self,
        *,
        DirectoryId: str,
        Type: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_regions(
        self,
        *,
        DirectoryId: str,
        RegionName: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_settings(
        self,
        *,
        DirectoryId: str,
        Status: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_shared_directories(
        self,
        *,
        OwnerDirectoryId: str,
        SharedDirectoryIds: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshots(
        self,
        *,
        DirectoryId: str | None = None,
        SnapshotIds: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trusts(
        self,
        *,
        DirectoryId: str | None = None,
        TrustIds: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_update_directory(
        self,
        *,
        DirectoryId: str,
        UpdateType: str,
        RegionName: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_ca_enrollment_policy(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_client_authentication(
        self,
        *,
        DirectoryId: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_directory_data_access(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_ldaps(
        self,
        *,
        DirectoryId: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_radius(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_sso(
        self,
        *,
        DirectoryId: str,
        UserName: str | None = None,
        Password: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ca_enrollment_policy(
        self,
        *,
        DirectoryId: str,
        PcaConnectorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_client_authentication(
        self,
        *,
        DirectoryId: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_directory_data_access(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ldaps(
        self,
        *,
        DirectoryId: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_radius(
        self,
        *,
        DirectoryId: str,
        RadiusSettings: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_sso(
        self,
        *,
        DirectoryId: str,
        UserName: str | None = None,
        Password: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_directory_limits(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_snapshot_limits(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ad_assessments(
        self,
        *,
        DirectoryId: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificates(
        self,
        *,
        DirectoryId: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ip_routes(
        self,
        *,
        DirectoryId: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_log_subscriptions(
        self,
        *,
        DirectoryId: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schema_extensions(
        self,
        *,
        DirectoryId: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceId: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_certificate(
        self,
        *,
        DirectoryId: str,
        CertificateData: str,
        Type: str | None = None,
        ClientCertAuthSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_event_topic(
        self,
        *,
        DirectoryId: str,
        TopicName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_shared_directory(
        self,
        *,
        SharedDirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_ip_routes(
        self,
        *,
        DirectoryId: str,
        CidrIps: list[str] | None = None,
        CidrIpv6s: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_region(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_resource(
        self,
        *,
        ResourceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_user_password(
        self,
        *,
        DirectoryId: str,
        UserName: str,
        NewPassword: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_from_snapshot(
        self,
        *,
        SnapshotId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def share_directory(
        self,
        *,
        DirectoryId: str,
        ShareTarget: dict[str, Any],
        ShareMethod: str,
        ShareNotes: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_ad_assessment(
        self,
        *,
        AssessmentConfiguration: dict[str, Any] | None = None,
        DirectoryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_schema_extension(
        self,
        *,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unshare_directory(
        self,
        *,
        DirectoryId: str,
        UnshareTarget: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_conditional_forwarder(
        self,
        *,
        DirectoryId: str,
        RemoteDomainName: str,
        DnsIpAddrs: list[str] | None = None,
        DnsIpv6Addrs: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_directory_setup(
        self,
        *,
        DirectoryId: str,
        UpdateType: str,
        OSUpdateSettings: dict[str, Any] | None = None,
        DirectorySizeUpdateSettings: dict[str, Any] | None = None,
        NetworkUpdateSettings: dict[str, Any] | None = None,
        CreateSnapshotBeforeUpdate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hybrid_ad(
        self,
        *,
        DirectoryId: str,
        HybridAdministratorAccountUpdate: dict[str, Any] | None = None,
        SelfManagedInstancesSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_number_of_domain_controllers(
        self,
        *,
        DirectoryId: str,
        DesiredNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_radius(
        self,
        *,
        DirectoryId: str,
        RadiusSettings: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_settings(
        self,
        *,
        DirectoryId: str,
        Settings: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trust(
        self,
        *,
        TrustId: str,
        SelectiveAuth: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_trust(
        self,
        *,
        TrustId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
