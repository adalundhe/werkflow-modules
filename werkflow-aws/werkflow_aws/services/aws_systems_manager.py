from werkflow_aws.models.systems_manager import (
    SSMAddTagsToResourceRequest,
    SSMAddTagsToResourceResponse,
    SSMAssociateOpsItemRelatedItemRequest,
    SSMAssociateOpsItemRelatedItemResponse,
    SSMCancelCommandRequest,
    SSMCancelCommandResponse,
    SSMCancelMaintenanceWindowExecutionRequest,
    SSMCancelMaintenanceWindowExecutionResponse,
    SSMCreateActivationRequest,
    SSMCreateActivationResponse,
    SSMCreateAssociationBatchRequest,
    SSMCreateAssociationBatchResponse,
    SSMCreateAssociationRequest,
    SSMCreateAssociationResponse,
    SSMCreateCloudConnectorRequest,
    SSMCreateCloudConnectorResponse,
    SSMCreateDocumentRequest,
    SSMCreateDocumentResponse,
    SSMCreateMaintenanceWindowRequest,
    SSMCreateMaintenanceWindowResponse,
    SSMCreateOpsItemRequest,
    SSMCreateOpsItemResponse,
    SSMCreateOpsMetadataRequest,
    SSMCreateOpsMetadataResponse,
    SSMCreatePatchBaselineRequest,
    SSMCreatePatchBaselineResponse,
    SSMCreateResourceDataSyncRequest,
    SSMCreateResourceDataSyncResponse,
    SSMDeleteActivationRequest,
    SSMDeleteActivationResponse,
    SSMDeleteAssociationRequest,
    SSMDeleteAssociationResponse,
    SSMDeleteCloudConnectorRequest,
    SSMDeleteCloudConnectorResponse,
    SSMDeleteDocumentRequest,
    SSMDeleteDocumentResponse,
    SSMDeleteInventoryRequest,
    SSMDeleteInventoryResponse,
    SSMDeleteMaintenanceWindowRequest,
    SSMDeleteMaintenanceWindowResponse,
    SSMDeleteOpsItemRequest,
    SSMDeleteOpsItemResponse,
    SSMDeleteOpsMetadataRequest,
    SSMDeleteOpsMetadataResponse,
    SSMDeleteParameterRequest,
    SSMDeleteParameterResponse,
    SSMDeleteParametersRequest,
    SSMDeleteParametersResponse,
    SSMDeletePatchBaselineRequest,
    SSMDeletePatchBaselineResponse,
    SSMDeleteResourceDataSyncRequest,
    SSMDeleteResourceDataSyncResponse,
    SSMDeleteResourcePolicyRequest,
    SSMDeleteResourcePolicyResponse,
    SSMDeregisterDefaultHostManagementConfigurationRequest,
    SSMDeregisterDefaultHostManagementConfigurationResponse,
    SSMDeregisterManagedInstanceRequest,
    SSMDeregisterManagedInstanceResponse,
    SSMDeregisterPatchBaselineForPatchGroupRequest,
    SSMDeregisterPatchBaselineForPatchGroupResponse,
    SSMDeregisterTargetFromMaintenanceWindowRequest,
    SSMDeregisterTargetFromMaintenanceWindowResponse,
    SSMDeregisterTaskFromMaintenanceWindowRequest,
    SSMDeregisterTaskFromMaintenanceWindowResponse,
    SSMDescribeActivationsRequest,
    SSMDescribeActivationsResponse,
    SSMDescribeAssociationExecutionTargetsRequest,
    SSMDescribeAssociationExecutionTargetsResponse,
    SSMDescribeAssociationExecutionsRequest,
    SSMDescribeAssociationExecutionsResponse,
    SSMDescribeAssociationRequest,
    SSMDescribeAssociationResponse,
    SSMDescribeAutomationExecutionsRequest,
    SSMDescribeAutomationExecutionsResponse,
    SSMDescribeAutomationStepExecutionsRequest,
    SSMDescribeAutomationStepExecutionsResponse,
    SSMDescribeAvailablePatchesRequest,
    SSMDescribeAvailablePatchesResponse,
    SSMDescribeDocumentPermissionRequest,
    SSMDescribeDocumentPermissionResponse,
    SSMDescribeDocumentRequest,
    SSMDescribeDocumentResponse,
    SSMDescribeEffectiveInstanceAssociationsRequest,
    SSMDescribeEffectiveInstanceAssociationsResponse,
    SSMDescribeEffectivePatchesForPatchBaselineRequest,
    SSMDescribeEffectivePatchesForPatchBaselineResponse,
    SSMDescribeInstanceAssociationsStatusRequest,
    SSMDescribeInstanceAssociationsStatusResponse,
    SSMDescribeInstanceInformationRequest,
    SSMDescribeInstanceInformationResponse,
    SSMDescribeInstancePatchStatesForPatchGroupRequest,
    SSMDescribeInstancePatchStatesForPatchGroupResponse,
    SSMDescribeInstancePatchStatesRequest,
    SSMDescribeInstancePatchStatesResponse,
    SSMDescribeInstancePatchesRequest,
    SSMDescribeInstancePatchesResponse,
    SSMDescribeInstancePropertiesRequest,
    SSMDescribeInstancePropertiesResponse,
    SSMDescribeInventoryDeletionsRequest,
    SSMDescribeInventoryDeletionsResponse,
    SSMDescribeMaintenanceWindowExecutionTaskInvocationsRequest,
    SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse,
    SSMDescribeMaintenanceWindowExecutionTasksRequest,
    SSMDescribeMaintenanceWindowExecutionTasksResponse,
    SSMDescribeMaintenanceWindowExecutionsRequest,
    SSMDescribeMaintenanceWindowExecutionsResponse,
    SSMDescribeMaintenanceWindowScheduleRequest,
    SSMDescribeMaintenanceWindowScheduleResponse,
    SSMDescribeMaintenanceWindowTargetsRequest,
    SSMDescribeMaintenanceWindowTargetsResponse,
    SSMDescribeMaintenanceWindowTasksRequest,
    SSMDescribeMaintenanceWindowTasksResponse,
    SSMDescribeMaintenanceWindowsForTargetRequest,
    SSMDescribeMaintenanceWindowsForTargetResponse,
    SSMDescribeMaintenanceWindowsRequest,
    SSMDescribeMaintenanceWindowsResponse,
    SSMDescribeOpsItemsRequest,
    SSMDescribeOpsItemsResponse,
    SSMDescribeParametersRequest,
    SSMDescribeParametersResponse,
    SSMDescribePatchBaselinesRequest,
    SSMDescribePatchBaselinesResponse,
    SSMDescribePatchGroupStateRequest,
    SSMDescribePatchGroupStateResponse,
    SSMDescribePatchGroupsRequest,
    SSMDescribePatchGroupsResponse,
    SSMDescribePatchPropertiesRequest,
    SSMDescribePatchPropertiesResponse,
    SSMDescribeSessionsRequest,
    SSMDescribeSessionsResponse,
    SSMDisassociateOpsItemRelatedItemRequest,
    SSMDisassociateOpsItemRelatedItemResponse,
    SSMGetAccessTokenRequest,
    SSMGetAccessTokenResponse,
    SSMGetAutomationExecutionRequest,
    SSMGetAutomationExecutionResponse,
    SSMGetCalendarStateRequest,
    SSMGetCalendarStateResponse,
    SSMGetCloudConnectorRequest,
    SSMGetCloudConnectorResponse,
    SSMGetCommandInvocationRequest,
    SSMGetCommandInvocationResponse,
    SSMGetConnectionStatusRequest,
    SSMGetConnectionStatusResponse,
    SSMGetDefaultPatchBaselineRequest,
    SSMGetDefaultPatchBaselineResponse,
    SSMGetDeployablePatchSnapshotForInstanceRequest,
    SSMGetDeployablePatchSnapshotForInstanceResponse,
    SSMGetDocumentRequest,
    SSMGetDocumentResponse,
    SSMGetExecutionPreviewRequest,
    SSMGetExecutionPreviewResponse,
    SSMGetInventoryRequest,
    SSMGetInventoryResponse,
    SSMGetInventorySchemaRequest,
    SSMGetInventorySchemaResponse,
    SSMGetMaintenanceWindowExecutionRequest,
    SSMGetMaintenanceWindowExecutionResponse,
    SSMGetMaintenanceWindowExecutionTaskInvocationRequest,
    SSMGetMaintenanceWindowExecutionTaskInvocationResponse,
    SSMGetMaintenanceWindowExecutionTaskRequest,
    SSMGetMaintenanceWindowExecutionTaskResponse,
    SSMGetMaintenanceWindowRequest,
    SSMGetMaintenanceWindowResponse,
    SSMGetMaintenanceWindowTaskRequest,
    SSMGetMaintenanceWindowTaskResponse,
    SSMGetOpsItemRequest,
    SSMGetOpsItemResponse,
    SSMGetOpsMetadataRequest,
    SSMGetOpsMetadataResponse,
    SSMGetOpsSummaryRequest,
    SSMGetOpsSummaryResponse,
    SSMGetParameterHistoryRequest,
    SSMGetParameterHistoryResponse,
    SSMGetParameterRequest,
    SSMGetParameterResponse,
    SSMGetParametersByPathRequest,
    SSMGetParametersByPathResponse,
    SSMGetParametersRequest,
    SSMGetParametersResponse,
    SSMGetPatchBaselineForPatchGroupRequest,
    SSMGetPatchBaselineForPatchGroupResponse,
    SSMGetPatchBaselineRequest,
    SSMGetPatchBaselineResponse,
    SSMGetResourcePoliciesRequest,
    SSMGetResourcePoliciesResponse,
    SSMGetServiceSettingRequest,
    SSMGetServiceSettingResponse,
    SSMLabelParameterVersionRequest,
    SSMLabelParameterVersionResponse,
    SSMListAssociationVersionsRequest,
    SSMListAssociationVersionsResponse,
    SSMListAssociationsRequest,
    SSMListAssociationsResponse,
    SSMListCloudConnectorsRequest,
    SSMListCloudConnectorsResponse,
    SSMListCommandInvocationsRequest,
    SSMListCommandInvocationsResponse,
    SSMListCommandsRequest,
    SSMListCommandsResponse,
    SSMListComplianceItemsRequest,
    SSMListComplianceItemsResponse,
    SSMListComplianceSummariesRequest,
    SSMListComplianceSummariesResponse,
    SSMListDocumentMetadataHistoryRequest,
    SSMListDocumentMetadataHistoryResponse,
    SSMListDocumentVersionsRequest,
    SSMListDocumentVersionsResponse,
    SSMListDocumentsRequest,
    SSMListDocumentsResponse,
    SSMListInventoryEntriesRequest,
    SSMListInventoryEntriesResponse,
    SSMListNodesRequest,
    SSMListNodesResponse,
    SSMListNodesSummaryRequest,
    SSMListNodesSummaryResponse,
    SSMListOpsItemEventsRequest,
    SSMListOpsItemEventsResponse,
    SSMListOpsItemRelatedItemsRequest,
    SSMListOpsItemRelatedItemsResponse,
    SSMListOpsMetadataRequest,
    SSMListOpsMetadataResponse,
    SSMListResourceComplianceSummariesRequest,
    SSMListResourceComplianceSummariesResponse,
    SSMListResourceDataSyncRequest,
    SSMListResourceDataSyncResponse,
    SSMListTagsForResourceRequest,
    SSMListTagsForResourceResponse,
    SSMModifyDocumentPermissionRequest,
    SSMModifyDocumentPermissionResponse,
    SSMPutComplianceItemsRequest,
    SSMPutComplianceItemsResponse,
    SSMPutInventoryRequest,
    SSMPutInventoryResponse,
    SSMPutParameterRequest,
    SSMPutParameterResponse,
    SSMPutResourcePolicyRequest,
    SSMPutResourcePolicyResponse,
    SSMRegisterDefaultHostManagementConfigurationRequest,
    SSMRegisterDefaultHostManagementConfigurationResponse,
    SSMRegisterDefaultPatchBaselineRequest,
    SSMRegisterDefaultPatchBaselineResponse,
    SSMRegisterPatchBaselineForPatchGroupRequest,
    SSMRegisterPatchBaselineForPatchGroupResponse,
    SSMRegisterTargetWithMaintenanceWindowRequest,
    SSMRegisterTargetWithMaintenanceWindowResponse,
    SSMRegisterTaskWithMaintenanceWindowRequest,
    SSMRegisterTaskWithMaintenanceWindowResponse,
    SSMRemoveTagsFromResourceRequest,
    SSMRemoveTagsFromResourceResponse,
    SSMResetServiceSettingRequest,
    SSMResetServiceSettingResponse,
    SSMResumeSessionRequest,
    SSMResumeSessionResponse,
    SSMSendAutomationSignalRequest,
    SSMSendAutomationSignalResponse,
    SSMSendCommandRequest,
    SSMSendCommandResponse,
    SSMStartAccessRequestRequest,
    SSMStartAccessRequestResponse,
    SSMStartAssociationsOnceRequest,
    SSMStartAssociationsOnceResponse,
    SSMStartAutomationExecutionRequest,
    SSMStartAutomationExecutionResponse,
    SSMStartChangeRequestExecutionRequest,
    SSMStartChangeRequestExecutionResponse,
    SSMStartExecutionPreviewRequest,
    SSMStartExecutionPreviewResponse,
    SSMStartSessionRequest,
    SSMStartSessionResponse,
    SSMStopAutomationExecutionRequest,
    SSMStopAutomationExecutionResponse,
    SSMTerminateSessionRequest,
    SSMTerminateSessionResponse,
    SSMUnlabelParameterVersionRequest,
    SSMUnlabelParameterVersionResponse,
    SSMUpdateAssociationRequest,
    SSMUpdateAssociationResponse,
    SSMUpdateAssociationStatusRequest,
    SSMUpdateAssociationStatusResponse,
    SSMUpdateCloudConnectorRequest,
    SSMUpdateCloudConnectorResponse,
    SSMUpdateDocumentDefaultVersionRequest,
    SSMUpdateDocumentDefaultVersionResponse,
    SSMUpdateDocumentMetadataRequest,
    SSMUpdateDocumentMetadataResponse,
    SSMUpdateDocumentRequest,
    SSMUpdateDocumentResponse,
    SSMUpdateMaintenanceWindowRequest,
    SSMUpdateMaintenanceWindowResponse,
    SSMUpdateMaintenanceWindowTargetRequest,
    SSMUpdateMaintenanceWindowTargetResponse,
    SSMUpdateMaintenanceWindowTaskRequest,
    SSMUpdateMaintenanceWindowTaskResponse,
    SSMUpdateManagedInstanceRoleRequest,
    SSMUpdateManagedInstanceRoleResponse,
    SSMUpdateOpsItemRequest,
    SSMUpdateOpsItemResponse,
    SSMUpdateOpsMetadataRequest,
    SSMUpdateOpsMetadataResponse,
    SSMUpdatePatchBaselineRequest,
    SSMUpdatePatchBaselineResponse,
    SSMUpdateResourceDataSyncRequest,
    SSMUpdateResourceDataSyncResponse,
    SSMUpdateServiceSettingRequest,
    SSMUpdateServiceSettingResponse,
    SSMValidateCloudConnectorRequest,
    SSMValidateCloudConnectorResponse,
)
from werkflow_aws.types.systems_manager_client import SSMClient
from .base import AWSBaseService


class AWSSSM(AWSBaseService[SSMClient]):
    service_name = 'systems-manager'
    boto3_service_name = 'ssm'

    def __init__(self) -> None:
        super().__init__(service_name='systems-manager', boto3_service_name='ssm')

    async def add_tags_to_resource(
        self,
        request: SSMAddTagsToResourceRequest,
    ) -> SSMAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, SSMAddTagsToResourceResponse)

    async def associate_ops_item_related_item(
        self,
        request: SSMAssociateOpsItemRelatedItemRequest,
    ) -> SSMAssociateOpsItemRelatedItemResponse:
        client = self._require_client()
        return await self._execute(client.associate_ops_item_related_item, request, SSMAssociateOpsItemRelatedItemResponse)

    async def cancel_command(
        self,
        request: SSMCancelCommandRequest,
    ) -> SSMCancelCommandResponse:
        client = self._require_client()
        return await self._execute(client.cancel_command, request, SSMCancelCommandResponse)

    async def cancel_maintenance_window_execution(
        self,
        request: SSMCancelMaintenanceWindowExecutionRequest,
    ) -> SSMCancelMaintenanceWindowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_maintenance_window_execution, request, SSMCancelMaintenanceWindowExecutionResponse)

    async def create_activation(
        self,
        request: SSMCreateActivationRequest,
    ) -> SSMCreateActivationResponse:
        client = self._require_client()
        return await self._execute(client.create_activation, request, SSMCreateActivationResponse)

    async def create_association(
        self,
        request: SSMCreateAssociationRequest,
    ) -> SSMCreateAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_association, request, SSMCreateAssociationResponse)

    async def create_association_batch(
        self,
        request: SSMCreateAssociationBatchRequest,
    ) -> SSMCreateAssociationBatchResponse:
        client = self._require_client()
        return await self._execute(client.create_association_batch, request, SSMCreateAssociationBatchResponse)

    async def create_cloud_connector(
        self,
        request: SSMCreateCloudConnectorRequest,
    ) -> SSMCreateCloudConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_cloud_connector, request, SSMCreateCloudConnectorResponse)

    async def create_document(
        self,
        request: SSMCreateDocumentRequest,
    ) -> SSMCreateDocumentResponse:
        client = self._require_client()
        return await self._execute(client.create_document, request, SSMCreateDocumentResponse)

    async def create_maintenance_window(
        self,
        request: SSMCreateMaintenanceWindowRequest,
    ) -> SSMCreateMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.create_maintenance_window, request, SSMCreateMaintenanceWindowResponse)

    async def create_ops_item(
        self,
        request: SSMCreateOpsItemRequest,
    ) -> SSMCreateOpsItemResponse:
        client = self._require_client()
        return await self._execute(client.create_ops_item, request, SSMCreateOpsItemResponse)

    async def create_ops_metadata(
        self,
        request: SSMCreateOpsMetadataRequest,
    ) -> SSMCreateOpsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.create_ops_metadata, request, SSMCreateOpsMetadataResponse)

    async def create_patch_baseline(
        self,
        request: SSMCreatePatchBaselineRequest,
    ) -> SSMCreatePatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.create_patch_baseline, request, SSMCreatePatchBaselineResponse)

    async def create_resource_data_sync(
        self,
        request: SSMCreateResourceDataSyncRequest,
    ) -> SSMCreateResourceDataSyncResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_data_sync, request, SSMCreateResourceDataSyncResponse)

    async def delete_activation(
        self,
        request: SSMDeleteActivationRequest,
    ) -> SSMDeleteActivationResponse:
        client = self._require_client()
        return await self._execute(client.delete_activation, request, SSMDeleteActivationResponse)

    async def delete_association(
        self,
        request: SSMDeleteAssociationRequest | None = None,
    ) -> SSMDeleteAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_association, request, SSMDeleteAssociationResponse)

    async def delete_cloud_connector(
        self,
        request: SSMDeleteCloudConnectorRequest,
    ) -> SSMDeleteCloudConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_cloud_connector, request, SSMDeleteCloudConnectorResponse)

    async def delete_document(
        self,
        request: SSMDeleteDocumentRequest,
    ) -> SSMDeleteDocumentResponse:
        client = self._require_client()
        return await self._execute(client.delete_document, request, SSMDeleteDocumentResponse)

    async def delete_inventory(
        self,
        request: SSMDeleteInventoryRequest,
    ) -> SSMDeleteInventoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_inventory, request, SSMDeleteInventoryResponse)

    async def delete_maintenance_window(
        self,
        request: SSMDeleteMaintenanceWindowRequest,
    ) -> SSMDeleteMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.delete_maintenance_window, request, SSMDeleteMaintenanceWindowResponse)

    async def delete_ops_item(
        self,
        request: SSMDeleteOpsItemRequest,
    ) -> SSMDeleteOpsItemResponse:
        client = self._require_client()
        return await self._execute(client.delete_ops_item, request, SSMDeleteOpsItemResponse)

    async def delete_ops_metadata(
        self,
        request: SSMDeleteOpsMetadataRequest,
    ) -> SSMDeleteOpsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.delete_ops_metadata, request, SSMDeleteOpsMetadataResponse)

    async def delete_parameter(
        self,
        request: SSMDeleteParameterRequest,
    ) -> SSMDeleteParameterResponse:
        client = self._require_client()
        return await self._execute(client.delete_parameter, request, SSMDeleteParameterResponse)

    async def delete_parameters(
        self,
        request: SSMDeleteParametersRequest,
    ) -> SSMDeleteParametersResponse:
        client = self._require_client()
        return await self._execute(client.delete_parameters, request, SSMDeleteParametersResponse)

    async def delete_patch_baseline(
        self,
        request: SSMDeletePatchBaselineRequest,
    ) -> SSMDeletePatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.delete_patch_baseline, request, SSMDeletePatchBaselineResponse)

    async def delete_resource_data_sync(
        self,
        request: SSMDeleteResourceDataSyncRequest,
    ) -> SSMDeleteResourceDataSyncResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_data_sync, request, SSMDeleteResourceDataSyncResponse)

    async def delete_resource_policy(
        self,
        request: SSMDeleteResourcePolicyRequest,
    ) -> SSMDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, SSMDeleteResourcePolicyResponse)

    async def deregister_default_host_management_configuration(
        self,
        request: SSMDeregisterDefaultHostManagementConfigurationRequest | None = None,
    ) -> SSMDeregisterDefaultHostManagementConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.deregister_default_host_management_configuration, request, SSMDeregisterDefaultHostManagementConfigurationResponse)

    async def deregister_managed_instance(
        self,
        request: SSMDeregisterManagedInstanceRequest,
    ) -> SSMDeregisterManagedInstanceResponse:
        client = self._require_client()
        return await self._execute(client.deregister_managed_instance, request, SSMDeregisterManagedInstanceResponse)

    async def deregister_patch_baseline_for_patch_group(
        self,
        request: SSMDeregisterPatchBaselineForPatchGroupRequest,
    ) -> SSMDeregisterPatchBaselineForPatchGroupResponse:
        client = self._require_client()
        return await self._execute(client.deregister_patch_baseline_for_patch_group, request, SSMDeregisterPatchBaselineForPatchGroupResponse)

    async def deregister_target_from_maintenance_window(
        self,
        request: SSMDeregisterTargetFromMaintenanceWindowRequest,
    ) -> SSMDeregisterTargetFromMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.deregister_target_from_maintenance_window, request, SSMDeregisterTargetFromMaintenanceWindowResponse)

    async def deregister_task_from_maintenance_window(
        self,
        request: SSMDeregisterTaskFromMaintenanceWindowRequest,
    ) -> SSMDeregisterTaskFromMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.deregister_task_from_maintenance_window, request, SSMDeregisterTaskFromMaintenanceWindowResponse)

    async def describe_activations(
        self,
        request: SSMDescribeActivationsRequest | None = None,
    ) -> SSMDescribeActivationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_activations, request, SSMDescribeActivationsResponse)

    async def describe_activations_paginated(
        self,
        request: SSMDescribeActivationsRequest | None = None,
    ) -> list[SSMDescribeActivationsResponse]:
        return await self._paginate('describe_activations', request, SSMDescribeActivationsResponse)

    async def describe_association(
        self,
        request: SSMDescribeAssociationRequest | None = None,
    ) -> SSMDescribeAssociationResponse:
        client = self._require_client()
        return await self._execute(client.describe_association, request, SSMDescribeAssociationResponse)

    async def describe_association_execution_targets(
        self,
        request: SSMDescribeAssociationExecutionTargetsRequest,
    ) -> SSMDescribeAssociationExecutionTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_association_execution_targets, request, SSMDescribeAssociationExecutionTargetsResponse)

    async def describe_association_execution_targets_paginated(
        self,
        request: SSMDescribeAssociationExecutionTargetsRequest,
    ) -> list[SSMDescribeAssociationExecutionTargetsResponse]:
        return await self._paginate('describe_association_execution_targets', request, SSMDescribeAssociationExecutionTargetsResponse)

    async def describe_association_executions(
        self,
        request: SSMDescribeAssociationExecutionsRequest,
    ) -> SSMDescribeAssociationExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_association_executions, request, SSMDescribeAssociationExecutionsResponse)

    async def describe_association_executions_paginated(
        self,
        request: SSMDescribeAssociationExecutionsRequest,
    ) -> list[SSMDescribeAssociationExecutionsResponse]:
        return await self._paginate('describe_association_executions', request, SSMDescribeAssociationExecutionsResponse)

    async def describe_automation_executions(
        self,
        request: SSMDescribeAutomationExecutionsRequest | None = None,
    ) -> SSMDescribeAutomationExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_automation_executions, request, SSMDescribeAutomationExecutionsResponse)

    async def describe_automation_executions_paginated(
        self,
        request: SSMDescribeAutomationExecutionsRequest | None = None,
    ) -> list[SSMDescribeAutomationExecutionsResponse]:
        return await self._paginate('describe_automation_executions', request, SSMDescribeAutomationExecutionsResponse)

    async def describe_automation_step_executions(
        self,
        request: SSMDescribeAutomationStepExecutionsRequest,
    ) -> SSMDescribeAutomationStepExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_automation_step_executions, request, SSMDescribeAutomationStepExecutionsResponse)

    async def describe_automation_step_executions_paginated(
        self,
        request: SSMDescribeAutomationStepExecutionsRequest,
    ) -> list[SSMDescribeAutomationStepExecutionsResponse]:
        return await self._paginate('describe_automation_step_executions', request, SSMDescribeAutomationStepExecutionsResponse)

    async def describe_available_patches(
        self,
        request: SSMDescribeAvailablePatchesRequest | None = None,
    ) -> SSMDescribeAvailablePatchesResponse:
        client = self._require_client()
        return await self._execute(client.describe_available_patches, request, SSMDescribeAvailablePatchesResponse)

    async def describe_available_patches_paginated(
        self,
        request: SSMDescribeAvailablePatchesRequest | None = None,
    ) -> list[SSMDescribeAvailablePatchesResponse]:
        return await self._paginate('describe_available_patches', request, SSMDescribeAvailablePatchesResponse)

    async def describe_document(
        self,
        request: SSMDescribeDocumentRequest,
    ) -> SSMDescribeDocumentResponse:
        client = self._require_client()
        return await self._execute(client.describe_document, request, SSMDescribeDocumentResponse)

    async def describe_document_permission(
        self,
        request: SSMDescribeDocumentPermissionRequest,
    ) -> SSMDescribeDocumentPermissionResponse:
        client = self._require_client()
        return await self._execute(client.describe_document_permission, request, SSMDescribeDocumentPermissionResponse)

    async def describe_effective_instance_associations(
        self,
        request: SSMDescribeEffectiveInstanceAssociationsRequest,
    ) -> SSMDescribeEffectiveInstanceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_effective_instance_associations, request, SSMDescribeEffectiveInstanceAssociationsResponse)

    async def describe_effective_instance_associations_paginated(
        self,
        request: SSMDescribeEffectiveInstanceAssociationsRequest,
    ) -> list[SSMDescribeEffectiveInstanceAssociationsResponse]:
        return await self._paginate('describe_effective_instance_associations', request, SSMDescribeEffectiveInstanceAssociationsResponse)

    async def describe_effective_patches_for_patch_baseline(
        self,
        request: SSMDescribeEffectivePatchesForPatchBaselineRequest,
    ) -> SSMDescribeEffectivePatchesForPatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.describe_effective_patches_for_patch_baseline, request, SSMDescribeEffectivePatchesForPatchBaselineResponse)

    async def describe_effective_patches_for_patch_baseline_paginated(
        self,
        request: SSMDescribeEffectivePatchesForPatchBaselineRequest,
    ) -> list[SSMDescribeEffectivePatchesForPatchBaselineResponse]:
        return await self._paginate('describe_effective_patches_for_patch_baseline', request, SSMDescribeEffectivePatchesForPatchBaselineResponse)

    async def describe_instance_associations_status(
        self,
        request: SSMDescribeInstanceAssociationsStatusRequest,
    ) -> SSMDescribeInstanceAssociationsStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_associations_status, request, SSMDescribeInstanceAssociationsStatusResponse)

    async def describe_instance_associations_status_paginated(
        self,
        request: SSMDescribeInstanceAssociationsStatusRequest,
    ) -> list[SSMDescribeInstanceAssociationsStatusResponse]:
        return await self._paginate('describe_instance_associations_status', request, SSMDescribeInstanceAssociationsStatusResponse)

    async def describe_instance_information(
        self,
        request: SSMDescribeInstanceInformationRequest | None = None,
    ) -> SSMDescribeInstanceInformationResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_information, request, SSMDescribeInstanceInformationResponse)

    async def describe_instance_information_paginated(
        self,
        request: SSMDescribeInstanceInformationRequest | None = None,
    ) -> list[SSMDescribeInstanceInformationResponse]:
        return await self._paginate('describe_instance_information', request, SSMDescribeInstanceInformationResponse)

    async def describe_instance_patch_states(
        self,
        request: SSMDescribeInstancePatchStatesRequest,
    ) -> SSMDescribeInstancePatchStatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_patch_states, request, SSMDescribeInstancePatchStatesResponse)

    async def describe_instance_patch_states_paginated(
        self,
        request: SSMDescribeInstancePatchStatesRequest,
    ) -> list[SSMDescribeInstancePatchStatesResponse]:
        return await self._paginate('describe_instance_patch_states', request, SSMDescribeInstancePatchStatesResponse)

    async def describe_instance_patch_states_for_patch_group(
        self,
        request: SSMDescribeInstancePatchStatesForPatchGroupRequest,
    ) -> SSMDescribeInstancePatchStatesForPatchGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_patch_states_for_patch_group, request, SSMDescribeInstancePatchStatesForPatchGroupResponse)

    async def describe_instance_patch_states_for_patch_group_paginated(
        self,
        request: SSMDescribeInstancePatchStatesForPatchGroupRequest,
    ) -> list[SSMDescribeInstancePatchStatesForPatchGroupResponse]:
        return await self._paginate('describe_instance_patch_states_for_patch_group', request, SSMDescribeInstancePatchStatesForPatchGroupResponse)

    async def describe_instance_patches(
        self,
        request: SSMDescribeInstancePatchesRequest,
    ) -> SSMDescribeInstancePatchesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_patches, request, SSMDescribeInstancePatchesResponse)

    async def describe_instance_patches_paginated(
        self,
        request: SSMDescribeInstancePatchesRequest,
    ) -> list[SSMDescribeInstancePatchesResponse]:
        return await self._paginate('describe_instance_patches', request, SSMDescribeInstancePatchesResponse)

    async def describe_instance_properties(
        self,
        request: SSMDescribeInstancePropertiesRequest | None = None,
    ) -> SSMDescribeInstancePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_properties, request, SSMDescribeInstancePropertiesResponse)

    async def describe_instance_properties_paginated(
        self,
        request: SSMDescribeInstancePropertiesRequest | None = None,
    ) -> list[SSMDescribeInstancePropertiesResponse]:
        return await self._paginate('describe_instance_properties', request, SSMDescribeInstancePropertiesResponse)

    async def describe_inventory_deletions(
        self,
        request: SSMDescribeInventoryDeletionsRequest | None = None,
    ) -> SSMDescribeInventoryDeletionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_inventory_deletions, request, SSMDescribeInventoryDeletionsResponse)

    async def describe_inventory_deletions_paginated(
        self,
        request: SSMDescribeInventoryDeletionsRequest | None = None,
    ) -> list[SSMDescribeInventoryDeletionsResponse]:
        return await self._paginate('describe_inventory_deletions', request, SSMDescribeInventoryDeletionsResponse)

    async def describe_maintenance_window_execution_task_invocations(
        self,
        request: SSMDescribeMaintenanceWindowExecutionTaskInvocationsRequest,
    ) -> SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_execution_task_invocations, request, SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse)

    async def describe_maintenance_window_execution_task_invocations_paginated(
        self,
        request: SSMDescribeMaintenanceWindowExecutionTaskInvocationsRequest,
    ) -> list[SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse]:
        return await self._paginate('describe_maintenance_window_execution_task_invocations', request, SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse)

    async def describe_maintenance_window_execution_tasks(
        self,
        request: SSMDescribeMaintenanceWindowExecutionTasksRequest,
    ) -> SSMDescribeMaintenanceWindowExecutionTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_execution_tasks, request, SSMDescribeMaintenanceWindowExecutionTasksResponse)

    async def describe_maintenance_window_execution_tasks_paginated(
        self,
        request: SSMDescribeMaintenanceWindowExecutionTasksRequest,
    ) -> list[SSMDescribeMaintenanceWindowExecutionTasksResponse]:
        return await self._paginate('describe_maintenance_window_execution_tasks', request, SSMDescribeMaintenanceWindowExecutionTasksResponse)

    async def describe_maintenance_window_executions(
        self,
        request: SSMDescribeMaintenanceWindowExecutionsRequest,
    ) -> SSMDescribeMaintenanceWindowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_executions, request, SSMDescribeMaintenanceWindowExecutionsResponse)

    async def describe_maintenance_window_executions_paginated(
        self,
        request: SSMDescribeMaintenanceWindowExecutionsRequest,
    ) -> list[SSMDescribeMaintenanceWindowExecutionsResponse]:
        return await self._paginate('describe_maintenance_window_executions', request, SSMDescribeMaintenanceWindowExecutionsResponse)

    async def describe_maintenance_window_schedule(
        self,
        request: SSMDescribeMaintenanceWindowScheduleRequest | None = None,
    ) -> SSMDescribeMaintenanceWindowScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_schedule, request, SSMDescribeMaintenanceWindowScheduleResponse)

    async def describe_maintenance_window_schedule_paginated(
        self,
        request: SSMDescribeMaintenanceWindowScheduleRequest | None = None,
    ) -> list[SSMDescribeMaintenanceWindowScheduleResponse]:
        return await self._paginate('describe_maintenance_window_schedule', request, SSMDescribeMaintenanceWindowScheduleResponse)

    async def describe_maintenance_window_targets(
        self,
        request: SSMDescribeMaintenanceWindowTargetsRequest,
    ) -> SSMDescribeMaintenanceWindowTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_targets, request, SSMDescribeMaintenanceWindowTargetsResponse)

    async def describe_maintenance_window_targets_paginated(
        self,
        request: SSMDescribeMaintenanceWindowTargetsRequest,
    ) -> list[SSMDescribeMaintenanceWindowTargetsResponse]:
        return await self._paginate('describe_maintenance_window_targets', request, SSMDescribeMaintenanceWindowTargetsResponse)

    async def describe_maintenance_window_tasks(
        self,
        request: SSMDescribeMaintenanceWindowTasksRequest,
    ) -> SSMDescribeMaintenanceWindowTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_window_tasks, request, SSMDescribeMaintenanceWindowTasksResponse)

    async def describe_maintenance_window_tasks_paginated(
        self,
        request: SSMDescribeMaintenanceWindowTasksRequest,
    ) -> list[SSMDescribeMaintenanceWindowTasksResponse]:
        return await self._paginate('describe_maintenance_window_tasks', request, SSMDescribeMaintenanceWindowTasksResponse)

    async def describe_maintenance_windows(
        self,
        request: SSMDescribeMaintenanceWindowsRequest | None = None,
    ) -> SSMDescribeMaintenanceWindowsResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_windows, request, SSMDescribeMaintenanceWindowsResponse)

    async def describe_maintenance_windows_paginated(
        self,
        request: SSMDescribeMaintenanceWindowsRequest | None = None,
    ) -> list[SSMDescribeMaintenanceWindowsResponse]:
        return await self._paginate('describe_maintenance_windows', request, SSMDescribeMaintenanceWindowsResponse)

    async def describe_maintenance_windows_for_target(
        self,
        request: SSMDescribeMaintenanceWindowsForTargetRequest,
    ) -> SSMDescribeMaintenanceWindowsForTargetResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_windows_for_target, request, SSMDescribeMaintenanceWindowsForTargetResponse)

    async def describe_maintenance_windows_for_target_paginated(
        self,
        request: SSMDescribeMaintenanceWindowsForTargetRequest,
    ) -> list[SSMDescribeMaintenanceWindowsForTargetResponse]:
        return await self._paginate('describe_maintenance_windows_for_target', request, SSMDescribeMaintenanceWindowsForTargetResponse)

    async def describe_ops_items(
        self,
        request: SSMDescribeOpsItemsRequest | None = None,
    ) -> SSMDescribeOpsItemsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ops_items, request, SSMDescribeOpsItemsResponse)

    async def describe_ops_items_paginated(
        self,
        request: SSMDescribeOpsItemsRequest | None = None,
    ) -> list[SSMDescribeOpsItemsResponse]:
        return await self._paginate('describe_ops_items', request, SSMDescribeOpsItemsResponse)

    async def describe_parameters(
        self,
        request: SSMDescribeParametersRequest | None = None,
    ) -> SSMDescribeParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_parameters, request, SSMDescribeParametersResponse)

    async def describe_parameters_paginated(
        self,
        request: SSMDescribeParametersRequest | None = None,
    ) -> list[SSMDescribeParametersResponse]:
        return await self._paginate('describe_parameters', request, SSMDescribeParametersResponse)

    async def describe_patch_baselines(
        self,
        request: SSMDescribePatchBaselinesRequest | None = None,
    ) -> SSMDescribePatchBaselinesResponse:
        client = self._require_client()
        return await self._execute(client.describe_patch_baselines, request, SSMDescribePatchBaselinesResponse)

    async def describe_patch_baselines_paginated(
        self,
        request: SSMDescribePatchBaselinesRequest | None = None,
    ) -> list[SSMDescribePatchBaselinesResponse]:
        return await self._paginate('describe_patch_baselines', request, SSMDescribePatchBaselinesResponse)

    async def describe_patch_group_state(
        self,
        request: SSMDescribePatchGroupStateRequest,
    ) -> SSMDescribePatchGroupStateResponse:
        client = self._require_client()
        return await self._execute(client.describe_patch_group_state, request, SSMDescribePatchGroupStateResponse)

    async def describe_patch_groups(
        self,
        request: SSMDescribePatchGroupsRequest | None = None,
    ) -> SSMDescribePatchGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_patch_groups, request, SSMDescribePatchGroupsResponse)

    async def describe_patch_groups_paginated(
        self,
        request: SSMDescribePatchGroupsRequest | None = None,
    ) -> list[SSMDescribePatchGroupsResponse]:
        return await self._paginate('describe_patch_groups', request, SSMDescribePatchGroupsResponse)

    async def describe_patch_properties(
        self,
        request: SSMDescribePatchPropertiesRequest,
    ) -> SSMDescribePatchPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_patch_properties, request, SSMDescribePatchPropertiesResponse)

    async def describe_patch_properties_paginated(
        self,
        request: SSMDescribePatchPropertiesRequest,
    ) -> list[SSMDescribePatchPropertiesResponse]:
        return await self._paginate('describe_patch_properties', request, SSMDescribePatchPropertiesResponse)

    async def describe_sessions(
        self,
        request: SSMDescribeSessionsRequest,
    ) -> SSMDescribeSessionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_sessions, request, SSMDescribeSessionsResponse)

    async def describe_sessions_paginated(
        self,
        request: SSMDescribeSessionsRequest,
    ) -> list[SSMDescribeSessionsResponse]:
        return await self._paginate('describe_sessions', request, SSMDescribeSessionsResponse)

    async def disassociate_ops_item_related_item(
        self,
        request: SSMDisassociateOpsItemRelatedItemRequest,
    ) -> SSMDisassociateOpsItemRelatedItemResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_ops_item_related_item, request, SSMDisassociateOpsItemRelatedItemResponse)

    async def get_access_token(
        self,
        request: SSMGetAccessTokenRequest,
    ) -> SSMGetAccessTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_access_token, request, SSMGetAccessTokenResponse)

    async def get_automation_execution(
        self,
        request: SSMGetAutomationExecutionRequest,
    ) -> SSMGetAutomationExecutionResponse:
        client = self._require_client()
        return await self._execute(client.get_automation_execution, request, SSMGetAutomationExecutionResponse)

    async def get_calendar_state(
        self,
        request: SSMGetCalendarStateRequest,
    ) -> SSMGetCalendarStateResponse:
        client = self._require_client()
        return await self._execute(client.get_calendar_state, request, SSMGetCalendarStateResponse)

    async def get_cloud_connector(
        self,
        request: SSMGetCloudConnectorRequest,
    ) -> SSMGetCloudConnectorResponse:
        client = self._require_client()
        return await self._execute(client.get_cloud_connector, request, SSMGetCloudConnectorResponse)

    async def get_command_invocation(
        self,
        request: SSMGetCommandInvocationRequest,
    ) -> SSMGetCommandInvocationResponse:
        client = self._require_client()
        return await self._execute(client.get_command_invocation, request, SSMGetCommandInvocationResponse)

    async def get_connection_status(
        self,
        request: SSMGetConnectionStatusRequest,
    ) -> SSMGetConnectionStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_connection_status, request, SSMGetConnectionStatusResponse)

    async def get_default_patch_baseline(
        self,
        request: SSMGetDefaultPatchBaselineRequest | None = None,
    ) -> SSMGetDefaultPatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.get_default_patch_baseline, request, SSMGetDefaultPatchBaselineResponse)

    async def get_deployable_patch_snapshot_for_instance(
        self,
        request: SSMGetDeployablePatchSnapshotForInstanceRequest,
    ) -> SSMGetDeployablePatchSnapshotForInstanceResponse:
        client = self._require_client()
        return await self._execute(client.get_deployable_patch_snapshot_for_instance, request, SSMGetDeployablePatchSnapshotForInstanceResponse)

    async def get_document(
        self,
        request: SSMGetDocumentRequest,
    ) -> SSMGetDocumentResponse:
        client = self._require_client()
        return await self._execute(client.get_document, request, SSMGetDocumentResponse)

    async def get_execution_preview(
        self,
        request: SSMGetExecutionPreviewRequest,
    ) -> SSMGetExecutionPreviewResponse:
        client = self._require_client()
        return await self._execute(client.get_execution_preview, request, SSMGetExecutionPreviewResponse)

    async def get_inventory(
        self,
        request: SSMGetInventoryRequest | None = None,
    ) -> SSMGetInventoryResponse:
        client = self._require_client()
        return await self._execute(client.get_inventory, request, SSMGetInventoryResponse)

    async def get_inventory_paginated(
        self,
        request: SSMGetInventoryRequest | None = None,
    ) -> list[SSMGetInventoryResponse]:
        return await self._paginate('get_inventory', request, SSMGetInventoryResponse)

    async def get_inventory_schema(
        self,
        request: SSMGetInventorySchemaRequest | None = None,
    ) -> SSMGetInventorySchemaResponse:
        client = self._require_client()
        return await self._execute(client.get_inventory_schema, request, SSMGetInventorySchemaResponse)

    async def get_inventory_schema_paginated(
        self,
        request: SSMGetInventorySchemaRequest | None = None,
    ) -> list[SSMGetInventorySchemaResponse]:
        return await self._paginate('get_inventory_schema', request, SSMGetInventorySchemaResponse)

    async def get_maintenance_window(
        self,
        request: SSMGetMaintenanceWindowRequest,
    ) -> SSMGetMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.get_maintenance_window, request, SSMGetMaintenanceWindowResponse)

    async def get_maintenance_window_execution(
        self,
        request: SSMGetMaintenanceWindowExecutionRequest,
    ) -> SSMGetMaintenanceWindowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.get_maintenance_window_execution, request, SSMGetMaintenanceWindowExecutionResponse)

    async def get_maintenance_window_execution_task(
        self,
        request: SSMGetMaintenanceWindowExecutionTaskRequest,
    ) -> SSMGetMaintenanceWindowExecutionTaskResponse:
        client = self._require_client()
        return await self._execute(client.get_maintenance_window_execution_task, request, SSMGetMaintenanceWindowExecutionTaskResponse)

    async def get_maintenance_window_execution_task_invocation(
        self,
        request: SSMGetMaintenanceWindowExecutionTaskInvocationRequest,
    ) -> SSMGetMaintenanceWindowExecutionTaskInvocationResponse:
        client = self._require_client()
        return await self._execute(client.get_maintenance_window_execution_task_invocation, request, SSMGetMaintenanceWindowExecutionTaskInvocationResponse)

    async def get_maintenance_window_task(
        self,
        request: SSMGetMaintenanceWindowTaskRequest,
    ) -> SSMGetMaintenanceWindowTaskResponse:
        client = self._require_client()
        return await self._execute(client.get_maintenance_window_task, request, SSMGetMaintenanceWindowTaskResponse)

    async def get_ops_item(
        self,
        request: SSMGetOpsItemRequest,
    ) -> SSMGetOpsItemResponse:
        client = self._require_client()
        return await self._execute(client.get_ops_item, request, SSMGetOpsItemResponse)

    async def get_ops_metadata(
        self,
        request: SSMGetOpsMetadataRequest,
    ) -> SSMGetOpsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_ops_metadata, request, SSMGetOpsMetadataResponse)

    async def get_ops_summary(
        self,
        request: SSMGetOpsSummaryRequest | None = None,
    ) -> SSMGetOpsSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_ops_summary, request, SSMGetOpsSummaryResponse)

    async def get_ops_summary_paginated(
        self,
        request: SSMGetOpsSummaryRequest | None = None,
    ) -> list[SSMGetOpsSummaryResponse]:
        return await self._paginate('get_ops_summary', request, SSMGetOpsSummaryResponse)

    async def get_parameter(
        self,
        request: SSMGetParameterRequest,
    ) -> SSMGetParameterResponse:
        client = self._require_client()
        return await self._execute(client.get_parameter, request, SSMGetParameterResponse)

    async def get_parameter_history(
        self,
        request: SSMGetParameterHistoryRequest,
    ) -> SSMGetParameterHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_parameter_history, request, SSMGetParameterHistoryResponse)

    async def get_parameter_history_paginated(
        self,
        request: SSMGetParameterHistoryRequest,
    ) -> list[SSMGetParameterHistoryResponse]:
        return await self._paginate('get_parameter_history', request, SSMGetParameterHistoryResponse)

    async def get_parameters(
        self,
        request: SSMGetParametersRequest,
    ) -> SSMGetParametersResponse:
        client = self._require_client()
        return await self._execute(client.get_parameters, request, SSMGetParametersResponse)

    async def get_parameters_by_path(
        self,
        request: SSMGetParametersByPathRequest,
    ) -> SSMGetParametersByPathResponse:
        client = self._require_client()
        return await self._execute(client.get_parameters_by_path, request, SSMGetParametersByPathResponse)

    async def get_parameters_by_path_paginated(
        self,
        request: SSMGetParametersByPathRequest,
    ) -> list[SSMGetParametersByPathResponse]:
        return await self._paginate('get_parameters_by_path', request, SSMGetParametersByPathResponse)

    async def get_patch_baseline(
        self,
        request: SSMGetPatchBaselineRequest,
    ) -> SSMGetPatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.get_patch_baseline, request, SSMGetPatchBaselineResponse)

    async def get_patch_baseline_for_patch_group(
        self,
        request: SSMGetPatchBaselineForPatchGroupRequest,
    ) -> SSMGetPatchBaselineForPatchGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_patch_baseline_for_patch_group, request, SSMGetPatchBaselineForPatchGroupResponse)

    async def get_resource_policies(
        self,
        request: SSMGetResourcePoliciesRequest,
    ) -> SSMGetResourcePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policies, request, SSMGetResourcePoliciesResponse)

    async def get_resource_policies_paginated(
        self,
        request: SSMGetResourcePoliciesRequest,
    ) -> list[SSMGetResourcePoliciesResponse]:
        return await self._paginate('get_resource_policies', request, SSMGetResourcePoliciesResponse)

    async def get_service_setting(
        self,
        request: SSMGetServiceSettingRequest,
    ) -> SSMGetServiceSettingResponse:
        client = self._require_client()
        return await self._execute(client.get_service_setting, request, SSMGetServiceSettingResponse)

    async def label_parameter_version(
        self,
        request: SSMLabelParameterVersionRequest,
    ) -> SSMLabelParameterVersionResponse:
        client = self._require_client()
        return await self._execute(client.label_parameter_version, request, SSMLabelParameterVersionResponse)

    async def list_association_versions(
        self,
        request: SSMListAssociationVersionsRequest,
    ) -> SSMListAssociationVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_association_versions, request, SSMListAssociationVersionsResponse)

    async def list_association_versions_paginated(
        self,
        request: SSMListAssociationVersionsRequest,
    ) -> list[SSMListAssociationVersionsResponse]:
        return await self._paginate('list_association_versions', request, SSMListAssociationVersionsResponse)

    async def list_associations(
        self,
        request: SSMListAssociationsRequest | None = None,
    ) -> SSMListAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_associations, request, SSMListAssociationsResponse)

    async def list_associations_paginated(
        self,
        request: SSMListAssociationsRequest | None = None,
    ) -> list[SSMListAssociationsResponse]:
        return await self._paginate('list_associations', request, SSMListAssociationsResponse)

    async def list_cloud_connectors(
        self,
        request: SSMListCloudConnectorsRequest | None = None,
    ) -> SSMListCloudConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_cloud_connectors, request, SSMListCloudConnectorsResponse)

    async def list_cloud_connectors_paginated(
        self,
        request: SSMListCloudConnectorsRequest | None = None,
    ) -> list[SSMListCloudConnectorsResponse]:
        return await self._paginate('list_cloud_connectors', request, SSMListCloudConnectorsResponse)

    async def list_command_invocations(
        self,
        request: SSMListCommandInvocationsRequest | None = None,
    ) -> SSMListCommandInvocationsResponse:
        client = self._require_client()
        return await self._execute(client.list_command_invocations, request, SSMListCommandInvocationsResponse)

    async def list_command_invocations_paginated(
        self,
        request: SSMListCommandInvocationsRequest | None = None,
    ) -> list[SSMListCommandInvocationsResponse]:
        return await self._paginate('list_command_invocations', request, SSMListCommandInvocationsResponse)

    async def list_commands(
        self,
        request: SSMListCommandsRequest | None = None,
    ) -> SSMListCommandsResponse:
        client = self._require_client()
        return await self._execute(client.list_commands, request, SSMListCommandsResponse)

    async def list_commands_paginated(
        self,
        request: SSMListCommandsRequest | None = None,
    ) -> list[SSMListCommandsResponse]:
        return await self._paginate('list_commands', request, SSMListCommandsResponse)

    async def list_compliance_items(
        self,
        request: SSMListComplianceItemsRequest | None = None,
    ) -> SSMListComplianceItemsResponse:
        client = self._require_client()
        return await self._execute(client.list_compliance_items, request, SSMListComplianceItemsResponse)

    async def list_compliance_items_paginated(
        self,
        request: SSMListComplianceItemsRequest | None = None,
    ) -> list[SSMListComplianceItemsResponse]:
        return await self._paginate('list_compliance_items', request, SSMListComplianceItemsResponse)

    async def list_compliance_summaries(
        self,
        request: SSMListComplianceSummariesRequest | None = None,
    ) -> SSMListComplianceSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_compliance_summaries, request, SSMListComplianceSummariesResponse)

    async def list_compliance_summaries_paginated(
        self,
        request: SSMListComplianceSummariesRequest | None = None,
    ) -> list[SSMListComplianceSummariesResponse]:
        return await self._paginate('list_compliance_summaries', request, SSMListComplianceSummariesResponse)

    async def list_document_metadata_history(
        self,
        request: SSMListDocumentMetadataHistoryRequest,
    ) -> SSMListDocumentMetadataHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_document_metadata_history, request, SSMListDocumentMetadataHistoryResponse)

    async def list_document_versions(
        self,
        request: SSMListDocumentVersionsRequest,
    ) -> SSMListDocumentVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_document_versions, request, SSMListDocumentVersionsResponse)

    async def list_document_versions_paginated(
        self,
        request: SSMListDocumentVersionsRequest,
    ) -> list[SSMListDocumentVersionsResponse]:
        return await self._paginate('list_document_versions', request, SSMListDocumentVersionsResponse)

    async def list_documents(
        self,
        request: SSMListDocumentsRequest | None = None,
    ) -> SSMListDocumentsResponse:
        client = self._require_client()
        return await self._execute(client.list_documents, request, SSMListDocumentsResponse)

    async def list_documents_paginated(
        self,
        request: SSMListDocumentsRequest | None = None,
    ) -> list[SSMListDocumentsResponse]:
        return await self._paginate('list_documents', request, SSMListDocumentsResponse)

    async def list_inventory_entries(
        self,
        request: SSMListInventoryEntriesRequest,
    ) -> SSMListInventoryEntriesResponse:
        client = self._require_client()
        return await self._execute(client.list_inventory_entries, request, SSMListInventoryEntriesResponse)

    async def list_nodes(
        self,
        request: SSMListNodesRequest | None = None,
    ) -> SSMListNodesResponse:
        client = self._require_client()
        return await self._execute(client.list_nodes, request, SSMListNodesResponse)

    async def list_nodes_paginated(
        self,
        request: SSMListNodesRequest | None = None,
    ) -> list[SSMListNodesResponse]:
        return await self._paginate('list_nodes', request, SSMListNodesResponse)

    async def list_nodes_summary(
        self,
        request: SSMListNodesSummaryRequest,
    ) -> SSMListNodesSummaryResponse:
        client = self._require_client()
        return await self._execute(client.list_nodes_summary, request, SSMListNodesSummaryResponse)

    async def list_nodes_summary_paginated(
        self,
        request: SSMListNodesSummaryRequest,
    ) -> list[SSMListNodesSummaryResponse]:
        return await self._paginate('list_nodes_summary', request, SSMListNodesSummaryResponse)

    async def list_ops_item_events(
        self,
        request: SSMListOpsItemEventsRequest | None = None,
    ) -> SSMListOpsItemEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_ops_item_events, request, SSMListOpsItemEventsResponse)

    async def list_ops_item_events_paginated(
        self,
        request: SSMListOpsItemEventsRequest | None = None,
    ) -> list[SSMListOpsItemEventsResponse]:
        return await self._paginate('list_ops_item_events', request, SSMListOpsItemEventsResponse)

    async def list_ops_item_related_items(
        self,
        request: SSMListOpsItemRelatedItemsRequest | None = None,
    ) -> SSMListOpsItemRelatedItemsResponse:
        client = self._require_client()
        return await self._execute(client.list_ops_item_related_items, request, SSMListOpsItemRelatedItemsResponse)

    async def list_ops_item_related_items_paginated(
        self,
        request: SSMListOpsItemRelatedItemsRequest | None = None,
    ) -> list[SSMListOpsItemRelatedItemsResponse]:
        return await self._paginate('list_ops_item_related_items', request, SSMListOpsItemRelatedItemsResponse)

    async def list_ops_metadata(
        self,
        request: SSMListOpsMetadataRequest | None = None,
    ) -> SSMListOpsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.list_ops_metadata, request, SSMListOpsMetadataResponse)

    async def list_ops_metadata_paginated(
        self,
        request: SSMListOpsMetadataRequest | None = None,
    ) -> list[SSMListOpsMetadataResponse]:
        return await self._paginate('list_ops_metadata', request, SSMListOpsMetadataResponse)

    async def list_resource_compliance_summaries(
        self,
        request: SSMListResourceComplianceSummariesRequest | None = None,
    ) -> SSMListResourceComplianceSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_compliance_summaries, request, SSMListResourceComplianceSummariesResponse)

    async def list_resource_compliance_summaries_paginated(
        self,
        request: SSMListResourceComplianceSummariesRequest | None = None,
    ) -> list[SSMListResourceComplianceSummariesResponse]:
        return await self._paginate('list_resource_compliance_summaries', request, SSMListResourceComplianceSummariesResponse)

    async def list_resource_data_sync(
        self,
        request: SSMListResourceDataSyncRequest | None = None,
    ) -> SSMListResourceDataSyncResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_data_sync, request, SSMListResourceDataSyncResponse)

    async def list_resource_data_sync_paginated(
        self,
        request: SSMListResourceDataSyncRequest | None = None,
    ) -> list[SSMListResourceDataSyncResponse]:
        return await self._paginate('list_resource_data_sync', request, SSMListResourceDataSyncResponse)

    async def list_tags_for_resource(
        self,
        request: SSMListTagsForResourceRequest,
    ) -> SSMListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SSMListTagsForResourceResponse)

    async def modify_document_permission(
        self,
        request: SSMModifyDocumentPermissionRequest,
    ) -> SSMModifyDocumentPermissionResponse:
        client = self._require_client()
        return await self._execute(client.modify_document_permission, request, SSMModifyDocumentPermissionResponse)

    async def put_compliance_items(
        self,
        request: SSMPutComplianceItemsRequest,
    ) -> SSMPutComplianceItemsResponse:
        client = self._require_client()
        return await self._execute(client.put_compliance_items, request, SSMPutComplianceItemsResponse)

    async def put_inventory(
        self,
        request: SSMPutInventoryRequest,
    ) -> SSMPutInventoryResponse:
        client = self._require_client()
        return await self._execute(client.put_inventory, request, SSMPutInventoryResponse)

    async def put_parameter(
        self,
        request: SSMPutParameterRequest,
    ) -> SSMPutParameterResponse:
        client = self._require_client()
        return await self._execute(client.put_parameter, request, SSMPutParameterResponse)

    async def put_resource_policy(
        self,
        request: SSMPutResourcePolicyRequest,
    ) -> SSMPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, SSMPutResourcePolicyResponse)

    async def register_default_host_management_configuration(
        self,
        request: SSMRegisterDefaultHostManagementConfigurationRequest,
    ) -> SSMRegisterDefaultHostManagementConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.register_default_host_management_configuration, request, SSMRegisterDefaultHostManagementConfigurationResponse)

    async def register_default_patch_baseline(
        self,
        request: SSMRegisterDefaultPatchBaselineRequest,
    ) -> SSMRegisterDefaultPatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.register_default_patch_baseline, request, SSMRegisterDefaultPatchBaselineResponse)

    async def register_patch_baseline_for_patch_group(
        self,
        request: SSMRegisterPatchBaselineForPatchGroupRequest,
    ) -> SSMRegisterPatchBaselineForPatchGroupResponse:
        client = self._require_client()
        return await self._execute(client.register_patch_baseline_for_patch_group, request, SSMRegisterPatchBaselineForPatchGroupResponse)

    async def register_target_with_maintenance_window(
        self,
        request: SSMRegisterTargetWithMaintenanceWindowRequest,
    ) -> SSMRegisterTargetWithMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.register_target_with_maintenance_window, request, SSMRegisterTargetWithMaintenanceWindowResponse)

    async def register_task_with_maintenance_window(
        self,
        request: SSMRegisterTaskWithMaintenanceWindowRequest,
    ) -> SSMRegisterTaskWithMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.register_task_with_maintenance_window, request, SSMRegisterTaskWithMaintenanceWindowResponse)

    async def remove_tags_from_resource(
        self,
        request: SSMRemoveTagsFromResourceRequest,
    ) -> SSMRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, SSMRemoveTagsFromResourceResponse)

    async def reset_service_setting(
        self,
        request: SSMResetServiceSettingRequest,
    ) -> SSMResetServiceSettingResponse:
        client = self._require_client()
        return await self._execute(client.reset_service_setting, request, SSMResetServiceSettingResponse)

    async def resume_session(
        self,
        request: SSMResumeSessionRequest,
    ) -> SSMResumeSessionResponse:
        client = self._require_client()
        return await self._execute(client.resume_session, request, SSMResumeSessionResponse)

    async def send_automation_signal(
        self,
        request: SSMSendAutomationSignalRequest,
    ) -> SSMSendAutomationSignalResponse:
        client = self._require_client()
        return await self._execute(client.send_automation_signal, request, SSMSendAutomationSignalResponse)

    async def send_command(
        self,
        request: SSMSendCommandRequest,
    ) -> SSMSendCommandResponse:
        client = self._require_client()
        return await self._execute(client.send_command, request, SSMSendCommandResponse)

    async def start_access_request(
        self,
        request: SSMStartAccessRequestRequest,
    ) -> SSMStartAccessRequestResponse:
        client = self._require_client()
        return await self._execute(client.start_access_request, request, SSMStartAccessRequestResponse)

    async def start_associations_once(
        self,
        request: SSMStartAssociationsOnceRequest,
    ) -> SSMStartAssociationsOnceResponse:
        client = self._require_client()
        return await self._execute(client.start_associations_once, request, SSMStartAssociationsOnceResponse)

    async def start_automation_execution(
        self,
        request: SSMStartAutomationExecutionRequest,
    ) -> SSMStartAutomationExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_automation_execution, request, SSMStartAutomationExecutionResponse)

    async def start_change_request_execution(
        self,
        request: SSMStartChangeRequestExecutionRequest,
    ) -> SSMStartChangeRequestExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_change_request_execution, request, SSMStartChangeRequestExecutionResponse)

    async def start_execution_preview(
        self,
        request: SSMStartExecutionPreviewRequest,
    ) -> SSMStartExecutionPreviewResponse:
        client = self._require_client()
        return await self._execute(client.start_execution_preview, request, SSMStartExecutionPreviewResponse)

    async def start_session(
        self,
        request: SSMStartSessionRequest,
    ) -> SSMStartSessionResponse:
        client = self._require_client()
        return await self._execute(client.start_session, request, SSMStartSessionResponse)

    async def stop_automation_execution(
        self,
        request: SSMStopAutomationExecutionRequest,
    ) -> SSMStopAutomationExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_automation_execution, request, SSMStopAutomationExecutionResponse)

    async def terminate_session(
        self,
        request: SSMTerminateSessionRequest,
    ) -> SSMTerminateSessionResponse:
        client = self._require_client()
        return await self._execute(client.terminate_session, request, SSMTerminateSessionResponse)

    async def unlabel_parameter_version(
        self,
        request: SSMUnlabelParameterVersionRequest,
    ) -> SSMUnlabelParameterVersionResponse:
        client = self._require_client()
        return await self._execute(client.unlabel_parameter_version, request, SSMUnlabelParameterVersionResponse)

    async def update_association(
        self,
        request: SSMUpdateAssociationRequest,
    ) -> SSMUpdateAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_association, request, SSMUpdateAssociationResponse)

    async def update_association_status(
        self,
        request: SSMUpdateAssociationStatusRequest,
    ) -> SSMUpdateAssociationStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_association_status, request, SSMUpdateAssociationStatusResponse)

    async def update_cloud_connector(
        self,
        request: SSMUpdateCloudConnectorRequest,
    ) -> SSMUpdateCloudConnectorResponse:
        client = self._require_client()
        return await self._execute(client.update_cloud_connector, request, SSMUpdateCloudConnectorResponse)

    async def update_document(
        self,
        request: SSMUpdateDocumentRequest,
    ) -> SSMUpdateDocumentResponse:
        client = self._require_client()
        return await self._execute(client.update_document, request, SSMUpdateDocumentResponse)

    async def update_document_default_version(
        self,
        request: SSMUpdateDocumentDefaultVersionRequest,
    ) -> SSMUpdateDocumentDefaultVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_document_default_version, request, SSMUpdateDocumentDefaultVersionResponse)

    async def update_document_metadata(
        self,
        request: SSMUpdateDocumentMetadataRequest,
    ) -> SSMUpdateDocumentMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_document_metadata, request, SSMUpdateDocumentMetadataResponse)

    async def update_maintenance_window(
        self,
        request: SSMUpdateMaintenanceWindowRequest,
    ) -> SSMUpdateMaintenanceWindowResponse:
        client = self._require_client()
        return await self._execute(client.update_maintenance_window, request, SSMUpdateMaintenanceWindowResponse)

    async def update_maintenance_window_target(
        self,
        request: SSMUpdateMaintenanceWindowTargetRequest,
    ) -> SSMUpdateMaintenanceWindowTargetResponse:
        client = self._require_client()
        return await self._execute(client.update_maintenance_window_target, request, SSMUpdateMaintenanceWindowTargetResponse)

    async def update_maintenance_window_task(
        self,
        request: SSMUpdateMaintenanceWindowTaskRequest,
    ) -> SSMUpdateMaintenanceWindowTaskResponse:
        client = self._require_client()
        return await self._execute(client.update_maintenance_window_task, request, SSMUpdateMaintenanceWindowTaskResponse)

    async def update_managed_instance_role(
        self,
        request: SSMUpdateManagedInstanceRoleRequest,
    ) -> SSMUpdateManagedInstanceRoleResponse:
        client = self._require_client()
        return await self._execute(client.update_managed_instance_role, request, SSMUpdateManagedInstanceRoleResponse)

    async def update_ops_item(
        self,
        request: SSMUpdateOpsItemRequest,
    ) -> SSMUpdateOpsItemResponse:
        client = self._require_client()
        return await self._execute(client.update_ops_item, request, SSMUpdateOpsItemResponse)

    async def update_ops_metadata(
        self,
        request: SSMUpdateOpsMetadataRequest,
    ) -> SSMUpdateOpsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_ops_metadata, request, SSMUpdateOpsMetadataResponse)

    async def update_patch_baseline(
        self,
        request: SSMUpdatePatchBaselineRequest,
    ) -> SSMUpdatePatchBaselineResponse:
        client = self._require_client()
        return await self._execute(client.update_patch_baseline, request, SSMUpdatePatchBaselineResponse)

    async def update_resource_data_sync(
        self,
        request: SSMUpdateResourceDataSyncRequest,
    ) -> SSMUpdateResourceDataSyncResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_data_sync, request, SSMUpdateResourceDataSyncResponse)

    async def update_service_setting(
        self,
        request: SSMUpdateServiceSettingRequest,
    ) -> SSMUpdateServiceSettingResponse:
        client = self._require_client()
        return await self._execute(client.update_service_setting, request, SSMUpdateServiceSettingResponse)

    async def validate_cloud_connector(
        self,
        request: SSMValidateCloudConnectorRequest,
    ) -> SSMValidateCloudConnectorResponse:
        client = self._require_client()
        return await self._execute(client.validate_cloud_connector, request, SSMValidateCloudConnectorResponse)

    async def validate_cloud_connector_paginated(
        self,
        request: SSMValidateCloudConnectorRequest,
    ) -> list[SSMValidateCloudConnectorResponse]:
        return await self._paginate('validate_cloud_connector', request, SSMValidateCloudConnectorResponse)
