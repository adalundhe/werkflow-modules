from werkflow_aws.models.cloud_formation import (
    CloudFormationActivateOrganizationsAccessRequest,
    CloudFormationActivateOrganizationsAccessResponse,
    CloudFormationActivateTypeRequest,
    CloudFormationActivateTypeResponse,
    CloudFormationBatchDescribeTypeConfigurationsRequest,
    CloudFormationBatchDescribeTypeConfigurationsResponse,
    CloudFormationCancelUpdateStackRequest,
    CloudFormationCancelUpdateStackResponse,
    CloudFormationContinueUpdateRollbackRequest,
    CloudFormationContinueUpdateRollbackResponse,
    CloudFormationCreateChangeSetRequest,
    CloudFormationCreateChangeSetResponse,
    CloudFormationCreateGeneratedTemplateRequest,
    CloudFormationCreateGeneratedTemplateResponse,
    CloudFormationCreateStackInstancesRequest,
    CloudFormationCreateStackInstancesResponse,
    CloudFormationCreateStackRefactorRequest,
    CloudFormationCreateStackRefactorResponse,
    CloudFormationCreateStackRequest,
    CloudFormationCreateStackResponse,
    CloudFormationCreateStackSetRequest,
    CloudFormationCreateStackSetResponse,
    CloudFormationDeactivateOrganizationsAccessRequest,
    CloudFormationDeactivateOrganizationsAccessResponse,
    CloudFormationDeactivateTypeRequest,
    CloudFormationDeactivateTypeResponse,
    CloudFormationDeleteChangeSetRequest,
    CloudFormationDeleteChangeSetResponse,
    CloudFormationDeleteGeneratedTemplateRequest,
    CloudFormationDeleteGeneratedTemplateResponse,
    CloudFormationDeleteStackInstancesRequest,
    CloudFormationDeleteStackInstancesResponse,
    CloudFormationDeleteStackRequest,
    CloudFormationDeleteStackResponse,
    CloudFormationDeleteStackSetRequest,
    CloudFormationDeleteStackSetResponse,
    CloudFormationDeregisterTypeRequest,
    CloudFormationDeregisterTypeResponse,
    CloudFormationDescribeAccountLimitsRequest,
    CloudFormationDescribeAccountLimitsResponse,
    CloudFormationDescribeChangeSetHooksRequest,
    CloudFormationDescribeChangeSetHooksResponse,
    CloudFormationDescribeChangeSetRequest,
    CloudFormationDescribeChangeSetResponse,
    CloudFormationDescribeEventsRequest,
    CloudFormationDescribeEventsResponse,
    CloudFormationDescribeGeneratedTemplateRequest,
    CloudFormationDescribeGeneratedTemplateResponse,
    CloudFormationDescribeOrganizationsAccessRequest,
    CloudFormationDescribeOrganizationsAccessResponse,
    CloudFormationDescribePublisherRequest,
    CloudFormationDescribePublisherResponse,
    CloudFormationDescribeResourceScanRequest,
    CloudFormationDescribeResourceScanResponse,
    CloudFormationDescribeStackDriftDetectionStatusRequest,
    CloudFormationDescribeStackDriftDetectionStatusResponse,
    CloudFormationDescribeStackEventsRequest,
    CloudFormationDescribeStackEventsResponse,
    CloudFormationDescribeStackInstanceRequest,
    CloudFormationDescribeStackInstanceResponse,
    CloudFormationDescribeStackRefactorRequest,
    CloudFormationDescribeStackRefactorResponse,
    CloudFormationDescribeStackResourceDriftsRequest,
    CloudFormationDescribeStackResourceDriftsResponse,
    CloudFormationDescribeStackResourceRequest,
    CloudFormationDescribeStackResourceResponse,
    CloudFormationDescribeStackResourcesRequest,
    CloudFormationDescribeStackResourcesResponse,
    CloudFormationDescribeStackSetOperationRequest,
    CloudFormationDescribeStackSetOperationResponse,
    CloudFormationDescribeStackSetRequest,
    CloudFormationDescribeStackSetResponse,
    CloudFormationDescribeStacksRequest,
    CloudFormationDescribeStacksResponse,
    CloudFormationDescribeTypeRegistrationRequest,
    CloudFormationDescribeTypeRegistrationResponse,
    CloudFormationDescribeTypeRequest,
    CloudFormationDescribeTypeResponse,
    CloudFormationDetectStackDriftRequest,
    CloudFormationDetectStackDriftResponse,
    CloudFormationDetectStackResourceDriftRequest,
    CloudFormationDetectStackResourceDriftResponse,
    CloudFormationDetectStackSetDriftRequest,
    CloudFormationDetectStackSetDriftResponse,
    CloudFormationEstimateTemplateCostRequest,
    CloudFormationEstimateTemplateCostResponse,
    CloudFormationExecuteChangeSetRequest,
    CloudFormationExecuteChangeSetResponse,
    CloudFormationExecuteStackRefactorRequest,
    CloudFormationExecuteStackRefactorResponse,
    CloudFormationGetGeneratedTemplateRequest,
    CloudFormationGetGeneratedTemplateResponse,
    CloudFormationGetHookResultRequest,
    CloudFormationGetHookResultResponse,
    CloudFormationGetStackPolicyRequest,
    CloudFormationGetStackPolicyResponse,
    CloudFormationGetTemplateRequest,
    CloudFormationGetTemplateResponse,
    CloudFormationGetTemplateSummaryRequest,
    CloudFormationGetTemplateSummaryResponse,
    CloudFormationImportStacksToStackSetRequest,
    CloudFormationImportStacksToStackSetResponse,
    CloudFormationListChangeSetsRequest,
    CloudFormationListChangeSetsResponse,
    CloudFormationListExportsRequest,
    CloudFormationListExportsResponse,
    CloudFormationListGeneratedTemplatesRequest,
    CloudFormationListGeneratedTemplatesResponse,
    CloudFormationListHookResultsRequest,
    CloudFormationListHookResultsResponse,
    CloudFormationListImportsRequest,
    CloudFormationListImportsResponse,
    CloudFormationListResourceScanRelatedResourcesRequest,
    CloudFormationListResourceScanRelatedResourcesResponse,
    CloudFormationListResourceScanResourcesRequest,
    CloudFormationListResourceScanResourcesResponse,
    CloudFormationListResourceScansRequest,
    CloudFormationListResourceScansResponse,
    CloudFormationListStackInstanceResourceDriftsRequest,
    CloudFormationListStackInstanceResourceDriftsResponse,
    CloudFormationListStackInstancesRequest,
    CloudFormationListStackInstancesResponse,
    CloudFormationListStackRefactorActionsRequest,
    CloudFormationListStackRefactorActionsResponse,
    CloudFormationListStackRefactorsRequest,
    CloudFormationListStackRefactorsResponse,
    CloudFormationListStackResourcesRequest,
    CloudFormationListStackResourcesResponse,
    CloudFormationListStackSetAutoDeploymentTargetsRequest,
    CloudFormationListStackSetAutoDeploymentTargetsResponse,
    CloudFormationListStackSetOperationResultsRequest,
    CloudFormationListStackSetOperationResultsResponse,
    CloudFormationListStackSetOperationsRequest,
    CloudFormationListStackSetOperationsResponse,
    CloudFormationListStackSetsRequest,
    CloudFormationListStackSetsResponse,
    CloudFormationListStacksRequest,
    CloudFormationListStacksResponse,
    CloudFormationListTypeRegistrationsRequest,
    CloudFormationListTypeRegistrationsResponse,
    CloudFormationListTypeVersionsRequest,
    CloudFormationListTypeVersionsResponse,
    CloudFormationListTypesRequest,
    CloudFormationListTypesResponse,
    CloudFormationPublishTypeRequest,
    CloudFormationPublishTypeResponse,
    CloudFormationRecordHandlerProgressRequest,
    CloudFormationRecordHandlerProgressResponse,
    CloudFormationRegisterPublisherRequest,
    CloudFormationRegisterPublisherResponse,
    CloudFormationRegisterTypeRequest,
    CloudFormationRegisterTypeResponse,
    CloudFormationRemoveAliasRequest,
    CloudFormationRemoveAliasResponse,
    CloudFormationRollbackStackRequest,
    CloudFormationRollbackStackResponse,
    CloudFormationSetAliasRequest,
    CloudFormationSetAliasResponse,
    CloudFormationSetStackPolicyRequest,
    CloudFormationSetStackPolicyResponse,
    CloudFormationSetTypeConfigurationRequest,
    CloudFormationSetTypeConfigurationResponse,
    CloudFormationSetTypeDefaultVersionRequest,
    CloudFormationSetTypeDefaultVersionResponse,
    CloudFormationSignalResourceRequest,
    CloudFormationSignalResourceResponse,
    CloudFormationStartResourceScanRequest,
    CloudFormationStartResourceScanResponse,
    CloudFormationStopStackSetOperationRequest,
    CloudFormationStopStackSetOperationResponse,
    CloudFormationTestTypeRequest,
    CloudFormationTestTypeResponse,
    CloudFormationUpdateGeneratedTemplateRequest,
    CloudFormationUpdateGeneratedTemplateResponse,
    CloudFormationUpdateStackInstancesRequest,
    CloudFormationUpdateStackInstancesResponse,
    CloudFormationUpdateStackRequest,
    CloudFormationUpdateStackResponse,
    CloudFormationUpdateStackSetRequest,
    CloudFormationUpdateStackSetResponse,
    CloudFormationUpdateTerminationProtectionRequest,
    CloudFormationUpdateTerminationProtectionResponse,
    CloudFormationValidateTemplateRequest,
    CloudFormationValidateTemplateResponse,
)
from werkflow_aws.types.cloud_formation_client import CloudFormationClient
from .base import AWSBaseService


class AWSCloudFormation(AWSBaseService[CloudFormationClient]):
    service_name = 'cloud-formation'
    boto3_service_name = 'cloudformation'

    def __init__(self) -> None:
        super().__init__(service_name='cloud-formation', boto3_service_name='cloudformation')

    async def activate_organizations_access(
        self,
        request: CloudFormationActivateOrganizationsAccessRequest | None = None,
    ) -> CloudFormationActivateOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.activate_organizations_access, request, CloudFormationActivateOrganizationsAccessResponse)

    async def activate_type(
        self,
        request: CloudFormationActivateTypeRequest | None = None,
    ) -> CloudFormationActivateTypeResponse:
        client = self._require_client()
        return await self._execute(client.activate_type, request, CloudFormationActivateTypeResponse)

    async def batch_describe_type_configurations(
        self,
        request: CloudFormationBatchDescribeTypeConfigurationsRequest,
    ) -> CloudFormationBatchDescribeTypeConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_describe_type_configurations, request, CloudFormationBatchDescribeTypeConfigurationsResponse)

    async def cancel_update_stack(
        self,
        request: CloudFormationCancelUpdateStackRequest,
    ) -> CloudFormationCancelUpdateStackResponse:
        client = self._require_client()
        return await self._execute(client.cancel_update_stack, request, CloudFormationCancelUpdateStackResponse)

    async def continue_update_rollback(
        self,
        request: CloudFormationContinueUpdateRollbackRequest,
    ) -> CloudFormationContinueUpdateRollbackResponse:
        client = self._require_client()
        return await self._execute(client.continue_update_rollback, request, CloudFormationContinueUpdateRollbackResponse)

    async def create_change_set(
        self,
        request: CloudFormationCreateChangeSetRequest,
    ) -> CloudFormationCreateChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.create_change_set, request, CloudFormationCreateChangeSetResponse)

    async def create_generated_template(
        self,
        request: CloudFormationCreateGeneratedTemplateRequest,
    ) -> CloudFormationCreateGeneratedTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_generated_template, request, CloudFormationCreateGeneratedTemplateResponse)

    async def create_stack(
        self,
        request: CloudFormationCreateStackRequest,
    ) -> CloudFormationCreateStackResponse:
        client = self._require_client()
        return await self._execute(client.create_stack, request, CloudFormationCreateStackResponse)

    async def create_stack_instances(
        self,
        request: CloudFormationCreateStackInstancesRequest,
    ) -> CloudFormationCreateStackInstancesResponse:
        client = self._require_client()
        return await self._execute(client.create_stack_instances, request, CloudFormationCreateStackInstancesResponse)

    async def create_stack_refactor(
        self,
        request: CloudFormationCreateStackRefactorRequest,
    ) -> CloudFormationCreateStackRefactorResponse:
        client = self._require_client()
        return await self._execute(client.create_stack_refactor, request, CloudFormationCreateStackRefactorResponse)

    async def create_stack_set(
        self,
        request: CloudFormationCreateStackSetRequest,
    ) -> CloudFormationCreateStackSetResponse:
        client = self._require_client()
        return await self._execute(client.create_stack_set, request, CloudFormationCreateStackSetResponse)

    async def deactivate_organizations_access(
        self,
        request: CloudFormationDeactivateOrganizationsAccessRequest | None = None,
    ) -> CloudFormationDeactivateOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_organizations_access, request, CloudFormationDeactivateOrganizationsAccessResponse)

    async def deactivate_type(
        self,
        request: CloudFormationDeactivateTypeRequest | None = None,
    ) -> CloudFormationDeactivateTypeResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_type, request, CloudFormationDeactivateTypeResponse)

    async def delete_change_set(
        self,
        request: CloudFormationDeleteChangeSetRequest,
    ) -> CloudFormationDeleteChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_change_set, request, CloudFormationDeleteChangeSetResponse)

    async def delete_generated_template(
        self,
        request: CloudFormationDeleteGeneratedTemplateRequest,
    ) -> CloudFormationDeleteGeneratedTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_generated_template, request, CloudFormationDeleteGeneratedTemplateResponse)

    async def delete_stack(
        self,
        request: CloudFormationDeleteStackRequest,
    ) -> CloudFormationDeleteStackResponse:
        client = self._require_client()
        return await self._execute(client.delete_stack, request, CloudFormationDeleteStackResponse)

    async def delete_stack_instances(
        self,
        request: CloudFormationDeleteStackInstancesRequest,
    ) -> CloudFormationDeleteStackInstancesResponse:
        client = self._require_client()
        return await self._execute(client.delete_stack_instances, request, CloudFormationDeleteStackInstancesResponse)

    async def delete_stack_set(
        self,
        request: CloudFormationDeleteStackSetRequest,
    ) -> CloudFormationDeleteStackSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_stack_set, request, CloudFormationDeleteStackSetResponse)

    async def deregister_type(
        self,
        request: CloudFormationDeregisterTypeRequest | None = None,
    ) -> CloudFormationDeregisterTypeResponse:
        client = self._require_client()
        return await self._execute(client.deregister_type, request, CloudFormationDeregisterTypeResponse)

    async def describe_account_limits(
        self,
        request: CloudFormationDescribeAccountLimitsRequest | None = None,
    ) -> CloudFormationDescribeAccountLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_limits, request, CloudFormationDescribeAccountLimitsResponse)

    async def describe_account_limits_paginated(
        self,
        request: CloudFormationDescribeAccountLimitsRequest | None = None,
    ) -> list[CloudFormationDescribeAccountLimitsResponse]:
        return await self._paginate('describe_account_limits', request, CloudFormationDescribeAccountLimitsResponse)

    async def describe_change_set(
        self,
        request: CloudFormationDescribeChangeSetRequest,
    ) -> CloudFormationDescribeChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.describe_change_set, request, CloudFormationDescribeChangeSetResponse)

    async def describe_change_set_paginated(
        self,
        request: CloudFormationDescribeChangeSetRequest,
    ) -> list[CloudFormationDescribeChangeSetResponse]:
        return await self._paginate('describe_change_set', request, CloudFormationDescribeChangeSetResponse)

    async def describe_change_set_hooks(
        self,
        request: CloudFormationDescribeChangeSetHooksRequest,
    ) -> CloudFormationDescribeChangeSetHooksResponse:
        client = self._require_client()
        return await self._execute(client.describe_change_set_hooks, request, CloudFormationDescribeChangeSetHooksResponse)

    async def describe_events(
        self,
        request: CloudFormationDescribeEventsRequest | None = None,
    ) -> CloudFormationDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, CloudFormationDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: CloudFormationDescribeEventsRequest | None = None,
    ) -> list[CloudFormationDescribeEventsResponse]:
        return await self._paginate('describe_events', request, CloudFormationDescribeEventsResponse)

    async def describe_generated_template(
        self,
        request: CloudFormationDescribeGeneratedTemplateRequest,
    ) -> CloudFormationDescribeGeneratedTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_generated_template, request, CloudFormationDescribeGeneratedTemplateResponse)

    async def describe_organizations_access(
        self,
        request: CloudFormationDescribeOrganizationsAccessRequest | None = None,
    ) -> CloudFormationDescribeOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.describe_organizations_access, request, CloudFormationDescribeOrganizationsAccessResponse)

    async def describe_publisher(
        self,
        request: CloudFormationDescribePublisherRequest | None = None,
    ) -> CloudFormationDescribePublisherResponse:
        client = self._require_client()
        return await self._execute(client.describe_publisher, request, CloudFormationDescribePublisherResponse)

    async def describe_resource_scan(
        self,
        request: CloudFormationDescribeResourceScanRequest,
    ) -> CloudFormationDescribeResourceScanResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_scan, request, CloudFormationDescribeResourceScanResponse)

    async def describe_stack_drift_detection_status(
        self,
        request: CloudFormationDescribeStackDriftDetectionStatusRequest,
    ) -> CloudFormationDescribeStackDriftDetectionStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_drift_detection_status, request, CloudFormationDescribeStackDriftDetectionStatusResponse)

    async def describe_stack_events(
        self,
        request: CloudFormationDescribeStackEventsRequest,
    ) -> CloudFormationDescribeStackEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_events, request, CloudFormationDescribeStackEventsResponse)

    async def describe_stack_events_paginated(
        self,
        request: CloudFormationDescribeStackEventsRequest,
    ) -> list[CloudFormationDescribeStackEventsResponse]:
        return await self._paginate('describe_stack_events', request, CloudFormationDescribeStackEventsResponse)

    async def describe_stack_instance(
        self,
        request: CloudFormationDescribeStackInstanceRequest,
    ) -> CloudFormationDescribeStackInstanceResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_instance, request, CloudFormationDescribeStackInstanceResponse)

    async def describe_stack_refactor(
        self,
        request: CloudFormationDescribeStackRefactorRequest,
    ) -> CloudFormationDescribeStackRefactorResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_refactor, request, CloudFormationDescribeStackRefactorResponse)

    async def describe_stack_resource(
        self,
        request: CloudFormationDescribeStackResourceRequest,
    ) -> CloudFormationDescribeStackResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_resource, request, CloudFormationDescribeStackResourceResponse)

    async def describe_stack_resource_drifts(
        self,
        request: CloudFormationDescribeStackResourceDriftsRequest,
    ) -> CloudFormationDescribeStackResourceDriftsResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_resource_drifts, request, CloudFormationDescribeStackResourceDriftsResponse)

    async def describe_stack_resources(
        self,
        request: CloudFormationDescribeStackResourcesRequest | None = None,
    ) -> CloudFormationDescribeStackResourcesResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_resources, request, CloudFormationDescribeStackResourcesResponse)

    async def describe_stack_set(
        self,
        request: CloudFormationDescribeStackSetRequest,
    ) -> CloudFormationDescribeStackSetResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_set, request, CloudFormationDescribeStackSetResponse)

    async def describe_stack_set_operation(
        self,
        request: CloudFormationDescribeStackSetOperationRequest,
    ) -> CloudFormationDescribeStackSetOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_stack_set_operation, request, CloudFormationDescribeStackSetOperationResponse)

    async def describe_stacks(
        self,
        request: CloudFormationDescribeStacksRequest | None = None,
    ) -> CloudFormationDescribeStacksResponse:
        client = self._require_client()
        return await self._execute(client.describe_stacks, request, CloudFormationDescribeStacksResponse)

    async def describe_stacks_paginated(
        self,
        request: CloudFormationDescribeStacksRequest | None = None,
    ) -> list[CloudFormationDescribeStacksResponse]:
        return await self._paginate('describe_stacks', request, CloudFormationDescribeStacksResponse)

    async def describe_type(
        self,
        request: CloudFormationDescribeTypeRequest | None = None,
    ) -> CloudFormationDescribeTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_type, request, CloudFormationDescribeTypeResponse)

    async def describe_type_registration(
        self,
        request: CloudFormationDescribeTypeRegistrationRequest,
    ) -> CloudFormationDescribeTypeRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.describe_type_registration, request, CloudFormationDescribeTypeRegistrationResponse)

    async def detect_stack_drift(
        self,
        request: CloudFormationDetectStackDriftRequest,
    ) -> CloudFormationDetectStackDriftResponse:
        client = self._require_client()
        return await self._execute(client.detect_stack_drift, request, CloudFormationDetectStackDriftResponse)

    async def detect_stack_resource_drift(
        self,
        request: CloudFormationDetectStackResourceDriftRequest,
    ) -> CloudFormationDetectStackResourceDriftResponse:
        client = self._require_client()
        return await self._execute(client.detect_stack_resource_drift, request, CloudFormationDetectStackResourceDriftResponse)

    async def detect_stack_set_drift(
        self,
        request: CloudFormationDetectStackSetDriftRequest,
    ) -> CloudFormationDetectStackSetDriftResponse:
        client = self._require_client()
        return await self._execute(client.detect_stack_set_drift, request, CloudFormationDetectStackSetDriftResponse)

    async def estimate_template_cost(
        self,
        request: CloudFormationEstimateTemplateCostRequest | None = None,
    ) -> CloudFormationEstimateTemplateCostResponse:
        client = self._require_client()
        return await self._execute(client.estimate_template_cost, request, CloudFormationEstimateTemplateCostResponse)

    async def execute_change_set(
        self,
        request: CloudFormationExecuteChangeSetRequest,
    ) -> CloudFormationExecuteChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.execute_change_set, request, CloudFormationExecuteChangeSetResponse)

    async def execute_stack_refactor(
        self,
        request: CloudFormationExecuteStackRefactorRequest,
    ) -> CloudFormationExecuteStackRefactorResponse:
        client = self._require_client()
        return await self._execute(client.execute_stack_refactor, request, CloudFormationExecuteStackRefactorResponse)

    async def get_generated_template(
        self,
        request: CloudFormationGetGeneratedTemplateRequest,
    ) -> CloudFormationGetGeneratedTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_generated_template, request, CloudFormationGetGeneratedTemplateResponse)

    async def get_hook_result(
        self,
        request: CloudFormationGetHookResultRequest | None = None,
    ) -> CloudFormationGetHookResultResponse:
        client = self._require_client()
        return await self._execute(client.get_hook_result, request, CloudFormationGetHookResultResponse)

    async def get_stack_policy(
        self,
        request: CloudFormationGetStackPolicyRequest,
    ) -> CloudFormationGetStackPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_stack_policy, request, CloudFormationGetStackPolicyResponse)

    async def get_template(
        self,
        request: CloudFormationGetTemplateRequest | None = None,
    ) -> CloudFormationGetTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_template, request, CloudFormationGetTemplateResponse)

    async def get_template_summary(
        self,
        request: CloudFormationGetTemplateSummaryRequest | None = None,
    ) -> CloudFormationGetTemplateSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_template_summary, request, CloudFormationGetTemplateSummaryResponse)

    async def import_stacks_to_stack_set(
        self,
        request: CloudFormationImportStacksToStackSetRequest,
    ) -> CloudFormationImportStacksToStackSetResponse:
        client = self._require_client()
        return await self._execute(client.import_stacks_to_stack_set, request, CloudFormationImportStacksToStackSetResponse)

    async def list_change_sets(
        self,
        request: CloudFormationListChangeSetsRequest,
    ) -> CloudFormationListChangeSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_change_sets, request, CloudFormationListChangeSetsResponse)

    async def list_change_sets_paginated(
        self,
        request: CloudFormationListChangeSetsRequest,
    ) -> list[CloudFormationListChangeSetsResponse]:
        return await self._paginate('list_change_sets', request, CloudFormationListChangeSetsResponse)

    async def list_exports(
        self,
        request: CloudFormationListExportsRequest | None = None,
    ) -> CloudFormationListExportsResponse:
        client = self._require_client()
        return await self._execute(client.list_exports, request, CloudFormationListExportsResponse)

    async def list_exports_paginated(
        self,
        request: CloudFormationListExportsRequest | None = None,
    ) -> list[CloudFormationListExportsResponse]:
        return await self._paginate('list_exports', request, CloudFormationListExportsResponse)

    async def list_generated_templates(
        self,
        request: CloudFormationListGeneratedTemplatesRequest | None = None,
    ) -> CloudFormationListGeneratedTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_generated_templates, request, CloudFormationListGeneratedTemplatesResponse)

    async def list_generated_templates_paginated(
        self,
        request: CloudFormationListGeneratedTemplatesRequest | None = None,
    ) -> list[CloudFormationListGeneratedTemplatesResponse]:
        return await self._paginate('list_generated_templates', request, CloudFormationListGeneratedTemplatesResponse)

    async def list_hook_results(
        self,
        request: CloudFormationListHookResultsRequest | None = None,
    ) -> CloudFormationListHookResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_hook_results, request, CloudFormationListHookResultsResponse)

    async def list_imports(
        self,
        request: CloudFormationListImportsRequest,
    ) -> CloudFormationListImportsResponse:
        client = self._require_client()
        return await self._execute(client.list_imports, request, CloudFormationListImportsResponse)

    async def list_imports_paginated(
        self,
        request: CloudFormationListImportsRequest,
    ) -> list[CloudFormationListImportsResponse]:
        return await self._paginate('list_imports', request, CloudFormationListImportsResponse)

    async def list_resource_scan_related_resources(
        self,
        request: CloudFormationListResourceScanRelatedResourcesRequest,
    ) -> CloudFormationListResourceScanRelatedResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_scan_related_resources, request, CloudFormationListResourceScanRelatedResourcesResponse)

    async def list_resource_scan_related_resources_paginated(
        self,
        request: CloudFormationListResourceScanRelatedResourcesRequest,
    ) -> list[CloudFormationListResourceScanRelatedResourcesResponse]:
        return await self._paginate('list_resource_scan_related_resources', request, CloudFormationListResourceScanRelatedResourcesResponse)

    async def list_resource_scan_resources(
        self,
        request: CloudFormationListResourceScanResourcesRequest,
    ) -> CloudFormationListResourceScanResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_scan_resources, request, CloudFormationListResourceScanResourcesResponse)

    async def list_resource_scan_resources_paginated(
        self,
        request: CloudFormationListResourceScanResourcesRequest,
    ) -> list[CloudFormationListResourceScanResourcesResponse]:
        return await self._paginate('list_resource_scan_resources', request, CloudFormationListResourceScanResourcesResponse)

    async def list_resource_scans(
        self,
        request: CloudFormationListResourceScansRequest | None = None,
    ) -> CloudFormationListResourceScansResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_scans, request, CloudFormationListResourceScansResponse)

    async def list_resource_scans_paginated(
        self,
        request: CloudFormationListResourceScansRequest | None = None,
    ) -> list[CloudFormationListResourceScansResponse]:
        return await self._paginate('list_resource_scans', request, CloudFormationListResourceScansResponse)

    async def list_stack_instance_resource_drifts(
        self,
        request: CloudFormationListStackInstanceResourceDriftsRequest,
    ) -> CloudFormationListStackInstanceResourceDriftsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_instance_resource_drifts, request, CloudFormationListStackInstanceResourceDriftsResponse)

    async def list_stack_instances(
        self,
        request: CloudFormationListStackInstancesRequest,
    ) -> CloudFormationListStackInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_instances, request, CloudFormationListStackInstancesResponse)

    async def list_stack_instances_paginated(
        self,
        request: CloudFormationListStackInstancesRequest,
    ) -> list[CloudFormationListStackInstancesResponse]:
        return await self._paginate('list_stack_instances', request, CloudFormationListStackInstancesResponse)

    async def list_stack_refactor_actions(
        self,
        request: CloudFormationListStackRefactorActionsRequest,
    ) -> CloudFormationListStackRefactorActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_refactor_actions, request, CloudFormationListStackRefactorActionsResponse)

    async def list_stack_refactor_actions_paginated(
        self,
        request: CloudFormationListStackRefactorActionsRequest,
    ) -> list[CloudFormationListStackRefactorActionsResponse]:
        return await self._paginate('list_stack_refactor_actions', request, CloudFormationListStackRefactorActionsResponse)

    async def list_stack_refactors(
        self,
        request: CloudFormationListStackRefactorsRequest | None = None,
    ) -> CloudFormationListStackRefactorsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_refactors, request, CloudFormationListStackRefactorsResponse)

    async def list_stack_refactors_paginated(
        self,
        request: CloudFormationListStackRefactorsRequest | None = None,
    ) -> list[CloudFormationListStackRefactorsResponse]:
        return await self._paginate('list_stack_refactors', request, CloudFormationListStackRefactorsResponse)

    async def list_stack_resources(
        self,
        request: CloudFormationListStackResourcesRequest,
    ) -> CloudFormationListStackResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_resources, request, CloudFormationListStackResourcesResponse)

    async def list_stack_resources_paginated(
        self,
        request: CloudFormationListStackResourcesRequest,
    ) -> list[CloudFormationListStackResourcesResponse]:
        return await self._paginate('list_stack_resources', request, CloudFormationListStackResourcesResponse)

    async def list_stack_set_auto_deployment_targets(
        self,
        request: CloudFormationListStackSetAutoDeploymentTargetsRequest,
    ) -> CloudFormationListStackSetAutoDeploymentTargetsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_set_auto_deployment_targets, request, CloudFormationListStackSetAutoDeploymentTargetsResponse)

    async def list_stack_set_operation_results(
        self,
        request: CloudFormationListStackSetOperationResultsRequest,
    ) -> CloudFormationListStackSetOperationResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_set_operation_results, request, CloudFormationListStackSetOperationResultsResponse)

    async def list_stack_set_operation_results_paginated(
        self,
        request: CloudFormationListStackSetOperationResultsRequest,
    ) -> list[CloudFormationListStackSetOperationResultsResponse]:
        return await self._paginate('list_stack_set_operation_results', request, CloudFormationListStackSetOperationResultsResponse)

    async def list_stack_set_operations(
        self,
        request: CloudFormationListStackSetOperationsRequest,
    ) -> CloudFormationListStackSetOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_set_operations, request, CloudFormationListStackSetOperationsResponse)

    async def list_stack_set_operations_paginated(
        self,
        request: CloudFormationListStackSetOperationsRequest,
    ) -> list[CloudFormationListStackSetOperationsResponse]:
        return await self._paginate('list_stack_set_operations', request, CloudFormationListStackSetOperationsResponse)

    async def list_stack_sets(
        self,
        request: CloudFormationListStackSetsRequest | None = None,
    ) -> CloudFormationListStackSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_sets, request, CloudFormationListStackSetsResponse)

    async def list_stack_sets_paginated(
        self,
        request: CloudFormationListStackSetsRequest | None = None,
    ) -> list[CloudFormationListStackSetsResponse]:
        return await self._paginate('list_stack_sets', request, CloudFormationListStackSetsResponse)

    async def list_stacks(
        self,
        request: CloudFormationListStacksRequest | None = None,
    ) -> CloudFormationListStacksResponse:
        client = self._require_client()
        return await self._execute(client.list_stacks, request, CloudFormationListStacksResponse)

    async def list_stacks_paginated(
        self,
        request: CloudFormationListStacksRequest | None = None,
    ) -> list[CloudFormationListStacksResponse]:
        return await self._paginate('list_stacks', request, CloudFormationListStacksResponse)

    async def list_type_registrations(
        self,
        request: CloudFormationListTypeRegistrationsRequest | None = None,
    ) -> CloudFormationListTypeRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.list_type_registrations, request, CloudFormationListTypeRegistrationsResponse)

    async def list_type_versions(
        self,
        request: CloudFormationListTypeVersionsRequest | None = None,
    ) -> CloudFormationListTypeVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_type_versions, request, CloudFormationListTypeVersionsResponse)

    async def list_types(
        self,
        request: CloudFormationListTypesRequest | None = None,
    ) -> CloudFormationListTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_types, request, CloudFormationListTypesResponse)

    async def list_types_paginated(
        self,
        request: CloudFormationListTypesRequest | None = None,
    ) -> list[CloudFormationListTypesResponse]:
        return await self._paginate('list_types', request, CloudFormationListTypesResponse)

    async def publish_type(
        self,
        request: CloudFormationPublishTypeRequest | None = None,
    ) -> CloudFormationPublishTypeResponse:
        client = self._require_client()
        return await self._execute(client.publish_type, request, CloudFormationPublishTypeResponse)

    async def record_handler_progress(
        self,
        request: CloudFormationRecordHandlerProgressRequest,
    ) -> CloudFormationRecordHandlerProgressResponse:
        client = self._require_client()
        return await self._execute(client.record_handler_progress, request, CloudFormationRecordHandlerProgressResponse)

    async def register_publisher(
        self,
        request: CloudFormationRegisterPublisherRequest | None = None,
    ) -> CloudFormationRegisterPublisherResponse:
        client = self._require_client()
        return await self._execute(client.register_publisher, request, CloudFormationRegisterPublisherResponse)

    async def register_type(
        self,
        request: CloudFormationRegisterTypeRequest,
    ) -> CloudFormationRegisterTypeResponse:
        client = self._require_client()
        return await self._execute(client.register_type, request, CloudFormationRegisterTypeResponse)

    async def remove_alias(
        self,
        request: CloudFormationRemoveAliasRequest,
    ) -> CloudFormationRemoveAliasResponse:
        client = self._require_client()
        return await self._execute(client.remove_alias, request, CloudFormationRemoveAliasResponse)

    async def rollback_stack(
        self,
        request: CloudFormationRollbackStackRequest,
    ) -> CloudFormationRollbackStackResponse:
        client = self._require_client()
        return await self._execute(client.rollback_stack, request, CloudFormationRollbackStackResponse)

    async def set_alias(
        self,
        request: CloudFormationSetAliasRequest,
    ) -> CloudFormationSetAliasResponse:
        client = self._require_client()
        return await self._execute(client.set_alias, request, CloudFormationSetAliasResponse)

    async def set_stack_policy(
        self,
        request: CloudFormationSetStackPolicyRequest,
    ) -> CloudFormationSetStackPolicyResponse:
        client = self._require_client()
        return await self._execute(client.set_stack_policy, request, CloudFormationSetStackPolicyResponse)

    async def set_type_configuration(
        self,
        request: CloudFormationSetTypeConfigurationRequest,
    ) -> CloudFormationSetTypeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_type_configuration, request, CloudFormationSetTypeConfigurationResponse)

    async def set_type_default_version(
        self,
        request: CloudFormationSetTypeDefaultVersionRequest | None = None,
    ) -> CloudFormationSetTypeDefaultVersionResponse:
        client = self._require_client()
        return await self._execute(client.set_type_default_version, request, CloudFormationSetTypeDefaultVersionResponse)

    async def signal_resource(
        self,
        request: CloudFormationSignalResourceRequest,
    ) -> CloudFormationSignalResourceResponse:
        client = self._require_client()
        return await self._execute(client.signal_resource, request, CloudFormationSignalResourceResponse)

    async def start_resource_scan(
        self,
        request: CloudFormationStartResourceScanRequest | None = None,
    ) -> CloudFormationStartResourceScanResponse:
        client = self._require_client()
        return await self._execute(client.start_resource_scan, request, CloudFormationStartResourceScanResponse)

    async def stop_stack_set_operation(
        self,
        request: CloudFormationStopStackSetOperationRequest,
    ) -> CloudFormationStopStackSetOperationResponse:
        client = self._require_client()
        return await self._execute(client.stop_stack_set_operation, request, CloudFormationStopStackSetOperationResponse)

    async def test_type(
        self,
        request: CloudFormationTestTypeRequest | None = None,
    ) -> CloudFormationTestTypeResponse:
        client = self._require_client()
        return await self._execute(client.test_type, request, CloudFormationTestTypeResponse)

    async def update_generated_template(
        self,
        request: CloudFormationUpdateGeneratedTemplateRequest,
    ) -> CloudFormationUpdateGeneratedTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_generated_template, request, CloudFormationUpdateGeneratedTemplateResponse)

    async def update_stack(
        self,
        request: CloudFormationUpdateStackRequest,
    ) -> CloudFormationUpdateStackResponse:
        client = self._require_client()
        return await self._execute(client.update_stack, request, CloudFormationUpdateStackResponse)

    async def update_stack_instances(
        self,
        request: CloudFormationUpdateStackInstancesRequest,
    ) -> CloudFormationUpdateStackInstancesResponse:
        client = self._require_client()
        return await self._execute(client.update_stack_instances, request, CloudFormationUpdateStackInstancesResponse)

    async def update_stack_set(
        self,
        request: CloudFormationUpdateStackSetRequest,
    ) -> CloudFormationUpdateStackSetResponse:
        client = self._require_client()
        return await self._execute(client.update_stack_set, request, CloudFormationUpdateStackSetResponse)

    async def update_termination_protection(
        self,
        request: CloudFormationUpdateTerminationProtectionRequest,
    ) -> CloudFormationUpdateTerminationProtectionResponse:
        client = self._require_client()
        return await self._execute(client.update_termination_protection, request, CloudFormationUpdateTerminationProtectionResponse)

    async def validate_template(
        self,
        request: CloudFormationValidateTemplateRequest | None = None,
    ) -> CloudFormationValidateTemplateResponse:
        client = self._require_client()
        return await self._execute(client.validate_template, request, CloudFormationValidateTemplateResponse)
