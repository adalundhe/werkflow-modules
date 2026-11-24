from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SupportClient(ABC):

    @abstractmethod
    def add_attachments_to_set(
        self,
        *,
        attachments: list[dict[str, Any]],
        attachmentSetId: str | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_communication_to_case(
        self,
        *,
        communicationBody: str,
        caseId: str | None = None,
        ccEmailAddresses: list[str] | None = None,
        attachmentSetId: str | None = None,
        uploadIds: list[str] | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_attachment_upload(
        self,
        *,
        uploadId: str,
        completedUploads: list[dict[str, Any]],
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_case(
        self,
        *,
        subject: str,
        communicationBody: str,
        serviceCode: str | None = None,
        severityCode: str | None = None,
        categoryCode: str | None = None,
        ccEmailAddresses: list[str] | None = None,
        language: str | None = None,
        issueType: str | None = None,
        attachmentSetId: str | None = None,
        uploadIds: list[str] | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_attachment(
        self,
        *,
        attachmentId: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_attachment_upload_status(
        self,
        *,
        uploadId: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cases(
        self,
        *,
        caseIdList: list[str] | None = None,
        displayId: str | None = None,
        afterTime: str | None = None,
        beforeTime: str | None = None,
        includeResolvedCases: bool | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        language: str | None = None,
        includeCommunications: bool | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_communications(
        self,
        *,
        caseId: str,
        beforeTime: str | None = None,
        afterTime: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_create_case_options(
        self,
        *,
        issueType: str,
        serviceCode: str,
        language: str,
        categoryCode: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_services(
        self,
        *,
        serviceCodeList: list[str] | None = None,
        language: str | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_severity_levels(
        self,
        *,
        language: str | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_supported_languages(
        self,
        *,
        issueType: str,
        serviceCode: str,
        categoryCode: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trusted_advisor_check_refresh_statuses(
        self,
        *,
        checkIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trusted_advisor_check_result(
        self,
        *,
        checkId: str,
        language: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trusted_advisor_check_summaries(
        self,
        *,
        checkIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trusted_advisor_checks(
        self,
        *,
        language: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_attachment_download_link(
        self,
        *,
        attachmentId: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_attachment_upload_links(
        self,
        *,
        fileName: str,
        fileSizeBytes: int | None = None,
        uploadId: str | None = None,
        uploadRange: dict[str, Any] | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def refresh_trusted_advisor_check(
        self,
        *,
        checkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resolve_case(
        self,
        *,
        caseId: str | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
