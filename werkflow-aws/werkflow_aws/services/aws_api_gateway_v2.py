from werkflow_aws.models.api_gateway_v2 import (
    APIGatewayV2CreateApiMappingRequest,
    APIGatewayV2CreateApiMappingResponse,
    APIGatewayV2CreateApiRequest,
    APIGatewayV2CreateApiResponse,
    APIGatewayV2CreateAuthorizerRequest,
    APIGatewayV2CreateAuthorizerResponse,
    APIGatewayV2CreateDeploymentRequest,
    APIGatewayV2CreateDeploymentResponse,
    APIGatewayV2CreateDomainNameRequest,
    APIGatewayV2CreateDomainNameResponse,
    APIGatewayV2CreateIntegrationRequest,
    APIGatewayV2CreateIntegrationResponse,
    APIGatewayV2CreateIntegrationResponseRequest,
    APIGatewayV2CreateIntegrationResponseResponse,
    APIGatewayV2CreateModelRequest,
    APIGatewayV2CreateModelResponse,
    APIGatewayV2CreatePortalProductRequest,
    APIGatewayV2CreatePortalProductResponse,
    APIGatewayV2CreatePortalRequest,
    APIGatewayV2CreatePortalResponse,
    APIGatewayV2CreateProductPageRequest,
    APIGatewayV2CreateProductPageResponse,
    APIGatewayV2CreateProductRestEndpointPageRequest,
    APIGatewayV2CreateProductRestEndpointPageResponse,
    APIGatewayV2CreateRouteRequest,
    APIGatewayV2CreateRouteResponse,
    APIGatewayV2CreateRouteResponseRequest,
    APIGatewayV2CreateRouteResponseResponse,
    APIGatewayV2CreateRoutingRuleRequest,
    APIGatewayV2CreateRoutingRuleResponse,
    APIGatewayV2CreateStageRequest,
    APIGatewayV2CreateStageResponse,
    APIGatewayV2CreateVpcLinkRequest,
    APIGatewayV2CreateVpcLinkResponse,
    APIGatewayV2DeleteAccessLogSettingsRequest,
    APIGatewayV2DeleteAccessLogSettingsResponse,
    APIGatewayV2DeleteApiMappingRequest,
    APIGatewayV2DeleteApiMappingResponse,
    APIGatewayV2DeleteApiRequest,
    APIGatewayV2DeleteApiResponse,
    APIGatewayV2DeleteAuthorizerRequest,
    APIGatewayV2DeleteAuthorizerResponse,
    APIGatewayV2DeleteCorsConfigurationRequest,
    APIGatewayV2DeleteCorsConfigurationResponse,
    APIGatewayV2DeleteDeploymentRequest,
    APIGatewayV2DeleteDeploymentResponse,
    APIGatewayV2DeleteDomainNameRequest,
    APIGatewayV2DeleteDomainNameResponse,
    APIGatewayV2DeleteIntegrationRequest,
    APIGatewayV2DeleteIntegrationResponse,
    APIGatewayV2DeleteIntegrationResponseRequest,
    APIGatewayV2DeleteIntegrationResponseResponse,
    APIGatewayV2DeleteModelRequest,
    APIGatewayV2DeleteModelResponse,
    APIGatewayV2DeletePortalProductRequest,
    APIGatewayV2DeletePortalProductResponse,
    APIGatewayV2DeletePortalProductSharingPolicyRequest,
    APIGatewayV2DeletePortalProductSharingPolicyResponse,
    APIGatewayV2DeletePortalRequest,
    APIGatewayV2DeletePortalResponse,
    APIGatewayV2DeleteProductPageRequest,
    APIGatewayV2DeleteProductPageResponse,
    APIGatewayV2DeleteProductRestEndpointPageRequest,
    APIGatewayV2DeleteProductRestEndpointPageResponse,
    APIGatewayV2DeleteRouteRequest,
    APIGatewayV2DeleteRouteRequestParameterRequest,
    APIGatewayV2DeleteRouteRequestParameterResponse,
    APIGatewayV2DeleteRouteResponse,
    APIGatewayV2DeleteRouteResponseRequest,
    APIGatewayV2DeleteRouteResponseResponse,
    APIGatewayV2DeleteRouteSettingsRequest,
    APIGatewayV2DeleteRouteSettingsResponse,
    APIGatewayV2DeleteRoutingRuleRequest,
    APIGatewayV2DeleteRoutingRuleResponse,
    APIGatewayV2DeleteStageRequest,
    APIGatewayV2DeleteStageResponse,
    APIGatewayV2DeleteVpcLinkRequest,
    APIGatewayV2DeleteVpcLinkResponse,
    APIGatewayV2DisablePortalRequest,
    APIGatewayV2DisablePortalResponse,
    APIGatewayV2ExportApiRequest,
    APIGatewayV2ExportApiResponse,
    APIGatewayV2GetApiMappingRequest,
    APIGatewayV2GetApiMappingResponse,
    APIGatewayV2GetApiMappingsRequest,
    APIGatewayV2GetApiMappingsResponse,
    APIGatewayV2GetApiRequest,
    APIGatewayV2GetApiResponse,
    APIGatewayV2GetApisRequest,
    APIGatewayV2GetApisResponse,
    APIGatewayV2GetAuthorizerRequest,
    APIGatewayV2GetAuthorizerResponse,
    APIGatewayV2GetAuthorizersRequest,
    APIGatewayV2GetAuthorizersResponse,
    APIGatewayV2GetDeploymentRequest,
    APIGatewayV2GetDeploymentResponse,
    APIGatewayV2GetDeploymentsRequest,
    APIGatewayV2GetDeploymentsResponse,
    APIGatewayV2GetDomainNameRequest,
    APIGatewayV2GetDomainNameResponse,
    APIGatewayV2GetDomainNamesRequest,
    APIGatewayV2GetDomainNamesResponse,
    APIGatewayV2GetIntegrationRequest,
    APIGatewayV2GetIntegrationResponse,
    APIGatewayV2GetIntegrationResponseRequest,
    APIGatewayV2GetIntegrationResponseResponse,
    APIGatewayV2GetIntegrationResponsesRequest,
    APIGatewayV2GetIntegrationResponsesResponse,
    APIGatewayV2GetIntegrationsRequest,
    APIGatewayV2GetIntegrationsResponse,
    APIGatewayV2GetModelRequest,
    APIGatewayV2GetModelResponse,
    APIGatewayV2GetModelTemplateRequest,
    APIGatewayV2GetModelTemplateResponse,
    APIGatewayV2GetModelsRequest,
    APIGatewayV2GetModelsResponse,
    APIGatewayV2GetPortalProductRequest,
    APIGatewayV2GetPortalProductResponse,
    APIGatewayV2GetPortalProductSharingPolicyRequest,
    APIGatewayV2GetPortalProductSharingPolicyResponse,
    APIGatewayV2GetPortalRequest,
    APIGatewayV2GetPortalResponse,
    APIGatewayV2GetProductPageRequest,
    APIGatewayV2GetProductPageResponse,
    APIGatewayV2GetProductRestEndpointPageRequest,
    APIGatewayV2GetProductRestEndpointPageResponse,
    APIGatewayV2GetRouteRequest,
    APIGatewayV2GetRouteResponse,
    APIGatewayV2GetRouteResponseRequest,
    APIGatewayV2GetRouteResponseResponse,
    APIGatewayV2GetRouteResponsesRequest,
    APIGatewayV2GetRouteResponsesResponse,
    APIGatewayV2GetRoutesRequest,
    APIGatewayV2GetRoutesResponse,
    APIGatewayV2GetRoutingRuleRequest,
    APIGatewayV2GetRoutingRuleResponse,
    APIGatewayV2GetStageRequest,
    APIGatewayV2GetStageResponse,
    APIGatewayV2GetStagesRequest,
    APIGatewayV2GetStagesResponse,
    APIGatewayV2GetTagsRequest,
    APIGatewayV2GetTagsResponse,
    APIGatewayV2GetVpcLinkRequest,
    APIGatewayV2GetVpcLinkResponse,
    APIGatewayV2GetVpcLinksRequest,
    APIGatewayV2GetVpcLinksResponse,
    APIGatewayV2ImportApiRequest,
    APIGatewayV2ImportApiResponse,
    APIGatewayV2ListPortalProductsRequest,
    APIGatewayV2ListPortalProductsResponse,
    APIGatewayV2ListPortalsRequest,
    APIGatewayV2ListPortalsResponse,
    APIGatewayV2ListProductPagesRequest,
    APIGatewayV2ListProductPagesResponse,
    APIGatewayV2ListProductRestEndpointPagesRequest,
    APIGatewayV2ListProductRestEndpointPagesResponse,
    APIGatewayV2ListRoutingRulesRequest,
    APIGatewayV2ListRoutingRulesResponse,
    APIGatewayV2PreviewPortalRequest,
    APIGatewayV2PreviewPortalResponse,
    APIGatewayV2PublishPortalRequest,
    APIGatewayV2PublishPortalResponse,
    APIGatewayV2PutPortalProductSharingPolicyRequest,
    APIGatewayV2PutPortalProductSharingPolicyResponse,
    APIGatewayV2PutRoutingRuleRequest,
    APIGatewayV2PutRoutingRuleResponse,
    APIGatewayV2ReimportApiRequest,
    APIGatewayV2ReimportApiResponse,
    APIGatewayV2ResetAuthorizersCacheRequest,
    APIGatewayV2ResetAuthorizersCacheResponse,
    APIGatewayV2TagResourceRequest,
    APIGatewayV2TagResourceResponse,
    APIGatewayV2UntagResourceRequest,
    APIGatewayV2UntagResourceResponse,
    APIGatewayV2UpdateApiMappingRequest,
    APIGatewayV2UpdateApiMappingResponse,
    APIGatewayV2UpdateApiRequest,
    APIGatewayV2UpdateApiResponse,
    APIGatewayV2UpdateAuthorizerRequest,
    APIGatewayV2UpdateAuthorizerResponse,
    APIGatewayV2UpdateDeploymentRequest,
    APIGatewayV2UpdateDeploymentResponse,
    APIGatewayV2UpdateDomainNameRequest,
    APIGatewayV2UpdateDomainNameResponse,
    APIGatewayV2UpdateIntegrationRequest,
    APIGatewayV2UpdateIntegrationResponse,
    APIGatewayV2UpdateIntegrationResponseRequest,
    APIGatewayV2UpdateIntegrationResponseResponse,
    APIGatewayV2UpdateModelRequest,
    APIGatewayV2UpdateModelResponse,
    APIGatewayV2UpdatePortalProductRequest,
    APIGatewayV2UpdatePortalProductResponse,
    APIGatewayV2UpdatePortalRequest,
    APIGatewayV2UpdatePortalResponse,
    APIGatewayV2UpdateProductPageRequest,
    APIGatewayV2UpdateProductPageResponse,
    APIGatewayV2UpdateProductRestEndpointPageRequest,
    APIGatewayV2UpdateProductRestEndpointPageResponse,
    APIGatewayV2UpdateRouteRequest,
    APIGatewayV2UpdateRouteResponse,
    APIGatewayV2UpdateRouteResponseRequest,
    APIGatewayV2UpdateRouteResponseResponse,
    APIGatewayV2UpdateStageRequest,
    APIGatewayV2UpdateStageResponse,
    APIGatewayV2UpdateVpcLinkRequest,
    APIGatewayV2UpdateVpcLinkResponse,
)
from werkflow_aws.types.api_gateway_v2_client import APIGatewayV2Client
from .base import AWSBaseService


class AWSAPIGatewayV2(AWSBaseService[APIGatewayV2Client]):
    service_name = 'api-gateway-v2'
    boto3_service_name = 'apigatewayv2'

    def __init__(self) -> None:
        super().__init__(service_name='api-gateway-v2', boto3_service_name='apigatewayv2')

    async def create_api(
        self,
        request: APIGatewayV2CreateApiRequest,
    ) -> APIGatewayV2CreateApiResponse:
        client = self._require_client()
        return await self._execute(client.create_api, request, APIGatewayV2CreateApiResponse)

    async def create_api_mapping(
        self,
        request: APIGatewayV2CreateApiMappingRequest,
    ) -> APIGatewayV2CreateApiMappingResponse:
        client = self._require_client()
        return await self._execute(client.create_api_mapping, request, APIGatewayV2CreateApiMappingResponse)

    async def create_authorizer(
        self,
        request: APIGatewayV2CreateAuthorizerRequest,
    ) -> APIGatewayV2CreateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.create_authorizer, request, APIGatewayV2CreateAuthorizerResponse)

    async def create_deployment(
        self,
        request: APIGatewayV2CreateDeploymentRequest,
    ) -> APIGatewayV2CreateDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_deployment, request, APIGatewayV2CreateDeploymentResponse)

    async def create_domain_name(
        self,
        request: APIGatewayV2CreateDomainNameRequest,
    ) -> APIGatewayV2CreateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_name, request, APIGatewayV2CreateDomainNameResponse)

    async def create_integration(
        self,
        request: APIGatewayV2CreateIntegrationRequest,
    ) -> APIGatewayV2CreateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.create_integration, request, APIGatewayV2CreateIntegrationResponse)

    async def create_integration_response(
        self,
        request: APIGatewayV2CreateIntegrationResponseRequest,
    ) -> APIGatewayV2CreateIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.create_integration_response, request, APIGatewayV2CreateIntegrationResponseResponse)

    async def create_model(
        self,
        request: APIGatewayV2CreateModelRequest,
    ) -> APIGatewayV2CreateModelResponse:
        client = self._require_client()
        return await self._execute(client.create_model, request, APIGatewayV2CreateModelResponse)

    async def create_portal(
        self,
        request: APIGatewayV2CreatePortalRequest,
    ) -> APIGatewayV2CreatePortalResponse:
        client = self._require_client()
        return await self._execute(client.create_portal, request, APIGatewayV2CreatePortalResponse)

    async def create_portal_product(
        self,
        request: APIGatewayV2CreatePortalProductRequest,
    ) -> APIGatewayV2CreatePortalProductResponse:
        client = self._require_client()
        return await self._execute(client.create_portal_product, request, APIGatewayV2CreatePortalProductResponse)

    async def create_product_page(
        self,
        request: APIGatewayV2CreateProductPageRequest,
    ) -> APIGatewayV2CreateProductPageResponse:
        client = self._require_client()
        return await self._execute(client.create_product_page, request, APIGatewayV2CreateProductPageResponse)

    async def create_product_rest_endpoint_page(
        self,
        request: APIGatewayV2CreateProductRestEndpointPageRequest,
    ) -> APIGatewayV2CreateProductRestEndpointPageResponse:
        client = self._require_client()
        return await self._execute(client.create_product_rest_endpoint_page, request, APIGatewayV2CreateProductRestEndpointPageResponse)

    async def create_route(
        self,
        request: APIGatewayV2CreateRouteRequest,
    ) -> APIGatewayV2CreateRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_route, request, APIGatewayV2CreateRouteResponse)

    async def create_route_response(
        self,
        request: APIGatewayV2CreateRouteResponseRequest,
    ) -> APIGatewayV2CreateRouteResponseResponse:
        client = self._require_client()
        return await self._execute(client.create_route_response, request, APIGatewayV2CreateRouteResponseResponse)

    async def create_routing_rule(
        self,
        request: APIGatewayV2CreateRoutingRuleRequest,
    ) -> APIGatewayV2CreateRoutingRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_routing_rule, request, APIGatewayV2CreateRoutingRuleResponse)

    async def create_stage(
        self,
        request: APIGatewayV2CreateStageRequest,
    ) -> APIGatewayV2CreateStageResponse:
        client = self._require_client()
        return await self._execute(client.create_stage, request, APIGatewayV2CreateStageResponse)

    async def create_vpc_link(
        self,
        request: APIGatewayV2CreateVpcLinkRequest,
    ) -> APIGatewayV2CreateVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_link, request, APIGatewayV2CreateVpcLinkResponse)

    async def delete_access_log_settings(
        self,
        request: APIGatewayV2DeleteAccessLogSettingsRequest,
    ) -> APIGatewayV2DeleteAccessLogSettingsResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_log_settings, request, APIGatewayV2DeleteAccessLogSettingsResponse)

    async def delete_api(
        self,
        request: APIGatewayV2DeleteApiRequest,
    ) -> APIGatewayV2DeleteApiResponse:
        client = self._require_client()
        return await self._execute(client.delete_api, request, APIGatewayV2DeleteApiResponse)

    async def delete_api_mapping(
        self,
        request: APIGatewayV2DeleteApiMappingRequest,
    ) -> APIGatewayV2DeleteApiMappingResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_mapping, request, APIGatewayV2DeleteApiMappingResponse)

    async def delete_authorizer(
        self,
        request: APIGatewayV2DeleteAuthorizerRequest,
    ) -> APIGatewayV2DeleteAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.delete_authorizer, request, APIGatewayV2DeleteAuthorizerResponse)

    async def delete_cors_configuration(
        self,
        request: APIGatewayV2DeleteCorsConfigurationRequest,
    ) -> APIGatewayV2DeleteCorsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_cors_configuration, request, APIGatewayV2DeleteCorsConfigurationResponse)

    async def delete_deployment(
        self,
        request: APIGatewayV2DeleteDeploymentRequest,
    ) -> APIGatewayV2DeleteDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.delete_deployment, request, APIGatewayV2DeleteDeploymentResponse)

    async def delete_domain_name(
        self,
        request: APIGatewayV2DeleteDomainNameRequest,
    ) -> APIGatewayV2DeleteDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_name, request, APIGatewayV2DeleteDomainNameResponse)

    async def delete_integration(
        self,
        request: APIGatewayV2DeleteIntegrationRequest,
    ) -> APIGatewayV2DeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, APIGatewayV2DeleteIntegrationResponse)

    async def delete_integration_response(
        self,
        request: APIGatewayV2DeleteIntegrationResponseRequest,
    ) -> APIGatewayV2DeleteIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration_response, request, APIGatewayV2DeleteIntegrationResponseResponse)

    async def delete_model(
        self,
        request: APIGatewayV2DeleteModelRequest,
    ) -> APIGatewayV2DeleteModelResponse:
        client = self._require_client()
        return await self._execute(client.delete_model, request, APIGatewayV2DeleteModelResponse)

    async def delete_portal(
        self,
        request: APIGatewayV2DeletePortalRequest,
    ) -> APIGatewayV2DeletePortalResponse:
        client = self._require_client()
        return await self._execute(client.delete_portal, request, APIGatewayV2DeletePortalResponse)

    async def delete_portal_product(
        self,
        request: APIGatewayV2DeletePortalProductRequest,
    ) -> APIGatewayV2DeletePortalProductResponse:
        client = self._require_client()
        return await self._execute(client.delete_portal_product, request, APIGatewayV2DeletePortalProductResponse)

    async def delete_portal_product_sharing_policy(
        self,
        request: APIGatewayV2DeletePortalProductSharingPolicyRequest,
    ) -> APIGatewayV2DeletePortalProductSharingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_portal_product_sharing_policy, request, APIGatewayV2DeletePortalProductSharingPolicyResponse)

    async def delete_product_page(
        self,
        request: APIGatewayV2DeleteProductPageRequest,
    ) -> APIGatewayV2DeleteProductPageResponse:
        client = self._require_client()
        return await self._execute(client.delete_product_page, request, APIGatewayV2DeleteProductPageResponse)

    async def delete_product_rest_endpoint_page(
        self,
        request: APIGatewayV2DeleteProductRestEndpointPageRequest,
    ) -> APIGatewayV2DeleteProductRestEndpointPageResponse:
        client = self._require_client()
        return await self._execute(client.delete_product_rest_endpoint_page, request, APIGatewayV2DeleteProductRestEndpointPageResponse)

    async def delete_route(
        self,
        request: APIGatewayV2DeleteRouteRequest,
    ) -> APIGatewayV2DeleteRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_route, request, APIGatewayV2DeleteRouteResponse)

    async def delete_route_request_parameter(
        self,
        request: APIGatewayV2DeleteRouteRequestParameterRequest,
    ) -> APIGatewayV2DeleteRouteRequestParameterResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_request_parameter, request, APIGatewayV2DeleteRouteRequestParameterResponse)

    async def delete_route_response(
        self,
        request: APIGatewayV2DeleteRouteResponseRequest,
    ) -> APIGatewayV2DeleteRouteResponseResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_response, request, APIGatewayV2DeleteRouteResponseResponse)

    async def delete_route_settings(
        self,
        request: APIGatewayV2DeleteRouteSettingsRequest,
    ) -> APIGatewayV2DeleteRouteSettingsResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_settings, request, APIGatewayV2DeleteRouteSettingsResponse)

    async def delete_routing_rule(
        self,
        request: APIGatewayV2DeleteRoutingRuleRequest,
    ) -> APIGatewayV2DeleteRoutingRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_routing_rule, request, APIGatewayV2DeleteRoutingRuleResponse)

    async def delete_stage(
        self,
        request: APIGatewayV2DeleteStageRequest,
    ) -> APIGatewayV2DeleteStageResponse:
        client = self._require_client()
        return await self._execute(client.delete_stage, request, APIGatewayV2DeleteStageResponse)

    async def delete_vpc_link(
        self,
        request: APIGatewayV2DeleteVpcLinkRequest,
    ) -> APIGatewayV2DeleteVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_link, request, APIGatewayV2DeleteVpcLinkResponse)

    async def disable_portal(
        self,
        request: APIGatewayV2DisablePortalRequest,
    ) -> APIGatewayV2DisablePortalResponse:
        client = self._require_client()
        return await self._execute(client.disable_portal, request, APIGatewayV2DisablePortalResponse)

    async def export_api(
        self,
        request: APIGatewayV2ExportApiRequest,
    ) -> APIGatewayV2ExportApiResponse:
        client = self._require_client()
        return await self._execute(client.export_api, request, APIGatewayV2ExportApiResponse)

    async def get_api(
        self,
        request: APIGatewayV2GetApiRequest,
    ) -> APIGatewayV2GetApiResponse:
        client = self._require_client()
        return await self._execute(client.get_api, request, APIGatewayV2GetApiResponse)

    async def get_api_mapping(
        self,
        request: APIGatewayV2GetApiMappingRequest,
    ) -> APIGatewayV2GetApiMappingResponse:
        client = self._require_client()
        return await self._execute(client.get_api_mapping, request, APIGatewayV2GetApiMappingResponse)

    async def get_api_mappings(
        self,
        request: APIGatewayV2GetApiMappingsRequest,
    ) -> APIGatewayV2GetApiMappingsResponse:
        client = self._require_client()
        return await self._execute(client.get_api_mappings, request, APIGatewayV2GetApiMappingsResponse)

    async def get_apis(
        self,
        request: APIGatewayV2GetApisRequest | None = None,
    ) -> APIGatewayV2GetApisResponse:
        client = self._require_client()
        return await self._execute(client.get_apis, request, APIGatewayV2GetApisResponse)

    async def get_apis_paginated(
        self,
        request: APIGatewayV2GetApisRequest | None = None,
    ) -> list[APIGatewayV2GetApisResponse]:
        return await self._paginate('get_apis', request, APIGatewayV2GetApisResponse)

    async def get_authorizer(
        self,
        request: APIGatewayV2GetAuthorizerRequest,
    ) -> APIGatewayV2GetAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.get_authorizer, request, APIGatewayV2GetAuthorizerResponse)

    async def get_authorizers(
        self,
        request: APIGatewayV2GetAuthorizersRequest,
    ) -> APIGatewayV2GetAuthorizersResponse:
        client = self._require_client()
        return await self._execute(client.get_authorizers, request, APIGatewayV2GetAuthorizersResponse)

    async def get_authorizers_paginated(
        self,
        request: APIGatewayV2GetAuthorizersRequest,
    ) -> list[APIGatewayV2GetAuthorizersResponse]:
        return await self._paginate('get_authorizers', request, APIGatewayV2GetAuthorizersResponse)

    async def get_deployment(
        self,
        request: APIGatewayV2GetDeploymentRequest,
    ) -> APIGatewayV2GetDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.get_deployment, request, APIGatewayV2GetDeploymentResponse)

    async def get_deployments(
        self,
        request: APIGatewayV2GetDeploymentsRequest,
    ) -> APIGatewayV2GetDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.get_deployments, request, APIGatewayV2GetDeploymentsResponse)

    async def get_deployments_paginated(
        self,
        request: APIGatewayV2GetDeploymentsRequest,
    ) -> list[APIGatewayV2GetDeploymentsResponse]:
        return await self._paginate('get_deployments', request, APIGatewayV2GetDeploymentsResponse)

    async def get_domain_name(
        self,
        request: APIGatewayV2GetDomainNameRequest,
    ) -> APIGatewayV2GetDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_name, request, APIGatewayV2GetDomainNameResponse)

    async def get_domain_names(
        self,
        request: APIGatewayV2GetDomainNamesRequest | None = None,
    ) -> APIGatewayV2GetDomainNamesResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_names, request, APIGatewayV2GetDomainNamesResponse)

    async def get_domain_names_paginated(
        self,
        request: APIGatewayV2GetDomainNamesRequest | None = None,
    ) -> list[APIGatewayV2GetDomainNamesResponse]:
        return await self._paginate('get_domain_names', request, APIGatewayV2GetDomainNamesResponse)

    async def get_integration(
        self,
        request: APIGatewayV2GetIntegrationRequest,
    ) -> APIGatewayV2GetIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.get_integration, request, APIGatewayV2GetIntegrationResponse)

    async def get_integration_response(
        self,
        request: APIGatewayV2GetIntegrationResponseRequest,
    ) -> APIGatewayV2GetIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.get_integration_response, request, APIGatewayV2GetIntegrationResponseResponse)

    async def get_integration_responses(
        self,
        request: APIGatewayV2GetIntegrationResponsesRequest,
    ) -> APIGatewayV2GetIntegrationResponsesResponse:
        client = self._require_client()
        return await self._execute(client.get_integration_responses, request, APIGatewayV2GetIntegrationResponsesResponse)

    async def get_integration_responses_paginated(
        self,
        request: APIGatewayV2GetIntegrationResponsesRequest,
    ) -> list[APIGatewayV2GetIntegrationResponsesResponse]:
        return await self._paginate('get_integration_responses', request, APIGatewayV2GetIntegrationResponsesResponse)

    async def get_integrations(
        self,
        request: APIGatewayV2GetIntegrationsRequest,
    ) -> APIGatewayV2GetIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.get_integrations, request, APIGatewayV2GetIntegrationsResponse)

    async def get_integrations_paginated(
        self,
        request: APIGatewayV2GetIntegrationsRequest,
    ) -> list[APIGatewayV2GetIntegrationsResponse]:
        return await self._paginate('get_integrations', request, APIGatewayV2GetIntegrationsResponse)

    async def get_model(
        self,
        request: APIGatewayV2GetModelRequest,
    ) -> APIGatewayV2GetModelResponse:
        client = self._require_client()
        return await self._execute(client.get_model, request, APIGatewayV2GetModelResponse)

    async def get_model_template(
        self,
        request: APIGatewayV2GetModelTemplateRequest,
    ) -> APIGatewayV2GetModelTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_model_template, request, APIGatewayV2GetModelTemplateResponse)

    async def get_models(
        self,
        request: APIGatewayV2GetModelsRequest,
    ) -> APIGatewayV2GetModelsResponse:
        client = self._require_client()
        return await self._execute(client.get_models, request, APIGatewayV2GetModelsResponse)

    async def get_models_paginated(
        self,
        request: APIGatewayV2GetModelsRequest,
    ) -> list[APIGatewayV2GetModelsResponse]:
        return await self._paginate('get_models', request, APIGatewayV2GetModelsResponse)

    async def get_portal(
        self,
        request: APIGatewayV2GetPortalRequest,
    ) -> APIGatewayV2GetPortalResponse:
        client = self._require_client()
        return await self._execute(client.get_portal, request, APIGatewayV2GetPortalResponse)

    async def get_portal_product(
        self,
        request: APIGatewayV2GetPortalProductRequest,
    ) -> APIGatewayV2GetPortalProductResponse:
        client = self._require_client()
        return await self._execute(client.get_portal_product, request, APIGatewayV2GetPortalProductResponse)

    async def get_portal_product_sharing_policy(
        self,
        request: APIGatewayV2GetPortalProductSharingPolicyRequest,
    ) -> APIGatewayV2GetPortalProductSharingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_portal_product_sharing_policy, request, APIGatewayV2GetPortalProductSharingPolicyResponse)

    async def get_product_page(
        self,
        request: APIGatewayV2GetProductPageRequest,
    ) -> APIGatewayV2GetProductPageResponse:
        client = self._require_client()
        return await self._execute(client.get_product_page, request, APIGatewayV2GetProductPageResponse)

    async def get_product_rest_endpoint_page(
        self,
        request: APIGatewayV2GetProductRestEndpointPageRequest,
    ) -> APIGatewayV2GetProductRestEndpointPageResponse:
        client = self._require_client()
        return await self._execute(client.get_product_rest_endpoint_page, request, APIGatewayV2GetProductRestEndpointPageResponse)

    async def get_route(
        self,
        request: APIGatewayV2GetRouteRequest,
    ) -> APIGatewayV2GetRouteResponse:
        client = self._require_client()
        return await self._execute(client.get_route, request, APIGatewayV2GetRouteResponse)

    async def get_route_response(
        self,
        request: APIGatewayV2GetRouteResponseRequest,
    ) -> APIGatewayV2GetRouteResponseResponse:
        client = self._require_client()
        return await self._execute(client.get_route_response, request, APIGatewayV2GetRouteResponseResponse)

    async def get_route_responses(
        self,
        request: APIGatewayV2GetRouteResponsesRequest,
    ) -> APIGatewayV2GetRouteResponsesResponse:
        client = self._require_client()
        return await self._execute(client.get_route_responses, request, APIGatewayV2GetRouteResponsesResponse)

    async def get_route_responses_paginated(
        self,
        request: APIGatewayV2GetRouteResponsesRequest,
    ) -> list[APIGatewayV2GetRouteResponsesResponse]:
        return await self._paginate('get_route_responses', request, APIGatewayV2GetRouteResponsesResponse)

    async def get_routes(
        self,
        request: APIGatewayV2GetRoutesRequest,
    ) -> APIGatewayV2GetRoutesResponse:
        client = self._require_client()
        return await self._execute(client.get_routes, request, APIGatewayV2GetRoutesResponse)

    async def get_routes_paginated(
        self,
        request: APIGatewayV2GetRoutesRequest,
    ) -> list[APIGatewayV2GetRoutesResponse]:
        return await self._paginate('get_routes', request, APIGatewayV2GetRoutesResponse)

    async def get_routing_rule(
        self,
        request: APIGatewayV2GetRoutingRuleRequest,
    ) -> APIGatewayV2GetRoutingRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_routing_rule, request, APIGatewayV2GetRoutingRuleResponse)

    async def get_stage(
        self,
        request: APIGatewayV2GetStageRequest,
    ) -> APIGatewayV2GetStageResponse:
        client = self._require_client()
        return await self._execute(client.get_stage, request, APIGatewayV2GetStageResponse)

    async def get_stages(
        self,
        request: APIGatewayV2GetStagesRequest,
    ) -> APIGatewayV2GetStagesResponse:
        client = self._require_client()
        return await self._execute(client.get_stages, request, APIGatewayV2GetStagesResponse)

    async def get_stages_paginated(
        self,
        request: APIGatewayV2GetStagesRequest,
    ) -> list[APIGatewayV2GetStagesResponse]:
        return await self._paginate('get_stages', request, APIGatewayV2GetStagesResponse)

    async def get_tags(
        self,
        request: APIGatewayV2GetTagsRequest,
    ) -> APIGatewayV2GetTagsResponse:
        client = self._require_client()
        return await self._execute(client.get_tags, request, APIGatewayV2GetTagsResponse)

    async def get_vpc_link(
        self,
        request: APIGatewayV2GetVpcLinkRequest,
    ) -> APIGatewayV2GetVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_link, request, APIGatewayV2GetVpcLinkResponse)

    async def get_vpc_links(
        self,
        request: APIGatewayV2GetVpcLinksRequest | None = None,
    ) -> APIGatewayV2GetVpcLinksResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_links, request, APIGatewayV2GetVpcLinksResponse)

    async def import_api(
        self,
        request: APIGatewayV2ImportApiRequest,
    ) -> APIGatewayV2ImportApiResponse:
        client = self._require_client()
        return await self._execute(client.import_api, request, APIGatewayV2ImportApiResponse)

    async def list_portal_products(
        self,
        request: APIGatewayV2ListPortalProductsRequest | None = None,
    ) -> APIGatewayV2ListPortalProductsResponse:
        client = self._require_client()
        return await self._execute(client.list_portal_products, request, APIGatewayV2ListPortalProductsResponse)

    async def list_portal_products_paginated(
        self,
        request: APIGatewayV2ListPortalProductsRequest | None = None,
    ) -> list[APIGatewayV2ListPortalProductsResponse]:
        return await self._paginate('list_portal_products', request, APIGatewayV2ListPortalProductsResponse)

    async def list_portals(
        self,
        request: APIGatewayV2ListPortalsRequest | None = None,
    ) -> APIGatewayV2ListPortalsResponse:
        client = self._require_client()
        return await self._execute(client.list_portals, request, APIGatewayV2ListPortalsResponse)

    async def list_portals_paginated(
        self,
        request: APIGatewayV2ListPortalsRequest | None = None,
    ) -> list[APIGatewayV2ListPortalsResponse]:
        return await self._paginate('list_portals', request, APIGatewayV2ListPortalsResponse)

    async def list_product_pages(
        self,
        request: APIGatewayV2ListProductPagesRequest,
    ) -> APIGatewayV2ListProductPagesResponse:
        client = self._require_client()
        return await self._execute(client.list_product_pages, request, APIGatewayV2ListProductPagesResponse)

    async def list_product_pages_paginated(
        self,
        request: APIGatewayV2ListProductPagesRequest,
    ) -> list[APIGatewayV2ListProductPagesResponse]:
        return await self._paginate('list_product_pages', request, APIGatewayV2ListProductPagesResponse)

    async def list_product_rest_endpoint_pages(
        self,
        request: APIGatewayV2ListProductRestEndpointPagesRequest,
    ) -> APIGatewayV2ListProductRestEndpointPagesResponse:
        client = self._require_client()
        return await self._execute(client.list_product_rest_endpoint_pages, request, APIGatewayV2ListProductRestEndpointPagesResponse)

    async def list_product_rest_endpoint_pages_paginated(
        self,
        request: APIGatewayV2ListProductRestEndpointPagesRequest,
    ) -> list[APIGatewayV2ListProductRestEndpointPagesResponse]:
        return await self._paginate('list_product_rest_endpoint_pages', request, APIGatewayV2ListProductRestEndpointPagesResponse)

    async def list_routing_rules(
        self,
        request: APIGatewayV2ListRoutingRulesRequest,
    ) -> APIGatewayV2ListRoutingRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_routing_rules, request, APIGatewayV2ListRoutingRulesResponse)

    async def list_routing_rules_paginated(
        self,
        request: APIGatewayV2ListRoutingRulesRequest,
    ) -> list[APIGatewayV2ListRoutingRulesResponse]:
        return await self._paginate('list_routing_rules', request, APIGatewayV2ListRoutingRulesResponse)

    async def preview_portal(
        self,
        request: APIGatewayV2PreviewPortalRequest,
    ) -> APIGatewayV2PreviewPortalResponse:
        client = self._require_client()
        return await self._execute(client.preview_portal, request, APIGatewayV2PreviewPortalResponse)

    async def publish_portal(
        self,
        request: APIGatewayV2PublishPortalRequest,
    ) -> APIGatewayV2PublishPortalResponse:
        client = self._require_client()
        return await self._execute(client.publish_portal, request, APIGatewayV2PublishPortalResponse)

    async def put_portal_product_sharing_policy(
        self,
        request: APIGatewayV2PutPortalProductSharingPolicyRequest,
    ) -> APIGatewayV2PutPortalProductSharingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_portal_product_sharing_policy, request, APIGatewayV2PutPortalProductSharingPolicyResponse)

    async def put_routing_rule(
        self,
        request: APIGatewayV2PutRoutingRuleRequest,
    ) -> APIGatewayV2PutRoutingRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_routing_rule, request, APIGatewayV2PutRoutingRuleResponse)

    async def reimport_api(
        self,
        request: APIGatewayV2ReimportApiRequest,
    ) -> APIGatewayV2ReimportApiResponse:
        client = self._require_client()
        return await self._execute(client.reimport_api, request, APIGatewayV2ReimportApiResponse)

    async def reset_authorizers_cache(
        self,
        request: APIGatewayV2ResetAuthorizersCacheRequest,
    ) -> APIGatewayV2ResetAuthorizersCacheResponse:
        client = self._require_client()
        return await self._execute(client.reset_authorizers_cache, request, APIGatewayV2ResetAuthorizersCacheResponse)

    async def tag_resource(
        self,
        request: APIGatewayV2TagResourceRequest,
    ) -> APIGatewayV2TagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, APIGatewayV2TagResourceResponse)

    async def untag_resource(
        self,
        request: APIGatewayV2UntagResourceRequest,
    ) -> APIGatewayV2UntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, APIGatewayV2UntagResourceResponse)

    async def update_api(
        self,
        request: APIGatewayV2UpdateApiRequest,
    ) -> APIGatewayV2UpdateApiResponse:
        client = self._require_client()
        return await self._execute(client.update_api, request, APIGatewayV2UpdateApiResponse)

    async def update_api_mapping(
        self,
        request: APIGatewayV2UpdateApiMappingRequest,
    ) -> APIGatewayV2UpdateApiMappingResponse:
        client = self._require_client()
        return await self._execute(client.update_api_mapping, request, APIGatewayV2UpdateApiMappingResponse)

    async def update_authorizer(
        self,
        request: APIGatewayV2UpdateAuthorizerRequest,
    ) -> APIGatewayV2UpdateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.update_authorizer, request, APIGatewayV2UpdateAuthorizerResponse)

    async def update_deployment(
        self,
        request: APIGatewayV2UpdateDeploymentRequest,
    ) -> APIGatewayV2UpdateDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.update_deployment, request, APIGatewayV2UpdateDeploymentResponse)

    async def update_domain_name(
        self,
        request: APIGatewayV2UpdateDomainNameRequest,
    ) -> APIGatewayV2UpdateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_name, request, APIGatewayV2UpdateDomainNameResponse)

    async def update_integration(
        self,
        request: APIGatewayV2UpdateIntegrationRequest,
    ) -> APIGatewayV2UpdateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.update_integration, request, APIGatewayV2UpdateIntegrationResponse)

    async def update_integration_response(
        self,
        request: APIGatewayV2UpdateIntegrationResponseRequest,
    ) -> APIGatewayV2UpdateIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.update_integration_response, request, APIGatewayV2UpdateIntegrationResponseResponse)

    async def update_model(
        self,
        request: APIGatewayV2UpdateModelRequest,
    ) -> APIGatewayV2UpdateModelResponse:
        client = self._require_client()
        return await self._execute(client.update_model, request, APIGatewayV2UpdateModelResponse)

    async def update_portal(
        self,
        request: APIGatewayV2UpdatePortalRequest,
    ) -> APIGatewayV2UpdatePortalResponse:
        client = self._require_client()
        return await self._execute(client.update_portal, request, APIGatewayV2UpdatePortalResponse)

    async def update_portal_product(
        self,
        request: APIGatewayV2UpdatePortalProductRequest,
    ) -> APIGatewayV2UpdatePortalProductResponse:
        client = self._require_client()
        return await self._execute(client.update_portal_product, request, APIGatewayV2UpdatePortalProductResponse)

    async def update_product_page(
        self,
        request: APIGatewayV2UpdateProductPageRequest,
    ) -> APIGatewayV2UpdateProductPageResponse:
        client = self._require_client()
        return await self._execute(client.update_product_page, request, APIGatewayV2UpdateProductPageResponse)

    async def update_product_rest_endpoint_page(
        self,
        request: APIGatewayV2UpdateProductRestEndpointPageRequest,
    ) -> APIGatewayV2UpdateProductRestEndpointPageResponse:
        client = self._require_client()
        return await self._execute(client.update_product_rest_endpoint_page, request, APIGatewayV2UpdateProductRestEndpointPageResponse)

    async def update_route(
        self,
        request: APIGatewayV2UpdateRouteRequest,
    ) -> APIGatewayV2UpdateRouteResponse:
        client = self._require_client()
        return await self._execute(client.update_route, request, APIGatewayV2UpdateRouteResponse)

    async def update_route_response(
        self,
        request: APIGatewayV2UpdateRouteResponseRequest,
    ) -> APIGatewayV2UpdateRouteResponseResponse:
        client = self._require_client()
        return await self._execute(client.update_route_response, request, APIGatewayV2UpdateRouteResponseResponse)

    async def update_stage(
        self,
        request: APIGatewayV2UpdateStageRequest,
    ) -> APIGatewayV2UpdateStageResponse:
        client = self._require_client()
        return await self._execute(client.update_stage, request, APIGatewayV2UpdateStageResponse)

    async def update_vpc_link(
        self,
        request: APIGatewayV2UpdateVpcLinkRequest,
    ) -> APIGatewayV2UpdateVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_link, request, APIGatewayV2UpdateVpcLinkResponse)
