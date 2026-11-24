from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class ComprehendClient(ABC):

    @abstractmethod
    def batch_detect_dominant_language(
        self,
        *,
        TextList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_detect_entities(
        self,
        *,
        TextList: list[str],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_detect_key_phrases(
        self,
        *,
        TextList: list[str],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_detect_sentiment(
        self,
        *,
        TextList: list[str],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_detect_syntax(
        self,
        *,
        TextList: list[str],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_detect_targeted_sentiment(
        self,
        *,
        TextList: list[str],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def classify_document(
        self,
        *,
        EndpointArn: str,
        Text: str | None = None,
        Bytes: bytes | BinaryIO | str | None = None,
        DocumentReaderConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def contains_pii_entities(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset(
        self,
        *,
        FlywheelArn: str,
        DatasetName: str,
        InputDataConfig: dict[str, Any],
        DatasetType: str | None = None,
        Description: str | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_document_classifier(
        self,
        *,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: dict[str, Any],
        LanguageCode: str,
        VersionName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        OutputDataConfig: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Mode: str | None = None,
        ModelKmsKeyId: str | None = None,
        ModelPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint(
        self,
        *,
        EndpointName: str,
        DesiredInferenceUnits: int,
        ModelArn: str | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataAccessRoleArn: str | None = None,
        FlywheelArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_entity_recognizer(
        self,
        *,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: dict[str, Any],
        LanguageCode: str,
        VersionName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        ModelKmsKeyId: str | None = None,
        ModelPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_flywheel(
        self,
        *,
        FlywheelName: str,
        DataAccessRoleArn: str,
        DataLakeS3Uri: str,
        ActiveModelArn: str | None = None,
        TaskConfig: dict[str, Any] | None = None,
        ModelType: str | None = None,
        DataSecurityConfig: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_document_classifier(
        self,
        *,
        DocumentClassifierArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_entity_recognizer(
        self,
        *,
        EntityRecognizerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_flywheel(
        self,
        *,
        FlywheelArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
        PolicyRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset(
        self,
        *,
        DatasetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_document_classification_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_document_classifier(
        self,
        *,
        DocumentClassifierArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dominant_language_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_entities_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_entity_recognizer(
        self,
        *,
        EntityRecognizerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_events_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flywheel(
        self,
        *,
        FlywheelArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flywheel_iteration(
        self,
        *,
        FlywheelArn: str,
        FlywheelIterationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key_phrases_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pii_entities_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_sentiment_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_targeted_sentiment_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topics_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_dominant_language(
        self,
        *,
        Text: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_entities(
        self,
        *,
        Text: str | None = None,
        LanguageCode: str | None = None,
        EndpointArn: str | None = None,
        Bytes: bytes | BinaryIO | str | None = None,
        DocumentReaderConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_key_phrases(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_pii_entities(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_sentiment(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_syntax(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_targeted_sentiment(
        self,
        *,
        Text: str,
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_toxic_content(
        self,
        *,
        TextSegments: list[dict[str, Any]],
        LanguageCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_model(
        self,
        *,
        SourceModelArn: str,
        ModelName: str | None = None,
        VersionName: str | None = None,
        ModelKmsKeyId: str | None = None,
        DataAccessRoleArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_datasets(
        self,
        *,
        FlywheelArn: str | None = None,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_document_classification_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_document_classifier_summaries(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_document_classifiers(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dominant_language_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_endpoints(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entities_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entity_recognizer_summaries(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entity_recognizers(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_events_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flywheel_iteration_history(
        self,
        *,
        FlywheelArn: str,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flywheels(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_key_phrases_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pii_entities_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sentiment_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
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
    def list_targeted_sentiment_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topics_detection_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        ResourcePolicy: str,
        PolicyRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_document_classification_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str | None = None,
        DocumentClassifierArn: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FlywheelArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dominant_language_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_entities_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str | None = None,
        EntityRecognizerArn: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FlywheelArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_events_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        TargetEventTypes: list[str],
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_flywheel_iteration(
        self,
        *,
        FlywheelArn: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_key_phrases_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_pii_entities_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        Mode: str,
        DataAccessRoleArn: str,
        LanguageCode: str,
        RedactionConfig: dict[str, Any] | None = None,
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_sentiment_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_targeted_sentiment_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_topics_detection_job(
        self,
        *,
        InputDataConfig: dict[str, Any],
        OutputDataConfig: dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str | None = None,
        NumberOfTopics: int | None = None,
        ClientRequestToken: str | None = None,
        VolumeKmsKeyId: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_dominant_language_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_entities_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_events_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_key_phrases_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_pii_entities_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_sentiment_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_targeted_sentiment_detection_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_training_document_classifier(
        self,
        *,
        DocumentClassifierArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_training_entity_recognizer(
        self,
        *,
        EntityRecognizerArn: str,
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
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoint(
        self,
        *,
        EndpointArn: str,
        DesiredModelArn: str | None = None,
        DesiredInferenceUnits: int | None = None,
        DesiredDataAccessRoleArn: str | None = None,
        FlywheelArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_flywheel(
        self,
        *,
        FlywheelArn: str,
        ActiveModelArn: str | None = None,
        DataAccessRoleArn: str | None = None,
        DataSecurityConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
