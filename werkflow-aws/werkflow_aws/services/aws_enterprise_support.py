from werkflow_aws.models.enterprise_support import (
    SupportAddAttachmentsToSetRequest,
    SupportAddAttachmentsToSetResponse,
    SupportAddCommunicationToCaseRequest,
    SupportAddCommunicationToCaseResponse,
    SupportCompleteAttachmentUploadRequest,
    SupportCompleteAttachmentUploadResponse,
    SupportCreateCaseRequest,
    SupportCreateCaseResponse,
    SupportDescribeAttachmentRequest,
    SupportDescribeAttachmentResponse,
    SupportDescribeAttachmentUploadStatusRequest,
    SupportDescribeAttachmentUploadStatusResponse,
    SupportDescribeCasesRequest,
    SupportDescribeCasesResponse,
    SupportDescribeCommunicationsRequest,
    SupportDescribeCommunicationsResponse,
    SupportDescribeCreateCaseOptionsRequest,
    SupportDescribeCreateCaseOptionsResponse,
    SupportDescribeServicesRequest,
    SupportDescribeServicesResponse,
    SupportDescribeSeverityLevelsRequest,
    SupportDescribeSeverityLevelsResponse,
    SupportDescribeSupportedLanguagesRequest,
    SupportDescribeSupportedLanguagesResponse,
    SupportDescribeTrustedAdvisorCheckRefreshStatusesRequest,
    SupportDescribeTrustedAdvisorCheckRefreshStatusesResponse,
    SupportDescribeTrustedAdvisorCheckResultRequest,
    SupportDescribeTrustedAdvisorCheckResultResponse,
    SupportDescribeTrustedAdvisorCheckSummariesRequest,
    SupportDescribeTrustedAdvisorCheckSummariesResponse,
    SupportDescribeTrustedAdvisorChecksRequest,
    SupportDescribeTrustedAdvisorChecksResponse,
    SupportGetAttachmentDownloadLinkRequest,
    SupportGetAttachmentDownloadLinkResponse,
    SupportGetAttachmentUploadLinksRequest,
    SupportGetAttachmentUploadLinksResponse,
    SupportRefreshTrustedAdvisorCheckRequest,
    SupportRefreshTrustedAdvisorCheckResponse,
    SupportResolveCaseRequest,
    SupportResolveCaseResponse,
)
from werkflow_aws.types.enterprise_support_client import SupportClient
from .base import AWSBaseService


class AWSSupport(AWSBaseService[SupportClient]):
    service_name = 'enterprise-support'
    boto3_service_name = 'support'

    def __init__(self) -> None:
        super().__init__(service_name='enterprise-support', boto3_service_name='support')

    async def add_attachments_to_set(
        self,
        request: SupportAddAttachmentsToSetRequest,
    ) -> SupportAddAttachmentsToSetResponse:
        client = self._require_client()
        return await self._execute(client.add_attachments_to_set, request, SupportAddAttachmentsToSetResponse)

    async def add_communication_to_case(
        self,
        request: SupportAddCommunicationToCaseRequest,
    ) -> SupportAddCommunicationToCaseResponse:
        client = self._require_client()
        return await self._execute(client.add_communication_to_case, request, SupportAddCommunicationToCaseResponse)

    async def complete_attachment_upload(
        self,
        request: SupportCompleteAttachmentUploadRequest,
    ) -> SupportCompleteAttachmentUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_attachment_upload, request, SupportCompleteAttachmentUploadResponse)

    async def create_case(
        self,
        request: SupportCreateCaseRequest,
    ) -> SupportCreateCaseResponse:
        client = self._require_client()
        return await self._execute(client.create_case, request, SupportCreateCaseResponse)

    async def describe_attachment(
        self,
        request: SupportDescribeAttachmentRequest,
    ) -> SupportDescribeAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_attachment, request, SupportDescribeAttachmentResponse)

    async def describe_attachment_upload_status(
        self,
        request: SupportDescribeAttachmentUploadStatusRequest,
    ) -> SupportDescribeAttachmentUploadStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_attachment_upload_status, request, SupportDescribeAttachmentUploadStatusResponse)

    async def describe_cases(
        self,
        request: SupportDescribeCasesRequest | None = None,
    ) -> SupportDescribeCasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_cases, request, SupportDescribeCasesResponse)

    async def describe_cases_paginated(
        self,
        request: SupportDescribeCasesRequest | None = None,
    ) -> list[SupportDescribeCasesResponse]:
        return await self._paginate('describe_cases', request, SupportDescribeCasesResponse)

    async def describe_communications(
        self,
        request: SupportDescribeCommunicationsRequest,
    ) -> SupportDescribeCommunicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_communications, request, SupportDescribeCommunicationsResponse)

    async def describe_communications_paginated(
        self,
        request: SupportDescribeCommunicationsRequest,
    ) -> list[SupportDescribeCommunicationsResponse]:
        return await self._paginate('describe_communications', request, SupportDescribeCommunicationsResponse)

    async def describe_create_case_options(
        self,
        request: SupportDescribeCreateCaseOptionsRequest,
    ) -> SupportDescribeCreateCaseOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_create_case_options, request, SupportDescribeCreateCaseOptionsResponse)

    async def describe_services(
        self,
        request: SupportDescribeServicesRequest | None = None,
    ) -> SupportDescribeServicesResponse:
        client = self._require_client()
        return await self._execute(client.describe_services, request, SupportDescribeServicesResponse)

    async def describe_severity_levels(
        self,
        request: SupportDescribeSeverityLevelsRequest | None = None,
    ) -> SupportDescribeSeverityLevelsResponse:
        client = self._require_client()
        return await self._execute(client.describe_severity_levels, request, SupportDescribeSeverityLevelsResponse)

    async def describe_supported_languages(
        self,
        request: SupportDescribeSupportedLanguagesRequest,
    ) -> SupportDescribeSupportedLanguagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_supported_languages, request, SupportDescribeSupportedLanguagesResponse)

    async def describe_trusted_advisor_check_refresh_statuses(
        self,
        request: SupportDescribeTrustedAdvisorCheckRefreshStatusesRequest,
    ) -> SupportDescribeTrustedAdvisorCheckRefreshStatusesResponse:
        client = self._require_client()
        return await self._execute(client.describe_trusted_advisor_check_refresh_statuses, request, SupportDescribeTrustedAdvisorCheckRefreshStatusesResponse)

    async def describe_trusted_advisor_check_result(
        self,
        request: SupportDescribeTrustedAdvisorCheckResultRequest,
    ) -> SupportDescribeTrustedAdvisorCheckResultResponse:
        client = self._require_client()
        return await self._execute(client.describe_trusted_advisor_check_result, request, SupportDescribeTrustedAdvisorCheckResultResponse)

    async def describe_trusted_advisor_check_summaries(
        self,
        request: SupportDescribeTrustedAdvisorCheckSummariesRequest,
    ) -> SupportDescribeTrustedAdvisorCheckSummariesResponse:
        client = self._require_client()
        return await self._execute(client.describe_trusted_advisor_check_summaries, request, SupportDescribeTrustedAdvisorCheckSummariesResponse)

    async def describe_trusted_advisor_checks(
        self,
        request: SupportDescribeTrustedAdvisorChecksRequest,
    ) -> SupportDescribeTrustedAdvisorChecksResponse:
        client = self._require_client()
        return await self._execute(client.describe_trusted_advisor_checks, request, SupportDescribeTrustedAdvisorChecksResponse)

    async def get_attachment_download_link(
        self,
        request: SupportGetAttachmentDownloadLinkRequest,
    ) -> SupportGetAttachmentDownloadLinkResponse:
        client = self._require_client()
        return await self._execute(client.get_attachment_download_link, request, SupportGetAttachmentDownloadLinkResponse)

    async def get_attachment_upload_links(
        self,
        request: SupportGetAttachmentUploadLinksRequest,
    ) -> SupportGetAttachmentUploadLinksResponse:
        client = self._require_client()
        return await self._execute(client.get_attachment_upload_links, request, SupportGetAttachmentUploadLinksResponse)

    async def refresh_trusted_advisor_check(
        self,
        request: SupportRefreshTrustedAdvisorCheckRequest,
    ) -> SupportRefreshTrustedAdvisorCheckResponse:
        client = self._require_client()
        return await self._execute(client.refresh_trusted_advisor_check, request, SupportRefreshTrustedAdvisorCheckResponse)

    async def resolve_case(
        self,
        request: SupportResolveCaseRequest | None = None,
    ) -> SupportResolveCaseResponse:
        client = self._require_client()
        return await self._execute(client.resolve_case, request, SupportResolveCaseResponse)
