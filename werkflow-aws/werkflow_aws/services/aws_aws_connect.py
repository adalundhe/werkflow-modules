from werkflow_aws.models.aws_connect import (
    ConnectActivateEvaluationFormRequest,
    ConnectActivateEvaluationFormResponse,
    ConnectAssociateAnalyticsDataSetRequest,
    ConnectAssociateAnalyticsDataSetResponse,
    ConnectAssociateApprovedOriginRequest,
    ConnectAssociateApprovedOriginResponse,
    ConnectAssociateBotRequest,
    ConnectAssociateBotResponse,
    ConnectAssociateContactWithUserRequest,
    ConnectAssociateContactWithUserResponse,
    ConnectAssociateDefaultVocabularyRequest,
    ConnectAssociateDefaultVocabularyResponse,
    ConnectAssociateEmailAddressAliasRequest,
    ConnectAssociateEmailAddressAliasResponse,
    ConnectAssociateFlowRequest,
    ConnectAssociateFlowResponse,
    ConnectAssociateHoursOfOperationsRequest,
    ConnectAssociateHoursOfOperationsResponse,
    ConnectAssociateInstanceStorageConfigRequest,
    ConnectAssociateInstanceStorageConfigResponse,
    ConnectAssociateLambdaFunctionRequest,
    ConnectAssociateLambdaFunctionResponse,
    ConnectAssociateLexBotRequest,
    ConnectAssociateLexBotResponse,
    ConnectAssociatePhoneNumberContactFlowRequest,
    ConnectAssociatePhoneNumberContactFlowResponse,
    ConnectAssociateQueueEmailAddressesRequest,
    ConnectAssociateQueueEmailAddressesResponse,
    ConnectAssociateQueueQuickConnectsRequest,
    ConnectAssociateQueueQuickConnectsResponse,
    ConnectAssociateRoutingProfileQueuesRequest,
    ConnectAssociateRoutingProfileQueuesResponse,
    ConnectAssociateSecurityKeyRequest,
    ConnectAssociateSecurityKeyResponse,
    ConnectAssociateSecurityProfilesRequest,
    ConnectAssociateSecurityProfilesResponse,
    ConnectAssociateTrafficDistributionGroupUserRequest,
    ConnectAssociateTrafficDistributionGroupUserResponse,
    ConnectAssociateUserProficienciesRequest,
    ConnectAssociateUserProficienciesResponse,
    ConnectAssociateWorkspaceRequest,
    ConnectAssociateWorkspaceResponse,
    ConnectBatchAssociateAnalyticsDataSetRequest,
    ConnectBatchAssociateAnalyticsDataSetResponse,
    ConnectBatchCreateDataTableValueRequest,
    ConnectBatchCreateDataTableValueResponse,
    ConnectBatchDeleteDataTableValueRequest,
    ConnectBatchDeleteDataTableValueResponse,
    ConnectBatchDescribeDataTableValueRequest,
    ConnectBatchDescribeDataTableValueResponse,
    ConnectBatchDisassociateAnalyticsDataSetRequest,
    ConnectBatchDisassociateAnalyticsDataSetResponse,
    ConnectBatchGetAttachedFileMetadataRequest,
    ConnectBatchGetAttachedFileMetadataResponse,
    ConnectBatchGetFlowAssociationRequest,
    ConnectBatchGetFlowAssociationResponse,
    ConnectBatchPutContactRequest,
    ConnectBatchPutContactResponse,
    ConnectBatchUpdateDataTableValueRequest,
    ConnectBatchUpdateDataTableValueResponse,
    ConnectClaimPhoneNumberRequest,
    ConnectClaimPhoneNumberResponse,
    ConnectCompleteAttachedFileUploadRequest,
    ConnectCompleteAttachedFileUploadResponse,
    ConnectCreateAgentStatusRequest,
    ConnectCreateAgentStatusResponse,
    ConnectCreateAttachedFileRequest,
    ConnectCreateAttachedFileResponse,
    ConnectCreateAuthCodeRequest,
    ConnectCreateAuthCodeResponse,
    ConnectCreateContactFlowAliasRequest,
    ConnectCreateContactFlowAliasResponse,
    ConnectCreateContactFlowModuleAliasRequest,
    ConnectCreateContactFlowModuleAliasResponse,
    ConnectCreateContactFlowModuleRequest,
    ConnectCreateContactFlowModuleResponse,
    ConnectCreateContactFlowModuleVersionRequest,
    ConnectCreateContactFlowModuleVersionResponse,
    ConnectCreateContactFlowRequest,
    ConnectCreateContactFlowResponse,
    ConnectCreateContactFlowVersionRequest,
    ConnectCreateContactFlowVersionResponse,
    ConnectCreateContactRequest,
    ConnectCreateContactResponse,
    ConnectCreateDataTableAttributeRequest,
    ConnectCreateDataTableAttributeResponse,
    ConnectCreateDataTableRequest,
    ConnectCreateDataTableResponse,
    ConnectCreateEmailAddressRequest,
    ConnectCreateEmailAddressResponse,
    ConnectCreateEvaluationFormRequest,
    ConnectCreateEvaluationFormResponse,
    ConnectCreateExtractionDefinitionRequest,
    ConnectCreateExtractionDefinitionResponse,
    ConnectCreateHoursOfOperationOverrideRequest,
    ConnectCreateHoursOfOperationOverrideResponse,
    ConnectCreateHoursOfOperationRequest,
    ConnectCreateHoursOfOperationResponse,
    ConnectCreateInstanceRequest,
    ConnectCreateInstanceResponse,
    ConnectCreateIntegrationAssociationRequest,
    ConnectCreateIntegrationAssociationResponse,
    ConnectCreateMetricRequest,
    ConnectCreateMetricResponse,
    ConnectCreateNotificationRequest,
    ConnectCreateNotificationResponse,
    ConnectCreateParticipantRequest,
    ConnectCreateParticipantResponse,
    ConnectCreatePersistentContactAssociationRequest,
    ConnectCreatePersistentContactAssociationResponse,
    ConnectCreatePredefinedAttributeRequest,
    ConnectCreatePredefinedAttributeResponse,
    ConnectCreatePromptRequest,
    ConnectCreatePromptResponse,
    ConnectCreatePushNotificationRegistrationRequest,
    ConnectCreatePushNotificationRegistrationResponse,
    ConnectCreateQueueRequest,
    ConnectCreateQueueResponse,
    ConnectCreateQuickConnectRequest,
    ConnectCreateQuickConnectResponse,
    ConnectCreateRoutingProfileRequest,
    ConnectCreateRoutingProfileResponse,
    ConnectCreateRuleRequest,
    ConnectCreateRuleResponse,
    ConnectCreateSecurityProfileRequest,
    ConnectCreateSecurityProfileResponse,
    ConnectCreateTaskTemplateRequest,
    ConnectCreateTaskTemplateResponse,
    ConnectCreateTestCaseRequest,
    ConnectCreateTestCaseResponse,
    ConnectCreateTrafficDistributionGroupRequest,
    ConnectCreateTrafficDistributionGroupResponse,
    ConnectCreateUseCaseRequest,
    ConnectCreateUseCaseResponse,
    ConnectCreateUserHierarchyGroupRequest,
    ConnectCreateUserHierarchyGroupResponse,
    ConnectCreateUserRequest,
    ConnectCreateUserResponse,
    ConnectCreateViewRequest,
    ConnectCreateViewResponse,
    ConnectCreateViewVersionRequest,
    ConnectCreateViewVersionResponse,
    ConnectCreateVocabularyRequest,
    ConnectCreateVocabularyResponse,
    ConnectCreateWorkspacePageRequest,
    ConnectCreateWorkspacePageResponse,
    ConnectCreateWorkspaceRequest,
    ConnectCreateWorkspaceResponse,
    ConnectDeactivateEvaluationFormRequest,
    ConnectDeactivateEvaluationFormResponse,
    ConnectDeleteAllEntitySessionsRequest,
    ConnectDeleteAllEntitySessionsResponse,
    ConnectDeleteAttachedFileRequest,
    ConnectDeleteAttachedFileResponse,
    ConnectDeleteContactDataRequest,
    ConnectDeleteContactDataResponse,
    ConnectDeleteContactEvaluationRequest,
    ConnectDeleteContactEvaluationResponse,
    ConnectDeleteContactFlowAliasRequest,
    ConnectDeleteContactFlowAliasResponse,
    ConnectDeleteContactFlowModuleAliasRequest,
    ConnectDeleteContactFlowModuleAliasResponse,
    ConnectDeleteContactFlowModuleRequest,
    ConnectDeleteContactFlowModuleResponse,
    ConnectDeleteContactFlowModuleVersionRequest,
    ConnectDeleteContactFlowModuleVersionResponse,
    ConnectDeleteContactFlowRequest,
    ConnectDeleteContactFlowResponse,
    ConnectDeleteContactFlowVersionRequest,
    ConnectDeleteContactFlowVersionResponse,
    ConnectDeleteDataTableAttributeRequest,
    ConnectDeleteDataTableAttributeResponse,
    ConnectDeleteDataTableRequest,
    ConnectDeleteDataTableResponse,
    ConnectDeleteEmailAddressRequest,
    ConnectDeleteEmailAddressResponse,
    ConnectDeleteEvaluationFormRequest,
    ConnectDeleteEvaluationFormResponse,
    ConnectDeleteExtractionDefinitionRequest,
    ConnectDeleteExtractionDefinitionResponse,
    ConnectDeleteHoursOfOperationOverrideRequest,
    ConnectDeleteHoursOfOperationOverrideResponse,
    ConnectDeleteHoursOfOperationRequest,
    ConnectDeleteHoursOfOperationResponse,
    ConnectDeleteInstanceRequest,
    ConnectDeleteInstanceResponse,
    ConnectDeleteIntegrationAssociationRequest,
    ConnectDeleteIntegrationAssociationResponse,
    ConnectDeleteMetricRequest,
    ConnectDeleteMetricResponse,
    ConnectDeleteNotificationRequest,
    ConnectDeleteNotificationResponse,
    ConnectDeletePredefinedAttributeRequest,
    ConnectDeletePredefinedAttributeResponse,
    ConnectDeletePromptRequest,
    ConnectDeletePromptResponse,
    ConnectDeletePushNotificationRegistrationRequest,
    ConnectDeletePushNotificationRegistrationResponse,
    ConnectDeleteQueueRequest,
    ConnectDeleteQueueResponse,
    ConnectDeleteQuickConnectRequest,
    ConnectDeleteQuickConnectResponse,
    ConnectDeleteRoutingProfileRequest,
    ConnectDeleteRoutingProfileResponse,
    ConnectDeleteRuleRequest,
    ConnectDeleteRuleResponse,
    ConnectDeleteSecurityProfileRequest,
    ConnectDeleteSecurityProfileResponse,
    ConnectDeleteSessionRequest,
    ConnectDeleteSessionResponse,
    ConnectDeleteTaskTemplateRequest,
    ConnectDeleteTaskTemplateResponse,
    ConnectDeleteTestCaseRequest,
    ConnectDeleteTestCaseResponse,
    ConnectDeleteTrafficDistributionGroupRequest,
    ConnectDeleteTrafficDistributionGroupResponse,
    ConnectDeleteUseCaseRequest,
    ConnectDeleteUseCaseResponse,
    ConnectDeleteUserHierarchyGroupRequest,
    ConnectDeleteUserHierarchyGroupResponse,
    ConnectDeleteUserRequest,
    ConnectDeleteUserResponse,
    ConnectDeleteViewRequest,
    ConnectDeleteViewResponse,
    ConnectDeleteViewVersionRequest,
    ConnectDeleteViewVersionResponse,
    ConnectDeleteVocabularyRequest,
    ConnectDeleteVocabularyResponse,
    ConnectDeleteWorkspaceMediaRequest,
    ConnectDeleteWorkspaceMediaResponse,
    ConnectDeleteWorkspacePageRequest,
    ConnectDeleteWorkspacePageResponse,
    ConnectDeleteWorkspaceRequest,
    ConnectDeleteWorkspaceResponse,
    ConnectDescribeAgentStatusRequest,
    ConnectDescribeAgentStatusResponse,
    ConnectDescribeAttachedFilesConfigurationRequest,
    ConnectDescribeAttachedFilesConfigurationResponse,
    ConnectDescribeAuthenticationProfileRequest,
    ConnectDescribeAuthenticationProfileResponse,
    ConnectDescribeContactEvaluationRequest,
    ConnectDescribeContactEvaluationResponse,
    ConnectDescribeContactFlowAliasRequest,
    ConnectDescribeContactFlowAliasResponse,
    ConnectDescribeContactFlowModuleAliasRequest,
    ConnectDescribeContactFlowModuleAliasResponse,
    ConnectDescribeContactFlowModuleRequest,
    ConnectDescribeContactFlowModuleResponse,
    ConnectDescribeContactFlowRequest,
    ConnectDescribeContactFlowResponse,
    ConnectDescribeContactRequest,
    ConnectDescribeContactResponse,
    ConnectDescribeDataTableAttributeRequest,
    ConnectDescribeDataTableAttributeResponse,
    ConnectDescribeDataTableRequest,
    ConnectDescribeDataTableResponse,
    ConnectDescribeEmailAddressRequest,
    ConnectDescribeEmailAddressResponse,
    ConnectDescribeEvaluationFormRequest,
    ConnectDescribeEvaluationFormResponse,
    ConnectDescribeExtractionDefinitionRequest,
    ConnectDescribeExtractionDefinitionResponse,
    ConnectDescribeHoursOfOperationOverrideRequest,
    ConnectDescribeHoursOfOperationOverrideResponse,
    ConnectDescribeHoursOfOperationRequest,
    ConnectDescribeHoursOfOperationResponse,
    ConnectDescribeInstanceAttributeRequest,
    ConnectDescribeInstanceAttributeResponse,
    ConnectDescribeInstanceRequest,
    ConnectDescribeInstanceResponse,
    ConnectDescribeInstanceStorageConfigRequest,
    ConnectDescribeInstanceStorageConfigResponse,
    ConnectDescribeMetricRequest,
    ConnectDescribeMetricResponse,
    ConnectDescribeNotificationRequest,
    ConnectDescribeNotificationResponse,
    ConnectDescribePhoneNumberRequest,
    ConnectDescribePhoneNumberResponse,
    ConnectDescribePredefinedAttributeRequest,
    ConnectDescribePredefinedAttributeResponse,
    ConnectDescribePromptRequest,
    ConnectDescribePromptResponse,
    ConnectDescribeQueueRequest,
    ConnectDescribeQueueResponse,
    ConnectDescribeQuickConnectRequest,
    ConnectDescribeQuickConnectResponse,
    ConnectDescribeRoutingProfileRequest,
    ConnectDescribeRoutingProfileResponse,
    ConnectDescribeRuleRequest,
    ConnectDescribeRuleResponse,
    ConnectDescribeSecurityProfileRequest,
    ConnectDescribeSecurityProfileResponse,
    ConnectDescribeTestCaseRequest,
    ConnectDescribeTestCaseResponse,
    ConnectDescribeTrafficDistributionGroupRequest,
    ConnectDescribeTrafficDistributionGroupResponse,
    ConnectDescribeUserHierarchyGroupRequest,
    ConnectDescribeUserHierarchyGroupResponse,
    ConnectDescribeUserHierarchyStructureRequest,
    ConnectDescribeUserHierarchyStructureResponse,
    ConnectDescribeUserRequest,
    ConnectDescribeUserResponse,
    ConnectDescribeViewRequest,
    ConnectDescribeViewResponse,
    ConnectDescribeVocabularyRequest,
    ConnectDescribeVocabularyResponse,
    ConnectDescribeWorkspaceRequest,
    ConnectDescribeWorkspaceResponse,
    ConnectDisassociateAnalyticsDataSetRequest,
    ConnectDisassociateAnalyticsDataSetResponse,
    ConnectDisassociateApprovedOriginRequest,
    ConnectDisassociateApprovedOriginResponse,
    ConnectDisassociateBotRequest,
    ConnectDisassociateBotResponse,
    ConnectDisassociateEmailAddressAliasRequest,
    ConnectDisassociateEmailAddressAliasResponse,
    ConnectDisassociateFlowRequest,
    ConnectDisassociateFlowResponse,
    ConnectDisassociateHoursOfOperationsRequest,
    ConnectDisassociateHoursOfOperationsResponse,
    ConnectDisassociateInstanceStorageConfigRequest,
    ConnectDisassociateInstanceStorageConfigResponse,
    ConnectDisassociateLambdaFunctionRequest,
    ConnectDisassociateLambdaFunctionResponse,
    ConnectDisassociateLexBotRequest,
    ConnectDisassociateLexBotResponse,
    ConnectDisassociatePhoneNumberContactFlowRequest,
    ConnectDisassociatePhoneNumberContactFlowResponse,
    ConnectDisassociateQueueEmailAddressesRequest,
    ConnectDisassociateQueueEmailAddressesResponse,
    ConnectDisassociateQueueQuickConnectsRequest,
    ConnectDisassociateQueueQuickConnectsResponse,
    ConnectDisassociateRoutingProfileQueuesRequest,
    ConnectDisassociateRoutingProfileQueuesResponse,
    ConnectDisassociateSecurityKeyRequest,
    ConnectDisassociateSecurityKeyResponse,
    ConnectDisassociateSecurityProfilesRequest,
    ConnectDisassociateSecurityProfilesResponse,
    ConnectDisassociateTrafficDistributionGroupUserRequest,
    ConnectDisassociateTrafficDistributionGroupUserResponse,
    ConnectDisassociateUserProficienciesRequest,
    ConnectDisassociateUserProficienciesResponse,
    ConnectDisassociateWorkspaceRequest,
    ConnectDisassociateWorkspaceResponse,
    ConnectDismissUserContactRequest,
    ConnectDismissUserContactResponse,
    ConnectEvaluateDataTableValuesRequest,
    ConnectEvaluateDataTableValuesResponse,
    ConnectGetAttachedFileRequest,
    ConnectGetAttachedFileResponse,
    ConnectGetContactAttributesRequest,
    ConnectGetContactAttributesResponse,
    ConnectGetContactMetricsRequest,
    ConnectGetContactMetricsResponse,
    ConnectGetCrossRegionRoutingRequest,
    ConnectGetCrossRegionRoutingResponse,
    ConnectGetCurrentMetricDataRequest,
    ConnectGetCurrentMetricDataResponse,
    ConnectGetCurrentUserDataRequest,
    ConnectGetCurrentUserDataResponse,
    ConnectGetEffectiveHoursOfOperationsRequest,
    ConnectGetEffectiveHoursOfOperationsResponse,
    ConnectGetEvaluationFormValidationRequest,
    ConnectGetEvaluationFormValidationResponse,
    ConnectGetFederationTokenRequest,
    ConnectGetFederationTokenResponse,
    ConnectGetFlowAssociationRequest,
    ConnectGetFlowAssociationResponse,
    ConnectGetMetricDataRequest,
    ConnectGetMetricDataResponse,
    ConnectGetMetricDataV2Request,
    ConnectGetMetricDataV2Response,
    ConnectGetPromptFileRequest,
    ConnectGetPromptFileResponse,
    ConnectGetTaskTemplateRequest,
    ConnectGetTaskTemplateResponse,
    ConnectGetTestCaseExecutionSummaryRequest,
    ConnectGetTestCaseExecutionSummaryResponse,
    ConnectGetTrafficDistributionRequest,
    ConnectGetTrafficDistributionResponse,
    ConnectImportPhoneNumberRequest,
    ConnectImportPhoneNumberResponse,
    ConnectImportWorkspaceMediaRequest,
    ConnectImportWorkspaceMediaResponse,
    ConnectListAgentStatusesRequest,
    ConnectListAgentStatusesResponse,
    ConnectListAnalyticsDataAssociationsRequest,
    ConnectListAnalyticsDataAssociationsResponse,
    ConnectListAnalyticsDataLakeDataSetsRequest,
    ConnectListAnalyticsDataLakeDataSetsResponse,
    ConnectListApprovedOriginsRequest,
    ConnectListApprovedOriginsResponse,
    ConnectListAssociatedContactsRequest,
    ConnectListAssociatedContactsResponse,
    ConnectListAttachedFilesConfigurationsRequest,
    ConnectListAttachedFilesConfigurationsResponse,
    ConnectListAuthenticationProfilesRequest,
    ConnectListAuthenticationProfilesResponse,
    ConnectListBotsRequest,
    ConnectListBotsResponse,
    ConnectListChildHoursOfOperationsRequest,
    ConnectListChildHoursOfOperationsResponse,
    ConnectListContactEvaluationsRequest,
    ConnectListContactEvaluationsResponse,
    ConnectListContactFlowAliasesRequest,
    ConnectListContactFlowAliasesResponse,
    ConnectListContactFlowModuleAliasesRequest,
    ConnectListContactFlowModuleAliasesResponse,
    ConnectListContactFlowModuleVersionsRequest,
    ConnectListContactFlowModuleVersionsResponse,
    ConnectListContactFlowModulesRequest,
    ConnectListContactFlowModulesResponse,
    ConnectListContactFlowVersionsRequest,
    ConnectListContactFlowVersionsResponse,
    ConnectListContactFlowsRequest,
    ConnectListContactFlowsResponse,
    ConnectListContactReferencesRequest,
    ConnectListContactReferencesResponse,
    ConnectListDataTableAttributesRequest,
    ConnectListDataTableAttributesResponse,
    ConnectListDataTablePrimaryValuesRequest,
    ConnectListDataTablePrimaryValuesResponse,
    ConnectListDataTableValuesRequest,
    ConnectListDataTableValuesResponse,
    ConnectListDataTablesRequest,
    ConnectListDataTablesResponse,
    ConnectListDefaultVocabulariesRequest,
    ConnectListDefaultVocabulariesResponse,
    ConnectListEntitySecurityProfilesRequest,
    ConnectListEntitySecurityProfilesResponse,
    ConnectListEvaluationFormAIVersionsRequest,
    ConnectListEvaluationFormAIVersionsResponse,
    ConnectListEvaluationFormVersionsRequest,
    ConnectListEvaluationFormVersionsResponse,
    ConnectListEvaluationFormsRequest,
    ConnectListEvaluationFormsResponse,
    ConnectListExtractionDefinitionsRequest,
    ConnectListExtractionDefinitionsResponse,
    ConnectListFlowAssociationsRequest,
    ConnectListFlowAssociationsResponse,
    ConnectListHoursOfOperationOverridesRequest,
    ConnectListHoursOfOperationOverridesResponse,
    ConnectListHoursOfOperationsRequest,
    ConnectListHoursOfOperationsResponse,
    ConnectListInstanceAttributesRequest,
    ConnectListInstanceAttributesResponse,
    ConnectListInstanceStorageConfigsRequest,
    ConnectListInstanceStorageConfigsResponse,
    ConnectListInstancesRequest,
    ConnectListInstancesResponse,
    ConnectListIntegrationAssociationsRequest,
    ConnectListIntegrationAssociationsResponse,
    ConnectListLambdaFunctionsRequest,
    ConnectListLambdaFunctionsResponse,
    ConnectListLexBotsRequest,
    ConnectListLexBotsResponse,
    ConnectListMetricsRequest,
    ConnectListMetricsResponse,
    ConnectListNotificationsRequest,
    ConnectListNotificationsResponse,
    ConnectListPhoneNumbersRequest,
    ConnectListPhoneNumbersResponse,
    ConnectListPhoneNumbersV2Request,
    ConnectListPhoneNumbersV2Response,
    ConnectListPredefinedAttributesRequest,
    ConnectListPredefinedAttributesResponse,
    ConnectListPromptsRequest,
    ConnectListPromptsResponse,
    ConnectListQueueEmailAddressesRequest,
    ConnectListQueueEmailAddressesResponse,
    ConnectListQueueQuickConnectsRequest,
    ConnectListQueueQuickConnectsResponse,
    ConnectListQueuesRequest,
    ConnectListQueuesResponse,
    ConnectListQuickConnectsRequest,
    ConnectListQuickConnectsResponse,
    ConnectListRealtimeContactAnalysisSegmentsV2Request,
    ConnectListRealtimeContactAnalysisSegmentsV2Response,
    ConnectListReplicationFindingsRequest,
    ConnectListReplicationFindingsResponse,
    ConnectListRoutingProfileManualAssignmentQueuesRequest,
    ConnectListRoutingProfileManualAssignmentQueuesResponse,
    ConnectListRoutingProfileQueuesRequest,
    ConnectListRoutingProfileQueuesResponse,
    ConnectListRoutingProfilesRequest,
    ConnectListRoutingProfilesResponse,
    ConnectListRulesRequest,
    ConnectListRulesResponse,
    ConnectListSecurityKeysRequest,
    ConnectListSecurityKeysResponse,
    ConnectListSecurityProfileAIAgentsRequest,
    ConnectListSecurityProfileAIAgentsResponse,
    ConnectListSecurityProfileApplicationsRequest,
    ConnectListSecurityProfileApplicationsResponse,
    ConnectListSecurityProfileFlowModulesRequest,
    ConnectListSecurityProfileFlowModulesResponse,
    ConnectListSecurityProfilePermissionsRequest,
    ConnectListSecurityProfilePermissionsResponse,
    ConnectListSecurityProfilesRequest,
    ConnectListSecurityProfilesResponse,
    ConnectListTagsForResourceRequest,
    ConnectListTagsForResourceResponse,
    ConnectListTaskTemplatesRequest,
    ConnectListTaskTemplatesResponse,
    ConnectListTestCaseExecutionRecordsRequest,
    ConnectListTestCaseExecutionRecordsResponse,
    ConnectListTestCaseExecutionsRequest,
    ConnectListTestCaseExecutionsResponse,
    ConnectListTestCasesRequest,
    ConnectListTestCasesResponse,
    ConnectListTrafficDistributionGroupUsersRequest,
    ConnectListTrafficDistributionGroupUsersResponse,
    ConnectListTrafficDistributionGroupsRequest,
    ConnectListTrafficDistributionGroupsResponse,
    ConnectListUseCasesRequest,
    ConnectListUseCasesResponse,
    ConnectListUserHierarchyGroupsRequest,
    ConnectListUserHierarchyGroupsResponse,
    ConnectListUserNotificationsRequest,
    ConnectListUserNotificationsResponse,
    ConnectListUserProficienciesRequest,
    ConnectListUserProficienciesResponse,
    ConnectListUsersRequest,
    ConnectListUsersResponse,
    ConnectListViewVersionsRequest,
    ConnectListViewVersionsResponse,
    ConnectListViewsRequest,
    ConnectListViewsResponse,
    ConnectListWorkspaceMediaRequest,
    ConnectListWorkspaceMediaResponse,
    ConnectListWorkspacePagesRequest,
    ConnectListWorkspacePagesResponse,
    ConnectListWorkspacesRequest,
    ConnectListWorkspacesResponse,
    ConnectMonitorContactRequest,
    ConnectMonitorContactResponse,
    ConnectPauseContactRequest,
    ConnectPauseContactResponse,
    ConnectPutUserStatusRequest,
    ConnectPutUserStatusResponse,
    ConnectReleasePhoneNumberRequest,
    ConnectReleasePhoneNumberResponse,
    ConnectReplicateInstanceRequest,
    ConnectReplicateInstanceResponse,
    ConnectResumeContactRecordingRequest,
    ConnectResumeContactRecordingResponse,
    ConnectResumeContactRequest,
    ConnectResumeContactResponse,
    ConnectSearchAgentStatusesRequest,
    ConnectSearchAgentStatusesResponse,
    ConnectSearchAvailablePhoneNumbersRequest,
    ConnectSearchAvailablePhoneNumbersResponse,
    ConnectSearchContactEvaluationsRequest,
    ConnectSearchContactEvaluationsResponse,
    ConnectSearchContactFlowModulesRequest,
    ConnectSearchContactFlowModulesResponse,
    ConnectSearchContactFlowsRequest,
    ConnectSearchContactFlowsResponse,
    ConnectSearchContactsRequest,
    ConnectSearchContactsResponse,
    ConnectSearchDataTablesRequest,
    ConnectSearchDataTablesResponse,
    ConnectSearchEmailAddressesRequest,
    ConnectSearchEmailAddressesResponse,
    ConnectSearchEvaluationFormsRequest,
    ConnectSearchEvaluationFormsResponse,
    ConnectSearchHoursOfOperationOverridesRequest,
    ConnectSearchHoursOfOperationOverridesResponse,
    ConnectSearchHoursOfOperationsRequest,
    ConnectSearchHoursOfOperationsResponse,
    ConnectSearchMetricsRequest,
    ConnectSearchMetricsResponse,
    ConnectSearchNotificationsRequest,
    ConnectSearchNotificationsResponse,
    ConnectSearchPredefinedAttributesRequest,
    ConnectSearchPredefinedAttributesResponse,
    ConnectSearchPromptsRequest,
    ConnectSearchPromptsResponse,
    ConnectSearchQueuesRequest,
    ConnectSearchQueuesResponse,
    ConnectSearchQuickConnectsRequest,
    ConnectSearchQuickConnectsResponse,
    ConnectSearchResourceTagsRequest,
    ConnectSearchResourceTagsResponse,
    ConnectSearchRoutingProfilesRequest,
    ConnectSearchRoutingProfilesResponse,
    ConnectSearchRulesRequest,
    ConnectSearchRulesResponse,
    ConnectSearchSecurityProfilesRequest,
    ConnectSearchSecurityProfilesResponse,
    ConnectSearchTestCasesRequest,
    ConnectSearchTestCasesResponse,
    ConnectSearchUserHierarchyGroupsRequest,
    ConnectSearchUserHierarchyGroupsResponse,
    ConnectSearchUsersRequest,
    ConnectSearchUsersResponse,
    ConnectSearchViewsRequest,
    ConnectSearchViewsResponse,
    ConnectSearchVocabulariesRequest,
    ConnectSearchVocabulariesResponse,
    ConnectSearchWorkspaceAssociationsRequest,
    ConnectSearchWorkspaceAssociationsResponse,
    ConnectSearchWorkspacesRequest,
    ConnectSearchWorkspacesResponse,
    ConnectSendChatIntegrationEventRequest,
    ConnectSendChatIntegrationEventResponse,
    ConnectSendOutboundEmailRequest,
    ConnectSendOutboundEmailResponse,
    ConnectSendOutboundWebNotificationRequest,
    ConnectSendOutboundWebNotificationResponse,
    ConnectStartAssistantContactRequest,
    ConnectStartAssistantContactResponse,
    ConnectStartAttachedFileUploadRequest,
    ConnectStartAttachedFileUploadResponse,
    ConnectStartChatContactRequest,
    ConnectStartChatContactResponse,
    ConnectStartContactConversationalAnalyticsJobRequest,
    ConnectStartContactConversationalAnalyticsJobResponse,
    ConnectStartContactEvaluationRequest,
    ConnectStartContactEvaluationResponse,
    ConnectStartContactMediaProcessingRequest,
    ConnectStartContactMediaProcessingResponse,
    ConnectStartContactRecordingRequest,
    ConnectStartContactRecordingResponse,
    ConnectStartContactStreamingRequest,
    ConnectStartContactStreamingResponse,
    ConnectStartEmailContactRequest,
    ConnectStartEmailContactResponse,
    ConnectStartEvaluationFormValidationRequest,
    ConnectStartEvaluationFormValidationResponse,
    ConnectStartOutboundChatContactRequest,
    ConnectStartOutboundChatContactResponse,
    ConnectStartOutboundEmailContactRequest,
    ConnectStartOutboundEmailContactResponse,
    ConnectStartOutboundVoiceContactRequest,
    ConnectStartOutboundVoiceContactResponse,
    ConnectStartScreenSharingRequest,
    ConnectStartScreenSharingResponse,
    ConnectStartTaskContactRequest,
    ConnectStartTaskContactResponse,
    ConnectStartTestCaseExecutionRequest,
    ConnectStartTestCaseExecutionResponse,
    ConnectStartWebRTCContactRequest,
    ConnectStartWebRTCContactResponse,
    ConnectStopContactMediaProcessingRequest,
    ConnectStopContactMediaProcessingResponse,
    ConnectStopContactRecordingRequest,
    ConnectStopContactRecordingResponse,
    ConnectStopContactRequest,
    ConnectStopContactResponse,
    ConnectStopContactStreamingRequest,
    ConnectStopContactStreamingResponse,
    ConnectStopTestCaseExecutionRequest,
    ConnectStopTestCaseExecutionResponse,
    ConnectSubmitContactEvaluationRequest,
    ConnectSubmitContactEvaluationResponse,
    ConnectSuspendContactRecordingRequest,
    ConnectSuspendContactRecordingResponse,
    ConnectTagContactRequest,
    ConnectTagContactResponse,
    ConnectTagResourceRequest,
    ConnectTagResourceResponse,
    ConnectTransferContactRequest,
    ConnectTransferContactResponse,
    ConnectUntagContactRequest,
    ConnectUntagContactResponse,
    ConnectUntagResourceRequest,
    ConnectUntagResourceResponse,
    ConnectUpdateAgentStatusRequest,
    ConnectUpdateAgentStatusResponse,
    ConnectUpdateAttachedFilesConfigurationRequest,
    ConnectUpdateAttachedFilesConfigurationResponse,
    ConnectUpdateAuthenticationProfileRequest,
    ConnectUpdateAuthenticationProfileResponse,
    ConnectUpdateContactAttributesRequest,
    ConnectUpdateContactAttributesResponse,
    ConnectUpdateContactEvaluationRequest,
    ConnectUpdateContactEvaluationResponse,
    ConnectUpdateContactFlowAliasRequest,
    ConnectUpdateContactFlowAliasResponse,
    ConnectUpdateContactFlowContentRequest,
    ConnectUpdateContactFlowContentResponse,
    ConnectUpdateContactFlowMetadataRequest,
    ConnectUpdateContactFlowMetadataResponse,
    ConnectUpdateContactFlowModuleAliasRequest,
    ConnectUpdateContactFlowModuleAliasResponse,
    ConnectUpdateContactFlowModuleContentRequest,
    ConnectUpdateContactFlowModuleContentResponse,
    ConnectUpdateContactFlowModuleMetadataRequest,
    ConnectUpdateContactFlowModuleMetadataResponse,
    ConnectUpdateContactFlowNameRequest,
    ConnectUpdateContactFlowNameResponse,
    ConnectUpdateContactRequest,
    ConnectUpdateContactResponse,
    ConnectUpdateContactRoutingDataRequest,
    ConnectUpdateContactRoutingDataResponse,
    ConnectUpdateContactScheduleRequest,
    ConnectUpdateContactScheduleResponse,
    ConnectUpdateContactTaskTemplateRequest,
    ConnectUpdateContactTaskTemplateResponse,
    ConnectUpdateCrossRegionRoutingRequest,
    ConnectUpdateCrossRegionRoutingResponse,
    ConnectUpdateDataTableAttributeRequest,
    ConnectUpdateDataTableAttributeResponse,
    ConnectUpdateDataTableMetadataRequest,
    ConnectUpdateDataTableMetadataResponse,
    ConnectUpdateDataTablePrimaryValuesRequest,
    ConnectUpdateDataTablePrimaryValuesResponse,
    ConnectUpdateEmailAddressMetadataRequest,
    ConnectUpdateEmailAddressMetadataResponse,
    ConnectUpdateEvaluationFormRequest,
    ConnectUpdateEvaluationFormResponse,
    ConnectUpdateExtractionDefinitionRequest,
    ConnectUpdateExtractionDefinitionResponse,
    ConnectUpdateHoursOfOperationOverrideRequest,
    ConnectUpdateHoursOfOperationOverrideResponse,
    ConnectUpdateHoursOfOperationRequest,
    ConnectUpdateHoursOfOperationResponse,
    ConnectUpdateInstanceAttributeRequest,
    ConnectUpdateInstanceAttributeResponse,
    ConnectUpdateInstanceStorageConfigRequest,
    ConnectUpdateInstanceStorageConfigResponse,
    ConnectUpdateMetricContentRequest,
    ConnectUpdateMetricContentResponse,
    ConnectUpdateMetricMetadataRequest,
    ConnectUpdateMetricMetadataResponse,
    ConnectUpdateNotificationContentRequest,
    ConnectUpdateNotificationContentResponse,
    ConnectUpdateOutboundEmailContactMessageRequest,
    ConnectUpdateOutboundEmailContactMessageResponse,
    ConnectUpdateParticipantAuthenticationRequest,
    ConnectUpdateParticipantAuthenticationResponse,
    ConnectUpdateParticipantRoleConfigRequest,
    ConnectUpdateParticipantRoleConfigResponse,
    ConnectUpdatePhoneNumberMetadataRequest,
    ConnectUpdatePhoneNumberMetadataResponse,
    ConnectUpdatePhoneNumberRequest,
    ConnectUpdatePhoneNumberResponse,
    ConnectUpdatePredefinedAttributeRequest,
    ConnectUpdatePredefinedAttributeResponse,
    ConnectUpdatePromptRequest,
    ConnectUpdatePromptResponse,
    ConnectUpdateQueueHoursOfOperationRequest,
    ConnectUpdateQueueHoursOfOperationResponse,
    ConnectUpdateQueueMaxContactsRequest,
    ConnectUpdateQueueMaxContactsResponse,
    ConnectUpdateQueueNameRequest,
    ConnectUpdateQueueNameResponse,
    ConnectUpdateQueueOutboundCallerConfigRequest,
    ConnectUpdateQueueOutboundCallerConfigResponse,
    ConnectUpdateQueueOutboundEmailConfigRequest,
    ConnectUpdateQueueOutboundEmailConfigResponse,
    ConnectUpdateQueueStatusRequest,
    ConnectUpdateQueueStatusResponse,
    ConnectUpdateQuickConnectConfigRequest,
    ConnectUpdateQuickConnectConfigResponse,
    ConnectUpdateQuickConnectNameRequest,
    ConnectUpdateQuickConnectNameResponse,
    ConnectUpdateRoutingProfileAgentAvailabilityTimerRequest,
    ConnectUpdateRoutingProfileAgentAvailabilityTimerResponse,
    ConnectUpdateRoutingProfileConcurrencyRequest,
    ConnectUpdateRoutingProfileConcurrencyResponse,
    ConnectUpdateRoutingProfileDefaultOutboundQueueRequest,
    ConnectUpdateRoutingProfileDefaultOutboundQueueResponse,
    ConnectUpdateRoutingProfileNameRequest,
    ConnectUpdateRoutingProfileNameResponse,
    ConnectUpdateRoutingProfileQueuesRequest,
    ConnectUpdateRoutingProfileQueuesResponse,
    ConnectUpdateRuleRequest,
    ConnectUpdateRuleResponse,
    ConnectUpdateSecurityProfileRequest,
    ConnectUpdateSecurityProfileResponse,
    ConnectUpdateTaskTemplateRequest,
    ConnectUpdateTaskTemplateResponse,
    ConnectUpdateTestCaseRequest,
    ConnectUpdateTestCaseResponse,
    ConnectUpdateTrafficDistributionRequest,
    ConnectUpdateTrafficDistributionResponse,
    ConnectUpdateUserConfigRequest,
    ConnectUpdateUserConfigResponse,
    ConnectUpdateUserHierarchyGroupNameRequest,
    ConnectUpdateUserHierarchyGroupNameResponse,
    ConnectUpdateUserHierarchyRequest,
    ConnectUpdateUserHierarchyResponse,
    ConnectUpdateUserHierarchyStructureRequest,
    ConnectUpdateUserHierarchyStructureResponse,
    ConnectUpdateUserIdentityInfoRequest,
    ConnectUpdateUserIdentityInfoResponse,
    ConnectUpdateUserNotificationStatusRequest,
    ConnectUpdateUserNotificationStatusResponse,
    ConnectUpdateUserPhoneConfigRequest,
    ConnectUpdateUserPhoneConfigResponse,
    ConnectUpdateUserProficienciesRequest,
    ConnectUpdateUserProficienciesResponse,
    ConnectUpdateUserRoutingProfileRequest,
    ConnectUpdateUserRoutingProfileResponse,
    ConnectUpdateUserSecurityProfilesRequest,
    ConnectUpdateUserSecurityProfilesResponse,
    ConnectUpdateViewContentRequest,
    ConnectUpdateViewContentResponse,
    ConnectUpdateViewMetadataRequest,
    ConnectUpdateViewMetadataResponse,
    ConnectUpdateWorkspaceMetadataRequest,
    ConnectUpdateWorkspaceMetadataResponse,
    ConnectUpdateWorkspacePageRequest,
    ConnectUpdateWorkspacePageResponse,
    ConnectUpdateWorkspaceThemeRequest,
    ConnectUpdateWorkspaceThemeResponse,
    ConnectUpdateWorkspaceVisibilityRequest,
    ConnectUpdateWorkspaceVisibilityResponse,
)
from werkflow_aws.types.aws_connect_client import ConnectClient
from .base import AWSBaseService


class AWSConnect(AWSBaseService[ConnectClient]):
    service_name = 'connect'
    boto3_service_name = 'connect'

    def __init__(self) -> None:
        super().__init__(service_name='connect', boto3_service_name='connect')

    async def activate_evaluation_form(
        self,
        request: ConnectActivateEvaluationFormRequest,
    ) -> ConnectActivateEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.activate_evaluation_form, request, ConnectActivateEvaluationFormResponse)

    async def associate_analytics_data_set(
        self,
        request: ConnectAssociateAnalyticsDataSetRequest,
    ) -> ConnectAssociateAnalyticsDataSetResponse:
        client = self._require_client()
        return await self._execute(client.associate_analytics_data_set, request, ConnectAssociateAnalyticsDataSetResponse)

    async def associate_approved_origin(
        self,
        request: ConnectAssociateApprovedOriginRequest,
    ) -> ConnectAssociateApprovedOriginResponse:
        client = self._require_client()
        return await self._execute(client.associate_approved_origin, request, ConnectAssociateApprovedOriginResponse)

    async def associate_bot(
        self,
        request: ConnectAssociateBotRequest,
    ) -> ConnectAssociateBotResponse:
        client = self._require_client()
        return await self._execute(client.associate_bot, request, ConnectAssociateBotResponse)

    async def associate_contact_with_user(
        self,
        request: ConnectAssociateContactWithUserRequest,
    ) -> ConnectAssociateContactWithUserResponse:
        client = self._require_client()
        return await self._execute(client.associate_contact_with_user, request, ConnectAssociateContactWithUserResponse)

    async def associate_default_vocabulary(
        self,
        request: ConnectAssociateDefaultVocabularyRequest,
    ) -> ConnectAssociateDefaultVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.associate_default_vocabulary, request, ConnectAssociateDefaultVocabularyResponse)

    async def associate_email_address_alias(
        self,
        request: ConnectAssociateEmailAddressAliasRequest,
    ) -> ConnectAssociateEmailAddressAliasResponse:
        client = self._require_client()
        return await self._execute(client.associate_email_address_alias, request, ConnectAssociateEmailAddressAliasResponse)

    async def associate_flow(
        self,
        request: ConnectAssociateFlowRequest,
    ) -> ConnectAssociateFlowResponse:
        client = self._require_client()
        return await self._execute(client.associate_flow, request, ConnectAssociateFlowResponse)

    async def associate_hours_of_operations(
        self,
        request: ConnectAssociateHoursOfOperationsRequest,
    ) -> ConnectAssociateHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.associate_hours_of_operations, request, ConnectAssociateHoursOfOperationsResponse)

    async def associate_instance_storage_config(
        self,
        request: ConnectAssociateInstanceStorageConfigRequest,
    ) -> ConnectAssociateInstanceStorageConfigResponse:
        client = self._require_client()
        return await self._execute(client.associate_instance_storage_config, request, ConnectAssociateInstanceStorageConfigResponse)

    async def associate_lambda_function(
        self,
        request: ConnectAssociateLambdaFunctionRequest,
    ) -> ConnectAssociateLambdaFunctionResponse:
        client = self._require_client()
        return await self._execute(client.associate_lambda_function, request, ConnectAssociateLambdaFunctionResponse)

    async def associate_lex_bot(
        self,
        request: ConnectAssociateLexBotRequest,
    ) -> ConnectAssociateLexBotResponse:
        client = self._require_client()
        return await self._execute(client.associate_lex_bot, request, ConnectAssociateLexBotResponse)

    async def associate_phone_number_contact_flow(
        self,
        request: ConnectAssociatePhoneNumberContactFlowRequest,
    ) -> ConnectAssociatePhoneNumberContactFlowResponse:
        client = self._require_client()
        return await self._execute(client.associate_phone_number_contact_flow, request, ConnectAssociatePhoneNumberContactFlowResponse)

    async def associate_queue_email_addresses(
        self,
        request: ConnectAssociateQueueEmailAddressesRequest,
    ) -> ConnectAssociateQueueEmailAddressesResponse:
        client = self._require_client()
        return await self._execute(client.associate_queue_email_addresses, request, ConnectAssociateQueueEmailAddressesResponse)

    async def associate_queue_quick_connects(
        self,
        request: ConnectAssociateQueueQuickConnectsRequest,
    ) -> ConnectAssociateQueueQuickConnectsResponse:
        client = self._require_client()
        return await self._execute(client.associate_queue_quick_connects, request, ConnectAssociateQueueQuickConnectsResponse)

    async def associate_routing_profile_queues(
        self,
        request: ConnectAssociateRoutingProfileQueuesRequest,
    ) -> ConnectAssociateRoutingProfileQueuesResponse:
        client = self._require_client()
        return await self._execute(client.associate_routing_profile_queues, request, ConnectAssociateRoutingProfileQueuesResponse)

    async def associate_security_key(
        self,
        request: ConnectAssociateSecurityKeyRequest,
    ) -> ConnectAssociateSecurityKeyResponse:
        client = self._require_client()
        return await self._execute(client.associate_security_key, request, ConnectAssociateSecurityKeyResponse)

    async def associate_security_profiles(
        self,
        request: ConnectAssociateSecurityProfilesRequest,
    ) -> ConnectAssociateSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.associate_security_profiles, request, ConnectAssociateSecurityProfilesResponse)

    async def associate_traffic_distribution_group_user(
        self,
        request: ConnectAssociateTrafficDistributionGroupUserRequest,
    ) -> ConnectAssociateTrafficDistributionGroupUserResponse:
        client = self._require_client()
        return await self._execute(client.associate_traffic_distribution_group_user, request, ConnectAssociateTrafficDistributionGroupUserResponse)

    async def associate_user_proficiencies(
        self,
        request: ConnectAssociateUserProficienciesRequest,
    ) -> ConnectAssociateUserProficienciesResponse:
        client = self._require_client()
        return await self._execute(client.associate_user_proficiencies, request, ConnectAssociateUserProficienciesResponse)

    async def associate_workspace(
        self,
        request: ConnectAssociateWorkspaceRequest,
    ) -> ConnectAssociateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.associate_workspace, request, ConnectAssociateWorkspaceResponse)

    async def batch_associate_analytics_data_set(
        self,
        request: ConnectBatchAssociateAnalyticsDataSetRequest,
    ) -> ConnectBatchAssociateAnalyticsDataSetResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_analytics_data_set, request, ConnectBatchAssociateAnalyticsDataSetResponse)

    async def batch_create_data_table_value(
        self,
        request: ConnectBatchCreateDataTableValueRequest,
    ) -> ConnectBatchCreateDataTableValueResponse:
        client = self._require_client()
        return await self._execute(client.batch_create_data_table_value, request, ConnectBatchCreateDataTableValueResponse)

    async def batch_delete_data_table_value(
        self,
        request: ConnectBatchDeleteDataTableValueRequest,
    ) -> ConnectBatchDeleteDataTableValueResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_data_table_value, request, ConnectBatchDeleteDataTableValueResponse)

    async def batch_describe_data_table_value(
        self,
        request: ConnectBatchDescribeDataTableValueRequest,
    ) -> ConnectBatchDescribeDataTableValueResponse:
        client = self._require_client()
        return await self._execute(client.batch_describe_data_table_value, request, ConnectBatchDescribeDataTableValueResponse)

    async def batch_disassociate_analytics_data_set(
        self,
        request: ConnectBatchDisassociateAnalyticsDataSetRequest,
    ) -> ConnectBatchDisassociateAnalyticsDataSetResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_analytics_data_set, request, ConnectBatchDisassociateAnalyticsDataSetResponse)

    async def batch_get_attached_file_metadata(
        self,
        request: ConnectBatchGetAttachedFileMetadataRequest,
    ) -> ConnectBatchGetAttachedFileMetadataResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_attached_file_metadata, request, ConnectBatchGetAttachedFileMetadataResponse)

    async def batch_get_flow_association(
        self,
        request: ConnectBatchGetFlowAssociationRequest,
    ) -> ConnectBatchGetFlowAssociationResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_flow_association, request, ConnectBatchGetFlowAssociationResponse)

    async def batch_put_contact(
        self,
        request: ConnectBatchPutContactRequest,
    ) -> ConnectBatchPutContactResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_contact, request, ConnectBatchPutContactResponse)

    async def batch_update_data_table_value(
        self,
        request: ConnectBatchUpdateDataTableValueRequest,
    ) -> ConnectBatchUpdateDataTableValueResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_data_table_value, request, ConnectBatchUpdateDataTableValueResponse)

    async def claim_phone_number(
        self,
        request: ConnectClaimPhoneNumberRequest,
    ) -> ConnectClaimPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.claim_phone_number, request, ConnectClaimPhoneNumberResponse)

    async def complete_attached_file_upload(
        self,
        request: ConnectCompleteAttachedFileUploadRequest,
    ) -> ConnectCompleteAttachedFileUploadResponse:
        client = self._require_client()
        return await self._execute(client.complete_attached_file_upload, request, ConnectCompleteAttachedFileUploadResponse)

    async def create_agent_status(
        self,
        request: ConnectCreateAgentStatusRequest,
    ) -> ConnectCreateAgentStatusResponse:
        client = self._require_client()
        return await self._execute(client.create_agent_status, request, ConnectCreateAgentStatusResponse)

    async def create_attached_file(
        self,
        request: ConnectCreateAttachedFileRequest,
    ) -> ConnectCreateAttachedFileResponse:
        client = self._require_client()
        return await self._execute(client.create_attached_file, request, ConnectCreateAttachedFileResponse)

    async def create_auth_code(
        self,
        request: ConnectCreateAuthCodeRequest,
    ) -> ConnectCreateAuthCodeResponse:
        client = self._require_client()
        return await self._execute(client.create_auth_code, request, ConnectCreateAuthCodeResponse)

    async def create_contact(
        self,
        request: ConnectCreateContactRequest,
    ) -> ConnectCreateContactResponse:
        client = self._require_client()
        return await self._execute(client.create_contact, request, ConnectCreateContactResponse)

    async def create_contact_flow(
        self,
        request: ConnectCreateContactFlowRequest,
    ) -> ConnectCreateContactFlowResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow, request, ConnectCreateContactFlowResponse)

    async def create_contact_flow_alias(
        self,
        request: ConnectCreateContactFlowAliasRequest,
    ) -> ConnectCreateContactFlowAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow_alias, request, ConnectCreateContactFlowAliasResponse)

    async def create_contact_flow_module(
        self,
        request: ConnectCreateContactFlowModuleRequest,
    ) -> ConnectCreateContactFlowModuleResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow_module, request, ConnectCreateContactFlowModuleResponse)

    async def create_contact_flow_module_alias(
        self,
        request: ConnectCreateContactFlowModuleAliasRequest,
    ) -> ConnectCreateContactFlowModuleAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow_module_alias, request, ConnectCreateContactFlowModuleAliasResponse)

    async def create_contact_flow_module_version(
        self,
        request: ConnectCreateContactFlowModuleVersionRequest,
    ) -> ConnectCreateContactFlowModuleVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow_module_version, request, ConnectCreateContactFlowModuleVersionResponse)

    async def create_contact_flow_version(
        self,
        request: ConnectCreateContactFlowVersionRequest,
    ) -> ConnectCreateContactFlowVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_flow_version, request, ConnectCreateContactFlowVersionResponse)

    async def create_data_table(
        self,
        request: ConnectCreateDataTableRequest,
    ) -> ConnectCreateDataTableResponse:
        client = self._require_client()
        return await self._execute(client.create_data_table, request, ConnectCreateDataTableResponse)

    async def create_data_table_attribute(
        self,
        request: ConnectCreateDataTableAttributeRequest,
    ) -> ConnectCreateDataTableAttributeResponse:
        client = self._require_client()
        return await self._execute(client.create_data_table_attribute, request, ConnectCreateDataTableAttributeResponse)

    async def create_email_address(
        self,
        request: ConnectCreateEmailAddressRequest,
    ) -> ConnectCreateEmailAddressResponse:
        client = self._require_client()
        return await self._execute(client.create_email_address, request, ConnectCreateEmailAddressResponse)

    async def create_evaluation_form(
        self,
        request: ConnectCreateEvaluationFormRequest,
    ) -> ConnectCreateEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.create_evaluation_form, request, ConnectCreateEvaluationFormResponse)

    async def create_extraction_definition(
        self,
        request: ConnectCreateExtractionDefinitionRequest,
    ) -> ConnectCreateExtractionDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_extraction_definition, request, ConnectCreateExtractionDefinitionResponse)

    async def create_hours_of_operation(
        self,
        request: ConnectCreateHoursOfOperationRequest,
    ) -> ConnectCreateHoursOfOperationResponse:
        client = self._require_client()
        return await self._execute(client.create_hours_of_operation, request, ConnectCreateHoursOfOperationResponse)

    async def create_hours_of_operation_override(
        self,
        request: ConnectCreateHoursOfOperationOverrideRequest,
    ) -> ConnectCreateHoursOfOperationOverrideResponse:
        client = self._require_client()
        return await self._execute(client.create_hours_of_operation_override, request, ConnectCreateHoursOfOperationOverrideResponse)

    async def create_instance(
        self,
        request: ConnectCreateInstanceRequest,
    ) -> ConnectCreateInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_instance, request, ConnectCreateInstanceResponse)

    async def create_integration_association(
        self,
        request: ConnectCreateIntegrationAssociationRequest,
    ) -> ConnectCreateIntegrationAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_integration_association, request, ConnectCreateIntegrationAssociationResponse)

    async def create_metric(
        self,
        request: ConnectCreateMetricRequest,
    ) -> ConnectCreateMetricResponse:
        client = self._require_client()
        return await self._execute(client.create_metric, request, ConnectCreateMetricResponse)

    async def create_notification(
        self,
        request: ConnectCreateNotificationRequest,
    ) -> ConnectCreateNotificationResponse:
        client = self._require_client()
        return await self._execute(client.create_notification, request, ConnectCreateNotificationResponse)

    async def create_participant(
        self,
        request: ConnectCreateParticipantRequest,
    ) -> ConnectCreateParticipantResponse:
        client = self._require_client()
        return await self._execute(client.create_participant, request, ConnectCreateParticipantResponse)

    async def create_persistent_contact_association(
        self,
        request: ConnectCreatePersistentContactAssociationRequest,
    ) -> ConnectCreatePersistentContactAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_persistent_contact_association, request, ConnectCreatePersistentContactAssociationResponse)

    async def create_predefined_attribute(
        self,
        request: ConnectCreatePredefinedAttributeRequest,
    ) -> ConnectCreatePredefinedAttributeResponse:
        client = self._require_client()
        return await self._execute(client.create_predefined_attribute, request, ConnectCreatePredefinedAttributeResponse)

    async def create_prompt(
        self,
        request: ConnectCreatePromptRequest,
    ) -> ConnectCreatePromptResponse:
        client = self._require_client()
        return await self._execute(client.create_prompt, request, ConnectCreatePromptResponse)

    async def create_push_notification_registration(
        self,
        request: ConnectCreatePushNotificationRegistrationRequest,
    ) -> ConnectCreatePushNotificationRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.create_push_notification_registration, request, ConnectCreatePushNotificationRegistrationResponse)

    async def create_queue(
        self,
        request: ConnectCreateQueueRequest,
    ) -> ConnectCreateQueueResponse:
        client = self._require_client()
        return await self._execute(client.create_queue, request, ConnectCreateQueueResponse)

    async def create_quick_connect(
        self,
        request: ConnectCreateQuickConnectRequest,
    ) -> ConnectCreateQuickConnectResponse:
        client = self._require_client()
        return await self._execute(client.create_quick_connect, request, ConnectCreateQuickConnectResponse)

    async def create_routing_profile(
        self,
        request: ConnectCreateRoutingProfileRequest,
    ) -> ConnectCreateRoutingProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_routing_profile, request, ConnectCreateRoutingProfileResponse)

    async def create_rule(
        self,
        request: ConnectCreateRuleRequest,
    ) -> ConnectCreateRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_rule, request, ConnectCreateRuleResponse)

    async def create_security_profile(
        self,
        request: ConnectCreateSecurityProfileRequest,
    ) -> ConnectCreateSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_security_profile, request, ConnectCreateSecurityProfileResponse)

    async def create_task_template(
        self,
        request: ConnectCreateTaskTemplateRequest,
    ) -> ConnectCreateTaskTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_task_template, request, ConnectCreateTaskTemplateResponse)

    async def create_test_case(
        self,
        request: ConnectCreateTestCaseRequest,
    ) -> ConnectCreateTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.create_test_case, request, ConnectCreateTestCaseResponse)

    async def create_traffic_distribution_group(
        self,
        request: ConnectCreateTrafficDistributionGroupRequest,
    ) -> ConnectCreateTrafficDistributionGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_distribution_group, request, ConnectCreateTrafficDistributionGroupResponse)

    async def create_use_case(
        self,
        request: ConnectCreateUseCaseRequest,
    ) -> ConnectCreateUseCaseResponse:
        client = self._require_client()
        return await self._execute(client.create_use_case, request, ConnectCreateUseCaseResponse)

    async def create_user(
        self,
        request: ConnectCreateUserRequest,
    ) -> ConnectCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, ConnectCreateUserResponse)

    async def create_user_hierarchy_group(
        self,
        request: ConnectCreateUserHierarchyGroupRequest,
    ) -> ConnectCreateUserHierarchyGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_user_hierarchy_group, request, ConnectCreateUserHierarchyGroupResponse)

    async def create_view(
        self,
        request: ConnectCreateViewRequest,
    ) -> ConnectCreateViewResponse:
        client = self._require_client()
        return await self._execute(client.create_view, request, ConnectCreateViewResponse)

    async def create_view_version(
        self,
        request: ConnectCreateViewVersionRequest,
    ) -> ConnectCreateViewVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_view_version, request, ConnectCreateViewVersionResponse)

    async def create_vocabulary(
        self,
        request: ConnectCreateVocabularyRequest,
    ) -> ConnectCreateVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.create_vocabulary, request, ConnectCreateVocabularyResponse)

    async def create_workspace(
        self,
        request: ConnectCreateWorkspaceRequest,
    ) -> ConnectCreateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace, request, ConnectCreateWorkspaceResponse)

    async def create_workspace_page(
        self,
        request: ConnectCreateWorkspacePageRequest,
    ) -> ConnectCreateWorkspacePageResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_page, request, ConnectCreateWorkspacePageResponse)

    async def deactivate_evaluation_form(
        self,
        request: ConnectDeactivateEvaluationFormRequest,
    ) -> ConnectDeactivateEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_evaluation_form, request, ConnectDeactivateEvaluationFormResponse)

    async def delete_all_entity_sessions(
        self,
        request: ConnectDeleteAllEntitySessionsRequest,
    ) -> ConnectDeleteAllEntitySessionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_all_entity_sessions, request, ConnectDeleteAllEntitySessionsResponse)

    async def delete_attached_file(
        self,
        request: ConnectDeleteAttachedFileRequest,
    ) -> ConnectDeleteAttachedFileResponse:
        client = self._require_client()
        return await self._execute(client.delete_attached_file, request, ConnectDeleteAttachedFileResponse)

    async def delete_contact_data(
        self,
        request: ConnectDeleteContactDataRequest,
    ) -> ConnectDeleteContactDataResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_data, request, ConnectDeleteContactDataResponse)

    async def delete_contact_evaluation(
        self,
        request: ConnectDeleteContactEvaluationRequest,
    ) -> ConnectDeleteContactEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_evaluation, request, ConnectDeleteContactEvaluationResponse)

    async def delete_contact_flow(
        self,
        request: ConnectDeleteContactFlowRequest,
    ) -> ConnectDeleteContactFlowResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow, request, ConnectDeleteContactFlowResponse)

    async def delete_contact_flow_alias(
        self,
        request: ConnectDeleteContactFlowAliasRequest,
    ) -> ConnectDeleteContactFlowAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow_alias, request, ConnectDeleteContactFlowAliasResponse)

    async def delete_contact_flow_module(
        self,
        request: ConnectDeleteContactFlowModuleRequest,
    ) -> ConnectDeleteContactFlowModuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow_module, request, ConnectDeleteContactFlowModuleResponse)

    async def delete_contact_flow_module_alias(
        self,
        request: ConnectDeleteContactFlowModuleAliasRequest,
    ) -> ConnectDeleteContactFlowModuleAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow_module_alias, request, ConnectDeleteContactFlowModuleAliasResponse)

    async def delete_contact_flow_module_version(
        self,
        request: ConnectDeleteContactFlowModuleVersionRequest,
    ) -> ConnectDeleteContactFlowModuleVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow_module_version, request, ConnectDeleteContactFlowModuleVersionResponse)

    async def delete_contact_flow_version(
        self,
        request: ConnectDeleteContactFlowVersionRequest,
    ) -> ConnectDeleteContactFlowVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_flow_version, request, ConnectDeleteContactFlowVersionResponse)

    async def delete_data_table(
        self,
        request: ConnectDeleteDataTableRequest,
    ) -> ConnectDeleteDataTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_table, request, ConnectDeleteDataTableResponse)

    async def delete_data_table_attribute(
        self,
        request: ConnectDeleteDataTableAttributeRequest,
    ) -> ConnectDeleteDataTableAttributeResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_table_attribute, request, ConnectDeleteDataTableAttributeResponse)

    async def delete_email_address(
        self,
        request: ConnectDeleteEmailAddressRequest,
    ) -> ConnectDeleteEmailAddressResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_address, request, ConnectDeleteEmailAddressResponse)

    async def delete_evaluation_form(
        self,
        request: ConnectDeleteEvaluationFormRequest,
    ) -> ConnectDeleteEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.delete_evaluation_form, request, ConnectDeleteEvaluationFormResponse)

    async def delete_extraction_definition(
        self,
        request: ConnectDeleteExtractionDefinitionRequest,
    ) -> ConnectDeleteExtractionDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_extraction_definition, request, ConnectDeleteExtractionDefinitionResponse)

    async def delete_hours_of_operation(
        self,
        request: ConnectDeleteHoursOfOperationRequest,
    ) -> ConnectDeleteHoursOfOperationResponse:
        client = self._require_client()
        return await self._execute(client.delete_hours_of_operation, request, ConnectDeleteHoursOfOperationResponse)

    async def delete_hours_of_operation_override(
        self,
        request: ConnectDeleteHoursOfOperationOverrideRequest,
    ) -> ConnectDeleteHoursOfOperationOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_hours_of_operation_override, request, ConnectDeleteHoursOfOperationOverrideResponse)

    async def delete_instance(
        self,
        request: ConnectDeleteInstanceRequest,
    ) -> ConnectDeleteInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance, request, ConnectDeleteInstanceResponse)

    async def delete_integration_association(
        self,
        request: ConnectDeleteIntegrationAssociationRequest,
    ) -> ConnectDeleteIntegrationAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration_association, request, ConnectDeleteIntegrationAssociationResponse)

    async def delete_metric(
        self,
        request: ConnectDeleteMetricRequest,
    ) -> ConnectDeleteMetricResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric, request, ConnectDeleteMetricResponse)

    async def delete_notification(
        self,
        request: ConnectDeleteNotificationRequest,
    ) -> ConnectDeleteNotificationResponse:
        client = self._require_client()
        return await self._execute(client.delete_notification, request, ConnectDeleteNotificationResponse)

    async def delete_predefined_attribute(
        self,
        request: ConnectDeletePredefinedAttributeRequest,
    ) -> ConnectDeletePredefinedAttributeResponse:
        client = self._require_client()
        return await self._execute(client.delete_predefined_attribute, request, ConnectDeletePredefinedAttributeResponse)

    async def delete_prompt(
        self,
        request: ConnectDeletePromptRequest,
    ) -> ConnectDeletePromptResponse:
        client = self._require_client()
        return await self._execute(client.delete_prompt, request, ConnectDeletePromptResponse)

    async def delete_push_notification_registration(
        self,
        request: ConnectDeletePushNotificationRegistrationRequest,
    ) -> ConnectDeletePushNotificationRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_push_notification_registration, request, ConnectDeletePushNotificationRegistrationResponse)

    async def delete_queue(
        self,
        request: ConnectDeleteQueueRequest,
    ) -> ConnectDeleteQueueResponse:
        client = self._require_client()
        return await self._execute(client.delete_queue, request, ConnectDeleteQueueResponse)

    async def delete_quick_connect(
        self,
        request: ConnectDeleteQuickConnectRequest,
    ) -> ConnectDeleteQuickConnectResponse:
        client = self._require_client()
        return await self._execute(client.delete_quick_connect, request, ConnectDeleteQuickConnectResponse)

    async def delete_routing_profile(
        self,
        request: ConnectDeleteRoutingProfileRequest,
    ) -> ConnectDeleteRoutingProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_routing_profile, request, ConnectDeleteRoutingProfileResponse)

    async def delete_rule(
        self,
        request: ConnectDeleteRuleRequest,
    ) -> ConnectDeleteRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_rule, request, ConnectDeleteRuleResponse)

    async def delete_security_profile(
        self,
        request: ConnectDeleteSecurityProfileRequest,
    ) -> ConnectDeleteSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_profile, request, ConnectDeleteSecurityProfileResponse)

    async def delete_session(
        self,
        request: ConnectDeleteSessionRequest,
    ) -> ConnectDeleteSessionResponse:
        client = self._require_client()
        return await self._execute(client.delete_session, request, ConnectDeleteSessionResponse)

    async def delete_task_template(
        self,
        request: ConnectDeleteTaskTemplateRequest,
    ) -> ConnectDeleteTaskTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_task_template, request, ConnectDeleteTaskTemplateResponse)

    async def delete_test_case(
        self,
        request: ConnectDeleteTestCaseRequest,
    ) -> ConnectDeleteTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_test_case, request, ConnectDeleteTestCaseResponse)

    async def delete_traffic_distribution_group(
        self,
        request: ConnectDeleteTrafficDistributionGroupRequest,
    ) -> ConnectDeleteTrafficDistributionGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_distribution_group, request, ConnectDeleteTrafficDistributionGroupResponse)

    async def delete_use_case(
        self,
        request: ConnectDeleteUseCaseRequest,
    ) -> ConnectDeleteUseCaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_use_case, request, ConnectDeleteUseCaseResponse)

    async def delete_user(
        self,
        request: ConnectDeleteUserRequest,
    ) -> ConnectDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, ConnectDeleteUserResponse)

    async def delete_user_hierarchy_group(
        self,
        request: ConnectDeleteUserHierarchyGroupRequest,
    ) -> ConnectDeleteUserHierarchyGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_hierarchy_group, request, ConnectDeleteUserHierarchyGroupResponse)

    async def delete_view(
        self,
        request: ConnectDeleteViewRequest,
    ) -> ConnectDeleteViewResponse:
        client = self._require_client()
        return await self._execute(client.delete_view, request, ConnectDeleteViewResponse)

    async def delete_view_version(
        self,
        request: ConnectDeleteViewVersionRequest,
    ) -> ConnectDeleteViewVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_view_version, request, ConnectDeleteViewVersionResponse)

    async def delete_vocabulary(
        self,
        request: ConnectDeleteVocabularyRequest,
    ) -> ConnectDeleteVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.delete_vocabulary, request, ConnectDeleteVocabularyResponse)

    async def delete_workspace(
        self,
        request: ConnectDeleteWorkspaceRequest,
    ) -> ConnectDeleteWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace, request, ConnectDeleteWorkspaceResponse)

    async def delete_workspace_media(
        self,
        request: ConnectDeleteWorkspaceMediaRequest,
    ) -> ConnectDeleteWorkspaceMediaResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_media, request, ConnectDeleteWorkspaceMediaResponse)

    async def delete_workspace_page(
        self,
        request: ConnectDeleteWorkspacePageRequest,
    ) -> ConnectDeleteWorkspacePageResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_page, request, ConnectDeleteWorkspacePageResponse)

    async def describe_agent_status(
        self,
        request: ConnectDescribeAgentStatusRequest,
    ) -> ConnectDescribeAgentStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_agent_status, request, ConnectDescribeAgentStatusResponse)

    async def describe_attached_files_configuration(
        self,
        request: ConnectDescribeAttachedFilesConfigurationRequest,
    ) -> ConnectDescribeAttachedFilesConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_attached_files_configuration, request, ConnectDescribeAttachedFilesConfigurationResponse)

    async def describe_authentication_profile(
        self,
        request: ConnectDescribeAuthenticationProfileRequest,
    ) -> ConnectDescribeAuthenticationProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_authentication_profile, request, ConnectDescribeAuthenticationProfileResponse)

    async def describe_contact(
        self,
        request: ConnectDescribeContactRequest,
    ) -> ConnectDescribeContactResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact, request, ConnectDescribeContactResponse)

    async def describe_contact_evaluation(
        self,
        request: ConnectDescribeContactEvaluationRequest,
    ) -> ConnectDescribeContactEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact_evaluation, request, ConnectDescribeContactEvaluationResponse)

    async def describe_contact_flow(
        self,
        request: ConnectDescribeContactFlowRequest,
    ) -> ConnectDescribeContactFlowResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact_flow, request, ConnectDescribeContactFlowResponse)

    async def describe_contact_flow_alias(
        self,
        request: ConnectDescribeContactFlowAliasRequest,
    ) -> ConnectDescribeContactFlowAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact_flow_alias, request, ConnectDescribeContactFlowAliasResponse)

    async def describe_contact_flow_module(
        self,
        request: ConnectDescribeContactFlowModuleRequest,
    ) -> ConnectDescribeContactFlowModuleResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact_flow_module, request, ConnectDescribeContactFlowModuleResponse)

    async def describe_contact_flow_module_alias(
        self,
        request: ConnectDescribeContactFlowModuleAliasRequest,
    ) -> ConnectDescribeContactFlowModuleAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_contact_flow_module_alias, request, ConnectDescribeContactFlowModuleAliasResponse)

    async def describe_data_table(
        self,
        request: ConnectDescribeDataTableRequest,
    ) -> ConnectDescribeDataTableResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_table, request, ConnectDescribeDataTableResponse)

    async def describe_data_table_attribute(
        self,
        request: ConnectDescribeDataTableAttributeRequest,
    ) -> ConnectDescribeDataTableAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_table_attribute, request, ConnectDescribeDataTableAttributeResponse)

    async def describe_email_address(
        self,
        request: ConnectDescribeEmailAddressRequest,
    ) -> ConnectDescribeEmailAddressResponse:
        client = self._require_client()
        return await self._execute(client.describe_email_address, request, ConnectDescribeEmailAddressResponse)

    async def describe_evaluation_form(
        self,
        request: ConnectDescribeEvaluationFormRequest,
    ) -> ConnectDescribeEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.describe_evaluation_form, request, ConnectDescribeEvaluationFormResponse)

    async def describe_extraction_definition(
        self,
        request: ConnectDescribeExtractionDefinitionRequest,
    ) -> ConnectDescribeExtractionDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_extraction_definition, request, ConnectDescribeExtractionDefinitionResponse)

    async def describe_hours_of_operation(
        self,
        request: ConnectDescribeHoursOfOperationRequest,
    ) -> ConnectDescribeHoursOfOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_hours_of_operation, request, ConnectDescribeHoursOfOperationResponse)

    async def describe_hours_of_operation_override(
        self,
        request: ConnectDescribeHoursOfOperationOverrideRequest,
    ) -> ConnectDescribeHoursOfOperationOverrideResponse:
        client = self._require_client()
        return await self._execute(client.describe_hours_of_operation_override, request, ConnectDescribeHoursOfOperationOverrideResponse)

    async def describe_instance(
        self,
        request: ConnectDescribeInstanceRequest,
    ) -> ConnectDescribeInstanceResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance, request, ConnectDescribeInstanceResponse)

    async def describe_instance_attribute(
        self,
        request: ConnectDescribeInstanceAttributeRequest,
    ) -> ConnectDescribeInstanceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_attribute, request, ConnectDescribeInstanceAttributeResponse)

    async def describe_instance_storage_config(
        self,
        request: ConnectDescribeInstanceStorageConfigRequest,
    ) -> ConnectDescribeInstanceStorageConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_storage_config, request, ConnectDescribeInstanceStorageConfigResponse)

    async def describe_metric(
        self,
        request: ConnectDescribeMetricRequest,
    ) -> ConnectDescribeMetricResponse:
        client = self._require_client()
        return await self._execute(client.describe_metric, request, ConnectDescribeMetricResponse)

    async def describe_notification(
        self,
        request: ConnectDescribeNotificationRequest,
    ) -> ConnectDescribeNotificationResponse:
        client = self._require_client()
        return await self._execute(client.describe_notification, request, ConnectDescribeNotificationResponse)

    async def describe_phone_number(
        self,
        request: ConnectDescribePhoneNumberRequest,
    ) -> ConnectDescribePhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.describe_phone_number, request, ConnectDescribePhoneNumberResponse)

    async def describe_predefined_attribute(
        self,
        request: ConnectDescribePredefinedAttributeRequest,
    ) -> ConnectDescribePredefinedAttributeResponse:
        client = self._require_client()
        return await self._execute(client.describe_predefined_attribute, request, ConnectDescribePredefinedAttributeResponse)

    async def describe_prompt(
        self,
        request: ConnectDescribePromptRequest,
    ) -> ConnectDescribePromptResponse:
        client = self._require_client()
        return await self._execute(client.describe_prompt, request, ConnectDescribePromptResponse)

    async def describe_queue(
        self,
        request: ConnectDescribeQueueRequest,
    ) -> ConnectDescribeQueueResponse:
        client = self._require_client()
        return await self._execute(client.describe_queue, request, ConnectDescribeQueueResponse)

    async def describe_quick_connect(
        self,
        request: ConnectDescribeQuickConnectRequest,
    ) -> ConnectDescribeQuickConnectResponse:
        client = self._require_client()
        return await self._execute(client.describe_quick_connect, request, ConnectDescribeQuickConnectResponse)

    async def describe_routing_profile(
        self,
        request: ConnectDescribeRoutingProfileRequest,
    ) -> ConnectDescribeRoutingProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_routing_profile, request, ConnectDescribeRoutingProfileResponse)

    async def describe_rule(
        self,
        request: ConnectDescribeRuleRequest,
    ) -> ConnectDescribeRuleResponse:
        client = self._require_client()
        return await self._execute(client.describe_rule, request, ConnectDescribeRuleResponse)

    async def describe_security_profile(
        self,
        request: ConnectDescribeSecurityProfileRequest,
    ) -> ConnectDescribeSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_profile, request, ConnectDescribeSecurityProfileResponse)

    async def describe_test_case(
        self,
        request: ConnectDescribeTestCaseRequest,
    ) -> ConnectDescribeTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_case, request, ConnectDescribeTestCaseResponse)

    async def describe_traffic_distribution_group(
        self,
        request: ConnectDescribeTrafficDistributionGroupRequest,
    ) -> ConnectDescribeTrafficDistributionGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_traffic_distribution_group, request, ConnectDescribeTrafficDistributionGroupResponse)

    async def describe_user(
        self,
        request: ConnectDescribeUserRequest,
    ) -> ConnectDescribeUserResponse:
        client = self._require_client()
        return await self._execute(client.describe_user, request, ConnectDescribeUserResponse)

    async def describe_user_hierarchy_group(
        self,
        request: ConnectDescribeUserHierarchyGroupRequest,
    ) -> ConnectDescribeUserHierarchyGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_hierarchy_group, request, ConnectDescribeUserHierarchyGroupResponse)

    async def describe_user_hierarchy_structure(
        self,
        request: ConnectDescribeUserHierarchyStructureRequest,
    ) -> ConnectDescribeUserHierarchyStructureResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_hierarchy_structure, request, ConnectDescribeUserHierarchyStructureResponse)

    async def describe_view(
        self,
        request: ConnectDescribeViewRequest,
    ) -> ConnectDescribeViewResponse:
        client = self._require_client()
        return await self._execute(client.describe_view, request, ConnectDescribeViewResponse)

    async def describe_vocabulary(
        self,
        request: ConnectDescribeVocabularyRequest,
    ) -> ConnectDescribeVocabularyResponse:
        client = self._require_client()
        return await self._execute(client.describe_vocabulary, request, ConnectDescribeVocabularyResponse)

    async def describe_workspace(
        self,
        request: ConnectDescribeWorkspaceRequest,
    ) -> ConnectDescribeWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace, request, ConnectDescribeWorkspaceResponse)

    async def disassociate_analytics_data_set(
        self,
        request: ConnectDisassociateAnalyticsDataSetRequest,
    ) -> ConnectDisassociateAnalyticsDataSetResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_analytics_data_set, request, ConnectDisassociateAnalyticsDataSetResponse)

    async def disassociate_approved_origin(
        self,
        request: ConnectDisassociateApprovedOriginRequest,
    ) -> ConnectDisassociateApprovedOriginResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_approved_origin, request, ConnectDisassociateApprovedOriginResponse)

    async def disassociate_bot(
        self,
        request: ConnectDisassociateBotRequest,
    ) -> ConnectDisassociateBotResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_bot, request, ConnectDisassociateBotResponse)

    async def disassociate_email_address_alias(
        self,
        request: ConnectDisassociateEmailAddressAliasRequest,
    ) -> ConnectDisassociateEmailAddressAliasResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_email_address_alias, request, ConnectDisassociateEmailAddressAliasResponse)

    async def disassociate_flow(
        self,
        request: ConnectDisassociateFlowRequest,
    ) -> ConnectDisassociateFlowResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_flow, request, ConnectDisassociateFlowResponse)

    async def disassociate_hours_of_operations(
        self,
        request: ConnectDisassociateHoursOfOperationsRequest,
    ) -> ConnectDisassociateHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_hours_of_operations, request, ConnectDisassociateHoursOfOperationsResponse)

    async def disassociate_instance_storage_config(
        self,
        request: ConnectDisassociateInstanceStorageConfigRequest,
    ) -> ConnectDisassociateInstanceStorageConfigResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_instance_storage_config, request, ConnectDisassociateInstanceStorageConfigResponse)

    async def disassociate_lambda_function(
        self,
        request: ConnectDisassociateLambdaFunctionRequest,
    ) -> ConnectDisassociateLambdaFunctionResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_lambda_function, request, ConnectDisassociateLambdaFunctionResponse)

    async def disassociate_lex_bot(
        self,
        request: ConnectDisassociateLexBotRequest,
    ) -> ConnectDisassociateLexBotResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_lex_bot, request, ConnectDisassociateLexBotResponse)

    async def disassociate_phone_number_contact_flow(
        self,
        request: ConnectDisassociatePhoneNumberContactFlowRequest,
    ) -> ConnectDisassociatePhoneNumberContactFlowResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_phone_number_contact_flow, request, ConnectDisassociatePhoneNumberContactFlowResponse)

    async def disassociate_queue_email_addresses(
        self,
        request: ConnectDisassociateQueueEmailAddressesRequest,
    ) -> ConnectDisassociateQueueEmailAddressesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_queue_email_addresses, request, ConnectDisassociateQueueEmailAddressesResponse)

    async def disassociate_queue_quick_connects(
        self,
        request: ConnectDisassociateQueueQuickConnectsRequest,
    ) -> ConnectDisassociateQueueQuickConnectsResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_queue_quick_connects, request, ConnectDisassociateQueueQuickConnectsResponse)

    async def disassociate_routing_profile_queues(
        self,
        request: ConnectDisassociateRoutingProfileQueuesRequest,
    ) -> ConnectDisassociateRoutingProfileQueuesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_routing_profile_queues, request, ConnectDisassociateRoutingProfileQueuesResponse)

    async def disassociate_security_key(
        self,
        request: ConnectDisassociateSecurityKeyRequest,
    ) -> ConnectDisassociateSecurityKeyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_security_key, request, ConnectDisassociateSecurityKeyResponse)

    async def disassociate_security_profiles(
        self,
        request: ConnectDisassociateSecurityProfilesRequest,
    ) -> ConnectDisassociateSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_security_profiles, request, ConnectDisassociateSecurityProfilesResponse)

    async def disassociate_traffic_distribution_group_user(
        self,
        request: ConnectDisassociateTrafficDistributionGroupUserRequest,
    ) -> ConnectDisassociateTrafficDistributionGroupUserResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_traffic_distribution_group_user, request, ConnectDisassociateTrafficDistributionGroupUserResponse)

    async def disassociate_user_proficiencies(
        self,
        request: ConnectDisassociateUserProficienciesRequest,
    ) -> ConnectDisassociateUserProficienciesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_user_proficiencies, request, ConnectDisassociateUserProficienciesResponse)

    async def disassociate_workspace(
        self,
        request: ConnectDisassociateWorkspaceRequest,
    ) -> ConnectDisassociateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_workspace, request, ConnectDisassociateWorkspaceResponse)

    async def dismiss_user_contact(
        self,
        request: ConnectDismissUserContactRequest,
    ) -> ConnectDismissUserContactResponse:
        client = self._require_client()
        return await self._execute(client.dismiss_user_contact, request, ConnectDismissUserContactResponse)

    async def evaluate_data_table_values(
        self,
        request: ConnectEvaluateDataTableValuesRequest,
    ) -> ConnectEvaluateDataTableValuesResponse:
        client = self._require_client()
        return await self._execute(client.evaluate_data_table_values, request, ConnectEvaluateDataTableValuesResponse)

    async def get_attached_file(
        self,
        request: ConnectGetAttachedFileRequest,
    ) -> ConnectGetAttachedFileResponse:
        client = self._require_client()
        return await self._execute(client.get_attached_file, request, ConnectGetAttachedFileResponse)

    async def get_contact_attributes(
        self,
        request: ConnectGetContactAttributesRequest,
    ) -> ConnectGetContactAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_contact_attributes, request, ConnectGetContactAttributesResponse)

    async def get_contact_metrics(
        self,
        request: ConnectGetContactMetricsRequest,
    ) -> ConnectGetContactMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_contact_metrics, request, ConnectGetContactMetricsResponse)

    async def get_cross_region_routing(
        self,
        request: ConnectGetCrossRegionRoutingRequest,
    ) -> ConnectGetCrossRegionRoutingResponse:
        client = self._require_client()
        return await self._execute(client.get_cross_region_routing, request, ConnectGetCrossRegionRoutingResponse)

    async def get_current_metric_data(
        self,
        request: ConnectGetCurrentMetricDataRequest,
    ) -> ConnectGetCurrentMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_current_metric_data, request, ConnectGetCurrentMetricDataResponse)

    async def get_current_user_data(
        self,
        request: ConnectGetCurrentUserDataRequest,
    ) -> ConnectGetCurrentUserDataResponse:
        client = self._require_client()
        return await self._execute(client.get_current_user_data, request, ConnectGetCurrentUserDataResponse)

    async def get_effective_hours_of_operations(
        self,
        request: ConnectGetEffectiveHoursOfOperationsRequest,
    ) -> ConnectGetEffectiveHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.get_effective_hours_of_operations, request, ConnectGetEffectiveHoursOfOperationsResponse)

    async def get_evaluation_form_validation(
        self,
        request: ConnectGetEvaluationFormValidationRequest,
    ) -> ConnectGetEvaluationFormValidationResponse:
        client = self._require_client()
        return await self._execute(client.get_evaluation_form_validation, request, ConnectGetEvaluationFormValidationResponse)

    async def get_federation_token(
        self,
        request: ConnectGetFederationTokenRequest,
    ) -> ConnectGetFederationTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_federation_token, request, ConnectGetFederationTokenResponse)

    async def get_flow_association(
        self,
        request: ConnectGetFlowAssociationRequest,
    ) -> ConnectGetFlowAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_flow_association, request, ConnectGetFlowAssociationResponse)

    async def get_metric_data(
        self,
        request: ConnectGetMetricDataRequest,
    ) -> ConnectGetMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_metric_data, request, ConnectGetMetricDataResponse)

    async def get_metric_data_paginated(
        self,
        request: ConnectGetMetricDataRequest,
    ) -> list[ConnectGetMetricDataResponse]:
        return await self._paginate('get_metric_data', request, ConnectGetMetricDataResponse)

    async def get_metric_data_v2(
        self,
        request: ConnectGetMetricDataV2Request,
    ) -> ConnectGetMetricDataV2Response:
        client = self._require_client()
        return await self._execute(client.get_metric_data_v2, request, ConnectGetMetricDataV2Response)

    async def get_prompt_file(
        self,
        request: ConnectGetPromptFileRequest,
    ) -> ConnectGetPromptFileResponse:
        client = self._require_client()
        return await self._execute(client.get_prompt_file, request, ConnectGetPromptFileResponse)

    async def get_task_template(
        self,
        request: ConnectGetTaskTemplateRequest,
    ) -> ConnectGetTaskTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_task_template, request, ConnectGetTaskTemplateResponse)

    async def get_test_case_execution_summary(
        self,
        request: ConnectGetTestCaseExecutionSummaryRequest,
    ) -> ConnectGetTestCaseExecutionSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_test_case_execution_summary, request, ConnectGetTestCaseExecutionSummaryResponse)

    async def get_traffic_distribution(
        self,
        request: ConnectGetTrafficDistributionRequest,
    ) -> ConnectGetTrafficDistributionResponse:
        client = self._require_client()
        return await self._execute(client.get_traffic_distribution, request, ConnectGetTrafficDistributionResponse)

    async def import_phone_number(
        self,
        request: ConnectImportPhoneNumberRequest,
    ) -> ConnectImportPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.import_phone_number, request, ConnectImportPhoneNumberResponse)

    async def import_workspace_media(
        self,
        request: ConnectImportWorkspaceMediaRequest,
    ) -> ConnectImportWorkspaceMediaResponse:
        client = self._require_client()
        return await self._execute(client.import_workspace_media, request, ConnectImportWorkspaceMediaResponse)

    async def list_agent_statuses(
        self,
        request: ConnectListAgentStatusesRequest,
    ) -> ConnectListAgentStatusesResponse:
        client = self._require_client()
        return await self._execute(client.list_agent_statuses, request, ConnectListAgentStatusesResponse)

    async def list_agent_statuses_paginated(
        self,
        request: ConnectListAgentStatusesRequest,
    ) -> list[ConnectListAgentStatusesResponse]:
        return await self._paginate('list_agent_statuses', request, ConnectListAgentStatusesResponse)

    async def list_analytics_data_associations(
        self,
        request: ConnectListAnalyticsDataAssociationsRequest,
    ) -> ConnectListAnalyticsDataAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_analytics_data_associations, request, ConnectListAnalyticsDataAssociationsResponse)

    async def list_analytics_data_lake_data_sets(
        self,
        request: ConnectListAnalyticsDataLakeDataSetsRequest,
    ) -> ConnectListAnalyticsDataLakeDataSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_analytics_data_lake_data_sets, request, ConnectListAnalyticsDataLakeDataSetsResponse)

    async def list_approved_origins(
        self,
        request: ConnectListApprovedOriginsRequest,
    ) -> ConnectListApprovedOriginsResponse:
        client = self._require_client()
        return await self._execute(client.list_approved_origins, request, ConnectListApprovedOriginsResponse)

    async def list_approved_origins_paginated(
        self,
        request: ConnectListApprovedOriginsRequest,
    ) -> list[ConnectListApprovedOriginsResponse]:
        return await self._paginate('list_approved_origins', request, ConnectListApprovedOriginsResponse)

    async def list_associated_contacts(
        self,
        request: ConnectListAssociatedContactsRequest,
    ) -> ConnectListAssociatedContactsResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_contacts, request, ConnectListAssociatedContactsResponse)

    async def list_attached_files_configurations(
        self,
        request: ConnectListAttachedFilesConfigurationsRequest,
    ) -> ConnectListAttachedFilesConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_attached_files_configurations, request, ConnectListAttachedFilesConfigurationsResponse)

    async def list_attached_files_configurations_paginated(
        self,
        request: ConnectListAttachedFilesConfigurationsRequest,
    ) -> list[ConnectListAttachedFilesConfigurationsResponse]:
        return await self._paginate('list_attached_files_configurations', request, ConnectListAttachedFilesConfigurationsResponse)

    async def list_authentication_profiles(
        self,
        request: ConnectListAuthenticationProfilesRequest,
    ) -> ConnectListAuthenticationProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_authentication_profiles, request, ConnectListAuthenticationProfilesResponse)

    async def list_authentication_profiles_paginated(
        self,
        request: ConnectListAuthenticationProfilesRequest,
    ) -> list[ConnectListAuthenticationProfilesResponse]:
        return await self._paginate('list_authentication_profiles', request, ConnectListAuthenticationProfilesResponse)

    async def list_bots(
        self,
        request: ConnectListBotsRequest,
    ) -> ConnectListBotsResponse:
        client = self._require_client()
        return await self._execute(client.list_bots, request, ConnectListBotsResponse)

    async def list_bots_paginated(
        self,
        request: ConnectListBotsRequest,
    ) -> list[ConnectListBotsResponse]:
        return await self._paginate('list_bots', request, ConnectListBotsResponse)

    async def list_child_hours_of_operations(
        self,
        request: ConnectListChildHoursOfOperationsRequest,
    ) -> ConnectListChildHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_child_hours_of_operations, request, ConnectListChildHoursOfOperationsResponse)

    async def list_child_hours_of_operations_paginated(
        self,
        request: ConnectListChildHoursOfOperationsRequest,
    ) -> list[ConnectListChildHoursOfOperationsResponse]:
        return await self._paginate('list_child_hours_of_operations', request, ConnectListChildHoursOfOperationsResponse)

    async def list_contact_evaluations(
        self,
        request: ConnectListContactEvaluationsRequest,
    ) -> ConnectListContactEvaluationsResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_evaluations, request, ConnectListContactEvaluationsResponse)

    async def list_contact_evaluations_paginated(
        self,
        request: ConnectListContactEvaluationsRequest,
    ) -> list[ConnectListContactEvaluationsResponse]:
        return await self._paginate('list_contact_evaluations', request, ConnectListContactEvaluationsResponse)

    async def list_contact_flow_aliases(
        self,
        request: ConnectListContactFlowAliasesRequest,
    ) -> ConnectListContactFlowAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flow_aliases, request, ConnectListContactFlowAliasesResponse)

    async def list_contact_flow_aliases_paginated(
        self,
        request: ConnectListContactFlowAliasesRequest,
    ) -> list[ConnectListContactFlowAliasesResponse]:
        return await self._paginate('list_contact_flow_aliases', request, ConnectListContactFlowAliasesResponse)

    async def list_contact_flow_module_aliases(
        self,
        request: ConnectListContactFlowModuleAliasesRequest,
    ) -> ConnectListContactFlowModuleAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flow_module_aliases, request, ConnectListContactFlowModuleAliasesResponse)

    async def list_contact_flow_module_aliases_paginated(
        self,
        request: ConnectListContactFlowModuleAliasesRequest,
    ) -> list[ConnectListContactFlowModuleAliasesResponse]:
        return await self._paginate('list_contact_flow_module_aliases', request, ConnectListContactFlowModuleAliasesResponse)

    async def list_contact_flow_module_versions(
        self,
        request: ConnectListContactFlowModuleVersionsRequest,
    ) -> ConnectListContactFlowModuleVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flow_module_versions, request, ConnectListContactFlowModuleVersionsResponse)

    async def list_contact_flow_module_versions_paginated(
        self,
        request: ConnectListContactFlowModuleVersionsRequest,
    ) -> list[ConnectListContactFlowModuleVersionsResponse]:
        return await self._paginate('list_contact_flow_module_versions', request, ConnectListContactFlowModuleVersionsResponse)

    async def list_contact_flow_modules(
        self,
        request: ConnectListContactFlowModulesRequest,
    ) -> ConnectListContactFlowModulesResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flow_modules, request, ConnectListContactFlowModulesResponse)

    async def list_contact_flow_modules_paginated(
        self,
        request: ConnectListContactFlowModulesRequest,
    ) -> list[ConnectListContactFlowModulesResponse]:
        return await self._paginate('list_contact_flow_modules', request, ConnectListContactFlowModulesResponse)

    async def list_contact_flow_versions(
        self,
        request: ConnectListContactFlowVersionsRequest,
    ) -> ConnectListContactFlowVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flow_versions, request, ConnectListContactFlowVersionsResponse)

    async def list_contact_flow_versions_paginated(
        self,
        request: ConnectListContactFlowVersionsRequest,
    ) -> list[ConnectListContactFlowVersionsResponse]:
        return await self._paginate('list_contact_flow_versions', request, ConnectListContactFlowVersionsResponse)

    async def list_contact_flows(
        self,
        request: ConnectListContactFlowsRequest,
    ) -> ConnectListContactFlowsResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_flows, request, ConnectListContactFlowsResponse)

    async def list_contact_flows_paginated(
        self,
        request: ConnectListContactFlowsRequest,
    ) -> list[ConnectListContactFlowsResponse]:
        return await self._paginate('list_contact_flows', request, ConnectListContactFlowsResponse)

    async def list_contact_references(
        self,
        request: ConnectListContactReferencesRequest,
    ) -> ConnectListContactReferencesResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_references, request, ConnectListContactReferencesResponse)

    async def list_contact_references_paginated(
        self,
        request: ConnectListContactReferencesRequest,
    ) -> list[ConnectListContactReferencesResponse]:
        return await self._paginate('list_contact_references', request, ConnectListContactReferencesResponse)

    async def list_data_table_attributes(
        self,
        request: ConnectListDataTableAttributesRequest,
    ) -> ConnectListDataTableAttributesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_table_attributes, request, ConnectListDataTableAttributesResponse)

    async def list_data_table_attributes_paginated(
        self,
        request: ConnectListDataTableAttributesRequest,
    ) -> list[ConnectListDataTableAttributesResponse]:
        return await self._paginate('list_data_table_attributes', request, ConnectListDataTableAttributesResponse)

    async def list_data_table_primary_values(
        self,
        request: ConnectListDataTablePrimaryValuesRequest,
    ) -> ConnectListDataTablePrimaryValuesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_table_primary_values, request, ConnectListDataTablePrimaryValuesResponse)

    async def list_data_table_primary_values_paginated(
        self,
        request: ConnectListDataTablePrimaryValuesRequest,
    ) -> list[ConnectListDataTablePrimaryValuesResponse]:
        return await self._paginate('list_data_table_primary_values', request, ConnectListDataTablePrimaryValuesResponse)

    async def list_data_table_values(
        self,
        request: ConnectListDataTableValuesRequest,
    ) -> ConnectListDataTableValuesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_table_values, request, ConnectListDataTableValuesResponse)

    async def list_data_table_values_paginated(
        self,
        request: ConnectListDataTableValuesRequest,
    ) -> list[ConnectListDataTableValuesResponse]:
        return await self._paginate('list_data_table_values', request, ConnectListDataTableValuesResponse)

    async def list_data_tables(
        self,
        request: ConnectListDataTablesRequest,
    ) -> ConnectListDataTablesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_tables, request, ConnectListDataTablesResponse)

    async def list_data_tables_paginated(
        self,
        request: ConnectListDataTablesRequest,
    ) -> list[ConnectListDataTablesResponse]:
        return await self._paginate('list_data_tables', request, ConnectListDataTablesResponse)

    async def list_default_vocabularies(
        self,
        request: ConnectListDefaultVocabulariesRequest,
    ) -> ConnectListDefaultVocabulariesResponse:
        client = self._require_client()
        return await self._execute(client.list_default_vocabularies, request, ConnectListDefaultVocabulariesResponse)

    async def list_default_vocabularies_paginated(
        self,
        request: ConnectListDefaultVocabulariesRequest,
    ) -> list[ConnectListDefaultVocabulariesResponse]:
        return await self._paginate('list_default_vocabularies', request, ConnectListDefaultVocabulariesResponse)

    async def list_entity_security_profiles(
        self,
        request: ConnectListEntitySecurityProfilesRequest,
    ) -> ConnectListEntitySecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_entity_security_profiles, request, ConnectListEntitySecurityProfilesResponse)

    async def list_entity_security_profiles_paginated(
        self,
        request: ConnectListEntitySecurityProfilesRequest,
    ) -> list[ConnectListEntitySecurityProfilesResponse]:
        return await self._paginate('list_entity_security_profiles', request, ConnectListEntitySecurityProfilesResponse)

    async def list_evaluation_form_ai_versions(
        self,
        request: ConnectListEvaluationFormAIVersionsRequest,
    ) -> ConnectListEvaluationFormAIVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_evaluation_form_ai_versions, request, ConnectListEvaluationFormAIVersionsResponse)

    async def list_evaluation_form_ai_versions_paginated(
        self,
        request: ConnectListEvaluationFormAIVersionsRequest,
    ) -> list[ConnectListEvaluationFormAIVersionsResponse]:
        return await self._paginate('list_evaluation_form_ai_versions', request, ConnectListEvaluationFormAIVersionsResponse)

    async def list_evaluation_form_versions(
        self,
        request: ConnectListEvaluationFormVersionsRequest,
    ) -> ConnectListEvaluationFormVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_evaluation_form_versions, request, ConnectListEvaluationFormVersionsResponse)

    async def list_evaluation_form_versions_paginated(
        self,
        request: ConnectListEvaluationFormVersionsRequest,
    ) -> list[ConnectListEvaluationFormVersionsResponse]:
        return await self._paginate('list_evaluation_form_versions', request, ConnectListEvaluationFormVersionsResponse)

    async def list_evaluation_forms(
        self,
        request: ConnectListEvaluationFormsRequest,
    ) -> ConnectListEvaluationFormsResponse:
        client = self._require_client()
        return await self._execute(client.list_evaluation_forms, request, ConnectListEvaluationFormsResponse)

    async def list_evaluation_forms_paginated(
        self,
        request: ConnectListEvaluationFormsRequest,
    ) -> list[ConnectListEvaluationFormsResponse]:
        return await self._paginate('list_evaluation_forms', request, ConnectListEvaluationFormsResponse)

    async def list_extraction_definitions(
        self,
        request: ConnectListExtractionDefinitionsRequest,
    ) -> ConnectListExtractionDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_extraction_definitions, request, ConnectListExtractionDefinitionsResponse)

    async def list_extraction_definitions_paginated(
        self,
        request: ConnectListExtractionDefinitionsRequest,
    ) -> list[ConnectListExtractionDefinitionsResponse]:
        return await self._paginate('list_extraction_definitions', request, ConnectListExtractionDefinitionsResponse)

    async def list_flow_associations(
        self,
        request: ConnectListFlowAssociationsRequest,
    ) -> ConnectListFlowAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_flow_associations, request, ConnectListFlowAssociationsResponse)

    async def list_flow_associations_paginated(
        self,
        request: ConnectListFlowAssociationsRequest,
    ) -> list[ConnectListFlowAssociationsResponse]:
        return await self._paginate('list_flow_associations', request, ConnectListFlowAssociationsResponse)

    async def list_hours_of_operation_overrides(
        self,
        request: ConnectListHoursOfOperationOverridesRequest,
    ) -> ConnectListHoursOfOperationOverridesResponse:
        client = self._require_client()
        return await self._execute(client.list_hours_of_operation_overrides, request, ConnectListHoursOfOperationOverridesResponse)

    async def list_hours_of_operation_overrides_paginated(
        self,
        request: ConnectListHoursOfOperationOverridesRequest,
    ) -> list[ConnectListHoursOfOperationOverridesResponse]:
        return await self._paginate('list_hours_of_operation_overrides', request, ConnectListHoursOfOperationOverridesResponse)

    async def list_hours_of_operations(
        self,
        request: ConnectListHoursOfOperationsRequest,
    ) -> ConnectListHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_hours_of_operations, request, ConnectListHoursOfOperationsResponse)

    async def list_hours_of_operations_paginated(
        self,
        request: ConnectListHoursOfOperationsRequest,
    ) -> list[ConnectListHoursOfOperationsResponse]:
        return await self._paginate('list_hours_of_operations', request, ConnectListHoursOfOperationsResponse)

    async def list_instance_attributes(
        self,
        request: ConnectListInstanceAttributesRequest,
    ) -> ConnectListInstanceAttributesResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_attributes, request, ConnectListInstanceAttributesResponse)

    async def list_instance_attributes_paginated(
        self,
        request: ConnectListInstanceAttributesRequest,
    ) -> list[ConnectListInstanceAttributesResponse]:
        return await self._paginate('list_instance_attributes', request, ConnectListInstanceAttributesResponse)

    async def list_instance_storage_configs(
        self,
        request: ConnectListInstanceStorageConfigsRequest,
    ) -> ConnectListInstanceStorageConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_storage_configs, request, ConnectListInstanceStorageConfigsResponse)

    async def list_instance_storage_configs_paginated(
        self,
        request: ConnectListInstanceStorageConfigsRequest,
    ) -> list[ConnectListInstanceStorageConfigsResponse]:
        return await self._paginate('list_instance_storage_configs', request, ConnectListInstanceStorageConfigsResponse)

    async def list_instances(
        self,
        request: ConnectListInstancesRequest | None = None,
    ) -> ConnectListInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_instances, request, ConnectListInstancesResponse)

    async def list_instances_paginated(
        self,
        request: ConnectListInstancesRequest | None = None,
    ) -> list[ConnectListInstancesResponse]:
        return await self._paginate('list_instances', request, ConnectListInstancesResponse)

    async def list_integration_associations(
        self,
        request: ConnectListIntegrationAssociationsRequest,
    ) -> ConnectListIntegrationAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_integration_associations, request, ConnectListIntegrationAssociationsResponse)

    async def list_integration_associations_paginated(
        self,
        request: ConnectListIntegrationAssociationsRequest,
    ) -> list[ConnectListIntegrationAssociationsResponse]:
        return await self._paginate('list_integration_associations', request, ConnectListIntegrationAssociationsResponse)

    async def list_lambda_functions(
        self,
        request: ConnectListLambdaFunctionsRequest,
    ) -> ConnectListLambdaFunctionsResponse:
        client = self._require_client()
        return await self._execute(client.list_lambda_functions, request, ConnectListLambdaFunctionsResponse)

    async def list_lambda_functions_paginated(
        self,
        request: ConnectListLambdaFunctionsRequest,
    ) -> list[ConnectListLambdaFunctionsResponse]:
        return await self._paginate('list_lambda_functions', request, ConnectListLambdaFunctionsResponse)

    async def list_lex_bots(
        self,
        request: ConnectListLexBotsRequest,
    ) -> ConnectListLexBotsResponse:
        client = self._require_client()
        return await self._execute(client.list_lex_bots, request, ConnectListLexBotsResponse)

    async def list_lex_bots_paginated(
        self,
        request: ConnectListLexBotsRequest,
    ) -> list[ConnectListLexBotsResponse]:
        return await self._paginate('list_lex_bots', request, ConnectListLexBotsResponse)

    async def list_metrics(
        self,
        request: ConnectListMetricsRequest,
    ) -> ConnectListMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_metrics, request, ConnectListMetricsResponse)

    async def list_metrics_paginated(
        self,
        request: ConnectListMetricsRequest,
    ) -> list[ConnectListMetricsResponse]:
        return await self._paginate('list_metrics', request, ConnectListMetricsResponse)

    async def list_notifications(
        self,
        request: ConnectListNotificationsRequest,
    ) -> ConnectListNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.list_notifications, request, ConnectListNotificationsResponse)

    async def list_phone_numbers(
        self,
        request: ConnectListPhoneNumbersRequest,
    ) -> ConnectListPhoneNumbersResponse:
        client = self._require_client()
        return await self._execute(client.list_phone_numbers, request, ConnectListPhoneNumbersResponse)

    async def list_phone_numbers_paginated(
        self,
        request: ConnectListPhoneNumbersRequest,
    ) -> list[ConnectListPhoneNumbersResponse]:
        return await self._paginate('list_phone_numbers', request, ConnectListPhoneNumbersResponse)

    async def list_phone_numbers_v2(
        self,
        request: ConnectListPhoneNumbersV2Request | None = None,
    ) -> ConnectListPhoneNumbersV2Response:
        client = self._require_client()
        return await self._execute(client.list_phone_numbers_v2, request, ConnectListPhoneNumbersV2Response)

    async def list_phone_numbers_v2_paginated(
        self,
        request: ConnectListPhoneNumbersV2Request | None = None,
    ) -> list[ConnectListPhoneNumbersV2Response]:
        return await self._paginate('list_phone_numbers_v2', request, ConnectListPhoneNumbersV2Response)

    async def list_predefined_attributes(
        self,
        request: ConnectListPredefinedAttributesRequest,
    ) -> ConnectListPredefinedAttributesResponse:
        client = self._require_client()
        return await self._execute(client.list_predefined_attributes, request, ConnectListPredefinedAttributesResponse)

    async def list_predefined_attributes_paginated(
        self,
        request: ConnectListPredefinedAttributesRequest,
    ) -> list[ConnectListPredefinedAttributesResponse]:
        return await self._paginate('list_predefined_attributes', request, ConnectListPredefinedAttributesResponse)

    async def list_prompts(
        self,
        request: ConnectListPromptsRequest,
    ) -> ConnectListPromptsResponse:
        client = self._require_client()
        return await self._execute(client.list_prompts, request, ConnectListPromptsResponse)

    async def list_prompts_paginated(
        self,
        request: ConnectListPromptsRequest,
    ) -> list[ConnectListPromptsResponse]:
        return await self._paginate('list_prompts', request, ConnectListPromptsResponse)

    async def list_queue_email_addresses(
        self,
        request: ConnectListQueueEmailAddressesRequest,
    ) -> ConnectListQueueEmailAddressesResponse:
        client = self._require_client()
        return await self._execute(client.list_queue_email_addresses, request, ConnectListQueueEmailAddressesResponse)

    async def list_queue_quick_connects(
        self,
        request: ConnectListQueueQuickConnectsRequest,
    ) -> ConnectListQueueQuickConnectsResponse:
        client = self._require_client()
        return await self._execute(client.list_queue_quick_connects, request, ConnectListQueueQuickConnectsResponse)

    async def list_queue_quick_connects_paginated(
        self,
        request: ConnectListQueueQuickConnectsRequest,
    ) -> list[ConnectListQueueQuickConnectsResponse]:
        return await self._paginate('list_queue_quick_connects', request, ConnectListQueueQuickConnectsResponse)

    async def list_queues(
        self,
        request: ConnectListQueuesRequest,
    ) -> ConnectListQueuesResponse:
        client = self._require_client()
        return await self._execute(client.list_queues, request, ConnectListQueuesResponse)

    async def list_queues_paginated(
        self,
        request: ConnectListQueuesRequest,
    ) -> list[ConnectListQueuesResponse]:
        return await self._paginate('list_queues', request, ConnectListQueuesResponse)

    async def list_quick_connects(
        self,
        request: ConnectListQuickConnectsRequest,
    ) -> ConnectListQuickConnectsResponse:
        client = self._require_client()
        return await self._execute(client.list_quick_connects, request, ConnectListQuickConnectsResponse)

    async def list_quick_connects_paginated(
        self,
        request: ConnectListQuickConnectsRequest,
    ) -> list[ConnectListQuickConnectsResponse]:
        return await self._paginate('list_quick_connects', request, ConnectListQuickConnectsResponse)

    async def list_realtime_contact_analysis_segments_v2(
        self,
        request: ConnectListRealtimeContactAnalysisSegmentsV2Request,
    ) -> ConnectListRealtimeContactAnalysisSegmentsV2Response:
        client = self._require_client()
        return await self._execute(client.list_realtime_contact_analysis_segments_v2, request, ConnectListRealtimeContactAnalysisSegmentsV2Response)

    async def list_replication_findings(
        self,
        request: ConnectListReplicationFindingsRequest,
    ) -> ConnectListReplicationFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_replication_findings, request, ConnectListReplicationFindingsResponse)

    async def list_replication_findings_paginated(
        self,
        request: ConnectListReplicationFindingsRequest,
    ) -> list[ConnectListReplicationFindingsResponse]:
        return await self._paginate('list_replication_findings', request, ConnectListReplicationFindingsResponse)

    async def list_routing_profile_manual_assignment_queues(
        self,
        request: ConnectListRoutingProfileManualAssignmentQueuesRequest,
    ) -> ConnectListRoutingProfileManualAssignmentQueuesResponse:
        client = self._require_client()
        return await self._execute(client.list_routing_profile_manual_assignment_queues, request, ConnectListRoutingProfileManualAssignmentQueuesResponse)

    async def list_routing_profile_manual_assignment_queues_paginated(
        self,
        request: ConnectListRoutingProfileManualAssignmentQueuesRequest,
    ) -> list[ConnectListRoutingProfileManualAssignmentQueuesResponse]:
        return await self._paginate('list_routing_profile_manual_assignment_queues', request, ConnectListRoutingProfileManualAssignmentQueuesResponse)

    async def list_routing_profile_queues(
        self,
        request: ConnectListRoutingProfileQueuesRequest,
    ) -> ConnectListRoutingProfileQueuesResponse:
        client = self._require_client()
        return await self._execute(client.list_routing_profile_queues, request, ConnectListRoutingProfileQueuesResponse)

    async def list_routing_profile_queues_paginated(
        self,
        request: ConnectListRoutingProfileQueuesRequest,
    ) -> list[ConnectListRoutingProfileQueuesResponse]:
        return await self._paginate('list_routing_profile_queues', request, ConnectListRoutingProfileQueuesResponse)

    async def list_routing_profiles(
        self,
        request: ConnectListRoutingProfilesRequest,
    ) -> ConnectListRoutingProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_routing_profiles, request, ConnectListRoutingProfilesResponse)

    async def list_routing_profiles_paginated(
        self,
        request: ConnectListRoutingProfilesRequest,
    ) -> list[ConnectListRoutingProfilesResponse]:
        return await self._paginate('list_routing_profiles', request, ConnectListRoutingProfilesResponse)

    async def list_rules(
        self,
        request: ConnectListRulesRequest,
    ) -> ConnectListRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_rules, request, ConnectListRulesResponse)

    async def list_rules_paginated(
        self,
        request: ConnectListRulesRequest,
    ) -> list[ConnectListRulesResponse]:
        return await self._paginate('list_rules', request, ConnectListRulesResponse)

    async def list_security_keys(
        self,
        request: ConnectListSecurityKeysRequest,
    ) -> ConnectListSecurityKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_security_keys, request, ConnectListSecurityKeysResponse)

    async def list_security_keys_paginated(
        self,
        request: ConnectListSecurityKeysRequest,
    ) -> list[ConnectListSecurityKeysResponse]:
        return await self._paginate('list_security_keys', request, ConnectListSecurityKeysResponse)

    async def list_security_profile_ai_agents(
        self,
        request: ConnectListSecurityProfileAIAgentsRequest,
    ) -> ConnectListSecurityProfileAIAgentsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profile_ai_agents, request, ConnectListSecurityProfileAIAgentsResponse)

    async def list_security_profile_ai_agents_paginated(
        self,
        request: ConnectListSecurityProfileAIAgentsRequest,
    ) -> list[ConnectListSecurityProfileAIAgentsResponse]:
        return await self._paginate('list_security_profile_ai_agents', request, ConnectListSecurityProfileAIAgentsResponse)

    async def list_security_profile_applications(
        self,
        request: ConnectListSecurityProfileApplicationsRequest,
    ) -> ConnectListSecurityProfileApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profile_applications, request, ConnectListSecurityProfileApplicationsResponse)

    async def list_security_profile_applications_paginated(
        self,
        request: ConnectListSecurityProfileApplicationsRequest,
    ) -> list[ConnectListSecurityProfileApplicationsResponse]:
        return await self._paginate('list_security_profile_applications', request, ConnectListSecurityProfileApplicationsResponse)

    async def list_security_profile_flow_modules(
        self,
        request: ConnectListSecurityProfileFlowModulesRequest,
    ) -> ConnectListSecurityProfileFlowModulesResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profile_flow_modules, request, ConnectListSecurityProfileFlowModulesResponse)

    async def list_security_profile_flow_modules_paginated(
        self,
        request: ConnectListSecurityProfileFlowModulesRequest,
    ) -> list[ConnectListSecurityProfileFlowModulesResponse]:
        return await self._paginate('list_security_profile_flow_modules', request, ConnectListSecurityProfileFlowModulesResponse)

    async def list_security_profile_permissions(
        self,
        request: ConnectListSecurityProfilePermissionsRequest,
    ) -> ConnectListSecurityProfilePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profile_permissions, request, ConnectListSecurityProfilePermissionsResponse)

    async def list_security_profile_permissions_paginated(
        self,
        request: ConnectListSecurityProfilePermissionsRequest,
    ) -> list[ConnectListSecurityProfilePermissionsResponse]:
        return await self._paginate('list_security_profile_permissions', request, ConnectListSecurityProfilePermissionsResponse)

    async def list_security_profiles(
        self,
        request: ConnectListSecurityProfilesRequest,
    ) -> ConnectListSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profiles, request, ConnectListSecurityProfilesResponse)

    async def list_security_profiles_paginated(
        self,
        request: ConnectListSecurityProfilesRequest,
    ) -> list[ConnectListSecurityProfilesResponse]:
        return await self._paginate('list_security_profiles', request, ConnectListSecurityProfilesResponse)

    async def list_tags_for_resource(
        self,
        request: ConnectListTagsForResourceRequest,
    ) -> ConnectListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ConnectListTagsForResourceResponse)

    async def list_task_templates(
        self,
        request: ConnectListTaskTemplatesRequest,
    ) -> ConnectListTaskTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_task_templates, request, ConnectListTaskTemplatesResponse)

    async def list_task_templates_paginated(
        self,
        request: ConnectListTaskTemplatesRequest,
    ) -> list[ConnectListTaskTemplatesResponse]:
        return await self._paginate('list_task_templates', request, ConnectListTaskTemplatesResponse)

    async def list_test_case_execution_records(
        self,
        request: ConnectListTestCaseExecutionRecordsRequest,
    ) -> ConnectListTestCaseExecutionRecordsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_case_execution_records, request, ConnectListTestCaseExecutionRecordsResponse)

    async def list_test_case_executions(
        self,
        request: ConnectListTestCaseExecutionsRequest,
    ) -> ConnectListTestCaseExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_case_executions, request, ConnectListTestCaseExecutionsResponse)

    async def list_test_cases(
        self,
        request: ConnectListTestCasesRequest,
    ) -> ConnectListTestCasesResponse:
        client = self._require_client()
        return await self._execute(client.list_test_cases, request, ConnectListTestCasesResponse)

    async def list_test_cases_paginated(
        self,
        request: ConnectListTestCasesRequest,
    ) -> list[ConnectListTestCasesResponse]:
        return await self._paginate('list_test_cases', request, ConnectListTestCasesResponse)

    async def list_traffic_distribution_group_users(
        self,
        request: ConnectListTrafficDistributionGroupUsersRequest,
    ) -> ConnectListTrafficDistributionGroupUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_distribution_group_users, request, ConnectListTrafficDistributionGroupUsersResponse)

    async def list_traffic_distribution_group_users_paginated(
        self,
        request: ConnectListTrafficDistributionGroupUsersRequest,
    ) -> list[ConnectListTrafficDistributionGroupUsersResponse]:
        return await self._paginate('list_traffic_distribution_group_users', request, ConnectListTrafficDistributionGroupUsersResponse)

    async def list_traffic_distribution_groups(
        self,
        request: ConnectListTrafficDistributionGroupsRequest | None = None,
    ) -> ConnectListTrafficDistributionGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_distribution_groups, request, ConnectListTrafficDistributionGroupsResponse)

    async def list_traffic_distribution_groups_paginated(
        self,
        request: ConnectListTrafficDistributionGroupsRequest | None = None,
    ) -> list[ConnectListTrafficDistributionGroupsResponse]:
        return await self._paginate('list_traffic_distribution_groups', request, ConnectListTrafficDistributionGroupsResponse)

    async def list_use_cases(
        self,
        request: ConnectListUseCasesRequest,
    ) -> ConnectListUseCasesResponse:
        client = self._require_client()
        return await self._execute(client.list_use_cases, request, ConnectListUseCasesResponse)

    async def list_use_cases_paginated(
        self,
        request: ConnectListUseCasesRequest,
    ) -> list[ConnectListUseCasesResponse]:
        return await self._paginate('list_use_cases', request, ConnectListUseCasesResponse)

    async def list_user_hierarchy_groups(
        self,
        request: ConnectListUserHierarchyGroupsRequest,
    ) -> ConnectListUserHierarchyGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_hierarchy_groups, request, ConnectListUserHierarchyGroupsResponse)

    async def list_user_hierarchy_groups_paginated(
        self,
        request: ConnectListUserHierarchyGroupsRequest,
    ) -> list[ConnectListUserHierarchyGroupsResponse]:
        return await self._paginate('list_user_hierarchy_groups', request, ConnectListUserHierarchyGroupsResponse)

    async def list_user_notifications(
        self,
        request: ConnectListUserNotificationsRequest,
    ) -> ConnectListUserNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_notifications, request, ConnectListUserNotificationsResponse)

    async def list_user_proficiencies(
        self,
        request: ConnectListUserProficienciesRequest,
    ) -> ConnectListUserProficienciesResponse:
        client = self._require_client()
        return await self._execute(client.list_user_proficiencies, request, ConnectListUserProficienciesResponse)

    async def list_user_proficiencies_paginated(
        self,
        request: ConnectListUserProficienciesRequest,
    ) -> list[ConnectListUserProficienciesResponse]:
        return await self._paginate('list_user_proficiencies', request, ConnectListUserProficienciesResponse)

    async def list_users(
        self,
        request: ConnectListUsersRequest,
    ) -> ConnectListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, ConnectListUsersResponse)

    async def list_users_paginated(
        self,
        request: ConnectListUsersRequest,
    ) -> list[ConnectListUsersResponse]:
        return await self._paginate('list_users', request, ConnectListUsersResponse)

    async def list_view_versions(
        self,
        request: ConnectListViewVersionsRequest,
    ) -> ConnectListViewVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_view_versions, request, ConnectListViewVersionsResponse)

    async def list_view_versions_paginated(
        self,
        request: ConnectListViewVersionsRequest,
    ) -> list[ConnectListViewVersionsResponse]:
        return await self._paginate('list_view_versions', request, ConnectListViewVersionsResponse)

    async def list_views(
        self,
        request: ConnectListViewsRequest,
    ) -> ConnectListViewsResponse:
        client = self._require_client()
        return await self._execute(client.list_views, request, ConnectListViewsResponse)

    async def list_views_paginated(
        self,
        request: ConnectListViewsRequest,
    ) -> list[ConnectListViewsResponse]:
        return await self._paginate('list_views', request, ConnectListViewsResponse)

    async def list_workspace_media(
        self,
        request: ConnectListWorkspaceMediaRequest,
    ) -> ConnectListWorkspaceMediaResponse:
        client = self._require_client()
        return await self._execute(client.list_workspace_media, request, ConnectListWorkspaceMediaResponse)

    async def list_workspace_pages(
        self,
        request: ConnectListWorkspacePagesRequest,
    ) -> ConnectListWorkspacePagesResponse:
        client = self._require_client()
        return await self._execute(client.list_workspace_pages, request, ConnectListWorkspacePagesResponse)

    async def list_workspace_pages_paginated(
        self,
        request: ConnectListWorkspacePagesRequest,
    ) -> list[ConnectListWorkspacePagesResponse]:
        return await self._paginate('list_workspace_pages', request, ConnectListWorkspacePagesResponse)

    async def list_workspaces(
        self,
        request: ConnectListWorkspacesRequest,
    ) -> ConnectListWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.list_workspaces, request, ConnectListWorkspacesResponse)

    async def list_workspaces_paginated(
        self,
        request: ConnectListWorkspacesRequest,
    ) -> list[ConnectListWorkspacesResponse]:
        return await self._paginate('list_workspaces', request, ConnectListWorkspacesResponse)

    async def monitor_contact(
        self,
        request: ConnectMonitorContactRequest,
    ) -> ConnectMonitorContactResponse:
        client = self._require_client()
        return await self._execute(client.monitor_contact, request, ConnectMonitorContactResponse)

    async def pause_contact(
        self,
        request: ConnectPauseContactRequest,
    ) -> ConnectPauseContactResponse:
        client = self._require_client()
        return await self._execute(client.pause_contact, request, ConnectPauseContactResponse)

    async def put_user_status(
        self,
        request: ConnectPutUserStatusRequest,
    ) -> ConnectPutUserStatusResponse:
        client = self._require_client()
        return await self._execute(client.put_user_status, request, ConnectPutUserStatusResponse)

    async def release_phone_number(
        self,
        request: ConnectReleasePhoneNumberRequest,
    ) -> ConnectReleasePhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.release_phone_number, request, ConnectReleasePhoneNumberResponse)

    async def replicate_instance(
        self,
        request: ConnectReplicateInstanceRequest,
    ) -> ConnectReplicateInstanceResponse:
        client = self._require_client()
        return await self._execute(client.replicate_instance, request, ConnectReplicateInstanceResponse)

    async def resume_contact(
        self,
        request: ConnectResumeContactRequest,
    ) -> ConnectResumeContactResponse:
        client = self._require_client()
        return await self._execute(client.resume_contact, request, ConnectResumeContactResponse)

    async def resume_contact_recording(
        self,
        request: ConnectResumeContactRecordingRequest,
    ) -> ConnectResumeContactRecordingResponse:
        client = self._require_client()
        return await self._execute(client.resume_contact_recording, request, ConnectResumeContactRecordingResponse)

    async def search_agent_statuses(
        self,
        request: ConnectSearchAgentStatusesRequest,
    ) -> ConnectSearchAgentStatusesResponse:
        client = self._require_client()
        return await self._execute(client.search_agent_statuses, request, ConnectSearchAgentStatusesResponse)

    async def search_agent_statuses_paginated(
        self,
        request: ConnectSearchAgentStatusesRequest,
    ) -> list[ConnectSearchAgentStatusesResponse]:
        return await self._paginate('search_agent_statuses', request, ConnectSearchAgentStatusesResponse)

    async def search_available_phone_numbers(
        self,
        request: ConnectSearchAvailablePhoneNumbersRequest,
    ) -> ConnectSearchAvailablePhoneNumbersResponse:
        client = self._require_client()
        return await self._execute(client.search_available_phone_numbers, request, ConnectSearchAvailablePhoneNumbersResponse)

    async def search_available_phone_numbers_paginated(
        self,
        request: ConnectSearchAvailablePhoneNumbersRequest,
    ) -> list[ConnectSearchAvailablePhoneNumbersResponse]:
        return await self._paginate('search_available_phone_numbers', request, ConnectSearchAvailablePhoneNumbersResponse)

    async def search_contact_evaluations(
        self,
        request: ConnectSearchContactEvaluationsRequest,
    ) -> ConnectSearchContactEvaluationsResponse:
        client = self._require_client()
        return await self._execute(client.search_contact_evaluations, request, ConnectSearchContactEvaluationsResponse)

    async def search_contact_flow_modules(
        self,
        request: ConnectSearchContactFlowModulesRequest,
    ) -> ConnectSearchContactFlowModulesResponse:
        client = self._require_client()
        return await self._execute(client.search_contact_flow_modules, request, ConnectSearchContactFlowModulesResponse)

    async def search_contact_flow_modules_paginated(
        self,
        request: ConnectSearchContactFlowModulesRequest,
    ) -> list[ConnectSearchContactFlowModulesResponse]:
        return await self._paginate('search_contact_flow_modules', request, ConnectSearchContactFlowModulesResponse)

    async def search_contact_flows(
        self,
        request: ConnectSearchContactFlowsRequest,
    ) -> ConnectSearchContactFlowsResponse:
        client = self._require_client()
        return await self._execute(client.search_contact_flows, request, ConnectSearchContactFlowsResponse)

    async def search_contact_flows_paginated(
        self,
        request: ConnectSearchContactFlowsRequest,
    ) -> list[ConnectSearchContactFlowsResponse]:
        return await self._paginate('search_contact_flows', request, ConnectSearchContactFlowsResponse)

    async def search_contacts(
        self,
        request: ConnectSearchContactsRequest,
    ) -> ConnectSearchContactsResponse:
        client = self._require_client()
        return await self._execute(client.search_contacts, request, ConnectSearchContactsResponse)

    async def search_contacts_paginated(
        self,
        request: ConnectSearchContactsRequest,
    ) -> list[ConnectSearchContactsResponse]:
        return await self._paginate('search_contacts', request, ConnectSearchContactsResponse)

    async def search_data_tables(
        self,
        request: ConnectSearchDataTablesRequest,
    ) -> ConnectSearchDataTablesResponse:
        client = self._require_client()
        return await self._execute(client.search_data_tables, request, ConnectSearchDataTablesResponse)

    async def search_data_tables_paginated(
        self,
        request: ConnectSearchDataTablesRequest,
    ) -> list[ConnectSearchDataTablesResponse]:
        return await self._paginate('search_data_tables', request, ConnectSearchDataTablesResponse)

    async def search_email_addresses(
        self,
        request: ConnectSearchEmailAddressesRequest,
    ) -> ConnectSearchEmailAddressesResponse:
        client = self._require_client()
        return await self._execute(client.search_email_addresses, request, ConnectSearchEmailAddressesResponse)

    async def search_evaluation_forms(
        self,
        request: ConnectSearchEvaluationFormsRequest,
    ) -> ConnectSearchEvaluationFormsResponse:
        client = self._require_client()
        return await self._execute(client.search_evaluation_forms, request, ConnectSearchEvaluationFormsResponse)

    async def search_hours_of_operation_overrides(
        self,
        request: ConnectSearchHoursOfOperationOverridesRequest,
    ) -> ConnectSearchHoursOfOperationOverridesResponse:
        client = self._require_client()
        return await self._execute(client.search_hours_of_operation_overrides, request, ConnectSearchHoursOfOperationOverridesResponse)

    async def search_hours_of_operation_overrides_paginated(
        self,
        request: ConnectSearchHoursOfOperationOverridesRequest,
    ) -> list[ConnectSearchHoursOfOperationOverridesResponse]:
        return await self._paginate('search_hours_of_operation_overrides', request, ConnectSearchHoursOfOperationOverridesResponse)

    async def search_hours_of_operations(
        self,
        request: ConnectSearchHoursOfOperationsRequest,
    ) -> ConnectSearchHoursOfOperationsResponse:
        client = self._require_client()
        return await self._execute(client.search_hours_of_operations, request, ConnectSearchHoursOfOperationsResponse)

    async def search_hours_of_operations_paginated(
        self,
        request: ConnectSearchHoursOfOperationsRequest,
    ) -> list[ConnectSearchHoursOfOperationsResponse]:
        return await self._paginate('search_hours_of_operations', request, ConnectSearchHoursOfOperationsResponse)

    async def search_metrics(
        self,
        request: ConnectSearchMetricsRequest,
    ) -> ConnectSearchMetricsResponse:
        client = self._require_client()
        return await self._execute(client.search_metrics, request, ConnectSearchMetricsResponse)

    async def search_metrics_paginated(
        self,
        request: ConnectSearchMetricsRequest,
    ) -> list[ConnectSearchMetricsResponse]:
        return await self._paginate('search_metrics', request, ConnectSearchMetricsResponse)

    async def search_notifications(
        self,
        request: ConnectSearchNotificationsRequest,
    ) -> ConnectSearchNotificationsResponse:
        client = self._require_client()
        return await self._execute(client.search_notifications, request, ConnectSearchNotificationsResponse)

    async def search_predefined_attributes(
        self,
        request: ConnectSearchPredefinedAttributesRequest,
    ) -> ConnectSearchPredefinedAttributesResponse:
        client = self._require_client()
        return await self._execute(client.search_predefined_attributes, request, ConnectSearchPredefinedAttributesResponse)

    async def search_predefined_attributes_paginated(
        self,
        request: ConnectSearchPredefinedAttributesRequest,
    ) -> list[ConnectSearchPredefinedAttributesResponse]:
        return await self._paginate('search_predefined_attributes', request, ConnectSearchPredefinedAttributesResponse)

    async def search_prompts(
        self,
        request: ConnectSearchPromptsRequest,
    ) -> ConnectSearchPromptsResponse:
        client = self._require_client()
        return await self._execute(client.search_prompts, request, ConnectSearchPromptsResponse)

    async def search_prompts_paginated(
        self,
        request: ConnectSearchPromptsRequest,
    ) -> list[ConnectSearchPromptsResponse]:
        return await self._paginate('search_prompts', request, ConnectSearchPromptsResponse)

    async def search_queues(
        self,
        request: ConnectSearchQueuesRequest,
    ) -> ConnectSearchQueuesResponse:
        client = self._require_client()
        return await self._execute(client.search_queues, request, ConnectSearchQueuesResponse)

    async def search_queues_paginated(
        self,
        request: ConnectSearchQueuesRequest,
    ) -> list[ConnectSearchQueuesResponse]:
        return await self._paginate('search_queues', request, ConnectSearchQueuesResponse)

    async def search_quick_connects(
        self,
        request: ConnectSearchQuickConnectsRequest,
    ) -> ConnectSearchQuickConnectsResponse:
        client = self._require_client()
        return await self._execute(client.search_quick_connects, request, ConnectSearchQuickConnectsResponse)

    async def search_quick_connects_paginated(
        self,
        request: ConnectSearchQuickConnectsRequest,
    ) -> list[ConnectSearchQuickConnectsResponse]:
        return await self._paginate('search_quick_connects', request, ConnectSearchQuickConnectsResponse)

    async def search_resource_tags(
        self,
        request: ConnectSearchResourceTagsRequest,
    ) -> ConnectSearchResourceTagsResponse:
        client = self._require_client()
        return await self._execute(client.search_resource_tags, request, ConnectSearchResourceTagsResponse)

    async def search_resource_tags_paginated(
        self,
        request: ConnectSearchResourceTagsRequest,
    ) -> list[ConnectSearchResourceTagsResponse]:
        return await self._paginate('search_resource_tags', request, ConnectSearchResourceTagsResponse)

    async def search_routing_profiles(
        self,
        request: ConnectSearchRoutingProfilesRequest,
    ) -> ConnectSearchRoutingProfilesResponse:
        client = self._require_client()
        return await self._execute(client.search_routing_profiles, request, ConnectSearchRoutingProfilesResponse)

    async def search_routing_profiles_paginated(
        self,
        request: ConnectSearchRoutingProfilesRequest,
    ) -> list[ConnectSearchRoutingProfilesResponse]:
        return await self._paginate('search_routing_profiles', request, ConnectSearchRoutingProfilesResponse)

    async def search_rules(
        self,
        request: ConnectSearchRulesRequest,
    ) -> ConnectSearchRulesResponse:
        client = self._require_client()
        return await self._execute(client.search_rules, request, ConnectSearchRulesResponse)

    async def search_rules_paginated(
        self,
        request: ConnectSearchRulesRequest,
    ) -> list[ConnectSearchRulesResponse]:
        return await self._paginate('search_rules', request, ConnectSearchRulesResponse)

    async def search_security_profiles(
        self,
        request: ConnectSearchSecurityProfilesRequest,
    ) -> ConnectSearchSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.search_security_profiles, request, ConnectSearchSecurityProfilesResponse)

    async def search_security_profiles_paginated(
        self,
        request: ConnectSearchSecurityProfilesRequest,
    ) -> list[ConnectSearchSecurityProfilesResponse]:
        return await self._paginate('search_security_profiles', request, ConnectSearchSecurityProfilesResponse)

    async def search_test_cases(
        self,
        request: ConnectSearchTestCasesRequest,
    ) -> ConnectSearchTestCasesResponse:
        client = self._require_client()
        return await self._execute(client.search_test_cases, request, ConnectSearchTestCasesResponse)

    async def search_test_cases_paginated(
        self,
        request: ConnectSearchTestCasesRequest,
    ) -> list[ConnectSearchTestCasesResponse]:
        return await self._paginate('search_test_cases', request, ConnectSearchTestCasesResponse)

    async def search_user_hierarchy_groups(
        self,
        request: ConnectSearchUserHierarchyGroupsRequest,
    ) -> ConnectSearchUserHierarchyGroupsResponse:
        client = self._require_client()
        return await self._execute(client.search_user_hierarchy_groups, request, ConnectSearchUserHierarchyGroupsResponse)

    async def search_user_hierarchy_groups_paginated(
        self,
        request: ConnectSearchUserHierarchyGroupsRequest,
    ) -> list[ConnectSearchUserHierarchyGroupsResponse]:
        return await self._paginate('search_user_hierarchy_groups', request, ConnectSearchUserHierarchyGroupsResponse)

    async def search_users(
        self,
        request: ConnectSearchUsersRequest,
    ) -> ConnectSearchUsersResponse:
        client = self._require_client()
        return await self._execute(client.search_users, request, ConnectSearchUsersResponse)

    async def search_users_paginated(
        self,
        request: ConnectSearchUsersRequest,
    ) -> list[ConnectSearchUsersResponse]:
        return await self._paginate('search_users', request, ConnectSearchUsersResponse)

    async def search_views(
        self,
        request: ConnectSearchViewsRequest,
    ) -> ConnectSearchViewsResponse:
        client = self._require_client()
        return await self._execute(client.search_views, request, ConnectSearchViewsResponse)

    async def search_views_paginated(
        self,
        request: ConnectSearchViewsRequest,
    ) -> list[ConnectSearchViewsResponse]:
        return await self._paginate('search_views', request, ConnectSearchViewsResponse)

    async def search_vocabularies(
        self,
        request: ConnectSearchVocabulariesRequest,
    ) -> ConnectSearchVocabulariesResponse:
        client = self._require_client()
        return await self._execute(client.search_vocabularies, request, ConnectSearchVocabulariesResponse)

    async def search_vocabularies_paginated(
        self,
        request: ConnectSearchVocabulariesRequest,
    ) -> list[ConnectSearchVocabulariesResponse]:
        return await self._paginate('search_vocabularies', request, ConnectSearchVocabulariesResponse)

    async def search_workspace_associations(
        self,
        request: ConnectSearchWorkspaceAssociationsRequest,
    ) -> ConnectSearchWorkspaceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.search_workspace_associations, request, ConnectSearchWorkspaceAssociationsResponse)

    async def search_workspace_associations_paginated(
        self,
        request: ConnectSearchWorkspaceAssociationsRequest,
    ) -> list[ConnectSearchWorkspaceAssociationsResponse]:
        return await self._paginate('search_workspace_associations', request, ConnectSearchWorkspaceAssociationsResponse)

    async def search_workspaces(
        self,
        request: ConnectSearchWorkspacesRequest,
    ) -> ConnectSearchWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.search_workspaces, request, ConnectSearchWorkspacesResponse)

    async def search_workspaces_paginated(
        self,
        request: ConnectSearchWorkspacesRequest,
    ) -> list[ConnectSearchWorkspacesResponse]:
        return await self._paginate('search_workspaces', request, ConnectSearchWorkspacesResponse)

    async def send_chat_integration_event(
        self,
        request: ConnectSendChatIntegrationEventRequest,
    ) -> ConnectSendChatIntegrationEventResponse:
        client = self._require_client()
        return await self._execute(client.send_chat_integration_event, request, ConnectSendChatIntegrationEventResponse)

    async def send_outbound_email(
        self,
        request: ConnectSendOutboundEmailRequest,
    ) -> ConnectSendOutboundEmailResponse:
        client = self._require_client()
        return await self._execute(client.send_outbound_email, request, ConnectSendOutboundEmailResponse)

    async def send_outbound_web_notification(
        self,
        request: ConnectSendOutboundWebNotificationRequest,
    ) -> ConnectSendOutboundWebNotificationResponse:
        client = self._require_client()
        return await self._execute(client.send_outbound_web_notification, request, ConnectSendOutboundWebNotificationResponse)

    async def start_assistant_contact(
        self,
        request: ConnectStartAssistantContactRequest,
    ) -> ConnectStartAssistantContactResponse:
        client = self._require_client()
        return await self._execute(client.start_assistant_contact, request, ConnectStartAssistantContactResponse)

    async def start_attached_file_upload(
        self,
        request: ConnectStartAttachedFileUploadRequest,
    ) -> ConnectStartAttachedFileUploadResponse:
        client = self._require_client()
        return await self._execute(client.start_attached_file_upload, request, ConnectStartAttachedFileUploadResponse)

    async def start_chat_contact(
        self,
        request: ConnectStartChatContactRequest,
    ) -> ConnectStartChatContactResponse:
        client = self._require_client()
        return await self._execute(client.start_chat_contact, request, ConnectStartChatContactResponse)

    async def start_contact_conversational_analytics_job(
        self,
        request: ConnectStartContactConversationalAnalyticsJobRequest,
    ) -> ConnectStartContactConversationalAnalyticsJobResponse:
        client = self._require_client()
        return await self._execute(client.start_contact_conversational_analytics_job, request, ConnectStartContactConversationalAnalyticsJobResponse)

    async def start_contact_evaluation(
        self,
        request: ConnectStartContactEvaluationRequest,
    ) -> ConnectStartContactEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.start_contact_evaluation, request, ConnectStartContactEvaluationResponse)

    async def start_contact_media_processing(
        self,
        request: ConnectStartContactMediaProcessingRequest | None = None,
    ) -> ConnectStartContactMediaProcessingResponse:
        client = self._require_client()
        return await self._execute(client.start_contact_media_processing, request, ConnectStartContactMediaProcessingResponse)

    async def start_contact_recording(
        self,
        request: ConnectStartContactRecordingRequest,
    ) -> ConnectStartContactRecordingResponse:
        client = self._require_client()
        return await self._execute(client.start_contact_recording, request, ConnectStartContactRecordingResponse)

    async def start_contact_streaming(
        self,
        request: ConnectStartContactStreamingRequest,
    ) -> ConnectStartContactStreamingResponse:
        client = self._require_client()
        return await self._execute(client.start_contact_streaming, request, ConnectStartContactStreamingResponse)

    async def start_email_contact(
        self,
        request: ConnectStartEmailContactRequest,
    ) -> ConnectStartEmailContactResponse:
        client = self._require_client()
        return await self._execute(client.start_email_contact, request, ConnectStartEmailContactResponse)

    async def start_evaluation_form_validation(
        self,
        request: ConnectStartEvaluationFormValidationRequest,
    ) -> ConnectStartEvaluationFormValidationResponse:
        client = self._require_client()
        return await self._execute(client.start_evaluation_form_validation, request, ConnectStartEvaluationFormValidationResponse)

    async def start_outbound_chat_contact(
        self,
        request: ConnectStartOutboundChatContactRequest,
    ) -> ConnectStartOutboundChatContactResponse:
        client = self._require_client()
        return await self._execute(client.start_outbound_chat_contact, request, ConnectStartOutboundChatContactResponse)

    async def start_outbound_email_contact(
        self,
        request: ConnectStartOutboundEmailContactRequest,
    ) -> ConnectStartOutboundEmailContactResponse:
        client = self._require_client()
        return await self._execute(client.start_outbound_email_contact, request, ConnectStartOutboundEmailContactResponse)

    async def start_outbound_voice_contact(
        self,
        request: ConnectStartOutboundVoiceContactRequest,
    ) -> ConnectStartOutboundVoiceContactResponse:
        client = self._require_client()
        return await self._execute(client.start_outbound_voice_contact, request, ConnectStartOutboundVoiceContactResponse)

    async def start_screen_sharing(
        self,
        request: ConnectStartScreenSharingRequest,
    ) -> ConnectStartScreenSharingResponse:
        client = self._require_client()
        return await self._execute(client.start_screen_sharing, request, ConnectStartScreenSharingResponse)

    async def start_task_contact(
        self,
        request: ConnectStartTaskContactRequest,
    ) -> ConnectStartTaskContactResponse:
        client = self._require_client()
        return await self._execute(client.start_task_contact, request, ConnectStartTaskContactResponse)

    async def start_test_case_execution(
        self,
        request: ConnectStartTestCaseExecutionRequest,
    ) -> ConnectStartTestCaseExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_test_case_execution, request, ConnectStartTestCaseExecutionResponse)

    async def start_web_rtc_contact(
        self,
        request: ConnectStartWebRTCContactRequest,
    ) -> ConnectStartWebRTCContactResponse:
        client = self._require_client()
        return await self._execute(client.start_web_rtc_contact, request, ConnectStartWebRTCContactResponse)

    async def stop_contact(
        self,
        request: ConnectStopContactRequest,
    ) -> ConnectStopContactResponse:
        client = self._require_client()
        return await self._execute(client.stop_contact, request, ConnectStopContactResponse)

    async def stop_contact_media_processing(
        self,
        request: ConnectStopContactMediaProcessingRequest | None = None,
    ) -> ConnectStopContactMediaProcessingResponse:
        client = self._require_client()
        return await self._execute(client.stop_contact_media_processing, request, ConnectStopContactMediaProcessingResponse)

    async def stop_contact_recording(
        self,
        request: ConnectStopContactRecordingRequest,
    ) -> ConnectStopContactRecordingResponse:
        client = self._require_client()
        return await self._execute(client.stop_contact_recording, request, ConnectStopContactRecordingResponse)

    async def stop_contact_streaming(
        self,
        request: ConnectStopContactStreamingRequest,
    ) -> ConnectStopContactStreamingResponse:
        client = self._require_client()
        return await self._execute(client.stop_contact_streaming, request, ConnectStopContactStreamingResponse)

    async def stop_test_case_execution(
        self,
        request: ConnectStopTestCaseExecutionRequest,
    ) -> ConnectStopTestCaseExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_test_case_execution, request, ConnectStopTestCaseExecutionResponse)

    async def submit_contact_evaluation(
        self,
        request: ConnectSubmitContactEvaluationRequest,
    ) -> ConnectSubmitContactEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.submit_contact_evaluation, request, ConnectSubmitContactEvaluationResponse)

    async def suspend_contact_recording(
        self,
        request: ConnectSuspendContactRecordingRequest,
    ) -> ConnectSuspendContactRecordingResponse:
        client = self._require_client()
        return await self._execute(client.suspend_contact_recording, request, ConnectSuspendContactRecordingResponse)

    async def tag_contact(
        self,
        request: ConnectTagContactRequest,
    ) -> ConnectTagContactResponse:
        client = self._require_client()
        return await self._execute(client.tag_contact, request, ConnectTagContactResponse)

    async def tag_resource(
        self,
        request: ConnectTagResourceRequest,
    ) -> ConnectTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ConnectTagResourceResponse)

    async def transfer_contact(
        self,
        request: ConnectTransferContactRequest,
    ) -> ConnectTransferContactResponse:
        client = self._require_client()
        return await self._execute(client.transfer_contact, request, ConnectTransferContactResponse)

    async def untag_contact(
        self,
        request: ConnectUntagContactRequest,
    ) -> ConnectUntagContactResponse:
        client = self._require_client()
        return await self._execute(client.untag_contact, request, ConnectUntagContactResponse)

    async def untag_resource(
        self,
        request: ConnectUntagResourceRequest,
    ) -> ConnectUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ConnectUntagResourceResponse)

    async def update_agent_status(
        self,
        request: ConnectUpdateAgentStatusRequest,
    ) -> ConnectUpdateAgentStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_agent_status, request, ConnectUpdateAgentStatusResponse)

    async def update_attached_files_configuration(
        self,
        request: ConnectUpdateAttachedFilesConfigurationRequest,
    ) -> ConnectUpdateAttachedFilesConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_attached_files_configuration, request, ConnectUpdateAttachedFilesConfigurationResponse)

    async def update_authentication_profile(
        self,
        request: ConnectUpdateAuthenticationProfileRequest,
    ) -> ConnectUpdateAuthenticationProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_authentication_profile, request, ConnectUpdateAuthenticationProfileResponse)

    async def update_contact(
        self,
        request: ConnectUpdateContactRequest,
    ) -> ConnectUpdateContactResponse:
        client = self._require_client()
        return await self._execute(client.update_contact, request, ConnectUpdateContactResponse)

    async def update_contact_attributes(
        self,
        request: ConnectUpdateContactAttributesRequest,
    ) -> ConnectUpdateContactAttributesResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_attributes, request, ConnectUpdateContactAttributesResponse)

    async def update_contact_evaluation(
        self,
        request: ConnectUpdateContactEvaluationRequest,
    ) -> ConnectUpdateContactEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_evaluation, request, ConnectUpdateContactEvaluationResponse)

    async def update_contact_flow_alias(
        self,
        request: ConnectUpdateContactFlowAliasRequest,
    ) -> ConnectUpdateContactFlowAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_alias, request, ConnectUpdateContactFlowAliasResponse)

    async def update_contact_flow_content(
        self,
        request: ConnectUpdateContactFlowContentRequest,
    ) -> ConnectUpdateContactFlowContentResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_content, request, ConnectUpdateContactFlowContentResponse)

    async def update_contact_flow_metadata(
        self,
        request: ConnectUpdateContactFlowMetadataRequest,
    ) -> ConnectUpdateContactFlowMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_metadata, request, ConnectUpdateContactFlowMetadataResponse)

    async def update_contact_flow_module_alias(
        self,
        request: ConnectUpdateContactFlowModuleAliasRequest,
    ) -> ConnectUpdateContactFlowModuleAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_module_alias, request, ConnectUpdateContactFlowModuleAliasResponse)

    async def update_contact_flow_module_content(
        self,
        request: ConnectUpdateContactFlowModuleContentRequest,
    ) -> ConnectUpdateContactFlowModuleContentResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_module_content, request, ConnectUpdateContactFlowModuleContentResponse)

    async def update_contact_flow_module_metadata(
        self,
        request: ConnectUpdateContactFlowModuleMetadataRequest,
    ) -> ConnectUpdateContactFlowModuleMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_module_metadata, request, ConnectUpdateContactFlowModuleMetadataResponse)

    async def update_contact_flow_name(
        self,
        request: ConnectUpdateContactFlowNameRequest,
    ) -> ConnectUpdateContactFlowNameResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_flow_name, request, ConnectUpdateContactFlowNameResponse)

    async def update_contact_routing_data(
        self,
        request: ConnectUpdateContactRoutingDataRequest,
    ) -> ConnectUpdateContactRoutingDataResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_routing_data, request, ConnectUpdateContactRoutingDataResponse)

    async def update_contact_schedule(
        self,
        request: ConnectUpdateContactScheduleRequest,
    ) -> ConnectUpdateContactScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_schedule, request, ConnectUpdateContactScheduleResponse)

    async def update_contact_task_template(
        self,
        request: ConnectUpdateContactTaskTemplateRequest,
    ) -> ConnectUpdateContactTaskTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_task_template, request, ConnectUpdateContactTaskTemplateResponse)

    async def update_cross_region_routing(
        self,
        request: ConnectUpdateCrossRegionRoutingRequest,
    ) -> ConnectUpdateCrossRegionRoutingResponse:
        client = self._require_client()
        return await self._execute(client.update_cross_region_routing, request, ConnectUpdateCrossRegionRoutingResponse)

    async def update_data_table_attribute(
        self,
        request: ConnectUpdateDataTableAttributeRequest,
    ) -> ConnectUpdateDataTableAttributeResponse:
        client = self._require_client()
        return await self._execute(client.update_data_table_attribute, request, ConnectUpdateDataTableAttributeResponse)

    async def update_data_table_metadata(
        self,
        request: ConnectUpdateDataTableMetadataRequest,
    ) -> ConnectUpdateDataTableMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_data_table_metadata, request, ConnectUpdateDataTableMetadataResponse)

    async def update_data_table_primary_values(
        self,
        request: ConnectUpdateDataTablePrimaryValuesRequest,
    ) -> ConnectUpdateDataTablePrimaryValuesResponse:
        client = self._require_client()
        return await self._execute(client.update_data_table_primary_values, request, ConnectUpdateDataTablePrimaryValuesResponse)

    async def update_email_address_metadata(
        self,
        request: ConnectUpdateEmailAddressMetadataRequest,
    ) -> ConnectUpdateEmailAddressMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_email_address_metadata, request, ConnectUpdateEmailAddressMetadataResponse)

    async def update_evaluation_form(
        self,
        request: ConnectUpdateEvaluationFormRequest,
    ) -> ConnectUpdateEvaluationFormResponse:
        client = self._require_client()
        return await self._execute(client.update_evaluation_form, request, ConnectUpdateEvaluationFormResponse)

    async def update_extraction_definition(
        self,
        request: ConnectUpdateExtractionDefinitionRequest,
    ) -> ConnectUpdateExtractionDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.update_extraction_definition, request, ConnectUpdateExtractionDefinitionResponse)

    async def update_hours_of_operation(
        self,
        request: ConnectUpdateHoursOfOperationRequest,
    ) -> ConnectUpdateHoursOfOperationResponse:
        client = self._require_client()
        return await self._execute(client.update_hours_of_operation, request, ConnectUpdateHoursOfOperationResponse)

    async def update_hours_of_operation_override(
        self,
        request: ConnectUpdateHoursOfOperationOverrideRequest,
    ) -> ConnectUpdateHoursOfOperationOverrideResponse:
        client = self._require_client()
        return await self._execute(client.update_hours_of_operation_override, request, ConnectUpdateHoursOfOperationOverrideResponse)

    async def update_instance_attribute(
        self,
        request: ConnectUpdateInstanceAttributeRequest,
    ) -> ConnectUpdateInstanceAttributeResponse:
        client = self._require_client()
        return await self._execute(client.update_instance_attribute, request, ConnectUpdateInstanceAttributeResponse)

    async def update_instance_storage_config(
        self,
        request: ConnectUpdateInstanceStorageConfigRequest,
    ) -> ConnectUpdateInstanceStorageConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_instance_storage_config, request, ConnectUpdateInstanceStorageConfigResponse)

    async def update_metric_content(
        self,
        request: ConnectUpdateMetricContentRequest,
    ) -> ConnectUpdateMetricContentResponse:
        client = self._require_client()
        return await self._execute(client.update_metric_content, request, ConnectUpdateMetricContentResponse)

    async def update_metric_metadata(
        self,
        request: ConnectUpdateMetricMetadataRequest,
    ) -> ConnectUpdateMetricMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_metric_metadata, request, ConnectUpdateMetricMetadataResponse)

    async def update_notification_content(
        self,
        request: ConnectUpdateNotificationContentRequest,
    ) -> ConnectUpdateNotificationContentResponse:
        client = self._require_client()
        return await self._execute(client.update_notification_content, request, ConnectUpdateNotificationContentResponse)

    async def update_outbound_email_contact_message(
        self,
        request: ConnectUpdateOutboundEmailContactMessageRequest,
    ) -> ConnectUpdateOutboundEmailContactMessageResponse:
        client = self._require_client()
        return await self._execute(client.update_outbound_email_contact_message, request, ConnectUpdateOutboundEmailContactMessageResponse)

    async def update_participant_authentication(
        self,
        request: ConnectUpdateParticipantAuthenticationRequest,
    ) -> ConnectUpdateParticipantAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.update_participant_authentication, request, ConnectUpdateParticipantAuthenticationResponse)

    async def update_participant_role_config(
        self,
        request: ConnectUpdateParticipantRoleConfigRequest,
    ) -> ConnectUpdateParticipantRoleConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_participant_role_config, request, ConnectUpdateParticipantRoleConfigResponse)

    async def update_phone_number(
        self,
        request: ConnectUpdatePhoneNumberRequest,
    ) -> ConnectUpdatePhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.update_phone_number, request, ConnectUpdatePhoneNumberResponse)

    async def update_phone_number_metadata(
        self,
        request: ConnectUpdatePhoneNumberMetadataRequest,
    ) -> ConnectUpdatePhoneNumberMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_phone_number_metadata, request, ConnectUpdatePhoneNumberMetadataResponse)

    async def update_predefined_attribute(
        self,
        request: ConnectUpdatePredefinedAttributeRequest,
    ) -> ConnectUpdatePredefinedAttributeResponse:
        client = self._require_client()
        return await self._execute(client.update_predefined_attribute, request, ConnectUpdatePredefinedAttributeResponse)

    async def update_prompt(
        self,
        request: ConnectUpdatePromptRequest,
    ) -> ConnectUpdatePromptResponse:
        client = self._require_client()
        return await self._execute(client.update_prompt, request, ConnectUpdatePromptResponse)

    async def update_queue_hours_of_operation(
        self,
        request: ConnectUpdateQueueHoursOfOperationRequest,
    ) -> ConnectUpdateQueueHoursOfOperationResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_hours_of_operation, request, ConnectUpdateQueueHoursOfOperationResponse)

    async def update_queue_max_contacts(
        self,
        request: ConnectUpdateQueueMaxContactsRequest,
    ) -> ConnectUpdateQueueMaxContactsResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_max_contacts, request, ConnectUpdateQueueMaxContactsResponse)

    async def update_queue_name(
        self,
        request: ConnectUpdateQueueNameRequest,
    ) -> ConnectUpdateQueueNameResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_name, request, ConnectUpdateQueueNameResponse)

    async def update_queue_outbound_caller_config(
        self,
        request: ConnectUpdateQueueOutboundCallerConfigRequest,
    ) -> ConnectUpdateQueueOutboundCallerConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_outbound_caller_config, request, ConnectUpdateQueueOutboundCallerConfigResponse)

    async def update_queue_outbound_email_config(
        self,
        request: ConnectUpdateQueueOutboundEmailConfigRequest,
    ) -> ConnectUpdateQueueOutboundEmailConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_outbound_email_config, request, ConnectUpdateQueueOutboundEmailConfigResponse)

    async def update_queue_status(
        self,
        request: ConnectUpdateQueueStatusRequest,
    ) -> ConnectUpdateQueueStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_status, request, ConnectUpdateQueueStatusResponse)

    async def update_quick_connect_config(
        self,
        request: ConnectUpdateQuickConnectConfigRequest,
    ) -> ConnectUpdateQuickConnectConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_quick_connect_config, request, ConnectUpdateQuickConnectConfigResponse)

    async def update_quick_connect_name(
        self,
        request: ConnectUpdateQuickConnectNameRequest,
    ) -> ConnectUpdateQuickConnectNameResponse:
        client = self._require_client()
        return await self._execute(client.update_quick_connect_name, request, ConnectUpdateQuickConnectNameResponse)

    async def update_routing_profile_agent_availability_timer(
        self,
        request: ConnectUpdateRoutingProfileAgentAvailabilityTimerRequest,
    ) -> ConnectUpdateRoutingProfileAgentAvailabilityTimerResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_profile_agent_availability_timer, request, ConnectUpdateRoutingProfileAgentAvailabilityTimerResponse)

    async def update_routing_profile_concurrency(
        self,
        request: ConnectUpdateRoutingProfileConcurrencyRequest,
    ) -> ConnectUpdateRoutingProfileConcurrencyResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_profile_concurrency, request, ConnectUpdateRoutingProfileConcurrencyResponse)

    async def update_routing_profile_default_outbound_queue(
        self,
        request: ConnectUpdateRoutingProfileDefaultOutboundQueueRequest,
    ) -> ConnectUpdateRoutingProfileDefaultOutboundQueueResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_profile_default_outbound_queue, request, ConnectUpdateRoutingProfileDefaultOutboundQueueResponse)

    async def update_routing_profile_name(
        self,
        request: ConnectUpdateRoutingProfileNameRequest,
    ) -> ConnectUpdateRoutingProfileNameResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_profile_name, request, ConnectUpdateRoutingProfileNameResponse)

    async def update_routing_profile_queues(
        self,
        request: ConnectUpdateRoutingProfileQueuesRequest,
    ) -> ConnectUpdateRoutingProfileQueuesResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_profile_queues, request, ConnectUpdateRoutingProfileQueuesResponse)

    async def update_rule(
        self,
        request: ConnectUpdateRuleRequest,
    ) -> ConnectUpdateRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_rule, request, ConnectUpdateRuleResponse)

    async def update_security_profile(
        self,
        request: ConnectUpdateSecurityProfileRequest,
    ) -> ConnectUpdateSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_security_profile, request, ConnectUpdateSecurityProfileResponse)

    async def update_task_template(
        self,
        request: ConnectUpdateTaskTemplateRequest,
    ) -> ConnectUpdateTaskTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_task_template, request, ConnectUpdateTaskTemplateResponse)

    async def update_test_case(
        self,
        request: ConnectUpdateTestCaseRequest,
    ) -> ConnectUpdateTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.update_test_case, request, ConnectUpdateTestCaseResponse)

    async def update_traffic_distribution(
        self,
        request: ConnectUpdateTrafficDistributionRequest,
    ) -> ConnectUpdateTrafficDistributionResponse:
        client = self._require_client()
        return await self._execute(client.update_traffic_distribution, request, ConnectUpdateTrafficDistributionResponse)

    async def update_user_config(
        self,
        request: ConnectUpdateUserConfigRequest,
    ) -> ConnectUpdateUserConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_user_config, request, ConnectUpdateUserConfigResponse)

    async def update_user_hierarchy(
        self,
        request: ConnectUpdateUserHierarchyRequest,
    ) -> ConnectUpdateUserHierarchyResponse:
        client = self._require_client()
        return await self._execute(client.update_user_hierarchy, request, ConnectUpdateUserHierarchyResponse)

    async def update_user_hierarchy_group_name(
        self,
        request: ConnectUpdateUserHierarchyGroupNameRequest,
    ) -> ConnectUpdateUserHierarchyGroupNameResponse:
        client = self._require_client()
        return await self._execute(client.update_user_hierarchy_group_name, request, ConnectUpdateUserHierarchyGroupNameResponse)

    async def update_user_hierarchy_structure(
        self,
        request: ConnectUpdateUserHierarchyStructureRequest,
    ) -> ConnectUpdateUserHierarchyStructureResponse:
        client = self._require_client()
        return await self._execute(client.update_user_hierarchy_structure, request, ConnectUpdateUserHierarchyStructureResponse)

    async def update_user_identity_info(
        self,
        request: ConnectUpdateUserIdentityInfoRequest,
    ) -> ConnectUpdateUserIdentityInfoResponse:
        client = self._require_client()
        return await self._execute(client.update_user_identity_info, request, ConnectUpdateUserIdentityInfoResponse)

    async def update_user_notification_status(
        self,
        request: ConnectUpdateUserNotificationStatusRequest,
    ) -> ConnectUpdateUserNotificationStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_user_notification_status, request, ConnectUpdateUserNotificationStatusResponse)

    async def update_user_phone_config(
        self,
        request: ConnectUpdateUserPhoneConfigRequest,
    ) -> ConnectUpdateUserPhoneConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_user_phone_config, request, ConnectUpdateUserPhoneConfigResponse)

    async def update_user_proficiencies(
        self,
        request: ConnectUpdateUserProficienciesRequest,
    ) -> ConnectUpdateUserProficienciesResponse:
        client = self._require_client()
        return await self._execute(client.update_user_proficiencies, request, ConnectUpdateUserProficienciesResponse)

    async def update_user_routing_profile(
        self,
        request: ConnectUpdateUserRoutingProfileRequest,
    ) -> ConnectUpdateUserRoutingProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_user_routing_profile, request, ConnectUpdateUserRoutingProfileResponse)

    async def update_user_security_profiles(
        self,
        request: ConnectUpdateUserSecurityProfilesRequest,
    ) -> ConnectUpdateUserSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.update_user_security_profiles, request, ConnectUpdateUserSecurityProfilesResponse)

    async def update_view_content(
        self,
        request: ConnectUpdateViewContentRequest,
    ) -> ConnectUpdateViewContentResponse:
        client = self._require_client()
        return await self._execute(client.update_view_content, request, ConnectUpdateViewContentResponse)

    async def update_view_metadata(
        self,
        request: ConnectUpdateViewMetadataRequest,
    ) -> ConnectUpdateViewMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_view_metadata, request, ConnectUpdateViewMetadataResponse)

    async def update_workspace_metadata(
        self,
        request: ConnectUpdateWorkspaceMetadataRequest,
    ) -> ConnectUpdateWorkspaceMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_metadata, request, ConnectUpdateWorkspaceMetadataResponse)

    async def update_workspace_page(
        self,
        request: ConnectUpdateWorkspacePageRequest,
    ) -> ConnectUpdateWorkspacePageResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_page, request, ConnectUpdateWorkspacePageResponse)

    async def update_workspace_theme(
        self,
        request: ConnectUpdateWorkspaceThemeRequest,
    ) -> ConnectUpdateWorkspaceThemeResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_theme, request, ConnectUpdateWorkspaceThemeResponse)

    async def update_workspace_visibility(
        self,
        request: ConnectUpdateWorkspaceVisibilityRequest,
    ) -> ConnectUpdateWorkspaceVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_visibility, request, ConnectUpdateWorkspaceVisibilityResponse)
