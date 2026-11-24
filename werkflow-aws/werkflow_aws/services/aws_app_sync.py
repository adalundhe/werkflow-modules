from werkflow_aws.models.app_sync import (
    AppSyncAssociateApiRequest,
    AppSyncAssociateApiResponse,
    AppSyncAssociateMergedGraphqlApiRequest,
    AppSyncAssociateMergedGraphqlApiResponse,
    AppSyncAssociateSourceGraphqlApiRequest,
    AppSyncAssociateSourceGraphqlApiResponse,
    AppSyncCreateApiCacheRequest,
    AppSyncCreateApiCacheResponse,
    AppSyncCreateApiKeyRequest,
    AppSyncCreateApiKeyResponse,
    AppSyncCreateApiRequest,
    AppSyncCreateApiResponse,
    AppSyncCreateChannelNamespaceRequest,
    AppSyncCreateChannelNamespaceResponse,
    AppSyncCreateDataSourceRequest,
    AppSyncCreateDataSourceResponse,
    AppSyncCreateDomainNameRequest,
    AppSyncCreateDomainNameResponse,
    AppSyncCreateFunctionRequest,
    AppSyncCreateFunctionResponse,
    AppSyncCreateGraphqlApiRequest,
    AppSyncCreateGraphqlApiResponse,
    AppSyncCreateResolverRequest,
    AppSyncCreateResolverResponse,
    AppSyncCreateTypeRequest,
    AppSyncCreateTypeResponse,
    AppSyncDeleteApiCacheRequest,
    AppSyncDeleteApiCacheResponse,
    AppSyncDeleteApiKeyRequest,
    AppSyncDeleteApiKeyResponse,
    AppSyncDeleteApiRequest,
    AppSyncDeleteApiResponse,
    AppSyncDeleteChannelNamespaceRequest,
    AppSyncDeleteChannelNamespaceResponse,
    AppSyncDeleteDataSourceRequest,
    AppSyncDeleteDataSourceResponse,
    AppSyncDeleteDomainNameRequest,
    AppSyncDeleteDomainNameResponse,
    AppSyncDeleteFunctionRequest,
    AppSyncDeleteFunctionResponse,
    AppSyncDeleteGraphqlApiRequest,
    AppSyncDeleteGraphqlApiResponse,
    AppSyncDeleteResolverRequest,
    AppSyncDeleteResolverResponse,
    AppSyncDeleteTypeRequest,
    AppSyncDeleteTypeResponse,
    AppSyncDisassociateApiRequest,
    AppSyncDisassociateApiResponse,
    AppSyncDisassociateMergedGraphqlApiRequest,
    AppSyncDisassociateMergedGraphqlApiResponse,
    AppSyncDisassociateSourceGraphqlApiRequest,
    AppSyncDisassociateSourceGraphqlApiResponse,
    AppSyncEvaluateCodeRequest,
    AppSyncEvaluateCodeResponse,
    AppSyncEvaluateMappingTemplateRequest,
    AppSyncEvaluateMappingTemplateResponse,
    AppSyncFlushApiCacheRequest,
    AppSyncFlushApiCacheResponse,
    AppSyncGetApiAssociationRequest,
    AppSyncGetApiAssociationResponse,
    AppSyncGetApiCacheRequest,
    AppSyncGetApiCacheResponse,
    AppSyncGetApiRequest,
    AppSyncGetApiResponse,
    AppSyncGetChannelNamespaceRequest,
    AppSyncGetChannelNamespaceResponse,
    AppSyncGetDataSourceIntrospectionRequest,
    AppSyncGetDataSourceIntrospectionResponse,
    AppSyncGetDataSourceRequest,
    AppSyncGetDataSourceResponse,
    AppSyncGetDomainNameRequest,
    AppSyncGetDomainNameResponse,
    AppSyncGetFunctionRequest,
    AppSyncGetFunctionResponse,
    AppSyncGetGraphqlApiEnvironmentVariablesRequest,
    AppSyncGetGraphqlApiEnvironmentVariablesResponse,
    AppSyncGetGraphqlApiRequest,
    AppSyncGetGraphqlApiResponse,
    AppSyncGetIntrospectionSchemaRequest,
    AppSyncGetIntrospectionSchemaResponse,
    AppSyncGetResolverRequest,
    AppSyncGetResolverResponse,
    AppSyncGetSchemaCreationStatusRequest,
    AppSyncGetSchemaCreationStatusResponse,
    AppSyncGetSourceApiAssociationRequest,
    AppSyncGetSourceApiAssociationResponse,
    AppSyncGetTypeRequest,
    AppSyncGetTypeResponse,
    AppSyncListApiKeysRequest,
    AppSyncListApiKeysResponse,
    AppSyncListApisRequest,
    AppSyncListApisResponse,
    AppSyncListChannelNamespacesRequest,
    AppSyncListChannelNamespacesResponse,
    AppSyncListDataSourcesRequest,
    AppSyncListDataSourcesResponse,
    AppSyncListDomainNamesRequest,
    AppSyncListDomainNamesResponse,
    AppSyncListFunctionsRequest,
    AppSyncListFunctionsResponse,
    AppSyncListGraphqlApisRequest,
    AppSyncListGraphqlApisResponse,
    AppSyncListResolversByFunctionRequest,
    AppSyncListResolversByFunctionResponse,
    AppSyncListResolversRequest,
    AppSyncListResolversResponse,
    AppSyncListSourceApiAssociationsRequest,
    AppSyncListSourceApiAssociationsResponse,
    AppSyncListTagsForResourceRequest,
    AppSyncListTagsForResourceResponse,
    AppSyncListTypesByAssociationRequest,
    AppSyncListTypesByAssociationResponse,
    AppSyncListTypesRequest,
    AppSyncListTypesResponse,
    AppSyncPutGraphqlApiEnvironmentVariablesRequest,
    AppSyncPutGraphqlApiEnvironmentVariablesResponse,
    AppSyncStartDataSourceIntrospectionRequest,
    AppSyncStartDataSourceIntrospectionResponse,
    AppSyncStartSchemaCreationRequest,
    AppSyncStartSchemaCreationResponse,
    AppSyncStartSchemaMergeRequest,
    AppSyncStartSchemaMergeResponse,
    AppSyncTagResourceRequest,
    AppSyncTagResourceResponse,
    AppSyncUntagResourceRequest,
    AppSyncUntagResourceResponse,
    AppSyncUpdateApiCacheRequest,
    AppSyncUpdateApiCacheResponse,
    AppSyncUpdateApiKeyRequest,
    AppSyncUpdateApiKeyResponse,
    AppSyncUpdateApiRequest,
    AppSyncUpdateApiResponse,
    AppSyncUpdateChannelNamespaceRequest,
    AppSyncUpdateChannelNamespaceResponse,
    AppSyncUpdateDataSourceRequest,
    AppSyncUpdateDataSourceResponse,
    AppSyncUpdateDomainNameRequest,
    AppSyncUpdateDomainNameResponse,
    AppSyncUpdateFunctionRequest,
    AppSyncUpdateFunctionResponse,
    AppSyncUpdateGraphqlApiRequest,
    AppSyncUpdateGraphqlApiResponse,
    AppSyncUpdateResolverRequest,
    AppSyncUpdateResolverResponse,
    AppSyncUpdateSourceApiAssociationRequest,
    AppSyncUpdateSourceApiAssociationResponse,
    AppSyncUpdateTypeRequest,
    AppSyncUpdateTypeResponse,
)
from werkflow_aws.types.app_sync_client import AppSyncClient
from .base import AWSBaseService


class AWSAppSync(AWSBaseService[AppSyncClient]):
    service_name = 'app-sync'
    boto3_service_name = 'appsync'

    def __init__(self) -> None:
        super().__init__(service_name='app-sync', boto3_service_name='appsync')

    async def associate_api(
        self,
        request: AppSyncAssociateApiRequest,
    ) -> AppSyncAssociateApiResponse:
        client = self._require_client()
        return await self._execute(client.associate_api, request, AppSyncAssociateApiResponse)

    async def associate_merged_graphql_api(
        self,
        request: AppSyncAssociateMergedGraphqlApiRequest,
    ) -> AppSyncAssociateMergedGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.associate_merged_graphql_api, request, AppSyncAssociateMergedGraphqlApiResponse)

    async def associate_source_graphql_api(
        self,
        request: AppSyncAssociateSourceGraphqlApiRequest,
    ) -> AppSyncAssociateSourceGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.associate_source_graphql_api, request, AppSyncAssociateSourceGraphqlApiResponse)

    async def create_api(
        self,
        request: AppSyncCreateApiRequest,
    ) -> AppSyncCreateApiResponse:
        client = self._require_client()
        return await self._execute(client.create_api, request, AppSyncCreateApiResponse)

    async def create_api_cache(
        self,
        request: AppSyncCreateApiCacheRequest,
    ) -> AppSyncCreateApiCacheResponse:
        client = self._require_client()
        return await self._execute(client.create_api_cache, request, AppSyncCreateApiCacheResponse)

    async def create_api_key(
        self,
        request: AppSyncCreateApiKeyRequest,
    ) -> AppSyncCreateApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_api_key, request, AppSyncCreateApiKeyResponse)

    async def create_channel_namespace(
        self,
        request: AppSyncCreateChannelNamespaceRequest,
    ) -> AppSyncCreateChannelNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.create_channel_namespace, request, AppSyncCreateChannelNamespaceResponse)

    async def create_data_source(
        self,
        request: AppSyncCreateDataSourceRequest,
    ) -> AppSyncCreateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_data_source, request, AppSyncCreateDataSourceResponse)

    async def create_domain_name(
        self,
        request: AppSyncCreateDomainNameRequest,
    ) -> AppSyncCreateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_name, request, AppSyncCreateDomainNameResponse)

    async def create_function(
        self,
        request: AppSyncCreateFunctionRequest,
    ) -> AppSyncCreateFunctionResponse:
        client = self._require_client()
        return await self._execute(client.create_function, request, AppSyncCreateFunctionResponse)

    async def create_graphql_api(
        self,
        request: AppSyncCreateGraphqlApiRequest,
    ) -> AppSyncCreateGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.create_graphql_api, request, AppSyncCreateGraphqlApiResponse)

    async def create_resolver(
        self,
        request: AppSyncCreateResolverRequest,
    ) -> AppSyncCreateResolverResponse:
        client = self._require_client()
        return await self._execute(client.create_resolver, request, AppSyncCreateResolverResponse)

    async def create_type(
        self,
        request: AppSyncCreateTypeRequest,
    ) -> AppSyncCreateTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_type, request, AppSyncCreateTypeResponse)

    async def delete_api(
        self,
        request: AppSyncDeleteApiRequest,
    ) -> AppSyncDeleteApiResponse:
        client = self._require_client()
        return await self._execute(client.delete_api, request, AppSyncDeleteApiResponse)

    async def delete_api_cache(
        self,
        request: AppSyncDeleteApiCacheRequest,
    ) -> AppSyncDeleteApiCacheResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_cache, request, AppSyncDeleteApiCacheResponse)

    async def delete_api_key(
        self,
        request: AppSyncDeleteApiKeyRequest,
    ) -> AppSyncDeleteApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_key, request, AppSyncDeleteApiKeyResponse)

    async def delete_channel_namespace(
        self,
        request: AppSyncDeleteChannelNamespaceRequest,
    ) -> AppSyncDeleteChannelNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_channel_namespace, request, AppSyncDeleteChannelNamespaceResponse)

    async def delete_data_source(
        self,
        request: AppSyncDeleteDataSourceRequest,
    ) -> AppSyncDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, AppSyncDeleteDataSourceResponse)

    async def delete_domain_name(
        self,
        request: AppSyncDeleteDomainNameRequest,
    ) -> AppSyncDeleteDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_name, request, AppSyncDeleteDomainNameResponse)

    async def delete_function(
        self,
        request: AppSyncDeleteFunctionRequest,
    ) -> AppSyncDeleteFunctionResponse:
        client = self._require_client()
        return await self._execute(client.delete_function, request, AppSyncDeleteFunctionResponse)

    async def delete_graphql_api(
        self,
        request: AppSyncDeleteGraphqlApiRequest,
    ) -> AppSyncDeleteGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.delete_graphql_api, request, AppSyncDeleteGraphqlApiResponse)

    async def delete_resolver(
        self,
        request: AppSyncDeleteResolverRequest,
    ) -> AppSyncDeleteResolverResponse:
        client = self._require_client()
        return await self._execute(client.delete_resolver, request, AppSyncDeleteResolverResponse)

    async def delete_type(
        self,
        request: AppSyncDeleteTypeRequest,
    ) -> AppSyncDeleteTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_type, request, AppSyncDeleteTypeResponse)

    async def disassociate_api(
        self,
        request: AppSyncDisassociateApiRequest,
    ) -> AppSyncDisassociateApiResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_api, request, AppSyncDisassociateApiResponse)

    async def disassociate_merged_graphql_api(
        self,
        request: AppSyncDisassociateMergedGraphqlApiRequest,
    ) -> AppSyncDisassociateMergedGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_merged_graphql_api, request, AppSyncDisassociateMergedGraphqlApiResponse)

    async def disassociate_source_graphql_api(
        self,
        request: AppSyncDisassociateSourceGraphqlApiRequest,
    ) -> AppSyncDisassociateSourceGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_source_graphql_api, request, AppSyncDisassociateSourceGraphqlApiResponse)

    async def evaluate_code(
        self,
        request: AppSyncEvaluateCodeRequest,
    ) -> AppSyncEvaluateCodeResponse:
        client = self._require_client()
        return await self._execute(client.evaluate_code, request, AppSyncEvaluateCodeResponse)

    async def evaluate_mapping_template(
        self,
        request: AppSyncEvaluateMappingTemplateRequest,
    ) -> AppSyncEvaluateMappingTemplateResponse:
        client = self._require_client()
        return await self._execute(client.evaluate_mapping_template, request, AppSyncEvaluateMappingTemplateResponse)

    async def flush_api_cache(
        self,
        request: AppSyncFlushApiCacheRequest,
    ) -> AppSyncFlushApiCacheResponse:
        client = self._require_client()
        return await self._execute(client.flush_api_cache, request, AppSyncFlushApiCacheResponse)

    async def get_api(
        self,
        request: AppSyncGetApiRequest,
    ) -> AppSyncGetApiResponse:
        client = self._require_client()
        return await self._execute(client.get_api, request, AppSyncGetApiResponse)

    async def get_api_association(
        self,
        request: AppSyncGetApiAssociationRequest,
    ) -> AppSyncGetApiAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_api_association, request, AppSyncGetApiAssociationResponse)

    async def get_api_cache(
        self,
        request: AppSyncGetApiCacheRequest,
    ) -> AppSyncGetApiCacheResponse:
        client = self._require_client()
        return await self._execute(client.get_api_cache, request, AppSyncGetApiCacheResponse)

    async def get_channel_namespace(
        self,
        request: AppSyncGetChannelNamespaceRequest,
    ) -> AppSyncGetChannelNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.get_channel_namespace, request, AppSyncGetChannelNamespaceResponse)

    async def get_data_source(
        self,
        request: AppSyncGetDataSourceRequest,
    ) -> AppSyncGetDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source, request, AppSyncGetDataSourceResponse)

    async def get_data_source_introspection(
        self,
        request: AppSyncGetDataSourceIntrospectionRequest,
    ) -> AppSyncGetDataSourceIntrospectionResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source_introspection, request, AppSyncGetDataSourceIntrospectionResponse)

    async def get_domain_name(
        self,
        request: AppSyncGetDomainNameRequest,
    ) -> AppSyncGetDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_name, request, AppSyncGetDomainNameResponse)

    async def get_function(
        self,
        request: AppSyncGetFunctionRequest,
    ) -> AppSyncGetFunctionResponse:
        client = self._require_client()
        return await self._execute(client.get_function, request, AppSyncGetFunctionResponse)

    async def get_graphql_api(
        self,
        request: AppSyncGetGraphqlApiRequest,
    ) -> AppSyncGetGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.get_graphql_api, request, AppSyncGetGraphqlApiResponse)

    async def get_graphql_api_environment_variables(
        self,
        request: AppSyncGetGraphqlApiEnvironmentVariablesRequest,
    ) -> AppSyncGetGraphqlApiEnvironmentVariablesResponse:
        client = self._require_client()
        return await self._execute(client.get_graphql_api_environment_variables, request, AppSyncGetGraphqlApiEnvironmentVariablesResponse)

    async def get_introspection_schema(
        self,
        request: AppSyncGetIntrospectionSchemaRequest,
    ) -> AppSyncGetIntrospectionSchemaResponse:
        client = self._require_client()
        return await self._execute(client.get_introspection_schema, request, AppSyncGetIntrospectionSchemaResponse)

    async def get_resolver(
        self,
        request: AppSyncGetResolverRequest,
    ) -> AppSyncGetResolverResponse:
        client = self._require_client()
        return await self._execute(client.get_resolver, request, AppSyncGetResolverResponse)

    async def get_schema_creation_status(
        self,
        request: AppSyncGetSchemaCreationStatusRequest,
    ) -> AppSyncGetSchemaCreationStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_schema_creation_status, request, AppSyncGetSchemaCreationStatusResponse)

    async def get_source_api_association(
        self,
        request: AppSyncGetSourceApiAssociationRequest,
    ) -> AppSyncGetSourceApiAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_source_api_association, request, AppSyncGetSourceApiAssociationResponse)

    async def get_type(
        self,
        request: AppSyncGetTypeRequest,
    ) -> AppSyncGetTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_type, request, AppSyncGetTypeResponse)

    async def list_api_keys(
        self,
        request: AppSyncListApiKeysRequest,
    ) -> AppSyncListApiKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_api_keys, request, AppSyncListApiKeysResponse)

    async def list_api_keys_paginated(
        self,
        request: AppSyncListApiKeysRequest,
    ) -> list[AppSyncListApiKeysResponse]:
        return await self._paginate('list_api_keys', request, AppSyncListApiKeysResponse)

    async def list_apis(
        self,
        request: AppSyncListApisRequest | None = None,
    ) -> AppSyncListApisResponse:
        client = self._require_client()
        return await self._execute(client.list_apis, request, AppSyncListApisResponse)

    async def list_apis_paginated(
        self,
        request: AppSyncListApisRequest | None = None,
    ) -> list[AppSyncListApisResponse]:
        return await self._paginate('list_apis', request, AppSyncListApisResponse)

    async def list_channel_namespaces(
        self,
        request: AppSyncListChannelNamespacesRequest,
    ) -> AppSyncListChannelNamespacesResponse:
        client = self._require_client()
        return await self._execute(client.list_channel_namespaces, request, AppSyncListChannelNamespacesResponse)

    async def list_channel_namespaces_paginated(
        self,
        request: AppSyncListChannelNamespacesRequest,
    ) -> list[AppSyncListChannelNamespacesResponse]:
        return await self._paginate('list_channel_namespaces', request, AppSyncListChannelNamespacesResponse)

    async def list_data_sources(
        self,
        request: AppSyncListDataSourcesRequest,
    ) -> AppSyncListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, AppSyncListDataSourcesResponse)

    async def list_data_sources_paginated(
        self,
        request: AppSyncListDataSourcesRequest,
    ) -> list[AppSyncListDataSourcesResponse]:
        return await self._paginate('list_data_sources', request, AppSyncListDataSourcesResponse)

    async def list_domain_names(
        self,
        request: AppSyncListDomainNamesRequest | None = None,
    ) -> AppSyncListDomainNamesResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_names, request, AppSyncListDomainNamesResponse)

    async def list_domain_names_paginated(
        self,
        request: AppSyncListDomainNamesRequest | None = None,
    ) -> list[AppSyncListDomainNamesResponse]:
        return await self._paginate('list_domain_names', request, AppSyncListDomainNamesResponse)

    async def list_functions(
        self,
        request: AppSyncListFunctionsRequest,
    ) -> AppSyncListFunctionsResponse:
        client = self._require_client()
        return await self._execute(client.list_functions, request, AppSyncListFunctionsResponse)

    async def list_functions_paginated(
        self,
        request: AppSyncListFunctionsRequest,
    ) -> list[AppSyncListFunctionsResponse]:
        return await self._paginate('list_functions', request, AppSyncListFunctionsResponse)

    async def list_graphql_apis(
        self,
        request: AppSyncListGraphqlApisRequest | None = None,
    ) -> AppSyncListGraphqlApisResponse:
        client = self._require_client()
        return await self._execute(client.list_graphql_apis, request, AppSyncListGraphqlApisResponse)

    async def list_graphql_apis_paginated(
        self,
        request: AppSyncListGraphqlApisRequest | None = None,
    ) -> list[AppSyncListGraphqlApisResponse]:
        return await self._paginate('list_graphql_apis', request, AppSyncListGraphqlApisResponse)

    async def list_resolvers(
        self,
        request: AppSyncListResolversRequest,
    ) -> AppSyncListResolversResponse:
        client = self._require_client()
        return await self._execute(client.list_resolvers, request, AppSyncListResolversResponse)

    async def list_resolvers_paginated(
        self,
        request: AppSyncListResolversRequest,
    ) -> list[AppSyncListResolversResponse]:
        return await self._paginate('list_resolvers', request, AppSyncListResolversResponse)

    async def list_resolvers_by_function(
        self,
        request: AppSyncListResolversByFunctionRequest,
    ) -> AppSyncListResolversByFunctionResponse:
        client = self._require_client()
        return await self._execute(client.list_resolvers_by_function, request, AppSyncListResolversByFunctionResponse)

    async def list_resolvers_by_function_paginated(
        self,
        request: AppSyncListResolversByFunctionRequest,
    ) -> list[AppSyncListResolversByFunctionResponse]:
        return await self._paginate('list_resolvers_by_function', request, AppSyncListResolversByFunctionResponse)

    async def list_source_api_associations(
        self,
        request: AppSyncListSourceApiAssociationsRequest,
    ) -> AppSyncListSourceApiAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_source_api_associations, request, AppSyncListSourceApiAssociationsResponse)

    async def list_source_api_associations_paginated(
        self,
        request: AppSyncListSourceApiAssociationsRequest,
    ) -> list[AppSyncListSourceApiAssociationsResponse]:
        return await self._paginate('list_source_api_associations', request, AppSyncListSourceApiAssociationsResponse)

    async def list_tags_for_resource(
        self,
        request: AppSyncListTagsForResourceRequest,
    ) -> AppSyncListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AppSyncListTagsForResourceResponse)

    async def list_types(
        self,
        request: AppSyncListTypesRequest,
    ) -> AppSyncListTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_types, request, AppSyncListTypesResponse)

    async def list_types_paginated(
        self,
        request: AppSyncListTypesRequest,
    ) -> list[AppSyncListTypesResponse]:
        return await self._paginate('list_types', request, AppSyncListTypesResponse)

    async def list_types_by_association(
        self,
        request: AppSyncListTypesByAssociationRequest,
    ) -> AppSyncListTypesByAssociationResponse:
        client = self._require_client()
        return await self._execute(client.list_types_by_association, request, AppSyncListTypesByAssociationResponse)

    async def list_types_by_association_paginated(
        self,
        request: AppSyncListTypesByAssociationRequest,
    ) -> list[AppSyncListTypesByAssociationResponse]:
        return await self._paginate('list_types_by_association', request, AppSyncListTypesByAssociationResponse)

    async def put_graphql_api_environment_variables(
        self,
        request: AppSyncPutGraphqlApiEnvironmentVariablesRequest,
    ) -> AppSyncPutGraphqlApiEnvironmentVariablesResponse:
        client = self._require_client()
        return await self._execute(client.put_graphql_api_environment_variables, request, AppSyncPutGraphqlApiEnvironmentVariablesResponse)

    async def start_data_source_introspection(
        self,
        request: AppSyncStartDataSourceIntrospectionRequest | None = None,
    ) -> AppSyncStartDataSourceIntrospectionResponse:
        client = self._require_client()
        return await self._execute(client.start_data_source_introspection, request, AppSyncStartDataSourceIntrospectionResponse)

    async def start_schema_creation(
        self,
        request: AppSyncStartSchemaCreationRequest,
    ) -> AppSyncStartSchemaCreationResponse:
        client = self._require_client()
        return await self._execute(client.start_schema_creation, request, AppSyncStartSchemaCreationResponse)

    async def start_schema_merge(
        self,
        request: AppSyncStartSchemaMergeRequest,
    ) -> AppSyncStartSchemaMergeResponse:
        client = self._require_client()
        return await self._execute(client.start_schema_merge, request, AppSyncStartSchemaMergeResponse)

    async def tag_resource(
        self,
        request: AppSyncTagResourceRequest,
    ) -> AppSyncTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AppSyncTagResourceResponse)

    async def untag_resource(
        self,
        request: AppSyncUntagResourceRequest,
    ) -> AppSyncUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AppSyncUntagResourceResponse)

    async def update_api(
        self,
        request: AppSyncUpdateApiRequest,
    ) -> AppSyncUpdateApiResponse:
        client = self._require_client()
        return await self._execute(client.update_api, request, AppSyncUpdateApiResponse)

    async def update_api_cache(
        self,
        request: AppSyncUpdateApiCacheRequest,
    ) -> AppSyncUpdateApiCacheResponse:
        client = self._require_client()
        return await self._execute(client.update_api_cache, request, AppSyncUpdateApiCacheResponse)

    async def update_api_key(
        self,
        request: AppSyncUpdateApiKeyRequest,
    ) -> AppSyncUpdateApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_api_key, request, AppSyncUpdateApiKeyResponse)

    async def update_channel_namespace(
        self,
        request: AppSyncUpdateChannelNamespaceRequest,
    ) -> AppSyncUpdateChannelNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.update_channel_namespace, request, AppSyncUpdateChannelNamespaceResponse)

    async def update_data_source(
        self,
        request: AppSyncUpdateDataSourceRequest,
    ) -> AppSyncUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, AppSyncUpdateDataSourceResponse)

    async def update_domain_name(
        self,
        request: AppSyncUpdateDomainNameRequest,
    ) -> AppSyncUpdateDomainNameResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_name, request, AppSyncUpdateDomainNameResponse)

    async def update_function(
        self,
        request: AppSyncUpdateFunctionRequest,
    ) -> AppSyncUpdateFunctionResponse:
        client = self._require_client()
        return await self._execute(client.update_function, request, AppSyncUpdateFunctionResponse)

    async def update_graphql_api(
        self,
        request: AppSyncUpdateGraphqlApiRequest,
    ) -> AppSyncUpdateGraphqlApiResponse:
        client = self._require_client()
        return await self._execute(client.update_graphql_api, request, AppSyncUpdateGraphqlApiResponse)

    async def update_resolver(
        self,
        request: AppSyncUpdateResolverRequest,
    ) -> AppSyncUpdateResolverResponse:
        client = self._require_client()
        return await self._execute(client.update_resolver, request, AppSyncUpdateResolverResponse)

    async def update_source_api_association(
        self,
        request: AppSyncUpdateSourceApiAssociationRequest,
    ) -> AppSyncUpdateSourceApiAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_source_api_association, request, AppSyncUpdateSourceApiAssociationResponse)

    async def update_type(
        self,
        request: AppSyncUpdateTypeRequest,
    ) -> AppSyncUpdateTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_type, request, AppSyncUpdateTypeResponse)
