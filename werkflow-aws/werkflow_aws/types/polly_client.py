from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class PollyClient(ABC):

    @abstractmethod
    def create_voice(
        self,
        *,
        Name: str,
        LanguageCode: str,
        TermsAccepted: bool,
        VoiceCreationData: dict[str, Any],
        CustomerManagedEncryption: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lexicon(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_voice(
        self,
        *,
        VoiceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_voices(
        self,
        *,
        Engine: str | None = None,
        LanguageCode: str | None = None,
        IncludeAdditionalLanguageCodes: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lexicon(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_speech_synthesis_task(
        self,
        *,
        TaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_voice(
        self,
        *,
        VoiceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lexicons(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_speech_synthesis_tasks(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_lexicon(
        self,
        *,
        Name: str,
        Content: str,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_speech_synthesis_stream(
        self,
        *,
        Engine: str,
        OutputFormat: str,
        VoiceId: str,
        LanguageCode: str | None = None,
        LexiconNames: list[str] | None = None,
        SampleRate: str | None = None,
        ActionStream: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_speech_synthesis_task(
        self,
        *,
        OutputFormat: str,
        OutputS3BucketName: str,
        Text: str,
        VoiceId: str,
        Engine: str | None = None,
        LanguageCode: str | None = None,
        LexiconNames: list[str] | None = None,
        OutputS3KeyPrefix: str | None = None,
        SampleRate: str | None = None,
        SnsTopicArn: str | None = None,
        SpeechMarkTypes: list[str] | None = None,
        TextType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def synthesize_speech(
        self,
        *,
        OutputFormat: str,
        Text: str,
        VoiceId: str,
        Engine: str | None = None,
        LanguageCode: str | None = None,
        LexiconNames: list[str] | None = None,
        SampleRate: str | None = None,
        SpeechMarkTypes: list[str] | None = None,
        TextType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
