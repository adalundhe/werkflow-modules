from werkflow_aws.models.translate import (
    TranslateCreateParallelDataRequest,
    TranslateCreateParallelDataResponse,
    TranslateDeleteParallelDataRequest,
    TranslateDeleteParallelDataResponse,
    TranslateDeleteTerminologyRequest,
    TranslateDeleteTerminologyResponse,
    TranslateDescribeTextTranslationJobRequest,
    TranslateDescribeTextTranslationJobResponse,
    TranslateGetParallelDataRequest,
    TranslateGetParallelDataResponse,
    TranslateGetTerminologyRequest,
    TranslateGetTerminologyResponse,
    TranslateImportTerminologyRequest,
    TranslateImportTerminologyResponse,
    TranslateListLanguagesRequest,
    TranslateListLanguagesResponse,
    TranslateListParallelDataRequest,
    TranslateListParallelDataResponse,
    TranslateListTagsForResourceRequest,
    TranslateListTagsForResourceResponse,
    TranslateListTerminologiesRequest,
    TranslateListTerminologiesResponse,
    TranslateListTextTranslationJobsRequest,
    TranslateListTextTranslationJobsResponse,
    TranslateStartTextTranslationJobRequest,
    TranslateStartTextTranslationJobResponse,
    TranslateStopTextTranslationJobRequest,
    TranslateStopTextTranslationJobResponse,
    TranslateTagResourceRequest,
    TranslateTagResourceResponse,
    TranslateTranslateDocumentRequest,
    TranslateTranslateDocumentResponse,
    TranslateTranslateTextRequest,
    TranslateTranslateTextResponse,
    TranslateUntagResourceRequest,
    TranslateUntagResourceResponse,
    TranslateUpdateParallelDataRequest,
    TranslateUpdateParallelDataResponse,
)
from werkflow_aws.types.translate_client import TranslateClient
from .base import AWSBaseService


class AWSTranslate(AWSBaseService[TranslateClient]):
    service_name = 'translate'
    boto3_service_name = 'translate'

    def __init__(self) -> None:
        super().__init__(service_name='translate', boto3_service_name='translate')

    async def create_parallel_data(
        self,
        request: TranslateCreateParallelDataRequest,
    ) -> TranslateCreateParallelDataResponse:
        client = self._require_client()
        return await self._execute(client.create_parallel_data, request, TranslateCreateParallelDataResponse)

    async def delete_parallel_data(
        self,
        request: TranslateDeleteParallelDataRequest,
    ) -> TranslateDeleteParallelDataResponse:
        client = self._require_client()
        return await self._execute(client.delete_parallel_data, request, TranslateDeleteParallelDataResponse)

    async def delete_terminology(
        self,
        request: TranslateDeleteTerminologyRequest,
    ) -> TranslateDeleteTerminologyResponse:
        client = self._require_client()
        return await self._execute(client.delete_terminology, request, TranslateDeleteTerminologyResponse)

    async def describe_text_translation_job(
        self,
        request: TranslateDescribeTextTranslationJobRequest,
    ) -> TranslateDescribeTextTranslationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_text_translation_job, request, TranslateDescribeTextTranslationJobResponse)

    async def get_parallel_data(
        self,
        request: TranslateGetParallelDataRequest,
    ) -> TranslateGetParallelDataResponse:
        client = self._require_client()
        return await self._execute(client.get_parallel_data, request, TranslateGetParallelDataResponse)

    async def get_terminology(
        self,
        request: TranslateGetTerminologyRequest,
    ) -> TranslateGetTerminologyResponse:
        client = self._require_client()
        return await self._execute(client.get_terminology, request, TranslateGetTerminologyResponse)

    async def import_terminology(
        self,
        request: TranslateImportTerminologyRequest,
    ) -> TranslateImportTerminologyResponse:
        client = self._require_client()
        return await self._execute(client.import_terminology, request, TranslateImportTerminologyResponse)

    async def list_languages(
        self,
        request: TranslateListLanguagesRequest | None = None,
    ) -> TranslateListLanguagesResponse:
        client = self._require_client()
        return await self._execute(client.list_languages, request, TranslateListLanguagesResponse)

    async def list_parallel_data(
        self,
        request: TranslateListParallelDataRequest | None = None,
    ) -> TranslateListParallelDataResponse:
        client = self._require_client()
        return await self._execute(client.list_parallel_data, request, TranslateListParallelDataResponse)

    async def list_tags_for_resource(
        self,
        request: TranslateListTagsForResourceRequest,
    ) -> TranslateListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TranslateListTagsForResourceResponse)

    async def list_terminologies(
        self,
        request: TranslateListTerminologiesRequest | None = None,
    ) -> TranslateListTerminologiesResponse:
        client = self._require_client()
        return await self._execute(client.list_terminologies, request, TranslateListTerminologiesResponse)

    async def list_terminologies_paginated(
        self,
        request: TranslateListTerminologiesRequest | None = None,
    ) -> list[TranslateListTerminologiesResponse]:
        return await self._paginate('list_terminologies', request, TranslateListTerminologiesResponse)

    async def list_text_translation_jobs(
        self,
        request: TranslateListTextTranslationJobsRequest | None = None,
    ) -> TranslateListTextTranslationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_text_translation_jobs, request, TranslateListTextTranslationJobsResponse)

    async def start_text_translation_job(
        self,
        request: TranslateStartTextTranslationJobRequest,
    ) -> TranslateStartTextTranslationJobResponse:
        client = self._require_client()
        return await self._execute(client.start_text_translation_job, request, TranslateStartTextTranslationJobResponse)

    async def stop_text_translation_job(
        self,
        request: TranslateStopTextTranslationJobRequest,
    ) -> TranslateStopTextTranslationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_text_translation_job, request, TranslateStopTextTranslationJobResponse)

    async def tag_resource(
        self,
        request: TranslateTagResourceRequest,
    ) -> TranslateTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TranslateTagResourceResponse)

    async def translate_document(
        self,
        request: TranslateTranslateDocumentRequest,
    ) -> TranslateTranslateDocumentResponse:
        client = self._require_client()
        return await self._execute(client.translate_document, request, TranslateTranslateDocumentResponse)

    async def translate_text(
        self,
        request: TranslateTranslateTextRequest,
    ) -> TranslateTranslateTextResponse:
        client = self._require_client()
        return await self._execute(client.translate_text, request, TranslateTranslateTextResponse)

    async def untag_resource(
        self,
        request: TranslateUntagResourceRequest,
    ) -> TranslateUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TranslateUntagResourceResponse)

    async def update_parallel_data(
        self,
        request: TranslateUpdateParallelDataRequest,
    ) -> TranslateUpdateParallelDataResponse:
        client = self._require_client()
        return await self._execute(client.update_parallel_data, request, TranslateUpdateParallelDataResponse)
