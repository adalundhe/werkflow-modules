from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class Route53ARCClient(ABC):

    @abstractmethod
    def create_cluster(
        self,
        *,
        ClusterName: str,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_control_panel(
        self,
        *,
        ClusterArn: str,
        ControlPanelName: str,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_routing_control(
        self,
        *,
        ClusterArn: str,
        RoutingControlName: str,
        ClientToken: str | None = None,
        ControlPanelArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_safety_rule(
        self,
        *,
        AssertionRule: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        GatingRule: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_control_panel(
        self,
        *,
        ControlPanelArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_routing_control(
        self,
        *,
        RoutingControlArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_safety_rule(
        self,
        *,
        SafetyRuleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_control_panel(
        self,
        *,
        ControlPanelArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_routing_control(
        self,
        *,
        RoutingControlArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_safety_rule(
        self,
        *,
        SafetyRuleArn: str,
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
    def list_associated_route53_health_checks(
        self,
        *,
        RoutingControlArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_clusters(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_control_panels(
        self,
        *,
        ClusterArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routing_controls(
        self,
        *,
        ControlPanelArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_safety_rules(
        self,
        *,
        ControlPanelArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
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
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster(
        self,
        *,
        ClusterArn: str,
        NetworkType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_control_panel(
        self,
        *,
        ControlPanelArn: str,
        ControlPanelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_control(
        self,
        *,
        RoutingControlArn: str,
        RoutingControlName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_safety_rule(
        self,
        *,
        AssertionRuleUpdate: dict[str, Any] | None = None,
        GatingRuleUpdate: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
