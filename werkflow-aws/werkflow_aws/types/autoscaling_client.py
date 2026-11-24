from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class AutoScalingClient(ABC):

    @abstractmethod
    def attach_instances(
        self,
        *,
        AutoScalingGroupName: str,
        InstanceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_load_balancer_target_groups(
        self,
        *,
        AutoScalingGroupName: str,
        TargetGroupARNs: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_load_balancers(
        self,
        *,
        AutoScalingGroupName: str,
        LoadBalancerNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_traffic_sources(
        self,
        *,
        AutoScalingGroupName: str,
        TrafficSources: list[dict[str, Any]],
        SkipZonalShiftValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_scheduled_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledActionNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_scheduled_update_group_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledUpdateGroupActions: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_instance_refresh(
        self,
        *,
        AutoScalingGroupName: str,
        WaitForTransitioningInstances: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_lifecycle_action(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionResult: str,
        LifecycleActionToken: str | None = None,
        InstanceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_auto_scaling_group(
        self,
        *,
        AutoScalingGroupName: str,
        MinSize: int,
        MaxSize: int,
        LaunchConfigurationName: str | None = None,
        LaunchTemplate: dict[str, Any] | None = None,
        MixedInstancesPolicy: dict[str, Any] | None = None,
        InstanceId: str | None = None,
        DesiredCapacity: int | None = None,
        DefaultCooldown: int | None = None,
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        LoadBalancerNames: list[str] | None = None,
        TargetGroupARNs: list[str] | None = None,
        HealthCheckType: str | None = None,
        HealthCheckGracePeriod: int | None = None,
        PlacementGroup: str | None = None,
        VPCZoneIdentifier: str | None = None,
        TerminationPolicies: list[str] | None = None,
        NewInstancesProtectedFromScaleIn: bool | None = None,
        CapacityRebalance: bool | None = None,
        LifecycleHookSpecificationList: list[dict[str, Any]] | None = None,
        DeletionProtection: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ServiceLinkedRoleARN: str | None = None,
        MaxInstanceLifetime: int | None = None,
        Context: str | None = None,
        DesiredCapacityType: str | None = None,
        DefaultInstanceWarmup: int | None = None,
        TrafficSources: list[dict[str, Any]] | None = None,
        InstanceMaintenancePolicy: dict[str, Any] | None = None,
        AvailabilityZoneDistribution: dict[str, Any] | None = None,
        AvailabilityZoneImpairmentPolicy: dict[str, Any] | None = None,
        SkipZonalShiftValidation: bool | None = None,
        CapacityReservationSpecification: dict[str, Any] | None = None,
        InstanceLifecyclePolicy: dict[str, Any] | None = None,
        Operator: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_launch_configuration(
        self,
        *,
        LaunchConfigurationName: str,
        ImageId: str | None = None,
        KeyName: str | None = None,
        SecurityGroups: list[str] | None = None,
        ClassicLinkVPCId: str | None = None,
        ClassicLinkVPCSecurityGroups: list[str] | None = None,
        UserData: str | None = None,
        InstanceId: str | None = None,
        InstanceType: str | None = None,
        KernelId: str | None = None,
        RamdiskId: str | None = None,
        BlockDeviceMappings: list[dict[str, Any]] | None = None,
        InstanceMonitoring: dict[str, Any] | None = None,
        SpotPrice: str | None = None,
        IamInstanceProfile: str | None = None,
        EbsOptimized: bool | None = None,
        AssociatePublicIpAddress: bool | None = None,
        PlacementTenancy: str | None = None,
        MetadataOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_or_update_tags(
        self,
        *,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_auto_scaling_group(
        self,
        *,
        AutoScalingGroupName: str,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_launch_configuration(
        self,
        *,
        LaunchConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lifecycle_hook(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notification_configuration(
        self,
        *,
        AutoScalingGroupName: str,
        TopicARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        PolicyName: str,
        AutoScalingGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduled_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_warm_pool(
        self,
        *,
        AutoScalingGroupName: str,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_limits(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_settings(
        self,
        *,
        Name: str | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_adjustment_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_scaling_groups(
        self,
        *,
        AutoScalingGroupNames: list[str] | None = None,
        IncludeInstances: bool | None = None,
        IncludeManagedResources: bool | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_scaling_instances(
        self,
        *,
        InstanceIds: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_scaling_notification_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_refreshes(
        self,
        *,
        AutoScalingGroupName: str,
        InstanceRefreshIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_launch_configurations(
        self,
        *,
        LaunchConfigurationNames: list[str] | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lifecycle_hook_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lifecycle_hooks(
        self,
        *,
        AutoScalingGroupName: str,
        LifecycleHookNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_load_balancer_target_groups(
        self,
        *,
        AutoScalingGroupName: str,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_load_balancers(
        self,
        *,
        AutoScalingGroupName: str,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metric_collection_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notification_configurations(
        self,
        *,
        AutoScalingGroupNames: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_policies(
        self,
        *,
        AutoScalingGroupName: str | None = None,
        PolicyNames: list[str] | None = None,
        PolicyTypes: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scaling_activities(
        self,
        *,
        ActivityIds: list[str] | None = None,
        AutoScalingGroupName: str | None = None,
        IncludeDeletedGroups: bool | None = None,
        IncludeManagedResources: bool | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scaling_process_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_actions(
        self,
        *,
        AutoScalingGroupName: str | None = None,
        ScheduledActionNames: list[str] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        IncludeManagedResources: bool | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        IncludeManagedResources: bool | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_termination_policy_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_sources(
        self,
        *,
        AutoScalingGroupName: str,
        TrafficSourceType: str | None = None,
        NextToken: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_warm_pool(
        self,
        *,
        AutoScalingGroupName: str,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_instances(
        self,
        *,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_load_balancer_target_groups(
        self,
        *,
        AutoScalingGroupName: str,
        TargetGroupARNs: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_load_balancers(
        self,
        *,
        AutoScalingGroupName: str,
        LoadBalancerNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_traffic_sources(
        self,
        *,
        AutoScalingGroupName: str,
        TrafficSources: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_metrics_collection(
        self,
        *,
        AutoScalingGroupName: str,
        Metrics: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_metrics_collection(
        self,
        *,
        AutoScalingGroupName: str,
        Granularity: str,
        Metrics: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enter_standby(
        self,
        *,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_policy(
        self,
        *,
        PolicyName: str,
        AutoScalingGroupName: str | None = None,
        HonorCooldown: bool | None = None,
        MetricValue: float | int | None = None,
        BreachThreshold: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def exit_standby(
        self,
        *,
        AutoScalingGroupName: str,
        InstanceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_predictive_scaling_forecast(
        self,
        *,
        AutoScalingGroupName: str,
        PolicyName: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def launch_instances(
        self,
        *,
        AutoScalingGroupName: str,
        RequestedCapacity: int,
        ClientToken: str,
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        SubnetIds: list[str] | None = None,
        RetryStrategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_setting(
        self,
        *,
        Name: str,
        Value: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_lifecycle_hook(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleTransition: str | None = None,
        RoleARN: str | None = None,
        NotificationTargetARN: str | None = None,
        NotificationMetadata: str | None = None,
        HeartbeatTimeout: int | None = None,
        DefaultResult: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_notification_configuration(
        self,
        *,
        AutoScalingGroupName: str,
        TopicARN: str,
        NotificationTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_scaling_policy(
        self,
        *,
        AutoScalingGroupName: str,
        PolicyName: str,
        PolicyType: str | None = None,
        AdjustmentType: str | None = None,
        MinAdjustmentStep: int | None = None,
        MinAdjustmentMagnitude: int | None = None,
        ScalingAdjustment: int | None = None,
        Cooldown: int | None = None,
        MetricAggregationType: str | None = None,
        StepAdjustments: list[dict[str, Any]] | None = None,
        EstimatedInstanceWarmup: int | None = None,
        TargetTrackingConfiguration: dict[str, Any] | None = None,
        Enabled: bool | None = None,
        PredictiveScalingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_scheduled_update_group_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
        Time: datetime.datetime | str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Recurrence: str | None = None,
        MinSize: int | None = None,
        MaxSize: int | None = None,
        DesiredCapacity: int | None = None,
        TimeZone: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_warm_pool(
        self,
        *,
        AutoScalingGroupName: str,
        MaxGroupPreparedCapacity: int | None = None,
        MinSize: int | None = None,
        PoolState: str | None = None,
        InstanceReusePolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def record_lifecycle_action_heartbeat(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionToken: str | None = None,
        InstanceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_processes(
        self,
        *,
        AutoScalingGroupName: str,
        ScalingProcesses: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rollback_instance_refresh(
        self,
        *,
        AutoScalingGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_desired_capacity(
        self,
        *,
        AutoScalingGroupName: str,
        DesiredCapacity: int,
        HonorCooldown: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_instance_health(
        self,
        *,
        InstanceId: str,
        HealthStatus: str,
        ShouldRespectGracePeriod: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_instance_protection(
        self,
        *,
        InstanceIds: list[str],
        AutoScalingGroupName: str,
        ProtectedFromScaleIn: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_instance_refresh(
        self,
        *,
        AutoScalingGroupName: str,
        Strategy: str | None = None,
        DesiredConfiguration: dict[str, Any] | None = None,
        Preferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def suspend_processes(
        self,
        *,
        AutoScalingGroupName: str,
        ScalingProcesses: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_instance_in_auto_scaling_group(
        self,
        *,
        ShouldDecrementDesiredCapacity: bool,
        InstanceId: str | None = None,
        InstanceIds: list[str] | None = None,
        AutoScalingGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_auto_scaling_group(
        self,
        *,
        AutoScalingGroupName: str,
        LaunchConfigurationName: str | None = None,
        LaunchTemplate: dict[str, Any] | None = None,
        MixedInstancesPolicy: dict[str, Any] | None = None,
        MinSize: int | None = None,
        MaxSize: int | None = None,
        DesiredCapacity: int | None = None,
        DefaultCooldown: int | None = None,
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        HealthCheckType: str | None = None,
        HealthCheckGracePeriod: int | None = None,
        PlacementGroup: str | None = None,
        VPCZoneIdentifier: str | None = None,
        TerminationPolicies: list[str] | None = None,
        NewInstancesProtectedFromScaleIn: bool | None = None,
        ServiceLinkedRoleARN: str | None = None,
        MaxInstanceLifetime: int | None = None,
        CapacityRebalance: bool | None = None,
        Context: str | None = None,
        DesiredCapacityType: str | None = None,
        DefaultInstanceWarmup: int | None = None,
        InstanceMaintenancePolicy: dict[str, Any] | None = None,
        AvailabilityZoneDistribution: dict[str, Any] | None = None,
        AvailabilityZoneImpairmentPolicy: dict[str, Any] | None = None,
        SkipZonalShiftValidation: bool | None = None,
        CapacityReservationSpecification: dict[str, Any] | None = None,
        InstanceLifecyclePolicy: dict[str, Any] | None = None,
        DeletionProtection: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
