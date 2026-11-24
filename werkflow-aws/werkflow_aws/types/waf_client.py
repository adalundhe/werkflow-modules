from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class WAFv2Client(ABC):

    @abstractmethod
    def associate_web_acl(
        self,
        *,
        WebACLArn: str,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_capacity(
        self,
        *,
        Scope: str,
        Rules: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api_key(
        self,
        *,
        Scope: str,
        TokenDomains: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ip_set(
        self,
        *,
        Name: str,
        Scope: str,
        IPAddressVersion: str,
        Addresses: list[str],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: str,
        RegularExpressionList: list[dict[str, Any]],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rule_group(
        self,
        *,
        Name: str,
        Scope: str,
        Capacity: int,
        VisibilityConfig: dict[str, Any],
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CustomResponseBodies: dict[str, dict[str, Any]] | None = None,
        MonetizationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_web_acl(
        self,
        *,
        Name: str,
        Scope: str,
        DefaultAction: dict[str, Any],
        VisibilityConfig: dict[str, Any],
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
        DataProtectionConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CustomResponseBodies: dict[str, dict[str, Any]] | None = None,
        CaptchaConfig: dict[str, Any] | None = None,
        ChallengeConfig: dict[str, Any] | None = None,
        TokenDomains: list[str] | None = None,
        AssociationConfig: dict[str, Any] | None = None,
        OnSourceDDoSProtectionConfig: dict[str, Any] | None = None,
        ApplicationConfig: dict[str, Any] | None = None,
        MonetizationConfig: dict[str, Any] | None = None,
        AnalyticsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_key(
        self,
        *,
        Scope: str,
        APIKey: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_firewall_manager_rule_groups(
        self,
        *,
        WebACLArn: str,
        WebACLLockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ip_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_logging_configuration(
        self,
        *,
        ResourceArn: str,
        LogType: str | None = None,
        LogScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_permission_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rule_group(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_web_acl(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_all_managed_products(
        self,
        *,
        Scope: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_products_by_vendor(
        self,
        *,
        VendorName: str,
        Scope: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_rule_group(
        self,
        *,
        VendorName: str,
        Name: str,
        Scope: str,
        VersionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_web_acl(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_mobile_sdk_release_url(
        self,
        *,
        Platform: str,
        ReleaseVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_decrypted_api_key(
        self,
        *,
        Scope: str,
        APIKey: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event(
        self,
        *,
        Scope: str,
        EventId: str,
        WebAclArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_actor(
        self,
        *,
        Scope: str,
        EventActorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ip_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_logging_configuration(
        self,
        *,
        ResourceArn: str,
        LogType: str | None = None,
        LogScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_rule_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_mobile_sdk_release(
        self,
        *,
        Platform: str,
        ReleaseVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_permission_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rate_based_statement_managed_keys(
        self,
        *,
        Scope: str,
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
        RuleGroupRuleName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_revenue_statistics(
        self,
        *,
        StatisticType: str,
        TimeWindow: dict[str, Any],
        Scope: str,
        Currency: str,
        GroupBy: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextMarker: str | None = None,
        Limit: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_revenue_statistics_summary(
        self,
        *,
        TimeWindow: dict[str, Any],
        Scope: str,
        Currency: str,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_revenue_statistics_time_series(
        self,
        *,
        StatisticType: str,
        TimeWindow: dict[str, Any],
        Scope: str,
        Interval: str,
        Currency: str,
        GroupBy: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextMarker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rule_group(
        self,
        *,
        Name: str | None = None,
        Scope: str | None = None,
        Id: str | None = None,
        ARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sampled_requests(
        self,
        *,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: str,
        TimeWindow: dict[str, Any],
        MaxItems: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_top_path_statistics_by_traffic(
        self,
        *,
        WebAclArn: str,
        Scope: str,
        TimeWindow: dict[str, Any],
        Limit: int,
        NumberOfTopTrafficBotsPerPath: int,
        UriPathPrefix: str | None = None,
        BotCategory: str | None = None,
        BotOrganization: str | None = None,
        BotName: str | None = None,
        NextMarker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_web_acl(
        self,
        *,
        Name: str | None = None,
        Scope: str | None = None,
        Id: str | None = None,
        ARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_web_acl_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_api_keys(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_available_managed_rule_group_versions(
        self,
        *,
        VendorName: str,
        Name: str,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_available_managed_rule_groups(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_actors(
        self,
        *,
        Scope: str,
        TimeWindow: dict[str, Any],
        SortBy: str | None = None,
        Limit: int | None = None,
        NextMarker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_events(
        self,
        *,
        Scope: str,
        TimeWindow: dict[str, Any] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ApiPatternFilters: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextMarker: str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        Include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_events_by_web_acl(
        self,
        *,
        Scope: str,
        WebAclArn: str,
        TimeWindow: dict[str, Any] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ApiPatternFilters: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextMarker: str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        Include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ip_sets(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_logging_configurations(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
        LogScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_managed_rule_sets(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mobile_sdk_releases(
        self,
        *,
        Platform: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_regex_pattern_sets(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resources_for_web_acl(
        self,
        *,
        WebACLArn: str,
        ResourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rule_groups(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_settlement_records(
        self,
        *,
        TimeWindow: dict[str, Any],
        Scope: str,
        Currency: str,
        Filters: list[dict[str, Any]] | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        Limit: int | None = None,
        NextMarker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_web_acls(
        self,
        *,
        Scope: str,
        NextMarker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_logging_configuration(
        self,
        *,
        LoggingConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_managed_rule_set_versions(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
        RecommendedVersion: str | None = None,
        VersionsToPublish: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_permission_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
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
    def update_ip_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        Addresses: list[str],
        LockToken: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_managed_rule_set_version_expiry_date(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        LockToken: str,
        VersionToExpire: str,
        ExpiryTimestamp: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        RegularExpressionList: list[dict[str, Any]],
        LockToken: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rule_group(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        VisibilityConfig: dict[str, Any],
        LockToken: str,
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
        CustomResponseBodies: dict[str, dict[str, Any]] | None = None,
        MonetizationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_web_acl(
        self,
        *,
        Name: str,
        Scope: str,
        Id: str,
        DefaultAction: dict[str, Any],
        VisibilityConfig: dict[str, Any],
        LockToken: str,
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
        DataProtectionConfig: dict[str, Any] | None = None,
        CustomResponseBodies: dict[str, dict[str, Any]] | None = None,
        CaptchaConfig: dict[str, Any] | None = None,
        ChallengeConfig: dict[str, Any] | None = None,
        TokenDomains: list[str] | None = None,
        AssociationConfig: dict[str, Any] | None = None,
        OnSourceDDoSProtectionConfig: dict[str, Any] | None = None,
        ApplicationConfig: dict[str, Any] | None = None,
        MonetizationConfig: dict[str, Any] | None = None,
        AnalyticsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
