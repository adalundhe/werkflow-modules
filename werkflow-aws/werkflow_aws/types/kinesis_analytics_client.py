from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class KinesisAnalyticsClient(ABC):

    @abstractmethod
    def add_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOption: dict[str, Any],
        CurrentApplicationVersionId: int | None = None,
        ConditionalToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_application_input(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Input: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_application_input_processing_configuration(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_application_output(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Output: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_application_reference_data_source(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfiguration: dict[str, Any],
        CurrentApplicationVersionId: int | None = None,
        ConditionalToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application(
        self,
        *,
        ApplicationName: str,
        RuntimeEnvironment: str,
        ServiceExecutionRole: str,
        ApplicationDescription: str | None = None,
        ApplicationConfiguration: dict[str, Any] | None = None,
        CloudWatchLoggingOptions: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ApplicationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application_presigned_url(
        self,
        *,
        ApplicationName: str,
        UrlType: str,
        SessionExpirationDurationInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application_snapshot(
        self,
        *,
        ApplicationName: str,
        SnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        ApplicationName: str,
        SnapshotName: str,
        SnapshotDescription: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application(
        self,
        *,
        ApplicationName: str,
        CreateTimestamp: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOptionId: str,
        CurrentApplicationVersionId: int | None = None,
        ConditionalToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_input_processing_configuration(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_output(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        OutputId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_reference_data_source(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_snapshot(
        self,
        *,
        ApplicationName: str,
        SnapshotName: str,
        SnapshotCreationTimestamp: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfigurationId: str,
        CurrentApplicationVersionId: int | None = None,
        ConditionalToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot(
        self,
        *,
        SnapshotName: str,
        SnapshotCreationTimestamp: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application(
        self,
        *,
        ApplicationName: str,
        IncludeAdditionalDetails: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_operation(
        self,
        *,
        ApplicationName: str,
        OperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_snapshot(
        self,
        *,
        ApplicationName: str,
        SnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_version(
        self,
        *,
        ApplicationName: str,
        ApplicationVersionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot(
        self,
        *,
        SnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_operation(
        self,
        *,
        SnapshotName: str,
        SnapshotOperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def discover_input_schema(
        self,
        *,
        ServiceExecutionRole: str,
        ResourceARN: str | None = None,
        InputStartingPositionConfiguration: dict[str, Any] | None = None,
        S3Configuration: dict[str, Any] | None = None,
        InputProcessingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_snapshot(
        self,
        *,
        SnapshotName: str,
        ExportDestinationConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_snapshot(
        self,
        *,
        SnapshotName: str,
        ImportSourceConfiguration: dict[str, Any],
        DestinationEncryptionConfiguration: dict[str, Any] | None = None,
        SnapshotDescription: str | None = None,
        SnapshotFormat: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_application_operations(
        self,
        *,
        ApplicationName: str,
        Limit: int | None = None,
        NextToken: str | None = None,
        Operation: str | None = None,
        OperationStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_application_snapshots(
        self,
        *,
        ApplicationName: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_application_versions(
        self,
        *,
        ApplicationName: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_applications(
        self,
        *,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_snapshot_operations(
        self,
        *,
        SnapshotName: str,
        SnapshotOperation: str | None = None,
        SnapshotOperationStatus: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_snapshots(
        self,
        *,
        SourceApplicationName: str | None = None,
        SnapshotInitiator: str | None = None,
        SnapshotInitiatorOperation: str | None = None,
        SnapshotStatus: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
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
    def rollback_application(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_application(
        self,
        *,
        ApplicationName: str,
        RunConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_application(
        self,
        *,
        ApplicationName: str,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
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
    def update_application(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int | None = None,
        ApplicationConfigurationUpdate: dict[str, Any] | None = None,
        ServiceExecutionRoleUpdate: str | None = None,
        RunConfigurationUpdate: dict[str, Any] | None = None,
        CloudWatchLoggingOptionUpdates: list[dict[str, Any]] | None = None,
        ConditionalToken: str | None = None,
        RuntimeEnvironmentUpdate: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application_maintenance_configuration(
        self,
        *,
        ApplicationName: str,
        ApplicationMaintenanceConfigurationUpdate: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
