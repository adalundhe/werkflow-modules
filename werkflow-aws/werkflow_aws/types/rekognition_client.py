from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class RekognitionClient(ABC):

    @abstractmethod
    def associate_faces(
        self,
        *,
        CollectionId: str,
        UserId: str,
        FaceIds: list[str],
        UserMatchThreshold: float | int | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def compare_faces(
        self,
        *,
        SourceImage: dict[str, Any],
        TargetImage: dict[str, Any],
        SimilarityThreshold: float | int | None = None,
        QualityFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_project_version(
        self,
        *,
        SourceProjectArn: str,
        SourceProjectVersionArn: str,
        DestinationProjectArn: str,
        VersionName: str,
        OutputConfig: dict[str, Any],
        Tags: dict[str, str] | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_collection(
        self,
        *,
        CollectionId: str,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dataset(
        self,
        *,
        DatasetType: str,
        ProjectArn: str,
        DatasetSource: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_face_liveness_session(
        self,
        *,
        KmsKeyId: str | None = None,
        Settings: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        ProjectName: str,
        Feature: str | None = None,
        AutoUpdate: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project_version(
        self,
        *,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: dict[str, Any],
        TrainingData: dict[str, Any] | None = None,
        TestingData: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        KmsKeyId: str | None = None,
        VersionDescription: str | None = None,
        FeatureConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stream_processor(
        self,
        *,
        Input: dict[str, Any],
        Output: dict[str, Any],
        Name: str,
        Settings: dict[str, Any],
        RoleArn: str,
        Tags: dict[str, str] | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        KmsKeyId: str | None = None,
        RegionsOfInterest: list[dict[str, Any]] | None = None,
        DataSharingPreference: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        CollectionId: str,
        UserId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_collection(
        self,
        *,
        CollectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dataset(
        self,
        *,
        DatasetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_faces(
        self,
        *,
        CollectionId: str,
        FaceIds: list[str],
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
    def delete_project_policy(
        self,
        *,
        ProjectArn: str,
        PolicyName: str,
        PolicyRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project_version(
        self,
        *,
        ProjectVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stream_processor(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        CollectionId: str,
        UserId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_collection(
        self,
        *,
        CollectionId: str,
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
    def describe_project_versions(
        self,
        *,
        ProjectArn: str,
        VersionNames: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_projects(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ProjectNames: list[str] | None = None,
        Features: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream_processor(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_custom_labels(
        self,
        *,
        ProjectVersionArn: str,
        Image: dict[str, Any],
        MaxResults: int | None = None,
        MinConfidence: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_faces(
        self,
        *,
        Image: dict[str, Any],
        Attributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_labels(
        self,
        *,
        Image: dict[str, Any],
        MaxLabels: int | None = None,
        MinConfidence: float | int | None = None,
        Features: list[str] | None = None,
        Settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_moderation_labels(
        self,
        *,
        Image: dict[str, Any],
        MinConfidence: float | int | None = None,
        HumanLoopConfig: dict[str, Any] | None = None,
        ProjectVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_protective_equipment(
        self,
        *,
        Image: dict[str, Any],
        SummarizationAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_text(
        self,
        *,
        Image: dict[str, Any],
        Filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_faces(
        self,
        *,
        CollectionId: str,
        UserId: str,
        FaceIds: list[str],
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def distribute_dataset_entries(
        self,
        *,
        Datasets: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_celebrity_info(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_celebrity_recognition(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_content_moderation(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        AggregateBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_face_detection(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_face_liveness_session_results(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_face_search(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_label_detection(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        AggregateBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_media_analysis_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_person_tracking(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment_detection(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_text_detection(
        self,
        *,
        JobId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def index_faces(
        self,
        *,
        CollectionId: str,
        Image: dict[str, Any],
        ExternalImageId: str | None = None,
        DetectionAttributes: list[str] | None = None,
        MaxFaces: int | None = None,
        QualityFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_collections(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dataset_entries(
        self,
        *,
        DatasetArn: str,
        ContainsLabels: list[str] | None = None,
        Labeled: bool | None = None,
        SourceRefContains: str | None = None,
        HasErrors: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dataset_labels(
        self,
        *,
        DatasetArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_faces(
        self,
        *,
        CollectionId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        UserId: str | None = None,
        FaceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_media_analysis_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_project_policies(
        self,
        *,
        ProjectArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stream_processors(
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
    def list_users(
        self,
        *,
        CollectionId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_project_policy(
        self,
        *,
        ProjectArn: str,
        PolicyName: str,
        PolicyDocument: str,
        PolicyRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def recognize_celebrities(
        self,
        *,
        Image: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_faces(
        self,
        *,
        CollectionId: str,
        FaceId: str,
        MaxFaces: int | None = None,
        FaceMatchThreshold: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_faces_by_image(
        self,
        *,
        CollectionId: str,
        Image: dict[str, Any],
        MaxFaces: int | None = None,
        FaceMatchThreshold: float | int | None = None,
        QualityFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_users(
        self,
        *,
        CollectionId: str,
        UserId: str | None = None,
        FaceId: str | None = None,
        UserMatchThreshold: float | int | None = None,
        MaxUsers: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_users_by_image(
        self,
        *,
        CollectionId: str,
        Image: dict[str, Any],
        UserMatchThreshold: float | int | None = None,
        MaxUsers: int | None = None,
        QualityFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_celebrity_recognition(
        self,
        *,
        Video: dict[str, Any],
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_content_moderation(
        self,
        *,
        Video: dict[str, Any],
        MinConfidence: float | int | None = None,
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_face_detection(
        self,
        *,
        Video: dict[str, Any],
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        FaceAttributes: str | None = None,
        JobTag: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_face_search(
        self,
        *,
        Video: dict[str, Any],
        CollectionId: str,
        ClientRequestToken: str | None = None,
        FaceMatchThreshold: float | int | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_label_detection(
        self,
        *,
        Video: dict[str, Any],
        ClientRequestToken: str | None = None,
        MinConfidence: float | int | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
        Features: list[str] | None = None,
        Settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_media_analysis_job(
        self,
        *,
        OperationsConfig: dict[str, Any],
        Input: dict[str, Any],
        OutputConfig: dict[str, Any],
        ClientRequestToken: str | None = None,
        JobName: str | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_person_tracking(
        self,
        *,
        Video: dict[str, Any],
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_project_version(
        self,
        *,
        ProjectVersionArn: str,
        MinInferenceUnits: int,
        MaxInferenceUnits: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_segment_detection(
        self,
        *,
        Video: dict[str, Any],
        SegmentTypes: list[str],
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
        Filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_stream_processor(
        self,
        *,
        Name: str,
        StartSelector: dict[str, Any] | None = None,
        StopSelector: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_text_detection(
        self,
        *,
        Video: dict[str, Any],
        ClientRequestToken: str | None = None,
        NotificationChannel: dict[str, Any] | None = None,
        JobTag: str | None = None,
        Filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_project_version(
        self,
        *,
        ProjectVersionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_stream_processor(
        self,
        *,
        Name: str,
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
    def update_dataset_entries(
        self,
        *,
        DatasetArn: str,
        Changes: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream_processor(
        self,
        *,
        Name: str,
        SettingsForUpdate: dict[str, Any] | None = None,
        RegionsOfInterestForUpdate: list[dict[str, Any]] | None = None,
        DataSharingPreferenceForUpdate: dict[str, Any] | None = None,
        ParametersToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
