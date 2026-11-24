from werkflow_aws.models.transcribe import (
    TranscribeCreateCallAnalyticsCategoryRequest,
    TranscribeCreateCallAnalyticsCategoryResponse,
    TranscribeCreateLanguageModelRequest,
    TranscribeCreateLanguageModelResponse,
    TranscribeCreateMedicalVocabularyRequest,
    TranscribeCreateMedicalVocabularyResponse,
    TranscribeCreateVocabularyFilterRequest,
    TranscribeCreateVocabularyFilterResponse,
    TranscribeCreateVocabularyRequest,
    TranscribeCreateVocabularyResponse,
    TranscribeDeleteCallAnalyticsCategoryRequest,
    TranscribeDeleteCallAnalyticsCategoryResponse,
    TranscribeDeleteCallAnalyticsJobRequest,
    TranscribeDeleteCallAnalyticsJobResponse,
    TranscribeDeleteLanguageModelRequest,
    TranscribeDeleteLanguageModelResponse,
    TranscribeDeleteMedicalScribeJobRequest,
    TranscribeDeleteMedicalScribeJobResponse,
    TranscribeDeleteMedicalTranscriptionJobRequest,
    TranscribeDeleteMedicalTranscriptionJobResponse,
    TranscribeDeleteMedicalVocabularyRequest,
    TranscribeDeleteMedicalVocabularyResponse,
    TranscribeDeleteTranscriptionJobRequest,
    TranscribeDeleteTranscriptionJobResponse,
    TranscribeDeleteVocabularyFilterRequest,
    TranscribeDeleteVocabularyFilterResponse,
    TranscribeDeleteVocabularyRequest,
    TranscribeDeleteVocabularyResponse,
    TranscribeDescribeLanguageModelRequest,
    TranscribeDescribeLanguageModelResponse,
    TranscribeGetCallAnalyticsCategoryRequest,
    TranscribeGetCallAnalyticsCategoryResponse,
    TranscribeGetCallAnalyticsJobRequest,
    TranscribeGetCallAnalyticsJobResponse,
    TranscribeGetMedicalScribeJobRequest,
    TranscribeGetMedicalScribeJobResponse,
    TranscribeGetMedicalTranscriptionJobRequest,
    TranscribeGetMedicalTranscriptionJobResponse,
    TranscribeGetMedicalVocabularyRequest,
    TranscribeGetMedicalVocabularyResponse,
    TranscribeGetTranscriptionJobRequest,
    TranscribeGetTranscriptionJobResponse,
    TranscribeGetVocabularyFilterRequest,
    TranscribeGetVocabularyFilterResponse,
    TranscribeGetVocabularyRequest,
    TranscribeGetVocabularyResponse,
    TranscribeListCallAnalyticsCategoriesRequest,
    TranscribeListCallAnalyticsCategoriesResponse,
    TranscribeListCallAnalyticsJobsRequest,
    TranscribeListCallAnalyticsJobsResponse,
    TranscribeListLanguageModelsRequest,
    TranscribeListLanguageModelsResponse,
    TranscribeListMedicalScribeJobsRequest,
    TranscribeListMedicalScribeJobsResponse,
    TranscribeListMedicalTranscriptionJobsRequest,
    TranscribeListMedicalTranscriptionJobsResponse,
    TranscribeListMedicalVocabulariesRequest,
    TranscribeListMedicalVocabulariesResponse,
    TranscribeListTagsForResourceRequest,
    TranscribeListTagsForResourceResponse,
    TranscribeListTranscriptionJobsRequest,
    TranscribeListTranscriptionJobsResponse,
    TranscribeListVocabulariesRequest,
    TranscribeListVocabulariesResponse,
    TranscribeListVocabularyFiltersRequest,
    TranscribeListVocabularyFiltersResponse,
    TranscribeStartCallAnalyticsJobRequest,
    TranscribeStartCallAnalyticsJobResponse,
    TranscribeStartMedicalScribeJobRequest,
    TranscribeStartMedicalScribeJobResponse,
    TranscribeStartMedicalTranscriptionJobRequest,
    TranscribeStartMedicalTranscriptionJobResponse,
    TranscribeStartTranscriptionJobRequest,
    TranscribeStartTranscriptionJobResponse,
    TranscribeTagResourceRequest,
    TranscribeTagResourceResponse,
    TranscribeTranscribeAudioRequest,
    TranscribeTranscribeAudioResponse,
    TranscribeUntagResourceRequest,
    TranscribeUntagResourceResponse,
    TranscribeUpdateCallAnalyticsCategoryRequest,
    TranscribeUpdateCallAnalyticsCategoryResponse,
    TranscribeUpdateLanguageModelRequest,
    TranscribeUpdateLanguageModelResponse,
    TranscribeUpdateMedicalVocabularyRequest,
    TranscribeUpdateMedicalVocabularyResponse,
    TranscribeUpdateVocabularyFilterRequest,
    TranscribeUpdateVocabularyFilterResponse,
    TranscribeUpdateVocabularyRequest,
    TranscribeUpdateVocabularyResponse,
)
from werkflow_aws.types.transcribe_client import TranscribeClient
from .base import AWSBaseService


class AWSTranscribe(AWSBaseService[TranscribeClient]):
    service_name = 'transcribe'
    boto3_service_name = 'transcribe'

    def __init__(self) -> None:
        super().__init__(service_name='transcribe', boto3_service_name='transcribe')

    async def create_call_analytics_category(
        self,
        request: TranscribeCreateCallAnalyticsCategoryRequest,
    ) -> TranscribeCreateCallAnalyticsCategoryResponse:
        client = self._require_client()
        return await self._execute(client.create_call_analytics_category, request, TranscribeCreateCallAnalyticsCategoryResponse)

    async def create_language_model(
        self,
        request: TranscribeCreateLanguageModelRequest,
    ) -> TranscribeCreateLanguageModelResponse:
        client = self._require_client()
        return await self._execute(client.create_language_model, request, TranscribeCreateLanguageModelResponse)

    async def create_medical_vocabulary(
        self,
        request: TranscribeCreateMedicalVocabularyRequest,
    ) -> TranscribeCreateMedicalVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.create_medical_vocabulary, request, TranscribeCreateMedicalVocabularyResponse)

    async def create_vocabulary(
        self,
        request: TranscribeCreateVocabularyRequest,
    ) -> TranscribeCreateVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.create_vocabulary, request, TranscribeCreateVocabularyResponse)

    async def create_vocabulary_filter(
        self,
        request: TranscribeCreateVocabularyFilterRequest,
    ) -> TranscribeCreateVocabularyFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_vocabulary_filter, request, TranscribeCreateVocabularyFilterResponse)

    async def delete_call_analytics_category(
        self,
        request: TranscribeDeleteCallAnalyticsCategoryRequest,
    ) -> TranscribeDeleteCallAnalyticsCategoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_call_analytics_category, request, TranscribeDeleteCallAnalyticsCategoryResponse)

    async def delete_call_analytics_job(
        self,
        request: TranscribeDeleteCallAnalyticsJobRequest,
    ) -> TranscribeDeleteCallAnalyticsJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_call_analytics_job, request, TranscribeDeleteCallAnalyticsJobResponse)

    async def delete_language_model(
        self,
        request: TranscribeDeleteLanguageModelRequest,
    ) -> TranscribeDeleteLanguageModelResponse:
        client = self._require_client()
        return await self._execute(client.delete_language_model, request, TranscribeDeleteLanguageModelResponse)

    async def delete_medical_scribe_job(
        self,
        request: TranscribeDeleteMedicalScribeJobRequest,
    ) -> TranscribeDeleteMedicalScribeJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_medical_scribe_job, request, TranscribeDeleteMedicalScribeJobResponse)

    async def delete_medical_transcription_job(
        self,
        request: TranscribeDeleteMedicalTranscriptionJobRequest,
    ) -> TranscribeDeleteMedicalTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_medical_transcription_job, request, TranscribeDeleteMedicalTranscriptionJobResponse)

    async def delete_medical_vocabulary(
        self,
        request: TranscribeDeleteMedicalVocabularyRequest,
    ) -> TranscribeDeleteMedicalVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.delete_medical_vocabulary, request, TranscribeDeleteMedicalVocabularyResponse)

    async def delete_transcription_job(
        self,
        request: TranscribeDeleteTranscriptionJobRequest,
    ) -> TranscribeDeleteTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_transcription_job, request, TranscribeDeleteTranscriptionJobResponse)

    async def delete_vocabulary(
        self,
        request: TranscribeDeleteVocabularyRequest,
    ) -> TranscribeDeleteVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.delete_vocabulary, request, TranscribeDeleteVocabularyResponse)

    async def delete_vocabulary_filter(
        self,
        request: TranscribeDeleteVocabularyFilterRequest,
    ) -> TranscribeDeleteVocabularyFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_vocabulary_filter, request, TranscribeDeleteVocabularyFilterResponse)

    async def describe_language_model(
        self,
        request: TranscribeDescribeLanguageModelRequest,
    ) -> TranscribeDescribeLanguageModelResponse:
        client = self._require_client()
        return await self._execute(client.describe_language_model, request, TranscribeDescribeLanguageModelResponse)

    async def get_call_analytics_category(
        self,
        request: TranscribeGetCallAnalyticsCategoryRequest,
    ) -> TranscribeGetCallAnalyticsCategoryResponse:
        client = self._require_client()
        return await self._execute(client.get_call_analytics_category, request, TranscribeGetCallAnalyticsCategoryResponse)

    async def get_call_analytics_job(
        self,
        request: TranscribeGetCallAnalyticsJobRequest,
    ) -> TranscribeGetCallAnalyticsJobResponse:
        client = self._require_client()
        return await self._execute(client.get_call_analytics_job, request, TranscribeGetCallAnalyticsJobResponse)

    async def get_medical_scribe_job(
        self,
        request: TranscribeGetMedicalScribeJobRequest,
    ) -> TranscribeGetMedicalScribeJobResponse:
        client = self._require_client()
        return await self._execute(client.get_medical_scribe_job, request, TranscribeGetMedicalScribeJobResponse)

    async def get_medical_transcription_job(
        self,
        request: TranscribeGetMedicalTranscriptionJobRequest,
    ) -> TranscribeGetMedicalTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.get_medical_transcription_job, request, TranscribeGetMedicalTranscriptionJobResponse)

    async def get_medical_vocabulary(
        self,
        request: TranscribeGetMedicalVocabularyRequest,
    ) -> TranscribeGetMedicalVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.get_medical_vocabulary, request, TranscribeGetMedicalVocabularyResponse)

    async def get_transcription_job(
        self,
        request: TranscribeGetTranscriptionJobRequest,
    ) -> TranscribeGetTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.get_transcription_job, request, TranscribeGetTranscriptionJobResponse)

    async def get_vocabulary(
        self,
        request: TranscribeGetVocabularyRequest,
    ) -> TranscribeGetVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.get_vocabulary, request, TranscribeGetVocabularyResponse)

    async def get_vocabulary_filter(
        self,
        request: TranscribeGetVocabularyFilterRequest,
    ) -> TranscribeGetVocabularyFilterResponse:
        client = self._require_client()
        return await self._execute(client.get_vocabulary_filter, request, TranscribeGetVocabularyFilterResponse)

    async def list_call_analytics_categories(
        self,
        request: TranscribeListCallAnalyticsCategoriesRequest | None = None,
    ) -> TranscribeListCallAnalyticsCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.list_call_analytics_categories, request, TranscribeListCallAnalyticsCategoriesResponse)

    async def list_call_analytics_jobs(
        self,
        request: TranscribeListCallAnalyticsJobsRequest | None = None,
    ) -> TranscribeListCallAnalyticsJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_call_analytics_jobs, request, TranscribeListCallAnalyticsJobsResponse)

    async def list_language_models(
        self,
        request: TranscribeListLanguageModelsRequest | None = None,
    ) -> TranscribeListLanguageModelsResponse:
        client = self._require_client()
        return await self._execute(client.list_language_models, request, TranscribeListLanguageModelsResponse)

    async def list_medical_scribe_jobs(
        self,
        request: TranscribeListMedicalScribeJobsRequest | None = None,
    ) -> TranscribeListMedicalScribeJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_medical_scribe_jobs, request, TranscribeListMedicalScribeJobsResponse)

    async def list_medical_transcription_jobs(
        self,
        request: TranscribeListMedicalTranscriptionJobsRequest | None = None,
    ) -> TranscribeListMedicalTranscriptionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_medical_transcription_jobs, request, TranscribeListMedicalTranscriptionJobsResponse)

    async def list_medical_vocabularies(
        self,
        request: TranscribeListMedicalVocabulariesRequest | None = None,
    ) -> TranscribeListMedicalVocabulariesResponse:
        client = self._require_client()
        return await self._execute(client.list_medical_vocabularies, request, TranscribeListMedicalVocabulariesResponse)

    async def list_tags_for_resource(
        self,
        request: TranscribeListTagsForResourceRequest,
    ) -> TranscribeListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TranscribeListTagsForResourceResponse)

    async def list_transcription_jobs(
        self,
        request: TranscribeListTranscriptionJobsRequest | None = None,
    ) -> TranscribeListTranscriptionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_transcription_jobs, request, TranscribeListTranscriptionJobsResponse)

    async def list_vocabularies(
        self,
        request: TranscribeListVocabulariesRequest | None = None,
    ) -> TranscribeListVocabulariesResponse:
        client = self._require_client()
        return await self._execute(client.list_vocabularies, request, TranscribeListVocabulariesResponse)

    async def list_vocabulary_filters(
        self,
        request: TranscribeListVocabularyFiltersRequest | None = None,
    ) -> TranscribeListVocabularyFiltersResponse:
        client = self._require_client()
        return await self._execute(client.list_vocabulary_filters, request, TranscribeListVocabularyFiltersResponse)

    async def start_call_analytics_job(
        self,
        request: TranscribeStartCallAnalyticsJobRequest,
    ) -> TranscribeStartCallAnalyticsJobResponse:
        client = self._require_client()
        return await self._execute(client.start_call_analytics_job, request, TranscribeStartCallAnalyticsJobResponse)

    async def start_medical_scribe_job(
        self,
        request: TranscribeStartMedicalScribeJobRequest,
    ) -> TranscribeStartMedicalScribeJobResponse:
        client = self._require_client()
        return await self._execute(client.start_medical_scribe_job, request, TranscribeStartMedicalScribeJobResponse)

    async def start_medical_transcription_job(
        self,
        request: TranscribeStartMedicalTranscriptionJobRequest,
    ) -> TranscribeStartMedicalTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_medical_transcription_job, request, TranscribeStartMedicalTranscriptionJobResponse)

    async def start_transcription_job(
        self,
        request: TranscribeStartTranscriptionJobRequest,
    ) -> TranscribeStartTranscriptionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_transcription_job, request, TranscribeStartTranscriptionJobResponse)

    async def tag_resource(
        self,
        request: TranscribeTagResourceRequest,
    ) -> TranscribeTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TranscribeTagResourceResponse)

    async def transcribe_audio(
        self,
        request: TranscribeTranscribeAudioRequest,
    ) -> TranscribeTranscribeAudioResponse:
        client = self._require_client()
        return await self._execute(client.transcribe_audio, request, TranscribeTranscribeAudioResponse)

    async def untag_resource(
        self,
        request: TranscribeUntagResourceRequest,
    ) -> TranscribeUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TranscribeUntagResourceResponse)

    async def update_call_analytics_category(
        self,
        request: TranscribeUpdateCallAnalyticsCategoryRequest,
    ) -> TranscribeUpdateCallAnalyticsCategoryResponse:
        client = self._require_client()
        return await self._execute(client.update_call_analytics_category, request, TranscribeUpdateCallAnalyticsCategoryResponse)

    async def update_language_model(
        self,
        request: TranscribeUpdateLanguageModelRequest,
    ) -> TranscribeUpdateLanguageModelResponse:
        client = self._require_client()
        return await self._execute(client.update_language_model, request, TranscribeUpdateLanguageModelResponse)

    async def update_medical_vocabulary(
        self,
        request: TranscribeUpdateMedicalVocabularyRequest,
    ) -> TranscribeUpdateMedicalVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.update_medical_vocabulary, request, TranscribeUpdateMedicalVocabularyResponse)

    async def update_vocabulary(
        self,
        request: TranscribeUpdateVocabularyRequest,
    ) -> TranscribeUpdateVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.update_vocabulary, request, TranscribeUpdateVocabularyResponse)

    async def update_vocabulary_filter(
        self,
        request: TranscribeUpdateVocabularyFilterRequest,
    ) -> TranscribeUpdateVocabularyFilterResponse:
        client = self._require_client()
        return await self._execute(client.update_vocabulary_filter, request, TranscribeUpdateVocabularyFilterResponse)
