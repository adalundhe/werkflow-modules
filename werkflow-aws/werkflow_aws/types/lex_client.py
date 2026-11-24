from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class LexClient(ABC):

    @abstractmethod
    def batch_create_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def build_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bot(
        self,
        *,
        botName: str,
        roleArn: str,
        dataPrivacy: dict[str, Any],
        idleSessionTTLInSeconds: int,
        description: str | None = None,
        botTags: dict[str, str] | None = None,
        testBotAliasTags: dict[str, str] | None = None,
        botType: str | None = None,
        botMembers: list[dict[str, Any]] | None = None,
        errorLogSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bot_alias(
        self,
        *,
        botAliasName: str,
        botId: str,
        description: str | None = None,
        botVersion: str | None = None,
        botAliasLocaleSettings: dict[str, dict[str, Any]] | None = None,
        conversationLogSettings: dict[str, Any] | None = None,
        sentimentAnalysisSettings: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float | int,
        description: str | None = None,
        voiceSettings: dict[str, Any] | None = None,
        unifiedSpeechSettings: dict[str, Any] | None = None,
        audioFillerSettings: dict[str, Any] | None = None,
        speechRecognitionSettings: dict[str, Any] | None = None,
        generativeAISettings: dict[str, Any] | None = None,
        speechDetectionSensitivity: str | None = None,
        speakerDiarizationSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bot_replica(
        self,
        *,
        botId: str,
        replicaRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bot_version(
        self,
        *,
        botId: str,
        botVersionLocaleSpecification: dict[str, dict[str, Any]],
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_export(
        self,
        *,
        resourceSpecification: dict[str, Any],
        fileFormat: str,
        filePassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_intent(
        self,
        *,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        intentDisplayName: str | None = None,
        description: str | None = None,
        parentIntentSignature: str | None = None,
        sampleUtterances: list[dict[str, Any]] | None = None,
        dialogCodeHook: dict[str, Any] | None = None,
        fulfillmentCodeHook: dict[str, Any] | None = None,
        intentConfirmationSetting: dict[str, Any] | None = None,
        intentClosingSetting: dict[str, Any] | None = None,
        inputContexts: list[dict[str, Any]] | None = None,
        outputContexts: list[dict[str, Any]] | None = None,
        kendraConfiguration: dict[str, Any] | None = None,
        initialResponseSetting: dict[str, Any] | None = None,
        qnAIntentConfiguration: dict[str, Any] | None = None,
        qInConnectIntentConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_policy(
        self,
        *,
        resourceArn: str,
        policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_policy_statement(
        self,
        *,
        resourceArn: str,
        statementId: str,
        effect: str,
        principal: list[dict[str, Any]],
        action: list[str],
        condition: dict[str, dict[str, str]] | None = None,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_slot(
        self,
        *,
        slotName: str,
        valueElicitationSetting: dict[str, Any],
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str | None = None,
        slotTypeId: str | None = None,
        obfuscationSetting: dict[str, Any] | None = None,
        multipleValuesSetting: dict[str, Any] | None = None,
        subSlotSetting: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_slot_type(
        self,
        *,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str | None = None,
        slotTypeValues: list[dict[str, Any]] | None = None,
        valueSelectionSetting: dict[str, Any] | None = None,
        parentSlotTypeSignature: str | None = None,
        externalSourceSetting: dict[str, Any] | None = None,
        compositeSlotTypeSetting: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_test_set_discrepancy_report(
        self,
        *,
        testSetId: str,
        target: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_upload_url(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot(
        self,
        *,
        botId: str,
        skipResourceInUseCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot_alias(
        self,
        *,
        botAliasId: str,
        botId: str,
        skipResourceInUseCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot_analyzer_recommendation(
        self,
        *,
        botId: str,
        botAnalyzerRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot_replica(
        self,
        *,
        botId: str,
        replicaRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bot_version(
        self,
        *,
        botId: str,
        botVersion: str,
        skipResourceInUseCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_vocabulary(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_export(
        self,
        *,
        exportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_import(
        self,
        *,
        importId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_intent(
        self,
        *,
        intentId: str,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        resourceArn: str,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy_statement(
        self,
        *,
        resourceArn: str,
        statementId: str,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_slot(
        self,
        *,
        slotId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_slot_type(
        self,
        *,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_test_set(
        self,
        *,
        testSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_utterances(
        self,
        *,
        botId: str,
        localeId: str | None = None,
        sessionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot(
        self,
        *,
        botId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_alias(
        self,
        *,
        botAliasId: str,
        botId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_analyzer_recommendation(
        self,
        *,
        botId: str,
        botAnalyzerRequestId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_replica(
        self,
        *,
        botId: str,
        replicaRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_resource_generation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        generationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bot_version(
        self,
        *,
        botId: str,
        botVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_vocabulary_metadata(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_export(
        self,
        *,
        exportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import(
        self,
        *,
        importId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_intent(
        self,
        *,
        intentId: str,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_policy(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_slot(
        self,
        *,
        slotId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_slot_type(
        self,
        *,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_execution(
        self,
        *,
        testExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_set(
        self,
        *,
        testSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_set_discrepancy_report(
        self,
        *,
        testSetDiscrepancyReportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_set_generation(
        self,
        *,
        testSetGenerationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_bot_element(
        self,
        *,
        intentId: str,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_test_execution_artifacts_url(
        self,
        *,
        testExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aggregated_utterances(
        self,
        *,
        botId: str,
        localeId: str,
        aggregationDuration: dict[str, Any],
        botAliasId: str | None = None,
        botVersion: str | None = None,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_alias_replicas(
        self,
        *,
        botId: str,
        replicaRegion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_aliases(
        self,
        *,
        botId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_analyzer_history(
        self,
        *,
        botId: str,
        localeId: str | None = None,
        botVersion: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_locales(
        self,
        *,
        botId: str,
        botVersion: str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_recommendations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_replicas(
        self,
        *,
        botId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_resource_generations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_version_replicas(
        self,
        *,
        botId: str,
        replicaRegion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bot_versions(
        self,
        *,
        botId: str,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bots(
        self,
        *,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_built_in_intents(
        self,
        *,
        localeId: str,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_built_in_slot_types(
        self,
        *,
        localeId: str,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_vocabulary_items(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_exports(
        self,
        *,
        botId: str | None = None,
        botVersion: str | None = None,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        localeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_imports(
        self,
        *,
        botId: str | None = None,
        botVersion: str | None = None,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        localeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_intent_metrics(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        metrics: list[dict[str, Any]],
        binBy: list[dict[str, Any]] | None = None,
        groupBy: list[dict[str, Any]] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_intent_paths(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        intentPath: str,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_intent_stage_metrics(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        metrics: list[dict[str, Any]],
        binBy: list[dict[str, Any]] | None = None,
        groupBy: list[dict[str, Any]] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommended_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_session_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_session_metrics(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        metrics: list[dict[str, Any]],
        binBy: list[dict[str, Any]] | None = None,
        groupBy: list[dict[str, Any]] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_slot_types(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_slots(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_execution_result_items(
        self,
        *,
        testExecutionId: str,
        resultFilterBy: dict[str, Any],
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_executions(
        self,
        *,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_set_records(
        self,
        *,
        testSetId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_sets(
        self,
        *,
        sortBy: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_utterance_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        sortBy: dict[str, Any] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_utterance_metrics(
        self,
        *,
        botId: str,
        startDateTime: datetime.datetime | str,
        endDateTime: datetime.datetime | str,
        metrics: list[dict[str, Any]],
        binBy: list[dict[str, Any]] | None = None,
        groupBy: list[dict[str, Any]] | None = None,
        attributes: list[dict[str, Any]] | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_associated_transcripts(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        filters: list[dict[str, Any]],
        searchOrder: str | None = None,
        maxResults: int | None = None,
        nextIndex: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_bot_analyzer(
        self,
        *,
        botId: str,
        analysisScope: str,
        localeId: str | None = None,
        botVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        transcriptSourceSetting: dict[str, Any],
        encryptionSetting: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_bot_resource_generation(
        self,
        *,
        generationInputPrompt: str,
        botId: str,
        botVersion: str,
        localeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_import(
        self,
        *,
        importId: str,
        resourceSpecification: dict[str, Any],
        mergeStrategy: str,
        filePassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_test_execution(
        self,
        *,
        testSetId: str,
        target: dict[str, Any],
        apiMode: str,
        testExecutionModality: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_test_set_generation(
        self,
        *,
        testSetName: str,
        storageLocation: dict[str, Any],
        generationDataSource: dict[str, Any],
        roleArn: str,
        description: str | None = None,
        testSetTags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_bot_analyzer(
        self,
        *,
        botId: str,
        botAnalyzerRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceARN: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceARN: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bot(
        self,
        *,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: dict[str, Any],
        idleSessionTTLInSeconds: int,
        description: str | None = None,
        botType: str | None = None,
        botMembers: list[dict[str, Any]] | None = None,
        errorLogSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bot_alias(
        self,
        *,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str | None = None,
        botVersion: str | None = None,
        botAliasLocaleSettings: dict[str, dict[str, Any]] | None = None,
        conversationLogSettings: dict[str, Any] | None = None,
        sentimentAnalysisSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float | int,
        description: str | None = None,
        voiceSettings: dict[str, Any] | None = None,
        unifiedSpeechSettings: dict[str, Any] | None = None,
        audioFillerSettings: dict[str, Any] | None = None,
        speechRecognitionSettings: dict[str, Any] | None = None,
        generativeAISettings: dict[str, Any] | None = None,
        speechDetectionSensitivity: str | None = None,
        speakerDiarizationSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        encryptionSetting: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_export(
        self,
        *,
        exportId: str,
        filePassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_intent(
        self,
        *,
        intentId: str,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        intentDisplayName: str | None = None,
        description: str | None = None,
        parentIntentSignature: str | None = None,
        sampleUtterances: list[dict[str, Any]] | None = None,
        dialogCodeHook: dict[str, Any] | None = None,
        fulfillmentCodeHook: dict[str, Any] | None = None,
        slotPriorities: list[dict[str, Any]] | None = None,
        intentConfirmationSetting: dict[str, Any] | None = None,
        intentClosingSetting: dict[str, Any] | None = None,
        inputContexts: list[dict[str, Any]] | None = None,
        outputContexts: list[dict[str, Any]] | None = None,
        kendraConfiguration: dict[str, Any] | None = None,
        initialResponseSetting: dict[str, Any] | None = None,
        qnAIntentConfiguration: dict[str, Any] | None = None,
        qInConnectIntentConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_policy(
        self,
        *,
        resourceArn: str,
        policy: str,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_slot(
        self,
        *,
        slotId: str,
        slotName: str,
        valueElicitationSetting: dict[str, Any],
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str | None = None,
        slotTypeId: str | None = None,
        obfuscationSetting: dict[str, Any] | None = None,
        multipleValuesSetting: dict[str, Any] | None = None,
        subSlotSetting: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_slot_type(
        self,
        *,
        slotTypeId: str,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str | None = None,
        slotTypeValues: list[dict[str, Any]] | None = None,
        valueSelectionSetting: dict[str, Any] | None = None,
        parentSlotTypeSignature: str | None = None,
        externalSourceSetting: dict[str, Any] | None = None,
        compositeSlotTypeSetting: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_test_set(
        self,
        *,
        testSetId: str,
        testSetName: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
