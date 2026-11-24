from werkflow_aws.models.autoscaling import (
    AutoScalingAttachInstancesRequest,
    AutoScalingAttachInstancesResponse,
    AutoScalingAttachLoadBalancerTargetGroupsRequest,
    AutoScalingAttachLoadBalancerTargetGroupsResponse,
    AutoScalingAttachLoadBalancersRequest,
    AutoScalingAttachLoadBalancersResponse,
    AutoScalingAttachTrafficSourcesRequest,
    AutoScalingAttachTrafficSourcesResponse,
    AutoScalingBatchDeleteScheduledActionRequest,
    AutoScalingBatchDeleteScheduledActionResponse,
    AutoScalingBatchPutScheduledUpdateGroupActionRequest,
    AutoScalingBatchPutScheduledUpdateGroupActionResponse,
    AutoScalingCancelInstanceRefreshRequest,
    AutoScalingCancelInstanceRefreshResponse,
    AutoScalingCompleteLifecycleActionRequest,
    AutoScalingCompleteLifecycleActionResponse,
    AutoScalingCreateAutoScalingGroupRequest,
    AutoScalingCreateAutoScalingGroupResponse,
    AutoScalingCreateLaunchConfigurationRequest,
    AutoScalingCreateLaunchConfigurationResponse,
    AutoScalingCreateOrUpdateTagsRequest,
    AutoScalingCreateOrUpdateTagsResponse,
    AutoScalingDeleteAutoScalingGroupRequest,
    AutoScalingDeleteAutoScalingGroupResponse,
    AutoScalingDeleteLaunchConfigurationRequest,
    AutoScalingDeleteLaunchConfigurationResponse,
    AutoScalingDeleteLifecycleHookRequest,
    AutoScalingDeleteLifecycleHookResponse,
    AutoScalingDeleteNotificationConfigurationRequest,
    AutoScalingDeleteNotificationConfigurationResponse,
    AutoScalingDeletePolicyRequest,
    AutoScalingDeletePolicyResponse,
    AutoScalingDeleteScheduledActionRequest,
    AutoScalingDeleteScheduledActionResponse,
    AutoScalingDeleteTagsRequest,
    AutoScalingDeleteTagsResponse,
    AutoScalingDeleteWarmPoolRequest,
    AutoScalingDeleteWarmPoolResponse,
    AutoScalingDescribeAccountLimitsRequest,
    AutoScalingDescribeAccountLimitsResponse,
    AutoScalingDescribeAccountSettingsRequest,
    AutoScalingDescribeAccountSettingsResponse,
    AutoScalingDescribeAdjustmentTypesRequest,
    AutoScalingDescribeAdjustmentTypesResponse,
    AutoScalingDescribeAutoScalingGroupsRequest,
    AutoScalingDescribeAutoScalingGroupsResponse,
    AutoScalingDescribeAutoScalingInstancesRequest,
    AutoScalingDescribeAutoScalingInstancesResponse,
    AutoScalingDescribeAutoScalingNotificationTypesRequest,
    AutoScalingDescribeAutoScalingNotificationTypesResponse,
    AutoScalingDescribeInstanceRefreshesRequest,
    AutoScalingDescribeInstanceRefreshesResponse,
    AutoScalingDescribeLaunchConfigurationsRequest,
    AutoScalingDescribeLaunchConfigurationsResponse,
    AutoScalingDescribeLifecycleHookTypesRequest,
    AutoScalingDescribeLifecycleHookTypesResponse,
    AutoScalingDescribeLifecycleHooksRequest,
    AutoScalingDescribeLifecycleHooksResponse,
    AutoScalingDescribeLoadBalancerTargetGroupsRequest,
    AutoScalingDescribeLoadBalancerTargetGroupsResponse,
    AutoScalingDescribeLoadBalancersRequest,
    AutoScalingDescribeLoadBalancersResponse,
    AutoScalingDescribeMetricCollectionTypesRequest,
    AutoScalingDescribeMetricCollectionTypesResponse,
    AutoScalingDescribeNotificationConfigurationsRequest,
    AutoScalingDescribeNotificationConfigurationsResponse,
    AutoScalingDescribePoliciesRequest,
    AutoScalingDescribePoliciesResponse,
    AutoScalingDescribeScalingActivitiesRequest,
    AutoScalingDescribeScalingActivitiesResponse,
    AutoScalingDescribeScalingProcessTypesRequest,
    AutoScalingDescribeScalingProcessTypesResponse,
    AutoScalingDescribeScheduledActionsRequest,
    AutoScalingDescribeScheduledActionsResponse,
    AutoScalingDescribeTagsRequest,
    AutoScalingDescribeTagsResponse,
    AutoScalingDescribeTerminationPolicyTypesRequest,
    AutoScalingDescribeTerminationPolicyTypesResponse,
    AutoScalingDescribeTrafficSourcesRequest,
    AutoScalingDescribeTrafficSourcesResponse,
    AutoScalingDescribeWarmPoolRequest,
    AutoScalingDescribeWarmPoolResponse,
    AutoScalingDetachInstancesRequest,
    AutoScalingDetachInstancesResponse,
    AutoScalingDetachLoadBalancerTargetGroupsRequest,
    AutoScalingDetachLoadBalancerTargetGroupsResponse,
    AutoScalingDetachLoadBalancersRequest,
    AutoScalingDetachLoadBalancersResponse,
    AutoScalingDetachTrafficSourcesRequest,
    AutoScalingDetachTrafficSourcesResponse,
    AutoScalingDisableMetricsCollectionRequest,
    AutoScalingDisableMetricsCollectionResponse,
    AutoScalingEnableMetricsCollectionRequest,
    AutoScalingEnableMetricsCollectionResponse,
    AutoScalingEnterStandbyRequest,
    AutoScalingEnterStandbyResponse,
    AutoScalingExecutePolicyRequest,
    AutoScalingExecutePolicyResponse,
    AutoScalingExitStandbyRequest,
    AutoScalingExitStandbyResponse,
    AutoScalingGetPredictiveScalingForecastRequest,
    AutoScalingGetPredictiveScalingForecastResponse,
    AutoScalingLaunchInstancesRequest,
    AutoScalingLaunchInstancesResponse,
    AutoScalingPutAccountSettingRequest,
    AutoScalingPutAccountSettingResponse,
    AutoScalingPutLifecycleHookRequest,
    AutoScalingPutLifecycleHookResponse,
    AutoScalingPutNotificationConfigurationRequest,
    AutoScalingPutNotificationConfigurationResponse,
    AutoScalingPutScalingPolicyRequest,
    AutoScalingPutScalingPolicyResponse,
    AutoScalingPutScheduledUpdateGroupActionRequest,
    AutoScalingPutScheduledUpdateGroupActionResponse,
    AutoScalingPutWarmPoolRequest,
    AutoScalingPutWarmPoolResponse,
    AutoScalingRecordLifecycleActionHeartbeatRequest,
    AutoScalingRecordLifecycleActionHeartbeatResponse,
    AutoScalingResumeProcessesRequest,
    AutoScalingResumeProcessesResponse,
    AutoScalingRollbackInstanceRefreshRequest,
    AutoScalingRollbackInstanceRefreshResponse,
    AutoScalingSetDesiredCapacityRequest,
    AutoScalingSetDesiredCapacityResponse,
    AutoScalingSetInstanceHealthRequest,
    AutoScalingSetInstanceHealthResponse,
    AutoScalingSetInstanceProtectionRequest,
    AutoScalingSetInstanceProtectionResponse,
    AutoScalingStartInstanceRefreshRequest,
    AutoScalingStartInstanceRefreshResponse,
    AutoScalingSuspendProcessesRequest,
    AutoScalingSuspendProcessesResponse,
    AutoScalingTerminateInstanceInAutoScalingGroupRequest,
    AutoScalingTerminateInstanceInAutoScalingGroupResponse,
    AutoScalingUpdateAutoScalingGroupRequest,
    AutoScalingUpdateAutoScalingGroupResponse,
)
from werkflow_aws.types.autoscaling_client import AutoScalingClient
from .base import AWSBaseService


class AWSAutoScaling(AWSBaseService[AutoScalingClient]):
    service_name = 'autoscaling'
    boto3_service_name = 'autoscaling'

    def __init__(self) -> None:
        super().__init__(service_name='autoscaling', boto3_service_name='autoscaling')

    async def attach_instances(
        self,
        request: AutoScalingAttachInstancesRequest,
    ) -> AutoScalingAttachInstancesResponse:
        client = self._require_client()
        return await self._execute(client.attach_instances, request, AutoScalingAttachInstancesResponse)

    async def attach_load_balancer_target_groups(
        self,
        request: AutoScalingAttachLoadBalancerTargetGroupsRequest,
    ) -> AutoScalingAttachLoadBalancerTargetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.attach_load_balancer_target_groups, request, AutoScalingAttachLoadBalancerTargetGroupsResponse)

    async def attach_load_balancers(
        self,
        request: AutoScalingAttachLoadBalancersRequest,
    ) -> AutoScalingAttachLoadBalancersResponse:
        client = self._require_client()
        return await self._execute(client.attach_load_balancers, request, AutoScalingAttachLoadBalancersResponse)

    async def attach_traffic_sources(
        self,
        request: AutoScalingAttachTrafficSourcesRequest,
    ) -> AutoScalingAttachTrafficSourcesResponse:
        client = self._require_client()
        return await self._execute(client.attach_traffic_sources, request, AutoScalingAttachTrafficSourcesResponse)

    async def batch_delete_scheduled_action(
        self,
        request: AutoScalingBatchDeleteScheduledActionRequest,
    ) -> AutoScalingBatchDeleteScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_scheduled_action, request, AutoScalingBatchDeleteScheduledActionResponse)

    async def batch_put_scheduled_update_group_action(
        self,
        request: AutoScalingBatchPutScheduledUpdateGroupActionRequest,
    ) -> AutoScalingBatchPutScheduledUpdateGroupActionResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_scheduled_update_group_action, request, AutoScalingBatchPutScheduledUpdateGroupActionResponse)

    async def cancel_instance_refresh(
        self,
        request: AutoScalingCancelInstanceRefreshRequest,
    ) -> AutoScalingCancelInstanceRefreshResponse:
        client = self._require_client()
        return await self._execute(client.cancel_instance_refresh, request, AutoScalingCancelInstanceRefreshResponse)

    async def complete_lifecycle_action(
        self,
        request: AutoScalingCompleteLifecycleActionRequest,
    ) -> AutoScalingCompleteLifecycleActionResponse:
        client = self._require_client()
        return await self._execute(client.complete_lifecycle_action, request, AutoScalingCompleteLifecycleActionResponse)

    async def create_auto_scaling_group(
        self,
        request: AutoScalingCreateAutoScalingGroupRequest,
    ) -> AutoScalingCreateAutoScalingGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_auto_scaling_group, request, AutoScalingCreateAutoScalingGroupResponse)

    async def create_launch_configuration(
        self,
        request: AutoScalingCreateLaunchConfigurationRequest,
    ) -> AutoScalingCreateLaunchConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_launch_configuration, request, AutoScalingCreateLaunchConfigurationResponse)

    async def create_or_update_tags(
        self,
        request: AutoScalingCreateOrUpdateTagsRequest,
    ) -> AutoScalingCreateOrUpdateTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_or_update_tags, request, AutoScalingCreateOrUpdateTagsResponse)

    async def delete_auto_scaling_group(
        self,
        request: AutoScalingDeleteAutoScalingGroupRequest,
    ) -> AutoScalingDeleteAutoScalingGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_auto_scaling_group, request, AutoScalingDeleteAutoScalingGroupResponse)

    async def delete_launch_configuration(
        self,
        request: AutoScalingDeleteLaunchConfigurationRequest,
    ) -> AutoScalingDeleteLaunchConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_launch_configuration, request, AutoScalingDeleteLaunchConfigurationResponse)

    async def delete_lifecycle_hook(
        self,
        request: AutoScalingDeleteLifecycleHookRequest,
    ) -> AutoScalingDeleteLifecycleHookResponse:
        client = self._require_client()
        return await self._execute(client.delete_lifecycle_hook, request, AutoScalingDeleteLifecycleHookResponse)

    async def delete_notification_configuration(
        self,
        request: AutoScalingDeleteNotificationConfigurationRequest,
    ) -> AutoScalingDeleteNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_notification_configuration, request, AutoScalingDeleteNotificationConfigurationResponse)

    async def delete_policy(
        self,
        request: AutoScalingDeletePolicyRequest,
    ) -> AutoScalingDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy, request, AutoScalingDeletePolicyResponse)

    async def delete_scheduled_action(
        self,
        request: AutoScalingDeleteScheduledActionRequest,
    ) -> AutoScalingDeleteScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduled_action, request, AutoScalingDeleteScheduledActionResponse)

    async def delete_tags(
        self,
        request: AutoScalingDeleteTagsRequest,
    ) -> AutoScalingDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, AutoScalingDeleteTagsResponse)

    async def delete_warm_pool(
        self,
        request: AutoScalingDeleteWarmPoolRequest,
    ) -> AutoScalingDeleteWarmPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_warm_pool, request, AutoScalingDeleteWarmPoolResponse)

    async def describe_account_limits(
        self,
        request: AutoScalingDescribeAccountLimitsRequest | None = None,
    ) -> AutoScalingDescribeAccountLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_limits, request, AutoScalingDescribeAccountLimitsResponse)

    async def describe_account_settings(
        self,
        request: AutoScalingDescribeAccountSettingsRequest | None = None,
    ) -> AutoScalingDescribeAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_settings, request, AutoScalingDescribeAccountSettingsResponse)

    async def describe_adjustment_types(
        self,
        request: AutoScalingDescribeAdjustmentTypesRequest | None = None,
    ) -> AutoScalingDescribeAdjustmentTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_adjustment_types, request, AutoScalingDescribeAdjustmentTypesResponse)

    async def describe_auto_scaling_groups(
        self,
        request: AutoScalingDescribeAutoScalingGroupsRequest | None = None,
    ) -> AutoScalingDescribeAutoScalingGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_auto_scaling_groups, request, AutoScalingDescribeAutoScalingGroupsResponse)

    async def describe_auto_scaling_groups_paginated(
        self,
        request: AutoScalingDescribeAutoScalingGroupsRequest | None = None,
    ) -> list[AutoScalingDescribeAutoScalingGroupsResponse]:
        return await self._paginate('describe_auto_scaling_groups', request, AutoScalingDescribeAutoScalingGroupsResponse)

    async def describe_auto_scaling_instances(
        self,
        request: AutoScalingDescribeAutoScalingInstancesRequest | None = None,
    ) -> AutoScalingDescribeAutoScalingInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_auto_scaling_instances, request, AutoScalingDescribeAutoScalingInstancesResponse)

    async def describe_auto_scaling_instances_paginated(
        self,
        request: AutoScalingDescribeAutoScalingInstancesRequest | None = None,
    ) -> list[AutoScalingDescribeAutoScalingInstancesResponse]:
        return await self._paginate('describe_auto_scaling_instances', request, AutoScalingDescribeAutoScalingInstancesResponse)

    async def describe_auto_scaling_notification_types(
        self,
        request: AutoScalingDescribeAutoScalingNotificationTypesRequest | None = None,
    ) -> AutoScalingDescribeAutoScalingNotificationTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_auto_scaling_notification_types, request, AutoScalingDescribeAutoScalingNotificationTypesResponse)

    async def describe_instance_refreshes(
        self,
        request: AutoScalingDescribeInstanceRefreshesRequest,
    ) -> AutoScalingDescribeInstanceRefreshesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_refreshes, request, AutoScalingDescribeInstanceRefreshesResponse)

    async def describe_launch_configurations(
        self,
        request: AutoScalingDescribeLaunchConfigurationsRequest | None = None,
    ) -> AutoScalingDescribeLaunchConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_launch_configurations, request, AutoScalingDescribeLaunchConfigurationsResponse)

    async def describe_launch_configurations_paginated(
        self,
        request: AutoScalingDescribeLaunchConfigurationsRequest | None = None,
    ) -> list[AutoScalingDescribeLaunchConfigurationsResponse]:
        return await self._paginate('describe_launch_configurations', request, AutoScalingDescribeLaunchConfigurationsResponse)

    async def describe_lifecycle_hook_types(
        self,
        request: AutoScalingDescribeLifecycleHookTypesRequest | None = None,
    ) -> AutoScalingDescribeLifecycleHookTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_lifecycle_hook_types, request, AutoScalingDescribeLifecycleHookTypesResponse)

    async def describe_lifecycle_hooks(
        self,
        request: AutoScalingDescribeLifecycleHooksRequest,
    ) -> AutoScalingDescribeLifecycleHooksResponse:
        client = self._require_client()
        return await self._execute(client.describe_lifecycle_hooks, request, AutoScalingDescribeLifecycleHooksResponse)

    async def describe_load_balancer_target_groups(
        self,
        request: AutoScalingDescribeLoadBalancerTargetGroupsRequest,
    ) -> AutoScalingDescribeLoadBalancerTargetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_load_balancer_target_groups, request, AutoScalingDescribeLoadBalancerTargetGroupsResponse)

    async def describe_load_balancer_target_groups_paginated(
        self,
        request: AutoScalingDescribeLoadBalancerTargetGroupsRequest,
    ) -> list[AutoScalingDescribeLoadBalancerTargetGroupsResponse]:
        return await self._paginate('describe_load_balancer_target_groups', request, AutoScalingDescribeLoadBalancerTargetGroupsResponse)

    async def describe_load_balancers(
        self,
        request: AutoScalingDescribeLoadBalancersRequest,
    ) -> AutoScalingDescribeLoadBalancersResponse:
        client = self._require_client()
        return await self._execute(client.describe_load_balancers, request, AutoScalingDescribeLoadBalancersResponse)

    async def describe_load_balancers_paginated(
        self,
        request: AutoScalingDescribeLoadBalancersRequest,
    ) -> list[AutoScalingDescribeLoadBalancersResponse]:
        return await self._paginate('describe_load_balancers', request, AutoScalingDescribeLoadBalancersResponse)

    async def describe_metric_collection_types(
        self,
        request: AutoScalingDescribeMetricCollectionTypesRequest | None = None,
    ) -> AutoScalingDescribeMetricCollectionTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_metric_collection_types, request, AutoScalingDescribeMetricCollectionTypesResponse)

    async def describe_notification_configurations(
        self,
        request: AutoScalingDescribeNotificationConfigurationsRequest | None = None,
    ) -> AutoScalingDescribeNotificationConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_notification_configurations, request, AutoScalingDescribeNotificationConfigurationsResponse)

    async def describe_notification_configurations_paginated(
        self,
        request: AutoScalingDescribeNotificationConfigurationsRequest | None = None,
    ) -> list[AutoScalingDescribeNotificationConfigurationsResponse]:
        return await self._paginate('describe_notification_configurations', request, AutoScalingDescribeNotificationConfigurationsResponse)

    async def describe_policies(
        self,
        request: AutoScalingDescribePoliciesRequest | None = None,
    ) -> AutoScalingDescribePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_policies, request, AutoScalingDescribePoliciesResponse)

    async def describe_policies_paginated(
        self,
        request: AutoScalingDescribePoliciesRequest | None = None,
    ) -> list[AutoScalingDescribePoliciesResponse]:
        return await self._paginate('describe_policies', request, AutoScalingDescribePoliciesResponse)

    async def describe_scaling_activities(
        self,
        request: AutoScalingDescribeScalingActivitiesRequest | None = None,
    ) -> AutoScalingDescribeScalingActivitiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_scaling_activities, request, AutoScalingDescribeScalingActivitiesResponse)

    async def describe_scaling_activities_paginated(
        self,
        request: AutoScalingDescribeScalingActivitiesRequest | None = None,
    ) -> list[AutoScalingDescribeScalingActivitiesResponse]:
        return await self._paginate('describe_scaling_activities', request, AutoScalingDescribeScalingActivitiesResponse)

    async def describe_scaling_process_types(
        self,
        request: AutoScalingDescribeScalingProcessTypesRequest | None = None,
    ) -> AutoScalingDescribeScalingProcessTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_scaling_process_types, request, AutoScalingDescribeScalingProcessTypesResponse)

    async def describe_scheduled_actions(
        self,
        request: AutoScalingDescribeScheduledActionsRequest | None = None,
    ) -> AutoScalingDescribeScheduledActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_actions, request, AutoScalingDescribeScheduledActionsResponse)

    async def describe_scheduled_actions_paginated(
        self,
        request: AutoScalingDescribeScheduledActionsRequest | None = None,
    ) -> list[AutoScalingDescribeScheduledActionsResponse]:
        return await self._paginate('describe_scheduled_actions', request, AutoScalingDescribeScheduledActionsResponse)

    async def describe_tags(
        self,
        request: AutoScalingDescribeTagsRequest | None = None,
    ) -> AutoScalingDescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, AutoScalingDescribeTagsResponse)

    async def describe_tags_paginated(
        self,
        request: AutoScalingDescribeTagsRequest | None = None,
    ) -> list[AutoScalingDescribeTagsResponse]:
        return await self._paginate('describe_tags', request, AutoScalingDescribeTagsResponse)

    async def describe_termination_policy_types(
        self,
        request: AutoScalingDescribeTerminationPolicyTypesRequest | None = None,
    ) -> AutoScalingDescribeTerminationPolicyTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_termination_policy_types, request, AutoScalingDescribeTerminationPolicyTypesResponse)

    async def describe_traffic_sources(
        self,
        request: AutoScalingDescribeTrafficSourcesRequest,
    ) -> AutoScalingDescribeTrafficSourcesResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_sources, request, AutoScalingDescribeTrafficSourcesResponse)

    async def describe_warm_pool(
        self,
        request: AutoScalingDescribeWarmPoolRequest,
    ) -> AutoScalingDescribeWarmPoolResponse:
        client = self._require_client()
        return await self._execute(client.describe_warm_pool, request, AutoScalingDescribeWarmPoolResponse)

    async def describe_warm_pool_paginated(
        self,
        request: AutoScalingDescribeWarmPoolRequest,
    ) -> list[AutoScalingDescribeWarmPoolResponse]:
        return await self._paginate('describe_warm_pool', request, AutoScalingDescribeWarmPoolResponse)

    async def detach_instances(
        self,
        request: AutoScalingDetachInstancesRequest,
    ) -> AutoScalingDetachInstancesResponse:
        client = self._require_client()
        return await self._execute(client.detach_instances, request, AutoScalingDetachInstancesResponse)

    async def detach_load_balancer_target_groups(
        self,
        request: AutoScalingDetachLoadBalancerTargetGroupsRequest,
    ) -> AutoScalingDetachLoadBalancerTargetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.detach_load_balancer_target_groups, request, AutoScalingDetachLoadBalancerTargetGroupsResponse)

    async def detach_load_balancers(
        self,
        request: AutoScalingDetachLoadBalancersRequest,
    ) -> AutoScalingDetachLoadBalancersResponse:
        client = self._require_client()
        return await self._execute(client.detach_load_balancers, request, AutoScalingDetachLoadBalancersResponse)

    async def detach_traffic_sources(
        self,
        request: AutoScalingDetachTrafficSourcesRequest,
    ) -> AutoScalingDetachTrafficSourcesResponse:
        client = self._require_client()
        return await self._execute(client.detach_traffic_sources, request, AutoScalingDetachTrafficSourcesResponse)

    async def disable_metrics_collection(
        self,
        request: AutoScalingDisableMetricsCollectionRequest,
    ) -> AutoScalingDisableMetricsCollectionResponse:
        client = self._require_client()
        return await self._execute(client.disable_metrics_collection, request, AutoScalingDisableMetricsCollectionResponse)

    async def enable_metrics_collection(
        self,
        request: AutoScalingEnableMetricsCollectionRequest,
    ) -> AutoScalingEnableMetricsCollectionResponse:
        client = self._require_client()
        return await self._execute(client.enable_metrics_collection, request, AutoScalingEnableMetricsCollectionResponse)

    async def enter_standby(
        self,
        request: AutoScalingEnterStandbyRequest,
    ) -> AutoScalingEnterStandbyResponse:
        client = self._require_client()
        return await self._execute(client.enter_standby, request, AutoScalingEnterStandbyResponse)

    async def execute_policy(
        self,
        request: AutoScalingExecutePolicyRequest,
    ) -> AutoScalingExecutePolicyResponse:
        client = self._require_client()
        return await self._execute(client.execute_policy, request, AutoScalingExecutePolicyResponse)

    async def exit_standby(
        self,
        request: AutoScalingExitStandbyRequest,
    ) -> AutoScalingExitStandbyResponse:
        client = self._require_client()
        return await self._execute(client.exit_standby, request, AutoScalingExitStandbyResponse)

    async def get_predictive_scaling_forecast(
        self,
        request: AutoScalingGetPredictiveScalingForecastRequest,
    ) -> AutoScalingGetPredictiveScalingForecastResponse:
        client = self._require_client()
        return await self._execute(client.get_predictive_scaling_forecast, request, AutoScalingGetPredictiveScalingForecastResponse)

    async def launch_instances(
        self,
        request: AutoScalingLaunchInstancesRequest,
    ) -> AutoScalingLaunchInstancesResponse:
        client = self._require_client()
        return await self._execute(client.launch_instances, request, AutoScalingLaunchInstancesResponse)

    async def put_account_setting(
        self,
        request: AutoScalingPutAccountSettingRequest,
    ) -> AutoScalingPutAccountSettingResponse:
        client = self._require_client()
        return await self._execute(client.put_account_setting, request, AutoScalingPutAccountSettingResponse)

    async def put_lifecycle_hook(
        self,
        request: AutoScalingPutLifecycleHookRequest,
    ) -> AutoScalingPutLifecycleHookResponse:
        client = self._require_client()
        return await self._execute(client.put_lifecycle_hook, request, AutoScalingPutLifecycleHookResponse)

    async def put_notification_configuration(
        self,
        request: AutoScalingPutNotificationConfigurationRequest,
    ) -> AutoScalingPutNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_notification_configuration, request, AutoScalingPutNotificationConfigurationResponse)

    async def put_scaling_policy(
        self,
        request: AutoScalingPutScalingPolicyRequest,
    ) -> AutoScalingPutScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_scaling_policy, request, AutoScalingPutScalingPolicyResponse)

    async def put_scheduled_update_group_action(
        self,
        request: AutoScalingPutScheduledUpdateGroupActionRequest,
    ) -> AutoScalingPutScheduledUpdateGroupActionResponse:
        client = self._require_client()
        return await self._execute(client.put_scheduled_update_group_action, request, AutoScalingPutScheduledUpdateGroupActionResponse)

    async def put_warm_pool(
        self,
        request: AutoScalingPutWarmPoolRequest,
    ) -> AutoScalingPutWarmPoolResponse:
        client = self._require_client()
        return await self._execute(client.put_warm_pool, request, AutoScalingPutWarmPoolResponse)

    async def record_lifecycle_action_heartbeat(
        self,
        request: AutoScalingRecordLifecycleActionHeartbeatRequest,
    ) -> AutoScalingRecordLifecycleActionHeartbeatResponse:
        client = self._require_client()
        return await self._execute(client.record_lifecycle_action_heartbeat, request, AutoScalingRecordLifecycleActionHeartbeatResponse)

    async def resume_processes(
        self,
        request: AutoScalingResumeProcessesRequest,
    ) -> AutoScalingResumeProcessesResponse:
        client = self._require_client()
        return await self._execute(client.resume_processes, request, AutoScalingResumeProcessesResponse)

    async def rollback_instance_refresh(
        self,
        request: AutoScalingRollbackInstanceRefreshRequest,
    ) -> AutoScalingRollbackInstanceRefreshResponse:
        client = self._require_client()
        return await self._execute(client.rollback_instance_refresh, request, AutoScalingRollbackInstanceRefreshResponse)

    async def set_desired_capacity(
        self,
        request: AutoScalingSetDesiredCapacityRequest,
    ) -> AutoScalingSetDesiredCapacityResponse:
        client = self._require_client()
        return await self._execute(client.set_desired_capacity, request, AutoScalingSetDesiredCapacityResponse)

    async def set_instance_health(
        self,
        request: AutoScalingSetInstanceHealthRequest,
    ) -> AutoScalingSetInstanceHealthResponse:
        client = self._require_client()
        return await self._execute(client.set_instance_health, request, AutoScalingSetInstanceHealthResponse)

    async def set_instance_protection(
        self,
        request: AutoScalingSetInstanceProtectionRequest,
    ) -> AutoScalingSetInstanceProtectionResponse:
        client = self._require_client()
        return await self._execute(client.set_instance_protection, request, AutoScalingSetInstanceProtectionResponse)

    async def start_instance_refresh(
        self,
        request: AutoScalingStartInstanceRefreshRequest,
    ) -> AutoScalingStartInstanceRefreshResponse:
        client = self._require_client()
        return await self._execute(client.start_instance_refresh, request, AutoScalingStartInstanceRefreshResponse)

    async def suspend_processes(
        self,
        request: AutoScalingSuspendProcessesRequest,
    ) -> AutoScalingSuspendProcessesResponse:
        client = self._require_client()
        return await self._execute(client.suspend_processes, request, AutoScalingSuspendProcessesResponse)

    async def terminate_instance_in_auto_scaling_group(
        self,
        request: AutoScalingTerminateInstanceInAutoScalingGroupRequest,
    ) -> AutoScalingTerminateInstanceInAutoScalingGroupResponse:
        client = self._require_client()
        return await self._execute(client.terminate_instance_in_auto_scaling_group, request, AutoScalingTerminateInstanceInAutoScalingGroupResponse)

    async def update_auto_scaling_group(
        self,
        request: AutoScalingUpdateAutoScalingGroupRequest,
    ) -> AutoScalingUpdateAutoScalingGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_auto_scaling_group, request, AutoScalingUpdateAutoScalingGroupResponse)
