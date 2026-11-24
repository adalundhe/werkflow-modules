from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class TranslateClient(ABC):

    @abstractmethod
    def create_parallel_data(
        self,
        *,
        Name: str,
        ParallelDataConfig: dict[str, Any],
        ClientToken: str,
        Description: str | None = None,
        EncryptionKey: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_parallel_data(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_terminology(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_text_translation_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parallel_data(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_terminology(
        self,
        *,
        Name: str,
        TerminologyDataFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_terminology(
        self,
        *,
        Name: str,
        MergeStrategy: str,
        TerminologyData: dict[str, Any],
        Description: str | None = None,
        EncryptionKey: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_languages(
        self,
        *,
        DisplayLanguageCode: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_parallel_data(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
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
    def list_terminologies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_text_translation_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_text_translation_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        SourceLanguageCode: str,
        TargetLanguageCodes: list[str],
        ClientToken: str,
        JobName: str | None = None,
        TerminologyNames: list[str] | None = None,
        ParallelDataNames: list[str] | None = None,
        Settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_text_translation_job(
        self,
        *,
        JobId: str,
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
    def translate_document(
        self,
        *,
        Document: dict[str, Any],
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: list[str] | None = None,
        Settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def translate_text(
        self,
        *,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: list[str] | None = None,
        Settings: dict[str, Any] | None = None,
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
    def update_parallel_data(
        self,
        *,
        Name: str,
        ParallelDataConfig: dict[str, Any],
        ClientToken: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
