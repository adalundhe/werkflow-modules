from werkflow_aws.models.iam_analyzer import (
    AccessAnalyzerApplyArchiveRuleRequest,
    AccessAnalyzerApplyArchiveRuleResponse,
    AccessAnalyzerCancelPolicyGenerationRequest,
    AccessAnalyzerCancelPolicyGenerationResponse,
    AccessAnalyzerCheckAccessNotGrantedRequest,
    AccessAnalyzerCheckAccessNotGrantedResponse,
    AccessAnalyzerCheckNoNewAccessRequest,
    AccessAnalyzerCheckNoNewAccessResponse,
    AccessAnalyzerCheckNoPublicAccessRequest,
    AccessAnalyzerCheckNoPublicAccessResponse,
    AccessAnalyzerCreateAccessPreviewRequest,
    AccessAnalyzerCreateAccessPreviewResponse,
    AccessAnalyzerCreateAnalyzerRequest,
    AccessAnalyzerCreateAnalyzerResponse,
    AccessAnalyzerCreateArchiveRuleRequest,
    AccessAnalyzerCreateArchiveRuleResponse,
    AccessAnalyzerCreateServiceLinkedAnalyzerRequest,
    AccessAnalyzerCreateServiceLinkedAnalyzerResponse,
    AccessAnalyzerDeleteAnalyzerRequest,
    AccessAnalyzerDeleteAnalyzerResponse,
    AccessAnalyzerDeleteArchiveRuleRequest,
    AccessAnalyzerDeleteArchiveRuleResponse,
    AccessAnalyzerDeleteServiceLinkedAnalyzerRequest,
    AccessAnalyzerDeleteServiceLinkedAnalyzerResponse,
    AccessAnalyzerGenerateFindingRecommendationRequest,
    AccessAnalyzerGenerateFindingRecommendationResponse,
    AccessAnalyzerGetAccessPreviewRequest,
    AccessAnalyzerGetAccessPreviewResponse,
    AccessAnalyzerGetAnalyzedResourceRequest,
    AccessAnalyzerGetAnalyzedResourceResponse,
    AccessAnalyzerGetAnalyzerRequest,
    AccessAnalyzerGetAnalyzerResponse,
    AccessAnalyzerGetArchiveRuleRequest,
    AccessAnalyzerGetArchiveRuleResponse,
    AccessAnalyzerGetFindingRecommendationRequest,
    AccessAnalyzerGetFindingRecommendationResponse,
    AccessAnalyzerGetFindingRequest,
    AccessAnalyzerGetFindingResponse,
    AccessAnalyzerGetFindingV2Request,
    AccessAnalyzerGetFindingV2Response,
    AccessAnalyzerGetFindingsStatisticsRequest,
    AccessAnalyzerGetFindingsStatisticsResponse,
    AccessAnalyzerGetGeneratedPolicyRequest,
    AccessAnalyzerGetGeneratedPolicyResponse,
    AccessAnalyzerListAccessPreviewFindingsRequest,
    AccessAnalyzerListAccessPreviewFindingsResponse,
    AccessAnalyzerListAccessPreviewsRequest,
    AccessAnalyzerListAccessPreviewsResponse,
    AccessAnalyzerListAnalyzedResourcesRequest,
    AccessAnalyzerListAnalyzedResourcesResponse,
    AccessAnalyzerListAnalyzersRequest,
    AccessAnalyzerListAnalyzersResponse,
    AccessAnalyzerListArchiveRulesRequest,
    AccessAnalyzerListArchiveRulesResponse,
    AccessAnalyzerListFindingsRequest,
    AccessAnalyzerListFindingsResponse,
    AccessAnalyzerListFindingsV2Request,
    AccessAnalyzerListFindingsV2Response,
    AccessAnalyzerListPolicyGenerationsRequest,
    AccessAnalyzerListPolicyGenerationsResponse,
    AccessAnalyzerListTagsForResourceRequest,
    AccessAnalyzerListTagsForResourceResponse,
    AccessAnalyzerStartPolicyGenerationRequest,
    AccessAnalyzerStartPolicyGenerationResponse,
    AccessAnalyzerStartResourceScanRequest,
    AccessAnalyzerStartResourceScanResponse,
    AccessAnalyzerTagResourceRequest,
    AccessAnalyzerTagResourceResponse,
    AccessAnalyzerUntagResourceRequest,
    AccessAnalyzerUntagResourceResponse,
    AccessAnalyzerUpdateAnalyzerRequest,
    AccessAnalyzerUpdateAnalyzerResponse,
    AccessAnalyzerUpdateArchiveRuleRequest,
    AccessAnalyzerUpdateArchiveRuleResponse,
    AccessAnalyzerUpdateFindingsRequest,
    AccessAnalyzerUpdateFindingsResponse,
    AccessAnalyzerValidatePolicyRequest,
    AccessAnalyzerValidatePolicyResponse,
)
from werkflow_aws.types.iam_analyzer_client import AccessAnalyzerClient
from .base import AWSBaseService


class AWSAccessAnalyzer(AWSBaseService[AccessAnalyzerClient]):
    service_name = 'iam-analyzer'
    boto3_service_name = 'accessanalyzer'

    def __init__(self) -> None:
        super().__init__(service_name='iam-analyzer', boto3_service_name='accessanalyzer')

    async def apply_archive_rule(
        self,
        request: AccessAnalyzerApplyArchiveRuleRequest,
    ) -> AccessAnalyzerApplyArchiveRuleResponse:
        client = self._require_client()
        return await self._execute(client.apply_archive_rule, request, AccessAnalyzerApplyArchiveRuleResponse)

    async def cancel_policy_generation(
        self,
        request: AccessAnalyzerCancelPolicyGenerationRequest,
    ) -> AccessAnalyzerCancelPolicyGenerationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_policy_generation, request, AccessAnalyzerCancelPolicyGenerationResponse)

    async def check_access_not_granted(
        self,
        request: AccessAnalyzerCheckAccessNotGrantedRequest,
    ) -> AccessAnalyzerCheckAccessNotGrantedResponse:
        client = self._require_client()
        return await self._execute(client.check_access_not_granted, request, AccessAnalyzerCheckAccessNotGrantedResponse)

    async def check_no_new_access(
        self,
        request: AccessAnalyzerCheckNoNewAccessRequest,
    ) -> AccessAnalyzerCheckNoNewAccessResponse:
        client = self._require_client()
        return await self._execute(client.check_no_new_access, request, AccessAnalyzerCheckNoNewAccessResponse)

    async def check_no_public_access(
        self,
        request: AccessAnalyzerCheckNoPublicAccessRequest,
    ) -> AccessAnalyzerCheckNoPublicAccessResponse:
        client = self._require_client()
        return await self._execute(client.check_no_public_access, request, AccessAnalyzerCheckNoPublicAccessResponse)

    async def create_access_preview(
        self,
        request: AccessAnalyzerCreateAccessPreviewRequest,
    ) -> AccessAnalyzerCreateAccessPreviewResponse:
        client = self._require_client()
        return await self._execute(client.create_access_preview, request, AccessAnalyzerCreateAccessPreviewResponse)

    async def create_analyzer(
        self,
        request: AccessAnalyzerCreateAnalyzerRequest,
    ) -> AccessAnalyzerCreateAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.create_analyzer, request, AccessAnalyzerCreateAnalyzerResponse)

    async def create_archive_rule(
        self,
        request: AccessAnalyzerCreateArchiveRuleRequest,
    ) -> AccessAnalyzerCreateArchiveRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_archive_rule, request, AccessAnalyzerCreateArchiveRuleResponse)

    async def create_service_linked_analyzer(
        self,
        request: AccessAnalyzerCreateServiceLinkedAnalyzerRequest,
    ) -> AccessAnalyzerCreateServiceLinkedAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.create_service_linked_analyzer, request, AccessAnalyzerCreateServiceLinkedAnalyzerResponse)

    async def delete_analyzer(
        self,
        request: AccessAnalyzerDeleteAnalyzerRequest,
    ) -> AccessAnalyzerDeleteAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.delete_analyzer, request, AccessAnalyzerDeleteAnalyzerResponse)

    async def delete_archive_rule(
        self,
        request: AccessAnalyzerDeleteArchiveRuleRequest,
    ) -> AccessAnalyzerDeleteArchiveRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_archive_rule, request, AccessAnalyzerDeleteArchiveRuleResponse)

    async def delete_service_linked_analyzer(
        self,
        request: AccessAnalyzerDeleteServiceLinkedAnalyzerRequest,
    ) -> AccessAnalyzerDeleteServiceLinkedAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_linked_analyzer, request, AccessAnalyzerDeleteServiceLinkedAnalyzerResponse)

    async def generate_finding_recommendation(
        self,
        request: AccessAnalyzerGenerateFindingRecommendationRequest,
    ) -> AccessAnalyzerGenerateFindingRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.generate_finding_recommendation, request, AccessAnalyzerGenerateFindingRecommendationResponse)

    async def get_access_preview(
        self,
        request: AccessAnalyzerGetAccessPreviewRequest,
    ) -> AccessAnalyzerGetAccessPreviewResponse:
        client = self._require_client()
        return await self._execute(client.get_access_preview, request, AccessAnalyzerGetAccessPreviewResponse)

    async def get_analyzed_resource(
        self,
        request: AccessAnalyzerGetAnalyzedResourceRequest,
    ) -> AccessAnalyzerGetAnalyzedResourceResponse:
        client = self._require_client()
        return await self._execute(client.get_analyzed_resource, request, AccessAnalyzerGetAnalyzedResourceResponse)

    async def get_analyzer(
        self,
        request: AccessAnalyzerGetAnalyzerRequest,
    ) -> AccessAnalyzerGetAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.get_analyzer, request, AccessAnalyzerGetAnalyzerResponse)

    async def get_archive_rule(
        self,
        request: AccessAnalyzerGetArchiveRuleRequest,
    ) -> AccessAnalyzerGetArchiveRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_archive_rule, request, AccessAnalyzerGetArchiveRuleResponse)

    async def get_finding(
        self,
        request: AccessAnalyzerGetFindingRequest,
    ) -> AccessAnalyzerGetFindingResponse:
        client = self._require_client()
        return await self._execute(client.get_finding, request, AccessAnalyzerGetFindingResponse)

    async def get_finding_recommendation(
        self,
        request: AccessAnalyzerGetFindingRecommendationRequest,
    ) -> AccessAnalyzerGetFindingRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.get_finding_recommendation, request, AccessAnalyzerGetFindingRecommendationResponse)

    async def get_finding_recommendation_paginated(
        self,
        request: AccessAnalyzerGetFindingRecommendationRequest,
    ) -> list[AccessAnalyzerGetFindingRecommendationResponse]:
        return await self._paginate('get_finding_recommendation', request, AccessAnalyzerGetFindingRecommendationResponse)

    async def get_finding_v2(
        self,
        request: AccessAnalyzerGetFindingV2Request,
    ) -> AccessAnalyzerGetFindingV2Response:
        client = self._require_client()
        return await self._execute(client.get_finding_v2, request, AccessAnalyzerGetFindingV2Response)

    async def get_finding_v2_paginated(
        self,
        request: AccessAnalyzerGetFindingV2Request,
    ) -> list[AccessAnalyzerGetFindingV2Response]:
        return await self._paginate('get_finding_v2', request, AccessAnalyzerGetFindingV2Response)

    async def get_findings_statistics(
        self,
        request: AccessAnalyzerGetFindingsStatisticsRequest,
    ) -> AccessAnalyzerGetFindingsStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_findings_statistics, request, AccessAnalyzerGetFindingsStatisticsResponse)

    async def get_generated_policy(
        self,
        request: AccessAnalyzerGetGeneratedPolicyRequest,
    ) -> AccessAnalyzerGetGeneratedPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_generated_policy, request, AccessAnalyzerGetGeneratedPolicyResponse)

    async def list_access_preview_findings(
        self,
        request: AccessAnalyzerListAccessPreviewFindingsRequest,
    ) -> AccessAnalyzerListAccessPreviewFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_access_preview_findings, request, AccessAnalyzerListAccessPreviewFindingsResponse)

    async def list_access_preview_findings_paginated(
        self,
        request: AccessAnalyzerListAccessPreviewFindingsRequest,
    ) -> list[AccessAnalyzerListAccessPreviewFindingsResponse]:
        return await self._paginate('list_access_preview_findings', request, AccessAnalyzerListAccessPreviewFindingsResponse)

    async def list_access_previews(
        self,
        request: AccessAnalyzerListAccessPreviewsRequest,
    ) -> AccessAnalyzerListAccessPreviewsResponse:
        client = self._require_client()
        return await self._execute(client.list_access_previews, request, AccessAnalyzerListAccessPreviewsResponse)

    async def list_access_previews_paginated(
        self,
        request: AccessAnalyzerListAccessPreviewsRequest,
    ) -> list[AccessAnalyzerListAccessPreviewsResponse]:
        return await self._paginate('list_access_previews', request, AccessAnalyzerListAccessPreviewsResponse)

    async def list_analyzed_resources(
        self,
        request: AccessAnalyzerListAnalyzedResourcesRequest,
    ) -> AccessAnalyzerListAnalyzedResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_analyzed_resources, request, AccessAnalyzerListAnalyzedResourcesResponse)

    async def list_analyzed_resources_paginated(
        self,
        request: AccessAnalyzerListAnalyzedResourcesRequest,
    ) -> list[AccessAnalyzerListAnalyzedResourcesResponse]:
        return await self._paginate('list_analyzed_resources', request, AccessAnalyzerListAnalyzedResourcesResponse)

    async def list_analyzers(
        self,
        request: AccessAnalyzerListAnalyzersRequest | None = None,
    ) -> AccessAnalyzerListAnalyzersResponse:
        client = self._require_client()
        return await self._execute(client.list_analyzers, request, AccessAnalyzerListAnalyzersResponse)

    async def list_analyzers_paginated(
        self,
        request: AccessAnalyzerListAnalyzersRequest | None = None,
    ) -> list[AccessAnalyzerListAnalyzersResponse]:
        return await self._paginate('list_analyzers', request, AccessAnalyzerListAnalyzersResponse)

    async def list_archive_rules(
        self,
        request: AccessAnalyzerListArchiveRulesRequest,
    ) -> AccessAnalyzerListArchiveRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_archive_rules, request, AccessAnalyzerListArchiveRulesResponse)

    async def list_archive_rules_paginated(
        self,
        request: AccessAnalyzerListArchiveRulesRequest,
    ) -> list[AccessAnalyzerListArchiveRulesResponse]:
        return await self._paginate('list_archive_rules', request, AccessAnalyzerListArchiveRulesResponse)

    async def list_findings(
        self,
        request: AccessAnalyzerListFindingsRequest,
    ) -> AccessAnalyzerListFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_findings, request, AccessAnalyzerListFindingsResponse)

    async def list_findings_paginated(
        self,
        request: AccessAnalyzerListFindingsRequest,
    ) -> list[AccessAnalyzerListFindingsResponse]:
        return await self._paginate('list_findings', request, AccessAnalyzerListFindingsResponse)

    async def list_findings_v2(
        self,
        request: AccessAnalyzerListFindingsV2Request,
    ) -> AccessAnalyzerListFindingsV2Response:
        client = self._require_client()
        return await self._execute(client.list_findings_v2, request, AccessAnalyzerListFindingsV2Response)

    async def list_findings_v2_paginated(
        self,
        request: AccessAnalyzerListFindingsV2Request,
    ) -> list[AccessAnalyzerListFindingsV2Response]:
        return await self._paginate('list_findings_v2', request, AccessAnalyzerListFindingsV2Response)

    async def list_policy_generations(
        self,
        request: AccessAnalyzerListPolicyGenerationsRequest | None = None,
    ) -> AccessAnalyzerListPolicyGenerationsResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_generations, request, AccessAnalyzerListPolicyGenerationsResponse)

    async def list_policy_generations_paginated(
        self,
        request: AccessAnalyzerListPolicyGenerationsRequest | None = None,
    ) -> list[AccessAnalyzerListPolicyGenerationsResponse]:
        return await self._paginate('list_policy_generations', request, AccessAnalyzerListPolicyGenerationsResponse)

    async def list_tags_for_resource(
        self,
        request: AccessAnalyzerListTagsForResourceRequest,
    ) -> AccessAnalyzerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AccessAnalyzerListTagsForResourceResponse)

    async def start_policy_generation(
        self,
        request: AccessAnalyzerStartPolicyGenerationRequest,
    ) -> AccessAnalyzerStartPolicyGenerationResponse:
        client = self._require_client()
        return await self._execute(client.start_policy_generation, request, AccessAnalyzerStartPolicyGenerationResponse)

    async def start_resource_scan(
        self,
        request: AccessAnalyzerStartResourceScanRequest,
    ) -> AccessAnalyzerStartResourceScanResponse:
        client = self._require_client()
        return await self._execute(client.start_resource_scan, request, AccessAnalyzerStartResourceScanResponse)

    async def tag_resource(
        self,
        request: AccessAnalyzerTagResourceRequest,
    ) -> AccessAnalyzerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AccessAnalyzerTagResourceResponse)

    async def untag_resource(
        self,
        request: AccessAnalyzerUntagResourceRequest,
    ) -> AccessAnalyzerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AccessAnalyzerUntagResourceResponse)

    async def update_analyzer(
        self,
        request: AccessAnalyzerUpdateAnalyzerRequest,
    ) -> AccessAnalyzerUpdateAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.update_analyzer, request, AccessAnalyzerUpdateAnalyzerResponse)

    async def update_archive_rule(
        self,
        request: AccessAnalyzerUpdateArchiveRuleRequest,
    ) -> AccessAnalyzerUpdateArchiveRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_archive_rule, request, AccessAnalyzerUpdateArchiveRuleResponse)

    async def update_findings(
        self,
        request: AccessAnalyzerUpdateFindingsRequest,
    ) -> AccessAnalyzerUpdateFindingsResponse:
        client = self._require_client()
        return await self._execute(client.update_findings, request, AccessAnalyzerUpdateFindingsResponse)

    async def validate_policy(
        self,
        request: AccessAnalyzerValidatePolicyRequest,
    ) -> AccessAnalyzerValidatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.validate_policy, request, AccessAnalyzerValidatePolicyResponse)

    async def validate_policy_paginated(
        self,
        request: AccessAnalyzerValidatePolicyRequest,
    ) -> list[AccessAnalyzerValidatePolicyResponse]:
        return await self._paginate('validate_policy', request, AccessAnalyzerValidatePolicyResponse)
