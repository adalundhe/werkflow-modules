from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class MigrationHubClient(ABC):

    @abstractmethod
    def create_application(
        self,
        *,
        EnvironmentIdentifier: str,
        Name: str,
        ProxyType: str,
        VpcId: str,
        ApiGatewayProxy: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment(
        self,
        *,
        Name: str,
        NetworkFabricType: str,
        ClientToken: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        RouteType: str,
        ServiceIdentifier: str,
        ClientToken: str | None = None,
        DefaultRoute: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        UriPathRoute: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service(
        self,
        *,
        ApplicationIdentifier: str,
        EndpointType: str,
        EnvironmentIdentifier: str,
        Name: str,
        ClientToken: str | None = None,
        Description: str | None = None,
        LambdaEndpoint: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        UrlEndpoint: dict[str, Any] | None = None,
        VpcId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment(
        self,
        *,
        EnvironmentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        RouteIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        ServiceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_application(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment(
        self,
        *,
        EnvironmentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        RouteIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        ServiceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_applications(
        self,
        *,
        EnvironmentIdentifier: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environment_vpcs(
        self,
        *,
        EnvironmentIdentifier: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environments(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routes(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_services(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
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
    def put_resource_policy(
        self,
        *,
        Policy: str,
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
    def update_route(
        self,
        *,
        ActivationState: str,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        RouteIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
