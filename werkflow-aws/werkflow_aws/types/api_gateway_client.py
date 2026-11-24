from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class APIGatewayClient(ABC):

    @abstractmethod
    def create_api_key(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        generateDistinctId: bool | None = None,
        value: str | None = None,
        stageKeys: list[dict[str, Any]] | None = None,
        customerId: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_authorizer(
        self,
        *,
        restApiId: str,
        name: str,
        type: str,
        providerARNs: list[str] | None = None,
        authType: str | None = None,
        authorizerUri: str | None = None,
        authorizerCredentials: str | None = None,
        identitySource: str | None = None,
        identityValidationExpression: str | None = None,
        authorizerResultTtlInSeconds: int | None = None,
        jwtConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_base_path_mapping(
        self,
        *,
        domainName: str,
        restApiId: str,
        domainNameId: str | None = None,
        basePath: str | None = None,
        stage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_deployment(
        self,
        *,
        restApiId: str,
        stageName: str | None = None,
        stageDescription: str | None = None,
        description: str | None = None,
        cacheClusterEnabled: bool | None = None,
        cacheClusterSize: str | None = None,
        variables: dict[str, str] | None = None,
        canarySettings: dict[str, Any] | None = None,
        tracingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_documentation_part(
        self,
        *,
        restApiId: str,
        location: dict[str, Any],
        properties: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
        stageName: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_name(
        self,
        *,
        domainName: str,
        certificateName: str | None = None,
        certificateBody: str | None = None,
        certificatePrivateKey: str | None = None,
        certificateChain: str | None = None,
        certificateArn: str | None = None,
        regionalCertificateName: str | None = None,
        regionalCertificateArn: str | None = None,
        endpointConfiguration: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
        securityPolicy: str | None = None,
        endpointAccessMode: str | None = None,
        mutualTlsAuthentication: dict[str, Any] | None = None,
        ownershipVerificationCertificateArn: str | None = None,
        policy: str | None = None,
        routingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_name_access_association(
        self,
        *,
        domainNameArn: str,
        accessAssociationSourceType: str,
        accessAssociationSource: str,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model(
        self,
        *,
        restApiId: str,
        name: str,
        contentType: str,
        description: str | None = None,
        schema: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_request_validator(
        self,
        *,
        restApiId: str,
        name: str | None = None,
        validateRequestBody: bool | None = None,
        validateRequestParameters: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource(
        self,
        *,
        restApiId: str,
        parentId: str,
        pathPart: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rest_api(
        self,
        *,
        name: str,
        description: str | None = None,
        version: str | None = None,
        cloneFrom: str | None = None,
        binaryMediaTypes: list[str] | None = None,
        minimumCompressionSize: int | None = None,
        apiKeySource: str | None = None,
        endpointConfiguration: dict[str, Any] | None = None,
        policy: str | None = None,
        tags: dict[str, str] | None = None,
        disableExecuteApiEndpoint: bool | None = None,
        securityPolicy: str | None = None,
        endpointAccessMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str | None = None,
        cacheClusterEnabled: bool | None = None,
        cacheClusterSize: str | None = None,
        variables: dict[str, str] | None = None,
        documentationVersion: str | None = None,
        canarySettings: dict[str, Any] | None = None,
        tracingEnabled: bool | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_usage_plan(
        self,
        *,
        name: str,
        description: str | None = None,
        apiStages: list[dict[str, Any]] | None = None,
        throttle: dict[str, Any] | None = None,
        quota: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_usage_plan_key(
        self,
        *,
        usagePlanId: str,
        keyId: str,
        keyType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_link(
        self,
        *,
        name: str,
        targetArns: list[str],
        description: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_key(
        self,
        *,
        apiKey: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_base_path_mapping(
        self,
        *,
        domainName: str,
        basePath: str,
        domainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_client_certificate(
        self,
        *,
        clientCertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_deployment(
        self,
        *,
        restApiId: str,
        deploymentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_documentation_part(
        self,
        *,
        restApiId: str,
        documentationPartId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_name(
        self,
        *,
        domainName: str,
        domainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_name_access_association(
        self,
        *,
        domainNameAccessAssociationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model(
        self,
        *,
        restApiId: str,
        modelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_request_validator(
        self,
        *,
        restApiId: str,
        requestValidatorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource(
        self,
        *,
        restApiId: str,
        resourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rest_api(
        self,
        *,
        restApiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_usage_plan(
        self,
        *,
        usagePlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_usage_plan_key(
        self,
        *,
        usagePlanId: str,
        keyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_link(
        self,
        *,
        vpcLinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def flush_stage_authorizers_cache(
        self,
        *,
        restApiId: str,
        stageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def flush_stage_cache(
        self,
        *,
        restApiId: str,
        stageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_client_certificate(
        self,
        *,
        description: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_key(
        self,
        *,
        apiKey: str,
        includeValue: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_keys(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
        nameQuery: str | None = None,
        customerId: str | None = None,
        includeValues: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorizers(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_base_path_mapping(
        self,
        *,
        domainName: str,
        basePath: str,
        domainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_base_path_mappings(
        self,
        *,
        domainName: str,
        domainNameId: str | None = None,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_client_certificate(
        self,
        *,
        clientCertificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_client_certificates(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deployment(
        self,
        *,
        restApiId: str,
        deploymentId: str,
        embed: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deployments(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_documentation_part(
        self,
        *,
        restApiId: str,
        documentationPartId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_documentation_parts(
        self,
        *,
        restApiId: str,
        type: str | None = None,
        nameQuery: str | None = None,
        path: str | None = None,
        position: str | None = None,
        limit: int | None = None,
        locationStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_documentation_versions(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_name(
        self,
        *,
        domainName: str,
        domainNameId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_name_access_associations(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
        resourceOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_names(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
        resourceOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export(
        self,
        *,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: dict[str, str] | None = None,
        accepts: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_gateway_responses(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model(
        self,
        *,
        restApiId: str,
        modelName: str,
        flatten: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_template(
        self,
        *,
        restApiId: str,
        modelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_models(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_request_validator(
        self,
        *,
        restApiId: str,
        requestValidatorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_request_validators(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource(
        self,
        *,
        restApiId: str,
        resourceId: str,
        embed: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resources(
        self,
        *,
        restApiId: str,
        position: str | None = None,
        limit: int | None = None,
        embed: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rest_api(
        self,
        *,
        restApiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rest_apis(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sdk(
        self,
        *,
        restApiId: str,
        stageName: str,
        sdkType: str,
        parameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sdk_type(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sdk_types(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stages(
        self,
        *,
        restApiId: str,
        deploymentId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tags(
        self,
        *,
        resourceArn: str,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage(
        self,
        *,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str | None = None,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_plan(
        self,
        *,
        usagePlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_plan_key(
        self,
        *,
        usagePlanId: str,
        keyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_plan_keys(
        self,
        *,
        usagePlanId: str,
        position: str | None = None,
        limit: int | None = None,
        nameQuery: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_plans(
        self,
        *,
        position: str | None = None,
        keyId: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_link(
        self,
        *,
        vpcLinkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_links(
        self,
        *,
        position: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_api_keys(
        self,
        *,
        body: bytes | BinaryIO | str,
        format: str,
        failOnWarnings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_documentation_parts(
        self,
        *,
        restApiId: str,
        body: bytes | BinaryIO | str,
        mode: str | None = None,
        failOnWarnings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_rest_api(
        self,
        *,
        body: bytes | BinaryIO | str,
        failOnWarnings: bool | None = None,
        parameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: str,
        statusCode: str | None = None,
        responseParameters: dict[str, str] | None = None,
        responseTemplates: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: str,
        integrationHttpMethod: str | None = None,
        uri: str | None = None,
        connectionType: str | None = None,
        connectionId: str | None = None,
        credentials: str | None = None,
        requestParameters: dict[str, str] | None = None,
        requestTemplates: dict[str, str] | None = None,
        passthroughBehavior: str | None = None,
        cacheNamespace: str | None = None,
        cacheKeyParameters: list[str] | None = None,
        contentHandling: str | None = None,
        timeoutInMillis: int | None = None,
        tlsConfig: dict[str, Any] | None = None,
        responseTransferMode: str | None = None,
        integrationTarget: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str | None = None,
        responseParameters: dict[str, str] | None = None,
        responseTemplates: dict[str, str] | None = None,
        contentHandling: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: str | None = None,
        apiKeyRequired: bool | None = None,
        operationName: str | None = None,
        requestParameters: dict[str, bool] | None = None,
        requestModels: dict[str, str] | None = None,
        requestValidatorId: str | None = None,
        authorizationScopes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: dict[str, bool] | None = None,
        responseModels: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_rest_api(
        self,
        *,
        restApiId: str,
        body: bytes | BinaryIO | str,
        mode: str | None = None,
        failOnWarnings: bool | None = None,
        parameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_domain_name_access_association(
        self,
        *,
        domainNameAccessAssociationArn: str,
        domainNameArn: str,
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
    def test_invoke_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
        headers: dict[str, str] | None = None,
        multiValueHeaders: dict[str, list[str]] | None = None,
        pathWithQueryString: str | None = None,
        body: str | None = None,
        stageVariables: dict[str, str] | None = None,
        additionalContext: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_invoke_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str | None = None,
        body: str | None = None,
        headers: dict[str, str] | None = None,
        multiValueHeaders: dict[str, list[str]] | None = None,
        clientCertificateId: str | None = None,
        stageVariables: dict[str, str] | None = None,
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
    def update_account(
        self,
        *,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_api_key(
        self,
        *,
        apiKey: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_base_path_mapping(
        self,
        *,
        domainName: str,
        basePath: str,
        domainNameId: str | None = None,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_client_certificate(
        self,
        *,
        clientCertificateId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_deployment(
        self,
        *,
        restApiId: str,
        deploymentId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_documentation_part(
        self,
        *,
        restApiId: str,
        documentationPartId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_name(
        self,
        *,
        domainName: str,
        domainNameId: str | None = None,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_model(
        self,
        *,
        restApiId: str,
        modelName: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_request_validator(
        self,
        *,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource(
        self,
        *,
        restApiId: str,
        resourceId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rest_api(
        self,
        *,
        restApiId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_usage(
        self,
        *,
        usagePlanId: str,
        keyId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_usage_plan(
        self,
        *,
        usagePlanId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_link(
        self,
        *,
        vpcLinkId: str,
        patchOperations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
