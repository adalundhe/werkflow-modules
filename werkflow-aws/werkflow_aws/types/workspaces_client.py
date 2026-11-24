from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class WorkSpacesClient(ABC):

    @abstractmethod
    def accept_account_link_invitation(
        self,
        *,
        LinkId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_connection_alias(
        self,
        *,
        AliasId: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_ip_groups(
        self,
        *,
        DirectoryId: str,
        GroupIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_workspace_application(
        self,
        *,
        WorkspaceId: str,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_ip_rules(
        self,
        *,
        GroupId: str,
        UserRules: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_workspace_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account_link_invitation(
        self,
        *,
        TargetAccountId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connect_client_add_in(
        self,
        *,
        ResourceId: str,
        Name: str,
        URL: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection_alias(
        self,
        *,
        ConnectionString: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ip_group(
        self,
        *,
        GroupName: str,
        GroupDesc: str | None = None,
        UserRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_standby_workspaces(
        self,
        *,
        PrimaryRegion: str,
        StandbyWorkspaces: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tags(
        self,
        *,
        ResourceId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_updated_workspace_image(
        self,
        *,
        Name: str,
        Description: str,
        SourceImageId: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_bundle(
        self,
        *,
        BundleName: str,
        BundleDescription: str,
        ImageId: str,
        ComputeType: dict[str, Any],
        UserStorage: dict[str, Any],
        RootStorage: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_image(
        self,
        *,
        Name: str,
        Description: str,
        WorkspaceId: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspaces(
        self,
        *,
        Workspaces: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspaces_pool(
        self,
        *,
        PoolName: str,
        Description: str,
        BundleId: str,
        DirectoryId: str,
        Capacity: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
        ApplicationSettings: dict[str, Any] | None = None,
        TimeoutSettings: dict[str, Any] | None = None,
        RunningMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_link_invitation(
        self,
        *,
        LinkId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_client_branding(
        self,
        *,
        ResourceId: str,
        Platforms: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connect_client_add_in(
        self,
        *,
        AddInId: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection_alias(
        self,
        *,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ip_group(
        self,
        *,
        GroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        ResourceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_bundle(
        self,
        *,
        BundleId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_image(
        self,
        *,
        ImageId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deploy_workspace_applications(
        self,
        *,
        WorkspaceId: str,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_workspace_directory(
        self,
        *,
        DirectoryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_modifications(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_associations(
        self,
        *,
        ApplicationId: str,
        AssociatedResourceTypes: list[str],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_applications(
        self,
        *,
        ApplicationIds: list[str] | None = None,
        ComputeTypeNames: list[str] | None = None,
        LicenseType: str | None = None,
        OperatingSystemNames: list[str] | None = None,
        Owner: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bundle_associations(
        self,
        *,
        BundleId: str,
        AssociatedResourceTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_branding(
        self,
        *,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_properties(
        self,
        *,
        ResourceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connect_client_add_ins(
        self,
        *,
        ResourceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection_alias_permissions(
        self,
        *,
        AliasId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection_aliases(
        self,
        *,
        AliasIds: list[str] | None = None,
        ResourceId: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_workspace_image_import(
        self,
        *,
        ImageId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_associations(
        self,
        *,
        ImageId: str,
        AssociatedResourceTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ip_groups(
        self,
        *,
        GroupIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_associations(
        self,
        *,
        WorkspaceId: str,
        AssociatedResourceTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_bundles(
        self,
        *,
        BundleIds: list[str] | None = None,
        Owner: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_directories(
        self,
        *,
        DirectoryIds: list[str] | None = None,
        WorkspaceDirectoryNames: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_image_permissions(
        self,
        *,
        ImageId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_images(
        self,
        *,
        ImageIds: list[str] | None = None,
        ImageType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_snapshots(
        self,
        *,
        WorkspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspaces(
        self,
        *,
        WorkspaceIds: list[str] | None = None,
        DirectoryId: str | None = None,
        UserName: str | None = None,
        BundleId: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
        WorkspaceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspaces_connection_status(
        self,
        *,
        WorkspaceIds: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspaces_pool_sessions(
        self,
        *,
        PoolId: str,
        UserId: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspaces_pools(
        self,
        *,
        PoolIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_connection_alias(
        self,
        *,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_ip_groups(
        self,
        *,
        DirectoryId: str,
        GroupIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_workspace_application(
        self,
        *,
        WorkspaceId: str,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_link(
        self,
        *,
        LinkId: str | None = None,
        LinkedAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_client_branding(
        self,
        *,
        ResourceId: str,
        DeviceTypeWindows: dict[str, Any] | None = None,
        DeviceTypeOsx: dict[str, Any] | None = None,
        DeviceTypeAndroid: dict[str, Any] | None = None,
        DeviceTypeIos: dict[str, Any] | None = None,
        DeviceTypeLinux: dict[str, Any] | None = None,
        DeviceTypeWeb: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_custom_workspace_image(
        self,
        *,
        ImageName: str,
        ImageDescription: str,
        ComputeType: str,
        Protocol: str,
        ImageSource: dict[str, Any],
        InfrastructureConfigurationArn: str,
        Platform: str,
        OsVersion: str,
        Tags: list[dict[str, Any]] | None = None,
        ImageValidationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_workspace_image(
        self,
        *,
        Ec2ImageId: str,
        IngestionProcess: str,
        ImageName: str,
        ImageDescription: str,
        Tags: list[dict[str, Any]] | None = None,
        Applications: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_account_links(
        self,
        *,
        LinkStatusFilter: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_available_management_cidr_ranges(
        self,
        *,
        ManagementCidrRangeConstraint: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def migrate_workspace(
        self,
        *,
        SourceWorkspaceId: str,
        BundleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_account(
        self,
        *,
        DedicatedTenancySupport: str | None = None,
        DedicatedTenancyManagementCidrRange: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_certificate_based_auth_properties(
        self,
        *,
        ResourceId: str,
        CertificateBasedAuthProperties: dict[str, Any] | None = None,
        PropertiesToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_client_properties(
        self,
        *,
        ResourceId: str,
        ClientProperties: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_endpoint_encryption_mode(
        self,
        *,
        DirectoryId: str,
        EndpointEncryptionMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_saml_properties(
        self,
        *,
        ResourceId: str,
        SamlProperties: dict[str, Any] | None = None,
        PropertiesToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_selfservice_permissions(
        self,
        *,
        ResourceId: str,
        SelfservicePermissions: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_streaming_properties(
        self,
        *,
        ResourceId: str,
        StreamingProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_workspace_access_properties(
        self,
        *,
        ResourceId: str,
        WorkspaceAccessProperties: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_workspace_creation_properties(
        self,
        *,
        ResourceId: str,
        WorkspaceCreationProperties: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_workspace_properties(
        self,
        *,
        WorkspaceId: str,
        WorkspaceProperties: dict[str, Any] | None = None,
        DataReplication: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_workspace_state(
        self,
        *,
        WorkspaceId: str,
        WorkspaceState: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_workspaces(
        self,
        *,
        RebootWorkspaceRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rebuild_workspaces(
        self,
        *,
        RebuildWorkspaceRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_workspace_directory(
        self,
        *,
        DirectoryId: str | None = None,
        SubnetIds: list[str] | None = None,
        EnableSelfService: bool | None = None,
        Tenancy: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WorkspaceDirectoryName: str | None = None,
        WorkspaceDirectoryDescription: str | None = None,
        UserIdentityType: str | None = None,
        WorkspaceOsUserMode: str | None = None,
        IdcInstanceArn: str | None = None,
        MicrosoftEntraConfig: dict[str, Any] | None = None,
        WorkspaceType: str | None = None,
        ActiveDirectoryConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_account_link_invitation(
        self,
        *,
        LinkId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_workspace(
        self,
        *,
        WorkspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_ip_rules(
        self,
        *,
        GroupId: str,
        UserRules: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_workspaces(
        self,
        *,
        StartWorkspaceRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_workspaces_pool(
        self,
        *,
        PoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_workspaces(
        self,
        *,
        StopWorkspaceRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_workspaces_pool(
        self,
        *,
        PoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_workspaces(
        self,
        *,
        TerminateWorkspaceRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_workspaces_pool(
        self,
        *,
        PoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_workspaces_pool_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connect_client_add_in(
        self,
        *,
        AddInId: str,
        ResourceId: str,
        Name: str | None = None,
        URL: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection_alias_permission(
        self,
        *,
        AliasId: str,
        ConnectionAliasPermission: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rules_of_ip_group(
        self,
        *,
        GroupId: str,
        UserRules: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_bundle(
        self,
        *,
        BundleId: str | None = None,
        ImageId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_image_permission(
        self,
        *,
        ImageId: str,
        AllowCopyImage: bool,
        SharedAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspaces_pool(
        self,
        *,
        PoolId: str,
        Description: str | None = None,
        BundleId: str | None = None,
        DirectoryId: str | None = None,
        Capacity: dict[str, Any] | None = None,
        ApplicationSettings: dict[str, Any] | None = None,
        TimeoutSettings: dict[str, Any] | None = None,
        RunningMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
