from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class AmplifyClient(ABC):

    @abstractmethod
    def create_app(
        self,
        *,
        name: str,
        description: str | None = None,
        repository: str | None = None,
        platform: str | None = None,
        computeRoleArn: str | None = None,
        iamServiceRoleArn: str | None = None,
        oauthToken: str | None = None,
        accessToken: str | None = None,
        environmentVariables: dict[str, str] | None = None,
        enableBranchAutoBuild: bool | None = None,
        enableBranchAutoDeletion: bool | None = None,
        enableBasicAuth: bool | None = None,
        basicAuthCredentials: str | None = None,
        customRules: list[dict[str, Any]] | None = None,
        tags: dict[str, str] | None = None,
        buildSpec: str | None = None,
        customHeaders: str | None = None,
        enableAutoBranchCreation: bool | None = None,
        autoBranchCreationPatterns: list[str] | None = None,
        autoBranchCreationConfig: dict[str, Any] | None = None,
        jobConfig: dict[str, Any] | None = None,
        cacheConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backend_environment(
        self,
        *,
        appId: str,
        environmentName: str,
        stackName: str | None = None,
        deploymentArtifacts: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_branch(
        self,
        *,
        appId: str,
        branchName: str,
        description: str | None = None,
        stage: str | None = None,
        framework: str | None = None,
        enableNotification: bool | None = None,
        enableAutoBuild: bool | None = None,
        enableSkewProtection: bool | None = None,
        environmentVariables: dict[str, str] | None = None,
        basicAuthCredentials: str | None = None,
        enableBasicAuth: bool | None = None,
        enablePerformanceMode: bool | None = None,
        tags: dict[str, str] | None = None,
        buildSpec: str | None = None,
        ttl: str | None = None,
        displayName: str | None = None,
        enablePullRequestPreview: bool | None = None,
        pullRequestEnvironmentName: str | None = None,
        backendEnvironmentArn: str | None = None,
        backend: dict[str, Any] | None = None,
        computeRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_deployment(
        self,
        *,
        appId: str,
        branchName: str,
        fileMap: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
        subDomainSettings: list[dict[str, Any]],
        enableAutoSubDomain: bool | None = None,
        autoSubDomainCreationPatterns: list[str] | None = None,
        autoSubDomainIAMRole: str | None = None,
        certificateSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_webhook(
        self,
        *,
        appId: str,
        branchName: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app(
        self,
        *,
        appId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backend_environment(
        self,
        *,
        appId: str,
        environmentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_branch(
        self,
        *,
        appId: str,
        branchName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_webhook(
        self,
        *,
        webhookId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_access_logs(
        self,
        *,
        domainName: str,
        appId: str,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_app(
        self,
        *,
        appId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_artifact_url(
        self,
        *,
        artifactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_backend_environment(
        self,
        *,
        appId: str,
        environmentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_branch(
        self,
        *,
        appId: str,
        branchName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_webhook(
        self,
        *,
        webhookId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apps(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_artifacts(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backend_environments(
        self,
        *,
        appId: str,
        environmentName: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_branches(
        self,
        *,
        appId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_associations(
        self,
        *,
        appId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        appId: str,
        branchName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
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
    def list_webhooks(
        self,
        *,
        appId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_deployment(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str | None = None,
        sourceUrl: str | None = None,
        sourceUrlType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_job(
        self,
        *,
        appId: str,
        branchName: str,
        jobType: str,
        jobId: str | None = None,
        jobReason: str | None = None,
        commitId: str | None = None,
        commitMessage: str | None = None,
        commitTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_job(
        self,
        *,
        appId: str,
        branchName: str,
        jobId: str,
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
        appId: str,
        name: str | None = None,
        description: str | None = None,
        platform: str | None = None,
        computeRoleArn: str | None = None,
        iamServiceRoleArn: str | None = None,
        environmentVariables: dict[str, str] | None = None,
        enableBranchAutoBuild: bool | None = None,
        enableBranchAutoDeletion: bool | None = None,
        enableBasicAuth: bool | None = None,
        basicAuthCredentials: str | None = None,
        customRules: list[dict[str, Any]] | None = None,
        buildSpec: str | None = None,
        customHeaders: str | None = None,
        enableAutoBranchCreation: bool | None = None,
        autoBranchCreationPatterns: list[str] | None = None,
        autoBranchCreationConfig: dict[str, Any] | None = None,
        repository: str | None = None,
        oauthToken: str | None = None,
        accessToken: str | None = None,
        jobConfig: dict[str, Any] | None = None,
        cacheConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_branch(
        self,
        *,
        appId: str,
        branchName: str,
        description: str | None = None,
        framework: str | None = None,
        stage: str | None = None,
        enableNotification: bool | None = None,
        enableAutoBuild: bool | None = None,
        enableSkewProtection: bool | None = None,
        environmentVariables: dict[str, str] | None = None,
        basicAuthCredentials: str | None = None,
        enableBasicAuth: bool | None = None,
        enablePerformanceMode: bool | None = None,
        buildSpec: str | None = None,
        ttl: str | None = None,
        displayName: str | None = None,
        enablePullRequestPreview: bool | None = None,
        pullRequestEnvironmentName: str | None = None,
        backendEnvironmentArn: str | None = None,
        backend: dict[str, Any] | None = None,
        computeRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_association(
        self,
        *,
        appId: str,
        domainName: str,
        enableAutoSubDomain: bool | None = None,
        subDomainSettings: list[dict[str, Any]] | None = None,
        autoSubDomainCreationPatterns: list[str] | None = None,
        autoSubDomainIAMRole: str | None = None,
        certificateSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_webhook(
        self,
        *,
        webhookId: str,
        branchName: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
