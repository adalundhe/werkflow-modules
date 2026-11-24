from werkflow_aws.models.datazone import (
    DataZoneAcceptPredictionsRequest,
    DataZoneAcceptPredictionsResponse,
    DataZoneAcceptSubscriptionRequestRequest,
    DataZoneAcceptSubscriptionRequestResponse,
    DataZoneAddEntityOwnerRequest,
    DataZoneAddEntityOwnerResponse,
    DataZoneAddPolicyGrantRequest,
    DataZoneAddPolicyGrantResponse,
    DataZoneAssociateEnvironmentRoleRequest,
    DataZoneAssociateEnvironmentRoleResponse,
    DataZoneAssociateGovernedTermsRequest,
    DataZoneAssociateGovernedTermsResponse,
    DataZoneBatchGetAttributesMetadataRequest,
    DataZoneBatchGetAttributesMetadataResponse,
    DataZoneBatchPutAttributesMetadataRequest,
    DataZoneBatchPutAttributesMetadataResponse,
    DataZoneCancelMetadataGenerationRunRequest,
    DataZoneCancelMetadataGenerationRunResponse,
    DataZoneCancelSubscriptionRequest,
    DataZoneCancelSubscriptionResponse,
    DataZoneCreateAccountPoolRequest,
    DataZoneCreateAccountPoolResponse,
    DataZoneCreateAssetFilterRequest,
    DataZoneCreateAssetFilterResponse,
    DataZoneCreateAssetRequest,
    DataZoneCreateAssetResponse,
    DataZoneCreateAssetRevisionRequest,
    DataZoneCreateAssetRevisionResponse,
    DataZoneCreateAssetTypeRequest,
    DataZoneCreateAssetTypeResponse,
    DataZoneCreateConnectionRequest,
    DataZoneCreateConnectionResponse,
    DataZoneCreateDataProductRequest,
    DataZoneCreateDataProductResponse,
    DataZoneCreateDataProductRevisionRequest,
    DataZoneCreateDataProductRevisionResponse,
    DataZoneCreateDataSourceRequest,
    DataZoneCreateDataSourceResponse,
    DataZoneCreateDesignationRequest,
    DataZoneCreateDesignationResponse,
    DataZoneCreateDomainRequest,
    DataZoneCreateDomainResponse,
    DataZoneCreateDomainUnitRequest,
    DataZoneCreateDomainUnitResponse,
    DataZoneCreateEnvironmentActionRequest,
    DataZoneCreateEnvironmentActionResponse,
    DataZoneCreateEnvironmentBlueprintRequest,
    DataZoneCreateEnvironmentBlueprintResponse,
    DataZoneCreateEnvironmentProfileRequest,
    DataZoneCreateEnvironmentProfileResponse,
    DataZoneCreateEnvironmentRequest,
    DataZoneCreateEnvironmentResponse,
    DataZoneCreateFormTypeRequest,
    DataZoneCreateFormTypeResponse,
    DataZoneCreateGlossaryRequest,
    DataZoneCreateGlossaryResponse,
    DataZoneCreateGlossaryTermRequest,
    DataZoneCreateGlossaryTermResponse,
    DataZoneCreateGroupProfileRequest,
    DataZoneCreateGroupProfileResponse,
    DataZoneCreateListingChangeSetRequest,
    DataZoneCreateListingChangeSetResponse,
    DataZoneCreateNotebookRequest,
    DataZoneCreateNotebookResponse,
    DataZoneCreateProjectMembershipRequest,
    DataZoneCreateProjectMembershipResponse,
    DataZoneCreateProjectProfileRequest,
    DataZoneCreateProjectProfileResponse,
    DataZoneCreateProjectRequest,
    DataZoneCreateProjectResponse,
    DataZoneCreateRuleRequest,
    DataZoneCreateRuleResponse,
    DataZoneCreateSubscriptionGrantRequest,
    DataZoneCreateSubscriptionGrantResponse,
    DataZoneCreateSubscriptionRequestRequest,
    DataZoneCreateSubscriptionRequestResponse,
    DataZoneCreateSubscriptionTargetRequest,
    DataZoneCreateSubscriptionTargetResponse,
    DataZoneCreateUserProfileRequest,
    DataZoneCreateUserProfileResponse,
    DataZoneDeleteAccountPoolRequest,
    DataZoneDeleteAccountPoolResponse,
    DataZoneDeleteAssetFilterRequest,
    DataZoneDeleteAssetFilterResponse,
    DataZoneDeleteAssetRequest,
    DataZoneDeleteAssetResponse,
    DataZoneDeleteAssetTypeRequest,
    DataZoneDeleteAssetTypeResponse,
    DataZoneDeleteConnectionRequest,
    DataZoneDeleteConnectionResponse,
    DataZoneDeleteDataExportConfigurationRequest,
    DataZoneDeleteDataExportConfigurationResponse,
    DataZoneDeleteDataProductRequest,
    DataZoneDeleteDataProductResponse,
    DataZoneDeleteDataSourceRequest,
    DataZoneDeleteDataSourceResponse,
    DataZoneDeleteDesignationRequest,
    DataZoneDeleteDesignationResponse,
    DataZoneDeleteDomainRequest,
    DataZoneDeleteDomainResponse,
    DataZoneDeleteDomainUnitRequest,
    DataZoneDeleteDomainUnitResponse,
    DataZoneDeleteEnvironmentActionRequest,
    DataZoneDeleteEnvironmentActionResponse,
    DataZoneDeleteEnvironmentBlueprintConfigurationRequest,
    DataZoneDeleteEnvironmentBlueprintConfigurationResponse,
    DataZoneDeleteEnvironmentBlueprintRequest,
    DataZoneDeleteEnvironmentBlueprintResponse,
    DataZoneDeleteEnvironmentProfileRequest,
    DataZoneDeleteEnvironmentProfileResponse,
    DataZoneDeleteEnvironmentRequest,
    DataZoneDeleteEnvironmentResponse,
    DataZoneDeleteFormTypeRequest,
    DataZoneDeleteFormTypeResponse,
    DataZoneDeleteGlossaryRequest,
    DataZoneDeleteGlossaryResponse,
    DataZoneDeleteGlossaryTermRequest,
    DataZoneDeleteGlossaryTermResponse,
    DataZoneDeleteLineageEventRequest,
    DataZoneDeleteLineageEventResponse,
    DataZoneDeleteListingRequest,
    DataZoneDeleteListingResponse,
    DataZoneDeleteNotebookRequest,
    DataZoneDeleteNotebookResponse,
    DataZoneDeleteProjectMembershipRequest,
    DataZoneDeleteProjectMembershipResponse,
    DataZoneDeleteProjectProfileRequest,
    DataZoneDeleteProjectProfileResponse,
    DataZoneDeleteProjectRequest,
    DataZoneDeleteProjectResponse,
    DataZoneDeleteRuleRequest,
    DataZoneDeleteRuleResponse,
    DataZoneDeleteSubscriptionGrantRequest,
    DataZoneDeleteSubscriptionGrantResponse,
    DataZoneDeleteSubscriptionRequestRequest,
    DataZoneDeleteSubscriptionRequestResponse,
    DataZoneDeleteSubscriptionTargetRequest,
    DataZoneDeleteSubscriptionTargetResponse,
    DataZoneDeleteTimeSeriesDataPointsRequest,
    DataZoneDeleteTimeSeriesDataPointsResponse,
    DataZoneDisassociateEnvironmentRoleRequest,
    DataZoneDisassociateEnvironmentRoleResponse,
    DataZoneDisassociateGovernedTermsRequest,
    DataZoneDisassociateGovernedTermsResponse,
    DataZoneGetAccountPoolRequest,
    DataZoneGetAccountPoolResponse,
    DataZoneGetAssetFilterRequest,
    DataZoneGetAssetFilterResponse,
    DataZoneGetAssetRequest,
    DataZoneGetAssetResponse,
    DataZoneGetAssetTypeRequest,
    DataZoneGetAssetTypeResponse,
    DataZoneGetConnectionRequest,
    DataZoneGetConnectionResponse,
    DataZoneGetDataExportConfigurationRequest,
    DataZoneGetDataExportConfigurationResponse,
    DataZoneGetDataProductRequest,
    DataZoneGetDataProductResponse,
    DataZoneGetDataSourceRequest,
    DataZoneGetDataSourceResponse,
    DataZoneGetDataSourceRunRequest,
    DataZoneGetDataSourceRunResponse,
    DataZoneGetDesignationRequest,
    DataZoneGetDesignationResponse,
    DataZoneGetDomainRequest,
    DataZoneGetDomainResponse,
    DataZoneGetDomainUnitRequest,
    DataZoneGetDomainUnitResponse,
    DataZoneGetEnvironmentActionRequest,
    DataZoneGetEnvironmentActionResponse,
    DataZoneGetEnvironmentBlueprintConfigurationRequest,
    DataZoneGetEnvironmentBlueprintConfigurationResponse,
    DataZoneGetEnvironmentBlueprintRequest,
    DataZoneGetEnvironmentBlueprintResponse,
    DataZoneGetEnvironmentCredentialsRequest,
    DataZoneGetEnvironmentCredentialsResponse,
    DataZoneGetEnvironmentProfileRequest,
    DataZoneGetEnvironmentProfileResponse,
    DataZoneGetEnvironmentRequest,
    DataZoneGetEnvironmentResponse,
    DataZoneGetFormTypeRequest,
    DataZoneGetFormTypeResponse,
    DataZoneGetGlossaryRequest,
    DataZoneGetGlossaryResponse,
    DataZoneGetGlossaryTermRequest,
    DataZoneGetGlossaryTermResponse,
    DataZoneGetGroupProfileRequest,
    DataZoneGetGroupProfileResponse,
    DataZoneGetIamPortalLoginUrlRequest,
    DataZoneGetIamPortalLoginUrlResponse,
    DataZoneGetJobRunRequest,
    DataZoneGetJobRunResponse,
    DataZoneGetLineageEventRequest,
    DataZoneGetLineageEventResponse,
    DataZoneGetLineageNodeRequest,
    DataZoneGetLineageNodeResponse,
    DataZoneGetListingRequest,
    DataZoneGetListingResponse,
    DataZoneGetMetadataGenerationRunRequest,
    DataZoneGetMetadataGenerationRunResponse,
    DataZoneGetNotebookExportRequest,
    DataZoneGetNotebookExportResponse,
    DataZoneGetNotebookRequest,
    DataZoneGetNotebookResponse,
    DataZoneGetNotebookRunRequest,
    DataZoneGetNotebookRunResponse,
    DataZoneGetProjectProfileRequest,
    DataZoneGetProjectProfileResponse,
    DataZoneGetProjectRequest,
    DataZoneGetProjectResponse,
    DataZoneGetRuleRequest,
    DataZoneGetRuleResponse,
    DataZoneGetSubscriptionGrantRequest,
    DataZoneGetSubscriptionGrantResponse,
    DataZoneGetSubscriptionRequest,
    DataZoneGetSubscriptionRequestDetailsRequest,
    DataZoneGetSubscriptionRequestDetailsResponse,
    DataZoneGetSubscriptionResponse,
    DataZoneGetSubscriptionTargetRequest,
    DataZoneGetSubscriptionTargetResponse,
    DataZoneGetTimeSeriesDataPointRequest,
    DataZoneGetTimeSeriesDataPointResponse,
    DataZoneGetUserProfileRequest,
    DataZoneGetUserProfileResponse,
    DataZoneListAccountPoolsRequest,
    DataZoneListAccountPoolsResponse,
    DataZoneListAccountsInAccountPoolRequest,
    DataZoneListAccountsInAccountPoolResponse,
    DataZoneListAssetFiltersRequest,
    DataZoneListAssetFiltersResponse,
    DataZoneListAssetRevisionsRequest,
    DataZoneListAssetRevisionsResponse,
    DataZoneListConnectionsRequest,
    DataZoneListConnectionsResponse,
    DataZoneListDataProductRevisionsRequest,
    DataZoneListDataProductRevisionsResponse,
    DataZoneListDataSourceRunActivitiesRequest,
    DataZoneListDataSourceRunActivitiesResponse,
    DataZoneListDataSourceRunsRequest,
    DataZoneListDataSourceRunsResponse,
    DataZoneListDataSourcesRequest,
    DataZoneListDataSourcesResponse,
    DataZoneListDesignationsRequest,
    DataZoneListDesignationsResponse,
    DataZoneListDomainUnitsForParentRequest,
    DataZoneListDomainUnitsForParentResponse,
    DataZoneListDomainsRequest,
    DataZoneListDomainsResponse,
    DataZoneListEntityOwnersRequest,
    DataZoneListEntityOwnersResponse,
    DataZoneListEnvironmentActionsRequest,
    DataZoneListEnvironmentActionsResponse,
    DataZoneListEnvironmentBlueprintConfigurationsRequest,
    DataZoneListEnvironmentBlueprintConfigurationsResponse,
    DataZoneListEnvironmentBlueprintsRequest,
    DataZoneListEnvironmentBlueprintsResponse,
    DataZoneListEnvironmentProfilesRequest,
    DataZoneListEnvironmentProfilesResponse,
    DataZoneListEnvironmentsRequest,
    DataZoneListEnvironmentsResponse,
    DataZoneListJobRunsRequest,
    DataZoneListJobRunsResponse,
    DataZoneListLineageEventsRequest,
    DataZoneListLineageEventsResponse,
    DataZoneListLineageNodeHistoryRequest,
    DataZoneListLineageNodeHistoryResponse,
    DataZoneListMetadataGenerationRunsRequest,
    DataZoneListMetadataGenerationRunsResponse,
    DataZoneListNotebookRunsRequest,
    DataZoneListNotebookRunsResponse,
    DataZoneListNotebooksRequest,
    DataZoneListNotebooksResponse,
    DataZoneListNotificationsRequest,
    DataZoneListNotificationsResponse,
    DataZoneListPolicyGrantsRequest,
    DataZoneListPolicyGrantsResponse,
    DataZoneListProjectMembershipsRequest,
    DataZoneListProjectMembershipsResponse,
    DataZoneListProjectProfilesRequest,
    DataZoneListProjectProfilesResponse,
    DataZoneListProjectsRequest,
    DataZoneListProjectsResponse,
    DataZoneListRulesRequest,
    DataZoneListRulesResponse,
    DataZoneListSubscriptionGrantsRequest,
    DataZoneListSubscriptionGrantsResponse,
    DataZoneListSubscriptionRequestsRequest,
    DataZoneListSubscriptionRequestsResponse,
    DataZoneListSubscriptionTargetsRequest,
    DataZoneListSubscriptionTargetsResponse,
    DataZoneListSubscriptionsRequest,
    DataZoneListSubscriptionsResponse,
    DataZoneListTagsForResourceRequest,
    DataZoneListTagsForResourceResponse,
    DataZoneListTimeSeriesDataPointsRequest,
    DataZoneListTimeSeriesDataPointsResponse,
    DataZonePostLineageEventRequest,
    DataZonePostLineageEventResponse,
    DataZonePostTimeSeriesDataPointsRequest,
    DataZonePostTimeSeriesDataPointsResponse,
    DataZonePutDataExportConfigurationRequest,
    DataZonePutDataExportConfigurationResponse,
    DataZonePutEnvironmentBlueprintConfigurationRequest,
    DataZonePutEnvironmentBlueprintConfigurationResponse,
    DataZoneQueryGraphRequest,
    DataZoneQueryGraphResponse,
    DataZoneRejectPredictionsRequest,
    DataZoneRejectPredictionsResponse,
    DataZoneRejectSubscriptionRequestRequest,
    DataZoneRejectSubscriptionRequestResponse,
    DataZoneRemoveEntityOwnerRequest,
    DataZoneRemoveEntityOwnerResponse,
    DataZoneRemovePolicyGrantRequest,
    DataZoneRemovePolicyGrantResponse,
    DataZoneRevokeSubscriptionRequest,
    DataZoneRevokeSubscriptionResponse,
    DataZoneSearchGroupProfilesRequest,
    DataZoneSearchGroupProfilesResponse,
    DataZoneSearchListingsRequest,
    DataZoneSearchListingsResponse,
    DataZoneSearchRequest,
    DataZoneSearchResponse,
    DataZoneSearchTypesRequest,
    DataZoneSearchTypesResponse,
    DataZoneSearchUserProfilesRequest,
    DataZoneSearchUserProfilesResponse,
    DataZoneStartDataSourceRunRequest,
    DataZoneStartDataSourceRunResponse,
    DataZoneStartMetadataGenerationRunRequest,
    DataZoneStartMetadataGenerationRunResponse,
    DataZoneStartNotebookExportRequest,
    DataZoneStartNotebookExportResponse,
    DataZoneStartNotebookImportRequest,
    DataZoneStartNotebookImportResponse,
    DataZoneStartNotebookRunRequest,
    DataZoneStartNotebookRunResponse,
    DataZoneStartNotebookSyncRequest,
    DataZoneStartNotebookSyncResponse,
    DataZoneStopNotebookRunRequest,
    DataZoneStopNotebookRunResponse,
    DataZoneTagResourceRequest,
    DataZoneTagResourceResponse,
    DataZoneUntagResourceRequest,
    DataZoneUntagResourceResponse,
    DataZoneUpdateAccountPoolRequest,
    DataZoneUpdateAccountPoolResponse,
    DataZoneUpdateAssetFilterRequest,
    DataZoneUpdateAssetFilterResponse,
    DataZoneUpdateAssetOwnerRequest,
    DataZoneUpdateAssetOwnerResponse,
    DataZoneUpdateConnectionRequest,
    DataZoneUpdateConnectionResponse,
    DataZoneUpdateDataSourceRequest,
    DataZoneUpdateDataSourceResponse,
    DataZoneUpdateDesignationRequest,
    DataZoneUpdateDesignationResponse,
    DataZoneUpdateDomainRequest,
    DataZoneUpdateDomainResponse,
    DataZoneUpdateDomainUnitRequest,
    DataZoneUpdateDomainUnitResponse,
    DataZoneUpdateEnvironmentActionRequest,
    DataZoneUpdateEnvironmentActionResponse,
    DataZoneUpdateEnvironmentBlueprintRequest,
    DataZoneUpdateEnvironmentBlueprintResponse,
    DataZoneUpdateEnvironmentProfileRequest,
    DataZoneUpdateEnvironmentProfileResponse,
    DataZoneUpdateEnvironmentRequest,
    DataZoneUpdateEnvironmentResponse,
    DataZoneUpdateGlossaryRequest,
    DataZoneUpdateGlossaryResponse,
    DataZoneUpdateGlossaryTermRequest,
    DataZoneUpdateGlossaryTermResponse,
    DataZoneUpdateGroupProfileRequest,
    DataZoneUpdateGroupProfileResponse,
    DataZoneUpdateNotebookRequest,
    DataZoneUpdateNotebookResponse,
    DataZoneUpdateProjectProfileRequest,
    DataZoneUpdateProjectProfileResponse,
    DataZoneUpdateProjectRequest,
    DataZoneUpdateProjectResponse,
    DataZoneUpdateRootDomainUnitOwnerRequest,
    DataZoneUpdateRootDomainUnitOwnerResponse,
    DataZoneUpdateRuleRequest,
    DataZoneUpdateRuleResponse,
    DataZoneUpdateSubscriptionGrantStatusRequest,
    DataZoneUpdateSubscriptionGrantStatusResponse,
    DataZoneUpdateSubscriptionRequestRequest,
    DataZoneUpdateSubscriptionRequestResponse,
    DataZoneUpdateSubscriptionTargetRequest,
    DataZoneUpdateSubscriptionTargetResponse,
    DataZoneUpdateUserProfileRequest,
    DataZoneUpdateUserProfileResponse,
)
from werkflow_aws.types.datazone_client import DataZoneClient
from .base import AWSBaseService


class AWSDataZone(AWSBaseService[DataZoneClient]):
    service_name = 'datazone'
    boto3_service_name = 'datazone'

    def __init__(self) -> None:
        super().__init__(service_name='datazone', boto3_service_name='datazone')

    async def accept_predictions(
        self,
        request: DataZoneAcceptPredictionsRequest,
    ) -> DataZoneAcceptPredictionsResponse:
        client = self._require_client()
        return await self._execute(client.accept_predictions, request, DataZoneAcceptPredictionsResponse)

    async def accept_subscription_request(
        self,
        request: DataZoneAcceptSubscriptionRequestRequest,
    ) -> DataZoneAcceptSubscriptionRequestResponse:
        client = self._require_client()
        return await self._execute(client.accept_subscription_request, request, DataZoneAcceptSubscriptionRequestResponse)

    async def add_entity_owner(
        self,
        request: DataZoneAddEntityOwnerRequest,
    ) -> DataZoneAddEntityOwnerResponse:
        client = self._require_client()
        return await self._execute(client.add_entity_owner, request, DataZoneAddEntityOwnerResponse)

    async def add_policy_grant(
        self,
        request: DataZoneAddPolicyGrantRequest,
    ) -> DataZoneAddPolicyGrantResponse:
        client = self._require_client()
        return await self._execute(client.add_policy_grant, request, DataZoneAddPolicyGrantResponse)

    async def associate_environment_role(
        self,
        request: DataZoneAssociateEnvironmentRoleRequest,
    ) -> DataZoneAssociateEnvironmentRoleResponse:
        client = self._require_client()
        return await self._execute(client.associate_environment_role, request, DataZoneAssociateEnvironmentRoleResponse)

    async def associate_governed_terms(
        self,
        request: DataZoneAssociateGovernedTermsRequest,
    ) -> DataZoneAssociateGovernedTermsResponse:
        client = self._require_client()
        return await self._execute(client.associate_governed_terms, request, DataZoneAssociateGovernedTermsResponse)

    async def batch_get_attributes_metadata(
        self,
        request: DataZoneBatchGetAttributesMetadataRequest,
    ) -> DataZoneBatchGetAttributesMetadataResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_attributes_metadata, request, DataZoneBatchGetAttributesMetadataResponse)

    async def batch_put_attributes_metadata(
        self,
        request: DataZoneBatchPutAttributesMetadataRequest,
    ) -> DataZoneBatchPutAttributesMetadataResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_attributes_metadata, request, DataZoneBatchPutAttributesMetadataResponse)

    async def cancel_metadata_generation_run(
        self,
        request: DataZoneCancelMetadataGenerationRunRequest,
    ) -> DataZoneCancelMetadataGenerationRunResponse:
        client = self._require_client()
        return await self._execute(client.cancel_metadata_generation_run, request, DataZoneCancelMetadataGenerationRunResponse)

    async def cancel_subscription(
        self,
        request: DataZoneCancelSubscriptionRequest,
    ) -> DataZoneCancelSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_subscription, request, DataZoneCancelSubscriptionResponse)

    async def create_account_pool(
        self,
        request: DataZoneCreateAccountPoolRequest,
    ) -> DataZoneCreateAccountPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_account_pool, request, DataZoneCreateAccountPoolResponse)

    async def create_asset(
        self,
        request: DataZoneCreateAssetRequest,
    ) -> DataZoneCreateAssetResponse:
        client = self._require_client()
        return await self._execute(client.create_asset, request, DataZoneCreateAssetResponse)

    async def create_asset_filter(
        self,
        request: DataZoneCreateAssetFilterRequest,
    ) -> DataZoneCreateAssetFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_asset_filter, request, DataZoneCreateAssetFilterResponse)

    async def create_asset_revision(
        self,
        request: DataZoneCreateAssetRevisionRequest,
    ) -> DataZoneCreateAssetRevisionResponse:
        client = self._require_client()
        return await self._execute(client.create_asset_revision, request, DataZoneCreateAssetRevisionResponse)

    async def create_asset_type(
        self,
        request: DataZoneCreateAssetTypeRequest,
    ) -> DataZoneCreateAssetTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_asset_type, request, DataZoneCreateAssetTypeResponse)

    async def create_connection(
        self,
        request: DataZoneCreateConnectionRequest,
    ) -> DataZoneCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, DataZoneCreateConnectionResponse)

    async def create_data_product(
        self,
        request: DataZoneCreateDataProductRequest,
    ) -> DataZoneCreateDataProductResponse:
        client = self._require_client()
        return await self._execute(client.create_data_product, request, DataZoneCreateDataProductResponse)

    async def create_data_product_revision(
        self,
        request: DataZoneCreateDataProductRevisionRequest,
    ) -> DataZoneCreateDataProductRevisionResponse:
        client = self._require_client()
        return await self._execute(client.create_data_product_revision, request, DataZoneCreateDataProductRevisionResponse)

    async def create_data_source(
        self,
        request: DataZoneCreateDataSourceRequest,
    ) -> DataZoneCreateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_data_source, request, DataZoneCreateDataSourceResponse)

    async def create_designation(
        self,
        request: DataZoneCreateDesignationRequest,
    ) -> DataZoneCreateDesignationResponse:
        client = self._require_client()
        return await self._execute(client.create_designation, request, DataZoneCreateDesignationResponse)

    async def create_domain(
        self,
        request: DataZoneCreateDomainRequest,
    ) -> DataZoneCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, DataZoneCreateDomainResponse)

    async def create_domain_unit(
        self,
        request: DataZoneCreateDomainUnitRequest,
    ) -> DataZoneCreateDomainUnitResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_unit, request, DataZoneCreateDomainUnitResponse)

    async def create_environment(
        self,
        request: DataZoneCreateEnvironmentRequest,
    ) -> DataZoneCreateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_environment, request, DataZoneCreateEnvironmentResponse)

    async def create_environment_action(
        self,
        request: DataZoneCreateEnvironmentActionRequest,
    ) -> DataZoneCreateEnvironmentActionResponse:
        client = self._require_client()
        return await self._execute(client.create_environment_action, request, DataZoneCreateEnvironmentActionResponse)

    async def create_environment_blueprint(
        self,
        request: DataZoneCreateEnvironmentBlueprintRequest,
    ) -> DataZoneCreateEnvironmentBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.create_environment_blueprint, request, DataZoneCreateEnvironmentBlueprintResponse)

    async def create_environment_profile(
        self,
        request: DataZoneCreateEnvironmentProfileRequest,
    ) -> DataZoneCreateEnvironmentProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_environment_profile, request, DataZoneCreateEnvironmentProfileResponse)

    async def create_form_type(
        self,
        request: DataZoneCreateFormTypeRequest,
    ) -> DataZoneCreateFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_form_type, request, DataZoneCreateFormTypeResponse)

    async def create_glossary(
        self,
        request: DataZoneCreateGlossaryRequest,
    ) -> DataZoneCreateGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.create_glossary, request, DataZoneCreateGlossaryResponse)

    async def create_glossary_term(
        self,
        request: DataZoneCreateGlossaryTermRequest,
    ) -> DataZoneCreateGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.create_glossary_term, request, DataZoneCreateGlossaryTermResponse)

    async def create_group_profile(
        self,
        request: DataZoneCreateGroupProfileRequest,
    ) -> DataZoneCreateGroupProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_group_profile, request, DataZoneCreateGroupProfileResponse)

    async def create_listing_change_set(
        self,
        request: DataZoneCreateListingChangeSetRequest,
    ) -> DataZoneCreateListingChangeSetResponse:
        client = self._require_client()
        return await self._execute(client.create_listing_change_set, request, DataZoneCreateListingChangeSetResponse)

    async def create_notebook(
        self,
        request: DataZoneCreateNotebookRequest,
    ) -> DataZoneCreateNotebookResponse:
        client = self._require_client()
        return await self._execute(client.create_notebook, request, DataZoneCreateNotebookResponse)

    async def create_project(
        self,
        request: DataZoneCreateProjectRequest,
    ) -> DataZoneCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, DataZoneCreateProjectResponse)

    async def create_project_membership(
        self,
        request: DataZoneCreateProjectMembershipRequest,
    ) -> DataZoneCreateProjectMembershipResponse:
        client = self._require_client()
        return await self._execute(client.create_project_membership, request, DataZoneCreateProjectMembershipResponse)

    async def create_project_profile(
        self,
        request: DataZoneCreateProjectProfileRequest,
    ) -> DataZoneCreateProjectProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_project_profile, request, DataZoneCreateProjectProfileResponse)

    async def create_rule(
        self,
        request: DataZoneCreateRuleRequest,
    ) -> DataZoneCreateRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_rule, request, DataZoneCreateRuleResponse)

    async def create_subscription_grant(
        self,
        request: DataZoneCreateSubscriptionGrantRequest,
    ) -> DataZoneCreateSubscriptionGrantResponse:
        client = self._require_client()
        return await self._execute(client.create_subscription_grant, request, DataZoneCreateSubscriptionGrantResponse)

    async def create_subscription_request(
        self,
        request: DataZoneCreateSubscriptionRequestRequest,
    ) -> DataZoneCreateSubscriptionRequestResponse:
        client = self._require_client()
        return await self._execute(client.create_subscription_request, request, DataZoneCreateSubscriptionRequestResponse)

    async def create_subscription_target(
        self,
        request: DataZoneCreateSubscriptionTargetRequest,
    ) -> DataZoneCreateSubscriptionTargetResponse:
        client = self._require_client()
        return await self._execute(client.create_subscription_target, request, DataZoneCreateSubscriptionTargetResponse)

    async def create_user_profile(
        self,
        request: DataZoneCreateUserProfileRequest,
    ) -> DataZoneCreateUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_user_profile, request, DataZoneCreateUserProfileResponse)

    async def delete_account_pool(
        self,
        request: DataZoneDeleteAccountPoolRequest,
    ) -> DataZoneDeleteAccountPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_pool, request, DataZoneDeleteAccountPoolResponse)

    async def delete_asset(
        self,
        request: DataZoneDeleteAssetRequest,
    ) -> DataZoneDeleteAssetResponse:
        client = self._require_client()
        return await self._execute(client.delete_asset, request, DataZoneDeleteAssetResponse)

    async def delete_asset_filter(
        self,
        request: DataZoneDeleteAssetFilterRequest,
    ) -> DataZoneDeleteAssetFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_asset_filter, request, DataZoneDeleteAssetFilterResponse)

    async def delete_asset_type(
        self,
        request: DataZoneDeleteAssetTypeRequest,
    ) -> DataZoneDeleteAssetTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_asset_type, request, DataZoneDeleteAssetTypeResponse)

    async def delete_connection(
        self,
        request: DataZoneDeleteConnectionRequest,
    ) -> DataZoneDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, DataZoneDeleteConnectionResponse)

    async def delete_data_export_configuration(
        self,
        request: DataZoneDeleteDataExportConfigurationRequest,
    ) -> DataZoneDeleteDataExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_export_configuration, request, DataZoneDeleteDataExportConfigurationResponse)

    async def delete_data_product(
        self,
        request: DataZoneDeleteDataProductRequest,
    ) -> DataZoneDeleteDataProductResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_product, request, DataZoneDeleteDataProductResponse)

    async def delete_data_source(
        self,
        request: DataZoneDeleteDataSourceRequest,
    ) -> DataZoneDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, DataZoneDeleteDataSourceResponse)

    async def delete_designation(
        self,
        request: DataZoneDeleteDesignationRequest,
    ) -> DataZoneDeleteDesignationResponse:
        client = self._require_client()
        return await self._execute(client.delete_designation, request, DataZoneDeleteDesignationResponse)

    async def delete_domain(
        self,
        request: DataZoneDeleteDomainRequest,
    ) -> DataZoneDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, DataZoneDeleteDomainResponse)

    async def delete_domain_unit(
        self,
        request: DataZoneDeleteDomainUnitRequest,
    ) -> DataZoneDeleteDomainUnitResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_unit, request, DataZoneDeleteDomainUnitResponse)

    async def delete_environment(
        self,
        request: DataZoneDeleteEnvironmentRequest,
    ) -> DataZoneDeleteEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment, request, DataZoneDeleteEnvironmentResponse)

    async def delete_environment_action(
        self,
        request: DataZoneDeleteEnvironmentActionRequest,
    ) -> DataZoneDeleteEnvironmentActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment_action, request, DataZoneDeleteEnvironmentActionResponse)

    async def delete_environment_blueprint(
        self,
        request: DataZoneDeleteEnvironmentBlueprintRequest,
    ) -> DataZoneDeleteEnvironmentBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment_blueprint, request, DataZoneDeleteEnvironmentBlueprintResponse)

    async def delete_environment_blueprint_configuration(
        self,
        request: DataZoneDeleteEnvironmentBlueprintConfigurationRequest,
    ) -> DataZoneDeleteEnvironmentBlueprintConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment_blueprint_configuration, request, DataZoneDeleteEnvironmentBlueprintConfigurationResponse)

    async def delete_environment_profile(
        self,
        request: DataZoneDeleteEnvironmentProfileRequest,
    ) -> DataZoneDeleteEnvironmentProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment_profile, request, DataZoneDeleteEnvironmentProfileResponse)

    async def delete_form_type(
        self,
        request: DataZoneDeleteFormTypeRequest,
    ) -> DataZoneDeleteFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_form_type, request, DataZoneDeleteFormTypeResponse)

    async def delete_glossary(
        self,
        request: DataZoneDeleteGlossaryRequest,
    ) -> DataZoneDeleteGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.delete_glossary, request, DataZoneDeleteGlossaryResponse)

    async def delete_glossary_term(
        self,
        request: DataZoneDeleteGlossaryTermRequest,
    ) -> DataZoneDeleteGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.delete_glossary_term, request, DataZoneDeleteGlossaryTermResponse)

    async def delete_lineage_event(
        self,
        request: DataZoneDeleteLineageEventRequest,
    ) -> DataZoneDeleteLineageEventResponse:
        client = self._require_client()
        return await self._execute(client.delete_lineage_event, request, DataZoneDeleteLineageEventResponse)

    async def delete_listing(
        self,
        request: DataZoneDeleteListingRequest,
    ) -> DataZoneDeleteListingResponse:
        client = self._require_client()
        return await self._execute(client.delete_listing, request, DataZoneDeleteListingResponse)

    async def delete_notebook(
        self,
        request: DataZoneDeleteNotebookRequest,
    ) -> DataZoneDeleteNotebookResponse:
        client = self._require_client()
        return await self._execute(client.delete_notebook, request, DataZoneDeleteNotebookResponse)

    async def delete_project(
        self,
        request: DataZoneDeleteProjectRequest,
    ) -> DataZoneDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, DataZoneDeleteProjectResponse)

    async def delete_project_membership(
        self,
        request: DataZoneDeleteProjectMembershipRequest,
    ) -> DataZoneDeleteProjectMembershipResponse:
        client = self._require_client()
        return await self._execute(client.delete_project_membership, request, DataZoneDeleteProjectMembershipResponse)

    async def delete_project_profile(
        self,
        request: DataZoneDeleteProjectProfileRequest,
    ) -> DataZoneDeleteProjectProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_project_profile, request, DataZoneDeleteProjectProfileResponse)

    async def delete_rule(
        self,
        request: DataZoneDeleteRuleRequest,
    ) -> DataZoneDeleteRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_rule, request, DataZoneDeleteRuleResponse)

    async def delete_subscription_grant(
        self,
        request: DataZoneDeleteSubscriptionGrantRequest,
    ) -> DataZoneDeleteSubscriptionGrantResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscription_grant, request, DataZoneDeleteSubscriptionGrantResponse)

    async def delete_subscription_request(
        self,
        request: DataZoneDeleteSubscriptionRequestRequest,
    ) -> DataZoneDeleteSubscriptionRequestResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscription_request, request, DataZoneDeleteSubscriptionRequestResponse)

    async def delete_subscription_target(
        self,
        request: DataZoneDeleteSubscriptionTargetRequest,
    ) -> DataZoneDeleteSubscriptionTargetResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscription_target, request, DataZoneDeleteSubscriptionTargetResponse)

    async def delete_time_series_data_points(
        self,
        request: DataZoneDeleteTimeSeriesDataPointsRequest,
    ) -> DataZoneDeleteTimeSeriesDataPointsResponse:
        client = self._require_client()
        return await self._execute(client.delete_time_series_data_points, request, DataZoneDeleteTimeSeriesDataPointsResponse)

    async def disassociate_environment_role(
        self,
        request: DataZoneDisassociateEnvironmentRoleRequest,
    ) -> DataZoneDisassociateEnvironmentRoleResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_environment_role, request, DataZoneDisassociateEnvironmentRoleResponse)

    async def disassociate_governed_terms(
        self,
        request: DataZoneDisassociateGovernedTermsRequest,
    ) -> DataZoneDisassociateGovernedTermsResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_governed_terms, request, DataZoneDisassociateGovernedTermsResponse)

    async def get_account_pool(
        self,
        request: DataZoneGetAccountPoolRequest,
    ) -> DataZoneGetAccountPoolResponse:
        client = self._require_client()
        return await self._execute(client.get_account_pool, request, DataZoneGetAccountPoolResponse)

    async def get_asset(
        self,
        request: DataZoneGetAssetRequest,
    ) -> DataZoneGetAssetResponse:
        client = self._require_client()
        return await self._execute(client.get_asset, request, DataZoneGetAssetResponse)

    async def get_asset_filter(
        self,
        request: DataZoneGetAssetFilterRequest,
    ) -> DataZoneGetAssetFilterResponse:
        client = self._require_client()
        return await self._execute(client.get_asset_filter, request, DataZoneGetAssetFilterResponse)

    async def get_asset_type(
        self,
        request: DataZoneGetAssetTypeRequest,
    ) -> DataZoneGetAssetTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_asset_type, request, DataZoneGetAssetTypeResponse)

    async def get_connection(
        self,
        request: DataZoneGetConnectionRequest,
    ) -> DataZoneGetConnectionResponse:
        client = self._require_client()
        return await self._execute(client.get_connection, request, DataZoneGetConnectionResponse)

    async def get_data_export_configuration(
        self,
        request: DataZoneGetDataExportConfigurationRequest,
    ) -> DataZoneGetDataExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_data_export_configuration, request, DataZoneGetDataExportConfigurationResponse)

    async def get_data_product(
        self,
        request: DataZoneGetDataProductRequest,
    ) -> DataZoneGetDataProductResponse:
        client = self._require_client()
        return await self._execute(client.get_data_product, request, DataZoneGetDataProductResponse)

    async def get_data_source(
        self,
        request: DataZoneGetDataSourceRequest,
    ) -> DataZoneGetDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source, request, DataZoneGetDataSourceResponse)

    async def get_data_source_run(
        self,
        request: DataZoneGetDataSourceRunRequest,
    ) -> DataZoneGetDataSourceRunResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source_run, request, DataZoneGetDataSourceRunResponse)

    async def get_designation(
        self,
        request: DataZoneGetDesignationRequest,
    ) -> DataZoneGetDesignationResponse:
        client = self._require_client()
        return await self._execute(client.get_designation, request, DataZoneGetDesignationResponse)

    async def get_domain(
        self,
        request: DataZoneGetDomainRequest,
    ) -> DataZoneGetDomainResponse:
        client = self._require_client()
        return await self._execute(client.get_domain, request, DataZoneGetDomainResponse)

    async def get_domain_unit(
        self,
        request: DataZoneGetDomainUnitRequest,
    ) -> DataZoneGetDomainUnitResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_unit, request, DataZoneGetDomainUnitResponse)

    async def get_environment(
        self,
        request: DataZoneGetEnvironmentRequest,
    ) -> DataZoneGetEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_environment, request, DataZoneGetEnvironmentResponse)

    async def get_environment_action(
        self,
        request: DataZoneGetEnvironmentActionRequest,
    ) -> DataZoneGetEnvironmentActionResponse:
        client = self._require_client()
        return await self._execute(client.get_environment_action, request, DataZoneGetEnvironmentActionResponse)

    async def get_environment_blueprint(
        self,
        request: DataZoneGetEnvironmentBlueprintRequest,
    ) -> DataZoneGetEnvironmentBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.get_environment_blueprint, request, DataZoneGetEnvironmentBlueprintResponse)

    async def get_environment_blueprint_configuration(
        self,
        request: DataZoneGetEnvironmentBlueprintConfigurationRequest,
    ) -> DataZoneGetEnvironmentBlueprintConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_environment_blueprint_configuration, request, DataZoneGetEnvironmentBlueprintConfigurationResponse)

    async def get_environment_credentials(
        self,
        request: DataZoneGetEnvironmentCredentialsRequest,
    ) -> DataZoneGetEnvironmentCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_environment_credentials, request, DataZoneGetEnvironmentCredentialsResponse)

    async def get_environment_profile(
        self,
        request: DataZoneGetEnvironmentProfileRequest,
    ) -> DataZoneGetEnvironmentProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_environment_profile, request, DataZoneGetEnvironmentProfileResponse)

    async def get_form_type(
        self,
        request: DataZoneGetFormTypeRequest,
    ) -> DataZoneGetFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_form_type, request, DataZoneGetFormTypeResponse)

    async def get_glossary(
        self,
        request: DataZoneGetGlossaryRequest,
    ) -> DataZoneGetGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.get_glossary, request, DataZoneGetGlossaryResponse)

    async def get_glossary_term(
        self,
        request: DataZoneGetGlossaryTermRequest,
    ) -> DataZoneGetGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.get_glossary_term, request, DataZoneGetGlossaryTermResponse)

    async def get_group_profile(
        self,
        request: DataZoneGetGroupProfileRequest,
    ) -> DataZoneGetGroupProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_group_profile, request, DataZoneGetGroupProfileResponse)

    async def get_iam_portal_login_url(
        self,
        request: DataZoneGetIamPortalLoginUrlRequest,
    ) -> DataZoneGetIamPortalLoginUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_iam_portal_login_url, request, DataZoneGetIamPortalLoginUrlResponse)

    async def get_job_run(
        self,
        request: DataZoneGetJobRunRequest,
    ) -> DataZoneGetJobRunResponse:
        client = self._require_client()
        return await self._execute(client.get_job_run, request, DataZoneGetJobRunResponse)

    async def get_lineage_event(
        self,
        request: DataZoneGetLineageEventRequest,
    ) -> DataZoneGetLineageEventResponse:
        client = self._require_client()
        return await self._execute(client.get_lineage_event, request, DataZoneGetLineageEventResponse)

    async def get_lineage_node(
        self,
        request: DataZoneGetLineageNodeRequest,
    ) -> DataZoneGetLineageNodeResponse:
        client = self._require_client()
        return await self._execute(client.get_lineage_node, request, DataZoneGetLineageNodeResponse)

    async def get_listing(
        self,
        request: DataZoneGetListingRequest,
    ) -> DataZoneGetListingResponse:
        client = self._require_client()
        return await self._execute(client.get_listing, request, DataZoneGetListingResponse)

    async def get_metadata_generation_run(
        self,
        request: DataZoneGetMetadataGenerationRunRequest,
    ) -> DataZoneGetMetadataGenerationRunResponse:
        client = self._require_client()
        return await self._execute(client.get_metadata_generation_run, request, DataZoneGetMetadataGenerationRunResponse)

    async def get_notebook(
        self,
        request: DataZoneGetNotebookRequest,
    ) -> DataZoneGetNotebookResponse:
        client = self._require_client()
        return await self._execute(client.get_notebook, request, DataZoneGetNotebookResponse)

    async def get_notebook_export(
        self,
        request: DataZoneGetNotebookExportRequest,
    ) -> DataZoneGetNotebookExportResponse:
        client = self._require_client()
        return await self._execute(client.get_notebook_export, request, DataZoneGetNotebookExportResponse)

    async def get_notebook_run(
        self,
        request: DataZoneGetNotebookRunRequest,
    ) -> DataZoneGetNotebookRunResponse:
        client = self._require_client()
        return await self._execute(client.get_notebook_run, request, DataZoneGetNotebookRunResponse)

    async def get_project(
        self,
        request: DataZoneGetProjectRequest,
    ) -> DataZoneGetProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_project, request, DataZoneGetProjectResponse)

    async def get_project_profile(
        self,
        request: DataZoneGetProjectProfileRequest,
    ) -> DataZoneGetProjectProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_project_profile, request, DataZoneGetProjectProfileResponse)

    async def get_rule(
        self,
        request: DataZoneGetRuleRequest,
    ) -> DataZoneGetRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_rule, request, DataZoneGetRuleResponse)

    async def get_subscription(
        self,
        request: DataZoneGetSubscriptionRequest,
    ) -> DataZoneGetSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription, request, DataZoneGetSubscriptionResponse)

    async def get_subscription_grant(
        self,
        request: DataZoneGetSubscriptionGrantRequest,
    ) -> DataZoneGetSubscriptionGrantResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription_grant, request, DataZoneGetSubscriptionGrantResponse)

    async def get_subscription_request_details(
        self,
        request: DataZoneGetSubscriptionRequestDetailsRequest,
    ) -> DataZoneGetSubscriptionRequestDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription_request_details, request, DataZoneGetSubscriptionRequestDetailsResponse)

    async def get_subscription_target(
        self,
        request: DataZoneGetSubscriptionTargetRequest,
    ) -> DataZoneGetSubscriptionTargetResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription_target, request, DataZoneGetSubscriptionTargetResponse)

    async def get_time_series_data_point(
        self,
        request: DataZoneGetTimeSeriesDataPointRequest,
    ) -> DataZoneGetTimeSeriesDataPointResponse:
        client = self._require_client()
        return await self._execute(client.get_time_series_data_point, request, DataZoneGetTimeSeriesDataPointResponse)

    async def get_user_profile(
        self,
        request: DataZoneGetUserProfileRequest,
    ) -> DataZoneGetUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_user_profile, request, DataZoneGetUserProfileResponse)

    async def list_account_pools(
        self,
        request: DataZoneListAccountPoolsRequest,
    ) -> DataZoneListAccountPoolsResponse:
        client = self._require_client()
        return await self._execute(client.list_account_pools, request, DataZoneListAccountPoolsResponse)

    async def list_account_pools_paginated(
        self,
        request: DataZoneListAccountPoolsRequest,
    ) -> list[DataZoneListAccountPoolsResponse]:
        return await self._paginate('list_account_pools', request, DataZoneListAccountPoolsResponse)

    async def list_accounts_in_account_pool(
        self,
        request: DataZoneListAccountsInAccountPoolRequest,
    ) -> DataZoneListAccountsInAccountPoolResponse:
        client = self._require_client()
        return await self._execute(client.list_accounts_in_account_pool, request, DataZoneListAccountsInAccountPoolResponse)

    async def list_accounts_in_account_pool_paginated(
        self,
        request: DataZoneListAccountsInAccountPoolRequest,
    ) -> list[DataZoneListAccountsInAccountPoolResponse]:
        return await self._paginate('list_accounts_in_account_pool', request, DataZoneListAccountsInAccountPoolResponse)

    async def list_asset_filters(
        self,
        request: DataZoneListAssetFiltersRequest,
    ) -> DataZoneListAssetFiltersResponse:
        client = self._require_client()
        return await self._execute(client.list_asset_filters, request, DataZoneListAssetFiltersResponse)

    async def list_asset_filters_paginated(
        self,
        request: DataZoneListAssetFiltersRequest,
    ) -> list[DataZoneListAssetFiltersResponse]:
        return await self._paginate('list_asset_filters', request, DataZoneListAssetFiltersResponse)

    async def list_asset_revisions(
        self,
        request: DataZoneListAssetRevisionsRequest,
    ) -> DataZoneListAssetRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.list_asset_revisions, request, DataZoneListAssetRevisionsResponse)

    async def list_asset_revisions_paginated(
        self,
        request: DataZoneListAssetRevisionsRequest,
    ) -> list[DataZoneListAssetRevisionsResponse]:
        return await self._paginate('list_asset_revisions', request, DataZoneListAssetRevisionsResponse)

    async def list_connections(
        self,
        request: DataZoneListConnectionsRequest,
    ) -> DataZoneListConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_connections, request, DataZoneListConnectionsResponse)

    async def list_connections_paginated(
        self,
        request: DataZoneListConnectionsRequest,
    ) -> list[DataZoneListConnectionsResponse]:
        return await self._paginate('list_connections', request, DataZoneListConnectionsResponse)

    async def list_data_product_revisions(
        self,
        request: DataZoneListDataProductRevisionsRequest,
    ) -> DataZoneListDataProductRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_product_revisions, request, DataZoneListDataProductRevisionsResponse)

    async def list_data_product_revisions_paginated(
        self,
        request: DataZoneListDataProductRevisionsRequest,
    ) -> list[DataZoneListDataProductRevisionsResponse]:
        return await self._paginate('list_data_product_revisions', request, DataZoneListDataProductRevisionsResponse)

    async def list_data_source_run_activities(
        self,
        request: DataZoneListDataSourceRunActivitiesRequest,
    ) -> DataZoneListDataSourceRunActivitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_source_run_activities, request, DataZoneListDataSourceRunActivitiesResponse)

    async def list_data_source_run_activities_paginated(
        self,
        request: DataZoneListDataSourceRunActivitiesRequest,
    ) -> list[DataZoneListDataSourceRunActivitiesResponse]:
        return await self._paginate('list_data_source_run_activities', request, DataZoneListDataSourceRunActivitiesResponse)

    async def list_data_source_runs(
        self,
        request: DataZoneListDataSourceRunsRequest,
    ) -> DataZoneListDataSourceRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_source_runs, request, DataZoneListDataSourceRunsResponse)

    async def list_data_source_runs_paginated(
        self,
        request: DataZoneListDataSourceRunsRequest,
    ) -> list[DataZoneListDataSourceRunsResponse]:
        return await self._paginate('list_data_source_runs', request, DataZoneListDataSourceRunsResponse)

    async def list_data_sources(
        self,
        request: DataZoneListDataSourcesRequest,
    ) -> DataZoneListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, DataZoneListDataSourcesResponse)

    async def list_data_sources_paginated(
        self,
        request: DataZoneListDataSourcesRequest,
    ) -> list[DataZoneListDataSourcesResponse]:
        return await self._paginate('list_data_sources', request, DataZoneListDataSourcesResponse)

    async def list_designations(
        self,
        request: DataZoneListDesignationsRequest,
    ) -> DataZoneListDesignationsResponse:
        client = self._require_client()
        return await self._execute(client.list_designations, request, DataZoneListDesignationsResponse)

    async def list_designations_paginated(
        self,
        request: DataZoneListDesignationsRequest,
    ) -> list[DataZoneListDesignationsResponse]:
        return await self._paginate('list_designations', request, DataZoneListDesignationsResponse)

    async def list_domain_units_for_parent(
        self,
        request: DataZoneListDomainUnitsForParentRequest,
    ) -> DataZoneListDomainUnitsForParentResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_units_for_parent, request, DataZoneListDomainUnitsForParentResponse)

    async def list_domain_units_for_parent_paginated(
        self,
        request: DataZoneListDomainUnitsForParentRequest,
    ) -> list[DataZoneListDomainUnitsForParentResponse]:
        return await self._paginate('list_domain_units_for_parent', request, DataZoneListDomainUnitsForParentResponse)

    async def list_domains(
        self,
        request: DataZoneListDomainsRequest | None = None,
    ) -> DataZoneListDomainsResponse:
        client = self._require_client()
        return await self._execute(client.list_domains, request, DataZoneListDomainsResponse)

    async def list_domains_paginated(
        self,
        request: DataZoneListDomainsRequest | None = None,
    ) -> list[DataZoneListDomainsResponse]:
        return await self._paginate('list_domains', request, DataZoneListDomainsResponse)

    async def list_entity_owners(
        self,
        request: DataZoneListEntityOwnersRequest,
    ) -> DataZoneListEntityOwnersResponse:
        client = self._require_client()
        return await self._execute(client.list_entity_owners, request, DataZoneListEntityOwnersResponse)

    async def list_entity_owners_paginated(
        self,
        request: DataZoneListEntityOwnersRequest,
    ) -> list[DataZoneListEntityOwnersResponse]:
        return await self._paginate('list_entity_owners', request, DataZoneListEntityOwnersResponse)

    async def list_environment_actions(
        self,
        request: DataZoneListEnvironmentActionsRequest,
    ) -> DataZoneListEnvironmentActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_environment_actions, request, DataZoneListEnvironmentActionsResponse)

    async def list_environment_actions_paginated(
        self,
        request: DataZoneListEnvironmentActionsRequest,
    ) -> list[DataZoneListEnvironmentActionsResponse]:
        return await self._paginate('list_environment_actions', request, DataZoneListEnvironmentActionsResponse)

    async def list_environment_blueprint_configurations(
        self,
        request: DataZoneListEnvironmentBlueprintConfigurationsRequest,
    ) -> DataZoneListEnvironmentBlueprintConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_environment_blueprint_configurations, request, DataZoneListEnvironmentBlueprintConfigurationsResponse)

    async def list_environment_blueprint_configurations_paginated(
        self,
        request: DataZoneListEnvironmentBlueprintConfigurationsRequest,
    ) -> list[DataZoneListEnvironmentBlueprintConfigurationsResponse]:
        return await self._paginate('list_environment_blueprint_configurations', request, DataZoneListEnvironmentBlueprintConfigurationsResponse)

    async def list_environment_blueprints(
        self,
        request: DataZoneListEnvironmentBlueprintsRequest,
    ) -> DataZoneListEnvironmentBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.list_environment_blueprints, request, DataZoneListEnvironmentBlueprintsResponse)

    async def list_environment_blueprints_paginated(
        self,
        request: DataZoneListEnvironmentBlueprintsRequest,
    ) -> list[DataZoneListEnvironmentBlueprintsResponse]:
        return await self._paginate('list_environment_blueprints', request, DataZoneListEnvironmentBlueprintsResponse)

    async def list_environment_profiles(
        self,
        request: DataZoneListEnvironmentProfilesRequest,
    ) -> DataZoneListEnvironmentProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_environment_profiles, request, DataZoneListEnvironmentProfilesResponse)

    async def list_environment_profiles_paginated(
        self,
        request: DataZoneListEnvironmentProfilesRequest,
    ) -> list[DataZoneListEnvironmentProfilesResponse]:
        return await self._paginate('list_environment_profiles', request, DataZoneListEnvironmentProfilesResponse)

    async def list_environments(
        self,
        request: DataZoneListEnvironmentsRequest,
    ) -> DataZoneListEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_environments, request, DataZoneListEnvironmentsResponse)

    async def list_environments_paginated(
        self,
        request: DataZoneListEnvironmentsRequest,
    ) -> list[DataZoneListEnvironmentsResponse]:
        return await self._paginate('list_environments', request, DataZoneListEnvironmentsResponse)

    async def list_job_runs(
        self,
        request: DataZoneListJobRunsRequest,
    ) -> DataZoneListJobRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_job_runs, request, DataZoneListJobRunsResponse)

    async def list_job_runs_paginated(
        self,
        request: DataZoneListJobRunsRequest,
    ) -> list[DataZoneListJobRunsResponse]:
        return await self._paginate('list_job_runs', request, DataZoneListJobRunsResponse)

    async def list_lineage_events(
        self,
        request: DataZoneListLineageEventsRequest,
    ) -> DataZoneListLineageEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_lineage_events, request, DataZoneListLineageEventsResponse)

    async def list_lineage_events_paginated(
        self,
        request: DataZoneListLineageEventsRequest,
    ) -> list[DataZoneListLineageEventsResponse]:
        return await self._paginate('list_lineage_events', request, DataZoneListLineageEventsResponse)

    async def list_lineage_node_history(
        self,
        request: DataZoneListLineageNodeHistoryRequest,
    ) -> DataZoneListLineageNodeHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_lineage_node_history, request, DataZoneListLineageNodeHistoryResponse)

    async def list_lineage_node_history_paginated(
        self,
        request: DataZoneListLineageNodeHistoryRequest,
    ) -> list[DataZoneListLineageNodeHistoryResponse]:
        return await self._paginate('list_lineage_node_history', request, DataZoneListLineageNodeHistoryResponse)

    async def list_metadata_generation_runs(
        self,
        request: DataZoneListMetadataGenerationRunsRequest,
    ) -> DataZoneListMetadataGenerationRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_metadata_generation_runs, request, DataZoneListMetadataGenerationRunsResponse)

    async def list_metadata_generation_runs_paginated(
        self,
        request: DataZoneListMetadataGenerationRunsRequest,
    ) -> list[DataZoneListMetadataGenerationRunsResponse]:
        return await self._paginate('list_metadata_generation_runs', request, DataZoneListMetadataGenerationRunsResponse)

    async def list_notebook_runs(
        self,
        request: DataZoneListNotebookRunsRequest,
    ) -> DataZoneListNotebookRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_notebook_runs, request, DataZoneListNotebookRunsResponse)

    async def list_notebook_runs_paginated(
        self,
        request: DataZoneListNotebookRunsRequest,
    ) -> list[DataZoneListNotebookRunsResponse]:
        return await self._paginate('list_notebook_runs', request, DataZoneListNotebookRunsResponse)

    async def list_notebooks(
        self,
        request: DataZoneListNotebooksRequest,
    ) -> DataZoneListNotebooksResponse:
        client = self._require_client()
        return await self._execute(client.list_notebooks, request, DataZoneListNotebooksResponse)

    async def list_notebooks_paginated(
        self,
        request: DataZoneListNotebooksRequest,
    ) -> list[DataZoneListNotebooksResponse]:
        return await self._paginate('list_notebooks', request, DataZoneListNotebooksResponse)

    async def list_notifications(
        self,
        request: DataZoneListNotificationsRequest,
    ) -> DataZoneListNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.list_notifications, request, DataZoneListNotificationsResponse)

    async def list_notifications_paginated(
        self,
        request: DataZoneListNotificationsRequest,
    ) -> list[DataZoneListNotificationsResponse]:
        return await self._paginate('list_notifications', request, DataZoneListNotificationsResponse)

    async def list_policy_grants(
        self,
        request: DataZoneListPolicyGrantsRequest,
    ) -> DataZoneListPolicyGrantsResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_grants, request, DataZoneListPolicyGrantsResponse)

    async def list_policy_grants_paginated(
        self,
        request: DataZoneListPolicyGrantsRequest,
    ) -> list[DataZoneListPolicyGrantsResponse]:
        return await self._paginate('list_policy_grants', request, DataZoneListPolicyGrantsResponse)

    async def list_project_memberships(
        self,
        request: DataZoneListProjectMembershipsRequest,
    ) -> DataZoneListProjectMembershipsResponse:
        client = self._require_client()
        return await self._execute(client.list_project_memberships, request, DataZoneListProjectMembershipsResponse)

    async def list_project_memberships_paginated(
        self,
        request: DataZoneListProjectMembershipsRequest,
    ) -> list[DataZoneListProjectMembershipsResponse]:
        return await self._paginate('list_project_memberships', request, DataZoneListProjectMembershipsResponse)

    async def list_project_profiles(
        self,
        request: DataZoneListProjectProfilesRequest,
    ) -> DataZoneListProjectProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_project_profiles, request, DataZoneListProjectProfilesResponse)

    async def list_project_profiles_paginated(
        self,
        request: DataZoneListProjectProfilesRequest,
    ) -> list[DataZoneListProjectProfilesResponse]:
        return await self._paginate('list_project_profiles', request, DataZoneListProjectProfilesResponse)

    async def list_projects(
        self,
        request: DataZoneListProjectsRequest,
    ) -> DataZoneListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, DataZoneListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: DataZoneListProjectsRequest,
    ) -> list[DataZoneListProjectsResponse]:
        return await self._paginate('list_projects', request, DataZoneListProjectsResponse)

    async def list_rules(
        self,
        request: DataZoneListRulesRequest,
    ) -> DataZoneListRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_rules, request, DataZoneListRulesResponse)

    async def list_rules_paginated(
        self,
        request: DataZoneListRulesRequest,
    ) -> list[DataZoneListRulesResponse]:
        return await self._paginate('list_rules', request, DataZoneListRulesResponse)

    async def list_subscription_grants(
        self,
        request: DataZoneListSubscriptionGrantsRequest,
    ) -> DataZoneListSubscriptionGrantsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscription_grants, request, DataZoneListSubscriptionGrantsResponse)

    async def list_subscription_grants_paginated(
        self,
        request: DataZoneListSubscriptionGrantsRequest,
    ) -> list[DataZoneListSubscriptionGrantsResponse]:
        return await self._paginate('list_subscription_grants', request, DataZoneListSubscriptionGrantsResponse)

    async def list_subscription_requests(
        self,
        request: DataZoneListSubscriptionRequestsRequest,
    ) -> DataZoneListSubscriptionRequestsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscription_requests, request, DataZoneListSubscriptionRequestsResponse)

    async def list_subscription_requests_paginated(
        self,
        request: DataZoneListSubscriptionRequestsRequest,
    ) -> list[DataZoneListSubscriptionRequestsResponse]:
        return await self._paginate('list_subscription_requests', request, DataZoneListSubscriptionRequestsResponse)

    async def list_subscription_targets(
        self,
        request: DataZoneListSubscriptionTargetsRequest,
    ) -> DataZoneListSubscriptionTargetsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscription_targets, request, DataZoneListSubscriptionTargetsResponse)

    async def list_subscription_targets_paginated(
        self,
        request: DataZoneListSubscriptionTargetsRequest,
    ) -> list[DataZoneListSubscriptionTargetsResponse]:
        return await self._paginate('list_subscription_targets', request, DataZoneListSubscriptionTargetsResponse)

    async def list_subscriptions(
        self,
        request: DataZoneListSubscriptionsRequest,
    ) -> DataZoneListSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscriptions, request, DataZoneListSubscriptionsResponse)

    async def list_subscriptions_paginated(
        self,
        request: DataZoneListSubscriptionsRequest,
    ) -> list[DataZoneListSubscriptionsResponse]:
        return await self._paginate('list_subscriptions', request, DataZoneListSubscriptionsResponse)

    async def list_tags_for_resource(
        self,
        request: DataZoneListTagsForResourceRequest,
    ) -> DataZoneListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DataZoneListTagsForResourceResponse)

    async def list_time_series_data_points(
        self,
        request: DataZoneListTimeSeriesDataPointsRequest,
    ) -> DataZoneListTimeSeriesDataPointsResponse:
        client = self._require_client()
        return await self._execute(client.list_time_series_data_points, request, DataZoneListTimeSeriesDataPointsResponse)

    async def list_time_series_data_points_paginated(
        self,
        request: DataZoneListTimeSeriesDataPointsRequest,
    ) -> list[DataZoneListTimeSeriesDataPointsResponse]:
        return await self._paginate('list_time_series_data_points', request, DataZoneListTimeSeriesDataPointsResponse)

    async def post_lineage_event(
        self,
        request: DataZonePostLineageEventRequest,
    ) -> DataZonePostLineageEventResponse:
        client = self._require_client()
        return await self._execute(client.post_lineage_event, request, DataZonePostLineageEventResponse)

    async def post_time_series_data_points(
        self,
        request: DataZonePostTimeSeriesDataPointsRequest,
    ) -> DataZonePostTimeSeriesDataPointsResponse:
        client = self._require_client()
        return await self._execute(client.post_time_series_data_points, request, DataZonePostTimeSeriesDataPointsResponse)

    async def put_data_export_configuration(
        self,
        request: DataZonePutDataExportConfigurationRequest,
    ) -> DataZonePutDataExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_data_export_configuration, request, DataZonePutDataExportConfigurationResponse)

    async def put_environment_blueprint_configuration(
        self,
        request: DataZonePutEnvironmentBlueprintConfigurationRequest,
    ) -> DataZonePutEnvironmentBlueprintConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_environment_blueprint_configuration, request, DataZonePutEnvironmentBlueprintConfigurationResponse)

    async def query_graph(
        self,
        request: DataZoneQueryGraphRequest,
    ) -> DataZoneQueryGraphResponse:
        client = self._require_client()
        return await self._execute(client.query_graph, request, DataZoneQueryGraphResponse)

    async def query_graph_paginated(
        self,
        request: DataZoneQueryGraphRequest,
    ) -> list[DataZoneQueryGraphResponse]:
        return await self._paginate('query_graph', request, DataZoneQueryGraphResponse)

    async def reject_predictions(
        self,
        request: DataZoneRejectPredictionsRequest,
    ) -> DataZoneRejectPredictionsResponse:
        client = self._require_client()
        return await self._execute(client.reject_predictions, request, DataZoneRejectPredictionsResponse)

    async def reject_subscription_request(
        self,
        request: DataZoneRejectSubscriptionRequestRequest,
    ) -> DataZoneRejectSubscriptionRequestResponse:
        client = self._require_client()
        return await self._execute(client.reject_subscription_request, request, DataZoneRejectSubscriptionRequestResponse)

    async def remove_entity_owner(
        self,
        request: DataZoneRemoveEntityOwnerRequest,
    ) -> DataZoneRemoveEntityOwnerResponse:
        client = self._require_client()
        return await self._execute(client.remove_entity_owner, request, DataZoneRemoveEntityOwnerResponse)

    async def remove_policy_grant(
        self,
        request: DataZoneRemovePolicyGrantRequest,
    ) -> DataZoneRemovePolicyGrantResponse:
        client = self._require_client()
        return await self._execute(client.remove_policy_grant, request, DataZoneRemovePolicyGrantResponse)

    async def revoke_subscription(
        self,
        request: DataZoneRevokeSubscriptionRequest,
    ) -> DataZoneRevokeSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.revoke_subscription, request, DataZoneRevokeSubscriptionResponse)

    async def search(
        self,
        request: DataZoneSearchRequest,
    ) -> DataZoneSearchResponse:
        client = self._require_client()
        return await self._execute(client.search, request, DataZoneSearchResponse)

    async def search_paginated(
        self,
        request: DataZoneSearchRequest,
    ) -> list[DataZoneSearchResponse]:
        return await self._paginate('search', request, DataZoneSearchResponse)

    async def search_group_profiles(
        self,
        request: DataZoneSearchGroupProfilesRequest,
    ) -> DataZoneSearchGroupProfilesResponse:
        client = self._require_client()
        return await self._execute(client.search_group_profiles, request, DataZoneSearchGroupProfilesResponse)

    async def search_group_profiles_paginated(
        self,
        request: DataZoneSearchGroupProfilesRequest,
    ) -> list[DataZoneSearchGroupProfilesResponse]:
        return await self._paginate('search_group_profiles', request, DataZoneSearchGroupProfilesResponse)

    async def search_listings(
        self,
        request: DataZoneSearchListingsRequest,
    ) -> DataZoneSearchListingsResponse:
        client = self._require_client()
        return await self._execute(client.search_listings, request, DataZoneSearchListingsResponse)

    async def search_listings_paginated(
        self,
        request: DataZoneSearchListingsRequest,
    ) -> list[DataZoneSearchListingsResponse]:
        return await self._paginate('search_listings', request, DataZoneSearchListingsResponse)

    async def search_types(
        self,
        request: DataZoneSearchTypesRequest,
    ) -> DataZoneSearchTypesResponse:
        client = self._require_client()
        return await self._execute(client.search_types, request, DataZoneSearchTypesResponse)

    async def search_types_paginated(
        self,
        request: DataZoneSearchTypesRequest,
    ) -> list[DataZoneSearchTypesResponse]:
        return await self._paginate('search_types', request, DataZoneSearchTypesResponse)

    async def search_user_profiles(
        self,
        request: DataZoneSearchUserProfilesRequest,
    ) -> DataZoneSearchUserProfilesResponse:
        client = self._require_client()
        return await self._execute(client.search_user_profiles, request, DataZoneSearchUserProfilesResponse)

    async def search_user_profiles_paginated(
        self,
        request: DataZoneSearchUserProfilesRequest,
    ) -> list[DataZoneSearchUserProfilesResponse]:
        return await self._paginate('search_user_profiles', request, DataZoneSearchUserProfilesResponse)

    async def start_data_source_run(
        self,
        request: DataZoneStartDataSourceRunRequest,
    ) -> DataZoneStartDataSourceRunResponse:
        client = self._require_client()
        return await self._execute(client.start_data_source_run, request, DataZoneStartDataSourceRunResponse)

    async def start_metadata_generation_run(
        self,
        request: DataZoneStartMetadataGenerationRunRequest,
    ) -> DataZoneStartMetadataGenerationRunResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_generation_run, request, DataZoneStartMetadataGenerationRunResponse)

    async def start_notebook_export(
        self,
        request: DataZoneStartNotebookExportRequest,
    ) -> DataZoneStartNotebookExportResponse:
        client = self._require_client()
        return await self._execute(client.start_notebook_export, request, DataZoneStartNotebookExportResponse)

    async def start_notebook_import(
        self,
        request: DataZoneStartNotebookImportRequest,
    ) -> DataZoneStartNotebookImportResponse:
        client = self._require_client()
        return await self._execute(client.start_notebook_import, request, DataZoneStartNotebookImportResponse)

    async def start_notebook_run(
        self,
        request: DataZoneStartNotebookRunRequest,
    ) -> DataZoneStartNotebookRunResponse:
        client = self._require_client()
        return await self._execute(client.start_notebook_run, request, DataZoneStartNotebookRunResponse)

    async def start_notebook_sync(
        self,
        request: DataZoneStartNotebookSyncRequest,
    ) -> DataZoneStartNotebookSyncResponse:
        client = self._require_client()
        return await self._execute(client.start_notebook_sync, request, DataZoneStartNotebookSyncResponse)

    async def stop_notebook_run(
        self,
        request: DataZoneStopNotebookRunRequest,
    ) -> DataZoneStopNotebookRunResponse:
        client = self._require_client()
        return await self._execute(client.stop_notebook_run, request, DataZoneStopNotebookRunResponse)

    async def tag_resource(
        self,
        request: DataZoneTagResourceRequest,
    ) -> DataZoneTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, DataZoneTagResourceResponse)

    async def untag_resource(
        self,
        request: DataZoneUntagResourceRequest,
    ) -> DataZoneUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, DataZoneUntagResourceResponse)

    async def update_account_pool(
        self,
        request: DataZoneUpdateAccountPoolRequest,
    ) -> DataZoneUpdateAccountPoolResponse:
        client = self._require_client()
        return await self._execute(client.update_account_pool, request, DataZoneUpdateAccountPoolResponse)

    async def update_asset_filter(
        self,
        request: DataZoneUpdateAssetFilterRequest,
    ) -> DataZoneUpdateAssetFilterResponse:
        client = self._require_client()
        return await self._execute(client.update_asset_filter, request, DataZoneUpdateAssetFilterResponse)

    async def update_asset_owner(
        self,
        request: DataZoneUpdateAssetOwnerRequest,
    ) -> DataZoneUpdateAssetOwnerResponse:
        client = self._require_client()
        return await self._execute(client.update_asset_owner, request, DataZoneUpdateAssetOwnerResponse)

    async def update_connection(
        self,
        request: DataZoneUpdateConnectionRequest,
    ) -> DataZoneUpdateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection, request, DataZoneUpdateConnectionResponse)

    async def update_data_source(
        self,
        request: DataZoneUpdateDataSourceRequest,
    ) -> DataZoneUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, DataZoneUpdateDataSourceResponse)

    async def update_designation(
        self,
        request: DataZoneUpdateDesignationRequest,
    ) -> DataZoneUpdateDesignationResponse:
        client = self._require_client()
        return await self._execute(client.update_designation, request, DataZoneUpdateDesignationResponse)

    async def update_domain(
        self,
        request: DataZoneUpdateDomainRequest,
    ) -> DataZoneUpdateDomainResponse:
        client = self._require_client()
        return await self._execute(client.update_domain, request, DataZoneUpdateDomainResponse)

    async def update_domain_unit(
        self,
        request: DataZoneUpdateDomainUnitRequest,
    ) -> DataZoneUpdateDomainUnitResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_unit, request, DataZoneUpdateDomainUnitResponse)

    async def update_environment(
        self,
        request: DataZoneUpdateEnvironmentRequest,
    ) -> DataZoneUpdateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_environment, request, DataZoneUpdateEnvironmentResponse)

    async def update_environment_action(
        self,
        request: DataZoneUpdateEnvironmentActionRequest,
    ) -> DataZoneUpdateEnvironmentActionResponse:
        client = self._require_client()
        return await self._execute(client.update_environment_action, request, DataZoneUpdateEnvironmentActionResponse)

    async def update_environment_blueprint(
        self,
        request: DataZoneUpdateEnvironmentBlueprintRequest,
    ) -> DataZoneUpdateEnvironmentBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.update_environment_blueprint, request, DataZoneUpdateEnvironmentBlueprintResponse)

    async def update_environment_profile(
        self,
        request: DataZoneUpdateEnvironmentProfileRequest,
    ) -> DataZoneUpdateEnvironmentProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_environment_profile, request, DataZoneUpdateEnvironmentProfileResponse)

    async def update_glossary(
        self,
        request: DataZoneUpdateGlossaryRequest,
    ) -> DataZoneUpdateGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.update_glossary, request, DataZoneUpdateGlossaryResponse)

    async def update_glossary_term(
        self,
        request: DataZoneUpdateGlossaryTermRequest,
    ) -> DataZoneUpdateGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.update_glossary_term, request, DataZoneUpdateGlossaryTermResponse)

    async def update_group_profile(
        self,
        request: DataZoneUpdateGroupProfileRequest,
    ) -> DataZoneUpdateGroupProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_group_profile, request, DataZoneUpdateGroupProfileResponse)

    async def update_notebook(
        self,
        request: DataZoneUpdateNotebookRequest,
    ) -> DataZoneUpdateNotebookResponse:
        client = self._require_client()
        return await self._execute(client.update_notebook, request, DataZoneUpdateNotebookResponse)

    async def update_project(
        self,
        request: DataZoneUpdateProjectRequest,
    ) -> DataZoneUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, DataZoneUpdateProjectResponse)

    async def update_project_profile(
        self,
        request: DataZoneUpdateProjectProfileRequest,
    ) -> DataZoneUpdateProjectProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_project_profile, request, DataZoneUpdateProjectProfileResponse)

    async def update_root_domain_unit_owner(
        self,
        request: DataZoneUpdateRootDomainUnitOwnerRequest,
    ) -> DataZoneUpdateRootDomainUnitOwnerResponse:
        client = self._require_client()
        return await self._execute(client.update_root_domain_unit_owner, request, DataZoneUpdateRootDomainUnitOwnerResponse)

    async def update_rule(
        self,
        request: DataZoneUpdateRuleRequest,
    ) -> DataZoneUpdateRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_rule, request, DataZoneUpdateRuleResponse)

    async def update_subscription_grant_status(
        self,
        request: DataZoneUpdateSubscriptionGrantStatusRequest,
    ) -> DataZoneUpdateSubscriptionGrantStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_subscription_grant_status, request, DataZoneUpdateSubscriptionGrantStatusResponse)

    async def update_subscription_request(
        self,
        request: DataZoneUpdateSubscriptionRequestRequest,
    ) -> DataZoneUpdateSubscriptionRequestResponse:
        client = self._require_client()
        return await self._execute(client.update_subscription_request, request, DataZoneUpdateSubscriptionRequestResponse)

    async def update_subscription_target(
        self,
        request: DataZoneUpdateSubscriptionTargetRequest,
    ) -> DataZoneUpdateSubscriptionTargetResponse:
        client = self._require_client()
        return await self._execute(client.update_subscription_target, request, DataZoneUpdateSubscriptionTargetResponse)

    async def update_user_profile(
        self,
        request: DataZoneUpdateUserProfileRequest,
    ) -> DataZoneUpdateUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_user_profile, request, DataZoneUpdateUserProfileResponse)
