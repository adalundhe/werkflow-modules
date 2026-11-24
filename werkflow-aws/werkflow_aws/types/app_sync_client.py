from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class AppSyncClient(ABC):

    @abstractmethod
    def associate_api(
        self,
        *,
        domainName: str,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_merged_graphql_api(
        self,
        *,
        sourceApiIdentifier: str,
        mergedApiIdentifier: str,
        description: str | None = None,
        sourceApiAssociationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_source_graphql_api(
        self,
        *,
        mergedApiIdentifier: str,
        sourceApiIdentifier: str,
        description: str | None = None,
        sourceApiAssociationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api(
        self,
        *,
        name: str,
        eventConfig: dict[str, Any],
        ownerContact: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api_cache(
        self,
        *,
        apiId: str,
        ttl: int,
        apiCachingBehavior: str,
        type: str,
        transitEncryptionEnabled: bool | None = None,
        atRestEncryptionEnabled: bool | None = None,
        healthMetricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api_key(
        self,
        *,
        apiId: str,
        description: str | None = None,
        expires: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_channel_namespace(
        self,
        *,
        apiId: str,
        name: str,
        subscribeAuthModes: list[dict[str, Any]] | None = None,
        publishAuthModes: list[dict[str, Any]] | None = None,
        codeHandlers: str | None = None,
        tags: dict[str, str] | None = None,
        handlerConfigs: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_source(
        self,
        *,
        apiId: str,
        name: str,
        type: str,
        description: str | None = None,
        serviceRoleArn: str | None = None,
        dynamodbConfig: dict[str, Any] | None = None,
        lambdaConfig: dict[str, Any] | None = None,
        elasticsearchConfig: dict[str, Any] | None = None,
        openSearchServiceConfig: dict[str, Any] | None = None,
        httpConfig: dict[str, Any] | None = None,
        relationalDatabaseConfig: dict[str, Any] | None = None,
        eventBridgeConfig: dict[str, Any] | None = None,
        metricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_name(
        self,
        *,
        domainName: str,
        certificateArn: str,
        description: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_function(
        self,
        *,
        apiId: str,
        name: str,
        dataSourceName: str,
        description: str | None = None,
        requestMappingTemplate: str | None = None,
        responseMappingTemplate: str | None = None,
        functionVersion: str | None = None,
        syncConfig: dict[str, Any] | None = None,
        maxBatchSize: int | None = None,
        runtime: dict[str, Any] | None = None,
        code: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_graphql_api(
        self,
        *,
        name: str,
        authenticationType: str,
        logConfig: dict[str, Any] | None = None,
        userPoolConfig: dict[str, Any] | None = None,
        openIDConnectConfig: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
        additionalAuthenticationProviders: list[dict[str, Any]] | None = None,
        xrayEnabled: bool | None = None,
        lambdaAuthorizerConfig: dict[str, Any] | None = None,
        apiType: str | None = None,
        mergedApiExecutionRoleArn: str | None = None,
        visibility: str | None = None,
        ownerContact: str | None = None,
        introspectionConfig: str | None = None,
        queryDepthLimit: int | None = None,
        resolverCountLimit: int | None = None,
        enhancedMetricsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str | None = None,
        requestMappingTemplate: str | None = None,
        responseMappingTemplate: str | None = None,
        kind: str | None = None,
        pipelineConfig: dict[str, Any] | None = None,
        syncConfig: dict[str, Any] | None = None,
        cachingConfig: dict[str, Any] | None = None,
        maxBatchSize: int | None = None,
        runtime: dict[str, Any] | None = None,
        code: str | None = None,
        metricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_type(
        self,
        *,
        apiId: str,
        definition: str,
        format: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_cache(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_key(
        self,
        *,
        apiId: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_channel_namespace(
        self,
        *,
        apiId: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        apiId: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_name(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function(
        self,
        *,
        apiId: str,
        functionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_graphql_api(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_type(
        self,
        *,
        apiId: str,
        typeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_api(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_merged_graphql_api(
        self,
        *,
        sourceApiIdentifier: str,
        associationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_source_graphql_api(
        self,
        *,
        mergedApiIdentifier: str,
        associationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evaluate_code(
        self,
        *,
        runtime: dict[str, Any],
        code: str,
        context: str,
        function: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evaluate_mapping_template(
        self,
        *,
        template: str,
        context: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def flush_api_cache(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_association(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_api_cache(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_channel_namespace(
        self,
        *,
        apiId: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source(
        self,
        *,
        apiId: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source_introspection(
        self,
        *,
        introspectionId: str,
        includeModelsSDL: bool | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_name(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function(
        self,
        *,
        apiId: str,
        functionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_graphql_api(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_graphql_api_environment_variables(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_introspection_schema(
        self,
        *,
        apiId: str,
        format: str,
        includeDirectives: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema_creation_status(
        self,
        *,
        apiId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_source_api_association(
        self,
        *,
        mergedApiIdentifier: str,
        associationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_type(
        self,
        *,
        apiId: str,
        typeName: str,
        format: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_api_keys(
        self,
        *,
        apiId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apis(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_channel_namespaces(
        self,
        *,
        apiId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        apiId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_names(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_functions(
        self,
        *,
        apiId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_graphql_apis(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        apiType: str | None = None,
        owner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resolvers(
        self,
        *,
        apiId: str,
        typeName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resolvers_by_function(
        self,
        *,
        apiId: str,
        functionId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_source_api_associations(
        self,
        *,
        apiId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_types(
        self,
        *,
        apiId: str,
        format: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_types_by_association(
        self,
        *,
        mergedApiIdentifier: str,
        associationId: str,
        format: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_graphql_api_environment_variables(
        self,
        *,
        apiId: str,
        environmentVariables: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_source_introspection(
        self,
        *,
        rdsDataApiConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_schema_creation(
        self,
        *,
        apiId: str,
        definition: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_schema_merge(
        self,
        *,
        associationId: str,
        mergedApiIdentifier: str,
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
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_api(
        self,
        *,
        apiId: str,
        name: str,
        eventConfig: dict[str, Any],
        ownerContact: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_api_cache(
        self,
        *,
        apiId: str,
        ttl: int,
        apiCachingBehavior: str,
        type: str,
        healthMetricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_api_key(
        self,
        *,
        apiId: str,
        id: str,
        description: str | None = None,
        expires: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_channel_namespace(
        self,
        *,
        apiId: str,
        name: str,
        subscribeAuthModes: list[dict[str, Any]] | None = None,
        publishAuthModes: list[dict[str, Any]] | None = None,
        codeHandlers: str | None = None,
        handlerConfigs: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        apiId: str,
        name: str,
        type: str,
        description: str | None = None,
        serviceRoleArn: str | None = None,
        dynamodbConfig: dict[str, Any] | None = None,
        lambdaConfig: dict[str, Any] | None = None,
        elasticsearchConfig: dict[str, Any] | None = None,
        openSearchServiceConfig: dict[str, Any] | None = None,
        httpConfig: dict[str, Any] | None = None,
        relationalDatabaseConfig: dict[str, Any] | None = None,
        eventBridgeConfig: dict[str, Any] | None = None,
        metricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_name(
        self,
        *,
        domainName: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function(
        self,
        *,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        description: str | None = None,
        requestMappingTemplate: str | None = None,
        responseMappingTemplate: str | None = None,
        functionVersion: str | None = None,
        syncConfig: dict[str, Any] | None = None,
        maxBatchSize: int | None = None,
        runtime: dict[str, Any] | None = None,
        code: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_graphql_api(
        self,
        *,
        apiId: str,
        name: str,
        authenticationType: str,
        logConfig: dict[str, Any] | None = None,
        userPoolConfig: dict[str, Any] | None = None,
        openIDConnectConfig: dict[str, Any] | None = None,
        additionalAuthenticationProviders: list[dict[str, Any]] | None = None,
        xrayEnabled: bool | None = None,
        lambdaAuthorizerConfig: dict[str, Any] | None = None,
        mergedApiExecutionRoleArn: str | None = None,
        ownerContact: str | None = None,
        introspectionConfig: str | None = None,
        queryDepthLimit: int | None = None,
        resolverCountLimit: int | None = None,
        enhancedMetricsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str | None = None,
        requestMappingTemplate: str | None = None,
        responseMappingTemplate: str | None = None,
        kind: str | None = None,
        pipelineConfig: dict[str, Any] | None = None,
        syncConfig: dict[str, Any] | None = None,
        cachingConfig: dict[str, Any] | None = None,
        maxBatchSize: int | None = None,
        runtime: dict[str, Any] | None = None,
        code: str | None = None,
        metricsConfig: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_source_api_association(
        self,
        *,
        associationId: str,
        mergedApiIdentifier: str,
        description: str | None = None,
        sourceApiAssociationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_type(
        self,
        *,
        apiId: str,
        typeName: str,
        format: str,
        definition: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
