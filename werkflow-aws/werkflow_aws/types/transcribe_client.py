from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class TranscribeClient(ABC):

    @abstractmethod
    def create_call_analytics_category(
        self,
        *,
        CategoryName: str,
        Rules: list[dict[str, Any]],
        Tags: list[dict[str, Any]] | None = None,
        InputType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_language_model(
        self,
        *,
        LanguageCode: str,
        BaseModelName: str,
        ModelName: str,
        InputDataConfig: dict[str, Any],
        EncryptionConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: str,
        VocabularyFileUri: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: list[str] | None = None,
        VocabularyFileUri: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataAccessRoleArn: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        LanguageCode: str,
        Words: list[str] | None = None,
        VocabularyFilterFileUri: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataAccessRoleArn: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_call_analytics_category(
        self,
        *,
        CategoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_call_analytics_job(
        self,
        *,
        CallAnalyticsJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_language_model(
        self,
        *,
        ModelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_medical_scribe_job(
        self,
        *,
        MedicalScribeJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vocabulary(
        self,
        *,
        VocabularyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_language_model(
        self,
        *,
        ModelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_call_analytics_category(
        self,
        *,
        CategoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_call_analytics_job(
        self,
        *,
        CallAnalyticsJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_medical_scribe_job(
        self,
        *,
        MedicalScribeJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vocabulary(
        self,
        *,
        VocabularyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_call_analytics_categories(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_call_analytics_jobs(
        self,
        *,
        Status: str | None = None,
        JobNameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_language_models(
        self,
        *,
        StatusEquals: str | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_medical_scribe_jobs(
        self,
        *,
        Status: str | None = None,
        JobNameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_medical_transcription_jobs(
        self,
        *,
        Status: str | None = None,
        JobNameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_medical_vocabularies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StateEquals: str | None = None,
        NameContains: str | None = None,
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
    def list_transcription_jobs(
        self,
        *,
        Status: str | None = None,
        JobNameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vocabularies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StateEquals: str | None = None,
        NameContains: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vocabulary_filters(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_call_analytics_job(
        self,
        *,
        CallAnalyticsJobName: str,
        Media: dict[str, Any],
        OutputLocation: str | None = None,
        OutputEncryptionKMSKeyId: str | None = None,
        DataAccessRoleArn: str | None = None,
        Settings: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ChannelDefinitions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_medical_scribe_job(
        self,
        *,
        MedicalScribeJobName: str,
        Media: dict[str, Any],
        OutputBucketName: str,
        DataAccessRoleArn: str,
        Settings: dict[str, Any],
        OutputEncryptionKMSKeyId: str | None = None,
        KMSEncryptionContext: dict[str, str] | None = None,
        ChannelDefinitions: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        MedicalScribeContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
        LanguageCode: str,
        Media: dict[str, Any],
        OutputBucketName: str,
        Specialty: str,
        Type: str,
        MediaSampleRateHertz: int | None = None,
        MediaFormat: str | None = None,
        OutputKey: str | None = None,
        OutputEncryptionKMSKeyId: str | None = None,
        KMSEncryptionContext: dict[str, str] | None = None,
        Settings: dict[str, Any] | None = None,
        ContentIdentificationType: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
        Media: dict[str, Any],
        LanguageCode: str | None = None,
        MediaSampleRateHertz: int | None = None,
        MediaFormat: str | None = None,
        OutputBucketName: str | None = None,
        OutputKey: str | None = None,
        OutputEncryptionKMSKeyId: str | None = None,
        KMSEncryptionContext: dict[str, str] | None = None,
        Settings: dict[str, Any] | None = None,
        ModelSettings: dict[str, Any] | None = None,
        JobExecutionSettings: dict[str, Any] | None = None,
        ContentRedaction: dict[str, Any] | None = None,
        IdentifyLanguage: bool | None = None,
        IdentifyMultipleLanguages: bool | None = None,
        LanguageOptions: list[str] | None = None,
        Subtitles: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        LanguageIdSettings: dict[str, dict[str, Any]] | None = None,
        ToxicityDetection: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transcribe_audio(
        self,
        *,
        Media: dict[str, Any],
        Language: str | None = None,
        LanguageDetectionMode: str | None = None,
        LanguageOptions: list[str] | None = None,
        ChannelIdentification: bool | None = None,
        ShowSpeakerLabels: bool | None = None,
        MaxSpeakerLabels: int | None = None,
        VocabularySettings: list[dict[str, Any]] | None = None,
        VocabularyFilterSettings: dict[str, Any] | None = None,
        ContentRedaction: dict[str, Any] | None = None,
        OutputConfiguration: dict[str, Any] | None = None,
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
    def update_call_analytics_category(
        self,
        *,
        CategoryName: str,
        Rules: list[dict[str, Any]],
        InputType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_language_model(
        self,
        *,
        ModelName: str,
        DataAccessRoleArn: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: str,
        VocabularyFileUri: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: list[str] | None = None,
        VocabularyFileUri: str | None = None,
        DataAccessRoleArn: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        Words: list[str] | None = None,
        VocabularyFilterFileUri: str | None = None,
        DataAccessRoleArn: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
