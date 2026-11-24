from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class Route53Client(ABC):

    @abstractmethod
    def list_hosted_zones(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
        DelegationSetId: str | None = None,
        HostedZoneType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hosted_zones_by_name(
        self,
        *,
        DNSName: str | None = None,
        HostedZoneId: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_hosted_zone(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hosted_zone(
        self,
        *,
        Name: str,
        CallerReference: str,
        VPC: dict[str, Any] | None = None,
        HostedZoneConfig: dict[str, Any] | None = None,
        DelegationSetId: str | None = None,
        EnablePublicDNSFallback: bool | None = None,
        ChangeGuardrails: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hosted_zone(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_record_sets(
        self,
        *,
        HostedZoneId: str,
        StartRecordName: str | None = None,
        StartRecordType: str | None = None,
        StartRecordIdentifier: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_resource_record_sets(
        self,
        *,
        HostedZoneId: str,
        ChangeBatch: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_change(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_health_checks(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_health_check(
        self,
        *,
        HealthCheckId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_health_check_status(
        self,
        *,
        HealthCheckId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_health_check(
        self,
        *,
        CallerReference: str,
        HealthCheckConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_health_check(
        self,
        *,
        HealthCheckId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_tags_for_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
        AddTags: list[dict[str, Any]] | None = None,
        RemoveTagKeys: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def activate_key_signing_key(
        self,
        *,
        HostedZoneId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_vpc_with_hosted_zone(
        self,
        *,
        HostedZoneId: str,
        VPC: dict[str, Any],
        Comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_cidr_collection(
        self,
        *,
        Id: str,
        Changes: list[dict[str, Any]],
        CollectionVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cidr_collection(
        self,
        *,
        Name: str,
        CallerReference: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_health_check_source(
        self,
        *,
        HealthCheckSourceConfig: dict[str, Any],
        CallerReference: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key_signing_key(
        self,
        *,
        CallerReference: str,
        HostedZoneId: str,
        KeyManagementServiceArn: str,
        Name: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_query_logging_config(
        self,
        *,
        HostedZoneId: str,
        CloudWatchLogsLogGroupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_record_set_protections(
        self,
        *,
        HostedZoneId: str,
        Protections: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_reusable_delegation_set(
        self,
        *,
        CallerReference: str,
        HostedZoneId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_policy(
        self,
        *,
        Name: str,
        Document: str,
        Comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_policy_instance(
        self,
        *,
        HostedZoneId: str,
        Name: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_policy_version(
        self,
        *,
        Id: str,
        Document: str,
        Comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_association_authorization(
        self,
        *,
        HostedZoneId: str,
        VPC: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_key_signing_key(
        self,
        *,
        HostedZoneId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cidr_collection(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_health_check_source(
        self,
        *,
        HealthCheckSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key_signing_key(
        self,
        *,
        HostedZoneId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_query_logging_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_record_set_protections(
        self,
        *,
        HostedZoneId: str,
        Protections: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_reusable_delegation_set(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_policy(
        self,
        *,
        Id: str,
        Version: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_policy_instance(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_association_authorization(
        self,
        *,
        HostedZoneId: str,
        VPC: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_hosted_zone_dnssec(
        self,
        *,
        HostedZoneId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_vpc_from_hosted_zone(
        self,
        *,
        HostedZoneId: str,
        VPC: dict[str, Any],
        Comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_hosted_zone_dnssec(
        self,
        *,
        HostedZoneId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_limit(
        self,
        *,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_checker_ip_ranges(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dnssec(
        self,
        *,
        HostedZoneId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_geo_location(
        self,
        *,
        ContinentCode: str | None = None,
        CountryCode: str | None = None,
        SubdivisionCode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_health_check_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_health_check_last_failure_reason(
        self,
        *,
        HealthCheckId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_health_check_source(
        self,
        *,
        HealthCheckSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_hosted_zone_change_batch(
        self,
        *,
        HostedZoneId: str,
        ChangeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_hosted_zone_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_hosted_zone_limit(
        self,
        *,
        Type: str,
        HostedZoneId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_logging_config(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reusable_delegation_set(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reusable_delegation_set_limit(
        self,
        *,
        Type: str,
        DelegationSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_traffic_policy(
        self,
        *,
        Id: str,
        Version: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_traffic_policy_instance(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_traffic_policy_instance_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cidr_blocks(
        self,
        *,
        CollectionId: str,
        LocationName: str | None = None,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cidr_collections(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cidr_locations(
        self,
        *,
        CollectionId: str,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_geo_locations(
        self,
        *,
        StartContinentCode: str | None = None,
        StartCountryCode: str | None = None,
        StartSubdivisionCode: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_health_check_sources(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_health_checks_by_source(
        self,
        *,
        HealthCheckSourceId: str,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hosted_zone_change_batches(
        self,
        *,
        HostedZoneId: str,
        SubmittedAfter: str | None = None,
        SubmittedBefore: str | None = None,
        StartAfterChangeId: str | None = None,
        SortOrder: str | None = None,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hosted_zones_by_vpc(
        self,
        *,
        VPCId: str,
        VPCRegion: str,
        MaxItems: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_query_logging_configs(
        self,
        *,
        HostedZoneId: str | None = None,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_record_set_changes(
        self,
        *,
        HostedZoneId: str,
        RecordName: str | None = None,
        RecordType: str | None = None,
        SubmittedAfter: str | None = None,
        SubmittedBefore: str | None = None,
        SortOrder: str | None = None,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_record_set_protections(
        self,
        *,
        HostedZoneId: str,
        StartRecordName: str | None = None,
        StartRecordType: str | None = None,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_reusable_delegation_sets(
        self,
        *,
        Marker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resources(
        self,
        *,
        ResourceType: str,
        ResourceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_policies(
        self,
        *,
        TrafficPolicyIdMarker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_policy_instances(
        self,
        *,
        HostedZoneIdMarker: str | None = None,
        TrafficPolicyInstanceNameMarker: str | None = None,
        TrafficPolicyInstanceTypeMarker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_policy_instances_by_hosted_zone(
        self,
        *,
        HostedZoneId: str,
        TrafficPolicyInstanceNameMarker: str | None = None,
        TrafficPolicyInstanceTypeMarker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_policy_instances_by_policy(
        self,
        *,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
        HostedZoneIdMarker: str | None = None,
        TrafficPolicyInstanceNameMarker: str | None = None,
        TrafficPolicyInstanceTypeMarker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_policy_versions(
        self,
        *,
        Id: str,
        TrafficPolicyVersionMarker: str | None = None,
        MaxItems: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_association_authorizations(
        self,
        *,
        HostedZoneId: str,
        NextToken: str | None = None,
        MaxResults: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_dns_answer(
        self,
        *,
        HostedZoneId: str,
        RecordName: str,
        RecordType: str,
        ResolverIP: str | None = None,
        EDNS0ClientSubnetIP: str | None = None,
        EDNS0ClientSubnetMask: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_health_check(
        self,
        *,
        HealthCheckId: str,
        HealthCheckVersion: int | None = None,
        IPAddress: str | None = None,
        Port: int | None = None,
        ResourcePath: str | None = None,
        FullyQualifiedDomainName: str | None = None,
        SearchString: str | None = None,
        FailureThreshold: int | None = None,
        Inverted: bool | None = None,
        Disabled: bool | None = None,
        HealthThreshold: int | None = None,
        ChildHealthChecks: list[str] | None = None,
        EnableSNI: bool | None = None,
        Regions: list[str] | None = None,
        AlarmIdentifier: dict[str, Any] | None = None,
        InsufficientDataHealthStatus: str | None = None,
        ResetElements: list[str] | None = None,
        HealthCheckSourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hosted_zone_comment(
        self,
        *,
        Id: str,
        Comment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hosted_zone_features(
        self,
        *,
        HostedZoneId: str,
        EnableAcceleratedRecovery: bool | None = None,
        EnablePublicDNSFallback: bool | None = None,
        ChangeGuardrails: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hosted_zone_tier(
        self,
        *,
        HostedZoneId: str,
        HostedZoneTier: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_traffic_policy_comment(
        self,
        *,
        Id: str,
        Version: int,
        Comment: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_traffic_policy_instance(
        self,
        *,
        Id: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
