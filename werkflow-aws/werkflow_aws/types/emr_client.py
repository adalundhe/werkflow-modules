from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class EMRClient(ABC):

    @abstractmethod
    def add_instance_fleet(
        self,
        *,
        ClusterId: str,
        InstanceFleet: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_instance_groups(
        self,
        *,
        InstanceGroups: list[dict[str, Any]],
        JobFlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_job_flow_steps(
        self,
        *,
        JobFlowId: str,
        Steps: list[dict[str, Any]],
        ExecutionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags(
        self,
        *,
        ResourceId: str,
        Tags: list[dict[str, Any]],
        ClusterId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_steps(
        self,
        *,
        ClusterId: str,
        StepIds: list[str],
        StepCancellationOption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_persistent_app_ui(
        self,
        *,
        TargetResourceArn: str,
        EMRContainersConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        XReferer: str | None = None,
        ProfilerType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_configuration(
        self,
        *,
        Name: str,
        SecurityConfiguration: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_studio(
        self,
        *,
        Name: str,
        AuthMode: str,
        VpcId: str,
        SubnetIds: list[str],
        ServiceRole: str,
        WorkspaceSecurityGroupId: str,
        EngineSecurityGroupId: str,
        DefaultS3Location: str,
        Description: str | None = None,
        UserRole: str | None = None,
        IdpAuthUrl: str | None = None,
        IdpRelayStateParameterName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TrustedIdentityPropagationEnabled: bool | None = None,
        IdcUserAssignment: str | None = None,
        IdcInstanceArn: str | None = None,
        EncryptionKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: str,
        SessionPolicyArn: str,
        IdentityId: str | None = None,
        IdentityName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_configuration(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_studio(
        self,
        *,
        StudioId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: str,
        IdentityId: str | None = None,
        IdentityName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_flows(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        JobFlowIds: list[str] | None = None,
        JobFlowStates: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notebook_execution(
        self,
        *,
        NotebookExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_persistent_app_ui(
        self,
        *,
        PersistentAppUIId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_release_label(
        self,
        *,
        ReleaseLabel: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_configuration(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_step(
        self,
        *,
        ClusterId: str,
        StepId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_studio(
        self,
        *,
        StudioId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_auto_termination_policy(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_block_public_access_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cluster_session_credentials(
        self,
        *,
        ClusterId: str,
        ExecutionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_scaling_policy(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_on_cluster_app_ui_presigned_url(
        self,
        *,
        ClusterId: str,
        OnClusterAppUIType: str | None = None,
        ApplicationId: str | None = None,
        DryRun: bool | None = None,
        ExecutionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_persistent_app_ui_presigned_url(
        self,
        *,
        PersistentAppUIId: str,
        PersistentAppUIType: str | None = None,
        ApplicationId: str | None = None,
        AuthProxyCall: bool | None = None,
        ExecutionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session(
        self,
        *,
        ClusterId: str,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_endpoint(
        self,
        *,
        ClusterId: str,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: str,
        IdentityId: str | None = None,
        IdentityName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bootstrap_actions(
        self,
        *,
        ClusterId: str,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_clusters(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        ClusterStates: list[str] | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_fleets(
        self,
        *,
        ClusterId: str,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_groups(
        self,
        *,
        ClusterId: str,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instances(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str | None = None,
        InstanceGroupTypes: list[str] | None = None,
        InstanceFleetId: str | None = None,
        InstanceFleetType: str | None = None,
        InstanceStates: list[str] | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_executions(
        self,
        *,
        EditorId: str | None = None,
        Status: str | None = None,
        From: datetime.datetime | str | None = None,
        To: datetime.datetime | str | None = None,
        Marker: str | None = None,
        ExecutionEngineId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_release_labels(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_configurations(
        self,
        *,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sessions(
        self,
        *,
        ClusterId: str,
        SessionStates: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_steps(
        self,
        *,
        ClusterId: str,
        StepStates: list[str] | None = None,
        StepIds: list[str] | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_studio_session_mappings(
        self,
        *,
        StudioId: str | None = None,
        IdentityType: str | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_studios(
        self,
        *,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_supported_instance_types(
        self,
        *,
        ReleaseLabel: str,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster(
        self,
        *,
        ClusterId: str,
        StepConcurrencyLevel: int | None = None,
        ExtendedSupport: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_fleet(
        self,
        *,
        ClusterId: str,
        InstanceFleet: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_groups(
        self,
        *,
        ClusterId: str | None = None,
        InstanceGroups: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_auto_scaling_policy(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str,
        AutoScalingPolicy: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_auto_termination_policy(
        self,
        *,
        ClusterId: str,
        AutoTerminationPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_block_public_access_configuration(
        self,
        *,
        BlockPublicAccessConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_managed_scaling_policy(
        self,
        *,
        ClusterId: str,
        ManagedScalingPolicy: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_auto_scaling_policy(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_auto_termination_policy(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_managed_scaling_policy(
        self,
        *,
        ClusterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags(
        self,
        *,
        ResourceId: str,
        TagKeys: list[str],
        ClusterId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_job_flow(
        self,
        *,
        Name: str,
        Instances: dict[str, Any],
        LogUri: str | None = None,
        LogEncryptionKmsKeyId: str | None = None,
        AdditionalInfo: str | None = None,
        AmiVersion: str | None = None,
        ReleaseLabel: str | None = None,
        Steps: list[dict[str, Any]] | None = None,
        StepExecutionRoleArn: str | None = None,
        BootstrapActions: list[dict[str, Any]] | None = None,
        SupportedProducts: list[str] | None = None,
        NewSupportedProducts: list[dict[str, Any]] | None = None,
        Applications: list[dict[str, Any]] | None = None,
        Configurations: list[dict[str, Any]] | None = None,
        VisibleToAllUsers: bool | None = None,
        JobFlowRole: str | None = None,
        ServiceRole: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SecurityConfiguration: str | None = None,
        AutoScalingRole: str | None = None,
        ScaleDownBehavior: str | None = None,
        CustomAmiId: str | None = None,
        EbsRootVolumeSize: int | None = None,
        RepoUpgradeOnBoot: str | None = None,
        KerberosAttributes: dict[str, Any] | None = None,
        StepConcurrencyLevel: int | None = None,
        ManagedScalingPolicy: dict[str, Any] | None = None,
        PlacementGroupConfigs: list[dict[str, Any]] | None = None,
        AutoTerminationPolicy: dict[str, Any] | None = None,
        OSReleaseLabel: str | None = None,
        EbsRootVolumeIops: int | None = None,
        EbsRootVolumeThroughput: int | None = None,
        ExtendedSupport: bool | None = None,
        MonitoringConfiguration: dict[str, Any] | None = None,
        SessionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_keep_job_flow_alive_when_no_steps(
        self,
        *,
        JobFlowIds: list[str],
        KeepJobFlowAliveWhenNoSteps: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_termination_protection(
        self,
        *,
        JobFlowIds: list[str],
        TerminationProtected: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_unhealthy_node_replacement(
        self,
        *,
        JobFlowIds: list[str],
        UnhealthyNodeReplacement: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_visible_to_all_users(
        self,
        *,
        JobFlowIds: list[str],
        VisibleToAllUsers: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_execution(
        self,
        *,
        ExecutionEngine: dict[str, Any],
        ServiceRole: str,
        EditorId: str | None = None,
        RelativePath: str | None = None,
        NotebookExecutionName: str | None = None,
        NotebookParams: str | None = None,
        NotebookInstanceSecurityGroupId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NotebookS3Location: dict[str, Any] | None = None,
        OutputNotebookS3Location: dict[str, Any] | None = None,
        OutputNotebookFormat: str | None = None,
        EnvironmentVariables: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_session(
        self,
        *,
        ClusterId: str,
        Name: str | None = None,
        ExecutionRoleArn: str | None = None,
        EngineConfigurations: list[dict[str, Any]] | None = None,
        MonitoringConfiguration: dict[str, Any] | None = None,
        SessionIdleTimeoutInMinutes: int | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_notebook_execution(
        self,
        *,
        NotebookExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_job_flows(
        self,
        *,
        JobFlowIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_session(
        self,
        *,
        ClusterId: str,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_studio(
        self,
        *,
        StudioId: str,
        Name: str | None = None,
        Description: str | None = None,
        SubnetIds: list[str] | None = None,
        DefaultS3Location: str | None = None,
        EncryptionKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: str,
        SessionPolicyArn: str,
        IdentityId: str | None = None,
        IdentityName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
