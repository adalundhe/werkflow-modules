from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class TextractClient(ABC):

    @abstractmethod
    def analyze_document(
        self,
        *,
        Document: dict[str, Any],
        FeatureTypes: list[str],
        HumanLoopConfig: dict[str, Any] | None = None,
        QueriesConfig: dict[str, Any] | None = None,
        AdaptersConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def analyze_expense(
        self,
        *,
        Document: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def analyze_id(
        self,
        *,
        DocumentPages: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_adapter(
        self,
        *,
        AdapterName: str,
        FeatureTypes: list[str],
        ClientRequestToken: str | None = None,
        Description: str | None = None,
        AutoUpdate: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_adapter_version(
        self,
        *,
        AdapterId: str,
        DatasetConfig: dict[str, Any],
        OutputConfig: dict[str, Any],
        ClientRequestToken: str | None = None,
        KMSKeyId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_blueprint(
        self,
        *,
        BlueprintName: str,
        Schema: str,
        ClientRequestToken: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_blueprint_version(
        self,
        *,
        BlueprintArn: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        ProjectName: str,
        ExtractionConfiguration: dict[str, Any],
        ClientRequestToken: str | None = None,
        ProjectDescription: str | None = None,
        GenerativeConfiguration: dict[str, Any] | None = None,
        CustomConfiguration: dict[str, Any] | None = None,
        SplitterConfiguration: dict[str, Any] | None = None,
        SensitiveDataConfiguration: dict[str, Any] | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_adapter(
        self,
        *,
        AdapterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_adapter_version(
        self,
        *,
        AdapterId: str,
        AdapterVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_blueprint(
        self,
        *,
        BlueprintArn: str,
        BlueprintVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        ProjectArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_document_text(
        self,
        *,
        Document: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_adapter(
        self,
        *,
        AdapterId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_adapter_version(
        self,
        *,
        AdapterId: str,
        AdapterVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blueprint(
        self,
        *,
        BlueprintArn: str,
        BlueprintVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_document_analysis(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_document_insights(
        self,
        *,
        JobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_document_text_detection(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_expense_analysis(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lending_analysis(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lending_analysis_summary(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project(
        self,
        *,
        ProjectArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_adapter_versions(
        self,
        *,
        AdapterId: str | None = None,
        AfterCreationTime: datetime.datetime | str | None = None,
        BeforeCreationTime: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_adapters(
        self,
        *,
        AfterCreationTime: datetime.datetime | str | None = None,
        BeforeCreationTime: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_blueprints(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        BlueprintArn: str | None = None,
        ProjectFilter: dict[str, Any] | None = None,
        ResourceOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        BlueprintFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_document_analysis(
        self,
        *,
        DocumentLocation: dict[str, Any],
        FeatureTypes: list[str],
        ClientRequestToken: str | None = None,
        JobTag: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        OutputConfig: dict[str, Any] | None = None,
        KMSKeyId: str | None = None,
        QueriesConfig: dict[str, Any] | None = None,
        AdaptersConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_document_insights(
        self,
        *,
        InputConfiguration: dict[str, Any],
        OutputConfiguration: dict[str, Any],
        ProjectArn: str | None = None,
        Blueprints: list[dict[str, Any]] | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
        NotificationConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_document_text_detection(
        self,
        *,
        DocumentLocation: dict[str, Any],
        ClientRequestToken: str | None = None,
        JobTag: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        OutputConfig: dict[str, Any] | None = None,
        KMSKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_expense_analysis(
        self,
        *,
        DocumentLocation: dict[str, Any],
        ClientRequestToken: str | None = None,
        JobTag: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        OutputConfig: dict[str, Any] | None = None,
        KMSKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_lending_analysis(
        self,
        *,
        DocumentLocation: dict[str, Any],
        ClientRequestToken: str | None = None,
        JobTag: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        OutputConfig: dict[str, Any] | None = None,
        KMSKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_adapter(
        self,
        *,
        AdapterId: str,
        Description: str | None = None,
        AdapterName: str | None = None,
        AutoUpdate: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_blueprint(
        self,
        *,
        BlueprintArn: str,
        Schema: str | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        ProjectArn: str,
        ProjectDescription: str | None = None,
        ExtractionConfiguration: dict[str, Any] | None = None,
        GenerativeConfiguration: dict[str, Any] | None = None,
        CustomConfiguration: dict[str, Any] | None = None,
        SplitterConfiguration: dict[str, Any] | None = None,
        SensitiveDataConfiguration: dict[str, Any] | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
