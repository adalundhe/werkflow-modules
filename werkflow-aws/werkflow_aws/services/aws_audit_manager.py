from werkflow_aws.models.audit_manager import (
    AuditManagerAssociateAssessmentReportEvidenceFolderRequest,
    AuditManagerAssociateAssessmentReportEvidenceFolderResponse,
    AuditManagerBatchAssociateAssessmentReportEvidenceRequest,
    AuditManagerBatchAssociateAssessmentReportEvidenceResponse,
    AuditManagerBatchCreateDelegationByAssessmentRequest,
    AuditManagerBatchCreateDelegationByAssessmentResponse,
    AuditManagerBatchDeleteDelegationByAssessmentRequest,
    AuditManagerBatchDeleteDelegationByAssessmentResponse,
    AuditManagerBatchDisassociateAssessmentReportEvidenceRequest,
    AuditManagerBatchDisassociateAssessmentReportEvidenceResponse,
    AuditManagerBatchImportEvidenceToAssessmentControlRequest,
    AuditManagerBatchImportEvidenceToAssessmentControlResponse,
    AuditManagerCreateAssessmentFrameworkRequest,
    AuditManagerCreateAssessmentFrameworkResponse,
    AuditManagerCreateAssessmentReportRequest,
    AuditManagerCreateAssessmentReportResponse,
    AuditManagerCreateAssessmentRequest,
    AuditManagerCreateAssessmentResponse,
    AuditManagerCreateControlRequest,
    AuditManagerCreateControlResponse,
    AuditManagerDeleteAssessmentFrameworkRequest,
    AuditManagerDeleteAssessmentFrameworkResponse,
    AuditManagerDeleteAssessmentFrameworkShareRequest,
    AuditManagerDeleteAssessmentFrameworkShareResponse,
    AuditManagerDeleteAssessmentReportRequest,
    AuditManagerDeleteAssessmentReportResponse,
    AuditManagerDeleteAssessmentRequest,
    AuditManagerDeleteAssessmentResponse,
    AuditManagerDeleteControlRequest,
    AuditManagerDeleteControlResponse,
    AuditManagerDeregisterAccountRequest,
    AuditManagerDeregisterAccountResponse,
    AuditManagerDeregisterOrganizationAdminAccountRequest,
    AuditManagerDeregisterOrganizationAdminAccountResponse,
    AuditManagerDisassociateAssessmentReportEvidenceFolderRequest,
    AuditManagerDisassociateAssessmentReportEvidenceFolderResponse,
    AuditManagerGetAccountStatusRequest,
    AuditManagerGetAccountStatusResponse,
    AuditManagerGetAssessmentFrameworkRequest,
    AuditManagerGetAssessmentFrameworkResponse,
    AuditManagerGetAssessmentReportUrlRequest,
    AuditManagerGetAssessmentReportUrlResponse,
    AuditManagerGetAssessmentRequest,
    AuditManagerGetAssessmentResponse,
    AuditManagerGetChangeLogsRequest,
    AuditManagerGetChangeLogsResponse,
    AuditManagerGetControlRequest,
    AuditManagerGetControlResponse,
    AuditManagerGetDelegationsRequest,
    AuditManagerGetDelegationsResponse,
    AuditManagerGetEvidenceByEvidenceFolderRequest,
    AuditManagerGetEvidenceByEvidenceFolderResponse,
    AuditManagerGetEvidenceFileUploadUrlRequest,
    AuditManagerGetEvidenceFileUploadUrlResponse,
    AuditManagerGetEvidenceFolderRequest,
    AuditManagerGetEvidenceFolderResponse,
    AuditManagerGetEvidenceFoldersByAssessmentControlRequest,
    AuditManagerGetEvidenceFoldersByAssessmentControlResponse,
    AuditManagerGetEvidenceFoldersByAssessmentRequest,
    AuditManagerGetEvidenceFoldersByAssessmentResponse,
    AuditManagerGetEvidenceRequest,
    AuditManagerGetEvidenceResponse,
    AuditManagerGetInsightsByAssessmentRequest,
    AuditManagerGetInsightsByAssessmentResponse,
    AuditManagerGetInsightsRequest,
    AuditManagerGetInsightsResponse,
    AuditManagerGetOrganizationAdminAccountRequest,
    AuditManagerGetOrganizationAdminAccountResponse,
    AuditManagerGetServicesInScopeRequest,
    AuditManagerGetServicesInScopeResponse,
    AuditManagerGetSettingsRequest,
    AuditManagerGetSettingsResponse,
    AuditManagerListAssessmentControlInsightsByControlDomainRequest,
    AuditManagerListAssessmentControlInsightsByControlDomainResponse,
    AuditManagerListAssessmentFrameworkShareRequestsRequest,
    AuditManagerListAssessmentFrameworkShareRequestsResponse,
    AuditManagerListAssessmentFrameworksRequest,
    AuditManagerListAssessmentFrameworksResponse,
    AuditManagerListAssessmentReportsRequest,
    AuditManagerListAssessmentReportsResponse,
    AuditManagerListAssessmentsRequest,
    AuditManagerListAssessmentsResponse,
    AuditManagerListControlDomainInsightsByAssessmentRequest,
    AuditManagerListControlDomainInsightsByAssessmentResponse,
    AuditManagerListControlDomainInsightsRequest,
    AuditManagerListControlDomainInsightsResponse,
    AuditManagerListControlInsightsByControlDomainRequest,
    AuditManagerListControlInsightsByControlDomainResponse,
    AuditManagerListControlsRequest,
    AuditManagerListControlsResponse,
    AuditManagerListKeywordsForDataSourceRequest,
    AuditManagerListKeywordsForDataSourceResponse,
    AuditManagerListNotificationsRequest,
    AuditManagerListNotificationsResponse,
    AuditManagerListTagsForResourceRequest,
    AuditManagerListTagsForResourceResponse,
    AuditManagerRegisterAccountRequest,
    AuditManagerRegisterAccountResponse,
    AuditManagerRegisterOrganizationAdminAccountRequest,
    AuditManagerRegisterOrganizationAdminAccountResponse,
    AuditManagerStartAssessmentFrameworkShareRequest,
    AuditManagerStartAssessmentFrameworkShareResponse,
    AuditManagerTagResourceRequest,
    AuditManagerTagResourceResponse,
    AuditManagerUntagResourceRequest,
    AuditManagerUntagResourceResponse,
    AuditManagerUpdateAssessmentControlRequest,
    AuditManagerUpdateAssessmentControlResponse,
    AuditManagerUpdateAssessmentControlSetStatusRequest,
    AuditManagerUpdateAssessmentControlSetStatusResponse,
    AuditManagerUpdateAssessmentFrameworkRequest,
    AuditManagerUpdateAssessmentFrameworkResponse,
    AuditManagerUpdateAssessmentFrameworkShareRequest,
    AuditManagerUpdateAssessmentFrameworkShareResponse,
    AuditManagerUpdateAssessmentRequest,
    AuditManagerUpdateAssessmentResponse,
    AuditManagerUpdateAssessmentStatusRequest,
    AuditManagerUpdateAssessmentStatusResponse,
    AuditManagerUpdateControlRequest,
    AuditManagerUpdateControlResponse,
    AuditManagerUpdateSettingsRequest,
    AuditManagerUpdateSettingsResponse,
    AuditManagerValidateAssessmentReportIntegrityRequest,
    AuditManagerValidateAssessmentReportIntegrityResponse,
)
from werkflow_aws.types.audit_manager_client import AuditManagerClient
from .base import AWSBaseService


class AWSAuditManager(AWSBaseService[AuditManagerClient]):
    service_name = 'audit-manager'
    boto3_service_name = 'auditmanager'

    def __init__(self) -> None:
        super().__init__(service_name='audit-manager', boto3_service_name='auditmanager')

    async def associate_assessment_report_evidence_folder(
        self,
        request: AuditManagerAssociateAssessmentReportEvidenceFolderRequest,
    ) -> AuditManagerAssociateAssessmentReportEvidenceFolderResponse:
        client = self._require_client()
        return await self._execute(client.associate_assessment_report_evidence_folder, request, AuditManagerAssociateAssessmentReportEvidenceFolderResponse)

    async def batch_associate_assessment_report_evidence(
        self,
        request: AuditManagerBatchAssociateAssessmentReportEvidenceRequest,
    ) -> AuditManagerBatchAssociateAssessmentReportEvidenceResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_assessment_report_evidence, request, AuditManagerBatchAssociateAssessmentReportEvidenceResponse)

    async def batch_create_delegation_by_assessment(
        self,
        request: AuditManagerBatchCreateDelegationByAssessmentRequest,
    ) -> AuditManagerBatchCreateDelegationByAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.batch_create_delegation_by_assessment, request, AuditManagerBatchCreateDelegationByAssessmentResponse)

    async def batch_delete_delegation_by_assessment(
        self,
        request: AuditManagerBatchDeleteDelegationByAssessmentRequest,
    ) -> AuditManagerBatchDeleteDelegationByAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_delegation_by_assessment, request, AuditManagerBatchDeleteDelegationByAssessmentResponse)

    async def batch_disassociate_assessment_report_evidence(
        self,
        request: AuditManagerBatchDisassociateAssessmentReportEvidenceRequest,
    ) -> AuditManagerBatchDisassociateAssessmentReportEvidenceResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_assessment_report_evidence, request, AuditManagerBatchDisassociateAssessmentReportEvidenceResponse)

    async def batch_import_evidence_to_assessment_control(
        self,
        request: AuditManagerBatchImportEvidenceToAssessmentControlRequest,
    ) -> AuditManagerBatchImportEvidenceToAssessmentControlResponse:
        client = self._require_client()
        return await self._execute(client.batch_import_evidence_to_assessment_control, request, AuditManagerBatchImportEvidenceToAssessmentControlResponse)

    async def create_assessment(
        self,
        request: AuditManagerCreateAssessmentRequest,
    ) -> AuditManagerCreateAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.create_assessment, request, AuditManagerCreateAssessmentResponse)

    async def create_assessment_framework(
        self,
        request: AuditManagerCreateAssessmentFrameworkRequest,
    ) -> AuditManagerCreateAssessmentFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.create_assessment_framework, request, AuditManagerCreateAssessmentFrameworkResponse)

    async def create_assessment_report(
        self,
        request: AuditManagerCreateAssessmentReportRequest,
    ) -> AuditManagerCreateAssessmentReportResponse:
        client = self._require_client()
        return await self._execute(client.create_assessment_report, request, AuditManagerCreateAssessmentReportResponse)

    async def create_control(
        self,
        request: AuditManagerCreateControlRequest,
    ) -> AuditManagerCreateControlResponse:
        client = self._require_client()
        return await self._execute(client.create_control, request, AuditManagerCreateControlResponse)

    async def delete_assessment(
        self,
        request: AuditManagerDeleteAssessmentRequest,
    ) -> AuditManagerDeleteAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_assessment, request, AuditManagerDeleteAssessmentResponse)

    async def delete_assessment_framework(
        self,
        request: AuditManagerDeleteAssessmentFrameworkRequest,
    ) -> AuditManagerDeleteAssessmentFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.delete_assessment_framework, request, AuditManagerDeleteAssessmentFrameworkResponse)

    async def delete_assessment_framework_share(
        self,
        request: AuditManagerDeleteAssessmentFrameworkShareRequest,
    ) -> AuditManagerDeleteAssessmentFrameworkShareResponse:
        client = self._require_client()
        return await self._execute(client.delete_assessment_framework_share, request, AuditManagerDeleteAssessmentFrameworkShareResponse)

    async def delete_assessment_report(
        self,
        request: AuditManagerDeleteAssessmentReportRequest,
    ) -> AuditManagerDeleteAssessmentReportResponse:
        client = self._require_client()
        return await self._execute(client.delete_assessment_report, request, AuditManagerDeleteAssessmentReportResponse)

    async def delete_control(
        self,
        request: AuditManagerDeleteControlRequest,
    ) -> AuditManagerDeleteControlResponse:
        client = self._require_client()
        return await self._execute(client.delete_control, request, AuditManagerDeleteControlResponse)

    async def deregister_account(
        self,
        request: AuditManagerDeregisterAccountRequest | None = None,
    ) -> AuditManagerDeregisterAccountResponse:
        client = self._require_client()
        return await self._execute(client.deregister_account, request, AuditManagerDeregisterAccountResponse)

    async def deregister_organization_admin_account(
        self,
        request: AuditManagerDeregisterOrganizationAdminAccountRequest | None = None,
    ) -> AuditManagerDeregisterOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.deregister_organization_admin_account, request, AuditManagerDeregisterOrganizationAdminAccountResponse)

    async def disassociate_assessment_report_evidence_folder(
        self,
        request: AuditManagerDisassociateAssessmentReportEvidenceFolderRequest,
    ) -> AuditManagerDisassociateAssessmentReportEvidenceFolderResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_assessment_report_evidence_folder, request, AuditManagerDisassociateAssessmentReportEvidenceFolderResponse)

    async def get_account_status(
        self,
        request: AuditManagerGetAccountStatusRequest | None = None,
    ) -> AuditManagerGetAccountStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_account_status, request, AuditManagerGetAccountStatusResponse)

    async def get_assessment(
        self,
        request: AuditManagerGetAssessmentRequest,
    ) -> AuditManagerGetAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.get_assessment, request, AuditManagerGetAssessmentResponse)

    async def get_assessment_framework(
        self,
        request: AuditManagerGetAssessmentFrameworkRequest,
    ) -> AuditManagerGetAssessmentFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.get_assessment_framework, request, AuditManagerGetAssessmentFrameworkResponse)

    async def get_assessment_report_url(
        self,
        request: AuditManagerGetAssessmentReportUrlRequest,
    ) -> AuditManagerGetAssessmentReportUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_assessment_report_url, request, AuditManagerGetAssessmentReportUrlResponse)

    async def get_change_logs(
        self,
        request: AuditManagerGetChangeLogsRequest,
    ) -> AuditManagerGetChangeLogsResponse:
        client = self._require_client()
        return await self._execute(client.get_change_logs, request, AuditManagerGetChangeLogsResponse)

    async def get_control(
        self,
        request: AuditManagerGetControlRequest,
    ) -> AuditManagerGetControlResponse:
        client = self._require_client()
        return await self._execute(client.get_control, request, AuditManagerGetControlResponse)

    async def get_delegations(
        self,
        request: AuditManagerGetDelegationsRequest | None = None,
    ) -> AuditManagerGetDelegationsResponse:
        client = self._require_client()
        return await self._execute(client.get_delegations, request, AuditManagerGetDelegationsResponse)

    async def get_evidence(
        self,
        request: AuditManagerGetEvidenceRequest,
    ) -> AuditManagerGetEvidenceResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence, request, AuditManagerGetEvidenceResponse)

    async def get_evidence_by_evidence_folder(
        self,
        request: AuditManagerGetEvidenceByEvidenceFolderRequest,
    ) -> AuditManagerGetEvidenceByEvidenceFolderResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence_by_evidence_folder, request, AuditManagerGetEvidenceByEvidenceFolderResponse)

    async def get_evidence_file_upload_url(
        self,
        request: AuditManagerGetEvidenceFileUploadUrlRequest,
    ) -> AuditManagerGetEvidenceFileUploadUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence_file_upload_url, request, AuditManagerGetEvidenceFileUploadUrlResponse)

    async def get_evidence_folder(
        self,
        request: AuditManagerGetEvidenceFolderRequest,
    ) -> AuditManagerGetEvidenceFolderResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence_folder, request, AuditManagerGetEvidenceFolderResponse)

    async def get_evidence_folders_by_assessment(
        self,
        request: AuditManagerGetEvidenceFoldersByAssessmentRequest,
    ) -> AuditManagerGetEvidenceFoldersByAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence_folders_by_assessment, request, AuditManagerGetEvidenceFoldersByAssessmentResponse)

    async def get_evidence_folders_by_assessment_control(
        self,
        request: AuditManagerGetEvidenceFoldersByAssessmentControlRequest,
    ) -> AuditManagerGetEvidenceFoldersByAssessmentControlResponse:
        client = self._require_client()
        return await self._execute(client.get_evidence_folders_by_assessment_control, request, AuditManagerGetEvidenceFoldersByAssessmentControlResponse)

    async def get_insights(
        self,
        request: AuditManagerGetInsightsRequest | None = None,
    ) -> AuditManagerGetInsightsResponse:
        client = self._require_client()
        return await self._execute(client.get_insights, request, AuditManagerGetInsightsResponse)

    async def get_insights_by_assessment(
        self,
        request: AuditManagerGetInsightsByAssessmentRequest,
    ) -> AuditManagerGetInsightsByAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.get_insights_by_assessment, request, AuditManagerGetInsightsByAssessmentResponse)

    async def get_organization_admin_account(
        self,
        request: AuditManagerGetOrganizationAdminAccountRequest | None = None,
    ) -> AuditManagerGetOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_admin_account, request, AuditManagerGetOrganizationAdminAccountResponse)

    async def get_services_in_scope(
        self,
        request: AuditManagerGetServicesInScopeRequest | None = None,
    ) -> AuditManagerGetServicesInScopeResponse:
        client = self._require_client()
        return await self._execute(client.get_services_in_scope, request, AuditManagerGetServicesInScopeResponse)

    async def get_settings(
        self,
        request: AuditManagerGetSettingsRequest,
    ) -> AuditManagerGetSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_settings, request, AuditManagerGetSettingsResponse)

    async def list_assessment_control_insights_by_control_domain(
        self,
        request: AuditManagerListAssessmentControlInsightsByControlDomainRequest,
    ) -> AuditManagerListAssessmentControlInsightsByControlDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_assessment_control_insights_by_control_domain, request, AuditManagerListAssessmentControlInsightsByControlDomainResponse)

    async def list_assessment_framework_share_requests(
        self,
        request: AuditManagerListAssessmentFrameworkShareRequestsRequest,
    ) -> AuditManagerListAssessmentFrameworkShareRequestsResponse:
        client = self._require_client()
        return await self._execute(client.list_assessment_framework_share_requests, request, AuditManagerListAssessmentFrameworkShareRequestsResponse)

    async def list_assessment_frameworks(
        self,
        request: AuditManagerListAssessmentFrameworksRequest,
    ) -> AuditManagerListAssessmentFrameworksResponse:
        client = self._require_client()
        return await self._execute(client.list_assessment_frameworks, request, AuditManagerListAssessmentFrameworksResponse)

    async def list_assessment_reports(
        self,
        request: AuditManagerListAssessmentReportsRequest | None = None,
    ) -> AuditManagerListAssessmentReportsResponse:
        client = self._require_client()
        return await self._execute(client.list_assessment_reports, request, AuditManagerListAssessmentReportsResponse)

    async def list_assessments(
        self,
        request: AuditManagerListAssessmentsRequest | None = None,
    ) -> AuditManagerListAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_assessments, request, AuditManagerListAssessmentsResponse)

    async def list_control_domain_insights(
        self,
        request: AuditManagerListControlDomainInsightsRequest | None = None,
    ) -> AuditManagerListControlDomainInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_control_domain_insights, request, AuditManagerListControlDomainInsightsResponse)

    async def list_control_domain_insights_by_assessment(
        self,
        request: AuditManagerListControlDomainInsightsByAssessmentRequest,
    ) -> AuditManagerListControlDomainInsightsByAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.list_control_domain_insights_by_assessment, request, AuditManagerListControlDomainInsightsByAssessmentResponse)

    async def list_control_insights_by_control_domain(
        self,
        request: AuditManagerListControlInsightsByControlDomainRequest,
    ) -> AuditManagerListControlInsightsByControlDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_control_insights_by_control_domain, request, AuditManagerListControlInsightsByControlDomainResponse)

    async def list_controls(
        self,
        request: AuditManagerListControlsRequest,
    ) -> AuditManagerListControlsResponse:
        client = self._require_client()
        return await self._execute(client.list_controls, request, AuditManagerListControlsResponse)

    async def list_keywords_for_data_source(
        self,
        request: AuditManagerListKeywordsForDataSourceRequest,
    ) -> AuditManagerListKeywordsForDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.list_keywords_for_data_source, request, AuditManagerListKeywordsForDataSourceResponse)

    async def list_notifications(
        self,
        request: AuditManagerListNotificationsRequest | None = None,
    ) -> AuditManagerListNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.list_notifications, request, AuditManagerListNotificationsResponse)

    async def list_tags_for_resource(
        self,
        request: AuditManagerListTagsForResourceRequest,
    ) -> AuditManagerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AuditManagerListTagsForResourceResponse)

    async def register_account(
        self,
        request: AuditManagerRegisterAccountRequest | None = None,
    ) -> AuditManagerRegisterAccountResponse:
        client = self._require_client()
        return await self._execute(client.register_account, request, AuditManagerRegisterAccountResponse)

    async def register_organization_admin_account(
        self,
        request: AuditManagerRegisterOrganizationAdminAccountRequest,
    ) -> AuditManagerRegisterOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.register_organization_admin_account, request, AuditManagerRegisterOrganizationAdminAccountResponse)

    async def start_assessment_framework_share(
        self,
        request: AuditManagerStartAssessmentFrameworkShareRequest,
    ) -> AuditManagerStartAssessmentFrameworkShareResponse:
        client = self._require_client()
        return await self._execute(client.start_assessment_framework_share, request, AuditManagerStartAssessmentFrameworkShareResponse)

    async def tag_resource(
        self,
        request: AuditManagerTagResourceRequest,
    ) -> AuditManagerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AuditManagerTagResourceResponse)

    async def untag_resource(
        self,
        request: AuditManagerUntagResourceRequest,
    ) -> AuditManagerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AuditManagerUntagResourceResponse)

    async def update_assessment(
        self,
        request: AuditManagerUpdateAssessmentRequest,
    ) -> AuditManagerUpdateAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment, request, AuditManagerUpdateAssessmentResponse)

    async def update_assessment_control(
        self,
        request: AuditManagerUpdateAssessmentControlRequest,
    ) -> AuditManagerUpdateAssessmentControlResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment_control, request, AuditManagerUpdateAssessmentControlResponse)

    async def update_assessment_control_set_status(
        self,
        request: AuditManagerUpdateAssessmentControlSetStatusRequest,
    ) -> AuditManagerUpdateAssessmentControlSetStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment_control_set_status, request, AuditManagerUpdateAssessmentControlSetStatusResponse)

    async def update_assessment_framework(
        self,
        request: AuditManagerUpdateAssessmentFrameworkRequest,
    ) -> AuditManagerUpdateAssessmentFrameworkResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment_framework, request, AuditManagerUpdateAssessmentFrameworkResponse)

    async def update_assessment_framework_share(
        self,
        request: AuditManagerUpdateAssessmentFrameworkShareRequest,
    ) -> AuditManagerUpdateAssessmentFrameworkShareResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment_framework_share, request, AuditManagerUpdateAssessmentFrameworkShareResponse)

    async def update_assessment_status(
        self,
        request: AuditManagerUpdateAssessmentStatusRequest,
    ) -> AuditManagerUpdateAssessmentStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_assessment_status, request, AuditManagerUpdateAssessmentStatusResponse)

    async def update_control(
        self,
        request: AuditManagerUpdateControlRequest,
    ) -> AuditManagerUpdateControlResponse:
        client = self._require_client()
        return await self._execute(client.update_control, request, AuditManagerUpdateControlResponse)

    async def update_settings(
        self,
        request: AuditManagerUpdateSettingsRequest | None = None,
    ) -> AuditManagerUpdateSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_settings, request, AuditManagerUpdateSettingsResponse)

    async def validate_assessment_report_integrity(
        self,
        request: AuditManagerValidateAssessmentReportIntegrityRequest,
    ) -> AuditManagerValidateAssessmentReportIntegrityResponse:
        client = self._require_client()
        return await self._execute(client.validate_assessment_report_integrity, request, AuditManagerValidateAssessmentReportIntegrityResponse)
