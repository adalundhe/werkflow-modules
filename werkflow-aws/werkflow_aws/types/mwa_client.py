from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class MWAAClient(ABC):

    @abstractmethod
    def create_cli_token(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment(
        self,
        *,
        Name: str,
        ExecutionRoleArn: str,
        SourceBucketArn: str,
        DagS3Path: str,
        NetworkConfiguration: dict[str, Any],
        PluginsS3Path: str | None = None,
        PluginsS3ObjectVersion: str | None = None,
        RequirementsS3Path: str | None = None,
        RequirementsS3ObjectVersion: str | None = None,
        StartupScriptS3Path: str | None = None,
        StartupScriptS3ObjectVersion: str | None = None,
        AirflowConfigurationOptions: dict[str, str] | None = None,
        EnvironmentClass: str | None = None,
        MaxWorkers: int | None = None,
        KmsKey: str | None = None,
        AirflowVersion: str | None = None,
        LoggingConfiguration: dict[str, Any] | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        Tags: dict[str, str] | None = None,
        WebserverAccessMode: str | None = None,
        MinWorkers: int | None = None,
        Schedulers: int | None = None,
        EndpointManagement: str | None = None,
        MinWebservers: int | None = None,
        MaxWebservers: int | None = None,
        IdentityCenterConfiguration: dict[str, Any] | None = None,
        Teams: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_web_login_token(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_rest_api(
        self,
        *,
        Name: str,
        Path: str,
        Method: str,
        QueryParameters: dict[str, Any] | None = None,
        Body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environments(
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
    def publish_metrics(
        self,
        *,
        EnvironmentName: str,
        MetricData: list[dict[str, Any]],
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
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment(
        self,
        *,
        Name: str,
        ExecutionRoleArn: str | None = None,
        AirflowConfigurationOptions: dict[str, str] | None = None,
        AirflowVersion: str | None = None,
        DagS3Path: str | None = None,
        EnvironmentClass: str | None = None,
        LoggingConfiguration: dict[str, Any] | None = None,
        MaxWorkers: int | None = None,
        MinWorkers: int | None = None,
        MaxWebservers: int | None = None,
        MinWebservers: int | None = None,
        WorkerReplacementStrategy: str | None = None,
        NetworkConfiguration: dict[str, Any] | None = None,
        PluginsS3Path: str | None = None,
        PluginsS3ObjectVersion: str | None = None,
        RequirementsS3Path: str | None = None,
        RequirementsS3ObjectVersion: str | None = None,
        Schedulers: int | None = None,
        SourceBucketArn: str | None = None,
        StartupScriptS3Path: str | None = None,
        StartupScriptS3ObjectVersion: str | None = None,
        WebserverAccessMode: str | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        IdentityCenterConfiguration: dict[str, Any] | None = None,
        Teams: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
