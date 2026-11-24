from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class ELBv2Client(ABC):

    @abstractmethod
    def add_listener_certificates(
        self,
        *,
        ListenerArn: str,
        Certificates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags(
        self,
        *,
        ResourceArns: list[str],
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_trust_store_revocations(
        self,
        *,
        TrustStoreArn: str,
        RevocationContents: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_listener(
        self,
        *,
        LoadBalancerArn: str,
        DefaultActions: list[dict[str, Any]],
        Protocol: str | None = None,
        Port: int | None = None,
        SslPolicy: str | None = None,
        Certificates: list[dict[str, Any]] | None = None,
        AlpnPolicy: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        MutualAuthentication: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_load_balancer(
        self,
        *,
        Name: str,
        Subnets: list[str] | None = None,
        SubnetMappings: list[dict[str, Any]] | None = None,
        SecurityGroups: list[str] | None = None,
        Scheme: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Type: str | None = None,
        IpAddressType: str | None = None,
        CustomerOwnedIpv4Pool: str | None = None,
        EnablePrefixForIpv6SourceNat: str | None = None,
        IpamPools: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rule(
        self,
        *,
        ListenerArn: str,
        Conditions: list[dict[str, Any]],
        Priority: int,
        Actions: list[dict[str, Any]],
        Tags: list[dict[str, Any]] | None = None,
        Transforms: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_target_group(
        self,
        *,
        Name: str,
        Protocol: str | None = None,
        ProtocolVersion: str | None = None,
        Port: int | None = None,
        VpcId: str | None = None,
        HealthCheckProtocol: str | None = None,
        HealthCheckPort: str | None = None,
        HealthCheckEnabled: bool | None = None,
        HealthCheckPath: str | None = None,
        HealthCheckIntervalSeconds: int | None = None,
        HealthCheckTimeoutSeconds: int | None = None,
        HealthyThresholdCount: int | None = None,
        UnhealthyThresholdCount: int | None = None,
        Matcher: dict[str, Any] | None = None,
        TargetType: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        IpAddressType: str | None = None,
        TargetControlPort: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trust_store(
        self,
        *,
        Name: str,
        CaCertificatesBundleS3Bucket: str,
        CaCertificatesBundleS3Key: str,
        CaCertificatesBundleS3ObjectVersion: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_listener(
        self,
        *,
        ListenerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_load_balancer(
        self,
        *,
        LoadBalancerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rule(
        self,
        *,
        RuleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_shared_trust_store_association(
        self,
        *,
        TrustStoreArn: str,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_target_group(
        self,
        *,
        TargetGroupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trust_store(
        self,
        *,
        TrustStoreArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_targets(
        self,
        *,
        TargetGroupArn: str,
        Targets: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_limits(
        self,
        *,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation(
        self,
        *,
        LoadBalancerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_listener_attributes(
        self,
        *,
        ListenerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_listener_certificates(
        self,
        *,
        ListenerArn: str,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_listeners(
        self,
        *,
        LoadBalancerArn: str | None = None,
        ListenerArns: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_load_balancer_attributes(
        self,
        *,
        LoadBalancerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_load_balancers(
        self,
        *,
        LoadBalancerArns: list[str] | None = None,
        Names: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_rules(
        self,
        *,
        ListenerArn: str | None = None,
        RuleArns: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ssl_policies(
        self,
        *,
        Names: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
        LoadBalancerType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        ResourceArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_target_group_attributes(
        self,
        *,
        TargetGroupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_target_groups(
        self,
        *,
        LoadBalancerArn: str | None = None,
        TargetGroupArns: list[str] | None = None,
        Names: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_target_health(
        self,
        *,
        TargetGroupArn: str,
        Targets: list[dict[str, Any]] | None = None,
        Include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trust_store_associations(
        self,
        *,
        TrustStoreArn: str,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trust_store_revocations(
        self,
        *,
        TrustStoreArn: str,
        RevocationIds: list[int] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trust_stores(
        self,
        *,
        TrustStoreArns: list[str] | None = None,
        Names: list[str] | None = None,
        Marker: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trust_store_ca_certificates_bundle(
        self,
        *,
        TrustStoreArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trust_store_revocation_content(
        self,
        *,
        TrustStoreArn: str,
        RevocationId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_capacity_reservation(
        self,
        *,
        LoadBalancerArn: str,
        MinimumLoadBalancerCapacity: dict[str, Any] | None = None,
        ResetCapacityReservation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ip_pools(
        self,
        *,
        LoadBalancerArn: str,
        IpamPools: dict[str, Any] | None = None,
        RemoveIpamPools: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_listener(
        self,
        *,
        ListenerArn: str,
        Port: int | None = None,
        Protocol: str | None = None,
        SslPolicy: str | None = None,
        Certificates: list[dict[str, Any]] | None = None,
        DefaultActions: list[dict[str, Any]] | None = None,
        AlpnPolicy: list[str] | None = None,
        MutualAuthentication: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_listener_attributes(
        self,
        *,
        ListenerArn: str,
        Attributes: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_load_balancer_attributes(
        self,
        *,
        LoadBalancerArn: str,
        Attributes: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_rule(
        self,
        *,
        RuleArn: str,
        Conditions: list[dict[str, Any]] | None = None,
        Actions: list[dict[str, Any]] | None = None,
        Transforms: list[dict[str, Any]] | None = None,
        ResetTransforms: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_target_group(
        self,
        *,
        TargetGroupArn: str,
        HealthCheckProtocol: str | None = None,
        HealthCheckPort: str | None = None,
        HealthCheckPath: str | None = None,
        HealthCheckEnabled: bool | None = None,
        HealthCheckIntervalSeconds: int | None = None,
        HealthCheckTimeoutSeconds: int | None = None,
        HealthyThresholdCount: int | None = None,
        UnhealthyThresholdCount: int | None = None,
        Matcher: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_target_group_attributes(
        self,
        *,
        TargetGroupArn: str,
        Attributes: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_trust_store(
        self,
        *,
        TrustStoreArn: str,
        CaCertificatesBundleS3Bucket: str,
        CaCertificatesBundleS3Key: str,
        CaCertificatesBundleS3ObjectVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_targets(
        self,
        *,
        TargetGroupArn: str,
        Targets: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_listener_certificates(
        self,
        *,
        ListenerArn: str,
        Certificates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags(
        self,
        *,
        ResourceArns: list[str],
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_trust_store_revocations(
        self,
        *,
        TrustStoreArn: str,
        RevocationIds: list[int],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_ip_address_type(
        self,
        *,
        LoadBalancerArn: str,
        IpAddressType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_rule_priorities(
        self,
        *,
        RulePriorities: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_security_groups(
        self,
        *,
        LoadBalancerArn: str,
        SecurityGroups: list[str],
        EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_subnets(
        self,
        *,
        LoadBalancerArn: str,
        Subnets: list[str] | None = None,
        SubnetMappings: list[dict[str, Any]] | None = None,
        IpAddressType: str | None = None,
        EnablePrefixForIpv6SourceNat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
