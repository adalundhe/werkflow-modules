from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class APIGatewayV2Client(ABC):

    @abstractmethod
    def create_api(
        self,
        *,
        Name: str,
        ProtocolType: str,
        ApiKeySelectionExpression: str | None = None,
        CorsConfiguration: dict[str, Any] | None = None,
        CredentialsArn: str | None = None,
        Description: str | None = None,
        DisableSchemaValidation: bool | None = None,
        DisableExecuteApiEndpoint: bool | None = None,
        IpAddressType: str | None = None,
        RouteKey: str | None = None,
        RouteSelectionExpression: str | None = None,
        Tags: dict[str, str] | None = None,
        Target: str | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api_mapping(
        self,
        *,
        ApiId: str,
        DomainName: str,
        Stage: str,
        ApiMappingKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_authorizer(
        self,
        *,
        ApiId: str,
        AuthorizerType: str,
        IdentitySource: list[str],
        Name: str,
        AuthorizerCredentialsArn: str | None = None,
        AuthorizerPayloadFormatVersion: str | None = None,
        AuthorizerResultTtlInSeconds: int | None = None,
        AuthorizerUri: str | None = None,
        EnableSimpleResponses: bool | None = None,
        IdentityValidationExpression: str | None = None,
        JwtConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_deployment(
        self,
        *,
        ApiId: str,
        Description: str | None = None,
        StageName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_name(
        self,
        *,
        DomainName: str,
        DomainNameConfigurations: list[dict[str, Any]] | None = None,
        MutualTlsAuthentication: dict[str, Any] | None = None,
        RoutingMode: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration(
        self,
        *,
        ApiId: str,
        IntegrationType: str,
        ConnectionId: str | None = None,
        ConnectionType: str | None = None,
        ContentHandlingStrategy: str | None = None,
        CredentialsArn: str | None = None,
        Description: str | None = None,
        IntegrationMethod: str | None = None,
        IntegrationSubtype: str | None = None,
        IntegrationUri: str | None = None,
        PassthroughBehavior: str | None = None,
        PayloadFormatVersion: str | None = None,
        RequestParameters: dict[str, str] | None = None,
        RequestTemplates: dict[str, str] | None = None,
        ResponseParameters: dict[str, dict[str, str]] | None = None,
        TemplateSelectionExpression: str | None = None,
        TimeoutInMillis: int | None = None,
        TlsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration_response(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: str | None = None,
        ResponseParameters: dict[str, str] | None = None,
        ResponseTemplates: dict[str, str] | None = None,
        TemplateSelectionExpression: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model(
        self,
        *,
        ApiId: str,
        Name: str,
        Schema: str,
        ContentType: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_portal(
        self,
        *,
        Authorization: dict[str, Any],
        EndpointConfiguration: dict[str, Any],
        PortalContent: dict[str, Any],
        IncludedPortalProductArns: list[str] | None = None,
        LogoUri: str | None = None,
        RumAppMonitorName: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_portal_product(
        self,
        *,
        DisplayName: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_product_page(
        self,
        *,
        DisplayContent: dict[str, Any],
        PortalProductId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_product_rest_endpoint_page(
        self,
        *,
        PortalProductId: str,
        RestEndpointIdentifier: dict[str, Any],
        DisplayContent: dict[str, Any] | None = None,
        TryItState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route(
        self,
        *,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: bool | None = None,
        AuthorizationScopes: list[str] | None = None,
        AuthorizationType: str | None = None,
        AuthorizerId: str | None = None,
        ModelSelectionExpression: str | None = None,
        OperationName: str | None = None,
        RequestModels: dict[str, str] | None = None,
        RequestParameters: dict[str, dict[str, Any]] | None = None,
        RouteResponseSelectionExpression: str | None = None,
        Target: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_response(
        self,
        *,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        ModelSelectionExpression: str | None = None,
        ResponseModels: dict[str, str] | None = None,
        ResponseParameters: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_routing_rule(
        self,
        *,
        Actions: list[dict[str, Any]],
        Conditions: list[dict[str, Any]],
        DomainName: str,
        Priority: int,
        DomainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stage(
        self,
        *,
        ApiId: str,
        StageName: str,
        AccessLogSettings: dict[str, Any] | None = None,
        AutoDeploy: bool | None = None,
        ClientCertificateId: str | None = None,
        DefaultRouteSettings: dict[str, Any] | None = None,
        DeploymentId: str | None = None,
        Description: str | None = None,
        RouteSettings: dict[str, dict[str, Any]] | None = None,
        StageVariables: dict[str, str] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_link(
        self,
        *,
        Name: str,
        SubnetIds: list[str],
        SecurityGroupIds: list[str] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_log_settings(
        self,
        *,
        ApiId: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api(
        self,
        *,
        ApiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_mapping(
        self,
        *,
        ApiMappingId: str,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_authorizer(
        self,
        *,
        ApiId: str,
        AuthorizerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cors_configuration(
        self,
        *,
        ApiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_deployment(
        self,
        *,
        ApiId: str,
        DeploymentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_name(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration_response(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model(
        self,
        *,
        ApiId: str,
        ModelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_portal(
        self,
        *,
        PortalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_portal_product(
        self,
        *,
        PortalProductId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_portal_product_sharing_policy(
        self,
        *,
        PortalProductId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_product_page(
        self,
        *,
        PortalProductId: str,
        ProductPageId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_product_rest_endpoint_page(
        self,
        *,
        PortalProductId: str,
        ProductRestEndpointPageId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route(
        self,
        *,
        ApiId: str,
        RouteId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_request_parameter(
        self,
        *,
        ApiId: str,
        RequestParameterKey: str,
        RouteId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_response(
        self,
        *,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_settings(
        self,
        *,
        ApiId: str,
        RouteKey: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_routing_rule(
        self,
        *,
        DomainName: str,
        RoutingRuleId: str,
        DomainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stage(
        self,
        *,
        ApiId: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_link(
        self,
        *,
        VpcLinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_portal(
        self,
        *,
        PortalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_api(
        self,
        *,
        ApiId: str,
        OutputType: str,
        Specification: str,
        ExportVersion: str | None = None,
        IncludeExtensions: bool | None = None,
        StageName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api(
        self,
        *,
        ApiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_mapping(
        self,
        *,
        ApiMappingId: str,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_mappings(
        self,
        *,
        DomainName: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apis(
        self,
        *,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorizer(
        self,
        *,
        ApiId: str,
        AuthorizerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorizers(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deployment(
        self,
        *,
        ApiId: str,
        DeploymentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deployments(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_name(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_names(
        self,
        *,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration_response(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration_responses(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integrations(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model(
        self,
        *,
        ApiId: str,
        ModelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_template(
        self,
        *,
        ApiId: str,
        ModelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_models(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_portal(
        self,
        *,
        PortalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_portal_product(
        self,
        *,
        PortalProductId: str,
        ResourceOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_portal_product_sharing_policy(
        self,
        *,
        PortalProductId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_product_page(
        self,
        *,
        PortalProductId: str,
        ProductPageId: str,
        ResourceOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_product_rest_endpoint_page(
        self,
        *,
        PortalProductId: str,
        ProductRestEndpointPageId: str,
        IncludeRawDisplayContent: str | None = None,
        ResourceOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route(
        self,
        *,
        ApiId: str,
        RouteId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route_response(
        self,
        *,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route_responses(
        self,
        *,
        ApiId: str,
        RouteId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_routes(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_routing_rule(
        self,
        *,
        DomainName: str,
        RoutingRuleId: str,
        DomainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stage(
        self,
        *,
        ApiId: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stages(
        self,
        *,
        ApiId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tags(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_link(
        self,
        *,
        VpcLinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_links(
        self,
        *,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_api(
        self,
        *,
        Body: str,
        Basepath: str | None = None,
        FailOnWarnings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_portal_products(
        self,
        *,
        MaxResults: str | None = None,
        NextToken: str | None = None,
        ResourceOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_portals(
        self,
        *,
        MaxResults: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_product_pages(
        self,
        *,
        PortalProductId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
        ResourceOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_product_rest_endpoint_pages(
        self,
        *,
        PortalProductId: str,
        MaxResults: str | None = None,
        NextToken: str | None = None,
        ResourceOwnerAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routing_rules(
        self,
        *,
        DomainName: str,
        DomainNameId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def preview_portal(
        self,
        *,
        PortalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_portal(
        self,
        *,
        PortalId: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_portal_product_sharing_policy(
        self,
        *,
        PolicyDocument: str,
        PortalProductId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_routing_rule(
        self,
        *,
        Actions: list[dict[str, Any]],
        Conditions: list[dict[str, Any]],
        DomainName: str,
        Priority: int,
        RoutingRuleId: str,
        DomainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reimport_api(
        self,
        *,
        ApiId: str,
        Body: str,
        Basepath: str | None = None,
        FailOnWarnings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_authorizers_cache(
        self,
        *,
        ApiId: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str] | None = None,
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
    def update_api(
        self,
        *,
        ApiId: str,
        ApiKeySelectionExpression: str | None = None,
        CorsConfiguration: dict[str, Any] | None = None,
        CredentialsArn: str | None = None,
        Description: str | None = None,
        DisableSchemaValidation: bool | None = None,
        DisableExecuteApiEndpoint: bool | None = None,
        IpAddressType: str | None = None,
        Name: str | None = None,
        RouteKey: str | None = None,
        RouteSelectionExpression: str | None = None,
        Target: str | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_api_mapping(
        self,
        *,
        ApiId: str,
        ApiMappingId: str,
        DomainName: str,
        ApiMappingKey: str | None = None,
        Stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_authorizer(
        self,
        *,
        ApiId: str,
        AuthorizerId: str,
        AuthorizerCredentialsArn: str | None = None,
        AuthorizerPayloadFormatVersion: str | None = None,
        AuthorizerResultTtlInSeconds: int | None = None,
        AuthorizerType: str | None = None,
        AuthorizerUri: str | None = None,
        EnableSimpleResponses: bool | None = None,
        IdentitySource: list[str] | None = None,
        IdentityValidationExpression: str | None = None,
        JwtConfiguration: dict[str, Any] | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_deployment(
        self,
        *,
        ApiId: str,
        DeploymentId: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_name(
        self,
        *,
        DomainName: str,
        DomainNameConfigurations: list[dict[str, Any]] | None = None,
        MutualTlsAuthentication: dict[str, Any] | None = None,
        RoutingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        ConnectionId: str | None = None,
        ConnectionType: str | None = None,
        ContentHandlingStrategy: str | None = None,
        CredentialsArn: str | None = None,
        Description: str | None = None,
        IntegrationMethod: str | None = None,
        IntegrationSubtype: str | None = None,
        IntegrationType: str | None = None,
        IntegrationUri: str | None = None,
        PassthroughBehavior: str | None = None,
        PayloadFormatVersion: str | None = None,
        RequestParameters: dict[str, str] | None = None,
        RequestTemplates: dict[str, str] | None = None,
        ResponseParameters: dict[str, dict[str, str]] | None = None,
        TemplateSelectionExpression: str | None = None,
        TimeoutInMillis: int | None = None,
        TlsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration_response(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
        ContentHandlingStrategy: str | None = None,
        IntegrationResponseKey: str | None = None,
        ResponseParameters: dict[str, str] | None = None,
        ResponseTemplates: dict[str, str] | None = None,
        TemplateSelectionExpression: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_model(
        self,
        *,
        ApiId: str,
        ModelId: str,
        ContentType: str | None = None,
        Description: str | None = None,
        Name: str | None = None,
        Schema: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_portal(
        self,
        *,
        PortalId: str,
        Authorization: dict[str, Any] | None = None,
        EndpointConfiguration: dict[str, Any] | None = None,
        IncludedPortalProductArns: list[str] | None = None,
        LogoUri: str | None = None,
        PortalContent: dict[str, Any] | None = None,
        RumAppMonitorName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_portal_product(
        self,
        *,
        PortalProductId: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        DisplayOrder: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_product_page(
        self,
        *,
        PortalProductId: str,
        ProductPageId: str,
        DisplayContent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_product_rest_endpoint_page(
        self,
        *,
        PortalProductId: str,
        ProductRestEndpointPageId: str,
        DisplayContent: dict[str, Any] | None = None,
        TryItState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_route(
        self,
        *,
        ApiId: str,
        RouteId: str,
        ApiKeyRequired: bool | None = None,
        AuthorizationScopes: list[str] | None = None,
        AuthorizationType: str | None = None,
        AuthorizerId: str | None = None,
        ModelSelectionExpression: str | None = None,
        OperationName: str | None = None,
        RequestModels: dict[str, str] | None = None,
        RequestParameters: dict[str, dict[str, Any]] | None = None,
        RouteKey: str | None = None,
        RouteResponseSelectionExpression: str | None = None,
        Target: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_route_response(
        self,
        *,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
        ModelSelectionExpression: str | None = None,
        ResponseModels: dict[str, str] | None = None,
        ResponseParameters: dict[str, dict[str, Any]] | None = None,
        RouteResponseKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stage(
        self,
        *,
        ApiId: str,
        StageName: str,
        AccessLogSettings: dict[str, Any] | None = None,
        AutoDeploy: bool | None = None,
        ClientCertificateId: str | None = None,
        DefaultRouteSettings: dict[str, Any] | None = None,
        DeploymentId: str | None = None,
        Description: str | None = None,
        RouteSettings: dict[str, dict[str, Any]] | None = None,
        StageVariables: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_link(
        self,
        *,
        VpcLinkId: str,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
