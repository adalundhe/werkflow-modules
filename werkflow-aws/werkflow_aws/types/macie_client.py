from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class MacieClient(ABC):

    @abstractmethod
    def accept_invitation(
        self,
        *,
        invitationId: str,
        administratorAccountId: str | None = None,
        masterAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_custom_data_identifiers(
        self,
        *,
        ids: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_automated_discovery_accounts(
        self,
        *,
        accounts: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_allow_list(
        self,
        *,
        clientToken: str,
        criteria: dict[str, Any],
        name: str,
        description: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_classification_job(
        self,
        *,
        clientToken: str,
        jobType: str,
        name: str,
        s3JobDefinition: dict[str, Any],
        allowListIds: list[str] | None = None,
        customDataIdentifierIds: list[str] | None = None,
        description: str | None = None,
        initialRun: bool | None = None,
        managedDataIdentifierIds: list[str] | None = None,
        managedDataIdentifierSelector: str | None = None,
        samplingPercentage: int | None = None,
        scheduleFrequency: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_data_identifier(
        self,
        *,
        name: str,
        regex: str,
        clientToken: str | None = None,
        description: str | None = None,
        ignoreWords: list[str] | None = None,
        keywords: list[str] | None = None,
        maximumMatchDistance: int | None = None,
        severityLevels: list[dict[str, Any]] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_findings_filter(
        self,
        *,
        action: str,
        findingCriteria: dict[str, Any],
        name: str,
        clientToken: str | None = None,
        description: str | None = None,
        position: int | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_invitations(
        self,
        *,
        accountIds: list[str],
        disableEmailNotification: bool | None = None,
        message: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_member(
        self,
        *,
        account: dict[str, Any],
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_sample_findings(
        self,
        *,
        findingTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decline_invitations(
        self,
        *,
        accountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_allow_list(
        self,
        *,
        id: str,
        ignoreJobChecks: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_data_identifier(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_findings_filter(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_invitations(
        self,
        *,
        accountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_member(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_buckets(
        self,
        *,
        criteria: dict[str, dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_classification_job(
        self,
        *,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_macie(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organization_admin_account(
        self,
        *,
        adminAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_administrator_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_master_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_member(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_macie(
        self,
        *,
        clientToken: str | None = None,
        findingPublishingFrequency: str | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organization_admin_account(
        self,
        *,
        adminAccountId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_administrator_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_allow_list(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_discovery_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_statistics(
        self,
        *,
        accountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_classification_export_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_classification_scope(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_data_identifier(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_statistics(
        self,
        *,
        groupBy: str,
        findingCriteria: dict[str, Any] | None = None,
        size: int | None = None,
        sortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings(
        self,
        *,
        findingIds: list[str],
        sortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_filter(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_publication_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_invitations_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_macie_session(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_master_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_member(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_profile(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reveal_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sensitive_data_occurrences(
        self,
        *,
        findingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sensitive_data_occurrences_availability(
        self,
        *,
        findingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sensitivity_inspection_template(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_statistics(
        self,
        *,
        filterBy: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: dict[str, Any] | None = None,
        timeRange: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_totals(
        self,
        *,
        timeRange: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_allow_lists(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automated_discovery_accounts(
        self,
        *,
        accountIds: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_classification_jobs(
        self,
        *,
        filterCriteria: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_classification_scopes(
        self,
        *,
        name: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_data_identifiers(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_findings(
        self,
        *,
        findingCriteria: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_findings_filters(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invitations(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_managed_data_identifiers(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_members(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        onlyAssociated: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_admin_accounts(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_profile_artifacts(
        self,
        *,
        resourceArn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_profile_detections(
        self,
        *,
        resourceArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sensitivity_inspection_templates(
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
    def put_classification_export_configuration(
        self,
        *,
        configuration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_findings_publication_configuration(
        self,
        *,
        clientToken: str | None = None,
        securityHubConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_resources(
        self,
        *,
        bucketCriteria: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortCriteria: dict[str, Any] | None = None,
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
    def test_custom_data_identifier(
        self,
        *,
        regex: str,
        sampleText: str,
        ignoreWords: list[str] | None = None,
        keywords: list[str] | None = None,
        maximumMatchDistance: int | None = None,
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
    def update_allow_list(
        self,
        *,
        criteria: dict[str, Any],
        id: str,
        name: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automated_discovery_configuration(
        self,
        *,
        status: str,
        autoEnableOrganizationMembers: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_classification_job(
        self,
        *,
        jobId: str,
        jobStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_classification_scope(
        self,
        *,
        id: str,
        s3: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_findings_filter(
        self,
        *,
        id: str,
        action: str | None = None,
        clientToken: str | None = None,
        description: str | None = None,
        findingCriteria: dict[str, Any] | None = None,
        name: str | None = None,
        position: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_macie_session(
        self,
        *,
        findingPublishingFrequency: str | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_member_session(
        self,
        *,
        id: str,
        status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_organization_configuration(
        self,
        *,
        autoEnable: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_profile(
        self,
        *,
        resourceArn: str,
        sensitivityScoreOverride: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_profile_detections(
        self,
        *,
        resourceArn: str,
        suppressDataIdentifiers: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_reveal_configuration(
        self,
        *,
        configuration: dict[str, Any],
        retrievalConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_sensitivity_inspection_template(
        self,
        *,
        id: str,
        description: str | None = None,
        excludes: dict[str, Any] | None = None,
        includes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
