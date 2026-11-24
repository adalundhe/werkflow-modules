from werkflow_aws.models.api_gateway import (
    APIGatewayCreateApiKeyRequest,
    APIGatewayCreateApiKeyResponse,
    APIGatewayCreateAuthorizerRequest,
    APIGatewayCreateAuthorizerResponse,
    APIGatewayCreateBasePathMappingRequest,
    APIGatewayCreateBasePathMappingResponse,
    APIGatewayCreateDeploymentRequest,
    APIGatewayCreateDeploymentResponse,
    APIGatewayCreateDocumentationPartRequest,
    APIGatewayCreateDocumentationPartResponse,
    APIGatewayCreateDocumentationVersionRequest,
    APIGatewayCreateDocumentationVersionResponse,
    APIGatewayCreateDomainNameAccessAssociationRequest,
    APIGatewayCreateDomainNameAccessAssociationResponse,
    APIGatewayCreateDomainNameRequest,
    APIGatewayCreateDomainNameResponse,
    APIGatewayCreateModelRequest,
    APIGatewayCreateModelResponse,
    APIGatewayCreateRequestValidatorRequest,
    APIGatewayCreateRequestValidatorResponse,
    APIGatewayCreateResourceRequest,
    APIGatewayCreateResourceResponse,
    APIGatewayCreateRestApiRequest,
    APIGatewayCreateRestApiResponse,
    APIGatewayCreateStageRequest,
    APIGatewayCreateStageResponse,
    APIGatewayCreateUsagePlanKeyRequest,
    APIGatewayCreateUsagePlanKeyResponse,
    APIGatewayCreateUsagePlanRequest,
    APIGatewayCreateUsagePlanResponse,
    APIGatewayCreateVpcLinkRequest,
    APIGatewayCreateVpcLinkResponse,
    APIGatewayDeleteApiKeyRequest,
    APIGatewayDeleteApiKeyResponse,
    APIGatewayDeleteAuthorizerRequest,
    APIGatewayDeleteAuthorizerResponse,
    APIGatewayDeleteBasePathMappingRequest,
    APIGatewayDeleteBasePathMappingResponse,
    APIGatewayDeleteClientCertificateRequest,
    APIGatewayDeleteClientCertificateResponse,
    APIGatewayDeleteDeploymentRequest,
    APIGatewayDeleteDeploymentResponse,
    APIGatewayDeleteDocumentationPartRequest,
    APIGatewayDeleteDocumentationPartResponse,
    APIGatewayDeleteDocumentationVersionRequest,
    APIGatewayDeleteDocumentationVersionResponse,
    APIGatewayDeleteDomainNameAccessAssociationRequest,
    APIGatewayDeleteDomainNameAccessAssociationResponse,
    APIGatewayDeleteDomainNameRequest,
    APIGatewayDeleteDomainNameResponse,
    APIGatewayDeleteGatewayResponseRequest,
    APIGatewayDeleteGatewayResponseResponse,
    APIGatewayDeleteIntegrationRequest,
    APIGatewayDeleteIntegrationResponse,
    APIGatewayDeleteIntegrationResponseRequest,
    APIGatewayDeleteIntegrationResponseResponse,
    APIGatewayDeleteMethodRequest,
    APIGatewayDeleteMethodResponse,
    APIGatewayDeleteMethodResponseRequest,
    APIGatewayDeleteMethodResponseResponse,
    APIGatewayDeleteModelRequest,
    APIGatewayDeleteModelResponse,
    APIGatewayDeleteRequestValidatorRequest,
    APIGatewayDeleteRequestValidatorResponse,
    APIGatewayDeleteResourceRequest,
    APIGatewayDeleteResourceResponse,
    APIGatewayDeleteRestApiRequest,
    APIGatewayDeleteRestApiResponse,
    APIGatewayDeleteStageRequest,
    APIGatewayDeleteStageResponse,
    APIGatewayDeleteUsagePlanKeyRequest,
    APIGatewayDeleteUsagePlanKeyResponse,
    APIGatewayDeleteUsagePlanRequest,
    APIGatewayDeleteUsagePlanResponse,
    APIGatewayDeleteVpcLinkRequest,
    APIGatewayDeleteVpcLinkResponse,
    APIGatewayFlushStageAuthorizersCacheRequest,
    APIGatewayFlushStageAuthorizersCacheResponse,
    APIGatewayFlushStageCacheRequest,
    APIGatewayFlushStageCacheResponse,
    APIGatewayGenerateClientCertificateRequest,
    APIGatewayGenerateClientCertificateResponse,
    APIGatewayGetAccountRequest,
    APIGatewayGetAccountResponse,
    APIGatewayGetApiKeyRequest,
    APIGatewayGetApiKeyResponse,
    APIGatewayGetApiKeysRequest,
    APIGatewayGetApiKeysResponse,
    APIGatewayGetAuthorizerRequest,
    APIGatewayGetAuthorizerResponse,
    APIGatewayGetAuthorizersRequest,
    APIGatewayGetAuthorizersResponse,
    APIGatewayGetBasePathMappingRequest,
    APIGatewayGetBasePathMappingResponse,
    APIGatewayGetBasePathMappingsRequest,
    APIGatewayGetBasePathMappingsResponse,
    APIGatewayGetClientCertificateRequest,
    APIGatewayGetClientCertificateResponse,
    APIGatewayGetClientCertificatesRequest,
    APIGatewayGetClientCertificatesResponse,
    APIGatewayGetDeploymentRequest,
    APIGatewayGetDeploymentResponse,
    APIGatewayGetDeploymentsRequest,
    APIGatewayGetDeploymentsResponse,
    APIGatewayGetDocumentationPartRequest,
    APIGatewayGetDocumentationPartResponse,
    APIGatewayGetDocumentationPartsRequest,
    APIGatewayGetDocumentationPartsResponse,
    APIGatewayGetDocumentationVersionRequest,
    APIGatewayGetDocumentationVersionResponse,
    APIGatewayGetDocumentationVersionsRequest,
    APIGatewayGetDocumentationVersionsResponse,
    APIGatewayGetDomainNameAccessAssociationsRequest,
    APIGatewayGetDomainNameAccessAssociationsResponse,
    APIGatewayGetDomainNameRequest,
    APIGatewayGetDomainNameResponse,
    APIGatewayGetDomainNamesRequest,
    APIGatewayGetDomainNamesResponse,
    APIGatewayGetExportRequest,
    APIGatewayGetExportResponse,
    APIGatewayGetGatewayResponseRequest,
    APIGatewayGetGatewayResponseResponse,
    APIGatewayGetGatewayResponsesRequest,
    APIGatewayGetGatewayResponsesResponse,
    APIGatewayGetIntegrationRequest,
    APIGatewayGetIntegrationResponse,
    APIGatewayGetIntegrationResponseRequest,
    APIGatewayGetIntegrationResponseResponse,
    APIGatewayGetMethodRequest,
    APIGatewayGetMethodResponse,
    APIGatewayGetMethodResponseRequest,
    APIGatewayGetMethodResponseResponse,
    APIGatewayGetModelRequest,
    APIGatewayGetModelResponse,
    APIGatewayGetModelTemplateRequest,
    APIGatewayGetModelTemplateResponse,
    APIGatewayGetModelsRequest,
    APIGatewayGetModelsResponse,
    APIGatewayGetRequestValidatorRequest,
    APIGatewayGetRequestValidatorResponse,
    APIGatewayGetRequestValidatorsRequest,
    APIGatewayGetRequestValidatorsResponse,
    APIGatewayGetResourceRequest,
    APIGatewayGetResourceResponse,
    APIGatewayGetResourcesRequest,
    APIGatewayGetResourcesResponse,
    APIGatewayGetRestApiRequest,
    APIGatewayGetRestApiResponse,
    APIGatewayGetRestApisRequest,
    APIGatewayGetRestApisResponse,
    APIGatewayGetSdkRequest,
    APIGatewayGetSdkResponse,
    APIGatewayGetSdkTypeRequest,
    APIGatewayGetSdkTypeResponse,
    APIGatewayGetSdkTypesRequest,
    APIGatewayGetSdkTypesResponse,
    APIGatewayGetStageRequest,
    APIGatewayGetStageResponse,
    APIGatewayGetStagesRequest,
    APIGatewayGetStagesResponse,
    APIGatewayGetTagsRequest,
    APIGatewayGetTagsResponse,
    APIGatewayGetUsagePlanKeyRequest,
    APIGatewayGetUsagePlanKeyResponse,
    APIGatewayGetUsagePlanKeysRequest,
    APIGatewayGetUsagePlanKeysResponse,
    APIGatewayGetUsagePlanRequest,
    APIGatewayGetUsagePlanResponse,
    APIGatewayGetUsagePlansRequest,
    APIGatewayGetUsagePlansResponse,
    APIGatewayGetUsageRequest,
    APIGatewayGetUsageResponse,
    APIGatewayGetVpcLinkRequest,
    APIGatewayGetVpcLinkResponse,
    APIGatewayGetVpcLinksRequest,
    APIGatewayGetVpcLinksResponse,
    APIGatewayImportApiKeysRequest,
    APIGatewayImportApiKeysResponse,
    APIGatewayImportDocumentationPartsRequest,
    APIGatewayImportDocumentationPartsResponse,
    APIGatewayImportRestApiRequest,
    APIGatewayImportRestApiResponse,
    APIGatewayPutGatewayResponseRequest,
    APIGatewayPutGatewayResponseResponse,
    APIGatewayPutIntegrationRequest,
    APIGatewayPutIntegrationResponse,
    APIGatewayPutIntegrationResponseRequest,
    APIGatewayPutIntegrationResponseResponse,
    APIGatewayPutMethodRequest,
    APIGatewayPutMethodResponse,
    APIGatewayPutMethodResponseRequest,
    APIGatewayPutMethodResponseResponse,
    APIGatewayPutRestApiRequest,
    APIGatewayPutRestApiResponse,
    APIGatewayRejectDomainNameAccessAssociationRequest,
    APIGatewayRejectDomainNameAccessAssociationResponse,
    APIGatewayTagResourceRequest,
    APIGatewayTagResourceResponse,
    APIGatewayTestInvokeAuthorizerRequest,
    APIGatewayTestInvokeAuthorizerResponse,
    APIGatewayTestInvokeMethodRequest,
    APIGatewayTestInvokeMethodResponse,
    APIGatewayUntagResourceRequest,
    APIGatewayUntagResourceResponse,
    APIGatewayUpdateAccountRequest,
    APIGatewayUpdateAccountResponse,
    APIGatewayUpdateApiKeyRequest,
    APIGatewayUpdateApiKeyResponse,
    APIGatewayUpdateAuthorizerRequest,
    APIGatewayUpdateAuthorizerResponse,
    APIGatewayUpdateBasePathMappingRequest,
    APIGatewayUpdateBasePathMappingResponse,
    APIGatewayUpdateClientCertificateRequest,
    APIGatewayUpdateClientCertificateResponse,
    APIGatewayUpdateDeploymentRequest,
    APIGatewayUpdateDeploymentResponse,
    APIGatewayUpdateDocumentationPartRequest,
    APIGatewayUpdateDocumentationPartResponse,
    APIGatewayUpdateDocumentationVersionRequest,
    APIGatewayUpdateDocumentationVersionResponse,
    APIGatewayUpdateDomainNameRequest,
    APIGatewayUpdateDomainNameResponse,
    APIGatewayUpdateGatewayResponseRequest,
    APIGatewayUpdateGatewayResponseResponse,
    APIGatewayUpdateIntegrationRequest,
    APIGatewayUpdateIntegrationResponse,
    APIGatewayUpdateIntegrationResponseRequest,
    APIGatewayUpdateIntegrationResponseResponse,
    APIGatewayUpdateMethodRequest,
    APIGatewayUpdateMethodResponse,
    APIGatewayUpdateMethodResponseRequest,
    APIGatewayUpdateMethodResponseResponse,
    APIGatewayUpdateModelRequest,
    APIGatewayUpdateModelResponse,
    APIGatewayUpdateRequestValidatorRequest,
    APIGatewayUpdateRequestValidatorResponse,
    APIGatewayUpdateResourceRequest,
    APIGatewayUpdateResourceResponse,
    APIGatewayUpdateRestApiRequest,
    APIGatewayUpdateRestApiResponse,
    APIGatewayUpdateStageRequest,
    APIGatewayUpdateStageResponse,
    APIGatewayUpdateUsagePlanRequest,
    APIGatewayUpdateUsagePlanResponse,
    APIGatewayUpdateUsageRequest,
    APIGatewayUpdateUsageResponse,
    APIGatewayUpdateVpcLinkRequest,
    APIGatewayUpdateVpcLinkResponse,
)
from werkflow_aws.types.api_gateway_client import APIGatewayClient
from .base import AWSBaseService


class AWSAPIGateway(AWSBaseService[APIGatewayClient]):
    service_name = 'api-gateway'
    boto3_service_name = 'apigateway'

    def __init__(self) -> None:
        super().__init__(service_name='api-gateway', boto3_service_name='apigateway')

    async def create_api_key(
        self,
        request: APIGatewayCreateApiKeyRequest | None = None,
    ) -> APIGatewayCreateApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_api_key, request, APIGatewayCreateApiKeyResponse)

    async def create_authorizer(
        self,
        request: APIGatewayCreateAuthorizerRequest,
    ) -> APIGatewayCreateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.create_authorizer, request, APIGatewayCreateAuthorizerResponse)

    async def create_base_path_mapping(
        self,
        request: APIGatewayCreateBasePathMappingRequest,
    ) -> APIGatewayCreateBasePathMappingResponse:
        client = self._require_client()
        return await self._execute(client.create_base_path_mapping, request, APIGatewayCreateBasePathMappingResponse)

    async def create_deployment(
        self,
        request: APIGatewayCreateDeploymentRequest,
    ) -> APIGatewayCreateDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_deployment, request, APIGatewayCreateDeploymentResponse)

    async def create_documentation_part(
        self,
        request: APIGatewayCreateDocumentationPartRequest,
    ) -> APIGatewayCreateDocumentationPartResponse:
        client = self._require_client()
        return await self._execute(client.create_documentation_part, request, APIGatewayCreateDocumentationPartResponse)

    async def create_documentation_version(
        self,
        request: APIGatewayCreateDocumentationVersionRequest,
    ) -> APIGatewayCreateDocumentationVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_documentation_version, request, APIGatewayCreateDocumentationVersionResponse)

    async def create_domain_name(
        self,
        request: APIGatewayCreateDomainNameRequest,
    ) -> APIGatewayCreateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_name, request, APIGatewayCreateDomainNameResponse)

    async def create_domain_name_access_association(
        self,
        request: APIGatewayCreateDomainNameAccessAssociationRequest,
    ) -> APIGatewayCreateDomainNameAccessAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_name_access_association, request, APIGatewayCreateDomainNameAccessAssociationResponse)

    async def create_model(
        self,
        request: APIGatewayCreateModelRequest,
    ) -> APIGatewayCreateModelResponse:
        client = self._require_client()
        return await self._execute(client.create_model, request, APIGatewayCreateModelResponse)

    async def create_request_validator(
        self,
        request: APIGatewayCreateRequestValidatorRequest,
    ) -> APIGatewayCreateRequestValidatorResponse:
        client = self._require_client()
        return await self._execute(client.create_request_validator, request, APIGatewayCreateRequestValidatorResponse)

    async def create_resource(
        self,
        request: APIGatewayCreateResourceRequest,
    ) -> APIGatewayCreateResourceResponse:
        client = self._require_client()
        return await self._execute(client.create_resource, request, APIGatewayCreateResourceResponse)

    async def create_rest_api(
        self,
        request: APIGatewayCreateRestApiRequest,
    ) -> APIGatewayCreateRestApiResponse:
        client = self._require_client()
        return await self._execute(client.create_rest_api, request, APIGatewayCreateRestApiResponse)

    async def create_stage(
        self,
        request: APIGatewayCreateStageRequest,
    ) -> APIGatewayCreateStageResponse:
        client = self._require_client()
        return await self._execute(client.create_stage, request, APIGatewayCreateStageResponse)

    async def create_usage_plan(
        self,
        request: APIGatewayCreateUsagePlanRequest,
    ) -> APIGatewayCreateUsagePlanResponse:
        client = self._require_client()
        return await self._execute(client.create_usage_plan, request, APIGatewayCreateUsagePlanResponse)

    async def create_usage_plan_key(
        self,
        request: APIGatewayCreateUsagePlanKeyRequest,
    ) -> APIGatewayCreateUsagePlanKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_usage_plan_key, request, APIGatewayCreateUsagePlanKeyResponse)

    async def create_vpc_link(
        self,
        request: APIGatewayCreateVpcLinkRequest,
    ) -> APIGatewayCreateVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_link, request, APIGatewayCreateVpcLinkResponse)

    async def delete_api_key(
        self,
        request: APIGatewayDeleteApiKeyRequest,
    ) -> APIGatewayDeleteApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_key, request, APIGatewayDeleteApiKeyResponse)

    async def delete_authorizer(
        self,
        request: APIGatewayDeleteAuthorizerRequest,
    ) -> APIGatewayDeleteAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.delete_authorizer, request, APIGatewayDeleteAuthorizerResponse)

    async def delete_base_path_mapping(
        self,
        request: APIGatewayDeleteBasePathMappingRequest,
    ) -> APIGatewayDeleteBasePathMappingResponse:
        client = self._require_client()
        return await self._execute(client.delete_base_path_mapping, request, APIGatewayDeleteBasePathMappingResponse)

    async def delete_client_certificate(
        self,
        request: APIGatewayDeleteClientCertificateRequest,
    ) -> APIGatewayDeleteClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_client_certificate, request, APIGatewayDeleteClientCertificateResponse)

    async def delete_deployment(
        self,
        request: APIGatewayDeleteDeploymentRequest,
    ) -> APIGatewayDeleteDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.delete_deployment, request, APIGatewayDeleteDeploymentResponse)

    async def delete_documentation_part(
        self,
        request: APIGatewayDeleteDocumentationPartRequest,
    ) -> APIGatewayDeleteDocumentationPartResponse:
        client = self._require_client()
        return await self._execute(client.delete_documentation_part, request, APIGatewayDeleteDocumentationPartResponse)

    async def delete_documentation_version(
        self,
        request: APIGatewayDeleteDocumentationVersionRequest,
    ) -> APIGatewayDeleteDocumentationVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_documentation_version, request, APIGatewayDeleteDocumentationVersionResponse)

    async def delete_domain_name(
        self,
        request: APIGatewayDeleteDomainNameRequest,
    ) -> APIGatewayDeleteDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_name, request, APIGatewayDeleteDomainNameResponse)

    async def delete_domain_name_access_association(
        self,
        request: APIGatewayDeleteDomainNameAccessAssociationRequest,
    ) -> APIGatewayDeleteDomainNameAccessAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_name_access_association, request, APIGatewayDeleteDomainNameAccessAssociationResponse)

    async def delete_gateway_response(
        self,
        request: APIGatewayDeleteGatewayResponseRequest,
    ) -> APIGatewayDeleteGatewayResponseResponse:
        client = self._require_client()
        return await self._execute(client.delete_gateway_response, request, APIGatewayDeleteGatewayResponseResponse)

    async def delete_integration(
        self,
        request: APIGatewayDeleteIntegrationRequest,
    ) -> APIGatewayDeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, APIGatewayDeleteIntegrationResponse)

    async def delete_integration_response(
        self,
        request: APIGatewayDeleteIntegrationResponseRequest,
    ) -> APIGatewayDeleteIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration_response, request, APIGatewayDeleteIntegrationResponseResponse)

    async def delete_method(
        self,
        request: APIGatewayDeleteMethodRequest,
    ) -> APIGatewayDeleteMethodResponse:
        client = self._require_client()
        return await self._execute(client.delete_method, request, APIGatewayDeleteMethodResponse)

    async def delete_method_response(
        self,
        request: APIGatewayDeleteMethodResponseRequest,
    ) -> APIGatewayDeleteMethodResponseResponse:
        client = self._require_client()
        return await self._execute(client.delete_method_response, request, APIGatewayDeleteMethodResponseResponse)

    async def delete_model(
        self,
        request: APIGatewayDeleteModelRequest,
    ) -> APIGatewayDeleteModelResponse:
        client = self._require_client()
        return await self._execute(client.delete_model, request, APIGatewayDeleteModelResponse)

    async def delete_request_validator(
        self,
        request: APIGatewayDeleteRequestValidatorRequest,
    ) -> APIGatewayDeleteRequestValidatorResponse:
        client = self._require_client()
        return await self._execute(client.delete_request_validator, request, APIGatewayDeleteRequestValidatorResponse)

    async def delete_resource(
        self,
        request: APIGatewayDeleteResourceRequest,
    ) -> APIGatewayDeleteResourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource, request, APIGatewayDeleteResourceResponse)

    async def delete_rest_api(
        self,
        request: APIGatewayDeleteRestApiRequest,
    ) -> APIGatewayDeleteRestApiResponse:
        client = self._require_client()
        return await self._execute(client.delete_rest_api, request, APIGatewayDeleteRestApiResponse)

    async def delete_stage(
        self,
        request: APIGatewayDeleteStageRequest,
    ) -> APIGatewayDeleteStageResponse:
        client = self._require_client()
        return await self._execute(client.delete_stage, request, APIGatewayDeleteStageResponse)

    async def delete_usage_plan(
        self,
        request: APIGatewayDeleteUsagePlanRequest,
    ) -> APIGatewayDeleteUsagePlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_usage_plan, request, APIGatewayDeleteUsagePlanResponse)

    async def delete_usage_plan_key(
        self,
        request: APIGatewayDeleteUsagePlanKeyRequest,
    ) -> APIGatewayDeleteUsagePlanKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_usage_plan_key, request, APIGatewayDeleteUsagePlanKeyResponse)

    async def delete_vpc_link(
        self,
        request: APIGatewayDeleteVpcLinkRequest,
    ) -> APIGatewayDeleteVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_link, request, APIGatewayDeleteVpcLinkResponse)

    async def flush_stage_authorizers_cache(
        self,
        request: APIGatewayFlushStageAuthorizersCacheRequest,
    ) -> APIGatewayFlushStageAuthorizersCacheResponse:
        client = self._require_client()
        return await self._execute(client.flush_stage_authorizers_cache, request, APIGatewayFlushStageAuthorizersCacheResponse)

    async def flush_stage_cache(
        self,
        request: APIGatewayFlushStageCacheRequest,
    ) -> APIGatewayFlushStageCacheResponse:
        client = self._require_client()
        return await self._execute(client.flush_stage_cache, request, APIGatewayFlushStageCacheResponse)

    async def generate_client_certificate(
        self,
        request: APIGatewayGenerateClientCertificateRequest | None = None,
    ) -> APIGatewayGenerateClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.generate_client_certificate, request, APIGatewayGenerateClientCertificateResponse)

    async def get_account(
        self,
        request: APIGatewayGetAccountRequest | None = None,
    ) -> APIGatewayGetAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_account, request, APIGatewayGetAccountResponse)

    async def get_api_key(
        self,
        request: APIGatewayGetApiKeyRequest,
    ) -> APIGatewayGetApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_api_key, request, APIGatewayGetApiKeyResponse)

    async def get_api_keys(
        self,
        request: APIGatewayGetApiKeysRequest | None = None,
    ) -> APIGatewayGetApiKeysResponse:
        client = self._require_client()
        return await self._execute(client.get_api_keys, request, APIGatewayGetApiKeysResponse)

    async def get_api_keys_paginated(
        self,
        request: APIGatewayGetApiKeysRequest | None = None,
    ) -> list[APIGatewayGetApiKeysResponse]:
        return await self._paginate('get_api_keys', request, APIGatewayGetApiKeysResponse)

    async def get_authorizer(
        self,
        request: APIGatewayGetAuthorizerRequest,
    ) -> APIGatewayGetAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.get_authorizer, request, APIGatewayGetAuthorizerResponse)

    async def get_authorizers(
        self,
        request: APIGatewayGetAuthorizersRequest,
    ) -> APIGatewayGetAuthorizersResponse:
        client = self._require_client()
        return await self._execute(client.get_authorizers, request, APIGatewayGetAuthorizersResponse)

    async def get_authorizers_paginated(
        self,
        request: APIGatewayGetAuthorizersRequest,
    ) -> list[APIGatewayGetAuthorizersResponse]:
        return await self._paginate('get_authorizers', request, APIGatewayGetAuthorizersResponse)

    async def get_base_path_mapping(
        self,
        request: APIGatewayGetBasePathMappingRequest,
    ) -> APIGatewayGetBasePathMappingResponse:
        client = self._require_client()
        return await self._execute(client.get_base_path_mapping, request, APIGatewayGetBasePathMappingResponse)

    async def get_base_path_mappings(
        self,
        request: APIGatewayGetBasePathMappingsRequest,
    ) -> APIGatewayGetBasePathMappingsResponse:
        client = self._require_client()
        return await self._execute(client.get_base_path_mappings, request, APIGatewayGetBasePathMappingsResponse)

    async def get_base_path_mappings_paginated(
        self,
        request: APIGatewayGetBasePathMappingsRequest,
    ) -> list[APIGatewayGetBasePathMappingsResponse]:
        return await self._paginate('get_base_path_mappings', request, APIGatewayGetBasePathMappingsResponse)

    async def get_client_certificate(
        self,
        request: APIGatewayGetClientCertificateRequest,
    ) -> APIGatewayGetClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.get_client_certificate, request, APIGatewayGetClientCertificateResponse)

    async def get_client_certificates(
        self,
        request: APIGatewayGetClientCertificatesRequest | None = None,
    ) -> APIGatewayGetClientCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.get_client_certificates, request, APIGatewayGetClientCertificatesResponse)

    async def get_client_certificates_paginated(
        self,
        request: APIGatewayGetClientCertificatesRequest | None = None,
    ) -> list[APIGatewayGetClientCertificatesResponse]:
        return await self._paginate('get_client_certificates', request, APIGatewayGetClientCertificatesResponse)

    async def get_deployment(
        self,
        request: APIGatewayGetDeploymentRequest,
    ) -> APIGatewayGetDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.get_deployment, request, APIGatewayGetDeploymentResponse)

    async def get_deployments(
        self,
        request: APIGatewayGetDeploymentsRequest,
    ) -> APIGatewayGetDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.get_deployments, request, APIGatewayGetDeploymentsResponse)

    async def get_deployments_paginated(
        self,
        request: APIGatewayGetDeploymentsRequest,
    ) -> list[APIGatewayGetDeploymentsResponse]:
        return await self._paginate('get_deployments', request, APIGatewayGetDeploymentsResponse)

    async def get_documentation_part(
        self,
        request: APIGatewayGetDocumentationPartRequest,
    ) -> APIGatewayGetDocumentationPartResponse:
        client = self._require_client()
        return await self._execute(client.get_documentation_part, request, APIGatewayGetDocumentationPartResponse)

    async def get_documentation_parts(
        self,
        request: APIGatewayGetDocumentationPartsRequest,
    ) -> APIGatewayGetDocumentationPartsResponse:
        client = self._require_client()
        return await self._execute(client.get_documentation_parts, request, APIGatewayGetDocumentationPartsResponse)

    async def get_documentation_parts_paginated(
        self,
        request: APIGatewayGetDocumentationPartsRequest,
    ) -> list[APIGatewayGetDocumentationPartsResponse]:
        return await self._paginate('get_documentation_parts', request, APIGatewayGetDocumentationPartsResponse)

    async def get_documentation_version(
        self,
        request: APIGatewayGetDocumentationVersionRequest,
    ) -> APIGatewayGetDocumentationVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_documentation_version, request, APIGatewayGetDocumentationVersionResponse)

    async def get_documentation_versions(
        self,
        request: APIGatewayGetDocumentationVersionsRequest,
    ) -> APIGatewayGetDocumentationVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_documentation_versions, request, APIGatewayGetDocumentationVersionsResponse)

    async def get_documentation_versions_paginated(
        self,
        request: APIGatewayGetDocumentationVersionsRequest,
    ) -> list[APIGatewayGetDocumentationVersionsResponse]:
        return await self._paginate('get_documentation_versions', request, APIGatewayGetDocumentationVersionsResponse)

    async def get_domain_name(
        self,
        request: APIGatewayGetDomainNameRequest,
    ) -> APIGatewayGetDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_name, request, APIGatewayGetDomainNameResponse)

    async def get_domain_name_access_associations(
        self,
        request: APIGatewayGetDomainNameAccessAssociationsRequest | None = None,
    ) -> APIGatewayGetDomainNameAccessAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_name_access_associations, request, APIGatewayGetDomainNameAccessAssociationsResponse)

    async def get_domain_names(
        self,
        request: APIGatewayGetDomainNamesRequest | None = None,
    ) -> APIGatewayGetDomainNamesResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_names, request, APIGatewayGetDomainNamesResponse)

    async def get_domain_names_paginated(
        self,
        request: APIGatewayGetDomainNamesRequest | None = None,
    ) -> list[APIGatewayGetDomainNamesResponse]:
        return await self._paginate('get_domain_names', request, APIGatewayGetDomainNamesResponse)

    async def get_export(
        self,
        request: APIGatewayGetExportRequest,
    ) -> APIGatewayGetExportResponse:
        client = self._require_client()
        return await self._execute(client.get_export, request, APIGatewayGetExportResponse)

    async def get_gateway_response(
        self,
        request: APIGatewayGetGatewayResponseRequest,
    ) -> APIGatewayGetGatewayResponseResponse:
        client = self._require_client()
        return await self._execute(client.get_gateway_response, request, APIGatewayGetGatewayResponseResponse)

    async def get_gateway_responses(
        self,
        request: APIGatewayGetGatewayResponsesRequest,
    ) -> APIGatewayGetGatewayResponsesResponse:
        client = self._require_client()
        return await self._execute(client.get_gateway_responses, request, APIGatewayGetGatewayResponsesResponse)

    async def get_gateway_responses_paginated(
        self,
        request: APIGatewayGetGatewayResponsesRequest,
    ) -> list[APIGatewayGetGatewayResponsesResponse]:
        return await self._paginate('get_gateway_responses', request, APIGatewayGetGatewayResponsesResponse)

    async def get_integration(
        self,
        request: APIGatewayGetIntegrationRequest,
    ) -> APIGatewayGetIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.get_integration, request, APIGatewayGetIntegrationResponse)

    async def get_integration_response(
        self,
        request: APIGatewayGetIntegrationResponseRequest,
    ) -> APIGatewayGetIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.get_integration_response, request, APIGatewayGetIntegrationResponseResponse)

    async def get_method(
        self,
        request: APIGatewayGetMethodRequest,
    ) -> APIGatewayGetMethodResponse:
        client = self._require_client()
        return await self._execute(client.get_method, request, APIGatewayGetMethodResponse)

    async def get_method_response(
        self,
        request: APIGatewayGetMethodResponseRequest,
    ) -> APIGatewayGetMethodResponseResponse:
        client = self._require_client()
        return await self._execute(client.get_method_response, request, APIGatewayGetMethodResponseResponse)

    async def get_model(
        self,
        request: APIGatewayGetModelRequest,
    ) -> APIGatewayGetModelResponse:
        client = self._require_client()
        return await self._execute(client.get_model, request, APIGatewayGetModelResponse)

    async def get_model_template(
        self,
        request: APIGatewayGetModelTemplateRequest,
    ) -> APIGatewayGetModelTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_model_template, request, APIGatewayGetModelTemplateResponse)

    async def get_models(
        self,
        request: APIGatewayGetModelsRequest,
    ) -> APIGatewayGetModelsResponse:
        client = self._require_client()
        return await self._execute(client.get_models, request, APIGatewayGetModelsResponse)

    async def get_models_paginated(
        self,
        request: APIGatewayGetModelsRequest,
    ) -> list[APIGatewayGetModelsResponse]:
        return await self._paginate('get_models', request, APIGatewayGetModelsResponse)

    async def get_request_validator(
        self,
        request: APIGatewayGetRequestValidatorRequest,
    ) -> APIGatewayGetRequestValidatorResponse:
        client = self._require_client()
        return await self._execute(client.get_request_validator, request, APIGatewayGetRequestValidatorResponse)

    async def get_request_validators(
        self,
        request: APIGatewayGetRequestValidatorsRequest,
    ) -> APIGatewayGetRequestValidatorsResponse:
        client = self._require_client()
        return await self._execute(client.get_request_validators, request, APIGatewayGetRequestValidatorsResponse)

    async def get_request_validators_paginated(
        self,
        request: APIGatewayGetRequestValidatorsRequest,
    ) -> list[APIGatewayGetRequestValidatorsResponse]:
        return await self._paginate('get_request_validators', request, APIGatewayGetRequestValidatorsResponse)

    async def get_resource(
        self,
        request: APIGatewayGetResourceRequest,
    ) -> APIGatewayGetResourceResponse:
        client = self._require_client()
        return await self._execute(client.get_resource, request, APIGatewayGetResourceResponse)

    async def get_resources(
        self,
        request: APIGatewayGetResourcesRequest,
    ) -> APIGatewayGetResourcesResponse:
        client = self._require_client()
        return await self._execute(client.get_resources, request, APIGatewayGetResourcesResponse)

    async def get_resources_paginated(
        self,
        request: APIGatewayGetResourcesRequest,
    ) -> list[APIGatewayGetResourcesResponse]:
        return await self._paginate('get_resources', request, APIGatewayGetResourcesResponse)

    async def get_rest_api(
        self,
        request: APIGatewayGetRestApiRequest,
    ) -> APIGatewayGetRestApiResponse:
        client = self._require_client()
        return await self._execute(client.get_rest_api, request, APIGatewayGetRestApiResponse)

    async def get_rest_apis(
        self,
        request: APIGatewayGetRestApisRequest | None = None,
    ) -> APIGatewayGetRestApisResponse:
        client = self._require_client()
        return await self._execute(client.get_rest_apis, request, APIGatewayGetRestApisResponse)

    async def get_rest_apis_paginated(
        self,
        request: APIGatewayGetRestApisRequest | None = None,
    ) -> list[APIGatewayGetRestApisResponse]:
        return await self._paginate('get_rest_apis', request, APIGatewayGetRestApisResponse)

    async def get_sdk(
        self,
        request: APIGatewayGetSdkRequest,
    ) -> APIGatewayGetSdkResponse:
        client = self._require_client()
        return await self._execute(client.get_sdk, request, APIGatewayGetSdkResponse)

    async def get_sdk_type(
        self,
        request: APIGatewayGetSdkTypeRequest,
    ) -> APIGatewayGetSdkTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_sdk_type, request, APIGatewayGetSdkTypeResponse)

    async def get_sdk_types(
        self,
        request: APIGatewayGetSdkTypesRequest | None = None,
    ) -> APIGatewayGetSdkTypesResponse:
        client = self._require_client()
        return await self._execute(client.get_sdk_types, request, APIGatewayGetSdkTypesResponse)

    async def get_sdk_types_paginated(
        self,
        request: APIGatewayGetSdkTypesRequest | None = None,
    ) -> list[APIGatewayGetSdkTypesResponse]:
        return await self._paginate('get_sdk_types', request, APIGatewayGetSdkTypesResponse)

    async def get_stage(
        self,
        request: APIGatewayGetStageRequest,
    ) -> APIGatewayGetStageResponse:
        client = self._require_client()
        return await self._execute(client.get_stage, request, APIGatewayGetStageResponse)

    async def get_stages(
        self,
        request: APIGatewayGetStagesRequest,
    ) -> APIGatewayGetStagesResponse:
        client = self._require_client()
        return await self._execute(client.get_stages, request, APIGatewayGetStagesResponse)

    async def get_tags(
        self,
        request: APIGatewayGetTagsRequest,
    ) -> APIGatewayGetTagsResponse:
        client = self._require_client()
        return await self._execute(client.get_tags, request, APIGatewayGetTagsResponse)

    async def get_usage(
        self,
        request: APIGatewayGetUsageRequest,
    ) -> APIGatewayGetUsageResponse:
        client = self._require_client()
        return await self._execute(client.get_usage, request, APIGatewayGetUsageResponse)

    async def get_usage_paginated(
        self,
        request: APIGatewayGetUsageRequest,
    ) -> list[APIGatewayGetUsageResponse]:
        return await self._paginate('get_usage', request, APIGatewayGetUsageResponse)

    async def get_usage_plan(
        self,
        request: APIGatewayGetUsagePlanRequest,
    ) -> APIGatewayGetUsagePlanResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_plan, request, APIGatewayGetUsagePlanResponse)

    async def get_usage_plan_key(
        self,
        request: APIGatewayGetUsagePlanKeyRequest,
    ) -> APIGatewayGetUsagePlanKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_plan_key, request, APIGatewayGetUsagePlanKeyResponse)

    async def get_usage_plan_keys(
        self,
        request: APIGatewayGetUsagePlanKeysRequest,
    ) -> APIGatewayGetUsagePlanKeysResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_plan_keys, request, APIGatewayGetUsagePlanKeysResponse)

    async def get_usage_plan_keys_paginated(
        self,
        request: APIGatewayGetUsagePlanKeysRequest,
    ) -> list[APIGatewayGetUsagePlanKeysResponse]:
        return await self._paginate('get_usage_plan_keys', request, APIGatewayGetUsagePlanKeysResponse)

    async def get_usage_plans(
        self,
        request: APIGatewayGetUsagePlansRequest | None = None,
    ) -> APIGatewayGetUsagePlansResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_plans, request, APIGatewayGetUsagePlansResponse)

    async def get_usage_plans_paginated(
        self,
        request: APIGatewayGetUsagePlansRequest | None = None,
    ) -> list[APIGatewayGetUsagePlansResponse]:
        return await self._paginate('get_usage_plans', request, APIGatewayGetUsagePlansResponse)

    async def get_vpc_link(
        self,
        request: APIGatewayGetVpcLinkRequest,
    ) -> APIGatewayGetVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_link, request, APIGatewayGetVpcLinkResponse)

    async def get_vpc_links(
        self,
        request: APIGatewayGetVpcLinksRequest | None = None,
    ) -> APIGatewayGetVpcLinksResponse:
        client = self._require_client()
        return await self._execute(client.get_vpc_links, request, APIGatewayGetVpcLinksResponse)

    async def get_vpc_links_paginated(
        self,
        request: APIGatewayGetVpcLinksRequest | None = None,
    ) -> list[APIGatewayGetVpcLinksResponse]:
        return await self._paginate('get_vpc_links', request, APIGatewayGetVpcLinksResponse)

    async def import_api_keys(
        self,
        request: APIGatewayImportApiKeysRequest,
    ) -> APIGatewayImportApiKeysResponse:
        client = self._require_client()
        return await self._execute(client.import_api_keys, request, APIGatewayImportApiKeysResponse)

    async def import_documentation_parts(
        self,
        request: APIGatewayImportDocumentationPartsRequest,
    ) -> APIGatewayImportDocumentationPartsResponse:
        client = self._require_client()
        return await self._execute(client.import_documentation_parts, request, APIGatewayImportDocumentationPartsResponse)

    async def import_rest_api(
        self,
        request: APIGatewayImportRestApiRequest,
    ) -> APIGatewayImportRestApiResponse:
        client = self._require_client()
        return await self._execute(client.import_rest_api, request, APIGatewayImportRestApiResponse)

    async def put_gateway_response(
        self,
        request: APIGatewayPutGatewayResponseRequest,
    ) -> APIGatewayPutGatewayResponseResponse:
        client = self._require_client()
        return await self._execute(client.put_gateway_response, request, APIGatewayPutGatewayResponseResponse)

    async def put_integration(
        self,
        request: APIGatewayPutIntegrationRequest,
    ) -> APIGatewayPutIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.put_integration, request, APIGatewayPutIntegrationResponse)

    async def put_integration_response(
        self,
        request: APIGatewayPutIntegrationResponseRequest,
    ) -> APIGatewayPutIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.put_integration_response, request, APIGatewayPutIntegrationResponseResponse)

    async def put_method(
        self,
        request: APIGatewayPutMethodRequest,
    ) -> APIGatewayPutMethodResponse:
        client = self._require_client()
        return await self._execute(client.put_method, request, APIGatewayPutMethodResponse)

    async def put_method_response(
        self,
        request: APIGatewayPutMethodResponseRequest,
    ) -> APIGatewayPutMethodResponseResponse:
        client = self._require_client()
        return await self._execute(client.put_method_response, request, APIGatewayPutMethodResponseResponse)

    async def put_rest_api(
        self,
        request: APIGatewayPutRestApiRequest,
    ) -> APIGatewayPutRestApiResponse:
        client = self._require_client()
        return await self._execute(client.put_rest_api, request, APIGatewayPutRestApiResponse)

    async def reject_domain_name_access_association(
        self,
        request: APIGatewayRejectDomainNameAccessAssociationRequest,
    ) -> APIGatewayRejectDomainNameAccessAssociationResponse:
        client = self._require_client()
        return await self._execute(client.reject_domain_name_access_association, request, APIGatewayRejectDomainNameAccessAssociationResponse)

    async def tag_resource(
        self,
        request: APIGatewayTagResourceRequest,
    ) -> APIGatewayTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, APIGatewayTagResourceResponse)

    async def test_invoke_authorizer(
        self,
        request: APIGatewayTestInvokeAuthorizerRequest,
    ) -> APIGatewayTestInvokeAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.test_invoke_authorizer, request, APIGatewayTestInvokeAuthorizerResponse)

    async def test_invoke_method(
        self,
        request: APIGatewayTestInvokeMethodRequest,
    ) -> APIGatewayTestInvokeMethodResponse:
        client = self._require_client()
        return await self._execute(client.test_invoke_method, request, APIGatewayTestInvokeMethodResponse)

    async def untag_resource(
        self,
        request: APIGatewayUntagResourceRequest,
    ) -> APIGatewayUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, APIGatewayUntagResourceResponse)

    async def update_account(
        self,
        request: APIGatewayUpdateAccountRequest | None = None,
    ) -> APIGatewayUpdateAccountResponse:
        client = self._require_client()
        return await self._execute(client.update_account, request, APIGatewayUpdateAccountResponse)

    async def update_api_key(
        self,
        request: APIGatewayUpdateApiKeyRequest,
    ) -> APIGatewayUpdateApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_api_key, request, APIGatewayUpdateApiKeyResponse)

    async def update_authorizer(
        self,
        request: APIGatewayUpdateAuthorizerRequest,
    ) -> APIGatewayUpdateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.update_authorizer, request, APIGatewayUpdateAuthorizerResponse)

    async def update_base_path_mapping(
        self,
        request: APIGatewayUpdateBasePathMappingRequest,
    ) -> APIGatewayUpdateBasePathMappingResponse:
        client = self._require_client()
        return await self._execute(client.update_base_path_mapping, request, APIGatewayUpdateBasePathMappingResponse)

    async def update_client_certificate(
        self,
        request: APIGatewayUpdateClientCertificateRequest,
    ) -> APIGatewayUpdateClientCertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_client_certificate, request, APIGatewayUpdateClientCertificateResponse)

    async def update_deployment(
        self,
        request: APIGatewayUpdateDeploymentRequest,
    ) -> APIGatewayUpdateDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.update_deployment, request, APIGatewayUpdateDeploymentResponse)

    async def update_documentation_part(
        self,
        request: APIGatewayUpdateDocumentationPartRequest,
    ) -> APIGatewayUpdateDocumentationPartResponse:
        client = self._require_client()
        return await self._execute(client.update_documentation_part, request, APIGatewayUpdateDocumentationPartResponse)

    async def update_documentation_version(
        self,
        request: APIGatewayUpdateDocumentationVersionRequest,
    ) -> APIGatewayUpdateDocumentationVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_documentation_version, request, APIGatewayUpdateDocumentationVersionResponse)

    async def update_domain_name(
        self,
        request: APIGatewayUpdateDomainNameRequest,
    ) -> APIGatewayUpdateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_name, request, APIGatewayUpdateDomainNameResponse)

    async def update_gateway_response(
        self,
        request: APIGatewayUpdateGatewayResponseRequest,
    ) -> APIGatewayUpdateGatewayResponseResponse:
        client = self._require_client()
        return await self._execute(client.update_gateway_response, request, APIGatewayUpdateGatewayResponseResponse)

    async def update_integration(
        self,
        request: APIGatewayUpdateIntegrationRequest,
    ) -> APIGatewayUpdateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.update_integration, request, APIGatewayUpdateIntegrationResponse)

    async def update_integration_response(
        self,
        request: APIGatewayUpdateIntegrationResponseRequest,
    ) -> APIGatewayUpdateIntegrationResponseResponse:
        client = self._require_client()
        return await self._execute(client.update_integration_response, request, APIGatewayUpdateIntegrationResponseResponse)

    async def update_method(
        self,
        request: APIGatewayUpdateMethodRequest,
    ) -> APIGatewayUpdateMethodResponse:
        client = self._require_client()
        return await self._execute(client.update_method, request, APIGatewayUpdateMethodResponse)

    async def update_method_response(
        self,
        request: APIGatewayUpdateMethodResponseRequest,
    ) -> APIGatewayUpdateMethodResponseResponse:
        client = self._require_client()
        return await self._execute(client.update_method_response, request, APIGatewayUpdateMethodResponseResponse)

    async def update_model(
        self,
        request: APIGatewayUpdateModelRequest,
    ) -> APIGatewayUpdateModelResponse:
        client = self._require_client()
        return await self._execute(client.update_model, request, APIGatewayUpdateModelResponse)

    async def update_request_validator(
        self,
        request: APIGatewayUpdateRequestValidatorRequest,
    ) -> APIGatewayUpdateRequestValidatorResponse:
        client = self._require_client()
        return await self._execute(client.update_request_validator, request, APIGatewayUpdateRequestValidatorResponse)

    async def update_resource(
        self,
        request: APIGatewayUpdateResourceRequest,
    ) -> APIGatewayUpdateResourceResponse:
        client = self._require_client()
        return await self._execute(client.update_resource, request, APIGatewayUpdateResourceResponse)

    async def update_rest_api(
        self,
        request: APIGatewayUpdateRestApiRequest,
    ) -> APIGatewayUpdateRestApiResponse:
        client = self._require_client()
        return await self._execute(client.update_rest_api, request, APIGatewayUpdateRestApiResponse)

    async def update_stage(
        self,
        request: APIGatewayUpdateStageRequest,
    ) -> APIGatewayUpdateStageResponse:
        client = self._require_client()
        return await self._execute(client.update_stage, request, APIGatewayUpdateStageResponse)

    async def update_usage(
        self,
        request: APIGatewayUpdateUsageRequest,
    ) -> APIGatewayUpdateUsageResponse:
        client = self._require_client()
        return await self._execute(client.update_usage, request, APIGatewayUpdateUsageResponse)

    async def update_usage_plan(
        self,
        request: APIGatewayUpdateUsagePlanRequest,
    ) -> APIGatewayUpdateUsagePlanResponse:
        client = self._require_client()
        return await self._execute(client.update_usage_plan, request, APIGatewayUpdateUsagePlanResponse)

    async def update_vpc_link(
        self,
        request: APIGatewayUpdateVpcLinkRequest,
    ) -> APIGatewayUpdateVpcLinkResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_link, request, APIGatewayUpdateVpcLinkResponse)
