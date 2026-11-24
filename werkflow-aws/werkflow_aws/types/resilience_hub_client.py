from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ResilienceHubClient(ABC):

    @abstractmethod
    def accept_resource_grouping_recommendations(
        self,
        *,
        appArn: str,
        entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_draft_app_version_resource_mappings(
        self,
        *,
        appArn: str,
        resourceMappings: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_recommendation_status(
        self,
        *,
        appArn: str,
        requestEntries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app(
        self,
        *,
        name: str,
        assessmentSchedule: str | None = None,
        awsApplicationArn: str | None = None,
        clientToken: str | None = None,
        description: str | None = None,
        eventSubscriptions: list[dict[str, Any]] | None = None,
        permissionModel: dict[str, Any] | None = None,
        policyArn: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_version_app_component(
        self,
        *,
        appArn: str,
        name: str,
        type: str,
        additionalInfo: dict[str, list[str]] | None = None,
        clientToken: str | None = None,
        id: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_version_resource(
        self,
        *,
        appArn: str,
        appComponents: list[str],
        logicalResourceId: dict[str, Any],
        physicalResourceId: str,
        resourceType: str,
        additionalInfo: dict[str, list[str]] | None = None,
        awsAccountId: str | None = None,
        awsRegion: str | None = None,
        clientToken: str | None = None,
        resourceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_recommendation_template(
        self,
        *,
        assessmentArn: str,
        name: str,
        bucketName: str | None = None,
        clientToken: str | None = None,
        format: str | None = None,
        recommendationIds: list[str] | None = None,
        recommendationTypes: list[str] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resiliency_policy(
        self,
        *,
        policy: dict[str, dict[str, Any]],
        policyName: str,
        tier: str,
        clientToken: str | None = None,
        dataLocationConstraint: str | None = None,
        policyDescription: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app(
        self,
        *,
        appArn: str,
        clientToken: str | None = None,
        forceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_assessment(
        self,
        *,
        assessmentArn: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_input_source(
        self,
        *,
        appArn: str,
        clientToken: str | None = None,
        eksSourceClusterNamespace: dict[str, Any] | None = None,
        sourceArn: str | None = None,
        terraformSource: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_version_app_component(
        self,
        *,
        appArn: str,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_version_resource(
        self,
        *,
        appArn: str,
        awsAccountId: str | None = None,
        awsRegion: str | None = None,
        clientToken: str | None = None,
        logicalResourceId: dict[str, Any] | None = None,
        physicalResourceId: str | None = None,
        resourceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_recommendation_template(
        self,
        *,
        recommendationTemplateArn: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resiliency_policy(
        self,
        *,
        policyArn: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app(
        self,
        *,
        appArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_assessment(
        self,
        *,
        assessmentArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_version(
        self,
        *,
        appArn: str,
        appVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_version_app_component(
        self,
        *,
        appArn: str,
        appVersion: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_version_resource(
        self,
        *,
        appArn: str,
        appVersion: str,
        awsAccountId: str | None = None,
        awsRegion: str | None = None,
        logicalResourceId: dict[str, Any] | None = None,
        physicalResourceId: str | None = None,
        resourceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_version_resources_resolution_status(
        self,
        *,
        appArn: str,
        appVersion: str,
        resolutionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_version_template(
        self,
        *,
        appArn: str,
        appVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_draft_app_version_resources_import_status(
        self,
        *,
        appArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metrics_export(
        self,
        *,
        metricsExportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resiliency_policy(
        self,
        *,
        policyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_grouping_recommendation_task(
        self,
        *,
        appArn: str,
        groupingId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_resources_to_draft_app_version(
        self,
        *,
        appArn: str,
        eksSources: list[dict[str, Any]] | None = None,
        importStrategy: str | None = None,
        sourceArns: list[str] | None = None,
        terraformSources: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_alarm_recommendations(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_assessment_compliance_drifts(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_assessment_resource_drifts(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_assessments(
        self,
        *,
        appArn: str | None = None,
        assessmentName: str | None = None,
        assessmentStatus: list[str] | None = None,
        complianceStatus: str | None = None,
        invoker: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        reverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_component_compliances(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_component_recommendations(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_input_sources(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_version_app_components(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_version_resource_mappings(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_version_resources(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        resolutionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_versions(
        self,
        *,
        appArn: str,
        endTime: datetime.datetime | str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        startTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apps(
        self,
        *,
        appArn: str | None = None,
        awsApplicationArn: str | None = None,
        fromLastAssessmentTime: datetime.datetime | str | None = None,
        maxResults: int | None = None,
        name: str | None = None,
        nextToken: str | None = None,
        reverseOrder: bool | None = None,
        toLastAssessmentTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metrics(
        self,
        *,
        conditions: list[dict[str, Any]] | None = None,
        dataSource: str | None = None,
        fields: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sorts: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommendation_templates(
        self,
        *,
        assessmentArn: str | None = None,
        maxResults: int | None = None,
        name: str | None = None,
        nextToken: str | None = None,
        recommendationTemplateArn: str | None = None,
        reverseOrder: bool | None = None,
        status: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resiliency_policies(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        policyName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_grouping_recommendations(
        self,
        *,
        appArn: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sop_recommendations(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_suggested_resiliency_policies(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_recommendations(
        self,
        *,
        assessmentArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_unsupported_app_version_resources(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        resolutionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_app_version(
        self,
        *,
        appArn: str,
        versionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_draft_app_version_template(
        self,
        *,
        appArn: str,
        appTemplateBody: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_resource_grouping_recommendations(
        self,
        *,
        appArn: str,
        entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_draft_app_version_resource_mappings(
        self,
        *,
        appArn: str,
        appRegistryAppNames: list[str] | None = None,
        eksSourceNames: list[str] | None = None,
        logicalStackNames: list[str] | None = None,
        resourceGroupNames: list[str] | None = None,
        resourceNames: list[str] | None = None,
        terraformSourceNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resolve_app_version_resources(
        self,
        *,
        appArn: str,
        appVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_app_assessment(
        self,
        *,
        appArn: str,
        appVersion: str,
        assessmentName: str,
        clientToken: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metrics_export(
        self,
        *,
        bucketName: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_resource_grouping_recommendation_task(
        self,
        *,
        appArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app(
        self,
        *,
        appArn: str,
        assessmentSchedule: str | None = None,
        clearResiliencyPolicyArn: bool | None = None,
        description: str | None = None,
        eventSubscriptions: list[dict[str, Any]] | None = None,
        permissionModel: dict[str, Any] | None = None,
        policyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_version(
        self,
        *,
        appArn: str,
        additionalInfo: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_version_app_component(
        self,
        *,
        appArn: str,
        id: str,
        additionalInfo: dict[str, list[str]] | None = None,
        name: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_version_resource(
        self,
        *,
        appArn: str,
        additionalInfo: dict[str, list[str]] | None = None,
        appComponents: list[str] | None = None,
        awsAccountId: str | None = None,
        awsRegion: str | None = None,
        excluded: bool | None = None,
        logicalResourceId: dict[str, Any] | None = None,
        physicalResourceId: str | None = None,
        resourceName: str | None = None,
        resourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resiliency_policy(
        self,
        *,
        policyArn: str,
        dataLocationConstraint: str | None = None,
        policy: dict[str, dict[str, Any]] | None = None,
        policyDescription: str | None = None,
        policyName: str | None = None,
        tier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
