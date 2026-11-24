from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AppRunnerClient(ABC):

    @abstractmethod
    def associate_custom_domain(
        self,
        *,
        ServiceArn: str,
        DomainName: str,
        EnableWWWSubdomain: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationName: str,
        MaxConcurrency: int | None = None,
        MinSize: int | None = None,
        MaxSize: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_observability_configuration(
        self,
        *,
        ObservabilityConfigurationName: str,
        TraceConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service(
        self,
        *,
        ServiceName: str,
        SourceConfiguration: dict[str, Any],
        InstanceConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
        HealthCheckConfiguration: dict[str, Any] | None = None,
        AutoScalingConfigurationArn: str | None = None,
        NetworkConfiguration: dict[str, Any] | None = None,
        ObservabilityConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_connector(
        self,
        *,
        VpcConnectorName: str,
        Subnets: list[str],
        SecurityGroups: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_ingress_connection(
        self,
        *,
        ServiceArn: str,
        VpcIngressConnectionName: str,
        IngressVpcConfiguration: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationArn: str,
        DeleteAllRevisions: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        ConnectionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_observability_configuration(
        self,
        *,
        ObservabilityConfigurationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service(
        self,
        *,
        ServiceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_connector(
        self,
        *,
        VpcConnectorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_ingress_connection(
        self,
        *,
        VpcIngressConnectionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_domains(
        self,
        *,
        ServiceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_observability_configuration(
        self,
        *,
        ObservabilityConfigurationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service(
        self,
        *,
        ServiceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_connector(
        self,
        *,
        VpcConnectorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_ingress_connection(
        self,
        *,
        VpcIngressConnectionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_custom_domain(
        self,
        *,
        ServiceArn: str,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_auto_scaling_configurations(
        self,
        *,
        AutoScalingConfigurationName: str | None = None,
        LatestOnly: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connections(
        self,
        *,
        ConnectionName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_observability_configurations(
        self,
        *,
        ObservabilityConfigurationName: str | None = None,
        LatestOnly: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_operations(
        self,
        *,
        ServiceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_services(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_services_for_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationArn: str,
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
    def list_vpc_connectors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_ingress_connections(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def pause_service(
        self,
        *,
        ServiceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_service(
        self,
        *,
        ServiceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_deployment(
        self,
        *,
        ServiceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
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
    def update_default_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service(
        self,
        *,
        ServiceArn: str,
        SourceConfiguration: dict[str, Any] | None = None,
        InstanceConfiguration: dict[str, Any] | None = None,
        AutoScalingConfigurationArn: str | None = None,
        HealthCheckConfiguration: dict[str, Any] | None = None,
        NetworkConfiguration: dict[str, Any] | None = None,
        ObservabilityConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_ingress_connection(
        self,
        *,
        VpcIngressConnectionArn: str,
        IngressVpcConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
