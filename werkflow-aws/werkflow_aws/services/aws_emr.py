from werkflow_aws.models.emr import (
    EMRAddInstanceFleetRequest,
    EMRAddInstanceFleetResponse,
    EMRAddInstanceGroupsRequest,
    EMRAddInstanceGroupsResponse,
    EMRAddJobFlowStepsRequest,
    EMRAddJobFlowStepsResponse,
    EMRAddTagsRequest,
    EMRAddTagsResponse,
    EMRCancelStepsRequest,
    EMRCancelStepsResponse,
    EMRCreatePersistentAppUIRequest,
    EMRCreatePersistentAppUIResponse,
    EMRCreateSecurityConfigurationRequest,
    EMRCreateSecurityConfigurationResponse,
    EMRCreateStudioRequest,
    EMRCreateStudioResponse,
    EMRCreateStudioSessionMappingRequest,
    EMRCreateStudioSessionMappingResponse,
    EMRDeleteSecurityConfigurationRequest,
    EMRDeleteSecurityConfigurationResponse,
    EMRDeleteStudioRequest,
    EMRDeleteStudioResponse,
    EMRDeleteStudioSessionMappingRequest,
    EMRDeleteStudioSessionMappingResponse,
    EMRDescribeClusterRequest,
    EMRDescribeClusterResponse,
    EMRDescribeJobFlowsRequest,
    EMRDescribeJobFlowsResponse,
    EMRDescribeNotebookExecutionRequest,
    EMRDescribeNotebookExecutionResponse,
    EMRDescribePersistentAppUIRequest,
    EMRDescribePersistentAppUIResponse,
    EMRDescribeReleaseLabelRequest,
    EMRDescribeReleaseLabelResponse,
    EMRDescribeSecurityConfigurationRequest,
    EMRDescribeSecurityConfigurationResponse,
    EMRDescribeStepRequest,
    EMRDescribeStepResponse,
    EMRDescribeStudioRequest,
    EMRDescribeStudioResponse,
    EMRGetAutoTerminationPolicyRequest,
    EMRGetAutoTerminationPolicyResponse,
    EMRGetBlockPublicAccessConfigurationRequest,
    EMRGetBlockPublicAccessConfigurationResponse,
    EMRGetClusterSessionCredentialsRequest,
    EMRGetClusterSessionCredentialsResponse,
    EMRGetManagedScalingPolicyRequest,
    EMRGetManagedScalingPolicyResponse,
    EMRGetOnClusterAppUIPresignedURLRequest,
    EMRGetOnClusterAppUIPresignedURLResponse,
    EMRGetPersistentAppUIPresignedURLRequest,
    EMRGetPersistentAppUIPresignedURLResponse,
    EMRGetSessionEndpointRequest,
    EMRGetSessionEndpointResponse,
    EMRGetSessionRequest,
    EMRGetSessionResponse,
    EMRGetStudioSessionMappingRequest,
    EMRGetStudioSessionMappingResponse,
    EMRListBootstrapActionsRequest,
    EMRListBootstrapActionsResponse,
    EMRListClustersRequest,
    EMRListClustersResponse,
    EMRListInstanceFleetsRequest,
    EMRListInstanceFleetsResponse,
    EMRListInstanceGroupsRequest,
    EMRListInstanceGroupsResponse,
    EMRListInstancesRequest,
    EMRListInstancesResponse,
    EMRListNotebookExecutionsRequest,
    EMRListNotebookExecutionsResponse,
    EMRListReleaseLabelsRequest,
    EMRListReleaseLabelsResponse,
    EMRListSecurityConfigurationsRequest,
    EMRListSecurityConfigurationsResponse,
    EMRListSessionsRequest,
    EMRListSessionsResponse,
    EMRListStepsRequest,
    EMRListStepsResponse,
    EMRListStudioSessionMappingsRequest,
    EMRListStudioSessionMappingsResponse,
    EMRListStudiosRequest,
    EMRListStudiosResponse,
    EMRListSupportedInstanceTypesRequest,
    EMRListSupportedInstanceTypesResponse,
    EMRModifyClusterRequest,
    EMRModifyClusterResponse,
    EMRModifyInstanceFleetRequest,
    EMRModifyInstanceFleetResponse,
    EMRModifyInstanceGroupsRequest,
    EMRModifyInstanceGroupsResponse,
    EMRPutAutoScalingPolicyRequest,
    EMRPutAutoScalingPolicyResponse,
    EMRPutAutoTerminationPolicyRequest,
    EMRPutAutoTerminationPolicyResponse,
    EMRPutBlockPublicAccessConfigurationRequest,
    EMRPutBlockPublicAccessConfigurationResponse,
    EMRPutManagedScalingPolicyRequest,
    EMRPutManagedScalingPolicyResponse,
    EMRRemoveAutoScalingPolicyRequest,
    EMRRemoveAutoScalingPolicyResponse,
    EMRRemoveAutoTerminationPolicyRequest,
    EMRRemoveAutoTerminationPolicyResponse,
    EMRRemoveManagedScalingPolicyRequest,
    EMRRemoveManagedScalingPolicyResponse,
    EMRRemoveTagsRequest,
    EMRRemoveTagsResponse,
    EMRRunJobFlowRequest,
    EMRRunJobFlowResponse,
    EMRSetKeepJobFlowAliveWhenNoStepsRequest,
    EMRSetKeepJobFlowAliveWhenNoStepsResponse,
    EMRSetTerminationProtectionRequest,
    EMRSetTerminationProtectionResponse,
    EMRSetUnhealthyNodeReplacementRequest,
    EMRSetUnhealthyNodeReplacementResponse,
    EMRSetVisibleToAllUsersRequest,
    EMRSetVisibleToAllUsersResponse,
    EMRStartNotebookExecutionRequest,
    EMRStartNotebookExecutionResponse,
    EMRStartSessionRequest,
    EMRStartSessionResponse,
    EMRStopNotebookExecutionRequest,
    EMRStopNotebookExecutionResponse,
    EMRTerminateJobFlowsRequest,
    EMRTerminateJobFlowsResponse,
    EMRTerminateSessionRequest,
    EMRTerminateSessionResponse,
    EMRUpdateStudioRequest,
    EMRUpdateStudioResponse,
    EMRUpdateStudioSessionMappingRequest,
    EMRUpdateStudioSessionMappingResponse,
)
from werkflow_aws.types.emr_client import EMRClient
from .base import AWSBaseService


class AWSEMR(AWSBaseService[EMRClient]):
    service_name = 'emr'
    boto3_service_name = 'emr'

    def __init__(self) -> None:
        super().__init__(service_name='emr', boto3_service_name='emr')

    async def add_instance_fleet(
        self,
        request: EMRAddInstanceFleetRequest,
    ) -> EMRAddInstanceFleetResponse:
        client = self._require_client()
        return await self._execute(client.add_instance_fleet, request, EMRAddInstanceFleetResponse)

    async def add_instance_groups(
        self,
        request: EMRAddInstanceGroupsRequest,
    ) -> EMRAddInstanceGroupsResponse:
        client = self._require_client()
        return await self._execute(client.add_instance_groups, request, EMRAddInstanceGroupsResponse)

    async def add_job_flow_steps(
        self,
        request: EMRAddJobFlowStepsRequest,
    ) -> EMRAddJobFlowStepsResponse:
        client = self._require_client()
        return await self._execute(client.add_job_flow_steps, request, EMRAddJobFlowStepsResponse)

    async def add_tags(
        self,
        request: EMRAddTagsRequest,
    ) -> EMRAddTagsResponse:
        client = self._require_client()
        return await self._execute(client.add_tags, request, EMRAddTagsResponse)

    async def cancel_steps(
        self,
        request: EMRCancelStepsRequest,
    ) -> EMRCancelStepsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_steps, request, EMRCancelStepsResponse)

    async def create_persistent_app_ui(
        self,
        request: EMRCreatePersistentAppUIRequest,
    ) -> EMRCreatePersistentAppUIResponse:
        client = self._require_client()
        return await self._execute(client.create_persistent_app_ui, request, EMRCreatePersistentAppUIResponse)

    async def create_security_configuration(
        self,
        request: EMRCreateSecurityConfigurationRequest,
    ) -> EMRCreateSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_security_configuration, request, EMRCreateSecurityConfigurationResponse)

    async def create_studio(
        self,
        request: EMRCreateStudioRequest,
    ) -> EMRCreateStudioResponse:
        client = self._require_client()
        return await self._execute(client.create_studio, request, EMRCreateStudioResponse)

    async def create_studio_session_mapping(
        self,
        request: EMRCreateStudioSessionMappingRequest,
    ) -> EMRCreateStudioSessionMappingResponse:
        client = self._require_client()
        return await self._execute(client.create_studio_session_mapping, request, EMRCreateStudioSessionMappingResponse)

    async def delete_security_configuration(
        self,
        request: EMRDeleteSecurityConfigurationRequest,
    ) -> EMRDeleteSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_configuration, request, EMRDeleteSecurityConfigurationResponse)

    async def delete_studio(
        self,
        request: EMRDeleteStudioRequest,
    ) -> EMRDeleteStudioResponse:
        client = self._require_client()
        return await self._execute(client.delete_studio, request, EMRDeleteStudioResponse)

    async def delete_studio_session_mapping(
        self,
        request: EMRDeleteStudioSessionMappingRequest,
    ) -> EMRDeleteStudioSessionMappingResponse:
        client = self._require_client()
        return await self._execute(client.delete_studio_session_mapping, request, EMRDeleteStudioSessionMappingResponse)

    async def describe_cluster(
        self,
        request: EMRDescribeClusterRequest,
    ) -> EMRDescribeClusterResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster, request, EMRDescribeClusterResponse)

    async def describe_job_flows(
        self,
        request: EMRDescribeJobFlowsRequest | None = None,
    ) -> EMRDescribeJobFlowsResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_flows, request, EMRDescribeJobFlowsResponse)

    async def describe_notebook_execution(
        self,
        request: EMRDescribeNotebookExecutionRequest,
    ) -> EMRDescribeNotebookExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_notebook_execution, request, EMRDescribeNotebookExecutionResponse)

    async def describe_persistent_app_ui(
        self,
        request: EMRDescribePersistentAppUIRequest,
    ) -> EMRDescribePersistentAppUIResponse:
        client = self._require_client()
        return await self._execute(client.describe_persistent_app_ui, request, EMRDescribePersistentAppUIResponse)

    async def describe_release_label(
        self,
        request: EMRDescribeReleaseLabelRequest | None = None,
    ) -> EMRDescribeReleaseLabelResponse:
        client = self._require_client()
        return await self._execute(client.describe_release_label, request, EMRDescribeReleaseLabelResponse)

    async def describe_security_configuration(
        self,
        request: EMRDescribeSecurityConfigurationRequest,
    ) -> EMRDescribeSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_configuration, request, EMRDescribeSecurityConfigurationResponse)

    async def describe_step(
        self,
        request: EMRDescribeStepRequest,
    ) -> EMRDescribeStepResponse:
        client = self._require_client()
        return await self._execute(client.describe_step, request, EMRDescribeStepResponse)

    async def describe_studio(
        self,
        request: EMRDescribeStudioRequest,
    ) -> EMRDescribeStudioResponse:
        client = self._require_client()
        return await self._execute(client.describe_studio, request, EMRDescribeStudioResponse)

    async def get_auto_termination_policy(
        self,
        request: EMRGetAutoTerminationPolicyRequest,
    ) -> EMRGetAutoTerminationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_auto_termination_policy, request, EMRGetAutoTerminationPolicyResponse)

    async def get_block_public_access_configuration(
        self,
        request: EMRGetBlockPublicAccessConfigurationRequest | None = None,
    ) -> EMRGetBlockPublicAccessConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_block_public_access_configuration, request, EMRGetBlockPublicAccessConfigurationResponse)

    async def get_cluster_session_credentials(
        self,
        request: EMRGetClusterSessionCredentialsRequest,
    ) -> EMRGetClusterSessionCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_cluster_session_credentials, request, EMRGetClusterSessionCredentialsResponse)

    async def get_managed_scaling_policy(
        self,
        request: EMRGetManagedScalingPolicyRequest,
    ) -> EMRGetManagedScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_scaling_policy, request, EMRGetManagedScalingPolicyResponse)

    async def get_on_cluster_app_ui_presigned_url(
        self,
        request: EMRGetOnClusterAppUIPresignedURLRequest,
    ) -> EMRGetOnClusterAppUIPresignedURLResponse:
        client = self._require_client()
        return await self._execute(client.get_on_cluster_app_ui_presigned_url, request, EMRGetOnClusterAppUIPresignedURLResponse)

    async def get_persistent_app_ui_presigned_url(
        self,
        request: EMRGetPersistentAppUIPresignedURLRequest,
    ) -> EMRGetPersistentAppUIPresignedURLResponse:
        client = self._require_client()
        return await self._execute(client.get_persistent_app_ui_presigned_url, request, EMRGetPersistentAppUIPresignedURLResponse)

    async def get_session(
        self,
        request: EMRGetSessionRequest,
    ) -> EMRGetSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_session, request, EMRGetSessionResponse)

    async def get_session_endpoint(
        self,
        request: EMRGetSessionEndpointRequest,
    ) -> EMRGetSessionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_session_endpoint, request, EMRGetSessionEndpointResponse)

    async def get_studio_session_mapping(
        self,
        request: EMRGetStudioSessionMappingRequest,
    ) -> EMRGetStudioSessionMappingResponse:
        client = self._require_client()
        return await self._execute(client.get_studio_session_mapping, request, EMRGetStudioSessionMappingResponse)

    async def list_bootstrap_actions(
        self,
        request: EMRListBootstrapActionsRequest,
    ) -> EMRListBootstrapActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_bootstrap_actions, request, EMRListBootstrapActionsResponse)

    async def list_bootstrap_actions_paginated(
        self,
        request: EMRListBootstrapActionsRequest,
    ) -> list[EMRListBootstrapActionsResponse]:
        return await self._paginate('list_bootstrap_actions', request, EMRListBootstrapActionsResponse)

    async def list_clusters(
        self,
        request: EMRListClustersRequest | None = None,
    ) -> EMRListClustersResponse:
        client = self._require_client()
        return await self._execute(client.list_clusters, request, EMRListClustersResponse)

    async def list_clusters_paginated(
        self,
        request: EMRListClustersRequest | None = None,
    ) -> list[EMRListClustersResponse]:
        return await self._paginate('list_clusters', request, EMRListClustersResponse)

    async def list_instance_fleets(
        self,
        request: EMRListInstanceFleetsRequest,
    ) -> EMRListInstanceFleetsResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_fleets, request, EMRListInstanceFleetsResponse)

    async def list_instance_fleets_paginated(
        self,
        request: EMRListInstanceFleetsRequest,
    ) -> list[EMRListInstanceFleetsResponse]:
        return await self._paginate('list_instance_fleets', request, EMRListInstanceFleetsResponse)

    async def list_instance_groups(
        self,
        request: EMRListInstanceGroupsRequest,
    ) -> EMRListInstanceGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_groups, request, EMRListInstanceGroupsResponse)

    async def list_instance_groups_paginated(
        self,
        request: EMRListInstanceGroupsRequest,
    ) -> list[EMRListInstanceGroupsResponse]:
        return await self._paginate('list_instance_groups', request, EMRListInstanceGroupsResponse)

    async def list_instances(
        self,
        request: EMRListInstancesRequest,
    ) -> EMRListInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_instances, request, EMRListInstancesResponse)

    async def list_instances_paginated(
        self,
        request: EMRListInstancesRequest,
    ) -> list[EMRListInstancesResponse]:
        return await self._paginate('list_instances', request, EMRListInstancesResponse)

    async def list_notebook_executions(
        self,
        request: EMRListNotebookExecutionsRequest | None = None,
    ) -> EMRListNotebookExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_notebook_executions, request, EMRListNotebookExecutionsResponse)

    async def list_notebook_executions_paginated(
        self,
        request: EMRListNotebookExecutionsRequest | None = None,
    ) -> list[EMRListNotebookExecutionsResponse]:
        return await self._paginate('list_notebook_executions', request, EMRListNotebookExecutionsResponse)

    async def list_release_labels(
        self,
        request: EMRListReleaseLabelsRequest | None = None,
    ) -> EMRListReleaseLabelsResponse:
        client = self._require_client()
        return await self._execute(client.list_release_labels, request, EMRListReleaseLabelsResponse)

    async def list_security_configurations(
        self,
        request: EMRListSecurityConfigurationsRequest | None = None,
    ) -> EMRListSecurityConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_configurations, request, EMRListSecurityConfigurationsResponse)

    async def list_security_configurations_paginated(
        self,
        request: EMRListSecurityConfigurationsRequest | None = None,
    ) -> list[EMRListSecurityConfigurationsResponse]:
        return await self._paginate('list_security_configurations', request, EMRListSecurityConfigurationsResponse)

    async def list_sessions(
        self,
        request: EMRListSessionsRequest,
    ) -> EMRListSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_sessions, request, EMRListSessionsResponse)

    async def list_sessions_paginated(
        self,
        request: EMRListSessionsRequest,
    ) -> list[EMRListSessionsResponse]:
        return await self._paginate('list_sessions', request, EMRListSessionsResponse)

    async def list_steps(
        self,
        request: EMRListStepsRequest,
    ) -> EMRListStepsResponse:
        client = self._require_client()
        return await self._execute(client.list_steps, request, EMRListStepsResponse)

    async def list_steps_paginated(
        self,
        request: EMRListStepsRequest,
    ) -> list[EMRListStepsResponse]:
        return await self._paginate('list_steps', request, EMRListStepsResponse)

    async def list_studio_session_mappings(
        self,
        request: EMRListStudioSessionMappingsRequest | None = None,
    ) -> EMRListStudioSessionMappingsResponse:
        client = self._require_client()
        return await self._execute(client.list_studio_session_mappings, request, EMRListStudioSessionMappingsResponse)

    async def list_studio_session_mappings_paginated(
        self,
        request: EMRListStudioSessionMappingsRequest | None = None,
    ) -> list[EMRListStudioSessionMappingsResponse]:
        return await self._paginate('list_studio_session_mappings', request, EMRListStudioSessionMappingsResponse)

    async def list_studios(
        self,
        request: EMRListStudiosRequest | None = None,
    ) -> EMRListStudiosResponse:
        client = self._require_client()
        return await self._execute(client.list_studios, request, EMRListStudiosResponse)

    async def list_studios_paginated(
        self,
        request: EMRListStudiosRequest | None = None,
    ) -> list[EMRListStudiosResponse]:
        return await self._paginate('list_studios', request, EMRListStudiosResponse)

    async def list_supported_instance_types(
        self,
        request: EMRListSupportedInstanceTypesRequest,
    ) -> EMRListSupportedInstanceTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_supported_instance_types, request, EMRListSupportedInstanceTypesResponse)

    async def modify_cluster(
        self,
        request: EMRModifyClusterRequest,
    ) -> EMRModifyClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster, request, EMRModifyClusterResponse)

    async def modify_instance_fleet(
        self,
        request: EMRModifyInstanceFleetRequest,
    ) -> EMRModifyInstanceFleetResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_fleet, request, EMRModifyInstanceFleetResponse)

    async def modify_instance_groups(
        self,
        request: EMRModifyInstanceGroupsRequest | None = None,
    ) -> EMRModifyInstanceGroupsResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_groups, request, EMRModifyInstanceGroupsResponse)

    async def put_auto_scaling_policy(
        self,
        request: EMRPutAutoScalingPolicyRequest,
    ) -> EMRPutAutoScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_auto_scaling_policy, request, EMRPutAutoScalingPolicyResponse)

    async def put_auto_termination_policy(
        self,
        request: EMRPutAutoTerminationPolicyRequest,
    ) -> EMRPutAutoTerminationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_auto_termination_policy, request, EMRPutAutoTerminationPolicyResponse)

    async def put_block_public_access_configuration(
        self,
        request: EMRPutBlockPublicAccessConfigurationRequest,
    ) -> EMRPutBlockPublicAccessConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_block_public_access_configuration, request, EMRPutBlockPublicAccessConfigurationResponse)

    async def put_managed_scaling_policy(
        self,
        request: EMRPutManagedScalingPolicyRequest,
    ) -> EMRPutManagedScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_managed_scaling_policy, request, EMRPutManagedScalingPolicyResponse)

    async def remove_auto_scaling_policy(
        self,
        request: EMRRemoveAutoScalingPolicyRequest,
    ) -> EMRRemoveAutoScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.remove_auto_scaling_policy, request, EMRRemoveAutoScalingPolicyResponse)

    async def remove_auto_termination_policy(
        self,
        request: EMRRemoveAutoTerminationPolicyRequest,
    ) -> EMRRemoveAutoTerminationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.remove_auto_termination_policy, request, EMRRemoveAutoTerminationPolicyResponse)

    async def remove_managed_scaling_policy(
        self,
        request: EMRRemoveManagedScalingPolicyRequest,
    ) -> EMRRemoveManagedScalingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.remove_managed_scaling_policy, request, EMRRemoveManagedScalingPolicyResponse)

    async def remove_tags(
        self,
        request: EMRRemoveTagsRequest,
    ) -> EMRRemoveTagsResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags, request, EMRRemoveTagsResponse)

    async def run_job_flow(
        self,
        request: EMRRunJobFlowRequest,
    ) -> EMRRunJobFlowResponse:
        client = self._require_client()
        return await self._execute(client.run_job_flow, request, EMRRunJobFlowResponse)

    async def set_keep_job_flow_alive_when_no_steps(
        self,
        request: EMRSetKeepJobFlowAliveWhenNoStepsRequest,
    ) -> EMRSetKeepJobFlowAliveWhenNoStepsResponse:
        client = self._require_client()
        return await self._execute(client.set_keep_job_flow_alive_when_no_steps, request, EMRSetKeepJobFlowAliveWhenNoStepsResponse)

    async def set_termination_protection(
        self,
        request: EMRSetTerminationProtectionRequest,
    ) -> EMRSetTerminationProtectionResponse:
        client = self._require_client()
        return await self._execute(client.set_termination_protection, request, EMRSetTerminationProtectionResponse)

    async def set_unhealthy_node_replacement(
        self,
        request: EMRSetUnhealthyNodeReplacementRequest,
    ) -> EMRSetUnhealthyNodeReplacementResponse:
        client = self._require_client()
        return await self._execute(client.set_unhealthy_node_replacement, request, EMRSetUnhealthyNodeReplacementResponse)

    async def set_visible_to_all_users(
        self,
        request: EMRSetVisibleToAllUsersRequest,
    ) -> EMRSetVisibleToAllUsersResponse:
        client = self._require_client()
        return await self._execute(client.set_visible_to_all_users, request, EMRSetVisibleToAllUsersResponse)

    async def start_notebook_execution(
        self,
        request: EMRStartNotebookExecutionRequest,
    ) -> EMRStartNotebookExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_notebook_execution, request, EMRStartNotebookExecutionResponse)

    async def start_session(
        self,
        request: EMRStartSessionRequest,
    ) -> EMRStartSessionResponse:
        client = self._require_client()
        return await self._execute(client.start_session, request, EMRStartSessionResponse)

    async def stop_notebook_execution(
        self,
        request: EMRStopNotebookExecutionRequest,
    ) -> EMRStopNotebookExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_notebook_execution, request, EMRStopNotebookExecutionResponse)

    async def terminate_job_flows(
        self,
        request: EMRTerminateJobFlowsRequest,
    ) -> EMRTerminateJobFlowsResponse:
        client = self._require_client()
        return await self._execute(client.terminate_job_flows, request, EMRTerminateJobFlowsResponse)

    async def terminate_session(
        self,
        request: EMRTerminateSessionRequest,
    ) -> EMRTerminateSessionResponse:
        client = self._require_client()
        return await self._execute(client.terminate_session, request, EMRTerminateSessionResponse)

    async def update_studio(
        self,
        request: EMRUpdateStudioRequest,
    ) -> EMRUpdateStudioResponse:
        client = self._require_client()
        return await self._execute(client.update_studio, request, EMRUpdateStudioResponse)

    async def update_studio_session_mapping(
        self,
        request: EMRUpdateStudioSessionMappingRequest,
    ) -> EMRUpdateStudioSessionMappingResponse:
        client = self._require_client()
        return await self._execute(client.update_studio_session_mapping, request, EMRUpdateStudioSessionMappingResponse)
