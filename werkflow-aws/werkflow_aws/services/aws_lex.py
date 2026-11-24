from werkflow_aws.models.lex import (
    LexBatchCreateCustomVocabularyItemRequest,
    LexBatchCreateCustomVocabularyItemResponse,
    LexBatchDeleteCustomVocabularyItemRequest,
    LexBatchDeleteCustomVocabularyItemResponse,
    LexBatchUpdateCustomVocabularyItemRequest,
    LexBatchUpdateCustomVocabularyItemResponse,
    LexBuildBotLocaleRequest,
    LexBuildBotLocaleResponse,
    LexCreateBotAliasRequest,
    LexCreateBotAliasResponse,
    LexCreateBotLocaleRequest,
    LexCreateBotLocaleResponse,
    LexCreateBotReplicaRequest,
    LexCreateBotReplicaResponse,
    LexCreateBotRequest,
    LexCreateBotResponse,
    LexCreateBotVersionRequest,
    LexCreateBotVersionResponse,
    LexCreateExportRequest,
    LexCreateExportResponse,
    LexCreateIntentRequest,
    LexCreateIntentResponse,
    LexCreateResourcePolicyRequest,
    LexCreateResourcePolicyResponse,
    LexCreateResourcePolicyStatementRequest,
    LexCreateResourcePolicyStatementResponse,
    LexCreateSlotRequest,
    LexCreateSlotResponse,
    LexCreateSlotTypeRequest,
    LexCreateSlotTypeResponse,
    LexCreateTestSetDiscrepancyReportRequest,
    LexCreateTestSetDiscrepancyReportResponse,
    LexCreateUploadUrlRequest,
    LexCreateUploadUrlResponse,
    LexDeleteBotAliasRequest,
    LexDeleteBotAliasResponse,
    LexDeleteBotAnalyzerRecommendationRequest,
    LexDeleteBotAnalyzerRecommendationResponse,
    LexDeleteBotLocaleRequest,
    LexDeleteBotLocaleResponse,
    LexDeleteBotReplicaRequest,
    LexDeleteBotReplicaResponse,
    LexDeleteBotRequest,
    LexDeleteBotResponse,
    LexDeleteBotVersionRequest,
    LexDeleteBotVersionResponse,
    LexDeleteCustomVocabularyRequest,
    LexDeleteCustomVocabularyResponse,
    LexDeleteExportRequest,
    LexDeleteExportResponse,
    LexDeleteImportRequest,
    LexDeleteImportResponse,
    LexDeleteIntentRequest,
    LexDeleteIntentResponse,
    LexDeleteResourcePolicyRequest,
    LexDeleteResourcePolicyResponse,
    LexDeleteResourcePolicyStatementRequest,
    LexDeleteResourcePolicyStatementResponse,
    LexDeleteSlotRequest,
    LexDeleteSlotResponse,
    LexDeleteSlotTypeRequest,
    LexDeleteSlotTypeResponse,
    LexDeleteTestSetRequest,
    LexDeleteTestSetResponse,
    LexDeleteUtterancesRequest,
    LexDeleteUtterancesResponse,
    LexDescribeBotAliasRequest,
    LexDescribeBotAliasResponse,
    LexDescribeBotAnalyzerRecommendationRequest,
    LexDescribeBotAnalyzerRecommendationResponse,
    LexDescribeBotLocaleRequest,
    LexDescribeBotLocaleResponse,
    LexDescribeBotRecommendationRequest,
    LexDescribeBotRecommendationResponse,
    LexDescribeBotReplicaRequest,
    LexDescribeBotReplicaResponse,
    LexDescribeBotRequest,
    LexDescribeBotResourceGenerationRequest,
    LexDescribeBotResourceGenerationResponse,
    LexDescribeBotResponse,
    LexDescribeBotVersionRequest,
    LexDescribeBotVersionResponse,
    LexDescribeCustomVocabularyMetadataRequest,
    LexDescribeCustomVocabularyMetadataResponse,
    LexDescribeExportRequest,
    LexDescribeExportResponse,
    LexDescribeImportRequest,
    LexDescribeImportResponse,
    LexDescribeIntentRequest,
    LexDescribeIntentResponse,
    LexDescribeResourcePolicyRequest,
    LexDescribeResourcePolicyResponse,
    LexDescribeSlotRequest,
    LexDescribeSlotResponse,
    LexDescribeSlotTypeRequest,
    LexDescribeSlotTypeResponse,
    LexDescribeTestExecutionRequest,
    LexDescribeTestExecutionResponse,
    LexDescribeTestSetDiscrepancyReportRequest,
    LexDescribeTestSetDiscrepancyReportResponse,
    LexDescribeTestSetGenerationRequest,
    LexDescribeTestSetGenerationResponse,
    LexDescribeTestSetRequest,
    LexDescribeTestSetResponse,
    LexGenerateBotElementRequest,
    LexGenerateBotElementResponse,
    LexGetTestExecutionArtifactsUrlRequest,
    LexGetTestExecutionArtifactsUrlResponse,
    LexListAggregatedUtterancesRequest,
    LexListAggregatedUtterancesResponse,
    LexListBotAliasReplicasRequest,
    LexListBotAliasReplicasResponse,
    LexListBotAliasesRequest,
    LexListBotAliasesResponse,
    LexListBotAnalyzerHistoryRequest,
    LexListBotAnalyzerHistoryResponse,
    LexListBotLocalesRequest,
    LexListBotLocalesResponse,
    LexListBotRecommendationsRequest,
    LexListBotRecommendationsResponse,
    LexListBotReplicasRequest,
    LexListBotReplicasResponse,
    LexListBotResourceGenerationsRequest,
    LexListBotResourceGenerationsResponse,
    LexListBotVersionReplicasRequest,
    LexListBotVersionReplicasResponse,
    LexListBotVersionsRequest,
    LexListBotVersionsResponse,
    LexListBotsRequest,
    LexListBotsResponse,
    LexListBuiltInIntentsRequest,
    LexListBuiltInIntentsResponse,
    LexListBuiltInSlotTypesRequest,
    LexListBuiltInSlotTypesResponse,
    LexListCustomVocabularyItemsRequest,
    LexListCustomVocabularyItemsResponse,
    LexListExportsRequest,
    LexListExportsResponse,
    LexListImportsRequest,
    LexListImportsResponse,
    LexListIntentMetricsRequest,
    LexListIntentMetricsResponse,
    LexListIntentPathsRequest,
    LexListIntentPathsResponse,
    LexListIntentStageMetricsRequest,
    LexListIntentStageMetricsResponse,
    LexListIntentsRequest,
    LexListIntentsResponse,
    LexListRecommendedIntentsRequest,
    LexListRecommendedIntentsResponse,
    LexListSessionAnalyticsDataRequest,
    LexListSessionAnalyticsDataResponse,
    LexListSessionMetricsRequest,
    LexListSessionMetricsResponse,
    LexListSlotTypesRequest,
    LexListSlotTypesResponse,
    LexListSlotsRequest,
    LexListSlotsResponse,
    LexListTagsForResourceRequest,
    LexListTagsForResourceResponse,
    LexListTestExecutionResultItemsRequest,
    LexListTestExecutionResultItemsResponse,
    LexListTestExecutionsRequest,
    LexListTestExecutionsResponse,
    LexListTestSetRecordsRequest,
    LexListTestSetRecordsResponse,
    LexListTestSetsRequest,
    LexListTestSetsResponse,
    LexListUtteranceAnalyticsDataRequest,
    LexListUtteranceAnalyticsDataResponse,
    LexListUtteranceMetricsRequest,
    LexListUtteranceMetricsResponse,
    LexSearchAssociatedTranscriptsRequest,
    LexSearchAssociatedTranscriptsResponse,
    LexStartBotAnalyzerRequest,
    LexStartBotAnalyzerResponse,
    LexStartBotRecommendationRequest,
    LexStartBotRecommendationResponse,
    LexStartBotResourceGenerationRequest,
    LexStartBotResourceGenerationResponse,
    LexStartImportRequest,
    LexStartImportResponse,
    LexStartTestExecutionRequest,
    LexStartTestExecutionResponse,
    LexStartTestSetGenerationRequest,
    LexStartTestSetGenerationResponse,
    LexStopBotAnalyzerRequest,
    LexStopBotAnalyzerResponse,
    LexStopBotRecommendationRequest,
    LexStopBotRecommendationResponse,
    LexTagResourceRequest,
    LexTagResourceResponse,
    LexUntagResourceRequest,
    LexUntagResourceResponse,
    LexUpdateBotAliasRequest,
    LexUpdateBotAliasResponse,
    LexUpdateBotLocaleRequest,
    LexUpdateBotLocaleResponse,
    LexUpdateBotRecommendationRequest,
    LexUpdateBotRecommendationResponse,
    LexUpdateBotRequest,
    LexUpdateBotResponse,
    LexUpdateExportRequest,
    LexUpdateExportResponse,
    LexUpdateIntentRequest,
    LexUpdateIntentResponse,
    LexUpdateResourcePolicyRequest,
    LexUpdateResourcePolicyResponse,
    LexUpdateSlotRequest,
    LexUpdateSlotResponse,
    LexUpdateSlotTypeRequest,
    LexUpdateSlotTypeResponse,
    LexUpdateTestSetRequest,
    LexUpdateTestSetResponse,
)
from werkflow_aws.types.lex_client import LexClient
from .base import AWSBaseService


class AWSLex(AWSBaseService[LexClient]):
    service_name = 'lex'
    boto3_service_name = 'lexv2-models'

    def __init__(self) -> None:
        super().__init__(service_name='lex', boto3_service_name='lexv2-models')

    async def batch_create_custom_vocabulary_item(
        self,
        request: LexBatchCreateCustomVocabularyItemRequest,
    ) -> LexBatchCreateCustomVocabularyItemResponse:
        client = self._require_client()
        return await self._execute(client.batch_create_custom_vocabulary_item, request, LexBatchCreateCustomVocabularyItemResponse)

    async def batch_delete_custom_vocabulary_item(
        self,
        request: LexBatchDeleteCustomVocabularyItemRequest,
    ) -> LexBatchDeleteCustomVocabularyItemResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_custom_vocabulary_item, request, LexBatchDeleteCustomVocabularyItemResponse)

    async def batch_update_custom_vocabulary_item(
        self,
        request: LexBatchUpdateCustomVocabularyItemRequest,
    ) -> LexBatchUpdateCustomVocabularyItemResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_custom_vocabulary_item, request, LexBatchUpdateCustomVocabularyItemResponse)

    async def build_bot_locale(
        self,
        request: LexBuildBotLocaleRequest,
    ) -> LexBuildBotLocaleResponse:
        client = self._require_client()
        return await self._execute(client.build_bot_locale, request, LexBuildBotLocaleResponse)

    async def create_bot(
        self,
        request: LexCreateBotRequest,
    ) -> LexCreateBotResponse:
        client = self._require_client()
        return await self._execute(client.create_bot, request, LexCreateBotResponse)

    async def create_bot_alias(
        self,
        request: LexCreateBotAliasRequest,
    ) -> LexCreateBotAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_bot_alias, request, LexCreateBotAliasResponse)

    async def create_bot_locale(
        self,
        request: LexCreateBotLocaleRequest,
    ) -> LexCreateBotLocaleResponse:
        client = self._require_client()
        return await self._execute(client.create_bot_locale, request, LexCreateBotLocaleResponse)

    async def create_bot_replica(
        self,
        request: LexCreateBotReplicaRequest,
    ) -> LexCreateBotReplicaResponse:
        client = self._require_client()
        return await self._execute(client.create_bot_replica, request, LexCreateBotReplicaResponse)

    async def create_bot_version(
        self,
        request: LexCreateBotVersionRequest,
    ) -> LexCreateBotVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_bot_version, request, LexCreateBotVersionResponse)

    async def create_export(
        self,
        request: LexCreateExportRequest,
    ) -> LexCreateExportResponse:
        client = self._require_client()
        return await self._execute(client.create_export, request, LexCreateExportResponse)

    async def create_intent(
        self,
        request: LexCreateIntentRequest,
    ) -> LexCreateIntentResponse:
        client = self._require_client()
        return await self._execute(client.create_intent, request, LexCreateIntentResponse)

    async def create_resource_policy(
        self,
        request: LexCreateResourcePolicyRequest,
    ) -> LexCreateResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_policy, request, LexCreateResourcePolicyResponse)

    async def create_resource_policy_statement(
        self,
        request: LexCreateResourcePolicyStatementRequest,
    ) -> LexCreateResourcePolicyStatementResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_policy_statement, request, LexCreateResourcePolicyStatementResponse)

    async def create_slot(
        self,
        request: LexCreateSlotRequest,
    ) -> LexCreateSlotResponse:
        client = self._require_client()
        return await self._execute(client.create_slot, request, LexCreateSlotResponse)

    async def create_slot_type(
        self,
        request: LexCreateSlotTypeRequest,
    ) -> LexCreateSlotTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_slot_type, request, LexCreateSlotTypeResponse)

    async def create_test_set_discrepancy_report(
        self,
        request: LexCreateTestSetDiscrepancyReportRequest,
    ) -> LexCreateTestSetDiscrepancyReportResponse:
        client = self._require_client()
        return await self._execute(client.create_test_set_discrepancy_report, request, LexCreateTestSetDiscrepancyReportResponse)

    async def create_upload_url(
        self,
        request: LexCreateUploadUrlRequest | None = None,
    ) -> LexCreateUploadUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_upload_url, request, LexCreateUploadUrlResponse)

    async def delete_bot(
        self,
        request: LexDeleteBotRequest,
    ) -> LexDeleteBotResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot, request, LexDeleteBotResponse)

    async def delete_bot_alias(
        self,
        request: LexDeleteBotAliasRequest,
    ) -> LexDeleteBotAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot_alias, request, LexDeleteBotAliasResponse)

    async def delete_bot_analyzer_recommendation(
        self,
        request: LexDeleteBotAnalyzerRecommendationRequest,
    ) -> LexDeleteBotAnalyzerRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot_analyzer_recommendation, request, LexDeleteBotAnalyzerRecommendationResponse)

    async def delete_bot_locale(
        self,
        request: LexDeleteBotLocaleRequest,
    ) -> LexDeleteBotLocaleResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot_locale, request, LexDeleteBotLocaleResponse)

    async def delete_bot_replica(
        self,
        request: LexDeleteBotReplicaRequest,
    ) -> LexDeleteBotReplicaResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot_replica, request, LexDeleteBotReplicaResponse)

    async def delete_bot_version(
        self,
        request: LexDeleteBotVersionRequest,
    ) -> LexDeleteBotVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_bot_version, request, LexDeleteBotVersionResponse)

    async def delete_custom_vocabulary(
        self,
        request: LexDeleteCustomVocabularyRequest,
    ) -> LexDeleteCustomVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_vocabulary, request, LexDeleteCustomVocabularyResponse)

    async def delete_export(
        self,
        request: LexDeleteExportRequest,
    ) -> LexDeleteExportResponse:
        client = self._require_client()
        return await self._execute(client.delete_export, request, LexDeleteExportResponse)

    async def delete_import(
        self,
        request: LexDeleteImportRequest,
    ) -> LexDeleteImportResponse:
        client = self._require_client()
        return await self._execute(client.delete_import, request, LexDeleteImportResponse)

    async def delete_intent(
        self,
        request: LexDeleteIntentRequest,
    ) -> LexDeleteIntentResponse:
        client = self._require_client()
        return await self._execute(client.delete_intent, request, LexDeleteIntentResponse)

    async def delete_resource_policy(
        self,
        request: LexDeleteResourcePolicyRequest,
    ) -> LexDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, LexDeleteResourcePolicyResponse)

    async def delete_resource_policy_statement(
        self,
        request: LexDeleteResourcePolicyStatementRequest,
    ) -> LexDeleteResourcePolicyStatementResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy_statement, request, LexDeleteResourcePolicyStatementResponse)

    async def delete_slot(
        self,
        request: LexDeleteSlotRequest,
    ) -> LexDeleteSlotResponse:
        client = self._require_client()
        return await self._execute(client.delete_slot, request, LexDeleteSlotResponse)

    async def delete_slot_type(
        self,
        request: LexDeleteSlotTypeRequest,
    ) -> LexDeleteSlotTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_slot_type, request, LexDeleteSlotTypeResponse)

    async def delete_test_set(
        self,
        request: LexDeleteTestSetRequest,
    ) -> LexDeleteTestSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_test_set, request, LexDeleteTestSetResponse)

    async def delete_utterances(
        self,
        request: LexDeleteUtterancesRequest,
    ) -> LexDeleteUtterancesResponse:
        client = self._require_client()
        return await self._execute(client.delete_utterances, request, LexDeleteUtterancesResponse)

    async def describe_bot(
        self,
        request: LexDescribeBotRequest,
    ) -> LexDescribeBotResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot, request, LexDescribeBotResponse)

    async def describe_bot_alias(
        self,
        request: LexDescribeBotAliasRequest,
    ) -> LexDescribeBotAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_alias, request, LexDescribeBotAliasResponse)

    async def describe_bot_analyzer_recommendation(
        self,
        request: LexDescribeBotAnalyzerRecommendationRequest,
    ) -> LexDescribeBotAnalyzerRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_analyzer_recommendation, request, LexDescribeBotAnalyzerRecommendationResponse)

    async def describe_bot_analyzer_recommendation_paginated(
        self,
        request: LexDescribeBotAnalyzerRecommendationRequest,
    ) -> list[LexDescribeBotAnalyzerRecommendationResponse]:
        return await self._paginate('describe_bot_analyzer_recommendation', request, LexDescribeBotAnalyzerRecommendationResponse)

    async def describe_bot_locale(
        self,
        request: LexDescribeBotLocaleRequest,
    ) -> LexDescribeBotLocaleResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_locale, request, LexDescribeBotLocaleResponse)

    async def describe_bot_recommendation(
        self,
        request: LexDescribeBotRecommendationRequest,
    ) -> LexDescribeBotRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_recommendation, request, LexDescribeBotRecommendationResponse)

    async def describe_bot_replica(
        self,
        request: LexDescribeBotReplicaRequest,
    ) -> LexDescribeBotReplicaResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_replica, request, LexDescribeBotReplicaResponse)

    async def describe_bot_resource_generation(
        self,
        request: LexDescribeBotResourceGenerationRequest,
    ) -> LexDescribeBotResourceGenerationResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_resource_generation, request, LexDescribeBotResourceGenerationResponse)

    async def describe_bot_version(
        self,
        request: LexDescribeBotVersionRequest,
    ) -> LexDescribeBotVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_bot_version, request, LexDescribeBotVersionResponse)

    async def describe_custom_vocabulary_metadata(
        self,
        request: LexDescribeCustomVocabularyMetadataRequest,
    ) -> LexDescribeCustomVocabularyMetadataResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_vocabulary_metadata, request, LexDescribeCustomVocabularyMetadataResponse)

    async def describe_export(
        self,
        request: LexDescribeExportRequest,
    ) -> LexDescribeExportResponse:
        client = self._require_client()
        return await self._execute(client.describe_export, request, LexDescribeExportResponse)

    async def describe_import(
        self,
        request: LexDescribeImportRequest,
    ) -> LexDescribeImportResponse:
        client = self._require_client()
        return await self._execute(client.describe_import, request, LexDescribeImportResponse)

    async def describe_intent(
        self,
        request: LexDescribeIntentRequest,
    ) -> LexDescribeIntentResponse:
        client = self._require_client()
        return await self._execute(client.describe_intent, request, LexDescribeIntentResponse)

    async def describe_resource_policy(
        self,
        request: LexDescribeResourcePolicyRequest,
    ) -> LexDescribeResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_policy, request, LexDescribeResourcePolicyResponse)

    async def describe_slot(
        self,
        request: LexDescribeSlotRequest,
    ) -> LexDescribeSlotResponse:
        client = self._require_client()
        return await self._execute(client.describe_slot, request, LexDescribeSlotResponse)

    async def describe_slot_type(
        self,
        request: LexDescribeSlotTypeRequest,
    ) -> LexDescribeSlotTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_slot_type, request, LexDescribeSlotTypeResponse)

    async def describe_test_execution(
        self,
        request: LexDescribeTestExecutionRequest,
    ) -> LexDescribeTestExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_execution, request, LexDescribeTestExecutionResponse)

    async def describe_test_set(
        self,
        request: LexDescribeTestSetRequest,
    ) -> LexDescribeTestSetResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_set, request, LexDescribeTestSetResponse)

    async def describe_test_set_discrepancy_report(
        self,
        request: LexDescribeTestSetDiscrepancyReportRequest,
    ) -> LexDescribeTestSetDiscrepancyReportResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_set_discrepancy_report, request, LexDescribeTestSetDiscrepancyReportResponse)

    async def describe_test_set_generation(
        self,
        request: LexDescribeTestSetGenerationRequest,
    ) -> LexDescribeTestSetGenerationResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_set_generation, request, LexDescribeTestSetGenerationResponse)

    async def generate_bot_element(
        self,
        request: LexGenerateBotElementRequest,
    ) -> LexGenerateBotElementResponse:
        client = self._require_client()
        return await self._execute(client.generate_bot_element, request, LexGenerateBotElementResponse)

    async def get_test_execution_artifacts_url(
        self,
        request: LexGetTestExecutionArtifactsUrlRequest,
    ) -> LexGetTestExecutionArtifactsUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_test_execution_artifacts_url, request, LexGetTestExecutionArtifactsUrlResponse)

    async def list_aggregated_utterances(
        self,
        request: LexListAggregatedUtterancesRequest,
    ) -> LexListAggregatedUtterancesResponse:
        client = self._require_client()
        return await self._execute(client.list_aggregated_utterances, request, LexListAggregatedUtterancesResponse)

    async def list_bot_alias_replicas(
        self,
        request: LexListBotAliasReplicasRequest,
    ) -> LexListBotAliasReplicasResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_alias_replicas, request, LexListBotAliasReplicasResponse)

    async def list_bot_aliases(
        self,
        request: LexListBotAliasesRequest,
    ) -> LexListBotAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_aliases, request, LexListBotAliasesResponse)

    async def list_bot_analyzer_history(
        self,
        request: LexListBotAnalyzerHistoryRequest,
    ) -> LexListBotAnalyzerHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_analyzer_history, request, LexListBotAnalyzerHistoryResponse)

    async def list_bot_analyzer_history_paginated(
        self,
        request: LexListBotAnalyzerHistoryRequest,
    ) -> list[LexListBotAnalyzerHistoryResponse]:
        return await self._paginate('list_bot_analyzer_history', request, LexListBotAnalyzerHistoryResponse)

    async def list_bot_locales(
        self,
        request: LexListBotLocalesRequest,
    ) -> LexListBotLocalesResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_locales, request, LexListBotLocalesResponse)

    async def list_bot_recommendations(
        self,
        request: LexListBotRecommendationsRequest,
    ) -> LexListBotRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_recommendations, request, LexListBotRecommendationsResponse)

    async def list_bot_replicas(
        self,
        request: LexListBotReplicasRequest,
    ) -> LexListBotReplicasResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_replicas, request, LexListBotReplicasResponse)

    async def list_bot_resource_generations(
        self,
        request: LexListBotResourceGenerationsRequest,
    ) -> LexListBotResourceGenerationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_resource_generations, request, LexListBotResourceGenerationsResponse)

    async def list_bot_version_replicas(
        self,
        request: LexListBotVersionReplicasRequest,
    ) -> LexListBotVersionReplicasResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_version_replicas, request, LexListBotVersionReplicasResponse)

    async def list_bot_versions(
        self,
        request: LexListBotVersionsRequest,
    ) -> LexListBotVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_bot_versions, request, LexListBotVersionsResponse)

    async def list_bots(
        self,
        request: LexListBotsRequest | None = None,
    ) -> LexListBotsResponse:
        client = self._require_client()
        return await self._execute(client.list_bots, request, LexListBotsResponse)

    async def list_built_in_intents(
        self,
        request: LexListBuiltInIntentsRequest,
    ) -> LexListBuiltInIntentsResponse:
        client = self._require_client()
        return await self._execute(client.list_built_in_intents, request, LexListBuiltInIntentsResponse)

    async def list_built_in_slot_types(
        self,
        request: LexListBuiltInSlotTypesRequest,
    ) -> LexListBuiltInSlotTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_built_in_slot_types, request, LexListBuiltInSlotTypesResponse)

    async def list_custom_vocabulary_items(
        self,
        request: LexListCustomVocabularyItemsRequest,
    ) -> LexListCustomVocabularyItemsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_vocabulary_items, request, LexListCustomVocabularyItemsResponse)

    async def list_exports(
        self,
        request: LexListExportsRequest | None = None,
    ) -> LexListExportsResponse:
        client = self._require_client()
        return await self._execute(client.list_exports, request, LexListExportsResponse)

    async def list_imports(
        self,
        request: LexListImportsRequest | None = None,
    ) -> LexListImportsResponse:
        client = self._require_client()
        return await self._execute(client.list_imports, request, LexListImportsResponse)

    async def list_intent_metrics(
        self,
        request: LexListIntentMetricsRequest,
    ) -> LexListIntentMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_intent_metrics, request, LexListIntentMetricsResponse)

    async def list_intent_paths(
        self,
        request: LexListIntentPathsRequest,
    ) -> LexListIntentPathsResponse:
        client = self._require_client()
        return await self._execute(client.list_intent_paths, request, LexListIntentPathsResponse)

    async def list_intent_stage_metrics(
        self,
        request: LexListIntentStageMetricsRequest,
    ) -> LexListIntentStageMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_intent_stage_metrics, request, LexListIntentStageMetricsResponse)

    async def list_intents(
        self,
        request: LexListIntentsRequest,
    ) -> LexListIntentsResponse:
        client = self._require_client()
        return await self._execute(client.list_intents, request, LexListIntentsResponse)

    async def list_recommended_intents(
        self,
        request: LexListRecommendedIntentsRequest,
    ) -> LexListRecommendedIntentsResponse:
        client = self._require_client()
        return await self._execute(client.list_recommended_intents, request, LexListRecommendedIntentsResponse)

    async def list_session_analytics_data(
        self,
        request: LexListSessionAnalyticsDataRequest,
    ) -> LexListSessionAnalyticsDataResponse:
        client = self._require_client()
        return await self._execute(client.list_session_analytics_data, request, LexListSessionAnalyticsDataResponse)

    async def list_session_metrics(
        self,
        request: LexListSessionMetricsRequest,
    ) -> LexListSessionMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_session_metrics, request, LexListSessionMetricsResponse)

    async def list_slot_types(
        self,
        request: LexListSlotTypesRequest,
    ) -> LexListSlotTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_slot_types, request, LexListSlotTypesResponse)

    async def list_slots(
        self,
        request: LexListSlotsRequest,
    ) -> LexListSlotsResponse:
        client = self._require_client()
        return await self._execute(client.list_slots, request, LexListSlotsResponse)

    async def list_tags_for_resource(
        self,
        request: LexListTagsForResourceRequest,
    ) -> LexListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, LexListTagsForResourceResponse)

    async def list_test_execution_result_items(
        self,
        request: LexListTestExecutionResultItemsRequest,
    ) -> LexListTestExecutionResultItemsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_execution_result_items, request, LexListTestExecutionResultItemsResponse)

    async def list_test_executions(
        self,
        request: LexListTestExecutionsRequest | None = None,
    ) -> LexListTestExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_executions, request, LexListTestExecutionsResponse)

    async def list_test_set_records(
        self,
        request: LexListTestSetRecordsRequest,
    ) -> LexListTestSetRecordsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_set_records, request, LexListTestSetRecordsResponse)

    async def list_test_sets(
        self,
        request: LexListTestSetsRequest | None = None,
    ) -> LexListTestSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_sets, request, LexListTestSetsResponse)

    async def list_utterance_analytics_data(
        self,
        request: LexListUtteranceAnalyticsDataRequest,
    ) -> LexListUtteranceAnalyticsDataResponse:
        client = self._require_client()
        return await self._execute(client.list_utterance_analytics_data, request, LexListUtteranceAnalyticsDataResponse)

    async def list_utterance_metrics(
        self,
        request: LexListUtteranceMetricsRequest,
    ) -> LexListUtteranceMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_utterance_metrics, request, LexListUtteranceMetricsResponse)

    async def search_associated_transcripts(
        self,
        request: LexSearchAssociatedTranscriptsRequest,
    ) -> LexSearchAssociatedTranscriptsResponse:
        client = self._require_client()
        return await self._execute(client.search_associated_transcripts, request, LexSearchAssociatedTranscriptsResponse)

    async def start_bot_analyzer(
        self,
        request: LexStartBotAnalyzerRequest,
    ) -> LexStartBotAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.start_bot_analyzer, request, LexStartBotAnalyzerResponse)

    async def start_bot_recommendation(
        self,
        request: LexStartBotRecommendationRequest,
    ) -> LexStartBotRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.start_bot_recommendation, request, LexStartBotRecommendationResponse)

    async def start_bot_resource_generation(
        self,
        request: LexStartBotResourceGenerationRequest,
    ) -> LexStartBotResourceGenerationResponse:
        client = self._require_client()
        return await self._execute(client.start_bot_resource_generation, request, LexStartBotResourceGenerationResponse)

    async def start_import(
        self,
        request: LexStartImportRequest,
    ) -> LexStartImportResponse:
        client = self._require_client()
        return await self._execute(client.start_import, request, LexStartImportResponse)

    async def start_test_execution(
        self,
        request: LexStartTestExecutionRequest,
    ) -> LexStartTestExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_test_execution, request, LexStartTestExecutionResponse)

    async def start_test_set_generation(
        self,
        request: LexStartTestSetGenerationRequest,
    ) -> LexStartTestSetGenerationResponse:
        client = self._require_client()
        return await self._execute(client.start_test_set_generation, request, LexStartTestSetGenerationResponse)

    async def stop_bot_analyzer(
        self,
        request: LexStopBotAnalyzerRequest,
    ) -> LexStopBotAnalyzerResponse:
        client = self._require_client()
        return await self._execute(client.stop_bot_analyzer, request, LexStopBotAnalyzerResponse)

    async def stop_bot_recommendation(
        self,
        request: LexStopBotRecommendationRequest,
    ) -> LexStopBotRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.stop_bot_recommendation, request, LexStopBotRecommendationResponse)

    async def tag_resource(
        self,
        request: LexTagResourceRequest,
    ) -> LexTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, LexTagResourceResponse)

    async def untag_resource(
        self,
        request: LexUntagResourceRequest,
    ) -> LexUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, LexUntagResourceResponse)

    async def update_bot(
        self,
        request: LexUpdateBotRequest,
    ) -> LexUpdateBotResponse:
        client = self._require_client()
        return await self._execute(client.update_bot, request, LexUpdateBotResponse)

    async def update_bot_alias(
        self,
        request: LexUpdateBotAliasRequest,
    ) -> LexUpdateBotAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_bot_alias, request, LexUpdateBotAliasResponse)

    async def update_bot_locale(
        self,
        request: LexUpdateBotLocaleRequest,
    ) -> LexUpdateBotLocaleResponse:
        client = self._require_client()
        return await self._execute(client.update_bot_locale, request, LexUpdateBotLocaleResponse)

    async def update_bot_recommendation(
        self,
        request: LexUpdateBotRecommendationRequest,
    ) -> LexUpdateBotRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.update_bot_recommendation, request, LexUpdateBotRecommendationResponse)

    async def update_export(
        self,
        request: LexUpdateExportRequest,
    ) -> LexUpdateExportResponse:
        client = self._require_client()
        return await self._execute(client.update_export, request, LexUpdateExportResponse)

    async def update_intent(
        self,
        request: LexUpdateIntentRequest,
    ) -> LexUpdateIntentResponse:
        client = self._require_client()
        return await self._execute(client.update_intent, request, LexUpdateIntentResponse)

    async def update_resource_policy(
        self,
        request: LexUpdateResourcePolicyRequest,
    ) -> LexUpdateResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_policy, request, LexUpdateResourcePolicyResponse)

    async def update_slot(
        self,
        request: LexUpdateSlotRequest,
    ) -> LexUpdateSlotResponse:
        client = self._require_client()
        return await self._execute(client.update_slot, request, LexUpdateSlotResponse)

    async def update_slot_type(
        self,
        request: LexUpdateSlotTypeRequest,
    ) -> LexUpdateSlotTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_slot_type, request, LexUpdateSlotTypeResponse)

    async def update_test_set(
        self,
        request: LexUpdateTestSetRequest,
    ) -> LexUpdateTestSetResponse:
        client = self._require_client()
        return await self._execute(client.update_test_set, request, LexUpdateTestSetResponse)
