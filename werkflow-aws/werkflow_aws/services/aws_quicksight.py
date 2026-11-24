from werkflow_aws.models.quicksight import (
    QuickSightBatchCreateTopicReviewedAnswerRequest,
    QuickSightBatchCreateTopicReviewedAnswerResponse,
    QuickSightBatchDeleteKnowledgeBaseRequest,
    QuickSightBatchDeleteKnowledgeBaseResponse,
    QuickSightBatchDeletePolicyAssignmentByPolicyRequest,
    QuickSightBatchDeletePolicyAssignmentByPolicyResponse,
    QuickSightBatchDeleteTopicReviewedAnswerRequest,
    QuickSightBatchDeleteTopicReviewedAnswerResponse,
    QuickSightBatchDescribeUserLimitsRequest,
    QuickSightBatchDescribeUserLimitsResponse,
    QuickSightBatchPutPolicyAssignmentByPolicyRequest,
    QuickSightBatchPutPolicyAssignmentByPolicyResponse,
    QuickSightCancelIngestionRequest,
    QuickSightCancelIngestionResponse,
    QuickSightCreateAccessControlApplicationRequest,
    QuickSightCreateAccessControlApplicationResponse,
    QuickSightCreateAccessControlApplicationSecretRequest,
    QuickSightCreateAccessControlApplicationSecretResponse,
    QuickSightCreateAccountCustomizationRequest,
    QuickSightCreateAccountCustomizationResponse,
    QuickSightCreateAccountSubscriptionRequest,
    QuickSightCreateAccountSubscriptionResponse,
    QuickSightCreateActionConnectorRequest,
    QuickSightCreateActionConnectorResponse,
    QuickSightCreateAgentRequest,
    QuickSightCreateAgentResponse,
    QuickSightCreateAnalysisRequest,
    QuickSightCreateAnalysisResponse,
    QuickSightCreateApprovalPolicyRequest,
    QuickSightCreateApprovalPolicyResponse,
    QuickSightCreateBrandRequest,
    QuickSightCreateBrandResponse,
    QuickSightCreateCustomPermissionsRequest,
    QuickSightCreateCustomPermissionsResponse,
    QuickSightCreateDashboardRequest,
    QuickSightCreateDashboardResponse,
    QuickSightCreateDataSetRequest,
    QuickSightCreateDataSetResponse,
    QuickSightCreateDataSourceRequest,
    QuickSightCreateDataSourceResponse,
    QuickSightCreateDlpSettingRequest,
    QuickSightCreateDlpSettingResponse,
    QuickSightCreateFlowRequest,
    QuickSightCreateFlowResponse,
    QuickSightCreateFolderMembershipRequest,
    QuickSightCreateFolderMembershipResponse,
    QuickSightCreateFolderRequest,
    QuickSightCreateFolderResponse,
    QuickSightCreateGroupMembershipRequest,
    QuickSightCreateGroupMembershipResponse,
    QuickSightCreateGroupRequest,
    QuickSightCreateGroupResponse,
    QuickSightCreateIAMPolicyAssignmentRequest,
    QuickSightCreateIAMPolicyAssignmentResponse,
    QuickSightCreateInboundConnectorRequest,
    QuickSightCreateInboundConnectorResponse,
    QuickSightCreateIngestionRequest,
    QuickSightCreateIngestionResponse,
    QuickSightCreateKnowledgeBaseRefreshScheduleRequest,
    QuickSightCreateKnowledgeBaseRefreshScheduleResponse,
    QuickSightCreateKnowledgeBaseRequest,
    QuickSightCreateKnowledgeBaseResponse,
    QuickSightCreateLimitsProfileRequest,
    QuickSightCreateLimitsProfileResponse,
    QuickSightCreateNamespaceRequest,
    QuickSightCreateNamespaceResponse,
    QuickSightCreateOAuthClientApplicationRequest,
    QuickSightCreateOAuthClientApplicationResponse,
    QuickSightCreateRefreshScheduleRequest,
    QuickSightCreateRefreshScheduleResponse,
    QuickSightCreateRoleMembershipRequest,
    QuickSightCreateRoleMembershipResponse,
    QuickSightCreateSpaceRequest,
    QuickSightCreateSpaceResponse,
    QuickSightCreateTemplateAliasRequest,
    QuickSightCreateTemplateAliasResponse,
    QuickSightCreateTemplateRequest,
    QuickSightCreateTemplateResponse,
    QuickSightCreateThemeAliasRequest,
    QuickSightCreateThemeAliasResponse,
    QuickSightCreateThemeRequest,
    QuickSightCreateThemeResponse,
    QuickSightCreateTopicRefreshScheduleRequest,
    QuickSightCreateTopicRefreshScheduleResponse,
    QuickSightCreateTopicRequest,
    QuickSightCreateTopicResponse,
    QuickSightCreateTopicV2Request,
    QuickSightCreateTopicV2Response,
    QuickSightCreateVPCConnectionRequest,
    QuickSightCreateVPCConnectionResponse,
    QuickSightDeleteAccessControlApplicationRequest,
    QuickSightDeleteAccessControlApplicationResponse,
    QuickSightDeleteAccessControlApplicationSecretRequest,
    QuickSightDeleteAccessControlApplicationSecretResponse,
    QuickSightDeleteAccountCustomPermissionRequest,
    QuickSightDeleteAccountCustomPermissionResponse,
    QuickSightDeleteAccountCustomizationRequest,
    QuickSightDeleteAccountCustomizationResponse,
    QuickSightDeleteAccountSubscriptionRequest,
    QuickSightDeleteAccountSubscriptionResponse,
    QuickSightDeleteActionConnectorRequest,
    QuickSightDeleteActionConnectorResponse,
    QuickSightDeleteAgentRequest,
    QuickSightDeleteAgentResponse,
    QuickSightDeleteAnalysisRequest,
    QuickSightDeleteAnalysisResponse,
    QuickSightDeleteAppRequest,
    QuickSightDeleteAppResponse,
    QuickSightDeleteApprovalPolicyRequest,
    QuickSightDeleteApprovalPolicyResponse,
    QuickSightDeleteBrandAssignmentRequest,
    QuickSightDeleteBrandAssignmentResponse,
    QuickSightDeleteBrandRequest,
    QuickSightDeleteBrandResponse,
    QuickSightDeleteCustomPermissionsRequest,
    QuickSightDeleteCustomPermissionsResponse,
    QuickSightDeleteDashboardRequest,
    QuickSightDeleteDashboardResponse,
    QuickSightDeleteDataSetRefreshPropertiesRequest,
    QuickSightDeleteDataSetRefreshPropertiesResponse,
    QuickSightDeleteDataSetRequest,
    QuickSightDeleteDataSetResponse,
    QuickSightDeleteDataSourceRequest,
    QuickSightDeleteDataSourceResponse,
    QuickSightDeleteDefaultQBusinessApplicationRequest,
    QuickSightDeleteDefaultQBusinessApplicationResponse,
    QuickSightDeleteDlpSettingRequest,
    QuickSightDeleteDlpSettingResponse,
    QuickSightDeleteFlowRequest,
    QuickSightDeleteFlowResponse,
    QuickSightDeleteFolderMembershipRequest,
    QuickSightDeleteFolderMembershipResponse,
    QuickSightDeleteFolderRequest,
    QuickSightDeleteFolderResponse,
    QuickSightDeleteGroupMembershipRequest,
    QuickSightDeleteGroupMembershipResponse,
    QuickSightDeleteGroupRequest,
    QuickSightDeleteGroupResponse,
    QuickSightDeleteIAMPolicyAssignmentRequest,
    QuickSightDeleteIAMPolicyAssignmentResponse,
    QuickSightDeleteIdentityPropagationConfigRequest,
    QuickSightDeleteIdentityPropagationConfigResponse,
    QuickSightDeleteInboundConnectorRequest,
    QuickSightDeleteInboundConnectorResponse,
    QuickSightDeleteKnowledgeBaseRefreshScheduleRequest,
    QuickSightDeleteKnowledgeBaseRefreshScheduleResponse,
    QuickSightDeleteKnowledgeBaseRequest,
    QuickSightDeleteKnowledgeBaseResponse,
    QuickSightDeleteLimitsProfileRequest,
    QuickSightDeleteLimitsProfileResponse,
    QuickSightDeleteNamespaceRequest,
    QuickSightDeleteNamespaceResponse,
    QuickSightDeleteOAuthClientApplicationRequest,
    QuickSightDeleteOAuthClientApplicationResponse,
    QuickSightDeletePolicyAssignmentRequest,
    QuickSightDeletePolicyAssignmentResponse,
    QuickSightDeleteRefreshScheduleRequest,
    QuickSightDeleteRefreshScheduleResponse,
    QuickSightDeleteRoleCustomPermissionRequest,
    QuickSightDeleteRoleCustomPermissionResponse,
    QuickSightDeleteRoleMembershipRequest,
    QuickSightDeleteRoleMembershipResponse,
    QuickSightDeleteSpaceRequest,
    QuickSightDeleteSpaceResponse,
    QuickSightDeleteTemplateAliasRequest,
    QuickSightDeleteTemplateAliasResponse,
    QuickSightDeleteTemplateRequest,
    QuickSightDeleteTemplateResponse,
    QuickSightDeleteThemeAliasRequest,
    QuickSightDeleteThemeAliasResponse,
    QuickSightDeleteThemeRequest,
    QuickSightDeleteThemeResponse,
    QuickSightDeleteTopicRefreshScheduleRequest,
    QuickSightDeleteTopicRefreshScheduleResponse,
    QuickSightDeleteTopicRequest,
    QuickSightDeleteTopicResponse,
    QuickSightDeleteTopicV2Request,
    QuickSightDeleteTopicV2Response,
    QuickSightDeleteUserByPrincipalIdRequest,
    QuickSightDeleteUserByPrincipalIdResponse,
    QuickSightDeleteUserCustomPermissionRequest,
    QuickSightDeleteUserCustomPermissionResponse,
    QuickSightDeleteUserRequest,
    QuickSightDeleteUserResponse,
    QuickSightDeleteVPCConnectionRequest,
    QuickSightDeleteVPCConnectionResponse,
    QuickSightDescribeAccessControlApplicationRequest,
    QuickSightDescribeAccessControlApplicationResponse,
    QuickSightDescribeAccountCustomPermissionRequest,
    QuickSightDescribeAccountCustomPermissionResponse,
    QuickSightDescribeAccountCustomizationRequest,
    QuickSightDescribeAccountCustomizationResponse,
    QuickSightDescribeAccountSettingsRequest,
    QuickSightDescribeAccountSettingsResponse,
    QuickSightDescribeAccountSubscriptionRequest,
    QuickSightDescribeAccountSubscriptionResponse,
    QuickSightDescribeActionConnectorPermissionsRequest,
    QuickSightDescribeActionConnectorPermissionsResponse,
    QuickSightDescribeActionConnectorRequest,
    QuickSightDescribeActionConnectorResponse,
    QuickSightDescribeAgentPermissionsRequest,
    QuickSightDescribeAgentPermissionsResponse,
    QuickSightDescribeAgentRequest,
    QuickSightDescribeAgentResponse,
    QuickSightDescribeAnalysisDefinitionRequest,
    QuickSightDescribeAnalysisDefinitionResponse,
    QuickSightDescribeAnalysisPermissionsRequest,
    QuickSightDescribeAnalysisPermissionsResponse,
    QuickSightDescribeAnalysisRequest,
    QuickSightDescribeAnalysisResponse,
    QuickSightDescribeAppPermissionsRequest,
    QuickSightDescribeAppPermissionsResponse,
    QuickSightDescribeAppRequest,
    QuickSightDescribeAppResponse,
    QuickSightDescribeApprovalPolicyRequest,
    QuickSightDescribeApprovalPolicyResponse,
    QuickSightDescribeAssetBundleExportJobRequest,
    QuickSightDescribeAssetBundleExportJobResponse,
    QuickSightDescribeAssetBundleImportJobRequest,
    QuickSightDescribeAssetBundleImportJobResponse,
    QuickSightDescribeAutomationJobRequest,
    QuickSightDescribeAutomationJobResponse,
    QuickSightDescribeBrandAssignmentRequest,
    QuickSightDescribeBrandAssignmentResponse,
    QuickSightDescribeBrandPublishedVersionRequest,
    QuickSightDescribeBrandPublishedVersionResponse,
    QuickSightDescribeBrandRequest,
    QuickSightDescribeBrandResponse,
    QuickSightDescribeCustomPermissionsRequest,
    QuickSightDescribeCustomPermissionsResponse,
    QuickSightDescribeDashboardDefinitionRequest,
    QuickSightDescribeDashboardDefinitionResponse,
    QuickSightDescribeDashboardPermissionsRequest,
    QuickSightDescribeDashboardPermissionsResponse,
    QuickSightDescribeDashboardRequest,
    QuickSightDescribeDashboardResponse,
    QuickSightDescribeDashboardSnapshotJobRequest,
    QuickSightDescribeDashboardSnapshotJobResponse,
    QuickSightDescribeDashboardSnapshotJobResultRequest,
    QuickSightDescribeDashboardSnapshotJobResultResponse,
    QuickSightDescribeDashboardsQAConfigurationRequest,
    QuickSightDescribeDashboardsQAConfigurationResponse,
    QuickSightDescribeDataSetPermissionsRequest,
    QuickSightDescribeDataSetPermissionsResponse,
    QuickSightDescribeDataSetRefreshPropertiesRequest,
    QuickSightDescribeDataSetRefreshPropertiesResponse,
    QuickSightDescribeDataSetRequest,
    QuickSightDescribeDataSetResponse,
    QuickSightDescribeDataSourcePermissionsRequest,
    QuickSightDescribeDataSourcePermissionsResponse,
    QuickSightDescribeDataSourceRequest,
    QuickSightDescribeDataSourceResponse,
    QuickSightDescribeDefaultQBusinessApplicationRequest,
    QuickSightDescribeDefaultQBusinessApplicationResponse,
    QuickSightDescribeDlpSettingRequest,
    QuickSightDescribeDlpSettingResponse,
    QuickSightDescribeFlowRequest,
    QuickSightDescribeFlowResponse,
    QuickSightDescribeFolderPermissionsRequest,
    QuickSightDescribeFolderPermissionsResponse,
    QuickSightDescribeFolderRequest,
    QuickSightDescribeFolderResolvedPermissionsRequest,
    QuickSightDescribeFolderResolvedPermissionsResponse,
    QuickSightDescribeFolderResponse,
    QuickSightDescribeGroupMembershipRequest,
    QuickSightDescribeGroupMembershipResponse,
    QuickSightDescribeGroupRequest,
    QuickSightDescribeGroupResponse,
    QuickSightDescribeIAMPolicyAssignmentRequest,
    QuickSightDescribeIAMPolicyAssignmentResponse,
    QuickSightDescribeInboundConnectorRequest,
    QuickSightDescribeInboundConnectorResponse,
    QuickSightDescribeIngestionRequest,
    QuickSightDescribeIngestionResponse,
    QuickSightDescribeIpRestrictionRequest,
    QuickSightDescribeIpRestrictionResponse,
    QuickSightDescribeKeyRegistrationRequest,
    QuickSightDescribeKeyRegistrationResponse,
    QuickSightDescribeKnowledgeBasePermissionsRequest,
    QuickSightDescribeKnowledgeBasePermissionsResponse,
    QuickSightDescribeKnowledgeBaseRefreshScheduleRequest,
    QuickSightDescribeKnowledgeBaseRefreshScheduleResponse,
    QuickSightDescribeKnowledgeBaseRequest,
    QuickSightDescribeKnowledgeBaseResponse,
    QuickSightDescribeLimitsProfileRequest,
    QuickSightDescribeLimitsProfileResponse,
    QuickSightDescribeNamespaceRequest,
    QuickSightDescribeNamespaceResponse,
    QuickSightDescribeOAuthClientApplicationRequest,
    QuickSightDescribeOAuthClientApplicationResponse,
    QuickSightDescribeQPersonalizationConfigurationRequest,
    QuickSightDescribeQPersonalizationConfigurationResponse,
    QuickSightDescribeQuickSightQSearchConfigurationRequest,
    QuickSightDescribeQuickSightQSearchConfigurationResponse,
    QuickSightDescribeRefreshScheduleRequest,
    QuickSightDescribeRefreshScheduleResponse,
    QuickSightDescribeResourcePermissionsRequest,
    QuickSightDescribeResourcePermissionsResponse,
    QuickSightDescribeRoleCustomPermissionRequest,
    QuickSightDescribeRoleCustomPermissionResponse,
    QuickSightDescribeSelfUpgradeConfigurationRequest,
    QuickSightDescribeSelfUpgradeConfigurationResponse,
    QuickSightDescribeSpacePermissionsRequest,
    QuickSightDescribeSpacePermissionsResponse,
    QuickSightDescribeSpaceRequest,
    QuickSightDescribeSpaceResponse,
    QuickSightDescribeTemplateAliasRequest,
    QuickSightDescribeTemplateAliasResponse,
    QuickSightDescribeTemplateDefinitionRequest,
    QuickSightDescribeTemplateDefinitionResponse,
    QuickSightDescribeTemplatePermissionsRequest,
    QuickSightDescribeTemplatePermissionsResponse,
    QuickSightDescribeTemplateRequest,
    QuickSightDescribeTemplateResponse,
    QuickSightDescribeThemeAliasRequest,
    QuickSightDescribeThemeAliasResponse,
    QuickSightDescribeThemePermissionsRequest,
    QuickSightDescribeThemePermissionsResponse,
    QuickSightDescribeThemeRequest,
    QuickSightDescribeThemeResponse,
    QuickSightDescribeTopicPermissionsRequest,
    QuickSightDescribeTopicPermissionsResponse,
    QuickSightDescribeTopicPermissionsV2Request,
    QuickSightDescribeTopicPermissionsV2Response,
    QuickSightDescribeTopicRefreshRequest,
    QuickSightDescribeTopicRefreshResponse,
    QuickSightDescribeTopicRefreshScheduleRequest,
    QuickSightDescribeTopicRefreshScheduleResponse,
    QuickSightDescribeTopicRequest,
    QuickSightDescribeTopicResponse,
    QuickSightDescribeTopicV2Request,
    QuickSightDescribeTopicV2Response,
    QuickSightDescribeUserRequest,
    QuickSightDescribeUserResponse,
    QuickSightDescribeVPCConnectionRequest,
    QuickSightDescribeVPCConnectionResponse,
    QuickSightGenerateEmbedUrlForAnonymousUserRequest,
    QuickSightGenerateEmbedUrlForAnonymousUserResponse,
    QuickSightGenerateEmbedUrlForRegisteredUserRequest,
    QuickSightGenerateEmbedUrlForRegisteredUserResponse,
    QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityRequest,
    QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityResponse,
    QuickSightGetDashboardEmbedUrlRequest,
    QuickSightGetDashboardEmbedUrlResponse,
    QuickSightGetFlowMetadataRequest,
    QuickSightGetFlowMetadataResponse,
    QuickSightGetFlowPermissionsRequest,
    QuickSightGetFlowPermissionsResponse,
    QuickSightGetIdentityContextRequest,
    QuickSightGetIdentityContextResponse,
    QuickSightGetPolicyAssignmentRequest,
    QuickSightGetPolicyAssignmentResponse,
    QuickSightGetSessionEmbedUrlRequest,
    QuickSightGetSessionEmbedUrlResponse,
    QuickSightListAccessControlApplicationsRequest,
    QuickSightListAccessControlApplicationsResponse,
    QuickSightListActionConnectorsRequest,
    QuickSightListActionConnectorsResponse,
    QuickSightListAgentsRequest,
    QuickSightListAgentsResponse,
    QuickSightListAnalysesRequest,
    QuickSightListAnalysesResponse,
    QuickSightListApprovalPoliciesRequest,
    QuickSightListApprovalPoliciesResponse,
    QuickSightListAppsRequest,
    QuickSightListAppsResponse,
    QuickSightListAssetBundleExportJobsRequest,
    QuickSightListAssetBundleExportJobsResponse,
    QuickSightListAssetBundleImportJobsRequest,
    QuickSightListAssetBundleImportJobsResponse,
    QuickSightListBrandsRequest,
    QuickSightListBrandsResponse,
    QuickSightListCustomPermissionsRequest,
    QuickSightListCustomPermissionsResponse,
    QuickSightListDashboardVersionsRequest,
    QuickSightListDashboardVersionsResponse,
    QuickSightListDashboardsRequest,
    QuickSightListDashboardsResponse,
    QuickSightListDataSetsRequest,
    QuickSightListDataSetsResponse,
    QuickSightListDataSourcesRequest,
    QuickSightListDataSourcesResponse,
    QuickSightListDlpSettingsRequest,
    QuickSightListDlpSettingsResponse,
    QuickSightListFlowsRequest,
    QuickSightListFlowsResponse,
    QuickSightListFolderMembersRequest,
    QuickSightListFolderMembersResponse,
    QuickSightListFoldersForResourceRequest,
    QuickSightListFoldersForResourceResponse,
    QuickSightListFoldersRequest,
    QuickSightListFoldersResponse,
    QuickSightListGroupMembershipsRequest,
    QuickSightListGroupMembershipsResponse,
    QuickSightListGroupsRequest,
    QuickSightListGroupsResponse,
    QuickSightListIAMPolicyAssignmentsForUserRequest,
    QuickSightListIAMPolicyAssignmentsForUserResponse,
    QuickSightListIAMPolicyAssignmentsRequest,
    QuickSightListIAMPolicyAssignmentsResponse,
    QuickSightListIdentityPropagationConfigsRequest,
    QuickSightListIdentityPropagationConfigsResponse,
    QuickSightListInboundConnectorApplicationAssociationsRequest,
    QuickSightListInboundConnectorApplicationAssociationsResponse,
    QuickSightListInboundConnectorsRequest,
    QuickSightListInboundConnectorsResponse,
    QuickSightListIngestionsRequest,
    QuickSightListIngestionsResponse,
    QuickSightListKnowledgeBaseRefreshSchedulesRequest,
    QuickSightListKnowledgeBaseRefreshSchedulesResponse,
    QuickSightListKnowledgeBasesRequest,
    QuickSightListKnowledgeBasesResponse,
    QuickSightListLimitsProfilesRequest,
    QuickSightListLimitsProfilesResponse,
    QuickSightListNamespacesRequest,
    QuickSightListNamespacesResponse,
    QuickSightListOAuthClientApplicationsRequest,
    QuickSightListOAuthClientApplicationsResponse,
    QuickSightListPrincipalsForPolicyRequest,
    QuickSightListPrincipalsForPolicyResponse,
    QuickSightListRefreshSchedulesRequest,
    QuickSightListRefreshSchedulesResponse,
    QuickSightListRoleMembershipsRequest,
    QuickSightListRoleMembershipsResponse,
    QuickSightListSelfUpgradesRequest,
    QuickSightListSelfUpgradesResponse,
    QuickSightListSpaceResourcesRequest,
    QuickSightListSpaceResourcesResponse,
    QuickSightListSpacesRequest,
    QuickSightListSpacesResponse,
    QuickSightListTagsForResourceRequest,
    QuickSightListTagsForResourceResponse,
    QuickSightListTemplateAliasesRequest,
    QuickSightListTemplateAliasesResponse,
    QuickSightListTemplateVersionsRequest,
    QuickSightListTemplateVersionsResponse,
    QuickSightListTemplatesRequest,
    QuickSightListTemplatesResponse,
    QuickSightListThemeAliasesRequest,
    QuickSightListThemeAliasesResponse,
    QuickSightListThemeVersionsRequest,
    QuickSightListThemeVersionsResponse,
    QuickSightListThemesRequest,
    QuickSightListThemesResponse,
    QuickSightListTopicRefreshSchedulesRequest,
    QuickSightListTopicRefreshSchedulesResponse,
    QuickSightListTopicReviewedAnswersRequest,
    QuickSightListTopicReviewedAnswersResponse,
    QuickSightListTopicsRequest,
    QuickSightListTopicsResponse,
    QuickSightListTopicsV2Request,
    QuickSightListTopicsV2Response,
    QuickSightListUserGroupsRequest,
    QuickSightListUserGroupsResponse,
    QuickSightListUsersIndexCapacityRequest,
    QuickSightListUsersIndexCapacityResponse,
    QuickSightListUsersRequest,
    QuickSightListUsersResponse,
    QuickSightListVPCConnectionsRequest,
    QuickSightListVPCConnectionsResponse,
    QuickSightPredictQAResultsRequest,
    QuickSightPredictQAResultsResponse,
    QuickSightPutDataSetRefreshPropertiesRequest,
    QuickSightPutDataSetRefreshPropertiesResponse,
    QuickSightPutPolicyAssignmentRequest,
    QuickSightPutPolicyAssignmentResponse,
    QuickSightRegisterUserRequest,
    QuickSightRegisterUserResponse,
    QuickSightRestoreAnalysisRequest,
    QuickSightRestoreAnalysisResponse,
    QuickSightSearchActionConnectorsRequest,
    QuickSightSearchActionConnectorsResponse,
    QuickSightSearchAgentsRequest,
    QuickSightSearchAgentsResponse,
    QuickSightSearchAnalysesRequest,
    QuickSightSearchAnalysesResponse,
    QuickSightSearchAppsRequest,
    QuickSightSearchAppsResponse,
    QuickSightSearchDashboardsRequest,
    QuickSightSearchDashboardsResponse,
    QuickSightSearchDataSetsRequest,
    QuickSightSearchDataSetsResponse,
    QuickSightSearchDataSourcesRequest,
    QuickSightSearchDataSourcesResponse,
    QuickSightSearchFlowsRequest,
    QuickSightSearchFlowsResponse,
    QuickSightSearchFoldersRequest,
    QuickSightSearchFoldersResponse,
    QuickSightSearchGroupsRequest,
    QuickSightSearchGroupsResponse,
    QuickSightSearchKnowledgeBasesRequest,
    QuickSightSearchKnowledgeBasesResponse,
    QuickSightSearchSpacesRequest,
    QuickSightSearchSpacesResponse,
    QuickSightSearchTopicsRequest,
    QuickSightSearchTopicsResponse,
    QuickSightSearchTopicsV2Request,
    QuickSightSearchTopicsV2Response,
    QuickSightStartAssetBundleExportJobRequest,
    QuickSightStartAssetBundleExportJobResponse,
    QuickSightStartAssetBundleImportJobRequest,
    QuickSightStartAssetBundleImportJobResponse,
    QuickSightStartAutomationJobRequest,
    QuickSightStartAutomationJobResponse,
    QuickSightStartDashboardSnapshotJobRequest,
    QuickSightStartDashboardSnapshotJobResponse,
    QuickSightStartDashboardSnapshotJobScheduleRequest,
    QuickSightStartDashboardSnapshotJobScheduleResponse,
    QuickSightTagResourceRequest,
    QuickSightTagResourceResponse,
    QuickSightUntagResourceRequest,
    QuickSightUntagResourceResponse,
    QuickSightUpdateAccessControlApplicationRequest,
    QuickSightUpdateAccessControlApplicationResponse,
    QuickSightUpdateAccessControlApplicationSecretRequest,
    QuickSightUpdateAccessControlApplicationSecretResponse,
    QuickSightUpdateAccountCustomPermissionRequest,
    QuickSightUpdateAccountCustomPermissionResponse,
    QuickSightUpdateAccountCustomizationRequest,
    QuickSightUpdateAccountCustomizationResponse,
    QuickSightUpdateAccountSettingsRequest,
    QuickSightUpdateAccountSettingsResponse,
    QuickSightUpdateActionConnectorPermissionsRequest,
    QuickSightUpdateActionConnectorPermissionsResponse,
    QuickSightUpdateActionConnectorRequest,
    QuickSightUpdateActionConnectorResponse,
    QuickSightUpdateAgentPermissionsRequest,
    QuickSightUpdateAgentPermissionsResponse,
    QuickSightUpdateAgentRequest,
    QuickSightUpdateAgentResponse,
    QuickSightUpdateAnalysisPermissionsRequest,
    QuickSightUpdateAnalysisPermissionsResponse,
    QuickSightUpdateAnalysisRequest,
    QuickSightUpdateAnalysisResponse,
    QuickSightUpdateAppPermissionsRequest,
    QuickSightUpdateAppPermissionsResponse,
    QuickSightUpdateApplicationWithTokenExchangeGrantRequest,
    QuickSightUpdateApplicationWithTokenExchangeGrantResponse,
    QuickSightUpdateApprovalPolicyRequest,
    QuickSightUpdateApprovalPolicyResponse,
    QuickSightUpdateBrandAssignmentRequest,
    QuickSightUpdateBrandAssignmentResponse,
    QuickSightUpdateBrandPublishedVersionRequest,
    QuickSightUpdateBrandPublishedVersionResponse,
    QuickSightUpdateBrandRequest,
    QuickSightUpdateBrandResponse,
    QuickSightUpdateCustomPermissionsRequest,
    QuickSightUpdateCustomPermissionsResponse,
    QuickSightUpdateDashboardLinksRequest,
    QuickSightUpdateDashboardLinksResponse,
    QuickSightUpdateDashboardPermissionsRequest,
    QuickSightUpdateDashboardPermissionsResponse,
    QuickSightUpdateDashboardPublishedVersionRequest,
    QuickSightUpdateDashboardPublishedVersionResponse,
    QuickSightUpdateDashboardRequest,
    QuickSightUpdateDashboardResponse,
    QuickSightUpdateDashboardsQAConfigurationRequest,
    QuickSightUpdateDashboardsQAConfigurationResponse,
    QuickSightUpdateDataSetPermissionsRequest,
    QuickSightUpdateDataSetPermissionsResponse,
    QuickSightUpdateDataSetRequest,
    QuickSightUpdateDataSetResponse,
    QuickSightUpdateDataSourcePermissionsRequest,
    QuickSightUpdateDataSourcePermissionsResponse,
    QuickSightUpdateDataSourceRequest,
    QuickSightUpdateDataSourceResponse,
    QuickSightUpdateDefaultQBusinessApplicationRequest,
    QuickSightUpdateDefaultQBusinessApplicationResponse,
    QuickSightUpdateDlpSettingRequest,
    QuickSightUpdateDlpSettingResponse,
    QuickSightUpdateFlowPermissionsRequest,
    QuickSightUpdateFlowPermissionsResponse,
    QuickSightUpdateFlowRequest,
    QuickSightUpdateFlowResponse,
    QuickSightUpdateFolderPermissionsRequest,
    QuickSightUpdateFolderPermissionsResponse,
    QuickSightUpdateFolderRequest,
    QuickSightUpdateFolderResponse,
    QuickSightUpdateGroupRequest,
    QuickSightUpdateGroupResponse,
    QuickSightUpdateIAMPolicyAssignmentRequest,
    QuickSightUpdateIAMPolicyAssignmentResponse,
    QuickSightUpdateIdentityPropagationConfigRequest,
    QuickSightUpdateIdentityPropagationConfigResponse,
    QuickSightUpdateInboundConnectorApplicationAssociationsRequest,
    QuickSightUpdateInboundConnectorApplicationAssociationsResponse,
    QuickSightUpdateInboundConnectorRequest,
    QuickSightUpdateInboundConnectorResponse,
    QuickSightUpdateIpRestrictionRequest,
    QuickSightUpdateIpRestrictionResponse,
    QuickSightUpdateKeyRegistrationRequest,
    QuickSightUpdateKeyRegistrationResponse,
    QuickSightUpdateKnowledgeBasePermissionsRequest,
    QuickSightUpdateKnowledgeBasePermissionsResponse,
    QuickSightUpdateKnowledgeBaseRefreshScheduleRequest,
    QuickSightUpdateKnowledgeBaseRefreshScheduleResponse,
    QuickSightUpdateKnowledgeBaseRequest,
    QuickSightUpdateKnowledgeBaseResponse,
    QuickSightUpdateLimitsProfileRequest,
    QuickSightUpdateLimitsProfileResponse,
    QuickSightUpdateOAuthClientApplicationRequest,
    QuickSightUpdateOAuthClientApplicationResponse,
    QuickSightUpdatePublicSharingSettingsRequest,
    QuickSightUpdatePublicSharingSettingsResponse,
    QuickSightUpdateQPersonalizationConfigurationRequest,
    QuickSightUpdateQPersonalizationConfigurationResponse,
    QuickSightUpdateQuickSightQSearchConfigurationRequest,
    QuickSightUpdateQuickSightQSearchConfigurationResponse,
    QuickSightUpdateRefreshScheduleRequest,
    QuickSightUpdateRefreshScheduleResponse,
    QuickSightUpdateResourcePermissionsRequest,
    QuickSightUpdateResourcePermissionsResponse,
    QuickSightUpdateRoleCustomPermissionRequest,
    QuickSightUpdateRoleCustomPermissionResponse,
    QuickSightUpdateSPICECapacityConfigurationRequest,
    QuickSightUpdateSPICECapacityConfigurationResponse,
    QuickSightUpdateSelfUpgradeConfigurationRequest,
    QuickSightUpdateSelfUpgradeConfigurationResponse,
    QuickSightUpdateSelfUpgradeRequest,
    QuickSightUpdateSelfUpgradeResponse,
    QuickSightUpdateSpacePermissionsRequest,
    QuickSightUpdateSpacePermissionsResponse,
    QuickSightUpdateSpaceRequest,
    QuickSightUpdateSpaceResourcesRequest,
    QuickSightUpdateSpaceResourcesResponse,
    QuickSightUpdateSpaceResponse,
    QuickSightUpdateTemplateAliasRequest,
    QuickSightUpdateTemplateAliasResponse,
    QuickSightUpdateTemplatePermissionsRequest,
    QuickSightUpdateTemplatePermissionsResponse,
    QuickSightUpdateTemplateRequest,
    QuickSightUpdateTemplateResponse,
    QuickSightUpdateThemeAliasRequest,
    QuickSightUpdateThemeAliasResponse,
    QuickSightUpdateThemePermissionsRequest,
    QuickSightUpdateThemePermissionsResponse,
    QuickSightUpdateThemeRequest,
    QuickSightUpdateThemeResponse,
    QuickSightUpdateTopicPermissionsRequest,
    QuickSightUpdateTopicPermissionsResponse,
    QuickSightUpdateTopicPermissionsV2Request,
    QuickSightUpdateTopicPermissionsV2Response,
    QuickSightUpdateTopicRefreshScheduleRequest,
    QuickSightUpdateTopicRefreshScheduleResponse,
    QuickSightUpdateTopicRequest,
    QuickSightUpdateTopicResponse,
    QuickSightUpdateTopicV2Request,
    QuickSightUpdateTopicV2Response,
    QuickSightUpdateUserCustomPermissionRequest,
    QuickSightUpdateUserCustomPermissionResponse,
    QuickSightUpdateUserRequest,
    QuickSightUpdateUserResponse,
    QuickSightUpdateVPCConnectionRequest,
    QuickSightUpdateVPCConnectionResponse,
)
from werkflow_aws.types.quicksight_client import QuickSightClient
from .base import AWSBaseService


class AWSQuickSight(AWSBaseService[QuickSightClient]):
    service_name = 'quicksight'
    boto3_service_name = 'quicksight'

    def __init__(self) -> None:
        super().__init__(service_name='quicksight', boto3_service_name='quicksight')

    async def batch_create_topic_reviewed_answer(
        self,
        request: QuickSightBatchCreateTopicReviewedAnswerRequest,
    ) -> QuickSightBatchCreateTopicReviewedAnswerResponse:
        client = self._require_client()
        return await self._execute(client.batch_create_topic_reviewed_answer, request, QuickSightBatchCreateTopicReviewedAnswerResponse)

    async def batch_delete_knowledge_base(
        self,
        request: QuickSightBatchDeleteKnowledgeBaseRequest,
    ) -> QuickSightBatchDeleteKnowledgeBaseResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_knowledge_base, request, QuickSightBatchDeleteKnowledgeBaseResponse)

    async def batch_delete_policy_assignment_by_policy(
        self,
        request: QuickSightBatchDeletePolicyAssignmentByPolicyRequest,
    ) -> QuickSightBatchDeletePolicyAssignmentByPolicyResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_policy_assignment_by_policy, request, QuickSightBatchDeletePolicyAssignmentByPolicyResponse)

    async def batch_delete_topic_reviewed_answer(
        self,
        request: QuickSightBatchDeleteTopicReviewedAnswerRequest,
    ) -> QuickSightBatchDeleteTopicReviewedAnswerResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_topic_reviewed_answer, request, QuickSightBatchDeleteTopicReviewedAnswerResponse)

    async def batch_describe_user_limits(
        self,
        request: QuickSightBatchDescribeUserLimitsRequest,
    ) -> QuickSightBatchDescribeUserLimitsResponse:
        client = self._require_client()
        return await self._execute(client.batch_describe_user_limits, request, QuickSightBatchDescribeUserLimitsResponse)

    async def batch_put_policy_assignment_by_policy(
        self,
        request: QuickSightBatchPutPolicyAssignmentByPolicyRequest,
    ) -> QuickSightBatchPutPolicyAssignmentByPolicyResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_policy_assignment_by_policy, request, QuickSightBatchPutPolicyAssignmentByPolicyResponse)

    async def cancel_ingestion(
        self,
        request: QuickSightCancelIngestionRequest,
    ) -> QuickSightCancelIngestionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_ingestion, request, QuickSightCancelIngestionResponse)

    async def create_access_control_application(
        self,
        request: QuickSightCreateAccessControlApplicationRequest,
    ) -> QuickSightCreateAccessControlApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_access_control_application, request, QuickSightCreateAccessControlApplicationResponse)

    async def create_access_control_application_secret(
        self,
        request: QuickSightCreateAccessControlApplicationSecretRequest,
    ) -> QuickSightCreateAccessControlApplicationSecretResponse:
        client = self._require_client()
        return await self._execute(client.create_access_control_application_secret, request, QuickSightCreateAccessControlApplicationSecretResponse)

    async def create_account_customization(
        self,
        request: QuickSightCreateAccountCustomizationRequest,
    ) -> QuickSightCreateAccountCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.create_account_customization, request, QuickSightCreateAccountCustomizationResponse)

    async def create_account_subscription(
        self,
        request: QuickSightCreateAccountSubscriptionRequest,
    ) -> QuickSightCreateAccountSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_account_subscription, request, QuickSightCreateAccountSubscriptionResponse)

    async def create_action_connector(
        self,
        request: QuickSightCreateActionConnectorRequest,
    ) -> QuickSightCreateActionConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_action_connector, request, QuickSightCreateActionConnectorResponse)

    async def create_agent(
        self,
        request: QuickSightCreateAgentRequest,
    ) -> QuickSightCreateAgentResponse:
        client = self._require_client()
        return await self._execute(client.create_agent, request, QuickSightCreateAgentResponse)

    async def create_analysis(
        self,
        request: QuickSightCreateAnalysisRequest,
    ) -> QuickSightCreateAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.create_analysis, request, QuickSightCreateAnalysisResponse)

    async def create_approval_policy(
        self,
        request: QuickSightCreateApprovalPolicyRequest,
    ) -> QuickSightCreateApprovalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_approval_policy, request, QuickSightCreateApprovalPolicyResponse)

    async def create_brand(
        self,
        request: QuickSightCreateBrandRequest,
    ) -> QuickSightCreateBrandResponse:
        client = self._require_client()
        return await self._execute(client.create_brand, request, QuickSightCreateBrandResponse)

    async def create_custom_permissions(
        self,
        request: QuickSightCreateCustomPermissionsRequest,
    ) -> QuickSightCreateCustomPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_permissions, request, QuickSightCreateCustomPermissionsResponse)

    async def create_dashboard(
        self,
        request: QuickSightCreateDashboardRequest,
    ) -> QuickSightCreateDashboardResponse:
        client = self._require_client()
        return await self._execute(client.create_dashboard, request, QuickSightCreateDashboardResponse)

    async def create_data_set(
        self,
        request: QuickSightCreateDataSetRequest,
    ) -> QuickSightCreateDataSetResponse:
        client = self._require_client()
        return await self._execute(client.create_data_set, request, QuickSightCreateDataSetResponse)

    async def create_data_source(
        self,
        request: QuickSightCreateDataSourceRequest,
    ) -> QuickSightCreateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_data_source, request, QuickSightCreateDataSourceResponse)

    async def create_dlp_setting(
        self,
        request: QuickSightCreateDlpSettingRequest,
    ) -> QuickSightCreateDlpSettingResponse:
        client = self._require_client()
        return await self._execute(client.create_dlp_setting, request, QuickSightCreateDlpSettingResponse)

    async def create_flow(
        self,
        request: QuickSightCreateFlowRequest,
    ) -> QuickSightCreateFlowResponse:
        client = self._require_client()
        return await self._execute(client.create_flow, request, QuickSightCreateFlowResponse)

    async def create_folder(
        self,
        request: QuickSightCreateFolderRequest,
    ) -> QuickSightCreateFolderResponse:
        client = self._require_client()
        return await self._execute(client.create_folder, request, QuickSightCreateFolderResponse)

    async def create_folder_membership(
        self,
        request: QuickSightCreateFolderMembershipRequest,
    ) -> QuickSightCreateFolderMembershipResponse:
        client = self._require_client()
        return await self._execute(client.create_folder_membership, request, QuickSightCreateFolderMembershipResponse)

    async def create_group(
        self,
        request: QuickSightCreateGroupRequest,
    ) -> QuickSightCreateGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_group, request, QuickSightCreateGroupResponse)

    async def create_group_membership(
        self,
        request: QuickSightCreateGroupMembershipRequest,
    ) -> QuickSightCreateGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.create_group_membership, request, QuickSightCreateGroupMembershipResponse)

    async def create_iam_policy_assignment(
        self,
        request: QuickSightCreateIAMPolicyAssignmentRequest,
    ) -> QuickSightCreateIAMPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.create_iam_policy_assignment, request, QuickSightCreateIAMPolicyAssignmentResponse)

    async def create_inbound_connector(
        self,
        request: QuickSightCreateInboundConnectorRequest,
    ) -> QuickSightCreateInboundConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_inbound_connector, request, QuickSightCreateInboundConnectorResponse)

    async def create_ingestion(
        self,
        request: QuickSightCreateIngestionRequest,
    ) -> QuickSightCreateIngestionResponse:
        client = self._require_client()
        return await self._execute(client.create_ingestion, request, QuickSightCreateIngestionResponse)

    async def create_knowledge_base(
        self,
        request: QuickSightCreateKnowledgeBaseRequest,
    ) -> QuickSightCreateKnowledgeBaseResponse:
        client = self._require_client()
        return await self._execute(client.create_knowledge_base, request, QuickSightCreateKnowledgeBaseResponse)

    async def create_knowledge_base_refresh_schedule(
        self,
        request: QuickSightCreateKnowledgeBaseRefreshScheduleRequest,
    ) -> QuickSightCreateKnowledgeBaseRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_knowledge_base_refresh_schedule, request, QuickSightCreateKnowledgeBaseRefreshScheduleResponse)

    async def create_limits_profile(
        self,
        request: QuickSightCreateLimitsProfileRequest,
    ) -> QuickSightCreateLimitsProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_limits_profile, request, QuickSightCreateLimitsProfileResponse)

    async def create_namespace(
        self,
        request: QuickSightCreateNamespaceRequest,
    ) -> QuickSightCreateNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.create_namespace, request, QuickSightCreateNamespaceResponse)

    async def create_o_auth_client_application(
        self,
        request: QuickSightCreateOAuthClientApplicationRequest,
    ) -> QuickSightCreateOAuthClientApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_o_auth_client_application, request, QuickSightCreateOAuthClientApplicationResponse)

    async def create_refresh_schedule(
        self,
        request: QuickSightCreateRefreshScheduleRequest,
    ) -> QuickSightCreateRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_refresh_schedule, request, QuickSightCreateRefreshScheduleResponse)

    async def create_role_membership(
        self,
        request: QuickSightCreateRoleMembershipRequest,
    ) -> QuickSightCreateRoleMembershipResponse:
        client = self._require_client()
        return await self._execute(client.create_role_membership, request, QuickSightCreateRoleMembershipResponse)

    async def create_space(
        self,
        request: QuickSightCreateSpaceRequest,
    ) -> QuickSightCreateSpaceResponse:
        client = self._require_client()
        return await self._execute(client.create_space, request, QuickSightCreateSpaceResponse)

    async def create_template(
        self,
        request: QuickSightCreateTemplateRequest,
    ) -> QuickSightCreateTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_template, request, QuickSightCreateTemplateResponse)

    async def create_template_alias(
        self,
        request: QuickSightCreateTemplateAliasRequest,
    ) -> QuickSightCreateTemplateAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_template_alias, request, QuickSightCreateTemplateAliasResponse)

    async def create_theme(
        self,
        request: QuickSightCreateThemeRequest,
    ) -> QuickSightCreateThemeResponse:
        client = self._require_client()
        return await self._execute(client.create_theme, request, QuickSightCreateThemeResponse)

    async def create_theme_alias(
        self,
        request: QuickSightCreateThemeAliasRequest,
    ) -> QuickSightCreateThemeAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_theme_alias, request, QuickSightCreateThemeAliasResponse)

    async def create_topic(
        self,
        request: QuickSightCreateTopicRequest,
    ) -> QuickSightCreateTopicResponse:
        client = self._require_client()
        return await self._execute(client.create_topic, request, QuickSightCreateTopicResponse)

    async def create_topic_refresh_schedule(
        self,
        request: QuickSightCreateTopicRefreshScheduleRequest,
    ) -> QuickSightCreateTopicRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_topic_refresh_schedule, request, QuickSightCreateTopicRefreshScheduleResponse)

    async def create_topic_v2(
        self,
        request: QuickSightCreateTopicV2Request,
    ) -> QuickSightCreateTopicV2Response:
        client = self._require_client()
        return await self._execute(client.create_topic_v2, request, QuickSightCreateTopicV2Response)

    async def create_vpc_connection(
        self,
        request: QuickSightCreateVPCConnectionRequest,
    ) -> QuickSightCreateVPCConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_connection, request, QuickSightCreateVPCConnectionResponse)

    async def delete_access_control_application(
        self,
        request: QuickSightDeleteAccessControlApplicationRequest,
    ) -> QuickSightDeleteAccessControlApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_control_application, request, QuickSightDeleteAccessControlApplicationResponse)

    async def delete_access_control_application_secret(
        self,
        request: QuickSightDeleteAccessControlApplicationSecretRequest,
    ) -> QuickSightDeleteAccessControlApplicationSecretResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_control_application_secret, request, QuickSightDeleteAccessControlApplicationSecretResponse)

    async def delete_account_custom_permission(
        self,
        request: QuickSightDeleteAccountCustomPermissionRequest,
    ) -> QuickSightDeleteAccountCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_custom_permission, request, QuickSightDeleteAccountCustomPermissionResponse)

    async def delete_account_customization(
        self,
        request: QuickSightDeleteAccountCustomizationRequest,
    ) -> QuickSightDeleteAccountCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_customization, request, QuickSightDeleteAccountCustomizationResponse)

    async def delete_account_subscription(
        self,
        request: QuickSightDeleteAccountSubscriptionRequest,
    ) -> QuickSightDeleteAccountSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_subscription, request, QuickSightDeleteAccountSubscriptionResponse)

    async def delete_action_connector(
        self,
        request: QuickSightDeleteActionConnectorRequest,
    ) -> QuickSightDeleteActionConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_action_connector, request, QuickSightDeleteActionConnectorResponse)

    async def delete_agent(
        self,
        request: QuickSightDeleteAgentRequest,
    ) -> QuickSightDeleteAgentResponse:
        client = self._require_client()
        return await self._execute(client.delete_agent, request, QuickSightDeleteAgentResponse)

    async def delete_analysis(
        self,
        request: QuickSightDeleteAnalysisRequest,
    ) -> QuickSightDeleteAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.delete_analysis, request, QuickSightDeleteAnalysisResponse)

    async def delete_app(
        self,
        request: QuickSightDeleteAppRequest,
    ) -> QuickSightDeleteAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_app, request, QuickSightDeleteAppResponse)

    async def delete_approval_policy(
        self,
        request: QuickSightDeleteApprovalPolicyRequest,
    ) -> QuickSightDeleteApprovalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_approval_policy, request, QuickSightDeleteApprovalPolicyResponse)

    async def delete_brand(
        self,
        request: QuickSightDeleteBrandRequest,
    ) -> QuickSightDeleteBrandResponse:
        client = self._require_client()
        return await self._execute(client.delete_brand, request, QuickSightDeleteBrandResponse)

    async def delete_brand_assignment(
        self,
        request: QuickSightDeleteBrandAssignmentRequest,
    ) -> QuickSightDeleteBrandAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_brand_assignment, request, QuickSightDeleteBrandAssignmentResponse)

    async def delete_custom_permissions(
        self,
        request: QuickSightDeleteCustomPermissionsRequest,
    ) -> QuickSightDeleteCustomPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_permissions, request, QuickSightDeleteCustomPermissionsResponse)

    async def delete_dashboard(
        self,
        request: QuickSightDeleteDashboardRequest,
    ) -> QuickSightDeleteDashboardResponse:
        client = self._require_client()
        return await self._execute(client.delete_dashboard, request, QuickSightDeleteDashboardResponse)

    async def delete_data_set(
        self,
        request: QuickSightDeleteDataSetRequest,
    ) -> QuickSightDeleteDataSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_set, request, QuickSightDeleteDataSetResponse)

    async def delete_data_set_refresh_properties(
        self,
        request: QuickSightDeleteDataSetRefreshPropertiesRequest,
    ) -> QuickSightDeleteDataSetRefreshPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_set_refresh_properties, request, QuickSightDeleteDataSetRefreshPropertiesResponse)

    async def delete_data_source(
        self,
        request: QuickSightDeleteDataSourceRequest,
    ) -> QuickSightDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, QuickSightDeleteDataSourceResponse)

    async def delete_default_q_business_application(
        self,
        request: QuickSightDeleteDefaultQBusinessApplicationRequest,
    ) -> QuickSightDeleteDefaultQBusinessApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_default_q_business_application, request, QuickSightDeleteDefaultQBusinessApplicationResponse)

    async def delete_dlp_setting(
        self,
        request: QuickSightDeleteDlpSettingRequest,
    ) -> QuickSightDeleteDlpSettingResponse:
        client = self._require_client()
        return await self._execute(client.delete_dlp_setting, request, QuickSightDeleteDlpSettingResponse)

    async def delete_flow(
        self,
        request: QuickSightDeleteFlowRequest,
    ) -> QuickSightDeleteFlowResponse:
        client = self._require_client()
        return await self._execute(client.delete_flow, request, QuickSightDeleteFlowResponse)

    async def delete_folder(
        self,
        request: QuickSightDeleteFolderRequest,
    ) -> QuickSightDeleteFolderResponse:
        client = self._require_client()
        return await self._execute(client.delete_folder, request, QuickSightDeleteFolderResponse)

    async def delete_folder_membership(
        self,
        request: QuickSightDeleteFolderMembershipRequest,
    ) -> QuickSightDeleteFolderMembershipResponse:
        client = self._require_client()
        return await self._execute(client.delete_folder_membership, request, QuickSightDeleteFolderMembershipResponse)

    async def delete_group(
        self,
        request: QuickSightDeleteGroupRequest,
    ) -> QuickSightDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_group, request, QuickSightDeleteGroupResponse)

    async def delete_group_membership(
        self,
        request: QuickSightDeleteGroupMembershipRequest,
    ) -> QuickSightDeleteGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.delete_group_membership, request, QuickSightDeleteGroupMembershipResponse)

    async def delete_iam_policy_assignment(
        self,
        request: QuickSightDeleteIAMPolicyAssignmentRequest,
    ) -> QuickSightDeleteIAMPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_iam_policy_assignment, request, QuickSightDeleteIAMPolicyAssignmentResponse)

    async def delete_identity_propagation_config(
        self,
        request: QuickSightDeleteIdentityPropagationConfigRequest,
    ) -> QuickSightDeleteIdentityPropagationConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_identity_propagation_config, request, QuickSightDeleteIdentityPropagationConfigResponse)

    async def delete_inbound_connector(
        self,
        request: QuickSightDeleteInboundConnectorRequest,
    ) -> QuickSightDeleteInboundConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_inbound_connector, request, QuickSightDeleteInboundConnectorResponse)

    async def delete_knowledge_base(
        self,
        request: QuickSightDeleteKnowledgeBaseRequest,
    ) -> QuickSightDeleteKnowledgeBaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_knowledge_base, request, QuickSightDeleteKnowledgeBaseResponse)

    async def delete_knowledge_base_refresh_schedule(
        self,
        request: QuickSightDeleteKnowledgeBaseRefreshScheduleRequest,
    ) -> QuickSightDeleteKnowledgeBaseRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_knowledge_base_refresh_schedule, request, QuickSightDeleteKnowledgeBaseRefreshScheduleResponse)

    async def delete_limits_profile(
        self,
        request: QuickSightDeleteLimitsProfileRequest,
    ) -> QuickSightDeleteLimitsProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_limits_profile, request, QuickSightDeleteLimitsProfileResponse)

    async def delete_namespace(
        self,
        request: QuickSightDeleteNamespaceRequest,
    ) -> QuickSightDeleteNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_namespace, request, QuickSightDeleteNamespaceResponse)

    async def delete_o_auth_client_application(
        self,
        request: QuickSightDeleteOAuthClientApplicationRequest,
    ) -> QuickSightDeleteOAuthClientApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_o_auth_client_application, request, QuickSightDeleteOAuthClientApplicationResponse)

    async def delete_policy_assignment(
        self,
        request: QuickSightDeletePolicyAssignmentRequest,
    ) -> QuickSightDeletePolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy_assignment, request, QuickSightDeletePolicyAssignmentResponse)

    async def delete_refresh_schedule(
        self,
        request: QuickSightDeleteRefreshScheduleRequest,
    ) -> QuickSightDeleteRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_refresh_schedule, request, QuickSightDeleteRefreshScheduleResponse)

    async def delete_role_custom_permission(
        self,
        request: QuickSightDeleteRoleCustomPermissionRequest,
    ) -> QuickSightDeleteRoleCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.delete_role_custom_permission, request, QuickSightDeleteRoleCustomPermissionResponse)

    async def delete_role_membership(
        self,
        request: QuickSightDeleteRoleMembershipRequest,
    ) -> QuickSightDeleteRoleMembershipResponse:
        client = self._require_client()
        return await self._execute(client.delete_role_membership, request, QuickSightDeleteRoleMembershipResponse)

    async def delete_space(
        self,
        request: QuickSightDeleteSpaceRequest,
    ) -> QuickSightDeleteSpaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_space, request, QuickSightDeleteSpaceResponse)

    async def delete_template(
        self,
        request: QuickSightDeleteTemplateRequest,
    ) -> QuickSightDeleteTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_template, request, QuickSightDeleteTemplateResponse)

    async def delete_template_alias(
        self,
        request: QuickSightDeleteTemplateAliasRequest,
    ) -> QuickSightDeleteTemplateAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_template_alias, request, QuickSightDeleteTemplateAliasResponse)

    async def delete_theme(
        self,
        request: QuickSightDeleteThemeRequest,
    ) -> QuickSightDeleteThemeResponse:
        client = self._require_client()
        return await self._execute(client.delete_theme, request, QuickSightDeleteThemeResponse)

    async def delete_theme_alias(
        self,
        request: QuickSightDeleteThemeAliasRequest,
    ) -> QuickSightDeleteThemeAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_theme_alias, request, QuickSightDeleteThemeAliasResponse)

    async def delete_topic(
        self,
        request: QuickSightDeleteTopicRequest,
    ) -> QuickSightDeleteTopicResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic, request, QuickSightDeleteTopicResponse)

    async def delete_topic_refresh_schedule(
        self,
        request: QuickSightDeleteTopicRefreshScheduleRequest,
    ) -> QuickSightDeleteTopicRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic_refresh_schedule, request, QuickSightDeleteTopicRefreshScheduleResponse)

    async def delete_topic_v2(
        self,
        request: QuickSightDeleteTopicV2Request,
    ) -> QuickSightDeleteTopicV2Response:
        client = self._require_client()
        return await self._execute(client.delete_topic_v2, request, QuickSightDeleteTopicV2Response)

    async def delete_user(
        self,
        request: QuickSightDeleteUserRequest,
    ) -> QuickSightDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, QuickSightDeleteUserResponse)

    async def delete_user_by_principal_id(
        self,
        request: QuickSightDeleteUserByPrincipalIdRequest,
    ) -> QuickSightDeleteUserByPrincipalIdResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_by_principal_id, request, QuickSightDeleteUserByPrincipalIdResponse)

    async def delete_user_custom_permission(
        self,
        request: QuickSightDeleteUserCustomPermissionRequest,
    ) -> QuickSightDeleteUserCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_custom_permission, request, QuickSightDeleteUserCustomPermissionResponse)

    async def delete_vpc_connection(
        self,
        request: QuickSightDeleteVPCConnectionRequest,
    ) -> QuickSightDeleteVPCConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_connection, request, QuickSightDeleteVPCConnectionResponse)

    async def describe_access_control_application(
        self,
        request: QuickSightDescribeAccessControlApplicationRequest,
    ) -> QuickSightDescribeAccessControlApplicationResponse:
        client = self._require_client()
        return await self._execute(client.describe_access_control_application, request, QuickSightDescribeAccessControlApplicationResponse)

    async def describe_account_custom_permission(
        self,
        request: QuickSightDescribeAccountCustomPermissionRequest,
    ) -> QuickSightDescribeAccountCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_custom_permission, request, QuickSightDescribeAccountCustomPermissionResponse)

    async def describe_account_customization(
        self,
        request: QuickSightDescribeAccountCustomizationRequest,
    ) -> QuickSightDescribeAccountCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_customization, request, QuickSightDescribeAccountCustomizationResponse)

    async def describe_account_settings(
        self,
        request: QuickSightDescribeAccountSettingsRequest,
    ) -> QuickSightDescribeAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_settings, request, QuickSightDescribeAccountSettingsResponse)

    async def describe_account_subscription(
        self,
        request: QuickSightDescribeAccountSubscriptionRequest,
    ) -> QuickSightDescribeAccountSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_subscription, request, QuickSightDescribeAccountSubscriptionResponse)

    async def describe_action_connector(
        self,
        request: QuickSightDescribeActionConnectorRequest,
    ) -> QuickSightDescribeActionConnectorResponse:
        client = self._require_client()
        return await self._execute(client.describe_action_connector, request, QuickSightDescribeActionConnectorResponse)

    async def describe_action_connector_permissions(
        self,
        request: QuickSightDescribeActionConnectorPermissionsRequest,
    ) -> QuickSightDescribeActionConnectorPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_action_connector_permissions, request, QuickSightDescribeActionConnectorPermissionsResponse)

    async def describe_agent(
        self,
        request: QuickSightDescribeAgentRequest,
    ) -> QuickSightDescribeAgentResponse:
        client = self._require_client()
        return await self._execute(client.describe_agent, request, QuickSightDescribeAgentResponse)

    async def describe_agent_permissions(
        self,
        request: QuickSightDescribeAgentPermissionsRequest,
    ) -> QuickSightDescribeAgentPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_agent_permissions, request, QuickSightDescribeAgentPermissionsResponse)

    async def describe_analysis(
        self,
        request: QuickSightDescribeAnalysisRequest,
    ) -> QuickSightDescribeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.describe_analysis, request, QuickSightDescribeAnalysisResponse)

    async def describe_analysis_definition(
        self,
        request: QuickSightDescribeAnalysisDefinitionRequest,
    ) -> QuickSightDescribeAnalysisDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_analysis_definition, request, QuickSightDescribeAnalysisDefinitionResponse)

    async def describe_analysis_permissions(
        self,
        request: QuickSightDescribeAnalysisPermissionsRequest,
    ) -> QuickSightDescribeAnalysisPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_analysis_permissions, request, QuickSightDescribeAnalysisPermissionsResponse)

    async def describe_app(
        self,
        request: QuickSightDescribeAppRequest,
    ) -> QuickSightDescribeAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_app, request, QuickSightDescribeAppResponse)

    async def describe_app_permissions(
        self,
        request: QuickSightDescribeAppPermissionsRequest,
    ) -> QuickSightDescribeAppPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_permissions, request, QuickSightDescribeAppPermissionsResponse)

    async def describe_approval_policy(
        self,
        request: QuickSightDescribeApprovalPolicyRequest,
    ) -> QuickSightDescribeApprovalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_approval_policy, request, QuickSightDescribeApprovalPolicyResponse)

    async def describe_asset_bundle_export_job(
        self,
        request: QuickSightDescribeAssetBundleExportJobRequest,
    ) -> QuickSightDescribeAssetBundleExportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_asset_bundle_export_job, request, QuickSightDescribeAssetBundleExportJobResponse)

    async def describe_asset_bundle_import_job(
        self,
        request: QuickSightDescribeAssetBundleImportJobRequest,
    ) -> QuickSightDescribeAssetBundleImportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_asset_bundle_import_job, request, QuickSightDescribeAssetBundleImportJobResponse)

    async def describe_automation_job(
        self,
        request: QuickSightDescribeAutomationJobRequest,
    ) -> QuickSightDescribeAutomationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_automation_job, request, QuickSightDescribeAutomationJobResponse)

    async def describe_brand(
        self,
        request: QuickSightDescribeBrandRequest,
    ) -> QuickSightDescribeBrandResponse:
        client = self._require_client()
        return await self._execute(client.describe_brand, request, QuickSightDescribeBrandResponse)

    async def describe_brand_assignment(
        self,
        request: QuickSightDescribeBrandAssignmentRequest,
    ) -> QuickSightDescribeBrandAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_brand_assignment, request, QuickSightDescribeBrandAssignmentResponse)

    async def describe_brand_published_version(
        self,
        request: QuickSightDescribeBrandPublishedVersionRequest,
    ) -> QuickSightDescribeBrandPublishedVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_brand_published_version, request, QuickSightDescribeBrandPublishedVersionResponse)

    async def describe_custom_permissions(
        self,
        request: QuickSightDescribeCustomPermissionsRequest,
    ) -> QuickSightDescribeCustomPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_permissions, request, QuickSightDescribeCustomPermissionsResponse)

    async def describe_dashboard(
        self,
        request: QuickSightDescribeDashboardRequest,
    ) -> QuickSightDescribeDashboardResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboard, request, QuickSightDescribeDashboardResponse)

    async def describe_dashboard_definition(
        self,
        request: QuickSightDescribeDashboardDefinitionRequest,
    ) -> QuickSightDescribeDashboardDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboard_definition, request, QuickSightDescribeDashboardDefinitionResponse)

    async def describe_dashboard_permissions(
        self,
        request: QuickSightDescribeDashboardPermissionsRequest,
    ) -> QuickSightDescribeDashboardPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboard_permissions, request, QuickSightDescribeDashboardPermissionsResponse)

    async def describe_dashboard_snapshot_job(
        self,
        request: QuickSightDescribeDashboardSnapshotJobRequest,
    ) -> QuickSightDescribeDashboardSnapshotJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboard_snapshot_job, request, QuickSightDescribeDashboardSnapshotJobResponse)

    async def describe_dashboard_snapshot_job_result(
        self,
        request: QuickSightDescribeDashboardSnapshotJobResultRequest,
    ) -> QuickSightDescribeDashboardSnapshotJobResultResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboard_snapshot_job_result, request, QuickSightDescribeDashboardSnapshotJobResultResponse)

    async def describe_dashboards_qa_configuration(
        self,
        request: QuickSightDescribeDashboardsQAConfigurationRequest,
    ) -> QuickSightDescribeDashboardsQAConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_dashboards_qa_configuration, request, QuickSightDescribeDashboardsQAConfigurationResponse)

    async def describe_data_set(
        self,
        request: QuickSightDescribeDataSetRequest,
    ) -> QuickSightDescribeDataSetResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_set, request, QuickSightDescribeDataSetResponse)

    async def describe_data_set_permissions(
        self,
        request: QuickSightDescribeDataSetPermissionsRequest,
    ) -> QuickSightDescribeDataSetPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_set_permissions, request, QuickSightDescribeDataSetPermissionsResponse)

    async def describe_data_set_refresh_properties(
        self,
        request: QuickSightDescribeDataSetRefreshPropertiesRequest,
    ) -> QuickSightDescribeDataSetRefreshPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_set_refresh_properties, request, QuickSightDescribeDataSetRefreshPropertiesResponse)

    async def describe_data_source(
        self,
        request: QuickSightDescribeDataSourceRequest,
    ) -> QuickSightDescribeDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_source, request, QuickSightDescribeDataSourceResponse)

    async def describe_data_source_permissions(
        self,
        request: QuickSightDescribeDataSourcePermissionsRequest,
    ) -> QuickSightDescribeDataSourcePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_source_permissions, request, QuickSightDescribeDataSourcePermissionsResponse)

    async def describe_default_q_business_application(
        self,
        request: QuickSightDescribeDefaultQBusinessApplicationRequest,
    ) -> QuickSightDescribeDefaultQBusinessApplicationResponse:
        client = self._require_client()
        return await self._execute(client.describe_default_q_business_application, request, QuickSightDescribeDefaultQBusinessApplicationResponse)

    async def describe_dlp_setting(
        self,
        request: QuickSightDescribeDlpSettingRequest,
    ) -> QuickSightDescribeDlpSettingResponse:
        client = self._require_client()
        return await self._execute(client.describe_dlp_setting, request, QuickSightDescribeDlpSettingResponse)

    async def describe_flow(
        self,
        request: QuickSightDescribeFlowRequest,
    ) -> QuickSightDescribeFlowResponse:
        client = self._require_client()
        return await self._execute(client.describe_flow, request, QuickSightDescribeFlowResponse)

    async def describe_folder(
        self,
        request: QuickSightDescribeFolderRequest,
    ) -> QuickSightDescribeFolderResponse:
        client = self._require_client()
        return await self._execute(client.describe_folder, request, QuickSightDescribeFolderResponse)

    async def describe_folder_permissions(
        self,
        request: QuickSightDescribeFolderPermissionsRequest,
    ) -> QuickSightDescribeFolderPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_folder_permissions, request, QuickSightDescribeFolderPermissionsResponse)

    async def describe_folder_permissions_paginated(
        self,
        request: QuickSightDescribeFolderPermissionsRequest,
    ) -> list[QuickSightDescribeFolderPermissionsResponse]:
        return await self._paginate('describe_folder_permissions', request, QuickSightDescribeFolderPermissionsResponse)

    async def describe_folder_resolved_permissions(
        self,
        request: QuickSightDescribeFolderResolvedPermissionsRequest,
    ) -> QuickSightDescribeFolderResolvedPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_folder_resolved_permissions, request, QuickSightDescribeFolderResolvedPermissionsResponse)

    async def describe_folder_resolved_permissions_paginated(
        self,
        request: QuickSightDescribeFolderResolvedPermissionsRequest,
    ) -> list[QuickSightDescribeFolderResolvedPermissionsResponse]:
        return await self._paginate('describe_folder_resolved_permissions', request, QuickSightDescribeFolderResolvedPermissionsResponse)

    async def describe_group(
        self,
        request: QuickSightDescribeGroupRequest,
    ) -> QuickSightDescribeGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_group, request, QuickSightDescribeGroupResponse)

    async def describe_group_membership(
        self,
        request: QuickSightDescribeGroupMembershipRequest,
    ) -> QuickSightDescribeGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.describe_group_membership, request, QuickSightDescribeGroupMembershipResponse)

    async def describe_iam_policy_assignment(
        self,
        request: QuickSightDescribeIAMPolicyAssignmentRequest,
    ) -> QuickSightDescribeIAMPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_iam_policy_assignment, request, QuickSightDescribeIAMPolicyAssignmentResponse)

    async def describe_inbound_connector(
        self,
        request: QuickSightDescribeInboundConnectorRequest,
    ) -> QuickSightDescribeInboundConnectorResponse:
        client = self._require_client()
        return await self._execute(client.describe_inbound_connector, request, QuickSightDescribeInboundConnectorResponse)

    async def describe_ingestion(
        self,
        request: QuickSightDescribeIngestionRequest,
    ) -> QuickSightDescribeIngestionResponse:
        client = self._require_client()
        return await self._execute(client.describe_ingestion, request, QuickSightDescribeIngestionResponse)

    async def describe_ip_restriction(
        self,
        request: QuickSightDescribeIpRestrictionRequest,
    ) -> QuickSightDescribeIpRestrictionResponse:
        client = self._require_client()
        return await self._execute(client.describe_ip_restriction, request, QuickSightDescribeIpRestrictionResponse)

    async def describe_key_registration(
        self,
        request: QuickSightDescribeKeyRegistrationRequest,
    ) -> QuickSightDescribeKeyRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.describe_key_registration, request, QuickSightDescribeKeyRegistrationResponse)

    async def describe_knowledge_base(
        self,
        request: QuickSightDescribeKnowledgeBaseRequest,
    ) -> QuickSightDescribeKnowledgeBaseResponse:
        client = self._require_client()
        return await self._execute(client.describe_knowledge_base, request, QuickSightDescribeKnowledgeBaseResponse)

    async def describe_knowledge_base_permissions(
        self,
        request: QuickSightDescribeKnowledgeBasePermissionsRequest,
    ) -> QuickSightDescribeKnowledgeBasePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_knowledge_base_permissions, request, QuickSightDescribeKnowledgeBasePermissionsResponse)

    async def describe_knowledge_base_refresh_schedule(
        self,
        request: QuickSightDescribeKnowledgeBaseRefreshScheduleRequest,
    ) -> QuickSightDescribeKnowledgeBaseRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_knowledge_base_refresh_schedule, request, QuickSightDescribeKnowledgeBaseRefreshScheduleResponse)

    async def describe_limits_profile(
        self,
        request: QuickSightDescribeLimitsProfileRequest,
    ) -> QuickSightDescribeLimitsProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_limits_profile, request, QuickSightDescribeLimitsProfileResponse)

    async def describe_namespace(
        self,
        request: QuickSightDescribeNamespaceRequest,
    ) -> QuickSightDescribeNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.describe_namespace, request, QuickSightDescribeNamespaceResponse)

    async def describe_o_auth_client_application(
        self,
        request: QuickSightDescribeOAuthClientApplicationRequest,
    ) -> QuickSightDescribeOAuthClientApplicationResponse:
        client = self._require_client()
        return await self._execute(client.describe_o_auth_client_application, request, QuickSightDescribeOAuthClientApplicationResponse)

    async def describe_q_personalization_configuration(
        self,
        request: QuickSightDescribeQPersonalizationConfigurationRequest,
    ) -> QuickSightDescribeQPersonalizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_q_personalization_configuration, request, QuickSightDescribeQPersonalizationConfigurationResponse)

    async def describe_quick_sight_q_search_configuration(
        self,
        request: QuickSightDescribeQuickSightQSearchConfigurationRequest,
    ) -> QuickSightDescribeQuickSightQSearchConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_quick_sight_q_search_configuration, request, QuickSightDescribeQuickSightQSearchConfigurationResponse)

    async def describe_refresh_schedule(
        self,
        request: QuickSightDescribeRefreshScheduleRequest,
    ) -> QuickSightDescribeRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_refresh_schedule, request, QuickSightDescribeRefreshScheduleResponse)

    async def describe_resource_permissions(
        self,
        request: QuickSightDescribeResourcePermissionsRequest,
    ) -> QuickSightDescribeResourcePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_permissions, request, QuickSightDescribeResourcePermissionsResponse)

    async def describe_role_custom_permission(
        self,
        request: QuickSightDescribeRoleCustomPermissionRequest,
    ) -> QuickSightDescribeRoleCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.describe_role_custom_permission, request, QuickSightDescribeRoleCustomPermissionResponse)

    async def describe_self_upgrade_configuration(
        self,
        request: QuickSightDescribeSelfUpgradeConfigurationRequest,
    ) -> QuickSightDescribeSelfUpgradeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_self_upgrade_configuration, request, QuickSightDescribeSelfUpgradeConfigurationResponse)

    async def describe_space(
        self,
        request: QuickSightDescribeSpaceRequest,
    ) -> QuickSightDescribeSpaceResponse:
        client = self._require_client()
        return await self._execute(client.describe_space, request, QuickSightDescribeSpaceResponse)

    async def describe_space_permissions(
        self,
        request: QuickSightDescribeSpacePermissionsRequest,
    ) -> QuickSightDescribeSpacePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_space_permissions, request, QuickSightDescribeSpacePermissionsResponse)

    async def describe_template(
        self,
        request: QuickSightDescribeTemplateRequest,
    ) -> QuickSightDescribeTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_template, request, QuickSightDescribeTemplateResponse)

    async def describe_template_alias(
        self,
        request: QuickSightDescribeTemplateAliasRequest,
    ) -> QuickSightDescribeTemplateAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_template_alias, request, QuickSightDescribeTemplateAliasResponse)

    async def describe_template_definition(
        self,
        request: QuickSightDescribeTemplateDefinitionRequest,
    ) -> QuickSightDescribeTemplateDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_template_definition, request, QuickSightDescribeTemplateDefinitionResponse)

    async def describe_template_permissions(
        self,
        request: QuickSightDescribeTemplatePermissionsRequest,
    ) -> QuickSightDescribeTemplatePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_template_permissions, request, QuickSightDescribeTemplatePermissionsResponse)

    async def describe_theme(
        self,
        request: QuickSightDescribeThemeRequest,
    ) -> QuickSightDescribeThemeResponse:
        client = self._require_client()
        return await self._execute(client.describe_theme, request, QuickSightDescribeThemeResponse)

    async def describe_theme_alias(
        self,
        request: QuickSightDescribeThemeAliasRequest,
    ) -> QuickSightDescribeThemeAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_theme_alias, request, QuickSightDescribeThemeAliasResponse)

    async def describe_theme_permissions(
        self,
        request: QuickSightDescribeThemePermissionsRequest,
    ) -> QuickSightDescribeThemePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_theme_permissions, request, QuickSightDescribeThemePermissionsResponse)

    async def describe_topic(
        self,
        request: QuickSightDescribeTopicRequest,
    ) -> QuickSightDescribeTopicResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic, request, QuickSightDescribeTopicResponse)

    async def describe_topic_permissions(
        self,
        request: QuickSightDescribeTopicPermissionsRequest,
    ) -> QuickSightDescribeTopicPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic_permissions, request, QuickSightDescribeTopicPermissionsResponse)

    async def describe_topic_permissions_v2(
        self,
        request: QuickSightDescribeTopicPermissionsV2Request,
    ) -> QuickSightDescribeTopicPermissionsV2Response:
        client = self._require_client()
        return await self._execute(client.describe_topic_permissions_v2, request, QuickSightDescribeTopicPermissionsV2Response)

    async def describe_topic_refresh(
        self,
        request: QuickSightDescribeTopicRefreshRequest,
    ) -> QuickSightDescribeTopicRefreshResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic_refresh, request, QuickSightDescribeTopicRefreshResponse)

    async def describe_topic_refresh_schedule(
        self,
        request: QuickSightDescribeTopicRefreshScheduleRequest,
    ) -> QuickSightDescribeTopicRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic_refresh_schedule, request, QuickSightDescribeTopicRefreshScheduleResponse)

    async def describe_topic_v2(
        self,
        request: QuickSightDescribeTopicV2Request,
    ) -> QuickSightDescribeTopicV2Response:
        client = self._require_client()
        return await self._execute(client.describe_topic_v2, request, QuickSightDescribeTopicV2Response)

    async def describe_user(
        self,
        request: QuickSightDescribeUserRequest,
    ) -> QuickSightDescribeUserResponse:
        client = self._require_client()
        return await self._execute(client.describe_user, request, QuickSightDescribeUserResponse)

    async def describe_vpc_connection(
        self,
        request: QuickSightDescribeVPCConnectionRequest,
    ) -> QuickSightDescribeVPCConnectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_connection, request, QuickSightDescribeVPCConnectionResponse)

    async def generate_embed_url_for_anonymous_user(
        self,
        request: QuickSightGenerateEmbedUrlForAnonymousUserRequest,
    ) -> QuickSightGenerateEmbedUrlForAnonymousUserResponse:
        client = self._require_client()
        return await self._execute(client.generate_embed_url_for_anonymous_user, request, QuickSightGenerateEmbedUrlForAnonymousUserResponse)

    async def generate_embed_url_for_registered_user(
        self,
        request: QuickSightGenerateEmbedUrlForRegisteredUserRequest,
    ) -> QuickSightGenerateEmbedUrlForRegisteredUserResponse:
        client = self._require_client()
        return await self._execute(client.generate_embed_url_for_registered_user, request, QuickSightGenerateEmbedUrlForRegisteredUserResponse)

    async def generate_embed_url_for_registered_user_with_identity(
        self,
        request: QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityRequest,
    ) -> QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityResponse:
        client = self._require_client()
        return await self._execute(client.generate_embed_url_for_registered_user_with_identity, request, QuickSightGenerateEmbedUrlForRegisteredUserWithIdentityResponse)

    async def get_dashboard_embed_url(
        self,
        request: QuickSightGetDashboardEmbedUrlRequest,
    ) -> QuickSightGetDashboardEmbedUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_dashboard_embed_url, request, QuickSightGetDashboardEmbedUrlResponse)

    async def get_flow_metadata(
        self,
        request: QuickSightGetFlowMetadataRequest,
    ) -> QuickSightGetFlowMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_flow_metadata, request, QuickSightGetFlowMetadataResponse)

    async def get_flow_permissions(
        self,
        request: QuickSightGetFlowPermissionsRequest,
    ) -> QuickSightGetFlowPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.get_flow_permissions, request, QuickSightGetFlowPermissionsResponse)

    async def get_identity_context(
        self,
        request: QuickSightGetIdentityContextRequest,
    ) -> QuickSightGetIdentityContextResponse:
        client = self._require_client()
        return await self._execute(client.get_identity_context, request, QuickSightGetIdentityContextResponse)

    async def get_policy_assignment(
        self,
        request: QuickSightGetPolicyAssignmentRequest,
    ) -> QuickSightGetPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.get_policy_assignment, request, QuickSightGetPolicyAssignmentResponse)

    async def get_session_embed_url(
        self,
        request: QuickSightGetSessionEmbedUrlRequest,
    ) -> QuickSightGetSessionEmbedUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_session_embed_url, request, QuickSightGetSessionEmbedUrlResponse)

    async def list_access_control_applications(
        self,
        request: QuickSightListAccessControlApplicationsRequest,
    ) -> QuickSightListAccessControlApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_access_control_applications, request, QuickSightListAccessControlApplicationsResponse)

    async def list_access_control_applications_paginated(
        self,
        request: QuickSightListAccessControlApplicationsRequest,
    ) -> list[QuickSightListAccessControlApplicationsResponse]:
        return await self._paginate('list_access_control_applications', request, QuickSightListAccessControlApplicationsResponse)

    async def list_action_connectors(
        self,
        request: QuickSightListActionConnectorsRequest,
    ) -> QuickSightListActionConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_action_connectors, request, QuickSightListActionConnectorsResponse)

    async def list_action_connectors_paginated(
        self,
        request: QuickSightListActionConnectorsRequest,
    ) -> list[QuickSightListActionConnectorsResponse]:
        return await self._paginate('list_action_connectors', request, QuickSightListActionConnectorsResponse)

    async def list_agents(
        self,
        request: QuickSightListAgentsRequest,
    ) -> QuickSightListAgentsResponse:
        client = self._require_client()
        return await self._execute(client.list_agents, request, QuickSightListAgentsResponse)

    async def list_analyses(
        self,
        request: QuickSightListAnalysesRequest,
    ) -> QuickSightListAnalysesResponse:
        client = self._require_client()
        return await self._execute(client.list_analyses, request, QuickSightListAnalysesResponse)

    async def list_analyses_paginated(
        self,
        request: QuickSightListAnalysesRequest,
    ) -> list[QuickSightListAnalysesResponse]:
        return await self._paginate('list_analyses', request, QuickSightListAnalysesResponse)

    async def list_approval_policies(
        self,
        request: QuickSightListApprovalPoliciesRequest | None = None,
    ) -> QuickSightListApprovalPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_approval_policies, request, QuickSightListApprovalPoliciesResponse)

    async def list_approval_policies_paginated(
        self,
        request: QuickSightListApprovalPoliciesRequest | None = None,
    ) -> list[QuickSightListApprovalPoliciesResponse]:
        return await self._paginate('list_approval_policies', request, QuickSightListApprovalPoliciesResponse)

    async def list_apps(
        self,
        request: QuickSightListAppsRequest,
    ) -> QuickSightListAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_apps, request, QuickSightListAppsResponse)

    async def list_apps_paginated(
        self,
        request: QuickSightListAppsRequest,
    ) -> list[QuickSightListAppsResponse]:
        return await self._paginate('list_apps', request, QuickSightListAppsResponse)

    async def list_asset_bundle_export_jobs(
        self,
        request: QuickSightListAssetBundleExportJobsRequest,
    ) -> QuickSightListAssetBundleExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_asset_bundle_export_jobs, request, QuickSightListAssetBundleExportJobsResponse)

    async def list_asset_bundle_export_jobs_paginated(
        self,
        request: QuickSightListAssetBundleExportJobsRequest,
    ) -> list[QuickSightListAssetBundleExportJobsResponse]:
        return await self._paginate('list_asset_bundle_export_jobs', request, QuickSightListAssetBundleExportJobsResponse)

    async def list_asset_bundle_import_jobs(
        self,
        request: QuickSightListAssetBundleImportJobsRequest,
    ) -> QuickSightListAssetBundleImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_asset_bundle_import_jobs, request, QuickSightListAssetBundleImportJobsResponse)

    async def list_asset_bundle_import_jobs_paginated(
        self,
        request: QuickSightListAssetBundleImportJobsRequest,
    ) -> list[QuickSightListAssetBundleImportJobsResponse]:
        return await self._paginate('list_asset_bundle_import_jobs', request, QuickSightListAssetBundleImportJobsResponse)

    async def list_brands(
        self,
        request: QuickSightListBrandsRequest,
    ) -> QuickSightListBrandsResponse:
        client = self._require_client()
        return await self._execute(client.list_brands, request, QuickSightListBrandsResponse)

    async def list_brands_paginated(
        self,
        request: QuickSightListBrandsRequest,
    ) -> list[QuickSightListBrandsResponse]:
        return await self._paginate('list_brands', request, QuickSightListBrandsResponse)

    async def list_custom_permissions(
        self,
        request: QuickSightListCustomPermissionsRequest,
    ) -> QuickSightListCustomPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_permissions, request, QuickSightListCustomPermissionsResponse)

    async def list_custom_permissions_paginated(
        self,
        request: QuickSightListCustomPermissionsRequest,
    ) -> list[QuickSightListCustomPermissionsResponse]:
        return await self._paginate('list_custom_permissions', request, QuickSightListCustomPermissionsResponse)

    async def list_dashboard_versions(
        self,
        request: QuickSightListDashboardVersionsRequest,
    ) -> QuickSightListDashboardVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_dashboard_versions, request, QuickSightListDashboardVersionsResponse)

    async def list_dashboard_versions_paginated(
        self,
        request: QuickSightListDashboardVersionsRequest,
    ) -> list[QuickSightListDashboardVersionsResponse]:
        return await self._paginate('list_dashboard_versions', request, QuickSightListDashboardVersionsResponse)

    async def list_dashboards(
        self,
        request: QuickSightListDashboardsRequest,
    ) -> QuickSightListDashboardsResponse:
        client = self._require_client()
        return await self._execute(client.list_dashboards, request, QuickSightListDashboardsResponse)

    async def list_dashboards_paginated(
        self,
        request: QuickSightListDashboardsRequest,
    ) -> list[QuickSightListDashboardsResponse]:
        return await self._paginate('list_dashboards', request, QuickSightListDashboardsResponse)

    async def list_data_sets(
        self,
        request: QuickSightListDataSetsRequest,
    ) -> QuickSightListDataSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sets, request, QuickSightListDataSetsResponse)

    async def list_data_sets_paginated(
        self,
        request: QuickSightListDataSetsRequest,
    ) -> list[QuickSightListDataSetsResponse]:
        return await self._paginate('list_data_sets', request, QuickSightListDataSetsResponse)

    async def list_data_sources(
        self,
        request: QuickSightListDataSourcesRequest,
    ) -> QuickSightListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, QuickSightListDataSourcesResponse)

    async def list_data_sources_paginated(
        self,
        request: QuickSightListDataSourcesRequest,
    ) -> list[QuickSightListDataSourcesResponse]:
        return await self._paginate('list_data_sources', request, QuickSightListDataSourcesResponse)

    async def list_dlp_settings(
        self,
        request: QuickSightListDlpSettingsRequest,
    ) -> QuickSightListDlpSettingsResponse:
        client = self._require_client()
        return await self._execute(client.list_dlp_settings, request, QuickSightListDlpSettingsResponse)

    async def list_dlp_settings_paginated(
        self,
        request: QuickSightListDlpSettingsRequest,
    ) -> list[QuickSightListDlpSettingsResponse]:
        return await self._paginate('list_dlp_settings', request, QuickSightListDlpSettingsResponse)

    async def list_flows(
        self,
        request: QuickSightListFlowsRequest,
    ) -> QuickSightListFlowsResponse:
        client = self._require_client()
        return await self._execute(client.list_flows, request, QuickSightListFlowsResponse)

    async def list_flows_paginated(
        self,
        request: QuickSightListFlowsRequest,
    ) -> list[QuickSightListFlowsResponse]:
        return await self._paginate('list_flows', request, QuickSightListFlowsResponse)

    async def list_folder_members(
        self,
        request: QuickSightListFolderMembersRequest,
    ) -> QuickSightListFolderMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_folder_members, request, QuickSightListFolderMembersResponse)

    async def list_folder_members_paginated(
        self,
        request: QuickSightListFolderMembersRequest,
    ) -> list[QuickSightListFolderMembersResponse]:
        return await self._paginate('list_folder_members', request, QuickSightListFolderMembersResponse)

    async def list_folders(
        self,
        request: QuickSightListFoldersRequest,
    ) -> QuickSightListFoldersResponse:
        client = self._require_client()
        return await self._execute(client.list_folders, request, QuickSightListFoldersResponse)

    async def list_folders_paginated(
        self,
        request: QuickSightListFoldersRequest,
    ) -> list[QuickSightListFoldersResponse]:
        return await self._paginate('list_folders', request, QuickSightListFoldersResponse)

    async def list_folders_for_resource(
        self,
        request: QuickSightListFoldersForResourceRequest,
    ) -> QuickSightListFoldersForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_folders_for_resource, request, QuickSightListFoldersForResourceResponse)

    async def list_folders_for_resource_paginated(
        self,
        request: QuickSightListFoldersForResourceRequest,
    ) -> list[QuickSightListFoldersForResourceResponse]:
        return await self._paginate('list_folders_for_resource', request, QuickSightListFoldersForResourceResponse)

    async def list_group_memberships(
        self,
        request: QuickSightListGroupMembershipsRequest,
    ) -> QuickSightListGroupMembershipsResponse:
        client = self._require_client()
        return await self._execute(client.list_group_memberships, request, QuickSightListGroupMembershipsResponse)

    async def list_group_memberships_paginated(
        self,
        request: QuickSightListGroupMembershipsRequest,
    ) -> list[QuickSightListGroupMembershipsResponse]:
        return await self._paginate('list_group_memberships', request, QuickSightListGroupMembershipsResponse)

    async def list_groups(
        self,
        request: QuickSightListGroupsRequest,
    ) -> QuickSightListGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_groups, request, QuickSightListGroupsResponse)

    async def list_groups_paginated(
        self,
        request: QuickSightListGroupsRequest,
    ) -> list[QuickSightListGroupsResponse]:
        return await self._paginate('list_groups', request, QuickSightListGroupsResponse)

    async def list_iam_policy_assignments(
        self,
        request: QuickSightListIAMPolicyAssignmentsRequest,
    ) -> QuickSightListIAMPolicyAssignmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_iam_policy_assignments, request, QuickSightListIAMPolicyAssignmentsResponse)

    async def list_iam_policy_assignments_paginated(
        self,
        request: QuickSightListIAMPolicyAssignmentsRequest,
    ) -> list[QuickSightListIAMPolicyAssignmentsResponse]:
        return await self._paginate('list_iam_policy_assignments', request, QuickSightListIAMPolicyAssignmentsResponse)

    async def list_iam_policy_assignments_for_user(
        self,
        request: QuickSightListIAMPolicyAssignmentsForUserRequest,
    ) -> QuickSightListIAMPolicyAssignmentsForUserResponse:
        client = self._require_client()
        return await self._execute(client.list_iam_policy_assignments_for_user, request, QuickSightListIAMPolicyAssignmentsForUserResponse)

    async def list_iam_policy_assignments_for_user_paginated(
        self,
        request: QuickSightListIAMPolicyAssignmentsForUserRequest,
    ) -> list[QuickSightListIAMPolicyAssignmentsForUserResponse]:
        return await self._paginate('list_iam_policy_assignments_for_user', request, QuickSightListIAMPolicyAssignmentsForUserResponse)

    async def list_identity_propagation_configs(
        self,
        request: QuickSightListIdentityPropagationConfigsRequest,
    ) -> QuickSightListIdentityPropagationConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_propagation_configs, request, QuickSightListIdentityPropagationConfigsResponse)

    async def list_inbound_connector_application_associations(
        self,
        request: QuickSightListInboundConnectorApplicationAssociationsRequest,
    ) -> QuickSightListInboundConnectorApplicationAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_inbound_connector_application_associations, request, QuickSightListInboundConnectorApplicationAssociationsResponse)

    async def list_inbound_connector_application_associations_paginated(
        self,
        request: QuickSightListInboundConnectorApplicationAssociationsRequest,
    ) -> list[QuickSightListInboundConnectorApplicationAssociationsResponse]:
        return await self._paginate('list_inbound_connector_application_associations', request, QuickSightListInboundConnectorApplicationAssociationsResponse)

    async def list_inbound_connectors(
        self,
        request: QuickSightListInboundConnectorsRequest,
    ) -> QuickSightListInboundConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_inbound_connectors, request, QuickSightListInboundConnectorsResponse)

    async def list_inbound_connectors_paginated(
        self,
        request: QuickSightListInboundConnectorsRequest,
    ) -> list[QuickSightListInboundConnectorsResponse]:
        return await self._paginate('list_inbound_connectors', request, QuickSightListInboundConnectorsResponse)

    async def list_ingestions(
        self,
        request: QuickSightListIngestionsRequest,
    ) -> QuickSightListIngestionsResponse:
        client = self._require_client()
        return await self._execute(client.list_ingestions, request, QuickSightListIngestionsResponse)

    async def list_ingestions_paginated(
        self,
        request: QuickSightListIngestionsRequest,
    ) -> list[QuickSightListIngestionsResponse]:
        return await self._paginate('list_ingestions', request, QuickSightListIngestionsResponse)

    async def list_knowledge_base_refresh_schedules(
        self,
        request: QuickSightListKnowledgeBaseRefreshSchedulesRequest,
    ) -> QuickSightListKnowledgeBaseRefreshSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.list_knowledge_base_refresh_schedules, request, QuickSightListKnowledgeBaseRefreshSchedulesResponse)

    async def list_knowledge_base_refresh_schedules_paginated(
        self,
        request: QuickSightListKnowledgeBaseRefreshSchedulesRequest,
    ) -> list[QuickSightListKnowledgeBaseRefreshSchedulesResponse]:
        return await self._paginate('list_knowledge_base_refresh_schedules', request, QuickSightListKnowledgeBaseRefreshSchedulesResponse)

    async def list_knowledge_bases(
        self,
        request: QuickSightListKnowledgeBasesRequest,
    ) -> QuickSightListKnowledgeBasesResponse:
        client = self._require_client()
        return await self._execute(client.list_knowledge_bases, request, QuickSightListKnowledgeBasesResponse)

    async def list_knowledge_bases_paginated(
        self,
        request: QuickSightListKnowledgeBasesRequest,
    ) -> list[QuickSightListKnowledgeBasesResponse]:
        return await self._paginate('list_knowledge_bases', request, QuickSightListKnowledgeBasesResponse)

    async def list_limits_profiles(
        self,
        request: QuickSightListLimitsProfilesRequest,
    ) -> QuickSightListLimitsProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_limits_profiles, request, QuickSightListLimitsProfilesResponse)

    async def list_limits_profiles_paginated(
        self,
        request: QuickSightListLimitsProfilesRequest,
    ) -> list[QuickSightListLimitsProfilesResponse]:
        return await self._paginate('list_limits_profiles', request, QuickSightListLimitsProfilesResponse)

    async def list_namespaces(
        self,
        request: QuickSightListNamespacesRequest,
    ) -> QuickSightListNamespacesResponse:
        client = self._require_client()
        return await self._execute(client.list_namespaces, request, QuickSightListNamespacesResponse)

    async def list_namespaces_paginated(
        self,
        request: QuickSightListNamespacesRequest,
    ) -> list[QuickSightListNamespacesResponse]:
        return await self._paginate('list_namespaces', request, QuickSightListNamespacesResponse)

    async def list_o_auth_client_applications(
        self,
        request: QuickSightListOAuthClientApplicationsRequest,
    ) -> QuickSightListOAuthClientApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_o_auth_client_applications, request, QuickSightListOAuthClientApplicationsResponse)

    async def list_o_auth_client_applications_paginated(
        self,
        request: QuickSightListOAuthClientApplicationsRequest,
    ) -> list[QuickSightListOAuthClientApplicationsResponse]:
        return await self._paginate('list_o_auth_client_applications', request, QuickSightListOAuthClientApplicationsResponse)

    async def list_principals_for_policy(
        self,
        request: QuickSightListPrincipalsForPolicyRequest,
    ) -> QuickSightListPrincipalsForPolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_principals_for_policy, request, QuickSightListPrincipalsForPolicyResponse)

    async def list_principals_for_policy_paginated(
        self,
        request: QuickSightListPrincipalsForPolicyRequest,
    ) -> list[QuickSightListPrincipalsForPolicyResponse]:
        return await self._paginate('list_principals_for_policy', request, QuickSightListPrincipalsForPolicyResponse)

    async def list_refresh_schedules(
        self,
        request: QuickSightListRefreshSchedulesRequest,
    ) -> QuickSightListRefreshSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.list_refresh_schedules, request, QuickSightListRefreshSchedulesResponse)

    async def list_role_memberships(
        self,
        request: QuickSightListRoleMembershipsRequest,
    ) -> QuickSightListRoleMembershipsResponse:
        client = self._require_client()
        return await self._execute(client.list_role_memberships, request, QuickSightListRoleMembershipsResponse)

    async def list_role_memberships_paginated(
        self,
        request: QuickSightListRoleMembershipsRequest,
    ) -> list[QuickSightListRoleMembershipsResponse]:
        return await self._paginate('list_role_memberships', request, QuickSightListRoleMembershipsResponse)

    async def list_self_upgrades(
        self,
        request: QuickSightListSelfUpgradesRequest,
    ) -> QuickSightListSelfUpgradesResponse:
        client = self._require_client()
        return await self._execute(client.list_self_upgrades, request, QuickSightListSelfUpgradesResponse)

    async def list_space_resources(
        self,
        request: QuickSightListSpaceResourcesRequest,
    ) -> QuickSightListSpaceResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_space_resources, request, QuickSightListSpaceResourcesResponse)

    async def list_spaces(
        self,
        request: QuickSightListSpacesRequest,
    ) -> QuickSightListSpacesResponse:
        client = self._require_client()
        return await self._execute(client.list_spaces, request, QuickSightListSpacesResponse)

    async def list_tags_for_resource(
        self,
        request: QuickSightListTagsForResourceRequest,
    ) -> QuickSightListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, QuickSightListTagsForResourceResponse)

    async def list_template_aliases(
        self,
        request: QuickSightListTemplateAliasesRequest,
    ) -> QuickSightListTemplateAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_template_aliases, request, QuickSightListTemplateAliasesResponse)

    async def list_template_aliases_paginated(
        self,
        request: QuickSightListTemplateAliasesRequest,
    ) -> list[QuickSightListTemplateAliasesResponse]:
        return await self._paginate('list_template_aliases', request, QuickSightListTemplateAliasesResponse)

    async def list_template_versions(
        self,
        request: QuickSightListTemplateVersionsRequest,
    ) -> QuickSightListTemplateVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_template_versions, request, QuickSightListTemplateVersionsResponse)

    async def list_template_versions_paginated(
        self,
        request: QuickSightListTemplateVersionsRequest,
    ) -> list[QuickSightListTemplateVersionsResponse]:
        return await self._paginate('list_template_versions', request, QuickSightListTemplateVersionsResponse)

    async def list_templates(
        self,
        request: QuickSightListTemplatesRequest,
    ) -> QuickSightListTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_templates, request, QuickSightListTemplatesResponse)

    async def list_templates_paginated(
        self,
        request: QuickSightListTemplatesRequest,
    ) -> list[QuickSightListTemplatesResponse]:
        return await self._paginate('list_templates', request, QuickSightListTemplatesResponse)

    async def list_theme_aliases(
        self,
        request: QuickSightListThemeAliasesRequest,
    ) -> QuickSightListThemeAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_theme_aliases, request, QuickSightListThemeAliasesResponse)

    async def list_theme_versions(
        self,
        request: QuickSightListThemeVersionsRequest,
    ) -> QuickSightListThemeVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_theme_versions, request, QuickSightListThemeVersionsResponse)

    async def list_theme_versions_paginated(
        self,
        request: QuickSightListThemeVersionsRequest,
    ) -> list[QuickSightListThemeVersionsResponse]:
        return await self._paginate('list_theme_versions', request, QuickSightListThemeVersionsResponse)

    async def list_themes(
        self,
        request: QuickSightListThemesRequest,
    ) -> QuickSightListThemesResponse:
        client = self._require_client()
        return await self._execute(client.list_themes, request, QuickSightListThemesResponse)

    async def list_themes_paginated(
        self,
        request: QuickSightListThemesRequest,
    ) -> list[QuickSightListThemesResponse]:
        return await self._paginate('list_themes', request, QuickSightListThemesResponse)

    async def list_topic_refresh_schedules(
        self,
        request: QuickSightListTopicRefreshSchedulesRequest,
    ) -> QuickSightListTopicRefreshSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.list_topic_refresh_schedules, request, QuickSightListTopicRefreshSchedulesResponse)

    async def list_topic_reviewed_answers(
        self,
        request: QuickSightListTopicReviewedAnswersRequest,
    ) -> QuickSightListTopicReviewedAnswersResponse:
        client = self._require_client()
        return await self._execute(client.list_topic_reviewed_answers, request, QuickSightListTopicReviewedAnswersResponse)

    async def list_topics(
        self,
        request: QuickSightListTopicsRequest,
    ) -> QuickSightListTopicsResponse:
        client = self._require_client()
        return await self._execute(client.list_topics, request, QuickSightListTopicsResponse)

    async def list_topics_v2(
        self,
        request: QuickSightListTopicsV2Request,
    ) -> QuickSightListTopicsV2Response:
        client = self._require_client()
        return await self._execute(client.list_topics_v2, request, QuickSightListTopicsV2Response)

    async def list_topics_v2_paginated(
        self,
        request: QuickSightListTopicsV2Request,
    ) -> list[QuickSightListTopicsV2Response]:
        return await self._paginate('list_topics_v2', request, QuickSightListTopicsV2Response)

    async def list_user_groups(
        self,
        request: QuickSightListUserGroupsRequest,
    ) -> QuickSightListUserGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_groups, request, QuickSightListUserGroupsResponse)

    async def list_user_groups_paginated(
        self,
        request: QuickSightListUserGroupsRequest,
    ) -> list[QuickSightListUserGroupsResponse]:
        return await self._paginate('list_user_groups', request, QuickSightListUserGroupsResponse)

    async def list_users(
        self,
        request: QuickSightListUsersRequest,
    ) -> QuickSightListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, QuickSightListUsersResponse)

    async def list_users_paginated(
        self,
        request: QuickSightListUsersRequest,
    ) -> list[QuickSightListUsersResponse]:
        return await self._paginate('list_users', request, QuickSightListUsersResponse)

    async def list_users_index_capacity(
        self,
        request: QuickSightListUsersIndexCapacityRequest,
    ) -> QuickSightListUsersIndexCapacityResponse:
        client = self._require_client()
        return await self._execute(client.list_users_index_capacity, request, QuickSightListUsersIndexCapacityResponse)

    async def list_vpc_connections(
        self,
        request: QuickSightListVPCConnectionsRequest,
    ) -> QuickSightListVPCConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_connections, request, QuickSightListVPCConnectionsResponse)

    async def predict_qa_results(
        self,
        request: QuickSightPredictQAResultsRequest,
    ) -> QuickSightPredictQAResultsResponse:
        client = self._require_client()
        return await self._execute(client.predict_qa_results, request, QuickSightPredictQAResultsResponse)

    async def put_data_set_refresh_properties(
        self,
        request: QuickSightPutDataSetRefreshPropertiesRequest,
    ) -> QuickSightPutDataSetRefreshPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.put_data_set_refresh_properties, request, QuickSightPutDataSetRefreshPropertiesResponse)

    async def put_policy_assignment(
        self,
        request: QuickSightPutPolicyAssignmentRequest,
    ) -> QuickSightPutPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.put_policy_assignment, request, QuickSightPutPolicyAssignmentResponse)

    async def register_user(
        self,
        request: QuickSightRegisterUserRequest,
    ) -> QuickSightRegisterUserResponse:
        client = self._require_client()
        return await self._execute(client.register_user, request, QuickSightRegisterUserResponse)

    async def restore_analysis(
        self,
        request: QuickSightRestoreAnalysisRequest,
    ) -> QuickSightRestoreAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.restore_analysis, request, QuickSightRestoreAnalysisResponse)

    async def search_action_connectors(
        self,
        request: QuickSightSearchActionConnectorsRequest,
    ) -> QuickSightSearchActionConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.search_action_connectors, request, QuickSightSearchActionConnectorsResponse)

    async def search_action_connectors_paginated(
        self,
        request: QuickSightSearchActionConnectorsRequest,
    ) -> list[QuickSightSearchActionConnectorsResponse]:
        return await self._paginate('search_action_connectors', request, QuickSightSearchActionConnectorsResponse)

    async def search_agents(
        self,
        request: QuickSightSearchAgentsRequest,
    ) -> QuickSightSearchAgentsResponse:
        client = self._require_client()
        return await self._execute(client.search_agents, request, QuickSightSearchAgentsResponse)

    async def search_analyses(
        self,
        request: QuickSightSearchAnalysesRequest,
    ) -> QuickSightSearchAnalysesResponse:
        client = self._require_client()
        return await self._execute(client.search_analyses, request, QuickSightSearchAnalysesResponse)

    async def search_analyses_paginated(
        self,
        request: QuickSightSearchAnalysesRequest,
    ) -> list[QuickSightSearchAnalysesResponse]:
        return await self._paginate('search_analyses', request, QuickSightSearchAnalysesResponse)

    async def search_apps(
        self,
        request: QuickSightSearchAppsRequest,
    ) -> QuickSightSearchAppsResponse:
        client = self._require_client()
        return await self._execute(client.search_apps, request, QuickSightSearchAppsResponse)

    async def search_apps_paginated(
        self,
        request: QuickSightSearchAppsRequest,
    ) -> list[QuickSightSearchAppsResponse]:
        return await self._paginate('search_apps', request, QuickSightSearchAppsResponse)

    async def search_dashboards(
        self,
        request: QuickSightSearchDashboardsRequest,
    ) -> QuickSightSearchDashboardsResponse:
        client = self._require_client()
        return await self._execute(client.search_dashboards, request, QuickSightSearchDashboardsResponse)

    async def search_dashboards_paginated(
        self,
        request: QuickSightSearchDashboardsRequest,
    ) -> list[QuickSightSearchDashboardsResponse]:
        return await self._paginate('search_dashboards', request, QuickSightSearchDashboardsResponse)

    async def search_data_sets(
        self,
        request: QuickSightSearchDataSetsRequest,
    ) -> QuickSightSearchDataSetsResponse:
        client = self._require_client()
        return await self._execute(client.search_data_sets, request, QuickSightSearchDataSetsResponse)

    async def search_data_sets_paginated(
        self,
        request: QuickSightSearchDataSetsRequest,
    ) -> list[QuickSightSearchDataSetsResponse]:
        return await self._paginate('search_data_sets', request, QuickSightSearchDataSetsResponse)

    async def search_data_sources(
        self,
        request: QuickSightSearchDataSourcesRequest,
    ) -> QuickSightSearchDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.search_data_sources, request, QuickSightSearchDataSourcesResponse)

    async def search_data_sources_paginated(
        self,
        request: QuickSightSearchDataSourcesRequest,
    ) -> list[QuickSightSearchDataSourcesResponse]:
        return await self._paginate('search_data_sources', request, QuickSightSearchDataSourcesResponse)

    async def search_flows(
        self,
        request: QuickSightSearchFlowsRequest,
    ) -> QuickSightSearchFlowsResponse:
        client = self._require_client()
        return await self._execute(client.search_flows, request, QuickSightSearchFlowsResponse)

    async def search_flows_paginated(
        self,
        request: QuickSightSearchFlowsRequest,
    ) -> list[QuickSightSearchFlowsResponse]:
        return await self._paginate('search_flows', request, QuickSightSearchFlowsResponse)

    async def search_folders(
        self,
        request: QuickSightSearchFoldersRequest,
    ) -> QuickSightSearchFoldersResponse:
        client = self._require_client()
        return await self._execute(client.search_folders, request, QuickSightSearchFoldersResponse)

    async def search_folders_paginated(
        self,
        request: QuickSightSearchFoldersRequest,
    ) -> list[QuickSightSearchFoldersResponse]:
        return await self._paginate('search_folders', request, QuickSightSearchFoldersResponse)

    async def search_groups(
        self,
        request: QuickSightSearchGroupsRequest,
    ) -> QuickSightSearchGroupsResponse:
        client = self._require_client()
        return await self._execute(client.search_groups, request, QuickSightSearchGroupsResponse)

    async def search_groups_paginated(
        self,
        request: QuickSightSearchGroupsRequest,
    ) -> list[QuickSightSearchGroupsResponse]:
        return await self._paginate('search_groups', request, QuickSightSearchGroupsResponse)

    async def search_knowledge_bases(
        self,
        request: QuickSightSearchKnowledgeBasesRequest,
    ) -> QuickSightSearchKnowledgeBasesResponse:
        client = self._require_client()
        return await self._execute(client.search_knowledge_bases, request, QuickSightSearchKnowledgeBasesResponse)

    async def search_knowledge_bases_paginated(
        self,
        request: QuickSightSearchKnowledgeBasesRequest,
    ) -> list[QuickSightSearchKnowledgeBasesResponse]:
        return await self._paginate('search_knowledge_bases', request, QuickSightSearchKnowledgeBasesResponse)

    async def search_spaces(
        self,
        request: QuickSightSearchSpacesRequest,
    ) -> QuickSightSearchSpacesResponse:
        client = self._require_client()
        return await self._execute(client.search_spaces, request, QuickSightSearchSpacesResponse)

    async def search_topics(
        self,
        request: QuickSightSearchTopicsRequest,
    ) -> QuickSightSearchTopicsResponse:
        client = self._require_client()
        return await self._execute(client.search_topics, request, QuickSightSearchTopicsResponse)

    async def search_topics_paginated(
        self,
        request: QuickSightSearchTopicsRequest,
    ) -> list[QuickSightSearchTopicsResponse]:
        return await self._paginate('search_topics', request, QuickSightSearchTopicsResponse)

    async def search_topics_v2(
        self,
        request: QuickSightSearchTopicsV2Request,
    ) -> QuickSightSearchTopicsV2Response:
        client = self._require_client()
        return await self._execute(client.search_topics_v2, request, QuickSightSearchTopicsV2Response)

    async def search_topics_v2_paginated(
        self,
        request: QuickSightSearchTopicsV2Request,
    ) -> list[QuickSightSearchTopicsV2Response]:
        return await self._paginate('search_topics_v2', request, QuickSightSearchTopicsV2Response)

    async def start_asset_bundle_export_job(
        self,
        request: QuickSightStartAssetBundleExportJobRequest,
    ) -> QuickSightStartAssetBundleExportJobResponse:
        client = self._require_client()
        return await self._execute(client.start_asset_bundle_export_job, request, QuickSightStartAssetBundleExportJobResponse)

    async def start_asset_bundle_import_job(
        self,
        request: QuickSightStartAssetBundleImportJobRequest,
    ) -> QuickSightStartAssetBundleImportJobResponse:
        client = self._require_client()
        return await self._execute(client.start_asset_bundle_import_job, request, QuickSightStartAssetBundleImportJobResponse)

    async def start_automation_job(
        self,
        request: QuickSightStartAutomationJobRequest,
    ) -> QuickSightStartAutomationJobResponse:
        client = self._require_client()
        return await self._execute(client.start_automation_job, request, QuickSightStartAutomationJobResponse)

    async def start_dashboard_snapshot_job(
        self,
        request: QuickSightStartDashboardSnapshotJobRequest,
    ) -> QuickSightStartDashboardSnapshotJobResponse:
        client = self._require_client()
        return await self._execute(client.start_dashboard_snapshot_job, request, QuickSightStartDashboardSnapshotJobResponse)

    async def start_dashboard_snapshot_job_schedule(
        self,
        request: QuickSightStartDashboardSnapshotJobScheduleRequest,
    ) -> QuickSightStartDashboardSnapshotJobScheduleResponse:
        client = self._require_client()
        return await self._execute(client.start_dashboard_snapshot_job_schedule, request, QuickSightStartDashboardSnapshotJobScheduleResponse)

    async def tag_resource(
        self,
        request: QuickSightTagResourceRequest,
    ) -> QuickSightTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, QuickSightTagResourceResponse)

    async def untag_resource(
        self,
        request: QuickSightUntagResourceRequest,
    ) -> QuickSightUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, QuickSightUntagResourceResponse)

    async def update_access_control_application(
        self,
        request: QuickSightUpdateAccessControlApplicationRequest,
    ) -> QuickSightUpdateAccessControlApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_access_control_application, request, QuickSightUpdateAccessControlApplicationResponse)

    async def update_access_control_application_secret(
        self,
        request: QuickSightUpdateAccessControlApplicationSecretRequest,
    ) -> QuickSightUpdateAccessControlApplicationSecretResponse:
        client = self._require_client()
        return await self._execute(client.update_access_control_application_secret, request, QuickSightUpdateAccessControlApplicationSecretResponse)

    async def update_account_custom_permission(
        self,
        request: QuickSightUpdateAccountCustomPermissionRequest,
    ) -> QuickSightUpdateAccountCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.update_account_custom_permission, request, QuickSightUpdateAccountCustomPermissionResponse)

    async def update_account_customization(
        self,
        request: QuickSightUpdateAccountCustomizationRequest,
    ) -> QuickSightUpdateAccountCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.update_account_customization, request, QuickSightUpdateAccountCustomizationResponse)

    async def update_account_settings(
        self,
        request: QuickSightUpdateAccountSettingsRequest,
    ) -> QuickSightUpdateAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_account_settings, request, QuickSightUpdateAccountSettingsResponse)

    async def update_action_connector(
        self,
        request: QuickSightUpdateActionConnectorRequest,
    ) -> QuickSightUpdateActionConnectorResponse:
        client = self._require_client()
        return await self._execute(client.update_action_connector, request, QuickSightUpdateActionConnectorResponse)

    async def update_action_connector_permissions(
        self,
        request: QuickSightUpdateActionConnectorPermissionsRequest,
    ) -> QuickSightUpdateActionConnectorPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_action_connector_permissions, request, QuickSightUpdateActionConnectorPermissionsResponse)

    async def update_agent(
        self,
        request: QuickSightUpdateAgentRequest,
    ) -> QuickSightUpdateAgentResponse:
        client = self._require_client()
        return await self._execute(client.update_agent, request, QuickSightUpdateAgentResponse)

    async def update_agent_permissions(
        self,
        request: QuickSightUpdateAgentPermissionsRequest,
    ) -> QuickSightUpdateAgentPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_agent_permissions, request, QuickSightUpdateAgentPermissionsResponse)

    async def update_analysis(
        self,
        request: QuickSightUpdateAnalysisRequest,
    ) -> QuickSightUpdateAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.update_analysis, request, QuickSightUpdateAnalysisResponse)

    async def update_analysis_permissions(
        self,
        request: QuickSightUpdateAnalysisPermissionsRequest,
    ) -> QuickSightUpdateAnalysisPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_analysis_permissions, request, QuickSightUpdateAnalysisPermissionsResponse)

    async def update_app_permissions(
        self,
        request: QuickSightUpdateAppPermissionsRequest,
    ) -> QuickSightUpdateAppPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_app_permissions, request, QuickSightUpdateAppPermissionsResponse)

    async def update_application_with_token_exchange_grant(
        self,
        request: QuickSightUpdateApplicationWithTokenExchangeGrantRequest,
    ) -> QuickSightUpdateApplicationWithTokenExchangeGrantResponse:
        client = self._require_client()
        return await self._execute(client.update_application_with_token_exchange_grant, request, QuickSightUpdateApplicationWithTokenExchangeGrantResponse)

    async def update_approval_policy(
        self,
        request: QuickSightUpdateApprovalPolicyRequest,
    ) -> QuickSightUpdateApprovalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_approval_policy, request, QuickSightUpdateApprovalPolicyResponse)

    async def update_brand(
        self,
        request: QuickSightUpdateBrandRequest,
    ) -> QuickSightUpdateBrandResponse:
        client = self._require_client()
        return await self._execute(client.update_brand, request, QuickSightUpdateBrandResponse)

    async def update_brand_assignment(
        self,
        request: QuickSightUpdateBrandAssignmentRequest,
    ) -> QuickSightUpdateBrandAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.update_brand_assignment, request, QuickSightUpdateBrandAssignmentResponse)

    async def update_brand_published_version(
        self,
        request: QuickSightUpdateBrandPublishedVersionRequest,
    ) -> QuickSightUpdateBrandPublishedVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_brand_published_version, request, QuickSightUpdateBrandPublishedVersionResponse)

    async def update_custom_permissions(
        self,
        request: QuickSightUpdateCustomPermissionsRequest,
    ) -> QuickSightUpdateCustomPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_permissions, request, QuickSightUpdateCustomPermissionsResponse)

    async def update_dashboard(
        self,
        request: QuickSightUpdateDashboardRequest,
    ) -> QuickSightUpdateDashboardResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboard, request, QuickSightUpdateDashboardResponse)

    async def update_dashboard_links(
        self,
        request: QuickSightUpdateDashboardLinksRequest,
    ) -> QuickSightUpdateDashboardLinksResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboard_links, request, QuickSightUpdateDashboardLinksResponse)

    async def update_dashboard_permissions(
        self,
        request: QuickSightUpdateDashboardPermissionsRequest,
    ) -> QuickSightUpdateDashboardPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboard_permissions, request, QuickSightUpdateDashboardPermissionsResponse)

    async def update_dashboard_published_version(
        self,
        request: QuickSightUpdateDashboardPublishedVersionRequest,
    ) -> QuickSightUpdateDashboardPublishedVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboard_published_version, request, QuickSightUpdateDashboardPublishedVersionResponse)

    async def update_dashboards_qa_configuration(
        self,
        request: QuickSightUpdateDashboardsQAConfigurationRequest,
    ) -> QuickSightUpdateDashboardsQAConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_dashboards_qa_configuration, request, QuickSightUpdateDashboardsQAConfigurationResponse)

    async def update_data_set(
        self,
        request: QuickSightUpdateDataSetRequest,
    ) -> QuickSightUpdateDataSetResponse:
        client = self._require_client()
        return await self._execute(client.update_data_set, request, QuickSightUpdateDataSetResponse)

    async def update_data_set_permissions(
        self,
        request: QuickSightUpdateDataSetPermissionsRequest,
    ) -> QuickSightUpdateDataSetPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_data_set_permissions, request, QuickSightUpdateDataSetPermissionsResponse)

    async def update_data_source(
        self,
        request: QuickSightUpdateDataSourceRequest,
    ) -> QuickSightUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, QuickSightUpdateDataSourceResponse)

    async def update_data_source_permissions(
        self,
        request: QuickSightUpdateDataSourcePermissionsRequest,
    ) -> QuickSightUpdateDataSourcePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source_permissions, request, QuickSightUpdateDataSourcePermissionsResponse)

    async def update_default_q_business_application(
        self,
        request: QuickSightUpdateDefaultQBusinessApplicationRequest,
    ) -> QuickSightUpdateDefaultQBusinessApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_default_q_business_application, request, QuickSightUpdateDefaultQBusinessApplicationResponse)

    async def update_dlp_setting(
        self,
        request: QuickSightUpdateDlpSettingRequest,
    ) -> QuickSightUpdateDlpSettingResponse:
        client = self._require_client()
        return await self._execute(client.update_dlp_setting, request, QuickSightUpdateDlpSettingResponse)

    async def update_flow(
        self,
        request: QuickSightUpdateFlowRequest,
    ) -> QuickSightUpdateFlowResponse:
        client = self._require_client()
        return await self._execute(client.update_flow, request, QuickSightUpdateFlowResponse)

    async def update_flow_permissions(
        self,
        request: QuickSightUpdateFlowPermissionsRequest,
    ) -> QuickSightUpdateFlowPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_flow_permissions, request, QuickSightUpdateFlowPermissionsResponse)

    async def update_folder(
        self,
        request: QuickSightUpdateFolderRequest,
    ) -> QuickSightUpdateFolderResponse:
        client = self._require_client()
        return await self._execute(client.update_folder, request, QuickSightUpdateFolderResponse)

    async def update_folder_permissions(
        self,
        request: QuickSightUpdateFolderPermissionsRequest,
    ) -> QuickSightUpdateFolderPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_folder_permissions, request, QuickSightUpdateFolderPermissionsResponse)

    async def update_group(
        self,
        request: QuickSightUpdateGroupRequest,
    ) -> QuickSightUpdateGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_group, request, QuickSightUpdateGroupResponse)

    async def update_iam_policy_assignment(
        self,
        request: QuickSightUpdateIAMPolicyAssignmentRequest,
    ) -> QuickSightUpdateIAMPolicyAssignmentResponse:
        client = self._require_client()
        return await self._execute(client.update_iam_policy_assignment, request, QuickSightUpdateIAMPolicyAssignmentResponse)

    async def update_identity_propagation_config(
        self,
        request: QuickSightUpdateIdentityPropagationConfigRequest,
    ) -> QuickSightUpdateIdentityPropagationConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_identity_propagation_config, request, QuickSightUpdateIdentityPropagationConfigResponse)

    async def update_inbound_connector(
        self,
        request: QuickSightUpdateInboundConnectorRequest,
    ) -> QuickSightUpdateInboundConnectorResponse:
        client = self._require_client()
        return await self._execute(client.update_inbound_connector, request, QuickSightUpdateInboundConnectorResponse)

    async def update_inbound_connector_application_associations(
        self,
        request: QuickSightUpdateInboundConnectorApplicationAssociationsRequest,
    ) -> QuickSightUpdateInboundConnectorApplicationAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.update_inbound_connector_application_associations, request, QuickSightUpdateInboundConnectorApplicationAssociationsResponse)

    async def update_ip_restriction(
        self,
        request: QuickSightUpdateIpRestrictionRequest,
    ) -> QuickSightUpdateIpRestrictionResponse:
        client = self._require_client()
        return await self._execute(client.update_ip_restriction, request, QuickSightUpdateIpRestrictionResponse)

    async def update_key_registration(
        self,
        request: QuickSightUpdateKeyRegistrationRequest,
    ) -> QuickSightUpdateKeyRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.update_key_registration, request, QuickSightUpdateKeyRegistrationResponse)

    async def update_knowledge_base(
        self,
        request: QuickSightUpdateKnowledgeBaseRequest,
    ) -> QuickSightUpdateKnowledgeBaseResponse:
        client = self._require_client()
        return await self._execute(client.update_knowledge_base, request, QuickSightUpdateKnowledgeBaseResponse)

    async def update_knowledge_base_permissions(
        self,
        request: QuickSightUpdateKnowledgeBasePermissionsRequest,
    ) -> QuickSightUpdateKnowledgeBasePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_knowledge_base_permissions, request, QuickSightUpdateKnowledgeBasePermissionsResponse)

    async def update_knowledge_base_refresh_schedule(
        self,
        request: QuickSightUpdateKnowledgeBaseRefreshScheduleRequest,
    ) -> QuickSightUpdateKnowledgeBaseRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_knowledge_base_refresh_schedule, request, QuickSightUpdateKnowledgeBaseRefreshScheduleResponse)

    async def update_limits_profile(
        self,
        request: QuickSightUpdateLimitsProfileRequest,
    ) -> QuickSightUpdateLimitsProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_limits_profile, request, QuickSightUpdateLimitsProfileResponse)

    async def update_o_auth_client_application(
        self,
        request: QuickSightUpdateOAuthClientApplicationRequest,
    ) -> QuickSightUpdateOAuthClientApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_o_auth_client_application, request, QuickSightUpdateOAuthClientApplicationResponse)

    async def update_public_sharing_settings(
        self,
        request: QuickSightUpdatePublicSharingSettingsRequest,
    ) -> QuickSightUpdatePublicSharingSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_public_sharing_settings, request, QuickSightUpdatePublicSharingSettingsResponse)

    async def update_q_personalization_configuration(
        self,
        request: QuickSightUpdateQPersonalizationConfigurationRequest,
    ) -> QuickSightUpdateQPersonalizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_q_personalization_configuration, request, QuickSightUpdateQPersonalizationConfigurationResponse)

    async def update_quick_sight_q_search_configuration(
        self,
        request: QuickSightUpdateQuickSightQSearchConfigurationRequest,
    ) -> QuickSightUpdateQuickSightQSearchConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_quick_sight_q_search_configuration, request, QuickSightUpdateQuickSightQSearchConfigurationResponse)

    async def update_refresh_schedule(
        self,
        request: QuickSightUpdateRefreshScheduleRequest,
    ) -> QuickSightUpdateRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_refresh_schedule, request, QuickSightUpdateRefreshScheduleResponse)

    async def update_resource_permissions(
        self,
        request: QuickSightUpdateResourcePermissionsRequest,
    ) -> QuickSightUpdateResourcePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_permissions, request, QuickSightUpdateResourcePermissionsResponse)

    async def update_role_custom_permission(
        self,
        request: QuickSightUpdateRoleCustomPermissionRequest,
    ) -> QuickSightUpdateRoleCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.update_role_custom_permission, request, QuickSightUpdateRoleCustomPermissionResponse)

    async def update_spice_capacity_configuration(
        self,
        request: QuickSightUpdateSPICECapacityConfigurationRequest,
    ) -> QuickSightUpdateSPICECapacityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_spice_capacity_configuration, request, QuickSightUpdateSPICECapacityConfigurationResponse)

    async def update_self_upgrade(
        self,
        request: QuickSightUpdateSelfUpgradeRequest,
    ) -> QuickSightUpdateSelfUpgradeResponse:
        client = self._require_client()
        return await self._execute(client.update_self_upgrade, request, QuickSightUpdateSelfUpgradeResponse)

    async def update_self_upgrade_configuration(
        self,
        request: QuickSightUpdateSelfUpgradeConfigurationRequest,
    ) -> QuickSightUpdateSelfUpgradeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_self_upgrade_configuration, request, QuickSightUpdateSelfUpgradeConfigurationResponse)

    async def update_space(
        self,
        request: QuickSightUpdateSpaceRequest,
    ) -> QuickSightUpdateSpaceResponse:
        client = self._require_client()
        return await self._execute(client.update_space, request, QuickSightUpdateSpaceResponse)

    async def update_space_permissions(
        self,
        request: QuickSightUpdateSpacePermissionsRequest,
    ) -> QuickSightUpdateSpacePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_space_permissions, request, QuickSightUpdateSpacePermissionsResponse)

    async def update_space_resources(
        self,
        request: QuickSightUpdateSpaceResourcesRequest,
    ) -> QuickSightUpdateSpaceResourcesResponse:
        client = self._require_client()
        return await self._execute(client.update_space_resources, request, QuickSightUpdateSpaceResourcesResponse)

    async def update_template(
        self,
        request: QuickSightUpdateTemplateRequest,
    ) -> QuickSightUpdateTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_template, request, QuickSightUpdateTemplateResponse)

    async def update_template_alias(
        self,
        request: QuickSightUpdateTemplateAliasRequest,
    ) -> QuickSightUpdateTemplateAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_template_alias, request, QuickSightUpdateTemplateAliasResponse)

    async def update_template_permissions(
        self,
        request: QuickSightUpdateTemplatePermissionsRequest,
    ) -> QuickSightUpdateTemplatePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_template_permissions, request, QuickSightUpdateTemplatePermissionsResponse)

    async def update_theme(
        self,
        request: QuickSightUpdateThemeRequest,
    ) -> QuickSightUpdateThemeResponse:
        client = self._require_client()
        return await self._execute(client.update_theme, request, QuickSightUpdateThemeResponse)

    async def update_theme_alias(
        self,
        request: QuickSightUpdateThemeAliasRequest,
    ) -> QuickSightUpdateThemeAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_theme_alias, request, QuickSightUpdateThemeAliasResponse)

    async def update_theme_permissions(
        self,
        request: QuickSightUpdateThemePermissionsRequest,
    ) -> QuickSightUpdateThemePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_theme_permissions, request, QuickSightUpdateThemePermissionsResponse)

    async def update_topic(
        self,
        request: QuickSightUpdateTopicRequest,
    ) -> QuickSightUpdateTopicResponse:
        client = self._require_client()
        return await self._execute(client.update_topic, request, QuickSightUpdateTopicResponse)

    async def update_topic_permissions(
        self,
        request: QuickSightUpdateTopicPermissionsRequest,
    ) -> QuickSightUpdateTopicPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_topic_permissions, request, QuickSightUpdateTopicPermissionsResponse)

    async def update_topic_permissions_v2(
        self,
        request: QuickSightUpdateTopicPermissionsV2Request,
    ) -> QuickSightUpdateTopicPermissionsV2Response:
        client = self._require_client()
        return await self._execute(client.update_topic_permissions_v2, request, QuickSightUpdateTopicPermissionsV2Response)

    async def update_topic_refresh_schedule(
        self,
        request: QuickSightUpdateTopicRefreshScheduleRequest,
    ) -> QuickSightUpdateTopicRefreshScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_topic_refresh_schedule, request, QuickSightUpdateTopicRefreshScheduleResponse)

    async def update_topic_v2(
        self,
        request: QuickSightUpdateTopicV2Request,
    ) -> QuickSightUpdateTopicV2Response:
        client = self._require_client()
        return await self._execute(client.update_topic_v2, request, QuickSightUpdateTopicV2Response)

    async def update_user(
        self,
        request: QuickSightUpdateUserRequest,
    ) -> QuickSightUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, QuickSightUpdateUserResponse)

    async def update_user_custom_permission(
        self,
        request: QuickSightUpdateUserCustomPermissionRequest,
    ) -> QuickSightUpdateUserCustomPermissionResponse:
        client = self._require_client()
        return await self._execute(client.update_user_custom_permission, request, QuickSightUpdateUserCustomPermissionResponse)

    async def update_vpc_connection(
        self,
        request: QuickSightUpdateVPCConnectionRequest,
    ) -> QuickSightUpdateVPCConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_connection, request, QuickSightUpdateVPCConnectionResponse)
