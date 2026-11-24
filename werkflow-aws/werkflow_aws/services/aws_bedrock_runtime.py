from werkflow_aws.models.bedrock_runtime import (
    BedrockRuntimeApplyGuardrailRequest,
    BedrockRuntimeApplyGuardrailResponse,
    BedrockRuntimeConverseRequest,
    BedrockRuntimeConverseResponse,
    BedrockRuntimeConverseStreamRequest,
    BedrockRuntimeConverseStreamResponse,
    BedrockRuntimeCountTokensRequest,
    BedrockRuntimeCountTokensResponse,
    BedrockRuntimeGetAsyncInvokeRequest,
    BedrockRuntimeGetAsyncInvokeResponse,
    BedrockRuntimeInvokeGuardrailChecksRequest,
    BedrockRuntimeInvokeGuardrailChecksResponse,
    BedrockRuntimeInvokeModelRequest,
    BedrockRuntimeInvokeModelResponse,
    BedrockRuntimeInvokeModelWithBidirectionalStreamRequest,
    BedrockRuntimeInvokeModelWithBidirectionalStreamResponse,
    BedrockRuntimeInvokeModelWithResponseStreamRequest,
    BedrockRuntimeInvokeModelWithResponseStreamResponse,
    BedrockRuntimeListAsyncInvokesRequest,
    BedrockRuntimeListAsyncInvokesResponse,
    BedrockRuntimeStartAsyncInvokeRequest,
    BedrockRuntimeStartAsyncInvokeResponse,
)
from werkflow_aws.types.bedrock_runtime_client import BedrockRuntimeClient
from .base import AWSBaseService


class AWSBedrockRuntime(AWSBaseService[BedrockRuntimeClient]):
    service_name = 'bedrock-runtime'
    boto3_service_name = 'bedrock-runtime'

    def __init__(self) -> None:
        super().__init__(service_name='bedrock-runtime', boto3_service_name='bedrock-runtime')

    async def apply_guardrail(
        self,
        request: BedrockRuntimeApplyGuardrailRequest,
    ) -> BedrockRuntimeApplyGuardrailResponse:
        client = self._require_client()
        return await self._execute(client.apply_guardrail, request, BedrockRuntimeApplyGuardrailResponse)

    async def converse(
        self,
        request: BedrockRuntimeConverseRequest,
    ) -> BedrockRuntimeConverseResponse:
        client = self._require_client()
        return await self._execute(client.converse, request, BedrockRuntimeConverseResponse)

    async def converse_stream(
        self,
        request: BedrockRuntimeConverseStreamRequest,
    ) -> BedrockRuntimeConverseStreamResponse:
        client = self._require_client()
        return await self._execute(client.converse_stream, request, BedrockRuntimeConverseStreamResponse)

    async def count_tokens(
        self,
        request: BedrockRuntimeCountTokensRequest,
    ) -> BedrockRuntimeCountTokensResponse:
        client = self._require_client()
        return await self._execute(client.count_tokens, request, BedrockRuntimeCountTokensResponse)

    async def get_async_invoke(
        self,
        request: BedrockRuntimeGetAsyncInvokeRequest,
    ) -> BedrockRuntimeGetAsyncInvokeResponse:
        client = self._require_client()
        return await self._execute(client.get_async_invoke, request, BedrockRuntimeGetAsyncInvokeResponse)

    async def invoke_guardrail_checks(
        self,
        request: BedrockRuntimeInvokeGuardrailChecksRequest,
    ) -> BedrockRuntimeInvokeGuardrailChecksResponse:
        client = self._require_client()
        return await self._execute(client.invoke_guardrail_checks, request, BedrockRuntimeInvokeGuardrailChecksResponse)

    async def invoke_model(
        self,
        request: BedrockRuntimeInvokeModelRequest,
    ) -> BedrockRuntimeInvokeModelResponse:
        client = self._require_client()
        return await self._execute(client.invoke_model, request, BedrockRuntimeInvokeModelResponse)

    async def invoke_model_with_bidirectional_stream(
        self,
        request: BedrockRuntimeInvokeModelWithBidirectionalStreamRequest,
    ) -> BedrockRuntimeInvokeModelWithBidirectionalStreamResponse:
        client = self._require_client()
        return await self._execute(client.invoke_model_with_bidirectional_stream, request, BedrockRuntimeInvokeModelWithBidirectionalStreamResponse)

    async def invoke_model_with_response_stream(
        self,
        request: BedrockRuntimeInvokeModelWithResponseStreamRequest,
    ) -> BedrockRuntimeInvokeModelWithResponseStreamResponse:
        client = self._require_client()
        return await self._execute(client.invoke_model_with_response_stream, request, BedrockRuntimeInvokeModelWithResponseStreamResponse)

    async def list_async_invokes(
        self,
        request: BedrockRuntimeListAsyncInvokesRequest | None = None,
    ) -> BedrockRuntimeListAsyncInvokesResponse:
        client = self._require_client()
        return await self._execute(client.list_async_invokes, request, BedrockRuntimeListAsyncInvokesResponse)

    async def list_async_invokes_paginated(
        self,
        request: BedrockRuntimeListAsyncInvokesRequest | None = None,
    ) -> list[BedrockRuntimeListAsyncInvokesResponse]:
        return await self._paginate('list_async_invokes', request, BedrockRuntimeListAsyncInvokesResponse)

    async def start_async_invoke(
        self,
        request: BedrockRuntimeStartAsyncInvokeRequest,
    ) -> BedrockRuntimeStartAsyncInvokeResponse:
        client = self._require_client()
        return await self._execute(client.start_async_invoke, request, BedrockRuntimeStartAsyncInvokeResponse)
