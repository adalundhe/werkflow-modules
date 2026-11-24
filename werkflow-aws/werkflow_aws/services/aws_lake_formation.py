from werkflow_aws.models.lake_formation import (
    LakeFormationAddLFTagsToResourceRequest,
    LakeFormationAddLFTagsToResourceResponse,
    LakeFormationAssumeDecoratedRoleWithSAMLRequest,
    LakeFormationAssumeDecoratedRoleWithSAMLResponse,
    LakeFormationAttachRLSPolicyRequest,
    LakeFormationAttachRLSPolicyResponse,
    LakeFormationBatchGrantPermissionsRequest,
    LakeFormationBatchGrantPermissionsResponse,
    LakeFormationBatchRevokePermissionsRequest,
    LakeFormationBatchRevokePermissionsResponse,
    LakeFormationCancelTransactionRequest,
    LakeFormationCancelTransactionResponse,
    LakeFormationCommitTransactionRequest,
    LakeFormationCommitTransactionResponse,
    LakeFormationCreateDataCellsFilterRequest,
    LakeFormationCreateDataCellsFilterResponse,
    LakeFormationCreateLFTagExpressionRequest,
    LakeFormationCreateLFTagExpressionResponse,
    LakeFormationCreateLFTagRequest,
    LakeFormationCreateLFTagResponse,
    LakeFormationCreateLakeFormationIdentityCenterConfigurationRequest,
    LakeFormationCreateLakeFormationIdentityCenterConfigurationResponse,
    LakeFormationCreateLakeFormationOptInRequest,
    LakeFormationCreateLakeFormationOptInResponse,
    LakeFormationCreateRLSPolicyRequest,
    LakeFormationCreateRLSPolicyResponse,
    LakeFormationDeleteDataCellsFilterRequest,
    LakeFormationDeleteDataCellsFilterResponse,
    LakeFormationDeleteLFTagExpressionRequest,
    LakeFormationDeleteLFTagExpressionResponse,
    LakeFormationDeleteLFTagRequest,
    LakeFormationDeleteLFTagResponse,
    LakeFormationDeleteLakeFormationIdentityCenterConfigurationRequest,
    LakeFormationDeleteLakeFormationIdentityCenterConfigurationResponse,
    LakeFormationDeleteLakeFormationOptInRequest,
    LakeFormationDeleteLakeFormationOptInResponse,
    LakeFormationDeleteObjectsOnCancelRequest,
    LakeFormationDeleteObjectsOnCancelResponse,
    LakeFormationDeleteRLSPolicyRequest,
    LakeFormationDeleteRLSPolicyResponse,
    LakeFormationDeregisterResourceRequest,
    LakeFormationDeregisterResourceResponse,
    LakeFormationDescribeLakeFormationIdentityCenterConfigurationRequest,
    LakeFormationDescribeLakeFormationIdentityCenterConfigurationResponse,
    LakeFormationDescribeResourceRequest,
    LakeFormationDescribeResourceResponse,
    LakeFormationDescribeTransactionRequest,
    LakeFormationDescribeTransactionResponse,
    LakeFormationDetachRLSPolicyRequest,
    LakeFormationDetachRLSPolicyResponse,
    LakeFormationExtendTransactionRequest,
    LakeFormationExtendTransactionResponse,
    LakeFormationGetDataCellsFilterRequest,
    LakeFormationGetDataCellsFilterResponse,
    LakeFormationGetDataLakePrincipalRequest,
    LakeFormationGetDataLakePrincipalResponse,
    LakeFormationGetDataLakeSettingsRequest,
    LakeFormationGetDataLakeSettingsResponse,
    LakeFormationGetEffectivePermissionsForPathRequest,
    LakeFormationGetEffectivePermissionsForPathResponse,
    LakeFormationGetGlueFunctionSessionContextRequest,
    LakeFormationGetGlueFunctionSessionContextResponse,
    LakeFormationGetLFTagExpressionRequest,
    LakeFormationGetLFTagExpressionResponse,
    LakeFormationGetLFTagRequest,
    LakeFormationGetLFTagResponse,
    LakeFormationGetQueryStateRequest,
    LakeFormationGetQueryStateResponse,
    LakeFormationGetQueryStatisticsRequest,
    LakeFormationGetQueryStatisticsResponse,
    LakeFormationGetRLSPolicyRequest,
    LakeFormationGetRLSPolicyResponse,
    LakeFormationGetResourceLFTagsRequest,
    LakeFormationGetResourceLFTagsResponse,
    LakeFormationGetTableObjectsRequest,
    LakeFormationGetTableObjectsResponse,
    LakeFormationGetTemporaryDataLocationCredentialsRequest,
    LakeFormationGetTemporaryDataLocationCredentialsResponse,
    LakeFormationGetTemporaryGlueFunctionCredentialsRequest,
    LakeFormationGetTemporaryGlueFunctionCredentialsResponse,
    LakeFormationGetTemporaryGluePartitionCredentialsRequest,
    LakeFormationGetTemporaryGluePartitionCredentialsResponse,
    LakeFormationGetTemporaryGlueTableCredentialsRequest,
    LakeFormationGetTemporaryGlueTableCredentialsResponse,
    LakeFormationGetWorkUnitResultsRequest,
    LakeFormationGetWorkUnitResultsResponse,
    LakeFormationGetWorkUnitsRequest,
    LakeFormationGetWorkUnitsResponse,
    LakeFormationGrantPermissionsRequest,
    LakeFormationGrantPermissionsResponse,
    LakeFormationListDataCellsFilterRequest,
    LakeFormationListDataCellsFilterResponse,
    LakeFormationListLFTagExpressionsRequest,
    LakeFormationListLFTagExpressionsResponse,
    LakeFormationListLFTagsRequest,
    LakeFormationListLFTagsResponse,
    LakeFormationListLakeFormationOptInsRequest,
    LakeFormationListLakeFormationOptInsResponse,
    LakeFormationListPermissionsRequest,
    LakeFormationListPermissionsResponse,
    LakeFormationListRLSPoliciesRequest,
    LakeFormationListRLSPoliciesResponse,
    LakeFormationListRLSPolicyAttachmentsRequest,
    LakeFormationListRLSPolicyAttachmentsResponse,
    LakeFormationListResourcesRequest,
    LakeFormationListResourcesResponse,
    LakeFormationListTableStorageOptimizersRequest,
    LakeFormationListTableStorageOptimizersResponse,
    LakeFormationListTransactionsRequest,
    LakeFormationListTransactionsResponse,
    LakeFormationPutDataLakeSettingsRequest,
    LakeFormationPutDataLakeSettingsResponse,
    LakeFormationRegisterResourceRequest,
    LakeFormationRegisterResourceResponse,
    LakeFormationRemoveLFTagsFromResourceRequest,
    LakeFormationRemoveLFTagsFromResourceResponse,
    LakeFormationRevokePermissionsRequest,
    LakeFormationRevokePermissionsResponse,
    LakeFormationSearchDatabasesByLFTagsRequest,
    LakeFormationSearchDatabasesByLFTagsResponse,
    LakeFormationSearchTablesByLFTagsRequest,
    LakeFormationSearchTablesByLFTagsResponse,
    LakeFormationStartQueryPlanningRequest,
    LakeFormationStartQueryPlanningResponse,
    LakeFormationStartTransactionRequest,
    LakeFormationStartTransactionResponse,
    LakeFormationUpdateDataCellsFilterRequest,
    LakeFormationUpdateDataCellsFilterResponse,
    LakeFormationUpdateLFTagExpressionRequest,
    LakeFormationUpdateLFTagExpressionResponse,
    LakeFormationUpdateLFTagRequest,
    LakeFormationUpdateLFTagResponse,
    LakeFormationUpdateLakeFormationIdentityCenterConfigurationRequest,
    LakeFormationUpdateLakeFormationIdentityCenterConfigurationResponse,
    LakeFormationUpdateRLSPolicyRequest,
    LakeFormationUpdateRLSPolicyResponse,
    LakeFormationUpdateResourceRequest,
    LakeFormationUpdateResourceResponse,
    LakeFormationUpdateTableObjectsRequest,
    LakeFormationUpdateTableObjectsResponse,
    LakeFormationUpdateTableStorageOptimizerRequest,
    LakeFormationUpdateTableStorageOptimizerResponse,
)
from werkflow_aws.types.lake_formation_client import LakeFormationClient
from .base import AWSBaseService


class AWSLakeFormation(AWSBaseService[LakeFormationClient]):
    service_name = 'lake-formation'
    boto3_service_name = 'lakeformation'

    def __init__(self) -> None:
        super().__init__(service_name='lake-formation', boto3_service_name='lakeformation')

    async def add_lf_tags_to_resource(
        self,
        request: LakeFormationAddLFTagsToResourceRequest,
    ) -> LakeFormationAddLFTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_lf_tags_to_resource, request, LakeFormationAddLFTagsToResourceResponse)

    async def assume_decorated_role_with_saml(
        self,
        request: LakeFormationAssumeDecoratedRoleWithSAMLRequest,
    ) -> LakeFormationAssumeDecoratedRoleWithSAMLResponse:
        client = self._require_client()
        return await self._execute(client.assume_decorated_role_with_saml, request, LakeFormationAssumeDecoratedRoleWithSAMLResponse)

    async def attach_rls_policy(
        self,
        request: LakeFormationAttachRLSPolicyRequest,
    ) -> LakeFormationAttachRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.attach_rls_policy, request, LakeFormationAttachRLSPolicyResponse)

    async def batch_grant_permissions(
        self,
        request: LakeFormationBatchGrantPermissionsRequest,
    ) -> LakeFormationBatchGrantPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.batch_grant_permissions, request, LakeFormationBatchGrantPermissionsResponse)

    async def batch_revoke_permissions(
        self,
        request: LakeFormationBatchRevokePermissionsRequest,
    ) -> LakeFormationBatchRevokePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.batch_revoke_permissions, request, LakeFormationBatchRevokePermissionsResponse)

    async def cancel_transaction(
        self,
        request: LakeFormationCancelTransactionRequest,
    ) -> LakeFormationCancelTransactionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_transaction, request, LakeFormationCancelTransactionResponse)

    async def commit_transaction(
        self,
        request: LakeFormationCommitTransactionRequest,
    ) -> LakeFormationCommitTransactionResponse:
        client = self._require_client()
        return await self._execute(client.commit_transaction, request, LakeFormationCommitTransactionResponse)

    async def create_data_cells_filter(
        self,
        request: LakeFormationCreateDataCellsFilterRequest,
    ) -> LakeFormationCreateDataCellsFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_data_cells_filter, request, LakeFormationCreateDataCellsFilterResponse)

    async def create_lf_tag(
        self,
        request: LakeFormationCreateLFTagRequest,
    ) -> LakeFormationCreateLFTagResponse:
        client = self._require_client()
        return await self._execute(client.create_lf_tag, request, LakeFormationCreateLFTagResponse)

    async def create_lf_tag_expression(
        self,
        request: LakeFormationCreateLFTagExpressionRequest,
    ) -> LakeFormationCreateLFTagExpressionResponse:
        client = self._require_client()
        return await self._execute(client.create_lf_tag_expression, request, LakeFormationCreateLFTagExpressionResponse)

    async def create_lake_formation_identity_center_configuration(
        self,
        request: LakeFormationCreateLakeFormationIdentityCenterConfigurationRequest | None = None,
    ) -> LakeFormationCreateLakeFormationIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_lake_formation_identity_center_configuration, request, LakeFormationCreateLakeFormationIdentityCenterConfigurationResponse)

    async def create_lake_formation_opt_in(
        self,
        request: LakeFormationCreateLakeFormationOptInRequest,
    ) -> LakeFormationCreateLakeFormationOptInResponse:
        client = self._require_client()
        return await self._execute(client.create_lake_formation_opt_in, request, LakeFormationCreateLakeFormationOptInResponse)

    async def create_rls_policy(
        self,
        request: LakeFormationCreateRLSPolicyRequest,
    ) -> LakeFormationCreateRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_rls_policy, request, LakeFormationCreateRLSPolicyResponse)

    async def delete_data_cells_filter(
        self,
        request: LakeFormationDeleteDataCellsFilterRequest | None = None,
    ) -> LakeFormationDeleteDataCellsFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_cells_filter, request, LakeFormationDeleteDataCellsFilterResponse)

    async def delete_lf_tag(
        self,
        request: LakeFormationDeleteLFTagRequest,
    ) -> LakeFormationDeleteLFTagResponse:
        client = self._require_client()
        return await self._execute(client.delete_lf_tag, request, LakeFormationDeleteLFTagResponse)

    async def delete_lf_tag_expression(
        self,
        request: LakeFormationDeleteLFTagExpressionRequest,
    ) -> LakeFormationDeleteLFTagExpressionResponse:
        client = self._require_client()
        return await self._execute(client.delete_lf_tag_expression, request, LakeFormationDeleteLFTagExpressionResponse)

    async def delete_lake_formation_identity_center_configuration(
        self,
        request: LakeFormationDeleteLakeFormationIdentityCenterConfigurationRequest | None = None,
    ) -> LakeFormationDeleteLakeFormationIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_lake_formation_identity_center_configuration, request, LakeFormationDeleteLakeFormationIdentityCenterConfigurationResponse)

    async def delete_lake_formation_opt_in(
        self,
        request: LakeFormationDeleteLakeFormationOptInRequest,
    ) -> LakeFormationDeleteLakeFormationOptInResponse:
        client = self._require_client()
        return await self._execute(client.delete_lake_formation_opt_in, request, LakeFormationDeleteLakeFormationOptInResponse)

    async def delete_objects_on_cancel(
        self,
        request: LakeFormationDeleteObjectsOnCancelRequest,
    ) -> LakeFormationDeleteObjectsOnCancelResponse:
        client = self._require_client()
        return await self._execute(client.delete_objects_on_cancel, request, LakeFormationDeleteObjectsOnCancelResponse)

    async def delete_rls_policy(
        self,
        request: LakeFormationDeleteRLSPolicyRequest,
    ) -> LakeFormationDeleteRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_rls_policy, request, LakeFormationDeleteRLSPolicyResponse)

    async def deregister_resource(
        self,
        request: LakeFormationDeregisterResourceRequest,
    ) -> LakeFormationDeregisterResourceResponse:
        client = self._require_client()
        return await self._execute(client.deregister_resource, request, LakeFormationDeregisterResourceResponse)

    async def describe_lake_formation_identity_center_configuration(
        self,
        request: LakeFormationDescribeLakeFormationIdentityCenterConfigurationRequest | None = None,
    ) -> LakeFormationDescribeLakeFormationIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_lake_formation_identity_center_configuration, request, LakeFormationDescribeLakeFormationIdentityCenterConfigurationResponse)

    async def describe_resource(
        self,
        request: LakeFormationDescribeResourceRequest,
    ) -> LakeFormationDescribeResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource, request, LakeFormationDescribeResourceResponse)

    async def describe_transaction(
        self,
        request: LakeFormationDescribeTransactionRequest,
    ) -> LakeFormationDescribeTransactionResponse:
        client = self._require_client()
        return await self._execute(client.describe_transaction, request, LakeFormationDescribeTransactionResponse)

    async def detach_rls_policy(
        self,
        request: LakeFormationDetachRLSPolicyRequest,
    ) -> LakeFormationDetachRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.detach_rls_policy, request, LakeFormationDetachRLSPolicyResponse)

    async def extend_transaction(
        self,
        request: LakeFormationExtendTransactionRequest | None = None,
    ) -> LakeFormationExtendTransactionResponse:
        client = self._require_client()
        return await self._execute(client.extend_transaction, request, LakeFormationExtendTransactionResponse)

    async def get_data_cells_filter(
        self,
        request: LakeFormationGetDataCellsFilterRequest,
    ) -> LakeFormationGetDataCellsFilterResponse:
        client = self._require_client()
        return await self._execute(client.get_data_cells_filter, request, LakeFormationGetDataCellsFilterResponse)

    async def get_data_lake_principal(
        self,
        request: LakeFormationGetDataLakePrincipalRequest | None = None,
    ) -> LakeFormationGetDataLakePrincipalResponse:
        client = self._require_client()
        return await self._execute(client.get_data_lake_principal, request, LakeFormationGetDataLakePrincipalResponse)

    async def get_data_lake_settings(
        self,
        request: LakeFormationGetDataLakeSettingsRequest | None = None,
    ) -> LakeFormationGetDataLakeSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_data_lake_settings, request, LakeFormationGetDataLakeSettingsResponse)

    async def get_effective_permissions_for_path(
        self,
        request: LakeFormationGetEffectivePermissionsForPathRequest,
    ) -> LakeFormationGetEffectivePermissionsForPathResponse:
        client = self._require_client()
        return await self._execute(client.get_effective_permissions_for_path, request, LakeFormationGetEffectivePermissionsForPathResponse)

    async def get_glue_function_session_context(
        self,
        request: LakeFormationGetGlueFunctionSessionContextRequest,
    ) -> LakeFormationGetGlueFunctionSessionContextResponse:
        client = self._require_client()
        return await self._execute(client.get_glue_function_session_context, request, LakeFormationGetGlueFunctionSessionContextResponse)

    async def get_lf_tag(
        self,
        request: LakeFormationGetLFTagRequest,
    ) -> LakeFormationGetLFTagResponse:
        client = self._require_client()
        return await self._execute(client.get_lf_tag, request, LakeFormationGetLFTagResponse)

    async def get_lf_tag_expression(
        self,
        request: LakeFormationGetLFTagExpressionRequest,
    ) -> LakeFormationGetLFTagExpressionResponse:
        client = self._require_client()
        return await self._execute(client.get_lf_tag_expression, request, LakeFormationGetLFTagExpressionResponse)

    async def get_query_state(
        self,
        request: LakeFormationGetQueryStateRequest,
    ) -> LakeFormationGetQueryStateResponse:
        client = self._require_client()
        return await self._execute(client.get_query_state, request, LakeFormationGetQueryStateResponse)

    async def get_query_statistics(
        self,
        request: LakeFormationGetQueryStatisticsRequest,
    ) -> LakeFormationGetQueryStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_query_statistics, request, LakeFormationGetQueryStatisticsResponse)

    async def get_rls_policy(
        self,
        request: LakeFormationGetRLSPolicyRequest,
    ) -> LakeFormationGetRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_rls_policy, request, LakeFormationGetRLSPolicyResponse)

    async def get_resource_lf_tags(
        self,
        request: LakeFormationGetResourceLFTagsRequest,
    ) -> LakeFormationGetResourceLFTagsResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_lf_tags, request, LakeFormationGetResourceLFTagsResponse)

    async def get_table_objects(
        self,
        request: LakeFormationGetTableObjectsRequest,
    ) -> LakeFormationGetTableObjectsResponse:
        client = self._require_client()
        return await self._execute(client.get_table_objects, request, LakeFormationGetTableObjectsResponse)

    async def get_temporary_data_location_credentials(
        self,
        request: LakeFormationGetTemporaryDataLocationCredentialsRequest | None = None,
    ) -> LakeFormationGetTemporaryDataLocationCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_temporary_data_location_credentials, request, LakeFormationGetTemporaryDataLocationCredentialsResponse)

    async def get_temporary_glue_function_credentials(
        self,
        request: LakeFormationGetTemporaryGlueFunctionCredentialsRequest,
    ) -> LakeFormationGetTemporaryGlueFunctionCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_temporary_glue_function_credentials, request, LakeFormationGetTemporaryGlueFunctionCredentialsResponse)

    async def get_temporary_glue_partition_credentials(
        self,
        request: LakeFormationGetTemporaryGluePartitionCredentialsRequest,
    ) -> LakeFormationGetTemporaryGluePartitionCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_temporary_glue_partition_credentials, request, LakeFormationGetTemporaryGluePartitionCredentialsResponse)

    async def get_temporary_glue_table_credentials(
        self,
        request: LakeFormationGetTemporaryGlueTableCredentialsRequest,
    ) -> LakeFormationGetTemporaryGlueTableCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_temporary_glue_table_credentials, request, LakeFormationGetTemporaryGlueTableCredentialsResponse)

    async def get_work_unit_results(
        self,
        request: LakeFormationGetWorkUnitResultsRequest,
    ) -> LakeFormationGetWorkUnitResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_work_unit_results, request, LakeFormationGetWorkUnitResultsResponse)

    async def get_work_units(
        self,
        request: LakeFormationGetWorkUnitsRequest,
    ) -> LakeFormationGetWorkUnitsResponse:
        client = self._require_client()
        return await self._execute(client.get_work_units, request, LakeFormationGetWorkUnitsResponse)

    async def get_work_units_paginated(
        self,
        request: LakeFormationGetWorkUnitsRequest,
    ) -> list[LakeFormationGetWorkUnitsResponse]:
        return await self._paginate('get_work_units', request, LakeFormationGetWorkUnitsResponse)

    async def grant_permissions(
        self,
        request: LakeFormationGrantPermissionsRequest,
    ) -> LakeFormationGrantPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.grant_permissions, request, LakeFormationGrantPermissionsResponse)

    async def list_data_cells_filter(
        self,
        request: LakeFormationListDataCellsFilterRequest | None = None,
    ) -> LakeFormationListDataCellsFilterResponse:
        client = self._require_client()
        return await self._execute(client.list_data_cells_filter, request, LakeFormationListDataCellsFilterResponse)

    async def list_data_cells_filter_paginated(
        self,
        request: LakeFormationListDataCellsFilterRequest | None = None,
    ) -> list[LakeFormationListDataCellsFilterResponse]:
        return await self._paginate('list_data_cells_filter', request, LakeFormationListDataCellsFilterResponse)

    async def list_lf_tag_expressions(
        self,
        request: LakeFormationListLFTagExpressionsRequest | None = None,
    ) -> LakeFormationListLFTagExpressionsResponse:
        client = self._require_client()
        return await self._execute(client.list_lf_tag_expressions, request, LakeFormationListLFTagExpressionsResponse)

    async def list_lf_tag_expressions_paginated(
        self,
        request: LakeFormationListLFTagExpressionsRequest | None = None,
    ) -> list[LakeFormationListLFTagExpressionsResponse]:
        return await self._paginate('list_lf_tag_expressions', request, LakeFormationListLFTagExpressionsResponse)

    async def list_lf_tags(
        self,
        request: LakeFormationListLFTagsRequest | None = None,
    ) -> LakeFormationListLFTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_lf_tags, request, LakeFormationListLFTagsResponse)

    async def list_lf_tags_paginated(
        self,
        request: LakeFormationListLFTagsRequest | None = None,
    ) -> list[LakeFormationListLFTagsResponse]:
        return await self._paginate('list_lf_tags', request, LakeFormationListLFTagsResponse)

    async def list_lake_formation_opt_ins(
        self,
        request: LakeFormationListLakeFormationOptInsRequest | None = None,
    ) -> LakeFormationListLakeFormationOptInsResponse:
        client = self._require_client()
        return await self._execute(client.list_lake_formation_opt_ins, request, LakeFormationListLakeFormationOptInsResponse)

    async def list_permissions(
        self,
        request: LakeFormationListPermissionsRequest | None = None,
    ) -> LakeFormationListPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.list_permissions, request, LakeFormationListPermissionsResponse)

    async def list_rls_policies(
        self,
        request: LakeFormationListRLSPoliciesRequest | None = None,
    ) -> LakeFormationListRLSPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_rls_policies, request, LakeFormationListRLSPoliciesResponse)

    async def list_rls_policies_paginated(
        self,
        request: LakeFormationListRLSPoliciesRequest | None = None,
    ) -> list[LakeFormationListRLSPoliciesResponse]:
        return await self._paginate('list_rls_policies', request, LakeFormationListRLSPoliciesResponse)

    async def list_rls_policy_attachments(
        self,
        request: LakeFormationListRLSPolicyAttachmentsRequest | None = None,
    ) -> LakeFormationListRLSPolicyAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_rls_policy_attachments, request, LakeFormationListRLSPolicyAttachmentsResponse)

    async def list_rls_policy_attachments_paginated(
        self,
        request: LakeFormationListRLSPolicyAttachmentsRequest | None = None,
    ) -> list[LakeFormationListRLSPolicyAttachmentsResponse]:
        return await self._paginate('list_rls_policy_attachments', request, LakeFormationListRLSPolicyAttachmentsResponse)

    async def list_resources(
        self,
        request: LakeFormationListResourcesRequest | None = None,
    ) -> LakeFormationListResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_resources, request, LakeFormationListResourcesResponse)

    async def list_table_storage_optimizers(
        self,
        request: LakeFormationListTableStorageOptimizersRequest,
    ) -> LakeFormationListTableStorageOptimizersResponse:
        client = self._require_client()
        return await self._execute(client.list_table_storage_optimizers, request, LakeFormationListTableStorageOptimizersResponse)

    async def list_transactions(
        self,
        request: LakeFormationListTransactionsRequest | None = None,
    ) -> LakeFormationListTransactionsResponse:
        client = self._require_client()
        return await self._execute(client.list_transactions, request, LakeFormationListTransactionsResponse)

    async def put_data_lake_settings(
        self,
        request: LakeFormationPutDataLakeSettingsRequest,
    ) -> LakeFormationPutDataLakeSettingsResponse:
        client = self._require_client()
        return await self._execute(client.put_data_lake_settings, request, LakeFormationPutDataLakeSettingsResponse)

    async def register_resource(
        self,
        request: LakeFormationRegisterResourceRequest,
    ) -> LakeFormationRegisterResourceResponse:
        client = self._require_client()
        return await self._execute(client.register_resource, request, LakeFormationRegisterResourceResponse)

    async def remove_lf_tags_from_resource(
        self,
        request: LakeFormationRemoveLFTagsFromResourceRequest,
    ) -> LakeFormationRemoveLFTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_lf_tags_from_resource, request, LakeFormationRemoveLFTagsFromResourceResponse)

    async def revoke_permissions(
        self,
        request: LakeFormationRevokePermissionsRequest,
    ) -> LakeFormationRevokePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.revoke_permissions, request, LakeFormationRevokePermissionsResponse)

    async def search_databases_by_lf_tags(
        self,
        request: LakeFormationSearchDatabasesByLFTagsRequest,
    ) -> LakeFormationSearchDatabasesByLFTagsResponse:
        client = self._require_client()
        return await self._execute(client.search_databases_by_lf_tags, request, LakeFormationSearchDatabasesByLFTagsResponse)

    async def search_databases_by_lf_tags_paginated(
        self,
        request: LakeFormationSearchDatabasesByLFTagsRequest,
    ) -> list[LakeFormationSearchDatabasesByLFTagsResponse]:
        return await self._paginate('search_databases_by_lf_tags', request, LakeFormationSearchDatabasesByLFTagsResponse)

    async def search_tables_by_lf_tags(
        self,
        request: LakeFormationSearchTablesByLFTagsRequest,
    ) -> LakeFormationSearchTablesByLFTagsResponse:
        client = self._require_client()
        return await self._execute(client.search_tables_by_lf_tags, request, LakeFormationSearchTablesByLFTagsResponse)

    async def search_tables_by_lf_tags_paginated(
        self,
        request: LakeFormationSearchTablesByLFTagsRequest,
    ) -> list[LakeFormationSearchTablesByLFTagsResponse]:
        return await self._paginate('search_tables_by_lf_tags', request, LakeFormationSearchTablesByLFTagsResponse)

    async def start_query_planning(
        self,
        request: LakeFormationStartQueryPlanningRequest,
    ) -> LakeFormationStartQueryPlanningResponse:
        client = self._require_client()
        return await self._execute(client.start_query_planning, request, LakeFormationStartQueryPlanningResponse)

    async def start_transaction(
        self,
        request: LakeFormationStartTransactionRequest | None = None,
    ) -> LakeFormationStartTransactionResponse:
        client = self._require_client()
        return await self._execute(client.start_transaction, request, LakeFormationStartTransactionResponse)

    async def update_data_cells_filter(
        self,
        request: LakeFormationUpdateDataCellsFilterRequest,
    ) -> LakeFormationUpdateDataCellsFilterResponse:
        client = self._require_client()
        return await self._execute(client.update_data_cells_filter, request, LakeFormationUpdateDataCellsFilterResponse)

    async def update_lf_tag(
        self,
        request: LakeFormationUpdateLFTagRequest,
    ) -> LakeFormationUpdateLFTagResponse:
        client = self._require_client()
        return await self._execute(client.update_lf_tag, request, LakeFormationUpdateLFTagResponse)

    async def update_lf_tag_expression(
        self,
        request: LakeFormationUpdateLFTagExpressionRequest,
    ) -> LakeFormationUpdateLFTagExpressionResponse:
        client = self._require_client()
        return await self._execute(client.update_lf_tag_expression, request, LakeFormationUpdateLFTagExpressionResponse)

    async def update_lake_formation_identity_center_configuration(
        self,
        request: LakeFormationUpdateLakeFormationIdentityCenterConfigurationRequest | None = None,
    ) -> LakeFormationUpdateLakeFormationIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_lake_formation_identity_center_configuration, request, LakeFormationUpdateLakeFormationIdentityCenterConfigurationResponse)

    async def update_rls_policy(
        self,
        request: LakeFormationUpdateRLSPolicyRequest,
    ) -> LakeFormationUpdateRLSPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_rls_policy, request, LakeFormationUpdateRLSPolicyResponse)

    async def update_resource(
        self,
        request: LakeFormationUpdateResourceRequest,
    ) -> LakeFormationUpdateResourceResponse:
        client = self._require_client()
        return await self._execute(client.update_resource, request, LakeFormationUpdateResourceResponse)

    async def update_table_objects(
        self,
        request: LakeFormationUpdateTableObjectsRequest,
    ) -> LakeFormationUpdateTableObjectsResponse:
        client = self._require_client()
        return await self._execute(client.update_table_objects, request, LakeFormationUpdateTableObjectsResponse)

    async def update_table_storage_optimizer(
        self,
        request: LakeFormationUpdateTableStorageOptimizerRequest,
    ) -> LakeFormationUpdateTableStorageOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.update_table_storage_optimizer, request, LakeFormationUpdateTableStorageOptimizerResponse)
