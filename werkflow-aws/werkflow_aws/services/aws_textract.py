from werkflow_aws.models.textract import (
    TextractAnalyzeDocumentRequest,
    TextractAnalyzeDocumentResponse,
    TextractAnalyzeExpenseRequest,
    TextractAnalyzeExpenseResponse,
    TextractAnalyzeIDRequest,
    TextractAnalyzeIDResponse,
    TextractCreateAdapterRequest,
    TextractCreateAdapterResponse,
    TextractCreateAdapterVersionRequest,
    TextractCreateAdapterVersionResponse,
    TextractCreateBlueprintRequest,
    TextractCreateBlueprintResponse,
    TextractCreateBlueprintVersionRequest,
    TextractCreateBlueprintVersionResponse,
    TextractCreateProjectRequest,
    TextractCreateProjectResponse,
    TextractDeleteAdapterRequest,
    TextractDeleteAdapterResponse,
    TextractDeleteAdapterVersionRequest,
    TextractDeleteAdapterVersionResponse,
    TextractDeleteBlueprintRequest,
    TextractDeleteBlueprintResponse,
    TextractDeleteProjectRequest,
    TextractDeleteProjectResponse,
    TextractDetectDocumentTextRequest,
    TextractDetectDocumentTextResponse,
    TextractGetAdapterRequest,
    TextractGetAdapterResponse,
    TextractGetAdapterVersionRequest,
    TextractGetAdapterVersionResponse,
    TextractGetBlueprintRequest,
    TextractGetBlueprintResponse,
    TextractGetDocumentAnalysisRequest,
    TextractGetDocumentAnalysisResponse,
    TextractGetDocumentInsightsRequest,
    TextractGetDocumentInsightsResponse,
    TextractGetDocumentTextDetectionRequest,
    TextractGetDocumentTextDetectionResponse,
    TextractGetExpenseAnalysisRequest,
    TextractGetExpenseAnalysisResponse,
    TextractGetLendingAnalysisRequest,
    TextractGetLendingAnalysisResponse,
    TextractGetLendingAnalysisSummaryRequest,
    TextractGetLendingAnalysisSummaryResponse,
    TextractGetProjectRequest,
    TextractGetProjectResponse,
    TextractListAdapterVersionsRequest,
    TextractListAdapterVersionsResponse,
    TextractListAdaptersRequest,
    TextractListAdaptersResponse,
    TextractListBlueprintsRequest,
    TextractListBlueprintsResponse,
    TextractListProjectsRequest,
    TextractListProjectsResponse,
    TextractListTagsForResourceRequest,
    TextractListTagsForResourceResponse,
    TextractStartDocumentAnalysisRequest,
    TextractStartDocumentAnalysisResponse,
    TextractStartDocumentInsightsRequest,
    TextractStartDocumentInsightsResponse,
    TextractStartDocumentTextDetectionRequest,
    TextractStartDocumentTextDetectionResponse,
    TextractStartExpenseAnalysisRequest,
    TextractStartExpenseAnalysisResponse,
    TextractStartLendingAnalysisRequest,
    TextractStartLendingAnalysisResponse,
    TextractTagResourceRequest,
    TextractTagResourceResponse,
    TextractUntagResourceRequest,
    TextractUntagResourceResponse,
    TextractUpdateAdapterRequest,
    TextractUpdateAdapterResponse,
    TextractUpdateBlueprintRequest,
    TextractUpdateBlueprintResponse,
    TextractUpdateProjectRequest,
    TextractUpdateProjectResponse,
)
from werkflow_aws.types.textract_client import TextractClient
from .base import AWSBaseService


class AWSTextract(AWSBaseService[TextractClient]):
    service_name = 'textract'
    boto3_service_name = 'textract'

    def __init__(self) -> None:
        super().__init__(service_name='textract', boto3_service_name='textract')

    async def analyze_document(
        self,
        request: TextractAnalyzeDocumentRequest,
    ) -> TextractAnalyzeDocumentResponse:
        client = self._require_client()
        return await self._execute(client.analyze_document, request, TextractAnalyzeDocumentResponse)

    async def analyze_expense(
        self,
        request: TextractAnalyzeExpenseRequest,
    ) -> TextractAnalyzeExpenseResponse:
        client = self._require_client()
        return await self._execute(client.analyze_expense, request, TextractAnalyzeExpenseResponse)

    async def analyze_id(
        self,
        request: TextractAnalyzeIDRequest,
    ) -> TextractAnalyzeIDResponse:
        client = self._require_client()
        return await self._execute(client.analyze_id, request, TextractAnalyzeIDResponse)

    async def create_adapter(
        self,
        request: TextractCreateAdapterRequest,
    ) -> TextractCreateAdapterResponse:
        client = self._require_client()
        return await self._execute(client.create_adapter, request, TextractCreateAdapterResponse)

    async def create_adapter_version(
        self,
        request: TextractCreateAdapterVersionRequest,
    ) -> TextractCreateAdapterVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_adapter_version, request, TextractCreateAdapterVersionResponse)

    async def create_blueprint(
        self,
        request: TextractCreateBlueprintRequest,
    ) -> TextractCreateBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.create_blueprint, request, TextractCreateBlueprintResponse)

    async def create_blueprint_version(
        self,
        request: TextractCreateBlueprintVersionRequest,
    ) -> TextractCreateBlueprintVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_blueprint_version, request, TextractCreateBlueprintVersionResponse)

    async def create_project(
        self,
        request: TextractCreateProjectRequest,
    ) -> TextractCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, TextractCreateProjectResponse)

    async def delete_adapter(
        self,
        request: TextractDeleteAdapterRequest,
    ) -> TextractDeleteAdapterResponse:
        client = self._require_client()
        return await self._execute(client.delete_adapter, request, TextractDeleteAdapterResponse)

    async def delete_adapter_version(
        self,
        request: TextractDeleteAdapterVersionRequest,
    ) -> TextractDeleteAdapterVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_adapter_version, request, TextractDeleteAdapterVersionResponse)

    async def delete_blueprint(
        self,
        request: TextractDeleteBlueprintRequest,
    ) -> TextractDeleteBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.delete_blueprint, request, TextractDeleteBlueprintResponse)

    async def delete_project(
        self,
        request: TextractDeleteProjectRequest,
    ) -> TextractDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, TextractDeleteProjectResponse)

    async def detect_document_text(
        self,
        request: TextractDetectDocumentTextRequest,
    ) -> TextractDetectDocumentTextResponse:
        client = self._require_client()
        return await self._execute(client.detect_document_text, request, TextractDetectDocumentTextResponse)

    async def get_adapter(
        self,
        request: TextractGetAdapterRequest,
    ) -> TextractGetAdapterResponse:
        client = self._require_client()
        return await self._execute(client.get_adapter, request, TextractGetAdapterResponse)

    async def get_adapter_version(
        self,
        request: TextractGetAdapterVersionRequest,
    ) -> TextractGetAdapterVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_adapter_version, request, TextractGetAdapterVersionResponse)

    async def get_blueprint(
        self,
        request: TextractGetBlueprintRequest,
    ) -> TextractGetBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.get_blueprint, request, TextractGetBlueprintResponse)

    async def get_document_analysis(
        self,
        request: TextractGetDocumentAnalysisRequest,
    ) -> TextractGetDocumentAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_document_analysis, request, TextractGetDocumentAnalysisResponse)

    async def get_document_insights(
        self,
        request: TextractGetDocumentInsightsRequest,
    ) -> TextractGetDocumentInsightsResponse:
        client = self._require_client()
        return await self._execute(client.get_document_insights, request, TextractGetDocumentInsightsResponse)

    async def get_document_text_detection(
        self,
        request: TextractGetDocumentTextDetectionRequest,
    ) -> TextractGetDocumentTextDetectionResponse:
        client = self._require_client()
        return await self._execute(client.get_document_text_detection, request, TextractGetDocumentTextDetectionResponse)

    async def get_expense_analysis(
        self,
        request: TextractGetExpenseAnalysisRequest,
    ) -> TextractGetExpenseAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_expense_analysis, request, TextractGetExpenseAnalysisResponse)

    async def get_lending_analysis(
        self,
        request: TextractGetLendingAnalysisRequest,
    ) -> TextractGetLendingAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_lending_analysis, request, TextractGetLendingAnalysisResponse)

    async def get_lending_analysis_summary(
        self,
        request: TextractGetLendingAnalysisSummaryRequest,
    ) -> TextractGetLendingAnalysisSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_lending_analysis_summary, request, TextractGetLendingAnalysisSummaryResponse)

    async def get_project(
        self,
        request: TextractGetProjectRequest,
    ) -> TextractGetProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_project, request, TextractGetProjectResponse)

    async def list_adapter_versions(
        self,
        request: TextractListAdapterVersionsRequest | None = None,
    ) -> TextractListAdapterVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_adapter_versions, request, TextractListAdapterVersionsResponse)

    async def list_adapter_versions_paginated(
        self,
        request: TextractListAdapterVersionsRequest | None = None,
    ) -> list[TextractListAdapterVersionsResponse]:
        return await self._paginate('list_adapter_versions', request, TextractListAdapterVersionsResponse)

    async def list_adapters(
        self,
        request: TextractListAdaptersRequest | None = None,
    ) -> TextractListAdaptersResponse:
        client = self._require_client()
        return await self._execute(client.list_adapters, request, TextractListAdaptersResponse)

    async def list_adapters_paginated(
        self,
        request: TextractListAdaptersRequest | None = None,
    ) -> list[TextractListAdaptersResponse]:
        return await self._paginate('list_adapters', request, TextractListAdaptersResponse)

    async def list_blueprints(
        self,
        request: TextractListBlueprintsRequest | None = None,
    ) -> TextractListBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.list_blueprints, request, TextractListBlueprintsResponse)

    async def list_blueprints_paginated(
        self,
        request: TextractListBlueprintsRequest | None = None,
    ) -> list[TextractListBlueprintsResponse]:
        return await self._paginate('list_blueprints', request, TextractListBlueprintsResponse)

    async def list_projects(
        self,
        request: TextractListProjectsRequest | None = None,
    ) -> TextractListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, TextractListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: TextractListProjectsRequest | None = None,
    ) -> list[TextractListProjectsResponse]:
        return await self._paginate('list_projects', request, TextractListProjectsResponse)

    async def list_tags_for_resource(
        self,
        request: TextractListTagsForResourceRequest,
    ) -> TextractListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TextractListTagsForResourceResponse)

    async def start_document_analysis(
        self,
        request: TextractStartDocumentAnalysisRequest,
    ) -> TextractStartDocumentAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_document_analysis, request, TextractStartDocumentAnalysisResponse)

    async def start_document_insights(
        self,
        request: TextractStartDocumentInsightsRequest,
    ) -> TextractStartDocumentInsightsResponse:
        client = self._require_client()
        return await self._execute(client.start_document_insights, request, TextractStartDocumentInsightsResponse)

    async def start_document_text_detection(
        self,
        request: TextractStartDocumentTextDetectionRequest,
    ) -> TextractStartDocumentTextDetectionResponse:
        client = self._require_client()
        return await self._execute(client.start_document_text_detection, request, TextractStartDocumentTextDetectionResponse)

    async def start_expense_analysis(
        self,
        request: TextractStartExpenseAnalysisRequest,
    ) -> TextractStartExpenseAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_expense_analysis, request, TextractStartExpenseAnalysisResponse)

    async def start_lending_analysis(
        self,
        request: TextractStartLendingAnalysisRequest,
    ) -> TextractStartLendingAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_lending_analysis, request, TextractStartLendingAnalysisResponse)

    async def tag_resource(
        self,
        request: TextractTagResourceRequest,
    ) -> TextractTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TextractTagResourceResponse)

    async def untag_resource(
        self,
        request: TextractUntagResourceRequest,
    ) -> TextractUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TextractUntagResourceResponse)

    async def update_adapter(
        self,
        request: TextractUpdateAdapterRequest,
    ) -> TextractUpdateAdapterResponse:
        client = self._require_client()
        return await self._execute(client.update_adapter, request, TextractUpdateAdapterResponse)

    async def update_blueprint(
        self,
        request: TextractUpdateBlueprintRequest,
    ) -> TextractUpdateBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.update_blueprint, request, TextractUpdateBlueprintResponse)

    async def update_project(
        self,
        request: TextractUpdateProjectRequest,
    ) -> TextractUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, TextractUpdateProjectResponse)
