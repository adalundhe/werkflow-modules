from werkflow_aws.models.verified_permissions import (
    VerifiedPermissionsBatchGetPolicyRequest,
    VerifiedPermissionsBatchGetPolicyResponse,
    VerifiedPermissionsBatchIsAuthorizedRequest,
    VerifiedPermissionsBatchIsAuthorizedResponse,
    VerifiedPermissionsBatchIsAuthorizedWithTokenRequest,
    VerifiedPermissionsBatchIsAuthorizedWithTokenResponse,
    VerifiedPermissionsCreateIdentitySourceRequest,
    VerifiedPermissionsCreateIdentitySourceResponse,
    VerifiedPermissionsCreatePolicyRequest,
    VerifiedPermissionsCreatePolicyResponse,
    VerifiedPermissionsCreatePolicyStoreAliasRequest,
    VerifiedPermissionsCreatePolicyStoreAliasResponse,
    VerifiedPermissionsCreatePolicyStoreRequest,
    VerifiedPermissionsCreatePolicyStoreResponse,
    VerifiedPermissionsCreatePolicyTemplateRequest,
    VerifiedPermissionsCreatePolicyTemplateResponse,
    VerifiedPermissionsDeleteIdentitySourceRequest,
    VerifiedPermissionsDeleteIdentitySourceResponse,
    VerifiedPermissionsDeletePolicyRequest,
    VerifiedPermissionsDeletePolicyResponse,
    VerifiedPermissionsDeletePolicyStoreAliasRequest,
    VerifiedPermissionsDeletePolicyStoreAliasResponse,
    VerifiedPermissionsDeletePolicyStoreRequest,
    VerifiedPermissionsDeletePolicyStoreResponse,
    VerifiedPermissionsDeletePolicyTemplateRequest,
    VerifiedPermissionsDeletePolicyTemplateResponse,
    VerifiedPermissionsGetIdentitySourceRequest,
    VerifiedPermissionsGetIdentitySourceResponse,
    VerifiedPermissionsGetPolicyRequest,
    VerifiedPermissionsGetPolicyResponse,
    VerifiedPermissionsGetPolicyStoreAliasRequest,
    VerifiedPermissionsGetPolicyStoreAliasResponse,
    VerifiedPermissionsGetPolicyStoreRequest,
    VerifiedPermissionsGetPolicyStoreResponse,
    VerifiedPermissionsGetPolicyTemplateRequest,
    VerifiedPermissionsGetPolicyTemplateResponse,
    VerifiedPermissionsGetSchemaRequest,
    VerifiedPermissionsGetSchemaResponse,
    VerifiedPermissionsIsAuthorizedRequest,
    VerifiedPermissionsIsAuthorizedResponse,
    VerifiedPermissionsIsAuthorizedWithTokenRequest,
    VerifiedPermissionsIsAuthorizedWithTokenResponse,
    VerifiedPermissionsListIdentitySourcesRequest,
    VerifiedPermissionsListIdentitySourcesResponse,
    VerifiedPermissionsListPoliciesRequest,
    VerifiedPermissionsListPoliciesResponse,
    VerifiedPermissionsListPolicyStoreAliasesRequest,
    VerifiedPermissionsListPolicyStoreAliasesResponse,
    VerifiedPermissionsListPolicyStoresRequest,
    VerifiedPermissionsListPolicyStoresResponse,
    VerifiedPermissionsListPolicyTemplatesRequest,
    VerifiedPermissionsListPolicyTemplatesResponse,
    VerifiedPermissionsListTagsForResourceRequest,
    VerifiedPermissionsListTagsForResourceResponse,
    VerifiedPermissionsPutSchemaRequest,
    VerifiedPermissionsPutSchemaResponse,
    VerifiedPermissionsTagResourceRequest,
    VerifiedPermissionsTagResourceResponse,
    VerifiedPermissionsUntagResourceRequest,
    VerifiedPermissionsUntagResourceResponse,
    VerifiedPermissionsUpdateIdentitySourceRequest,
    VerifiedPermissionsUpdateIdentitySourceResponse,
    VerifiedPermissionsUpdatePolicyRequest,
    VerifiedPermissionsUpdatePolicyResponse,
    VerifiedPermissionsUpdatePolicyStoreRequest,
    VerifiedPermissionsUpdatePolicyStoreResponse,
    VerifiedPermissionsUpdatePolicyTemplateRequest,
    VerifiedPermissionsUpdatePolicyTemplateResponse,
)
from werkflow_aws.types.verified_permissions_client import VerifiedPermissionsClient
from .base import AWSBaseService


class AWSVerifiedPermissions(AWSBaseService[VerifiedPermissionsClient]):
    service_name = 'verified-permissions'
    boto3_service_name = 'verifiedpermissions'

    def __init__(self) -> None:
        super().__init__(service_name='verified-permissions', boto3_service_name='verifiedpermissions')

    async def batch_get_policy(
        self,
        request: VerifiedPermissionsBatchGetPolicyRequest,
    ) -> VerifiedPermissionsBatchGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_policy, request, VerifiedPermissionsBatchGetPolicyResponse)

    async def batch_is_authorized(
        self,
        request: VerifiedPermissionsBatchIsAuthorizedRequest,
    ) -> VerifiedPermissionsBatchIsAuthorizedResponse:
        client = self._require_client()
        return await self._execute(client.batch_is_authorized, request, VerifiedPermissionsBatchIsAuthorizedResponse)

    async def batch_is_authorized_with_token(
        self,
        request: VerifiedPermissionsBatchIsAuthorizedWithTokenRequest,
    ) -> VerifiedPermissionsBatchIsAuthorizedWithTokenResponse:
        client = self._require_client()
        return await self._execute(client.batch_is_authorized_with_token, request, VerifiedPermissionsBatchIsAuthorizedWithTokenResponse)

    async def create_identity_source(
        self,
        request: VerifiedPermissionsCreateIdentitySourceRequest,
    ) -> VerifiedPermissionsCreateIdentitySourceResponse:
        client = self._require_client()
        return await self._execute(client.create_identity_source, request, VerifiedPermissionsCreateIdentitySourceResponse)

    async def create_policy(
        self,
        request: VerifiedPermissionsCreatePolicyRequest,
    ) -> VerifiedPermissionsCreatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_policy, request, VerifiedPermissionsCreatePolicyResponse)

    async def create_policy_store(
        self,
        request: VerifiedPermissionsCreatePolicyStoreRequest,
    ) -> VerifiedPermissionsCreatePolicyStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_policy_store, request, VerifiedPermissionsCreatePolicyStoreResponse)

    async def create_policy_store_alias(
        self,
        request: VerifiedPermissionsCreatePolicyStoreAliasRequest,
    ) -> VerifiedPermissionsCreatePolicyStoreAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_policy_store_alias, request, VerifiedPermissionsCreatePolicyStoreAliasResponse)

    async def create_policy_template(
        self,
        request: VerifiedPermissionsCreatePolicyTemplateRequest,
    ) -> VerifiedPermissionsCreatePolicyTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_policy_template, request, VerifiedPermissionsCreatePolicyTemplateResponse)

    async def delete_identity_source(
        self,
        request: VerifiedPermissionsDeleteIdentitySourceRequest,
    ) -> VerifiedPermissionsDeleteIdentitySourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_identity_source, request, VerifiedPermissionsDeleteIdentitySourceResponse)

    async def delete_policy(
        self,
        request: VerifiedPermissionsDeletePolicyRequest,
    ) -> VerifiedPermissionsDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy, request, VerifiedPermissionsDeletePolicyResponse)

    async def delete_policy_store(
        self,
        request: VerifiedPermissionsDeletePolicyStoreRequest,
    ) -> VerifiedPermissionsDeletePolicyStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy_store, request, VerifiedPermissionsDeletePolicyStoreResponse)

    async def delete_policy_store_alias(
        self,
        request: VerifiedPermissionsDeletePolicyStoreAliasRequest,
    ) -> VerifiedPermissionsDeletePolicyStoreAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy_store_alias, request, VerifiedPermissionsDeletePolicyStoreAliasResponse)

    async def delete_policy_template(
        self,
        request: VerifiedPermissionsDeletePolicyTemplateRequest,
    ) -> VerifiedPermissionsDeletePolicyTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy_template, request, VerifiedPermissionsDeletePolicyTemplateResponse)

    async def get_identity_source(
        self,
        request: VerifiedPermissionsGetIdentitySourceRequest,
    ) -> VerifiedPermissionsGetIdentitySourceResponse:
        client = self._require_client()
        return await self._execute(client.get_identity_source, request, VerifiedPermissionsGetIdentitySourceResponse)

    async def get_policy(
        self,
        request: VerifiedPermissionsGetPolicyRequest,
    ) -> VerifiedPermissionsGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_policy, request, VerifiedPermissionsGetPolicyResponse)

    async def get_policy_store(
        self,
        request: VerifiedPermissionsGetPolicyStoreRequest,
    ) -> VerifiedPermissionsGetPolicyStoreResponse:
        client = self._require_client()
        return await self._execute(client.get_policy_store, request, VerifiedPermissionsGetPolicyStoreResponse)

    async def get_policy_store_alias(
        self,
        request: VerifiedPermissionsGetPolicyStoreAliasRequest,
    ) -> VerifiedPermissionsGetPolicyStoreAliasResponse:
        client = self._require_client()
        return await self._execute(client.get_policy_store_alias, request, VerifiedPermissionsGetPolicyStoreAliasResponse)

    async def get_policy_template(
        self,
        request: VerifiedPermissionsGetPolicyTemplateRequest,
    ) -> VerifiedPermissionsGetPolicyTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_policy_template, request, VerifiedPermissionsGetPolicyTemplateResponse)

    async def get_schema(
        self,
        request: VerifiedPermissionsGetSchemaRequest,
    ) -> VerifiedPermissionsGetSchemaResponse:
        client = self._require_client()
        return await self._execute(client.get_schema, request, VerifiedPermissionsGetSchemaResponse)

    async def is_authorized(
        self,
        request: VerifiedPermissionsIsAuthorizedRequest,
    ) -> VerifiedPermissionsIsAuthorizedResponse:
        client = self._require_client()
        return await self._execute(client.is_authorized, request, VerifiedPermissionsIsAuthorizedResponse)

    async def is_authorized_with_token(
        self,
        request: VerifiedPermissionsIsAuthorizedWithTokenRequest,
    ) -> VerifiedPermissionsIsAuthorizedWithTokenResponse:
        client = self._require_client()
        return await self._execute(client.is_authorized_with_token, request, VerifiedPermissionsIsAuthorizedWithTokenResponse)

    async def list_identity_sources(
        self,
        request: VerifiedPermissionsListIdentitySourcesRequest,
    ) -> VerifiedPermissionsListIdentitySourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_sources, request, VerifiedPermissionsListIdentitySourcesResponse)

    async def list_identity_sources_paginated(
        self,
        request: VerifiedPermissionsListIdentitySourcesRequest,
    ) -> list[VerifiedPermissionsListIdentitySourcesResponse]:
        return await self._paginate('list_identity_sources', request, VerifiedPermissionsListIdentitySourcesResponse)

    async def list_policies(
        self,
        request: VerifiedPermissionsListPoliciesRequest,
    ) -> VerifiedPermissionsListPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_policies, request, VerifiedPermissionsListPoliciesResponse)

    async def list_policies_paginated(
        self,
        request: VerifiedPermissionsListPoliciesRequest,
    ) -> list[VerifiedPermissionsListPoliciesResponse]:
        return await self._paginate('list_policies', request, VerifiedPermissionsListPoliciesResponse)

    async def list_policy_store_aliases(
        self,
        request: VerifiedPermissionsListPolicyStoreAliasesRequest | None = None,
    ) -> VerifiedPermissionsListPolicyStoreAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_store_aliases, request, VerifiedPermissionsListPolicyStoreAliasesResponse)

    async def list_policy_store_aliases_paginated(
        self,
        request: VerifiedPermissionsListPolicyStoreAliasesRequest | None = None,
    ) -> list[VerifiedPermissionsListPolicyStoreAliasesResponse]:
        return await self._paginate('list_policy_store_aliases', request, VerifiedPermissionsListPolicyStoreAliasesResponse)

    async def list_policy_stores(
        self,
        request: VerifiedPermissionsListPolicyStoresRequest | None = None,
    ) -> VerifiedPermissionsListPolicyStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_stores, request, VerifiedPermissionsListPolicyStoresResponse)

    async def list_policy_stores_paginated(
        self,
        request: VerifiedPermissionsListPolicyStoresRequest | None = None,
    ) -> list[VerifiedPermissionsListPolicyStoresResponse]:
        return await self._paginate('list_policy_stores', request, VerifiedPermissionsListPolicyStoresResponse)

    async def list_policy_templates(
        self,
        request: VerifiedPermissionsListPolicyTemplatesRequest,
    ) -> VerifiedPermissionsListPolicyTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_templates, request, VerifiedPermissionsListPolicyTemplatesResponse)

    async def list_policy_templates_paginated(
        self,
        request: VerifiedPermissionsListPolicyTemplatesRequest,
    ) -> list[VerifiedPermissionsListPolicyTemplatesResponse]:
        return await self._paginate('list_policy_templates', request, VerifiedPermissionsListPolicyTemplatesResponse)

    async def list_tags_for_resource(
        self,
        request: VerifiedPermissionsListTagsForResourceRequest,
    ) -> VerifiedPermissionsListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, VerifiedPermissionsListTagsForResourceResponse)

    async def put_schema(
        self,
        request: VerifiedPermissionsPutSchemaRequest,
    ) -> VerifiedPermissionsPutSchemaResponse:
        client = self._require_client()
        return await self._execute(client.put_schema, request, VerifiedPermissionsPutSchemaResponse)

    async def tag_resource(
        self,
        request: VerifiedPermissionsTagResourceRequest,
    ) -> VerifiedPermissionsTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, VerifiedPermissionsTagResourceResponse)

    async def untag_resource(
        self,
        request: VerifiedPermissionsUntagResourceRequest,
    ) -> VerifiedPermissionsUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, VerifiedPermissionsUntagResourceResponse)

    async def update_identity_source(
        self,
        request: VerifiedPermissionsUpdateIdentitySourceRequest,
    ) -> VerifiedPermissionsUpdateIdentitySourceResponse:
        client = self._require_client()
        return await self._execute(client.update_identity_source, request, VerifiedPermissionsUpdateIdentitySourceResponse)

    async def update_policy(
        self,
        request: VerifiedPermissionsUpdatePolicyRequest,
    ) -> VerifiedPermissionsUpdatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_policy, request, VerifiedPermissionsUpdatePolicyResponse)

    async def update_policy_store(
        self,
        request: VerifiedPermissionsUpdatePolicyStoreRequest,
    ) -> VerifiedPermissionsUpdatePolicyStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_policy_store, request, VerifiedPermissionsUpdatePolicyStoreResponse)

    async def update_policy_template(
        self,
        request: VerifiedPermissionsUpdatePolicyTemplateRequest,
    ) -> VerifiedPermissionsUpdatePolicyTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_policy_template, request, VerifiedPermissionsUpdatePolicyTemplateResponse)
