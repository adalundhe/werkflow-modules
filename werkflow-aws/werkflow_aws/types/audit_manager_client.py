from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AuditManagerClient(ABC):

    @abstractmethod
    def associate_assessment_report_evidence_folder(
        self,
        *,
        assessmentId: str,
        evidenceFolderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_assessment_report_evidence(
        self,
        *,
        assessmentId: str,
        evidenceFolderId: str,
        evidenceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_create_delegation_by_assessment(
        self,
        *,
        createDelegationRequests: list[dict[str, Any]],
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_delegation_by_assessment(
        self,
        *,
        delegationIds: list[str],
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_assessment_report_evidence(
        self,
        *,
        assessmentId: str,
        evidenceFolderId: str,
        evidenceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_import_evidence_to_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        manualEvidence: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_assessment(
        self,
        *,
        name: str,
        assessmentReportsDestination: dict[str, Any],
        scope: dict[str, Any],
        roles: list[dict[str, Any]],
        frameworkId: str,
        description: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_assessment_framework(
        self,
        *,
        name: str,
        controlSets: list[dict[str, Any]],
        description: str | None = None,
        complianceType: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_assessment_report(
        self,
        *,
        name: str,
        assessmentId: str,
        description: str | None = None,
        queryStatement: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_control(
        self,
        *,
        name: str,
        controlMappingSources: list[dict[str, Any]],
        description: str | None = None,
        testingInformation: str | None = None,
        actionPlanTitle: str | None = None,
        actionPlanInstructions: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_assessment(
        self,
        *,
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_assessment_framework(
        self,
        *,
        frameworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_assessment_framework_share(
        self,
        *,
        requestId: str,
        requestType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_assessment_report(
        self,
        *,
        assessmentId: str,
        assessmentReportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_control(
        self,
        *,
        controlId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_organization_admin_account(
        self,
        *,
        adminAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_assessment_report_evidence_folder(
        self,
        *,
        assessmentId: str,
        evidenceFolderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_status(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_assessment(
        self,
        *,
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_assessment_framework(
        self,
        *,
        frameworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_assessment_report_url(
        self,
        *,
        assessmentReportId: str,
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_change_logs(
        self,
        *,
        assessmentId: str,
        controlSetId: str | None = None,
        controlId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_control(
        self,
        *,
        controlId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delegations(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
        evidenceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence_by_evidence_folder(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence_file_upload_url(
        self,
        *,
        fileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence_folder(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence_folders_by_assessment(
        self,
        *,
        assessmentId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evidence_folders_by_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insights(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insights_by_assessment(
        self,
        *,
        assessmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_admin_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_services_in_scope(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_settings(
        self,
        *,
        attribute: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessment_control_insights_by_control_domain(
        self,
        *,
        controlDomainId: str,
        assessmentId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessment_framework_share_requests(
        self,
        *,
        requestType: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessment_frameworks(
        self,
        *,
        frameworkType: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessment_reports(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessments(
        self,
        *,
        status: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_control_domain_insights(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_control_domain_insights_by_assessment(
        self,
        *,
        assessmentId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_control_insights_by_control_domain(
        self,
        *,
        controlDomainId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_controls(
        self,
        *,
        controlType: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        controlCatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_keywords_for_data_source(
        self,
        *,
        source: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notifications(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_account(
        self,
        *,
        kmsKey: str | None = None,
        delegatedAdminAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_organization_admin_account(
        self,
        *,
        adminAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_assessment_framework_share(
        self,
        *,
        frameworkId: str,
        destinationAccount: str,
        destinationRegion: str,
        comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment(
        self,
        *,
        assessmentId: str,
        scope: dict[str, Any],
        assessmentName: str | None = None,
        assessmentDescription: str | None = None,
        assessmentReportsDestination: dict[str, Any] | None = None,
        roles: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        controlStatus: str | None = None,
        commentBody: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment_control_set_status(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        status: str,
        comment: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment_framework(
        self,
        *,
        frameworkId: str,
        name: str,
        controlSets: list[dict[str, Any]],
        description: str | None = None,
        complianceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment_framework_share(
        self,
        *,
        requestId: str,
        requestType: str,
        action: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assessment_status(
        self,
        *,
        assessmentId: str,
        status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_control(
        self,
        *,
        controlId: str,
        name: str,
        controlMappingSources: list[dict[str, Any]],
        description: str | None = None,
        testingInformation: str | None = None,
        actionPlanTitle: str | None = None,
        actionPlanInstructions: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_settings(
        self,
        *,
        snsTopic: str | None = None,
        defaultAssessmentReportsDestination: dict[str, Any] | None = None,
        defaultProcessOwners: list[dict[str, Any]] | None = None,
        kmsKey: str | None = None,
        evidenceFinderEnabled: bool | None = None,
        deregistrationPolicy: dict[str, Any] | None = None,
        defaultExportDestination: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_assessment_report_integrity(
        self,
        *,
        s3RelativePath: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
