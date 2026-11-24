from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class BedrockRuntimeClient(ABC):

    @abstractmethod
    def apply_guardrail(
        self,
        *,
        guardrailIdentifier: str,
        guardrailVersion: str,
        source: str,
        content: list[dict[str, Any]],
        outputScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def converse(
        self,
        *,
        modelId: str,
        messages: list[dict[str, Any]] | None = None,
        system: list[dict[str, Any]] | None = None,
        inferenceConfig: dict[str, Any] | None = None,
        toolConfig: dict[str, Any] | None = None,
        guardrailConfig: dict[str, Any] | None = None,
        projectIdentifier: str | None = None,
        additionalModelRequestFields: dict[str, Any] | None = None,
        promptVariables: dict[str, dict[str, Any]] | None = None,
        additionalModelResponseFieldPaths: list[str] | None = None,
        requestMetadata: dict[str, str] | None = None,
        performanceConfig: dict[str, Any] | None = None,
        serviceTier: dict[str, Any] | None = None,
        outputConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def converse_stream(
        self,
        *,
        modelId: str,
        messages: list[dict[str, Any]] | None = None,
        system: list[dict[str, Any]] | None = None,
        inferenceConfig: dict[str, Any] | None = None,
        toolConfig: dict[str, Any] | None = None,
        guardrailConfig: dict[str, Any] | None = None,
        projectIdentifier: str | None = None,
        additionalModelRequestFields: dict[str, Any] | None = None,
        promptVariables: dict[str, dict[str, Any]] | None = None,
        additionalModelResponseFieldPaths: list[str] | None = None,
        requestMetadata: dict[str, str] | None = None,
        performanceConfig: dict[str, Any] | None = None,
        serviceTier: dict[str, Any] | None = None,
        outputConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def count_tokens(
        self,
        *,
        modelId: str,
        input: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_async_invoke(
        self,
        *,
        invocationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_guardrail_checks(
        self,
        *,
        messages: list[dict[str, Any]],
        checks: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_model(
        self,
        *,
        modelId: str,
        body: bytes | BinaryIO | str | None = None,
        contentType: str | None = None,
        accept: str | None = None,
        trace: str | None = None,
        guardrailIdentifier: str | None = None,
        guardrailVersion: str | None = None,
        performanceConfigLatency: str | None = None,
        serviceTier: str | None = None,
        requestMetadata: str | None = None,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_model_with_bidirectional_stream(
        self,
        *,
        modelId: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_model_with_response_stream(
        self,
        *,
        modelId: str,
        body: bytes | BinaryIO | str | None = None,
        contentType: str | None = None,
        accept: str | None = None,
        trace: str | None = None,
        guardrailIdentifier: str | None = None,
        guardrailVersion: str | None = None,
        performanceConfigLatency: str | None = None,
        serviceTier: str | None = None,
        requestMetadata: str | None = None,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_async_invokes(
        self,
        *,
        submitTimeAfter: datetime.datetime | str | None = None,
        submitTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_async_invoke(
        self,
        *,
        modelId: str,
        modelInput: dict[str, Any],
        outputDataConfig: dict[str, Any],
        clientRequestToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
