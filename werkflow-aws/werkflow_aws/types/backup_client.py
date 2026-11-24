from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class BackupClient(ABC):

    @abstractmethod
    def associate_backup_vault_mpa_approval_team(
        self,
        *,
        BackupVaultName: str,
        MpaApprovalTeamArn: str,
        RequesterComment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_legal_hold(
        self,
        *,
        LegalHoldId: str,
        CancelDescription: str,
        RetainRecordInDays: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup_access_point(
        self,
        *,
        Name: str,
        RecoveryPointArn: str,
        AccessPointMetadata: dict[str, str] | None = None,
        AccessPointPolicy: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup_plan(
        self,
        *,
        BackupPlan: dict[str, Any],
        BackupPlanTags: dict[str, str] | None = None,
        CreatorRequestId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup_selection(
        self,
        *,
        BackupPlanId: str,
        BackupSelection: dict[str, Any],
        CreatorRequestId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultTags: dict[str, str] | None = None,
        EncryptionKeyArn: str | None = None,
        CreatorRequestId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkControls: list[dict[str, Any]],
        FrameworkDescription: str | None = None,
        IdempotencyToken: str | None = None,
        FrameworkTags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_legal_hold(
        self,
        *,
        Title: str,
        Description: str,
        IdempotencyToken: str | None = None,
        RecoveryPointSelection: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_logically_air_gapped_backup_vault(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int,
        MaxRetentionDays: int,
        BackupVaultTags: dict[str, str] | None = None,
        CreatorRequestId: str | None = None,
        EncryptionKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportDeliveryChannel: dict[str, Any],
        ReportSetting: dict[str, Any],
        ReportPlanDescription: str | None = None,
        ReportPlanTags: dict[str, str] | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_restore_access_backup_vault(
        self,
        *,
        SourceBackupVaultArn: str,
        BackupVaultName: str | None = None,
        BackupVaultTags: dict[str, str] | None = None,
        CreatorRequestId: str | None = None,
        RequesterComment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_restore_testing_plan(
        self,
        *,
        RestoreTestingPlan: dict[str, Any],
        CreatorRequestId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: dict[str, Any],
        CreatorRequestId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tiering_configuration(
        self,
        *,
        TieringConfiguration: dict[str, Any],
        TieringConfigurationTags: dict[str, str] | None = None,
        CreatorRequestId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_access_point(
        self,
        *,
        AccessPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_plan(
        self,
        *,
        BackupPlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_selection(
        self,
        *,
        BackupPlanId: str,
        SelectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_vault(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_vault_access_policy(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_vault_lock_configuration(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup_vault_notifications(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_framework(
        self,
        *,
        FrameworkName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_recovery_point(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_report_plan(
        self,
        *,
        ReportPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_restore_testing_plan(
        self,
        *,
        RestoreTestingPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelectionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tiering_configuration(
        self,
        *,
        TieringConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backup_access_point(
        self,
        *,
        AccessPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backup_job(
        self,
        *,
        BackupJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_copy_job(
        self,
        *,
        CopyJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_framework(
        self,
        *,
        FrameworkName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_protected_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recovery_point(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
        BackupVaultAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_region_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_report_job(
        self,
        *,
        ReportJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_report_plan(
        self,
        *,
        ReportPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_restore_job(
        self,
        *,
        RestoreJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scan_job(
        self,
        *,
        ScanJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_backup_vault_mpa_approval_team(
        self,
        *,
        BackupVaultName: str,
        RequesterComment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_recovery_point(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_recovery_point_from_parent(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_backup_plan_template(
        self,
        *,
        BackupPlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_plan(
        self,
        *,
        BackupPlanId: str,
        VersionId: str | None = None,
        MaxScheduledRunsPreview: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_plan_from_json(
        self,
        *,
        BackupPlanTemplateJson: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_plan_from_template(
        self,
        *,
        BackupPlanTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_selection(
        self,
        *,
        BackupPlanId: str,
        SelectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_vault_access_policy(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backup_vault_notifications(
        self,
        *,
        BackupVaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_legal_hold(
        self,
        *,
        LegalHoldId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pitr_malware_scan_results(
        self,
        *,
        RecoveryPointArn: str,
        BackupVaultName: str,
        ScanEndTime: datetime.datetime | str,
        MalwareScanner: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recovery_point_index_details(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recovery_point_restore_metadata(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
        BackupVaultAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_restore_job_metadata(
        self,
        *,
        RestoreJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_restore_testing_inferred_metadata(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
        BackupVaultAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_restore_testing_plan(
        self,
        *,
        RestoreTestingPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelectionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_resource_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tiering_configuration(
        self,
        *,
        TieringConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_access_points(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_access_points_by_recovery_point(
        self,
        *,
        RecoveryPointArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_access_points_by_resource(
        self,
        *,
        ResourceArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_job_summaries(
        self,
        *,
        AccountId: str | None = None,
        State: str | None = None,
        ResourceType: str | None = None,
        MessageCategory: str | None = None,
        AggregationPeriod: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ByResourceArn: str | None = None,
        ByState: str | None = None,
        ByBackupVaultName: str | None = None,
        ByCreatedBefore: datetime.datetime | str | None = None,
        ByCreatedAfter: datetime.datetime | str | None = None,
        ByResourceType: str | None = None,
        ByAccountId: str | None = None,
        ByCompleteAfter: datetime.datetime | str | None = None,
        ByCompleteBefore: datetime.datetime | str | None = None,
        ByParentJobId: str | None = None,
        ByMessageCategory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_plan_templates(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_plan_versions(
        self,
        *,
        BackupPlanId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_plans(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IncludeDeleted: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_selections(
        self,
        *,
        BackupPlanId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backup_vaults(
        self,
        *,
        ByVaultType: str | None = None,
        ByShared: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_copy_job_summaries(
        self,
        *,
        AccountId: str | None = None,
        State: str | None = None,
        ResourceType: str | None = None,
        MessageCategory: str | None = None,
        AggregationPeriod: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_copy_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ByResourceArn: str | None = None,
        ByState: str | None = None,
        ByCreatedBefore: datetime.datetime | str | None = None,
        ByCreatedAfter: datetime.datetime | str | None = None,
        ByResourceType: str | None = None,
        ByDestinationVaultArn: str | None = None,
        ByAccountId: str | None = None,
        ByCompleteBefore: datetime.datetime | str | None = None,
        ByCompleteAfter: datetime.datetime | str | None = None,
        ByParentJobId: str | None = None,
        ByMessageCategory: str | None = None,
        BySourceRecoveryPointArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_frameworks(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_indexed_recovery_points(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SourceResourceArn: str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        ResourceType: str | None = None,
        IndexStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_legal_holds(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_protected_resources(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_protected_resources_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recovery_points_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ByResourceArn: str | None = None,
        ByResourceType: str | None = None,
        ByBackupPlanId: str | None = None,
        ByCreatedBefore: datetime.datetime | str | None = None,
        ByCreatedAfter: datetime.datetime | str | None = None,
        ByParentRecoveryPointArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recovery_points_by_legal_hold(
        self,
        *,
        LegalHoldId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recovery_points_by_resource(
        self,
        *,
        ResourceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ManagedByAWSBackupOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_report_jobs(
        self,
        *,
        ByReportPlanName: str | None = None,
        ByCreationBefore: datetime.datetime | str | None = None,
        ByCreationAfter: datetime.datetime | str | None = None,
        ByStatus: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_report_plans(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_access_backup_vaults(
        self,
        *,
        BackupVaultName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_job_summaries(
        self,
        *,
        AccountId: str | None = None,
        State: str | None = None,
        ResourceType: str | None = None,
        AggregationPeriod: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ByAccountId: str | None = None,
        ByResourceType: str | None = None,
        ByCreatedBefore: datetime.datetime | str | None = None,
        ByCreatedAfter: datetime.datetime | str | None = None,
        ByStatus: str | None = None,
        ByCompleteBefore: datetime.datetime | str | None = None,
        ByCompleteAfter: datetime.datetime | str | None = None,
        ByRestoreTestingPlanArn: str | None = None,
        ByParentJobId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_jobs_by_protected_resource(
        self,
        *,
        ResourceArn: str,
        ByStatus: str | None = None,
        ByRecoveryPointCreationDateAfter: datetime.datetime | str | None = None,
        ByRecoveryPointCreationDateBefore: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_testing_plans(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_restore_testing_selections(
        self,
        *,
        RestoreTestingPlanName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scan_job_summaries(
        self,
        *,
        AccountId: str | None = None,
        ResourceType: str | None = None,
        MalwareScanner: str | None = None,
        ScanResultStatus: str | None = None,
        State: str | None = None,
        AggregationPeriod: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scan_jobs(
        self,
        *,
        ByAccountId: str | None = None,
        ByBackupVaultName: str | None = None,
        ByCompleteAfter: datetime.datetime | str | None = None,
        ByCompleteBefore: datetime.datetime | str | None = None,
        ByMalwareScanner: str | None = None,
        ByRecoveryPointArn: str | None = None,
        ByResourceArn: str | None = None,
        ByResourceType: str | None = None,
        ByScanResultStatus: str | None = None,
        ByState: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tiering_configurations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_backup_vault_access_policy(
        self,
        *,
        BackupVaultName: str,
        Policy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_backup_vault_lock_configuration(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int | None = None,
        MaxRetentionDays: int | None = None,
        ChangeableForDays: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_backup_vault_notifications(
        self,
        *,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_restore_validation_result(
        self,
        *,
        RestoreJobId: str,
        ValidationStatus: str,
        ValidationStatusMessage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_restore_access_backup_vault(
        self,
        *,
        BackupVaultName: str,
        RestoreAccessBackupVaultArn: str,
        RequesterComment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_backup_job(
        self,
        *,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        LogicallyAirGappedBackupVaultArn: str | None = None,
        IdempotencyToken: str | None = None,
        StartWindowMinutes: int | None = None,
        CompleteWindowMinutes: int | None = None,
        Lifecycle: dict[str, Any] | None = None,
        RecoveryPointTags: dict[str, str] | None = None,
        BackupOptions: dict[str, str] | None = None,
        Index: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_copy_job(
        self,
        *,
        RecoveryPointArn: str,
        SourceBackupVaultName: str,
        DestinationBackupVaultArn: str,
        IamRoleArn: str,
        IdempotencyToken: str | None = None,
        Lifecycle: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_report_job(
        self,
        *,
        ReportPlanName: str,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_restore_job(
        self,
        *,
        RecoveryPointArn: str,
        Metadata: dict[str, str],
        IamRoleArn: str | None = None,
        IdempotencyToken: str | None = None,
        ResourceType: str | None = None,
        CopySourceTagsToRestoredResource: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_scan_job(
        self,
        *,
        BackupVaultName: str,
        IamRoleArn: str,
        MalwareScanner: str,
        RecoveryPointArn: str,
        ScanMode: str,
        ScannerRoleArn: str,
        ContinuousScanEndTime: datetime.datetime | str | None = None,
        IdempotencyToken: str | None = None,
        ScanBaseRecoveryPointArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_backup_job(
        self,
        *,
        BackupJobId: str,
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
        TagKeyList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_backup_plan(
        self,
        *,
        BackupPlanId: str,
        BackupPlan: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkDescription: str | None = None,
        FrameworkControls: list[dict[str, Any]] | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_global_settings(
        self,
        *,
        GlobalSettings: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_recovery_point_index_settings(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
        Index: str,
        IamRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_recovery_point_lifecycle(
        self,
        *,
        BackupVaultName: str,
        RecoveryPointArn: str,
        Lifecycle: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_region_settings(
        self,
        *,
        ResourceTypeOptInPreference: dict[str, bool] | None = None,
        ResourceTypeManagementPreference: dict[str, bool] | None = None,
        ResourceTypeOptInIncremental: dict[str, bool] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportPlanDescription: str | None = None,
        ReportDeliveryChannel: dict[str, Any] | None = None,
        ReportSetting: dict[str, Any] | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_restore_testing_plan(
        self,
        *,
        RestoreTestingPlan: dict[str, Any],
        RestoreTestingPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: dict[str, Any],
        RestoreTestingSelectionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_tiering_configuration(
        self,
        *,
        TieringConfigurationName: str,
        TieringConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
