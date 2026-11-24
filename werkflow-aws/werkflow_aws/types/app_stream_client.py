from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AppStreamClient(ABC):

    @abstractmethod
    def associate_app_block_builder_app_block(
        self,
        *,
        AppBlockArn: str,
        AppBlockBuilderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_application_fleet(
        self,
        *,
        FleetName: str,
        ApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_application_to_entitlement(
        self,
        *,
        StackName: str,
        EntitlementName: str,
        ApplicationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_fleet(
        self,
        *,
        FleetName: str,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_software_to_image_builder(
        self,
        *,
        ImageBuilderName: str,
        SoftwareNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_user_stack(
        self,
        *,
        UserStackAssociations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_user_stack(
        self,
        *,
        UserStackAssociations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_image(
        self,
        *,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_block(
        self,
        *,
        Name: str,
        SourceS3Location: dict[str, Any],
        Description: str | None = None,
        DisplayName: str | None = None,
        SetupScriptDetails: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        PostSetupScriptDetails: dict[str, Any] | None = None,
        PackagingType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_block_builder(
        self,
        *,
        Name: str,
        Platform: str,
        InstanceType: str,
        VpcConfig: dict[str, Any],
        Description: str | None = None,
        DisplayName: str | None = None,
        Tags: dict[str, str] | None = None,
        EnableDefaultInternetAccess: bool | None = None,
        IamRoleArn: str | None = None,
        AccessEndpoints: list[dict[str, Any]] | None = None,
        DisableIMDSV1: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_block_builder_streaming_url(
        self,
        *,
        AppBlockBuilderName: str,
        Validity: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application(
        self,
        *,
        Name: str,
        IconS3Location: dict[str, Any],
        LaunchPath: str,
        Platforms: list[str],
        InstanceFamilies: list[str],
        AppBlockArn: str,
        DisplayName: str | None = None,
        Description: str | None = None,
        WorkingDirectory: str | None = None,
        LaunchParameters: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: list[str],
        ServiceAccountCredentials: dict[str, Any] | None = None,
        CertificateBasedAuthProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_entitlement(
        self,
        *,
        Name: str,
        StackName: str,
        AppVisibility: str,
        Attributes: list[dict[str, Any]],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_export_image_task(
        self,
        *,
        ImageName: str,
        AmiName: str,
        IamRoleArn: str,
        TagSpecifications: dict[str, str] | None = None,
        AmiDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fleet(
        self,
        *,
        Name: str,
        InstanceType: str,
        ImageName: str | None = None,
        ImageArn: str | None = None,
        FleetType: str | None = None,
        ComputeCapacity: dict[str, Any] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        MaxUserDurationInSeconds: int | None = None,
        DisconnectTimeoutInSeconds: int | None = None,
        Description: str | None = None,
        DisplayName: str | None = None,
        EnableDefaultInternetAccess: bool | None = None,
        DomainJoinInfo: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        IdleDisconnectTimeoutInSeconds: int | None = None,
        IamRoleArn: str | None = None,
        StreamView: str | None = None,
        Platform: str | None = None,
        MaxConcurrentSessions: int | None = None,
        UsbDeviceFilterStrings: list[str] | None = None,
        SessionScriptS3Location: dict[str, Any] | None = None,
        MaxSessionsPerInstance: int | None = None,
        RootVolumeConfig: dict[str, Any] | None = None,
        DisableIMDSV1: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image_builder(
        self,
        *,
        Name: str,
        InstanceType: str,
        ImageName: str | None = None,
        ImageArn: str | None = None,
        Description: str | None = None,
        DisplayName: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        IamRoleArn: str | None = None,
        EnableDefaultInternetAccess: bool | None = None,
        DomainJoinInfo: dict[str, Any] | None = None,
        AppstreamAgentVersion: str | None = None,
        Tags: dict[str, str] | None = None,
        AccessEndpoints: list[dict[str, Any]] | None = None,
        RootVolumeConfig: dict[str, Any] | None = None,
        SoftwaresToInstall: list[str] | None = None,
        SoftwaresToUninstall: list[str] | None = None,
        DisableIMDSV1: bool | None = None,
        AgentAccessConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image_builder_streaming_url(
        self,
        *,
        Name: str,
        Validity: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_imported_image(
        self,
        *,
        Name: str,
        SourceAmiId: str | None = None,
        WorkspaceImageId: str | None = None,
        IamRoleArn: str | None = None,
        Description: str | None = None,
        DisplayName: str | None = None,
        Tags: dict[str, str] | None = None,
        RuntimeValidationConfig: dict[str, Any] | None = None,
        AgentSoftwareVersion: str | None = None,
        AppCatalogConfig: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stack(
        self,
        *,
        Name: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        StorageConnectors: list[dict[str, Any]] | None = None,
        RedirectURL: str | None = None,
        FeedbackURL: str | None = None,
        UserSettings: list[dict[str, Any]] | None = None,
        ApplicationSettings: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        AccessEndpoints: list[dict[str, Any]] | None = None,
        EmbedHostDomains: list[str] | None = None,
        StreamingExperienceSettings: dict[str, Any] | None = None,
        ContentRedirection: dict[str, Any] | None = None,
        WebAuthnRedirection: dict[str, Any] | None = None,
        AgentAccessConfig: dict[str, Any] | None = None,
        StorageConnectorAuthentication: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_streaming_url(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str | None = None,
        Validity: int | None = None,
        SessionContext: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_theme_for_stack(
        self,
        *,
        StackName: str,
        TitleText: str,
        ThemeStyling: str,
        OrganizationLogoS3Location: dict[str, Any],
        FaviconS3Location: dict[str, Any],
        FooterLinks: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_updated_image(
        self,
        *,
        existingImageName: str,
        newImageName: str,
        newImageDescription: str | None = None,
        newImageDisplayName: str | None = None,
        newImageTags: dict[str, str] | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_usage_report_subscription(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        UserName: str,
        AuthenticationType: str,
        MessageAction: str | None = None,
        FirstName: str | None = None,
        LastName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_block(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_block_builder(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_directory_config(
        self,
        *,
        DirectoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_entitlement(
        self,
        *,
        Name: str,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleet(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image_builder(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image_permissions(
        self,
        *,
        Name: str,
        SharedAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stack(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_theme_for_stack(
        self,
        *,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_usage_report_subscription(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        UserName: str,
        AuthenticationType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_block_builder_app_block_associations(
        self,
        *,
        AppBlockArn: str | None = None,
        AppBlockBuilderName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_block_builders(
        self,
        *,
        Names: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_blocks(
        self,
        *,
        Arns: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_license_usage(
        self,
        *,
        BillingPeriod: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_fleet_associations(
        self,
        *,
        FleetName: str | None = None,
        ApplicationArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_applications(
        self,
        *,
        Arns: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_directory_configs(
        self,
        *,
        DirectoryNames: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_entitlements(
        self,
        *,
        StackName: str,
        Name: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleets(
        self,
        *,
        Names: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_builders(
        self,
        *,
        Names: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_permissions(
        self,
        *,
        Name: str,
        MaxResults: int | None = None,
        SharedAwsAccountIds: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_images(
        self,
        *,
        Names: list[str] | None = None,
        Arns: list[str] | None = None,
        Type: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_sessions(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
        AuthenticationType: str | None = None,
        InstanceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_software_associations(
        self,
        *,
        AssociatedResource: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stacks(
        self,
        *,
        Names: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_theme_for_stack(
        self,
        *,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_usage_report_subscriptions(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_stack_associations(
        self,
        *,
        StackName: str | None = None,
        UserName: str | None = None,
        AuthenticationType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_users(
        self,
        *,
        AuthenticationType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_user(
        self,
        *,
        UserName: str,
        AuthenticationType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_app_block_builder_app_block(
        self,
        *,
        AppBlockArn: str,
        AppBlockBuilderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_application_fleet(
        self,
        *,
        FleetName: str,
        ApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_application_from_entitlement(
        self,
        *,
        StackName: str,
        EntitlementName: str,
        ApplicationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_fleet(
        self,
        *,
        FleetName: str,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_software_from_image_builder(
        self,
        *,
        ImageBuilderName: str,
        SoftwareNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def drain_session_instance(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_user(
        self,
        *,
        UserName: str,
        AuthenticationType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def expire_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_image_task(
        self,
        *,
        TaskId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_fleets(
        self,
        *,
        StackName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_stacks(
        self,
        *,
        FleetName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entitled_applications(
        self,
        *,
        StackName: str,
        EntitlementName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_export_image_tasks(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_app_block_builder(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_fleet(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_image_builder(
        self,
        *,
        Name: str,
        AppstreamAgentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_software_deployment_to_image_builder(
        self,
        *,
        ImageBuilderName: str,
        RetryFailedDeployments: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_app_block_builder(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_fleet(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_image_builder(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_block_builder(
        self,
        *,
        Name: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        Platform: str | None = None,
        InstanceType: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        EnableDefaultInternetAccess: bool | None = None,
        IamRoleArn: str | None = None,
        AccessEndpoints: list[dict[str, Any]] | None = None,
        AttributesToDelete: list[str] | None = None,
        DisableIMDSV1: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application(
        self,
        *,
        Name: str,
        DisplayName: str | None = None,
        Description: str | None = None,
        IconS3Location: dict[str, Any] | None = None,
        LaunchPath: str | None = None,
        WorkingDirectory: str | None = None,
        LaunchParameters: str | None = None,
        AppBlockArn: str | None = None,
        AttributesToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: list[str] | None = None,
        ServiceAccountCredentials: dict[str, Any] | None = None,
        CertificateBasedAuthProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_entitlement(
        self,
        *,
        Name: str,
        StackName: str,
        Description: str | None = None,
        AppVisibility: str | None = None,
        Attributes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_fleet(
        self,
        *,
        ImageName: str | None = None,
        ImageArn: str | None = None,
        Name: str | None = None,
        InstanceType: str | None = None,
        ComputeCapacity: dict[str, Any] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        MaxUserDurationInSeconds: int | None = None,
        DisconnectTimeoutInSeconds: int | None = None,
        DeleteVpcConfig: bool | None = None,
        Description: str | None = None,
        DisplayName: str | None = None,
        EnableDefaultInternetAccess: bool | None = None,
        DomainJoinInfo: dict[str, Any] | None = None,
        IdleDisconnectTimeoutInSeconds: int | None = None,
        AttributesToDelete: list[str] | None = None,
        IamRoleArn: str | None = None,
        StreamView: str | None = None,
        Platform: str | None = None,
        MaxConcurrentSessions: int | None = None,
        UsbDeviceFilterStrings: list[str] | None = None,
        SessionScriptS3Location: dict[str, Any] | None = None,
        MaxSessionsPerInstance: int | None = None,
        RootVolumeConfig: dict[str, Any] | None = None,
        DisableIMDSV1: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image_builder(
        self,
        *,
        Name: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        AgentAccessConfig: dict[str, Any] | None = None,
        AttributesToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image_permissions(
        self,
        *,
        Name: str,
        SharedAccountId: str,
        ImagePermissions: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stack(
        self,
        *,
        Name: str,
        DisplayName: str | None = None,
        Description: str | None = None,
        StorageConnectors: list[dict[str, Any]] | None = None,
        DeleteStorageConnectors: bool | None = None,
        RedirectURL: str | None = None,
        FeedbackURL: str | None = None,
        AttributesToDelete: list[str] | None = None,
        UserSettings: list[dict[str, Any]] | None = None,
        ApplicationSettings: dict[str, Any] | None = None,
        AccessEndpoints: list[dict[str, Any]] | None = None,
        EmbedHostDomains: list[str] | None = None,
        StreamingExperienceSettings: dict[str, Any] | None = None,
        ContentRedirection: dict[str, Any] | None = None,
        WebAuthnRedirection: dict[str, Any] | None = None,
        AgentAccessConfig: dict[str, Any] | None = None,
        StorageConnectorAuthentication: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_theme_for_stack(
        self,
        *,
        StackName: str,
        FooterLinks: list[dict[str, Any]] | None = None,
        TitleText: str | None = None,
        ThemeStyling: str | None = None,
        OrganizationLogoS3Location: dict[str, Any] | None = None,
        FaviconS3Location: dict[str, Any] | None = None,
        State: str | None = None,
        AttributesToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
