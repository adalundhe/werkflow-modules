from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AccessAnalyzerClient(ABC):

    @abstractmethod
    def apply_archive_rule(
        self,
        *,
        analyzerArn: str,
        ruleName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_policy_generation(
        self,
        *,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_access_not_granted(
        self,
        *,
        policyDocument: str,
        access: list[dict[str, Any]],
        policyType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_no_new_access(
        self,
        *,
        newPolicyDocument: str,
        existingPolicyDocument: str,
        policyType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_no_public_access(
        self,
        *,
        policyDocument: str,
        resourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_preview(
        self,
        *,
        analyzerArn: str,
        configurations: dict[str, dict[str, Any]],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_analyzer(
        self,
        *,
        analyzerName: str,
        type: str,
        archiveRules: list[dict[str, Any]] | None = None,
        tags: dict[str, str] | None = None,
        clientToken: str | None = None,
        configuration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_archive_rule(
        self,
        *,
        analyzerName: str,
        ruleName: str,
        filter: dict[str, dict[str, Any]],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service_linked_analyzer(
        self,
        *,
        type: str,
        archiveRules: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
        configuration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_analyzer(
        self,
        *,
        analyzerName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_archive_rule(
        self,
        *,
        analyzerName: str,
        ruleName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_linked_analyzer(
        self,
        *,
        analyzerName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_finding_recommendation(
        self,
        *,
        analyzerArn: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_access_preview(
        self,
        *,
        accessPreviewId: str,
        analyzerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_analyzed_resource(
        self,
        *,
        analyzerArn: str,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_analyzer(
        self,
        *,
        analyzerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_archive_rule(
        self,
        *,
        analyzerName: str,
        ruleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding(
        self,
        *,
        analyzerArn: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_recommendation(
        self,
        *,
        analyzerArn: str,
        id: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_v2(
        self,
        *,
        analyzerArn: str,
        id: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_statistics(
        self,
        *,
        analyzerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_generated_policy(
        self,
        *,
        jobId: str,
        includeResourcePlaceholders: bool | None = None,
        includeServiceLevelTemplate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_preview_findings(
        self,
        *,
        accessPreviewId: str,
        analyzerArn: str,
        filter: dict[str, dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_previews(
        self,
        *,
        analyzerArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_analyzed_resources(
        self,
        *,
        analyzerArn: str,
        resourceType: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_analyzers(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_archive_rules(
        self,
        *,
        analyzerName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_findings(
        self,
        *,
        analyzerArn: str,
        filter: dict[str, dict[str, Any]] | None = None,
        sort: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_findings_v2(
        self,
        *,
        analyzerArn: str,
        filter: dict[str, dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sort: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_generations(
        self,
        *,
        principalArn: str | None = None,
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
    def start_policy_generation(
        self,
        *,
        policyGenerationDetails: dict[str, Any],
        cloudTrailDetails: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_resource_scan(
        self,
        *,
        analyzerArn: str,
        resourceArn: str,
        resourceOwnerAccount: str | None = None,
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
    def update_analyzer(
        self,
        *,
        analyzerName: str,
        configuration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_archive_rule(
        self,
        *,
        analyzerName: str,
        ruleName: str,
        filter: dict[str, dict[str, Any]],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_findings(
        self,
        *,
        analyzerArn: str,
        status: str,
        ids: list[str] | None = None,
        resourceArn: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_policy(
        self,
        *,
        policyDocument: str,
        policyType: str,
        locale: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        validatePolicyResourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
