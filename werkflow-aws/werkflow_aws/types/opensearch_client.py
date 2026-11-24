from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class OpenSearchClient(ABC):

    @abstractmethod
    def accept_inbound_connection(
        self,
        *,
        ConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_data_source(
        self,
        *,
        DomainName: str,
        Name: str,
        DataSourceType: dict[str, Any],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_direct_query_data_source(
        self,
        *,
        DataSourceName: str,
        DataSourceType: dict[str, Any],
        Description: str | None = None,
        OpenSearchArns: list[str] | None = None,
        DataSourceAccessPolicy: str | None = None,
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_replication_peer(
        self,
        *,
        DomainName: str,
        PeerDomainArn: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags(
        self,
        *,
        ARN: str,
        TagList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_package(
        self,
        *,
        PackageID: str,
        DomainName: str,
        PrerequisitePackageIDList: list[str] | None = None,
        AssociationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_packages(
        self,
        *,
        PackageList: list[dict[str, Any]],
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_data_source(
        self,
        *,
        id: str,
        dataSourceArn: str,
        workspaceId: str | None = None,
        workspaceConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_vpc_endpoint_access(
        self,
        *,
        DomainName: str,
        Account: str | None = None,
        Service: str | None = None,
        ServiceOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_domain_config_change(
        self,
        *,
        DomainName: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_service_software_update(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def compare_domain_configuration(
        self,
        *,
        SourceDomainArn: str,
        TargetDomainArn: str,
        Categories: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application(
        self,
        *,
        name: str,
        clientToken: str | None = None,
        dataSources: list[dict[str, Any]] | None = None,
        iamIdentityCenterOptions: dict[str, Any] | None = None,
        appConfigs: list[dict[str, Any]] | None = None,
        tagList: list[dict[str, Any]] | None = None,
        kmsKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        DomainName: str,
        EngineVersion: str | None = None,
        ClusterConfig: dict[str, Any] | None = None,
        EBSOptions: dict[str, Any] | None = None,
        AccessPolicies: str | None = None,
        IPAddressType: str | None = None,
        SnapshotOptions: dict[str, Any] | None = None,
        VPCOptions: dict[str, Any] | None = None,
        CognitoOptions: dict[str, Any] | None = None,
        EncryptionAtRestOptions: dict[str, Any] | None = None,
        NodeToNodeEncryptionOptions: dict[str, Any] | None = None,
        AdvancedOptions: dict[str, str] | None = None,
        LogPublishingOptions: dict[str, dict[str, Any]] | None = None,
        DomainEndpointOptions: dict[str, Any] | None = None,
        AdvancedSecurityOptions: dict[str, Any] | None = None,
        IdentityCenterOptions: dict[str, Any] | None = None,
        TagList: list[dict[str, Any]] | None = None,
        AutoTuneOptions: dict[str, Any] | None = None,
        OffPeakWindowOptions: dict[str, Any] | None = None,
        SoftwareUpdateOptions: dict[str, Any] | None = None,
        AIMLOptions: dict[str, Any] | None = None,
        DeploymentStrategyOptions: dict[str, Any] | None = None,
        AutomatedSnapshotPauseOptions: dict[str, Any] | None = None,
        UseCase: str | None = None,
        EngineMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_index(
        self,
        *,
        DomainName: str,
        IndexName: str,
        IndexSchema: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_outbound_connection(
        self,
        *,
        LocalDomainInfo: dict[str, Any],
        RemoteDomainInfo: dict[str, Any],
        ConnectionAlias: str,
        ConnectionMode: str | None = None,
        ConnectionProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_package(
        self,
        *,
        PackageName: str,
        PackageType: str,
        PackageSource: dict[str, Any],
        PackageDescription: str | None = None,
        PackageConfiguration: dict[str, Any] | None = None,
        EngineVersion: str | None = None,
        PackageVendingOptions: dict[str, Any] | None = None,
        PackageEncryptionOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_endpoint(
        self,
        *,
        DomainArn: str,
        VpcOptions: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        DomainName: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_direct_query_data_source(
        self,
        *,
        DataSourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inbound_connection(
        self,
        *,
        ConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index(
        self,
        *,
        DomainName: str,
        IndexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_outbound_connection(
        self,
        *,
        ConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package(
        self,
        *,
        PackageID: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_endpoint(
        self,
        *,
        VpcEndpointId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_capability(
        self,
        *,
        applicationId: str,
        capabilityName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_source_attachment(
        self,
        *,
        id: str,
        dataSourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_auto_tunes(
        self,
        *,
        DomainName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_change_progress(
        self,
        *,
        DomainName: str,
        ChangeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_config(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_health(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_nodes(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_replication(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domains(
        self,
        *,
        DomainNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dry_run_progress(
        self,
        *,
        DomainName: str,
        DryRunId: str | None = None,
        LoadDryRunConfig: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inbound_connections(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_insight_details(
        self,
        *,
        Entity: dict[str, Any],
        InsightId: str,
        ShowHtmlContent: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_type_limits(
        self,
        *,
        InstanceType: str,
        EngineVersion: str,
        DomainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_outbound_connections(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_packages(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instance_offerings(
        self,
        *,
        ReservedInstanceOfferingId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instances(
        self,
        *,
        ReservedInstanceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoints(
        self,
        *,
        VpcEndpointIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_data_source(
        self,
        *,
        id: str,
        dataSourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def dissociate_package(
        self,
        *,
        PackageID: str,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def dissociate_packages(
        self,
        *,
        PackageList: list[str],
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_replication(
        self,
        *,
        DomainName: str,
        PeerDomainArn: str,
        AllowDataLoss: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_application(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capability(
        self,
        *,
        applicationId: str,
        capabilityName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compatible_versions(
        self,
        *,
        DomainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source(
        self,
        *,
        DomainName: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_default_application_setting(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_direct_query_data_source(
        self,
        *,
        DataSourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_maintenance_status(
        self,
        *,
        DomainName: str,
        MaintenanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_index(
        self,
        *,
        DomainName: str,
        IndexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_migration(
        self,
        *,
        migrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package_version_history(
        self,
        *,
        PackageID: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_upgrade_history(
        self,
        *,
        DomainName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_upgrade_status(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def insight_feedback(
        self,
        *,
        Entity: dict[str, Any],
        InsightId: str,
        Thumbs: str,
        FeedbackText: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_applications(
        self,
        *,
        nextToken: str | None = None,
        statuses: list[str] | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_source_attachments(
        self,
        *,
        id: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_direct_query_data_sources(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_maintenances(
        self,
        *,
        DomainName: str,
        Action: str | None = None,
        Status: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_names(
        self,
        *,
        EngineType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains_for_package(
        self,
        *,
        PackageID: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_insights(
        self,
        *,
        Entity: dict[str, Any],
        TimeRange: dict[str, Any] | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_type_details(
        self,
        *,
        EngineVersion: str,
        DomainName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        RetrieveAZs: bool | None = None,
        InstanceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_migrations(
        self,
        *,
        applicationId: str,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_packages_for_domain(
        self,
        *,
        DomainName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scheduled_actions(
        self,
        *,
        DomainName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_versions(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_endpoint_access(
        self,
        *,
        DomainName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_endpoints(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_endpoints_for_domain(
        self,
        *,
        DomainName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_reserved_instance_offering(
        self,
        *,
        ReservedInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_default_application_setting(
        self,
        *,
        applicationArn: str,
        setAsDefault: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_capability(
        self,
        *,
        applicationId: str,
        capabilityName: str,
        capabilityConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_inbound_connection(
        self,
        *,
        ConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_replication_peer(
        self,
        *,
        DomainName: str,
        PeerDomainArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags(
        self,
        *,
        ARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_vpc_endpoint_access(
        self,
        *,
        DomainName: str,
        Account: str | None = None,
        Service: str | None = None,
        ServiceOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rollback_service_software_update(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_domain_maintenance(
        self,
        *,
        DomainName: str,
        Action: str,
        NodeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_migration(
        self,
        *,
        applicationId: str,
        migrationOptions: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_service_software_update(
        self,
        *,
        DomainName: str,
        ScheduleAt: str | None = None,
        DesiredStartTime: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def switchover_replication(
        self,
        *,
        DomainName: str,
        PeerDomainArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application(
        self,
        *,
        id: str,
        dataSources: list[dict[str, Any]] | None = None,
        appConfigs: list[dict[str, Any]] | None = None,
        iamIdentityCenterOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_clone(
        self,
        *,
        DomainName: str,
        TrafficSplitOptions: dict[str, Any] | None = None,
        CutoverOptions: dict[str, Any] | None = None,
        RetentionOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        DomainName: str,
        Name: str,
        DataSourceType: dict[str, Any],
        Description: str | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_direct_query_data_source(
        self,
        *,
        DataSourceName: str,
        DataSourceType: dict[str, Any],
        Description: str | None = None,
        OpenSearchArns: list[str] | None = None,
        DataSourceAccessPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_config(
        self,
        *,
        DomainName: str,
        ClusterConfig: dict[str, Any] | None = None,
        EBSOptions: dict[str, Any] | None = None,
        SnapshotOptions: dict[str, Any] | None = None,
        VPCOptions: dict[str, Any] | None = None,
        CognitoOptions: dict[str, Any] | None = None,
        AdvancedOptions: dict[str, str] | None = None,
        AccessPolicies: str | None = None,
        IPAddressType: str | None = None,
        LogPublishingOptions: dict[str, dict[str, Any]] | None = None,
        EncryptionAtRestOptions: dict[str, Any] | None = None,
        DomainEndpointOptions: dict[str, Any] | None = None,
        NodeToNodeEncryptionOptions: dict[str, Any] | None = None,
        AdvancedSecurityOptions: dict[str, Any] | None = None,
        IdentityCenterOptions: dict[str, Any] | None = None,
        AutoTuneOptions: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        DryRunMode: str | None = None,
        OffPeakWindowOptions: dict[str, Any] | None = None,
        SoftwareUpdateOptions: dict[str, Any] | None = None,
        AIMLOptions: dict[str, Any] | None = None,
        DeploymentStrategyOptions: dict[str, Any] | None = None,
        AutomatedSnapshotPauseOptions: dict[str, Any] | None = None,
        UseCase: str | None = None,
        EngineMode: str | None = None,
        AcceptedWarnings: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_index(
        self,
        *,
        DomainName: str,
        IndexName: str,
        IndexSchema: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package(
        self,
        *,
        PackageID: str,
        PackageSource: dict[str, Any],
        PackageDescription: str | None = None,
        CommitMessage: str | None = None,
        PackageConfiguration: dict[str, Any] | None = None,
        PackageEncryptionOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package_scope(
        self,
        *,
        PackageID: str,
        Operation: str,
        PackageUserList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scheduled_action(
        self,
        *,
        DomainName: str,
        ActionID: str,
        ActionType: str,
        ScheduleAt: str,
        DesiredStartTime: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_endpoint(
        self,
        *,
        VpcEndpointId: str,
        VpcOptions: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upgrade_domain(
        self,
        *,
        DomainName: str,
        TargetVersion: str,
        PerformCheckOnly: bool | None = None,
        AdvancedOptions: dict[str, str] | None = None,
        DeploymentStrategyOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
