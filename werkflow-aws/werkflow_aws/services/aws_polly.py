from werkflow_aws.models.polly import (
    PollyCreateVoiceRequest,
    PollyCreateVoiceResponse,
    PollyDeleteLexiconRequest,
    PollyDeleteLexiconResponse,
    PollyDeleteVoiceRequest,
    PollyDeleteVoiceResponse,
    PollyDescribeVoicesRequest,
    PollyDescribeVoicesResponse,
    PollyGetLexiconRequest,
    PollyGetLexiconResponse,
    PollyGetSpeechSynthesisTaskRequest,
    PollyGetSpeechSynthesisTaskResponse,
    PollyGetVoiceRequest,
    PollyGetVoiceResponse,
    PollyListLexiconsRequest,
    PollyListLexiconsResponse,
    PollyListSpeechSynthesisTasksRequest,
    PollyListSpeechSynthesisTasksResponse,
    PollyListTagsForResourceRequest,
    PollyListTagsForResourceResponse,
    PollyPutLexiconRequest,
    PollyPutLexiconResponse,
    PollyStartSpeechSynthesisStreamRequest,
    PollyStartSpeechSynthesisStreamResponse,
    PollyStartSpeechSynthesisTaskRequest,
    PollyStartSpeechSynthesisTaskResponse,
    PollySynthesizeSpeechRequest,
    PollySynthesizeSpeechResponse,
    PollyTagResourceRequest,
    PollyTagResourceResponse,
    PollyUntagResourceRequest,
    PollyUntagResourceResponse,
)
from werkflow_aws.types.polly_client import PollyClient
from .base import AWSBaseService


class AWSPolly(AWSBaseService[PollyClient]):
    service_name = 'polly'
    boto3_service_name = 'polly'

    def __init__(self) -> None:
        super().__init__(service_name='polly', boto3_service_name='polly')

    async def create_voice(
        self,
        request: PollyCreateVoiceRequest,
    ) -> PollyCreateVoiceResponse:
        client = self._require_client()
        return await self._execute(client.create_voice, request, PollyCreateVoiceResponse)

    async def delete_lexicon(
        self,
        request: PollyDeleteLexiconRequest,
    ) -> PollyDeleteLexiconResponse:
        client = self._require_client()
        return await self._execute(client.delete_lexicon, request, PollyDeleteLexiconResponse)

    async def delete_voice(
        self,
        request: PollyDeleteVoiceRequest,
    ) -> PollyDeleteVoiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_voice, request, PollyDeleteVoiceResponse)

    async def describe_voices(
        self,
        request: PollyDescribeVoicesRequest | None = None,
    ) -> PollyDescribeVoicesResponse:
        client = self._require_client()
        return await self._execute(client.describe_voices, request, PollyDescribeVoicesResponse)

    async def describe_voices_paginated(
        self,
        request: PollyDescribeVoicesRequest | None = None,
    ) -> list[PollyDescribeVoicesResponse]:
        return await self._paginate('describe_voices', request, PollyDescribeVoicesResponse)

    async def get_lexicon(
        self,
        request: PollyGetLexiconRequest,
    ) -> PollyGetLexiconResponse:
        client = self._require_client()
        return await self._execute(client.get_lexicon, request, PollyGetLexiconResponse)

    async def get_speech_synthesis_task(
        self,
        request: PollyGetSpeechSynthesisTaskRequest,
    ) -> PollyGetSpeechSynthesisTaskResponse:
        client = self._require_client()
        return await self._execute(client.get_speech_synthesis_task, request, PollyGetSpeechSynthesisTaskResponse)

    async def get_voice(
        self,
        request: PollyGetVoiceRequest,
    ) -> PollyGetVoiceResponse:
        client = self._require_client()
        return await self._execute(client.get_voice, request, PollyGetVoiceResponse)

    async def list_lexicons(
        self,
        request: PollyListLexiconsRequest | None = None,
    ) -> PollyListLexiconsResponse:
        client = self._require_client()
        return await self._execute(client.list_lexicons, request, PollyListLexiconsResponse)

    async def list_lexicons_paginated(
        self,
        request: PollyListLexiconsRequest | None = None,
    ) -> list[PollyListLexiconsResponse]:
        return await self._paginate('list_lexicons', request, PollyListLexiconsResponse)

    async def list_speech_synthesis_tasks(
        self,
        request: PollyListSpeechSynthesisTasksRequest | None = None,
    ) -> PollyListSpeechSynthesisTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_speech_synthesis_tasks, request, PollyListSpeechSynthesisTasksResponse)

    async def list_speech_synthesis_tasks_paginated(
        self,
        request: PollyListSpeechSynthesisTasksRequest | None = None,
    ) -> list[PollyListSpeechSynthesisTasksResponse]:
        return await self._paginate('list_speech_synthesis_tasks', request, PollyListSpeechSynthesisTasksResponse)

    async def list_tags_for_resource(
        self,
        request: PollyListTagsForResourceRequest,
    ) -> PollyListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, PollyListTagsForResourceResponse)

    async def put_lexicon(
        self,
        request: PollyPutLexiconRequest,
    ) -> PollyPutLexiconResponse:
        client = self._require_client()
        return await self._execute(client.put_lexicon, request, PollyPutLexiconResponse)

    async def start_speech_synthesis_stream(
        self,
        request: PollyStartSpeechSynthesisStreamRequest,
    ) -> PollyStartSpeechSynthesisStreamResponse:
        client = self._require_client()
        return await self._execute(client.start_speech_synthesis_stream, request, PollyStartSpeechSynthesisStreamResponse)

    async def start_speech_synthesis_task(
        self,
        request: PollyStartSpeechSynthesisTaskRequest,
    ) -> PollyStartSpeechSynthesisTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_speech_synthesis_task, request, PollyStartSpeechSynthesisTaskResponse)

    async def synthesize_speech(
        self,
        request: PollySynthesizeSpeechRequest,
    ) -> PollySynthesizeSpeechResponse:
        client = self._require_client()
        return await self._execute(client.synthesize_speech, request, PollySynthesizeSpeechResponse)

    async def tag_resource(
        self,
        request: PollyTagResourceRequest,
    ) -> PollyTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, PollyTagResourceResponse)

    async def untag_resource(
        self,
        request: PollyUntagResourceRequest,
    ) -> PollyUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, PollyUntagResourceResponse)
