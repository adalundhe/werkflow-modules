from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CodeBuildClient(ABC):

    @abstractmethod
    def batch_delete_builds(
        self,
        *,
        ids: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_build_batches(
        self,
        *,
        ids: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_builds(
        self,
        *,
        ids: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_command_executions(
        self,
        *,
        sandboxId: str,
        commandExecutionIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_fleets(
        self,
        *,
        names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_projects(
        self,
        *,
        names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_report_groups(
        self,
        *,
        reportGroupArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_reports(
        self,
        *,
        reportArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_sandboxes(
        self,
        *,
        ids: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fleet(
        self,
        *,
        name: str,
        baseCapacity: int,
        environmentType: str,
        computeType: str,
        computeConfiguration: dict[str, Any] | None = None,
        scalingConfiguration: dict[str, Any] | None = None,
        overflowBehavior: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
        proxyConfiguration: dict[str, Any] | None = None,
        imageId: str | None = None,
        fleetServiceRole: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        name: str,
        source: dict[str, Any],
        artifacts: dict[str, Any],
        environment: dict[str, Any],
        serviceRole: str,
        description: str | None = None,
        secondarySources: list[dict[str, Any]] | None = None,
        sourceVersion: str | None = None,
        secondarySourceVersions: list[dict[str, Any]] | None = None,
        secondaryArtifacts: list[dict[str, Any]] | None = None,
        cache: dict[str, Any] | None = None,
        timeoutInMinutes: int | None = None,
        queuedTimeoutInMinutes: int | None = None,
        encryptionKey: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        vpcConfig: dict[str, Any] | None = None,
        badgeEnabled: bool | None = None,
        logsConfig: dict[str, Any] | None = None,
        fileSystemLocations: list[dict[str, Any]] | None = None,
        buildBatchConfig: dict[str, Any] | None = None,
        concurrentBuildLimit: int | None = None,
        autoRetryLimit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_report_group(
        self,
        *,
        name: str,
        type: str,
        exportConfig: dict[str, Any],
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_webhook(
        self,
        *,
        projectName: str,
        branchFilter: str | None = None,
        filterGroups: list[list[dict[str, Any]]] | None = None,
        buildType: str | None = None,
        manualCreation: bool | None = None,
        scopeConfiguration: dict[str, Any] | None = None,
        pullRequestBuildPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_build_batch(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleet(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_report(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_report_group(
        self,
        *,
        arn: str,
        deleteReports: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_source_credentials(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_webhook(
        self,
        *,
        projectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_code_coverages(
        self,
        *,
        reportArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        sortBy: str | None = None,
        minLineCoveragePercentage: float | int | None = None,
        maxLineCoveragePercentage: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_cases(
        self,
        *,
        reportArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_report_group_trend(
        self,
        *,
        reportGroupArn: str,
        trendField: str,
        numOfReports: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_source_credentials(
        self,
        *,
        token: str,
        serverType: str,
        authType: str,
        username: str | None = None,
        shouldOverwrite: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invalidate_project_cache(
        self,
        *,
        projectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_build_batches(
        self,
        *,
        filter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_build_batches_for_project(
        self,
        *,
        projectName: str | None = None,
        filter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_builds(
        self,
        *,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_builds_for_project(
        self,
        *,
        projectName: str,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_command_executions_for_sandbox(
        self,
        *,
        sandboxId: str,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_curated_environment_images(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_fleets(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        sortBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_report_groups(
        self,
        *,
        sortOrder: str | None = None,
        sortBy: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_reports(
        self,
        *,
        sortOrder: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_reports_for_report_group(
        self,
        *,
        reportGroupArn: str,
        nextToken: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sandboxes(
        self,
        *,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sandboxes_for_project(
        self,
        *,
        projectName: str,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_shared_projects(
        self,
        *,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_shared_report_groups(
        self,
        *,
        sortOrder: str | None = None,
        sortBy: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_source_credentials(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        policy: str,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retry_build(
        self,
        *,
        id: str | None = None,
        idempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retry_build_batch(
        self,
        *,
        id: str | None = None,
        idempotencyToken: str | None = None,
        retryType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_build(
        self,
        *,
        projectName: str,
        secondarySourcesOverride: list[dict[str, Any]] | None = None,
        secondarySourcesVersionOverride: list[dict[str, Any]] | None = None,
        sourceVersion: str | None = None,
        artifactsOverride: dict[str, Any] | None = None,
        secondaryArtifactsOverride: list[dict[str, Any]] | None = None,
        environmentVariablesOverride: list[dict[str, Any]] | None = None,
        sourceTypeOverride: str | None = None,
        sourceLocationOverride: str | None = None,
        sourceAuthOverride: dict[str, Any] | None = None,
        gitCloneDepthOverride: int | None = None,
        gitSubmodulesConfigOverride: dict[str, Any] | None = None,
        buildspecOverride: str | None = None,
        insecureSslOverride: bool | None = None,
        reportBuildStatusOverride: bool | None = None,
        buildStatusConfigOverride: dict[str, Any] | None = None,
        environmentTypeOverride: str | None = None,
        imageOverride: str | None = None,
        computeTypeOverride: str | None = None,
        certificateOverride: str | None = None,
        cacheOverride: dict[str, Any] | None = None,
        serviceRoleOverride: str | None = None,
        privilegedModeOverride: bool | None = None,
        timeoutInMinutesOverride: int | None = None,
        queuedTimeoutInMinutesOverride: int | None = None,
        encryptionKeyOverride: str | None = None,
        idempotencyToken: str | None = None,
        logsConfigOverride: dict[str, Any] | None = None,
        registryCredentialOverride: dict[str, Any] | None = None,
        imagePullCredentialsTypeOverride: str | None = None,
        debugSessionEnabled: bool | None = None,
        fleetOverride: dict[str, Any] | None = None,
        autoRetryLimitOverride: int | None = None,
        hostKernelOverride: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_build_batch(
        self,
        *,
        projectName: str,
        secondarySourcesOverride: list[dict[str, Any]] | None = None,
        secondarySourcesVersionOverride: list[dict[str, Any]] | None = None,
        sourceVersion: str | None = None,
        artifactsOverride: dict[str, Any] | None = None,
        secondaryArtifactsOverride: list[dict[str, Any]] | None = None,
        environmentVariablesOverride: list[dict[str, Any]] | None = None,
        sourceTypeOverride: str | None = None,
        sourceLocationOverride: str | None = None,
        sourceAuthOverride: dict[str, Any] | None = None,
        gitCloneDepthOverride: int | None = None,
        gitSubmodulesConfigOverride: dict[str, Any] | None = None,
        buildspecOverride: str | None = None,
        insecureSslOverride: bool | None = None,
        reportBuildBatchStatusOverride: bool | None = None,
        environmentTypeOverride: str | None = None,
        imageOverride: str | None = None,
        computeTypeOverride: str | None = None,
        certificateOverride: str | None = None,
        cacheOverride: dict[str, Any] | None = None,
        serviceRoleOverride: str | None = None,
        privilegedModeOverride: bool | None = None,
        buildTimeoutInMinutesOverride: int | None = None,
        queuedTimeoutInMinutesOverride: int | None = None,
        encryptionKeyOverride: str | None = None,
        idempotencyToken: str | None = None,
        logsConfigOverride: dict[str, Any] | None = None,
        registryCredentialOverride: dict[str, Any] | None = None,
        imagePullCredentialsTypeOverride: str | None = None,
        buildBatchConfigOverride: dict[str, Any] | None = None,
        debugSessionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_command_execution(
        self,
        *,
        sandboxId: str,
        command: str,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_sandbox(
        self,
        *,
        projectName: str | None = None,
        idempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_sandbox_connection(
        self,
        *,
        sandboxId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_build(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_build_batch(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_sandbox(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_fleet(
        self,
        *,
        arn: str,
        baseCapacity: int | None = None,
        environmentType: str | None = None,
        computeType: str | None = None,
        computeConfiguration: dict[str, Any] | None = None,
        scalingConfiguration: dict[str, Any] | None = None,
        overflowBehavior: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
        proxyConfiguration: dict[str, Any] | None = None,
        imageId: str | None = None,
        fleetServiceRole: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        name: str,
        description: str | None = None,
        source: dict[str, Any] | None = None,
        secondarySources: list[dict[str, Any]] | None = None,
        sourceVersion: str | None = None,
        secondarySourceVersions: list[dict[str, Any]] | None = None,
        artifacts: dict[str, Any] | None = None,
        secondaryArtifacts: list[dict[str, Any]] | None = None,
        cache: dict[str, Any] | None = None,
        environment: dict[str, Any] | None = None,
        serviceRole: str | None = None,
        timeoutInMinutes: int | None = None,
        queuedTimeoutInMinutes: int | None = None,
        encryptionKey: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        vpcConfig: dict[str, Any] | None = None,
        badgeEnabled: bool | None = None,
        logsConfig: dict[str, Any] | None = None,
        fileSystemLocations: list[dict[str, Any]] | None = None,
        buildBatchConfig: dict[str, Any] | None = None,
        concurrentBuildLimit: int | None = None,
        autoRetryLimit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project_visibility(
        self,
        *,
        projectArn: str,
        projectVisibility: str,
        resourceAccessRole: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_report_group(
        self,
        *,
        arn: str,
        exportConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_webhook(
        self,
        *,
        projectName: str,
        branchFilter: str | None = None,
        rotateSecret: bool | None = None,
        filterGroups: list[list[dict[str, Any]]] | None = None,
        buildType: str | None = None,
        pullRequestBuildPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
