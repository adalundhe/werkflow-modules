from werkflow_aws.models.backup import (
    BackupAssociateBackupVaultMpaApprovalTeamRequest,
    BackupAssociateBackupVaultMpaApprovalTeamResponse,
    BackupCancelLegalHoldRequest,
    BackupCancelLegalHoldResponse,
    BackupCreateBackupAccessPointRequest,
    BackupCreateBackupAccessPointResponse,
    BackupCreateBackupPlanRequest,
    BackupCreateBackupPlanResponse,
    BackupCreateBackupSelectionRequest,
    BackupCreateBackupSelectionResponse,
    BackupCreateBackupVaultRequest,
    BackupCreateBackupVaultResponse,
    BackupCreateFrameworkRequest,
    BackupCreateFrameworkResponse,
    BackupCreateLegalHoldRequest,
    BackupCreateLegalHoldResponse,
    BackupCreateLogicallyAirGappedBackupVaultRequest,
    BackupCreateLogicallyAirGappedBackupVaultResponse,
    BackupCreateReportPlanRequest,
    BackupCreateReportPlanResponse,
    BackupCreateRestoreAccessBackupVaultRequest,
    BackupCreateRestoreAccessBackupVaultResponse,
    BackupCreateRestoreTestingPlanRequest,
    BackupCreateRestoreTestingPlanResponse,
    BackupCreateRestoreTestingSelectionRequest,
    BackupCreateRestoreTestingSelectionResponse,
    BackupCreateTieringConfigurationRequest,
    BackupCreateTieringConfigurationResponse,
    BackupDeleteBackupAccessPointRequest,
    BackupDeleteBackupAccessPointResponse,
    BackupDeleteBackupPlanRequest,
    BackupDeleteBackupPlanResponse,
    BackupDeleteBackupSelectionRequest,
    BackupDeleteBackupSelectionResponse,
    BackupDeleteBackupVaultAccessPolicyRequest,
    BackupDeleteBackupVaultAccessPolicyResponse,
    BackupDeleteBackupVaultLockConfigurationRequest,
    BackupDeleteBackupVaultLockConfigurationResponse,
    BackupDeleteBackupVaultNotificationsRequest,
    BackupDeleteBackupVaultNotificationsResponse,
    BackupDeleteBackupVaultRequest,
    BackupDeleteBackupVaultResponse,
    BackupDeleteFrameworkRequest,
    BackupDeleteFrameworkResponse,
    BackupDeleteRecoveryPointRequest,
    BackupDeleteRecoveryPointResponse,
    BackupDeleteReportPlanRequest,
    BackupDeleteReportPlanResponse,
    BackupDeleteRestoreTestingPlanRequest,
    BackupDeleteRestoreTestingPlanResponse,
    BackupDeleteRestoreTestingSelectionRequest,
    BackupDeleteRestoreTestingSelectionResponse,
    BackupDeleteTieringConfigurationRequest,
    BackupDeleteTieringConfigurationResponse,
    BackupDescribeBackupAccessPointRequest,
    BackupDescribeBackupAccessPointResponse,
    BackupDescribeBackupJobRequest,
    BackupDescribeBackupJobResponse,
    BackupDescribeBackupVaultRequest,
    BackupDescribeBackupVaultResponse,
    BackupDescribeCopyJobRequest,
    BackupDescribeCopyJobResponse,
    BackupDescribeFrameworkRequest,
    BackupDescribeFrameworkResponse,
    BackupDescribeGlobalSettingsRequest,
    BackupDescribeGlobalSettingsResponse,
    BackupDescribeProtectedResourceRequest,
    BackupDescribeProtectedResourceResponse,
    BackupDescribeRecoveryPointRequest,
    BackupDescribeRecoveryPointResponse,
    BackupDescribeRegionSettingsRequest,
    BackupDescribeRegionSettingsResponse,
    BackupDescribeReportJobRequest,
    BackupDescribeReportJobResponse,
    BackupDescribeReportPlanRequest,
    BackupDescribeReportPlanResponse,
    BackupDescribeRestoreJobRequest,
    BackupDescribeRestoreJobResponse,
    BackupDescribeScanJobRequest,
    BackupDescribeScanJobResponse,
    BackupDisassociateBackupVaultMpaApprovalTeamRequest,
    BackupDisassociateBackupVaultMpaApprovalTeamResponse,
    BackupDisassociateRecoveryPointFromParentRequest,
    BackupDisassociateRecoveryPointFromParentResponse,
    BackupDisassociateRecoveryPointRequest,
    BackupDisassociateRecoveryPointResponse,
    BackupExportBackupPlanTemplateRequest,
    BackupExportBackupPlanTemplateResponse,
    BackupGetBackupPlanFromJSONRequest,
    BackupGetBackupPlanFromJSONResponse,
    BackupGetBackupPlanFromTemplateRequest,
    BackupGetBackupPlanFromTemplateResponse,
    BackupGetBackupPlanRequest,
    BackupGetBackupPlanResponse,
    BackupGetBackupSelectionRequest,
    BackupGetBackupSelectionResponse,
    BackupGetBackupVaultAccessPolicyRequest,
    BackupGetBackupVaultAccessPolicyResponse,
    BackupGetBackupVaultNotificationsRequest,
    BackupGetBackupVaultNotificationsResponse,
    BackupGetLegalHoldRequest,
    BackupGetLegalHoldResponse,
    BackupGetPITRMalwareScanResultsRequest,
    BackupGetPITRMalwareScanResultsResponse,
    BackupGetRecoveryPointIndexDetailsRequest,
    BackupGetRecoveryPointIndexDetailsResponse,
    BackupGetRecoveryPointRestoreMetadataRequest,
    BackupGetRecoveryPointRestoreMetadataResponse,
    BackupGetRestoreJobMetadataRequest,
    BackupGetRestoreJobMetadataResponse,
    BackupGetRestoreTestingInferredMetadataRequest,
    BackupGetRestoreTestingInferredMetadataResponse,
    BackupGetRestoreTestingPlanRequest,
    BackupGetRestoreTestingPlanResponse,
    BackupGetRestoreTestingSelectionRequest,
    BackupGetRestoreTestingSelectionResponse,
    BackupGetSupportedResourceTypesRequest,
    BackupGetSupportedResourceTypesResponse,
    BackupGetTieringConfigurationRequest,
    BackupGetTieringConfigurationResponse,
    BackupListBackupAccessPointsByRecoveryPointRequest,
    BackupListBackupAccessPointsByRecoveryPointResponse,
    BackupListBackupAccessPointsByResourceRequest,
    BackupListBackupAccessPointsByResourceResponse,
    BackupListBackupAccessPointsRequest,
    BackupListBackupAccessPointsResponse,
    BackupListBackupJobSummariesRequest,
    BackupListBackupJobSummariesResponse,
    BackupListBackupJobsRequest,
    BackupListBackupJobsResponse,
    BackupListBackupPlanTemplatesRequest,
    BackupListBackupPlanTemplatesResponse,
    BackupListBackupPlanVersionsRequest,
    BackupListBackupPlanVersionsResponse,
    BackupListBackupPlansRequest,
    BackupListBackupPlansResponse,
    BackupListBackupSelectionsRequest,
    BackupListBackupSelectionsResponse,
    BackupListBackupVaultsRequest,
    BackupListBackupVaultsResponse,
    BackupListCopyJobSummariesRequest,
    BackupListCopyJobSummariesResponse,
    BackupListCopyJobsRequest,
    BackupListCopyJobsResponse,
    BackupListFrameworksRequest,
    BackupListFrameworksResponse,
    BackupListIndexedRecoveryPointsRequest,
    BackupListIndexedRecoveryPointsResponse,
    BackupListLegalHoldsRequest,
    BackupListLegalHoldsResponse,
    BackupListProtectedResourcesByBackupVaultRequest,
    BackupListProtectedResourcesByBackupVaultResponse,
    BackupListProtectedResourcesRequest,
    BackupListProtectedResourcesResponse,
    BackupListRecoveryPointsByBackupVaultRequest,
    BackupListRecoveryPointsByBackupVaultResponse,
    BackupListRecoveryPointsByLegalHoldRequest,
    BackupListRecoveryPointsByLegalHoldResponse,
    BackupListRecoveryPointsByResourceRequest,
    BackupListRecoveryPointsByResourceResponse,
    BackupListReportJobsRequest,
    BackupListReportJobsResponse,
    BackupListReportPlansRequest,
    BackupListReportPlansResponse,
    BackupListRestoreAccessBackupVaultsRequest,
    BackupListRestoreAccessBackupVaultsResponse,
    BackupListRestoreJobSummariesRequest,
    BackupListRestoreJobSummariesResponse,
    BackupListRestoreJobsByProtectedResourceRequest,
    BackupListRestoreJobsByProtectedResourceResponse,
    BackupListRestoreJobsRequest,
    BackupListRestoreJobsResponse,
    BackupListRestoreTestingPlansRequest,
    BackupListRestoreTestingPlansResponse,
    BackupListRestoreTestingSelectionsRequest,
    BackupListRestoreTestingSelectionsResponse,
    BackupListScanJobSummariesRequest,
    BackupListScanJobSummariesResponse,
    BackupListScanJobsRequest,
    BackupListScanJobsResponse,
    BackupListTagsRequest,
    BackupListTagsResponse,
    BackupListTieringConfigurationsRequest,
    BackupListTieringConfigurationsResponse,
    BackupPutBackupVaultAccessPolicyRequest,
    BackupPutBackupVaultAccessPolicyResponse,
    BackupPutBackupVaultLockConfigurationRequest,
    BackupPutBackupVaultLockConfigurationResponse,
    BackupPutBackupVaultNotificationsRequest,
    BackupPutBackupVaultNotificationsResponse,
    BackupPutRestoreValidationResultRequest,
    BackupPutRestoreValidationResultResponse,
    BackupRevokeRestoreAccessBackupVaultRequest,
    BackupRevokeRestoreAccessBackupVaultResponse,
    BackupStartBackupJobRequest,
    BackupStartBackupJobResponse,
    BackupStartCopyJobRequest,
    BackupStartCopyJobResponse,
    BackupStartReportJobRequest,
    BackupStartReportJobResponse,
    BackupStartRestoreJobRequest,
    BackupStartRestoreJobResponse,
    BackupStartScanJobRequest,
    BackupStartScanJobResponse,
    BackupStopBackupJobRequest,
    BackupStopBackupJobResponse,
    BackupTagResourceRequest,
    BackupTagResourceResponse,
    BackupUntagResourceRequest,
    BackupUntagResourceResponse,
    BackupUpdateBackupPlanRequest,
    BackupUpdateBackupPlanResponse,
    BackupUpdateFrameworkRequest,
    BackupUpdateFrameworkResponse,
    BackupUpdateGlobalSettingsRequest,
    BackupUpdateGlobalSettingsResponse,
    BackupUpdateRecoveryPointIndexSettingsRequest,
    BackupUpdateRecoveryPointIndexSettingsResponse,
    BackupUpdateRecoveryPointLifecycleRequest,
    BackupUpdateRecoveryPointLifecycleResponse,
    BackupUpdateRegionSettingsRequest,
    BackupUpdateRegionSettingsResponse,
    BackupUpdateReportPlanRequest,
    BackupUpdateReportPlanResponse,
    BackupUpdateRestoreTestingPlanRequest,
    BackupUpdateRestoreTestingPlanResponse,
    BackupUpdateRestoreTestingSelectionRequest,
    BackupUpdateRestoreTestingSelectionResponse,
    BackupUpdateTieringConfigurationRequest,
    BackupUpdateTieringConfigurationResponse,
)
from werkflow_aws.types.backup_client import BackupClient
from .base import AWSBaseService


class AWSBackup(AWSBaseService[BackupClient]):
    service_name = 'backup'
    boto3_service_name = 'backup'

    def __init__(self) -> None:
        super().__init__(service_name='backup', boto3_service_name='backup')

    async def associate_backup_vault_mpa_approval_team(
        self,
        request: BackupAssociateBackupVaultMpaApprovalTeamRequest,
    ) -> BackupAssociateBackupVaultMpaApprovalTeamResponse:
        client = self._require_client()
        return await self._execute(client.associate_backup_vault_mpa_approval_team, request, BackupAssociateBackupVaultMpaApprovalTeamResponse)

    async def cancel_legal_hold(
        self,
        request: BackupCancelLegalHoldRequest,
    ) -> BackupCancelLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.cancel_legal_hold, request, BackupCancelLegalHoldResponse)

    async def create_backup_access_point(
        self,
        request: BackupCreateBackupAccessPointRequest,
    ) -> BackupCreateBackupAccessPointResponse:
        client = self._require_client()
        return await self._execute(client.create_backup_access_point, request, BackupCreateBackupAccessPointResponse)

    async def create_backup_plan(
        self,
        request: BackupCreateBackupPlanRequest,
    ) -> BackupCreateBackupPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_backup_plan, request, BackupCreateBackupPlanResponse)

    async def create_backup_selection(
        self,
        request: BackupCreateBackupSelectionRequest,
    ) -> BackupCreateBackupSelectionResponse:
        client = self._require_client()
        return await self._execute(client.create_backup_selection, request, BackupCreateBackupSelectionResponse)

    async def create_backup_vault(
        self,
        request: BackupCreateBackupVaultRequest,
    ) -> BackupCreateBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.create_backup_vault, request, BackupCreateBackupVaultResponse)

    async def create_framework(
        self,
        request: BackupCreateFrameworkRequest,
    ) -> BackupCreateFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.create_framework, request, BackupCreateFrameworkResponse)

    async def create_legal_hold(
        self,
        request: BackupCreateLegalHoldRequest,
    ) -> BackupCreateLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.create_legal_hold, request, BackupCreateLegalHoldResponse)

    async def create_logically_air_gapped_backup_vault(
        self,
        request: BackupCreateLogicallyAirGappedBackupVaultRequest,
    ) -> BackupCreateLogicallyAirGappedBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.create_logically_air_gapped_backup_vault, request, BackupCreateLogicallyAirGappedBackupVaultResponse)

    async def create_report_plan(
        self,
        request: BackupCreateReportPlanRequest,
    ) -> BackupCreateReportPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_report_plan, request, BackupCreateReportPlanResponse)

    async def create_restore_access_backup_vault(
        self,
        request: BackupCreateRestoreAccessBackupVaultRequest,
    ) -> BackupCreateRestoreAccessBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.create_restore_access_backup_vault, request, BackupCreateRestoreAccessBackupVaultResponse)

    async def create_restore_testing_plan(
        self,
        request: BackupCreateRestoreTestingPlanRequest,
    ) -> BackupCreateRestoreTestingPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_restore_testing_plan, request, BackupCreateRestoreTestingPlanResponse)

    async def create_restore_testing_selection(
        self,
        request: BackupCreateRestoreTestingSelectionRequest,
    ) -> BackupCreateRestoreTestingSelectionResponse:
        client = self._require_client()
        return await self._execute(client.create_restore_testing_selection, request, BackupCreateRestoreTestingSelectionResponse)

    async def create_tiering_configuration(
        self,
        request: BackupCreateTieringConfigurationRequest,
    ) -> BackupCreateTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_tiering_configuration, request, BackupCreateTieringConfigurationResponse)

    async def delete_backup_access_point(
        self,
        request: BackupDeleteBackupAccessPointRequest,
    ) -> BackupDeleteBackupAccessPointResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_access_point, request, BackupDeleteBackupAccessPointResponse)

    async def delete_backup_plan(
        self,
        request: BackupDeleteBackupPlanRequest,
    ) -> BackupDeleteBackupPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_plan, request, BackupDeleteBackupPlanResponse)

    async def delete_backup_selection(
        self,
        request: BackupDeleteBackupSelectionRequest,
    ) -> BackupDeleteBackupSelectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_selection, request, BackupDeleteBackupSelectionResponse)

    async def delete_backup_vault(
        self,
        request: BackupDeleteBackupVaultRequest,
    ) -> BackupDeleteBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_vault, request, BackupDeleteBackupVaultResponse)

    async def delete_backup_vault_access_policy(
        self,
        request: BackupDeleteBackupVaultAccessPolicyRequest,
    ) -> BackupDeleteBackupVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_vault_access_policy, request, BackupDeleteBackupVaultAccessPolicyResponse)

    async def delete_backup_vault_lock_configuration(
        self,
        request: BackupDeleteBackupVaultLockConfigurationRequest,
    ) -> BackupDeleteBackupVaultLockConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_vault_lock_configuration, request, BackupDeleteBackupVaultLockConfigurationResponse)

    async def delete_backup_vault_notifications(
        self,
        request: BackupDeleteBackupVaultNotificationsRequest,
    ) -> BackupDeleteBackupVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup_vault_notifications, request, BackupDeleteBackupVaultNotificationsResponse)

    async def delete_framework(
        self,
        request: BackupDeleteFrameworkRequest,
    ) -> BackupDeleteFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.delete_framework, request, BackupDeleteFrameworkResponse)

    async def delete_recovery_point(
        self,
        request: BackupDeleteRecoveryPointRequest,
    ) -> BackupDeleteRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.delete_recovery_point, request, BackupDeleteRecoveryPointResponse)

    async def delete_report_plan(
        self,
        request: BackupDeleteReportPlanRequest,
    ) -> BackupDeleteReportPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_report_plan, request, BackupDeleteReportPlanResponse)

    async def delete_restore_testing_plan(
        self,
        request: BackupDeleteRestoreTestingPlanRequest,
    ) -> BackupDeleteRestoreTestingPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_restore_testing_plan, request, BackupDeleteRestoreTestingPlanResponse)

    async def delete_restore_testing_selection(
        self,
        request: BackupDeleteRestoreTestingSelectionRequest,
    ) -> BackupDeleteRestoreTestingSelectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_restore_testing_selection, request, BackupDeleteRestoreTestingSelectionResponse)

    async def delete_tiering_configuration(
        self,
        request: BackupDeleteTieringConfigurationRequest,
    ) -> BackupDeleteTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_tiering_configuration, request, BackupDeleteTieringConfigurationResponse)

    async def describe_backup_access_point(
        self,
        request: BackupDescribeBackupAccessPointRequest,
    ) -> BackupDescribeBackupAccessPointResponse:
        client = self._require_client()
        return await self._execute(client.describe_backup_access_point, request, BackupDescribeBackupAccessPointResponse)

    async def describe_backup_job(
        self,
        request: BackupDescribeBackupJobRequest,
    ) -> BackupDescribeBackupJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_backup_job, request, BackupDescribeBackupJobResponse)

    async def describe_backup_vault(
        self,
        request: BackupDescribeBackupVaultRequest,
    ) -> BackupDescribeBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.describe_backup_vault, request, BackupDescribeBackupVaultResponse)

    async def describe_copy_job(
        self,
        request: BackupDescribeCopyJobRequest,
    ) -> BackupDescribeCopyJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_copy_job, request, BackupDescribeCopyJobResponse)

    async def describe_framework(
        self,
        request: BackupDescribeFrameworkRequest,
    ) -> BackupDescribeFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.describe_framework, request, BackupDescribeFrameworkResponse)

    async def describe_global_settings(
        self,
        request: BackupDescribeGlobalSettingsRequest | None = None,
    ) -> BackupDescribeGlobalSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_settings, request, BackupDescribeGlobalSettingsResponse)

    async def describe_protected_resource(
        self,
        request: BackupDescribeProtectedResourceRequest,
    ) -> BackupDescribeProtectedResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_protected_resource, request, BackupDescribeProtectedResourceResponse)

    async def describe_recovery_point(
        self,
        request: BackupDescribeRecoveryPointRequest,
    ) -> BackupDescribeRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.describe_recovery_point, request, BackupDescribeRecoveryPointResponse)

    async def describe_region_settings(
        self,
        request: BackupDescribeRegionSettingsRequest | None = None,
    ) -> BackupDescribeRegionSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_region_settings, request, BackupDescribeRegionSettingsResponse)

    async def describe_report_job(
        self,
        request: BackupDescribeReportJobRequest,
    ) -> BackupDescribeReportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_report_job, request, BackupDescribeReportJobResponse)

    async def describe_report_plan(
        self,
        request: BackupDescribeReportPlanRequest,
    ) -> BackupDescribeReportPlanResponse:
        client = self._require_client()
        return await self._execute(client.describe_report_plan, request, BackupDescribeReportPlanResponse)

    async def describe_restore_job(
        self,
        request: BackupDescribeRestoreJobRequest,
    ) -> BackupDescribeRestoreJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_restore_job, request, BackupDescribeRestoreJobResponse)

    async def describe_scan_job(
        self,
        request: BackupDescribeScanJobRequest,
    ) -> BackupDescribeScanJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_scan_job, request, BackupDescribeScanJobResponse)

    async def disassociate_backup_vault_mpa_approval_team(
        self,
        request: BackupDisassociateBackupVaultMpaApprovalTeamRequest,
    ) -> BackupDisassociateBackupVaultMpaApprovalTeamResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_backup_vault_mpa_approval_team, request, BackupDisassociateBackupVaultMpaApprovalTeamResponse)

    async def disassociate_recovery_point(
        self,
        request: BackupDisassociateRecoveryPointRequest,
    ) -> BackupDisassociateRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_recovery_point, request, BackupDisassociateRecoveryPointResponse)

    async def disassociate_recovery_point_from_parent(
        self,
        request: BackupDisassociateRecoveryPointFromParentRequest,
    ) -> BackupDisassociateRecoveryPointFromParentResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_recovery_point_from_parent, request, BackupDisassociateRecoveryPointFromParentResponse)

    async def export_backup_plan_template(
        self,
        request: BackupExportBackupPlanTemplateRequest,
    ) -> BackupExportBackupPlanTemplateResponse:
        client = self._require_client()
        return await self._execute(client.export_backup_plan_template, request, BackupExportBackupPlanTemplateResponse)

    async def get_backup_plan(
        self,
        request: BackupGetBackupPlanRequest,
    ) -> BackupGetBackupPlanResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_plan, request, BackupGetBackupPlanResponse)

    async def get_backup_plan_from_json(
        self,
        request: BackupGetBackupPlanFromJSONRequest,
    ) -> BackupGetBackupPlanFromJSONResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_plan_from_json, request, BackupGetBackupPlanFromJSONResponse)

    async def get_backup_plan_from_template(
        self,
        request: BackupGetBackupPlanFromTemplateRequest,
    ) -> BackupGetBackupPlanFromTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_plan_from_template, request, BackupGetBackupPlanFromTemplateResponse)

    async def get_backup_selection(
        self,
        request: BackupGetBackupSelectionRequest,
    ) -> BackupGetBackupSelectionResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_selection, request, BackupGetBackupSelectionResponse)

    async def get_backup_vault_access_policy(
        self,
        request: BackupGetBackupVaultAccessPolicyRequest,
    ) -> BackupGetBackupVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_vault_access_policy, request, BackupGetBackupVaultAccessPolicyResponse)

    async def get_backup_vault_notifications(
        self,
        request: BackupGetBackupVaultNotificationsRequest,
    ) -> BackupGetBackupVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.get_backup_vault_notifications, request, BackupGetBackupVaultNotificationsResponse)

    async def get_legal_hold(
        self,
        request: BackupGetLegalHoldRequest,
    ) -> BackupGetLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.get_legal_hold, request, BackupGetLegalHoldResponse)

    async def get_pitr_malware_scan_results(
        self,
        request: BackupGetPITRMalwareScanResultsRequest,
    ) -> BackupGetPITRMalwareScanResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_pitr_malware_scan_results, request, BackupGetPITRMalwareScanResultsResponse)

    async def get_recovery_point_index_details(
        self,
        request: BackupGetRecoveryPointIndexDetailsRequest,
    ) -> BackupGetRecoveryPointIndexDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_recovery_point_index_details, request, BackupGetRecoveryPointIndexDetailsResponse)

    async def get_recovery_point_restore_metadata(
        self,
        request: BackupGetRecoveryPointRestoreMetadataRequest,
    ) -> BackupGetRecoveryPointRestoreMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_recovery_point_restore_metadata, request, BackupGetRecoveryPointRestoreMetadataResponse)

    async def get_restore_job_metadata(
        self,
        request: BackupGetRestoreJobMetadataRequest,
    ) -> BackupGetRestoreJobMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_restore_job_metadata, request, BackupGetRestoreJobMetadataResponse)

    async def get_restore_testing_inferred_metadata(
        self,
        request: BackupGetRestoreTestingInferredMetadataRequest,
    ) -> BackupGetRestoreTestingInferredMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_restore_testing_inferred_metadata, request, BackupGetRestoreTestingInferredMetadataResponse)

    async def get_restore_testing_plan(
        self,
        request: BackupGetRestoreTestingPlanRequest,
    ) -> BackupGetRestoreTestingPlanResponse:
        client = self._require_client()
        return await self._execute(client.get_restore_testing_plan, request, BackupGetRestoreTestingPlanResponse)

    async def get_restore_testing_selection(
        self,
        request: BackupGetRestoreTestingSelectionRequest,
    ) -> BackupGetRestoreTestingSelectionResponse:
        client = self._require_client()
        return await self._execute(client.get_restore_testing_selection, request, BackupGetRestoreTestingSelectionResponse)

    async def get_supported_resource_types(
        self,
        request: BackupGetSupportedResourceTypesRequest | None = None,
    ) -> BackupGetSupportedResourceTypesResponse:
        client = self._require_client()
        return await self._execute(client.get_supported_resource_types, request, BackupGetSupportedResourceTypesResponse)

    async def get_tiering_configuration(
        self,
        request: BackupGetTieringConfigurationRequest,
    ) -> BackupGetTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_tiering_configuration, request, BackupGetTieringConfigurationResponse)

    async def list_backup_access_points(
        self,
        request: BackupListBackupAccessPointsRequest | None = None,
    ) -> BackupListBackupAccessPointsResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_access_points, request, BackupListBackupAccessPointsResponse)

    async def list_backup_access_points_paginated(
        self,
        request: BackupListBackupAccessPointsRequest | None = None,
    ) -> list[BackupListBackupAccessPointsResponse]:
        return await self._paginate('list_backup_access_points', request, BackupListBackupAccessPointsResponse)

    async def list_backup_access_points_by_recovery_point(
        self,
        request: BackupListBackupAccessPointsByRecoveryPointRequest,
    ) -> BackupListBackupAccessPointsByRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_access_points_by_recovery_point, request, BackupListBackupAccessPointsByRecoveryPointResponse)

    async def list_backup_access_points_by_recovery_point_paginated(
        self,
        request: BackupListBackupAccessPointsByRecoveryPointRequest,
    ) -> list[BackupListBackupAccessPointsByRecoveryPointResponse]:
        return await self._paginate('list_backup_access_points_by_recovery_point', request, BackupListBackupAccessPointsByRecoveryPointResponse)

    async def list_backup_access_points_by_resource(
        self,
        request: BackupListBackupAccessPointsByResourceRequest,
    ) -> BackupListBackupAccessPointsByResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_access_points_by_resource, request, BackupListBackupAccessPointsByResourceResponse)

    async def list_backup_access_points_by_resource_paginated(
        self,
        request: BackupListBackupAccessPointsByResourceRequest,
    ) -> list[BackupListBackupAccessPointsByResourceResponse]:
        return await self._paginate('list_backup_access_points_by_resource', request, BackupListBackupAccessPointsByResourceResponse)

    async def list_backup_job_summaries(
        self,
        request: BackupListBackupJobSummariesRequest | None = None,
    ) -> BackupListBackupJobSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_job_summaries, request, BackupListBackupJobSummariesResponse)

    async def list_backup_jobs(
        self,
        request: BackupListBackupJobsRequest | None = None,
    ) -> BackupListBackupJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_jobs, request, BackupListBackupJobsResponse)

    async def list_backup_jobs_paginated(
        self,
        request: BackupListBackupJobsRequest | None = None,
    ) -> list[BackupListBackupJobsResponse]:
        return await self._paginate('list_backup_jobs', request, BackupListBackupJobsResponse)

    async def list_backup_plan_templates(
        self,
        request: BackupListBackupPlanTemplatesRequest | None = None,
    ) -> BackupListBackupPlanTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_plan_templates, request, BackupListBackupPlanTemplatesResponse)

    async def list_backup_plan_templates_paginated(
        self,
        request: BackupListBackupPlanTemplatesRequest | None = None,
    ) -> list[BackupListBackupPlanTemplatesResponse]:
        return await self._paginate('list_backup_plan_templates', request, BackupListBackupPlanTemplatesResponse)

    async def list_backup_plan_versions(
        self,
        request: BackupListBackupPlanVersionsRequest,
    ) -> BackupListBackupPlanVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_plan_versions, request, BackupListBackupPlanVersionsResponse)

    async def list_backup_plan_versions_paginated(
        self,
        request: BackupListBackupPlanVersionsRequest,
    ) -> list[BackupListBackupPlanVersionsResponse]:
        return await self._paginate('list_backup_plan_versions', request, BackupListBackupPlanVersionsResponse)

    async def list_backup_plans(
        self,
        request: BackupListBackupPlansRequest | None = None,
    ) -> BackupListBackupPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_plans, request, BackupListBackupPlansResponse)

    async def list_backup_plans_paginated(
        self,
        request: BackupListBackupPlansRequest | None = None,
    ) -> list[BackupListBackupPlansResponse]:
        return await self._paginate('list_backup_plans', request, BackupListBackupPlansResponse)

    async def list_backup_selections(
        self,
        request: BackupListBackupSelectionsRequest,
    ) -> BackupListBackupSelectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_selections, request, BackupListBackupSelectionsResponse)

    async def list_backup_selections_paginated(
        self,
        request: BackupListBackupSelectionsRequest,
    ) -> list[BackupListBackupSelectionsResponse]:
        return await self._paginate('list_backup_selections', request, BackupListBackupSelectionsResponse)

    async def list_backup_vaults(
        self,
        request: BackupListBackupVaultsRequest | None = None,
    ) -> BackupListBackupVaultsResponse:
        client = self._require_client()
        return await self._execute(client.list_backup_vaults, request, BackupListBackupVaultsResponse)

    async def list_backup_vaults_paginated(
        self,
        request: BackupListBackupVaultsRequest | None = None,
    ) -> list[BackupListBackupVaultsResponse]:
        return await self._paginate('list_backup_vaults', request, BackupListBackupVaultsResponse)

    async def list_copy_job_summaries(
        self,
        request: BackupListCopyJobSummariesRequest | None = None,
    ) -> BackupListCopyJobSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_copy_job_summaries, request, BackupListCopyJobSummariesResponse)

    async def list_copy_jobs(
        self,
        request: BackupListCopyJobsRequest | None = None,
    ) -> BackupListCopyJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_copy_jobs, request, BackupListCopyJobsResponse)

    async def list_copy_jobs_paginated(
        self,
        request: BackupListCopyJobsRequest | None = None,
    ) -> list[BackupListCopyJobsResponse]:
        return await self._paginate('list_copy_jobs', request, BackupListCopyJobsResponse)

    async def list_frameworks(
        self,
        request: BackupListFrameworksRequest | None = None,
    ) -> BackupListFrameworksResponse:
        client = self._require_client()
        return await self._execute(client.list_frameworks, request, BackupListFrameworksResponse)

    async def list_indexed_recovery_points(
        self,
        request: BackupListIndexedRecoveryPointsRequest | None = None,
    ) -> BackupListIndexedRecoveryPointsResponse:
        client = self._require_client()
        return await self._execute(client.list_indexed_recovery_points, request, BackupListIndexedRecoveryPointsResponse)

    async def list_indexed_recovery_points_paginated(
        self,
        request: BackupListIndexedRecoveryPointsRequest | None = None,
    ) -> list[BackupListIndexedRecoveryPointsResponse]:
        return await self._paginate('list_indexed_recovery_points', request, BackupListIndexedRecoveryPointsResponse)

    async def list_legal_holds(
        self,
        request: BackupListLegalHoldsRequest | None = None,
    ) -> BackupListLegalHoldsResponse:
        client = self._require_client()
        return await self._execute(client.list_legal_holds, request, BackupListLegalHoldsResponse)

    async def list_legal_holds_paginated(
        self,
        request: BackupListLegalHoldsRequest | None = None,
    ) -> list[BackupListLegalHoldsResponse]:
        return await self._paginate('list_legal_holds', request, BackupListLegalHoldsResponse)

    async def list_protected_resources(
        self,
        request: BackupListProtectedResourcesRequest | None = None,
    ) -> BackupListProtectedResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_protected_resources, request, BackupListProtectedResourcesResponse)

    async def list_protected_resources_paginated(
        self,
        request: BackupListProtectedResourcesRequest | None = None,
    ) -> list[BackupListProtectedResourcesResponse]:
        return await self._paginate('list_protected_resources', request, BackupListProtectedResourcesResponse)

    async def list_protected_resources_by_backup_vault(
        self,
        request: BackupListProtectedResourcesByBackupVaultRequest,
    ) -> BackupListProtectedResourcesByBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.list_protected_resources_by_backup_vault, request, BackupListProtectedResourcesByBackupVaultResponse)

    async def list_protected_resources_by_backup_vault_paginated(
        self,
        request: BackupListProtectedResourcesByBackupVaultRequest,
    ) -> list[BackupListProtectedResourcesByBackupVaultResponse]:
        return await self._paginate('list_protected_resources_by_backup_vault', request, BackupListProtectedResourcesByBackupVaultResponse)

    async def list_recovery_points_by_backup_vault(
        self,
        request: BackupListRecoveryPointsByBackupVaultRequest,
    ) -> BackupListRecoveryPointsByBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.list_recovery_points_by_backup_vault, request, BackupListRecoveryPointsByBackupVaultResponse)

    async def list_recovery_points_by_backup_vault_paginated(
        self,
        request: BackupListRecoveryPointsByBackupVaultRequest,
    ) -> list[BackupListRecoveryPointsByBackupVaultResponse]:
        return await self._paginate('list_recovery_points_by_backup_vault', request, BackupListRecoveryPointsByBackupVaultResponse)

    async def list_recovery_points_by_legal_hold(
        self,
        request: BackupListRecoveryPointsByLegalHoldRequest,
    ) -> BackupListRecoveryPointsByLegalHoldResponse:
        client = self._require_client()
        return await self._execute(client.list_recovery_points_by_legal_hold, request, BackupListRecoveryPointsByLegalHoldResponse)

    async def list_recovery_points_by_legal_hold_paginated(
        self,
        request: BackupListRecoveryPointsByLegalHoldRequest,
    ) -> list[BackupListRecoveryPointsByLegalHoldResponse]:
        return await self._paginate('list_recovery_points_by_legal_hold', request, BackupListRecoveryPointsByLegalHoldResponse)

    async def list_recovery_points_by_resource(
        self,
        request: BackupListRecoveryPointsByResourceRequest,
    ) -> BackupListRecoveryPointsByResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_recovery_points_by_resource, request, BackupListRecoveryPointsByResourceResponse)

    async def list_recovery_points_by_resource_paginated(
        self,
        request: BackupListRecoveryPointsByResourceRequest,
    ) -> list[BackupListRecoveryPointsByResourceResponse]:
        return await self._paginate('list_recovery_points_by_resource', request, BackupListRecoveryPointsByResourceResponse)

    async def list_report_jobs(
        self,
        request: BackupListReportJobsRequest | None = None,
    ) -> BackupListReportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_report_jobs, request, BackupListReportJobsResponse)

    async def list_report_plans(
        self,
        request: BackupListReportPlansRequest | None = None,
    ) -> BackupListReportPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_report_plans, request, BackupListReportPlansResponse)

    async def list_restore_access_backup_vaults(
        self,
        request: BackupListRestoreAccessBackupVaultsRequest,
    ) -> BackupListRestoreAccessBackupVaultsResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_access_backup_vaults, request, BackupListRestoreAccessBackupVaultsResponse)

    async def list_restore_access_backup_vaults_paginated(
        self,
        request: BackupListRestoreAccessBackupVaultsRequest,
    ) -> list[BackupListRestoreAccessBackupVaultsResponse]:
        return await self._paginate('list_restore_access_backup_vaults', request, BackupListRestoreAccessBackupVaultsResponse)

    async def list_restore_job_summaries(
        self,
        request: BackupListRestoreJobSummariesRequest | None = None,
    ) -> BackupListRestoreJobSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_job_summaries, request, BackupListRestoreJobSummariesResponse)

    async def list_restore_jobs(
        self,
        request: BackupListRestoreJobsRequest | None = None,
    ) -> BackupListRestoreJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_jobs, request, BackupListRestoreJobsResponse)

    async def list_restore_jobs_paginated(
        self,
        request: BackupListRestoreJobsRequest | None = None,
    ) -> list[BackupListRestoreJobsResponse]:
        return await self._paginate('list_restore_jobs', request, BackupListRestoreJobsResponse)

    async def list_restore_jobs_by_protected_resource(
        self,
        request: BackupListRestoreJobsByProtectedResourceRequest,
    ) -> BackupListRestoreJobsByProtectedResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_jobs_by_protected_resource, request, BackupListRestoreJobsByProtectedResourceResponse)

    async def list_restore_jobs_by_protected_resource_paginated(
        self,
        request: BackupListRestoreJobsByProtectedResourceRequest,
    ) -> list[BackupListRestoreJobsByProtectedResourceResponse]:
        return await self._paginate('list_restore_jobs_by_protected_resource', request, BackupListRestoreJobsByProtectedResourceResponse)

    async def list_restore_testing_plans(
        self,
        request: BackupListRestoreTestingPlansRequest | None = None,
    ) -> BackupListRestoreTestingPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_testing_plans, request, BackupListRestoreTestingPlansResponse)

    async def list_restore_testing_plans_paginated(
        self,
        request: BackupListRestoreTestingPlansRequest | None = None,
    ) -> list[BackupListRestoreTestingPlansResponse]:
        return await self._paginate('list_restore_testing_plans', request, BackupListRestoreTestingPlansResponse)

    async def list_restore_testing_selections(
        self,
        request: BackupListRestoreTestingSelectionsRequest,
    ) -> BackupListRestoreTestingSelectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_restore_testing_selections, request, BackupListRestoreTestingSelectionsResponse)

    async def list_restore_testing_selections_paginated(
        self,
        request: BackupListRestoreTestingSelectionsRequest,
    ) -> list[BackupListRestoreTestingSelectionsResponse]:
        return await self._paginate('list_restore_testing_selections', request, BackupListRestoreTestingSelectionsResponse)

    async def list_scan_job_summaries(
        self,
        request: BackupListScanJobSummariesRequest | None = None,
    ) -> BackupListScanJobSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_scan_job_summaries, request, BackupListScanJobSummariesResponse)

    async def list_scan_job_summaries_paginated(
        self,
        request: BackupListScanJobSummariesRequest | None = None,
    ) -> list[BackupListScanJobSummariesResponse]:
        return await self._paginate('list_scan_job_summaries', request, BackupListScanJobSummariesResponse)

    async def list_scan_jobs(
        self,
        request: BackupListScanJobsRequest | None = None,
    ) -> BackupListScanJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_scan_jobs, request, BackupListScanJobsResponse)

    async def list_scan_jobs_paginated(
        self,
        request: BackupListScanJobsRequest | None = None,
    ) -> list[BackupListScanJobsResponse]:
        return await self._paginate('list_scan_jobs', request, BackupListScanJobsResponse)

    async def list_tags(
        self,
        request: BackupListTagsRequest,
    ) -> BackupListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, BackupListTagsResponse)

    async def list_tiering_configurations(
        self,
        request: BackupListTieringConfigurationsRequest | None = None,
    ) -> BackupListTieringConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_tiering_configurations, request, BackupListTieringConfigurationsResponse)

    async def list_tiering_configurations_paginated(
        self,
        request: BackupListTieringConfigurationsRequest | None = None,
    ) -> list[BackupListTieringConfigurationsResponse]:
        return await self._paginate('list_tiering_configurations', request, BackupListTieringConfigurationsResponse)

    async def put_backup_vault_access_policy(
        self,
        request: BackupPutBackupVaultAccessPolicyRequest,
    ) -> BackupPutBackupVaultAccessPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_backup_vault_access_policy, request, BackupPutBackupVaultAccessPolicyResponse)

    async def put_backup_vault_lock_configuration(
        self,
        request: BackupPutBackupVaultLockConfigurationRequest,
    ) -> BackupPutBackupVaultLockConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_backup_vault_lock_configuration, request, BackupPutBackupVaultLockConfigurationResponse)

    async def put_backup_vault_notifications(
        self,
        request: BackupPutBackupVaultNotificationsRequest,
    ) -> BackupPutBackupVaultNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.put_backup_vault_notifications, request, BackupPutBackupVaultNotificationsResponse)

    async def put_restore_validation_result(
        self,
        request: BackupPutRestoreValidationResultRequest,
    ) -> BackupPutRestoreValidationResultResponse:
        client = self._require_client()
        return await self._execute(client.put_restore_validation_result, request, BackupPutRestoreValidationResultResponse)

    async def revoke_restore_access_backup_vault(
        self,
        request: BackupRevokeRestoreAccessBackupVaultRequest,
    ) -> BackupRevokeRestoreAccessBackupVaultResponse:
        client = self._require_client()
        return await self._execute(client.revoke_restore_access_backup_vault, request, BackupRevokeRestoreAccessBackupVaultResponse)

    async def start_backup_job(
        self,
        request: BackupStartBackupJobRequest,
    ) -> BackupStartBackupJobResponse:
        client = self._require_client()
        return await self._execute(client.start_backup_job, request, BackupStartBackupJobResponse)

    async def start_copy_job(
        self,
        request: BackupStartCopyJobRequest,
    ) -> BackupStartCopyJobResponse:
        client = self._require_client()
        return await self._execute(client.start_copy_job, request, BackupStartCopyJobResponse)

    async def start_report_job(
        self,
        request: BackupStartReportJobRequest,
    ) -> BackupStartReportJobResponse:
        client = self._require_client()
        return await self._execute(client.start_report_job, request, BackupStartReportJobResponse)

    async def start_restore_job(
        self,
        request: BackupStartRestoreJobRequest,
    ) -> BackupStartRestoreJobResponse:
        client = self._require_client()
        return await self._execute(client.start_restore_job, request, BackupStartRestoreJobResponse)

    async def start_scan_job(
        self,
        request: BackupStartScanJobRequest,
    ) -> BackupStartScanJobResponse:
        client = self._require_client()
        return await self._execute(client.start_scan_job, request, BackupStartScanJobResponse)

    async def stop_backup_job(
        self,
        request: BackupStopBackupJobRequest,
    ) -> BackupStopBackupJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_backup_job, request, BackupStopBackupJobResponse)

    async def tag_resource(
        self,
        request: BackupTagResourceRequest,
    ) -> BackupTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, BackupTagResourceResponse)

    async def untag_resource(
        self,
        request: BackupUntagResourceRequest,
    ) -> BackupUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, BackupUntagResourceResponse)

    async def update_backup_plan(
        self,
        request: BackupUpdateBackupPlanRequest,
    ) -> BackupUpdateBackupPlanResponse:
        client = self._require_client()
        return await self._execute(client.update_backup_plan, request, BackupUpdateBackupPlanResponse)

    async def update_framework(
        self,
        request: BackupUpdateFrameworkRequest,
    ) -> BackupUpdateFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.update_framework, request, BackupUpdateFrameworkResponse)

    async def update_global_settings(
        self,
        request: BackupUpdateGlobalSettingsRequest | None = None,
    ) -> BackupUpdateGlobalSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_global_settings, request, BackupUpdateGlobalSettingsResponse)

    async def update_recovery_point_index_settings(
        self,
        request: BackupUpdateRecoveryPointIndexSettingsRequest,
    ) -> BackupUpdateRecoveryPointIndexSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_recovery_point_index_settings, request, BackupUpdateRecoveryPointIndexSettingsResponse)

    async def update_recovery_point_lifecycle(
        self,
        request: BackupUpdateRecoveryPointLifecycleRequest,
    ) -> BackupUpdateRecoveryPointLifecycleResponse:
        client = self._require_client()
        return await self._execute(client.update_recovery_point_lifecycle, request, BackupUpdateRecoveryPointLifecycleResponse)

    async def update_region_settings(
        self,
        request: BackupUpdateRegionSettingsRequest | None = None,
    ) -> BackupUpdateRegionSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_region_settings, request, BackupUpdateRegionSettingsResponse)

    async def update_report_plan(
        self,
        request: BackupUpdateReportPlanRequest,
    ) -> BackupUpdateReportPlanResponse:
        client = self._require_client()
        return await self._execute(client.update_report_plan, request, BackupUpdateReportPlanResponse)

    async def update_restore_testing_plan(
        self,
        request: BackupUpdateRestoreTestingPlanRequest,
    ) -> BackupUpdateRestoreTestingPlanResponse:
        client = self._require_client()
        return await self._execute(client.update_restore_testing_plan, request, BackupUpdateRestoreTestingPlanResponse)

    async def update_restore_testing_selection(
        self,
        request: BackupUpdateRestoreTestingSelectionRequest,
    ) -> BackupUpdateRestoreTestingSelectionResponse:
        client = self._require_client()
        return await self._execute(client.update_restore_testing_selection, request, BackupUpdateRestoreTestingSelectionResponse)

    async def update_tiering_configuration(
        self,
        request: BackupUpdateTieringConfigurationRequest,
    ) -> BackupUpdateTieringConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_tiering_configuration, request, BackupUpdateTieringConfigurationResponse)
