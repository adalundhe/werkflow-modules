from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ComputeOptimizerClient(ABC):

    @abstractmethod
    def delete_recommendation_preferences(
        self,
        *,
        resourceType: str,
        recommendationPreferenceNames: list[str],
        scope: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recommendation_export_jobs(
        self,
        *,
        jobIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_auto_scaling_group_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_ebs_volume_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_ec2_instance_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_ecs_service_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_idle_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_lambda_function_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_license_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_rds_database_recommendations(
        self,
        *,
        s3DestinationConfig: dict[str, Any],
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        fieldsToExport: list[str] | None = None,
        fileFormat: str | None = None,
        includeMemberAccounts: bool | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_auto_scaling_group_recommendations(
        self,
        *,
        accountIds: list[str] | None = None,
        autoScalingGroupArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ebs_volume_recommendations(
        self,
        *,
        volumeArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ec2_instance_recommendations(
        self,
        *,
        instanceArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ec2_recommendation_projected_metrics(
        self,
        *,
        instanceArn: str,
        stat: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ecs_service_recommendation_projected_metrics(
        self,
        *,
        serviceArn: str,
        stat: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ecs_service_recommendations(
        self,
        *,
        serviceArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_effective_recommendation_preferences(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_enrollment_status(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_enrollment_statuses_for_organization(
        self,
        *,
        filters: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_idle_recommendations(
        self,
        *,
        resourceArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
        orderBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lambda_function_recommendations(
        self,
        *,
        functionArns: list[str] | None = None,
        accountIds: list[str] | None = None,
        filters: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_license_recommendations(
        self,
        *,
        resourceArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rds_database_recommendation_projected_metrics(
        self,
        *,
        resourceArn: str,
        stat: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rds_database_recommendations(
        self,
        *,
        resourceArns: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
        accountIds: list[str] | None = None,
        recommendationPreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recommendation_preferences(
        self,
        *,
        resourceType: str,
        scope: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recommendation_summaries(
        self,
        *,
        accountIds: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_recommendation_preferences(
        self,
        *,
        resourceType: str,
        scope: dict[str, Any] | None = None,
        enhancedInfrastructureMetrics: str | None = None,
        inferredWorkloadTypes: str | None = None,
        externalMetricsPreference: dict[str, Any] | None = None,
        lookBackPeriod: str | None = None,
        utilizationPreferences: list[dict[str, Any]] | None = None,
        preferredResources: list[dict[str, Any]] | None = None,
        savingsEstimationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_enrollment_status(
        self,
        *,
        status: str,
        includeMemberAccounts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
