from werkflow_aws.models.iot import (
    IoTAcceptCertificateTransferRequest,
    IoTAcceptCertificateTransferResponse,
    IoTAddThingToBillingGroupRequest,
    IoTAddThingToBillingGroupResponse,
    IoTAddThingToThingGroupRequest,
    IoTAddThingToThingGroupResponse,
    IoTAssociateSbomWithPackageVersionRequest,
    IoTAssociateSbomWithPackageVersionResponse,
    IoTAssociateTargetsWithJobRequest,
    IoTAssociateTargetsWithJobResponse,
    IoTAttachPolicyRequest,
    IoTAttachPolicyResponse,
    IoTAttachPrincipalPolicyRequest,
    IoTAttachPrincipalPolicyResponse,
    IoTAttachSecurityProfileRequest,
    IoTAttachSecurityProfileResponse,
    IoTAttachThingPrincipalRequest,
    IoTAttachThingPrincipalResponse,
    IoTCancelAuditMitigationActionsTaskRequest,
    IoTCancelAuditMitigationActionsTaskResponse,
    IoTCancelAuditTaskRequest,
    IoTCancelAuditTaskResponse,
    IoTCancelCertificateTransferRequest,
    IoTCancelCertificateTransferResponse,
    IoTCancelDetectMitigationActionsTaskRequest,
    IoTCancelDetectMitigationActionsTaskResponse,
    IoTCancelJobExecutionRequest,
    IoTCancelJobExecutionResponse,
    IoTCancelJobRequest,
    IoTCancelJobResponse,
    IoTClearDefaultAuthorizerRequest,
    IoTClearDefaultAuthorizerResponse,
    IoTConfirmTopicRuleDestinationRequest,
    IoTConfirmTopicRuleDestinationResponse,
    IoTCreateAuditSuppressionRequest,
    IoTCreateAuditSuppressionResponse,
    IoTCreateAuthorizerRequest,
    IoTCreateAuthorizerResponse,
    IoTCreateBillingGroupRequest,
    IoTCreateBillingGroupResponse,
    IoTCreateCertificateFromCsrRequest,
    IoTCreateCertificateFromCsrResponse,
    IoTCreateCertificateProviderRequest,
    IoTCreateCertificateProviderResponse,
    IoTCreateCommandRequest,
    IoTCreateCommandResponse,
    IoTCreateCustomMetricRequest,
    IoTCreateCustomMetricResponse,
    IoTCreateDimensionRequest,
    IoTCreateDimensionResponse,
    IoTCreateDomainConfigurationRequest,
    IoTCreateDomainConfigurationResponse,
    IoTCreateDynamicThingGroupRequest,
    IoTCreateDynamicThingGroupResponse,
    IoTCreateFleetMetricRequest,
    IoTCreateFleetMetricResponse,
    IoTCreateJobRequest,
    IoTCreateJobResponse,
    IoTCreateJobTemplateRequest,
    IoTCreateJobTemplateResponse,
    IoTCreateKeysAndCertificateRequest,
    IoTCreateKeysAndCertificateResponse,
    IoTCreateMitigationActionRequest,
    IoTCreateMitigationActionResponse,
    IoTCreateOTAUpdateRequest,
    IoTCreateOTAUpdateResponse,
    IoTCreatePackageRequest,
    IoTCreatePackageResponse,
    IoTCreatePackageVersionRequest,
    IoTCreatePackageVersionResponse,
    IoTCreatePolicyRequest,
    IoTCreatePolicyResponse,
    IoTCreatePolicyVersionRequest,
    IoTCreatePolicyVersionResponse,
    IoTCreateProvisioningClaimRequest,
    IoTCreateProvisioningClaimResponse,
    IoTCreateProvisioningTemplateRequest,
    IoTCreateProvisioningTemplateResponse,
    IoTCreateProvisioningTemplateVersionRequest,
    IoTCreateProvisioningTemplateVersionResponse,
    IoTCreateRoleAliasRequest,
    IoTCreateRoleAliasResponse,
    IoTCreateScheduledAuditRequest,
    IoTCreateScheduledAuditResponse,
    IoTCreateSecurityProfileRequest,
    IoTCreateSecurityProfileResponse,
    IoTCreateStreamRequest,
    IoTCreateStreamResponse,
    IoTCreateThingGroupRequest,
    IoTCreateThingGroupResponse,
    IoTCreateThingRequest,
    IoTCreateThingResponse,
    IoTCreateThingTypeRequest,
    IoTCreateThingTypeResponse,
    IoTCreateTopicRuleDestinationRequest,
    IoTCreateTopicRuleDestinationResponse,
    IoTCreateTopicRuleRequest,
    IoTCreateTopicRuleResponse,
    IoTDeleteAccountAuditConfigurationRequest,
    IoTDeleteAccountAuditConfigurationResponse,
    IoTDeleteAuditSuppressionRequest,
    IoTDeleteAuditSuppressionResponse,
    IoTDeleteAuthorizerRequest,
    IoTDeleteAuthorizerResponse,
    IoTDeleteBillingGroupRequest,
    IoTDeleteBillingGroupResponse,
    IoTDeleteCACertificateRequest,
    IoTDeleteCACertificateResponse,
    IoTDeleteCertificateProviderRequest,
    IoTDeleteCertificateProviderResponse,
    IoTDeleteCertificateRequest,
    IoTDeleteCertificateResponse,
    IoTDeleteCommandExecutionRequest,
    IoTDeleteCommandExecutionResponse,
    IoTDeleteCommandRequest,
    IoTDeleteCommandResponse,
    IoTDeleteCustomMetricRequest,
    IoTDeleteCustomMetricResponse,
    IoTDeleteDimensionRequest,
    IoTDeleteDimensionResponse,
    IoTDeleteDomainConfigurationRequest,
    IoTDeleteDomainConfigurationResponse,
    IoTDeleteDynamicThingGroupRequest,
    IoTDeleteDynamicThingGroupResponse,
    IoTDeleteFleetMetricRequest,
    IoTDeleteFleetMetricResponse,
    IoTDeleteJobExecutionRequest,
    IoTDeleteJobExecutionResponse,
    IoTDeleteJobRequest,
    IoTDeleteJobResponse,
    IoTDeleteJobTemplateRequest,
    IoTDeleteJobTemplateResponse,
    IoTDeleteMitigationActionRequest,
    IoTDeleteMitigationActionResponse,
    IoTDeleteOTAUpdateRequest,
    IoTDeleteOTAUpdateResponse,
    IoTDeletePackageRequest,
    IoTDeletePackageResponse,
    IoTDeletePackageVersionRequest,
    IoTDeletePackageVersionResponse,
    IoTDeletePolicyRequest,
    IoTDeletePolicyResponse,
    IoTDeletePolicyVersionRequest,
    IoTDeletePolicyVersionResponse,
    IoTDeleteProvisioningTemplateRequest,
    IoTDeleteProvisioningTemplateResponse,
    IoTDeleteProvisioningTemplateVersionRequest,
    IoTDeleteProvisioningTemplateVersionResponse,
    IoTDeleteRegistrationCodeRequest,
    IoTDeleteRegistrationCodeResponse,
    IoTDeleteRoleAliasRequest,
    IoTDeleteRoleAliasResponse,
    IoTDeleteScheduledAuditRequest,
    IoTDeleteScheduledAuditResponse,
    IoTDeleteSecurityProfileRequest,
    IoTDeleteSecurityProfileResponse,
    IoTDeleteStreamRequest,
    IoTDeleteStreamResponse,
    IoTDeleteThingGroupRequest,
    IoTDeleteThingGroupResponse,
    IoTDeleteThingRequest,
    IoTDeleteThingResponse,
    IoTDeleteThingTypeRequest,
    IoTDeleteThingTypeResponse,
    IoTDeleteTopicRuleDestinationRequest,
    IoTDeleteTopicRuleDestinationResponse,
    IoTDeleteTopicRuleRequest,
    IoTDeleteTopicRuleResponse,
    IoTDeleteV2LoggingLevelRequest,
    IoTDeleteV2LoggingLevelResponse,
    IoTDeprecateThingTypeRequest,
    IoTDeprecateThingTypeResponse,
    IoTDescribeAccountAuditConfigurationRequest,
    IoTDescribeAccountAuditConfigurationResponse,
    IoTDescribeAuditFindingRequest,
    IoTDescribeAuditFindingResponse,
    IoTDescribeAuditMitigationActionsTaskRequest,
    IoTDescribeAuditMitigationActionsTaskResponse,
    IoTDescribeAuditSuppressionRequest,
    IoTDescribeAuditSuppressionResponse,
    IoTDescribeAuditTaskRequest,
    IoTDescribeAuditTaskResponse,
    IoTDescribeAuthorizerRequest,
    IoTDescribeAuthorizerResponse,
    IoTDescribeBillingGroupRequest,
    IoTDescribeBillingGroupResponse,
    IoTDescribeCACertificateRequest,
    IoTDescribeCACertificateResponse,
    IoTDescribeCertificateProviderRequest,
    IoTDescribeCertificateProviderResponse,
    IoTDescribeCertificateRequest,
    IoTDescribeCertificateResponse,
    IoTDescribeCustomMetricRequest,
    IoTDescribeCustomMetricResponse,
    IoTDescribeDefaultAuthorizerRequest,
    IoTDescribeDefaultAuthorizerResponse,
    IoTDescribeDetectMitigationActionsTaskRequest,
    IoTDescribeDetectMitigationActionsTaskResponse,
    IoTDescribeDimensionRequest,
    IoTDescribeDimensionResponse,
    IoTDescribeDomainConfigurationRequest,
    IoTDescribeDomainConfigurationResponse,
    IoTDescribeEncryptionConfigurationRequest,
    IoTDescribeEncryptionConfigurationResponse,
    IoTDescribeEndpointRequest,
    IoTDescribeEndpointResponse,
    IoTDescribeEventConfigurationsRequest,
    IoTDescribeEventConfigurationsResponse,
    IoTDescribeFleetMetricRequest,
    IoTDescribeFleetMetricResponse,
    IoTDescribeIndexRequest,
    IoTDescribeIndexResponse,
    IoTDescribeJobExecutionRequest,
    IoTDescribeJobExecutionResponse,
    IoTDescribeJobRequest,
    IoTDescribeJobResponse,
    IoTDescribeJobTemplateRequest,
    IoTDescribeJobTemplateResponse,
    IoTDescribeManagedJobTemplateRequest,
    IoTDescribeManagedJobTemplateResponse,
    IoTDescribeMitigationActionRequest,
    IoTDescribeMitigationActionResponse,
    IoTDescribeProvisioningTemplateRequest,
    IoTDescribeProvisioningTemplateResponse,
    IoTDescribeProvisioningTemplateVersionRequest,
    IoTDescribeProvisioningTemplateVersionResponse,
    IoTDescribeRoleAliasRequest,
    IoTDescribeRoleAliasResponse,
    IoTDescribeScheduledAuditRequest,
    IoTDescribeScheduledAuditResponse,
    IoTDescribeSecurityProfileRequest,
    IoTDescribeSecurityProfileResponse,
    IoTDescribeStreamRequest,
    IoTDescribeStreamResponse,
    IoTDescribeThingGroupRequest,
    IoTDescribeThingGroupResponse,
    IoTDescribeThingRegistrationTaskRequest,
    IoTDescribeThingRegistrationTaskResponse,
    IoTDescribeThingRequest,
    IoTDescribeThingResponse,
    IoTDescribeThingTypeRequest,
    IoTDescribeThingTypeResponse,
    IoTDetachPolicyRequest,
    IoTDetachPolicyResponse,
    IoTDetachPrincipalPolicyRequest,
    IoTDetachPrincipalPolicyResponse,
    IoTDetachSecurityProfileRequest,
    IoTDetachSecurityProfileResponse,
    IoTDetachThingPrincipalRequest,
    IoTDetachThingPrincipalResponse,
    IoTDisableTopicRuleRequest,
    IoTDisableTopicRuleResponse,
    IoTDisassociateSbomFromPackageVersionRequest,
    IoTDisassociateSbomFromPackageVersionResponse,
    IoTEnableTopicRuleRequest,
    IoTEnableTopicRuleResponse,
    IoTGetBehaviorModelTrainingSummariesRequest,
    IoTGetBehaviorModelTrainingSummariesResponse,
    IoTGetBucketsAggregationRequest,
    IoTGetBucketsAggregationResponse,
    IoTGetCardinalityRequest,
    IoTGetCardinalityResponse,
    IoTGetCommandExecutionRequest,
    IoTGetCommandExecutionResponse,
    IoTGetCommandRequest,
    IoTGetCommandResponse,
    IoTGetEffectivePoliciesRequest,
    IoTGetEffectivePoliciesResponse,
    IoTGetIndexingConfigurationRequest,
    IoTGetIndexingConfigurationResponse,
    IoTGetJobDocumentRequest,
    IoTGetJobDocumentResponse,
    IoTGetLoggingOptionsRequest,
    IoTGetLoggingOptionsResponse,
    IoTGetOTAUpdateRequest,
    IoTGetOTAUpdateResponse,
    IoTGetPackageConfigurationRequest,
    IoTGetPackageConfigurationResponse,
    IoTGetPackageRequest,
    IoTGetPackageResponse,
    IoTGetPackageVersionRequest,
    IoTGetPackageVersionResponse,
    IoTGetPercentilesRequest,
    IoTGetPercentilesResponse,
    IoTGetPolicyRequest,
    IoTGetPolicyResponse,
    IoTGetPolicyVersionRequest,
    IoTGetPolicyVersionResponse,
    IoTGetRegistrationCodeRequest,
    IoTGetRegistrationCodeResponse,
    IoTGetStatisticsRequest,
    IoTGetStatisticsResponse,
    IoTGetThingConnectivityDataRequest,
    IoTGetThingConnectivityDataResponse,
    IoTGetTopicRuleDestinationRequest,
    IoTGetTopicRuleDestinationResponse,
    IoTGetTopicRuleRequest,
    IoTGetTopicRuleResponse,
    IoTGetV2LoggingOptionsRequest,
    IoTGetV2LoggingOptionsResponse,
    IoTListActiveViolationsRequest,
    IoTListActiveViolationsResponse,
    IoTListAttachedPoliciesRequest,
    IoTListAttachedPoliciesResponse,
    IoTListAuditFindingsRequest,
    IoTListAuditFindingsResponse,
    IoTListAuditMitigationActionsExecutionsRequest,
    IoTListAuditMitigationActionsExecutionsResponse,
    IoTListAuditMitigationActionsTasksRequest,
    IoTListAuditMitigationActionsTasksResponse,
    IoTListAuditSuppressionsRequest,
    IoTListAuditSuppressionsResponse,
    IoTListAuditTasksRequest,
    IoTListAuditTasksResponse,
    IoTListAuthorizersRequest,
    IoTListAuthorizersResponse,
    IoTListBillingGroupsRequest,
    IoTListBillingGroupsResponse,
    IoTListCACertificatesRequest,
    IoTListCACertificatesResponse,
    IoTListCertificateProvidersRequest,
    IoTListCertificateProvidersResponse,
    IoTListCertificatesByCARequest,
    IoTListCertificatesByCAResponse,
    IoTListCertificatesRequest,
    IoTListCertificatesResponse,
    IoTListCommandExecutionsRequest,
    IoTListCommandExecutionsResponse,
    IoTListCommandsRequest,
    IoTListCommandsResponse,
    IoTListCustomMetricsRequest,
    IoTListCustomMetricsResponse,
    IoTListDetectMitigationActionsExecutionsRequest,
    IoTListDetectMitigationActionsExecutionsResponse,
    IoTListDetectMitigationActionsTasksRequest,
    IoTListDetectMitigationActionsTasksResponse,
    IoTListDimensionsRequest,
    IoTListDimensionsResponse,
    IoTListDomainConfigurationsRequest,
    IoTListDomainConfigurationsResponse,
    IoTListFleetMetricsRequest,
    IoTListFleetMetricsResponse,
    IoTListIndicesRequest,
    IoTListIndicesResponse,
    IoTListJobExecutionsForJobRequest,
    IoTListJobExecutionsForJobResponse,
    IoTListJobExecutionsForThingRequest,
    IoTListJobExecutionsForThingResponse,
    IoTListJobTemplatesRequest,
    IoTListJobTemplatesResponse,
    IoTListJobsRequest,
    IoTListJobsResponse,
    IoTListManagedJobTemplatesRequest,
    IoTListManagedJobTemplatesResponse,
    IoTListMetricValuesRequest,
    IoTListMetricValuesResponse,
    IoTListMitigationActionsRequest,
    IoTListMitigationActionsResponse,
    IoTListOTAUpdatesRequest,
    IoTListOTAUpdatesResponse,
    IoTListOutgoingCertificatesRequest,
    IoTListOutgoingCertificatesResponse,
    IoTListPackageVersionsRequest,
    IoTListPackageVersionsResponse,
    IoTListPackagesRequest,
    IoTListPackagesResponse,
    IoTListPoliciesRequest,
    IoTListPoliciesResponse,
    IoTListPolicyPrincipalsRequest,
    IoTListPolicyPrincipalsResponse,
    IoTListPolicyVersionsRequest,
    IoTListPolicyVersionsResponse,
    IoTListPrincipalPoliciesRequest,
    IoTListPrincipalPoliciesResponse,
    IoTListPrincipalThingsRequest,
    IoTListPrincipalThingsResponse,
    IoTListPrincipalThingsV2Request,
    IoTListPrincipalThingsV2Response,
    IoTListProvisioningTemplateVersionsRequest,
    IoTListProvisioningTemplateVersionsResponse,
    IoTListProvisioningTemplatesRequest,
    IoTListProvisioningTemplatesResponse,
    IoTListRelatedResourcesForAuditFindingRequest,
    IoTListRelatedResourcesForAuditFindingResponse,
    IoTListRoleAliasesRequest,
    IoTListRoleAliasesResponse,
    IoTListSbomValidationResultsRequest,
    IoTListSbomValidationResultsResponse,
    IoTListScheduledAuditsRequest,
    IoTListScheduledAuditsResponse,
    IoTListSecurityProfilesForTargetRequest,
    IoTListSecurityProfilesForTargetResponse,
    IoTListSecurityProfilesRequest,
    IoTListSecurityProfilesResponse,
    IoTListStreamsRequest,
    IoTListStreamsResponse,
    IoTListTagsForResourceRequest,
    IoTListTagsForResourceResponse,
    IoTListTargetsForPolicyRequest,
    IoTListTargetsForPolicyResponse,
    IoTListTargetsForSecurityProfileRequest,
    IoTListTargetsForSecurityProfileResponse,
    IoTListThingGroupsForThingRequest,
    IoTListThingGroupsForThingResponse,
    IoTListThingGroupsRequest,
    IoTListThingGroupsResponse,
    IoTListThingPrincipalsRequest,
    IoTListThingPrincipalsResponse,
    IoTListThingPrincipalsV2Request,
    IoTListThingPrincipalsV2Response,
    IoTListThingRegistrationTaskReportsRequest,
    IoTListThingRegistrationTaskReportsResponse,
    IoTListThingRegistrationTasksRequest,
    IoTListThingRegistrationTasksResponse,
    IoTListThingTypesRequest,
    IoTListThingTypesResponse,
    IoTListThingsInBillingGroupRequest,
    IoTListThingsInBillingGroupResponse,
    IoTListThingsInThingGroupRequest,
    IoTListThingsInThingGroupResponse,
    IoTListThingsRequest,
    IoTListThingsResponse,
    IoTListTopicRuleDestinationsRequest,
    IoTListTopicRuleDestinationsResponse,
    IoTListTopicRulesRequest,
    IoTListTopicRulesResponse,
    IoTListV2LoggingLevelsRequest,
    IoTListV2LoggingLevelsResponse,
    IoTListViolationEventsRequest,
    IoTListViolationEventsResponse,
    IoTPutVerificationStateOnViolationRequest,
    IoTPutVerificationStateOnViolationResponse,
    IoTRegisterCACertificateRequest,
    IoTRegisterCACertificateResponse,
    IoTRegisterCertificateRequest,
    IoTRegisterCertificateResponse,
    IoTRegisterCertificateWithoutCARequest,
    IoTRegisterCertificateWithoutCAResponse,
    IoTRegisterThingRequest,
    IoTRegisterThingResponse,
    IoTRejectCertificateTransferRequest,
    IoTRejectCertificateTransferResponse,
    IoTRemoveThingFromBillingGroupRequest,
    IoTRemoveThingFromBillingGroupResponse,
    IoTRemoveThingFromThingGroupRequest,
    IoTRemoveThingFromThingGroupResponse,
    IoTReplaceTopicRuleRequest,
    IoTReplaceTopicRuleResponse,
    IoTSearchIndexRequest,
    IoTSearchIndexResponse,
    IoTSetDefaultAuthorizerRequest,
    IoTSetDefaultAuthorizerResponse,
    IoTSetDefaultPolicyVersionRequest,
    IoTSetDefaultPolicyVersionResponse,
    IoTSetLoggingOptionsRequest,
    IoTSetLoggingOptionsResponse,
    IoTSetV2LoggingLevelRequest,
    IoTSetV2LoggingLevelResponse,
    IoTSetV2LoggingOptionsRequest,
    IoTSetV2LoggingOptionsResponse,
    IoTStartAuditMitigationActionsTaskRequest,
    IoTStartAuditMitigationActionsTaskResponse,
    IoTStartDetectMitigationActionsTaskRequest,
    IoTStartDetectMitigationActionsTaskResponse,
    IoTStartOnDemandAuditTaskRequest,
    IoTStartOnDemandAuditTaskResponse,
    IoTStartThingRegistrationTaskRequest,
    IoTStartThingRegistrationTaskResponse,
    IoTStopThingRegistrationTaskRequest,
    IoTStopThingRegistrationTaskResponse,
    IoTTagResourceRequest,
    IoTTagResourceResponse,
    IoTTestAuthorizationRequest,
    IoTTestAuthorizationResponse,
    IoTTestInvokeAuthorizerRequest,
    IoTTestInvokeAuthorizerResponse,
    IoTTransferCertificateRequest,
    IoTTransferCertificateResponse,
    IoTUntagResourceRequest,
    IoTUntagResourceResponse,
    IoTUpdateAccountAuditConfigurationRequest,
    IoTUpdateAccountAuditConfigurationResponse,
    IoTUpdateAuditSuppressionRequest,
    IoTUpdateAuditSuppressionResponse,
    IoTUpdateAuthorizerRequest,
    IoTUpdateAuthorizerResponse,
    IoTUpdateBillingGroupRequest,
    IoTUpdateBillingGroupResponse,
    IoTUpdateCACertificateRequest,
    IoTUpdateCACertificateResponse,
    IoTUpdateCertificateProviderRequest,
    IoTUpdateCertificateProviderResponse,
    IoTUpdateCertificateRequest,
    IoTUpdateCertificateResponse,
    IoTUpdateCommandRequest,
    IoTUpdateCommandResponse,
    IoTUpdateCustomMetricRequest,
    IoTUpdateCustomMetricResponse,
    IoTUpdateDimensionRequest,
    IoTUpdateDimensionResponse,
    IoTUpdateDomainConfigurationRequest,
    IoTUpdateDomainConfigurationResponse,
    IoTUpdateDynamicThingGroupRequest,
    IoTUpdateDynamicThingGroupResponse,
    IoTUpdateEncryptionConfigurationRequest,
    IoTUpdateEncryptionConfigurationResponse,
    IoTUpdateEventConfigurationsRequest,
    IoTUpdateEventConfigurationsResponse,
    IoTUpdateFleetMetricRequest,
    IoTUpdateFleetMetricResponse,
    IoTUpdateIndexingConfigurationRequest,
    IoTUpdateIndexingConfigurationResponse,
    IoTUpdateJobRequest,
    IoTUpdateJobResponse,
    IoTUpdateMitigationActionRequest,
    IoTUpdateMitigationActionResponse,
    IoTUpdatePackageConfigurationRequest,
    IoTUpdatePackageConfigurationResponse,
    IoTUpdatePackageRequest,
    IoTUpdatePackageResponse,
    IoTUpdatePackageVersionRequest,
    IoTUpdatePackageVersionResponse,
    IoTUpdateProvisioningTemplateRequest,
    IoTUpdateProvisioningTemplateResponse,
    IoTUpdateRoleAliasRequest,
    IoTUpdateRoleAliasResponse,
    IoTUpdateScheduledAuditRequest,
    IoTUpdateScheduledAuditResponse,
    IoTUpdateSecurityProfileRequest,
    IoTUpdateSecurityProfileResponse,
    IoTUpdateStreamRequest,
    IoTUpdateStreamResponse,
    IoTUpdateThingGroupRequest,
    IoTUpdateThingGroupResponse,
    IoTUpdateThingGroupsForThingRequest,
    IoTUpdateThingGroupsForThingResponse,
    IoTUpdateThingRequest,
    IoTUpdateThingResponse,
    IoTUpdateThingTypeRequest,
    IoTUpdateThingTypeResponse,
    IoTUpdateTopicRuleDestinationRequest,
    IoTUpdateTopicRuleDestinationResponse,
    IoTValidateSecurityProfileBehaviorsRequest,
    IoTValidateSecurityProfileBehaviorsResponse,
)
from werkflow_aws.types.iot_client import IoTClient
from .base import AWSBaseService


class AWSIoT(AWSBaseService[IoTClient]):
    service_name = 'iot'
    boto3_service_name = 'iot'

    def __init__(self) -> None:
        super().__init__(service_name='iot', boto3_service_name='iot')

    async def accept_certificate_transfer(
        self,
        request: IoTAcceptCertificateTransferRequest,
    ) -> IoTAcceptCertificateTransferResponse:
        client = self._require_client()
        return await self._execute(client.accept_certificate_transfer, request, IoTAcceptCertificateTransferResponse)

    async def add_thing_to_billing_group(
        self,
        request: IoTAddThingToBillingGroupRequest | None = None,
    ) -> IoTAddThingToBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.add_thing_to_billing_group, request, IoTAddThingToBillingGroupResponse)

    async def add_thing_to_thing_group(
        self,
        request: IoTAddThingToThingGroupRequest | None = None,
    ) -> IoTAddThingToThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.add_thing_to_thing_group, request, IoTAddThingToThingGroupResponse)

    async def associate_sbom_with_package_version(
        self,
        request: IoTAssociateSbomWithPackageVersionRequest,
    ) -> IoTAssociateSbomWithPackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.associate_sbom_with_package_version, request, IoTAssociateSbomWithPackageVersionResponse)

    async def associate_targets_with_job(
        self,
        request: IoTAssociateTargetsWithJobRequest,
    ) -> IoTAssociateTargetsWithJobResponse:
        client = self._require_client()
        return await self._execute(client.associate_targets_with_job, request, IoTAssociateTargetsWithJobResponse)

    async def attach_policy(
        self,
        request: IoTAttachPolicyRequest,
    ) -> IoTAttachPolicyResponse:
        client = self._require_client()
        return await self._execute(client.attach_policy, request, IoTAttachPolicyResponse)

    async def attach_principal_policy(
        self,
        request: IoTAttachPrincipalPolicyRequest,
    ) -> IoTAttachPrincipalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.attach_principal_policy, request, IoTAttachPrincipalPolicyResponse)

    async def attach_security_profile(
        self,
        request: IoTAttachSecurityProfileRequest,
    ) -> IoTAttachSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.attach_security_profile, request, IoTAttachSecurityProfileResponse)

    async def attach_thing_principal(
        self,
        request: IoTAttachThingPrincipalRequest,
    ) -> IoTAttachThingPrincipalResponse:
        client = self._require_client()
        return await self._execute(client.attach_thing_principal, request, IoTAttachThingPrincipalResponse)

    async def cancel_audit_mitigation_actions_task(
        self,
        request: IoTCancelAuditMitigationActionsTaskRequest,
    ) -> IoTCancelAuditMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_audit_mitigation_actions_task, request, IoTCancelAuditMitigationActionsTaskResponse)

    async def cancel_audit_task(
        self,
        request: IoTCancelAuditTaskRequest,
    ) -> IoTCancelAuditTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_audit_task, request, IoTCancelAuditTaskResponse)

    async def cancel_certificate_transfer(
        self,
        request: IoTCancelCertificateTransferRequest,
    ) -> IoTCancelCertificateTransferResponse:
        client = self._require_client()
        return await self._execute(client.cancel_certificate_transfer, request, IoTCancelCertificateTransferResponse)

    async def cancel_detect_mitigation_actions_task(
        self,
        request: IoTCancelDetectMitigationActionsTaskRequest,
    ) -> IoTCancelDetectMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_detect_mitigation_actions_task, request, IoTCancelDetectMitigationActionsTaskResponse)

    async def cancel_job(
        self,
        request: IoTCancelJobRequest,
    ) -> IoTCancelJobResponse:
        client = self._require_client()
        return await self._execute(client.cancel_job, request, IoTCancelJobResponse)

    async def cancel_job_execution(
        self,
        request: IoTCancelJobExecutionRequest,
    ) -> IoTCancelJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_job_execution, request, IoTCancelJobExecutionResponse)

    async def clear_default_authorizer(
        self,
        request: IoTClearDefaultAuthorizerRequest | None = None,
    ) -> IoTClearDefaultAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.clear_default_authorizer, request, IoTClearDefaultAuthorizerResponse)

    async def confirm_topic_rule_destination(
        self,
        request: IoTConfirmTopicRuleDestinationRequest,
    ) -> IoTConfirmTopicRuleDestinationResponse:
        client = self._require_client()
        return await self._execute(client.confirm_topic_rule_destination, request, IoTConfirmTopicRuleDestinationResponse)

    async def create_audit_suppression(
        self,
        request: IoTCreateAuditSuppressionRequest,
    ) -> IoTCreateAuditSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.create_audit_suppression, request, IoTCreateAuditSuppressionResponse)

    async def create_authorizer(
        self,
        request: IoTCreateAuthorizerRequest,
    ) -> IoTCreateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.create_authorizer, request, IoTCreateAuthorizerResponse)

    async def create_billing_group(
        self,
        request: IoTCreateBillingGroupRequest,
    ) -> IoTCreateBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_billing_group, request, IoTCreateBillingGroupResponse)

    async def create_certificate_from_csr(
        self,
        request: IoTCreateCertificateFromCsrRequest,
    ) -> IoTCreateCertificateFromCsrResponse:
        client = self._require_client()
        return await self._execute(client.create_certificate_from_csr, request, IoTCreateCertificateFromCsrResponse)

    async def create_certificate_provider(
        self,
        request: IoTCreateCertificateProviderRequest,
    ) -> IoTCreateCertificateProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_certificate_provider, request, IoTCreateCertificateProviderResponse)

    async def create_command(
        self,
        request: IoTCreateCommandRequest,
    ) -> IoTCreateCommandResponse:
        client = self._require_client()
        return await self._execute(client.create_command, request, IoTCreateCommandResponse)

    async def create_custom_metric(
        self,
        request: IoTCreateCustomMetricRequest,
    ) -> IoTCreateCustomMetricResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_metric, request, IoTCreateCustomMetricResponse)

    async def create_dimension(
        self,
        request: IoTCreateDimensionRequest,
    ) -> IoTCreateDimensionResponse:
        client = self._require_client()
        return await self._execute(client.create_dimension, request, IoTCreateDimensionResponse)

    async def create_domain_configuration(
        self,
        request: IoTCreateDomainConfigurationRequest,
    ) -> IoTCreateDomainConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_configuration, request, IoTCreateDomainConfigurationResponse)

    async def create_dynamic_thing_group(
        self,
        request: IoTCreateDynamicThingGroupRequest,
    ) -> IoTCreateDynamicThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_dynamic_thing_group, request, IoTCreateDynamicThingGroupResponse)

    async def create_fleet_metric(
        self,
        request: IoTCreateFleetMetricRequest,
    ) -> IoTCreateFleetMetricResponse:
        client = self._require_client()
        return await self._execute(client.create_fleet_metric, request, IoTCreateFleetMetricResponse)

    async def create_job(
        self,
        request: IoTCreateJobRequest,
    ) -> IoTCreateJobResponse:
        client = self._require_client()
        return await self._execute(client.create_job, request, IoTCreateJobResponse)

    async def create_job_template(
        self,
        request: IoTCreateJobTemplateRequest,
    ) -> IoTCreateJobTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_job_template, request, IoTCreateJobTemplateResponse)

    async def create_keys_and_certificate(
        self,
        request: IoTCreateKeysAndCertificateRequest | None = None,
    ) -> IoTCreateKeysAndCertificateResponse:
        client = self._require_client()
        return await self._execute(client.create_keys_and_certificate, request, IoTCreateKeysAndCertificateResponse)

    async def create_mitigation_action(
        self,
        request: IoTCreateMitigationActionRequest,
    ) -> IoTCreateMitigationActionResponse:
        client = self._require_client()
        return await self._execute(client.create_mitigation_action, request, IoTCreateMitigationActionResponse)

    async def create_ota_update(
        self,
        request: IoTCreateOTAUpdateRequest,
    ) -> IoTCreateOTAUpdateResponse:
        client = self._require_client()
        return await self._execute(client.create_ota_update, request, IoTCreateOTAUpdateResponse)

    async def create_package(
        self,
        request: IoTCreatePackageRequest,
    ) -> IoTCreatePackageResponse:
        client = self._require_client()
        return await self._execute(client.create_package, request, IoTCreatePackageResponse)

    async def create_package_version(
        self,
        request: IoTCreatePackageVersionRequest,
    ) -> IoTCreatePackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_package_version, request, IoTCreatePackageVersionResponse)

    async def create_policy(
        self,
        request: IoTCreatePolicyRequest,
    ) -> IoTCreatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_policy, request, IoTCreatePolicyResponse)

    async def create_policy_version(
        self,
        request: IoTCreatePolicyVersionRequest,
    ) -> IoTCreatePolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_policy_version, request, IoTCreatePolicyVersionResponse)

    async def create_provisioning_claim(
        self,
        request: IoTCreateProvisioningClaimRequest,
    ) -> IoTCreateProvisioningClaimResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioning_claim, request, IoTCreateProvisioningClaimResponse)

    async def create_provisioning_template(
        self,
        request: IoTCreateProvisioningTemplateRequest,
    ) -> IoTCreateProvisioningTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioning_template, request, IoTCreateProvisioningTemplateResponse)

    async def create_provisioning_template_version(
        self,
        request: IoTCreateProvisioningTemplateVersionRequest,
    ) -> IoTCreateProvisioningTemplateVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioning_template_version, request, IoTCreateProvisioningTemplateVersionResponse)

    async def create_role_alias(
        self,
        request: IoTCreateRoleAliasRequest,
    ) -> IoTCreateRoleAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_role_alias, request, IoTCreateRoleAliasResponse)

    async def create_scheduled_audit(
        self,
        request: IoTCreateScheduledAuditRequest,
    ) -> IoTCreateScheduledAuditResponse:
        client = self._require_client()
        return await self._execute(client.create_scheduled_audit, request, IoTCreateScheduledAuditResponse)

    async def create_security_profile(
        self,
        request: IoTCreateSecurityProfileRequest,
    ) -> IoTCreateSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_security_profile, request, IoTCreateSecurityProfileResponse)

    async def create_stream(
        self,
        request: IoTCreateStreamRequest,
    ) -> IoTCreateStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_stream, request, IoTCreateStreamResponse)

    async def create_thing(
        self,
        request: IoTCreateThingRequest,
    ) -> IoTCreateThingResponse:
        client = self._require_client()
        return await self._execute(client.create_thing, request, IoTCreateThingResponse)

    async def create_thing_group(
        self,
        request: IoTCreateThingGroupRequest,
    ) -> IoTCreateThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_thing_group, request, IoTCreateThingGroupResponse)

    async def create_thing_type(
        self,
        request: IoTCreateThingTypeRequest,
    ) -> IoTCreateThingTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_thing_type, request, IoTCreateThingTypeResponse)

    async def create_topic_rule(
        self,
        request: IoTCreateTopicRuleRequest,
    ) -> IoTCreateTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_topic_rule, request, IoTCreateTopicRuleResponse)

    async def create_topic_rule_destination(
        self,
        request: IoTCreateTopicRuleDestinationRequest,
    ) -> IoTCreateTopicRuleDestinationResponse:
        client = self._require_client()
        return await self._execute(client.create_topic_rule_destination, request, IoTCreateTopicRuleDestinationResponse)

    async def delete_account_audit_configuration(
        self,
        request: IoTDeleteAccountAuditConfigurationRequest | None = None,
    ) -> IoTDeleteAccountAuditConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_audit_configuration, request, IoTDeleteAccountAuditConfigurationResponse)

    async def delete_audit_suppression(
        self,
        request: IoTDeleteAuditSuppressionRequest,
    ) -> IoTDeleteAuditSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.delete_audit_suppression, request, IoTDeleteAuditSuppressionResponse)

    async def delete_authorizer(
        self,
        request: IoTDeleteAuthorizerRequest,
    ) -> IoTDeleteAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.delete_authorizer, request, IoTDeleteAuthorizerResponse)

    async def delete_billing_group(
        self,
        request: IoTDeleteBillingGroupRequest,
    ) -> IoTDeleteBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_billing_group, request, IoTDeleteBillingGroupResponse)

    async def delete_ca_certificate(
        self,
        request: IoTDeleteCACertificateRequest,
    ) -> IoTDeleteCACertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_ca_certificate, request, IoTDeleteCACertificateResponse)

    async def delete_certificate(
        self,
        request: IoTDeleteCertificateRequest,
    ) -> IoTDeleteCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate, request, IoTDeleteCertificateResponse)

    async def delete_certificate_provider(
        self,
        request: IoTDeleteCertificateProviderRequest,
    ) -> IoTDeleteCertificateProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate_provider, request, IoTDeleteCertificateProviderResponse)

    async def delete_command(
        self,
        request: IoTDeleteCommandRequest,
    ) -> IoTDeleteCommandResponse:
        client = self._require_client()
        return await self._execute(client.delete_command, request, IoTDeleteCommandResponse)

    async def delete_command_execution(
        self,
        request: IoTDeleteCommandExecutionRequest,
    ) -> IoTDeleteCommandExecutionResponse:
        client = self._require_client()
        return await self._execute(client.delete_command_execution, request, IoTDeleteCommandExecutionResponse)

    async def delete_custom_metric(
        self,
        request: IoTDeleteCustomMetricRequest,
    ) -> IoTDeleteCustomMetricResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_metric, request, IoTDeleteCustomMetricResponse)

    async def delete_dimension(
        self,
        request: IoTDeleteDimensionRequest,
    ) -> IoTDeleteDimensionResponse:
        client = self._require_client()
        return await self._execute(client.delete_dimension, request, IoTDeleteDimensionResponse)

    async def delete_domain_configuration(
        self,
        request: IoTDeleteDomainConfigurationRequest,
    ) -> IoTDeleteDomainConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_configuration, request, IoTDeleteDomainConfigurationResponse)

    async def delete_dynamic_thing_group(
        self,
        request: IoTDeleteDynamicThingGroupRequest,
    ) -> IoTDeleteDynamicThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_dynamic_thing_group, request, IoTDeleteDynamicThingGroupResponse)

    async def delete_fleet_metric(
        self,
        request: IoTDeleteFleetMetricRequest,
    ) -> IoTDeleteFleetMetricResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleet_metric, request, IoTDeleteFleetMetricResponse)

    async def delete_job(
        self,
        request: IoTDeleteJobRequest,
    ) -> IoTDeleteJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_job, request, IoTDeleteJobResponse)

    async def delete_job_execution(
        self,
        request: IoTDeleteJobExecutionRequest,
    ) -> IoTDeleteJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.delete_job_execution, request, IoTDeleteJobExecutionResponse)

    async def delete_job_template(
        self,
        request: IoTDeleteJobTemplateRequest,
    ) -> IoTDeleteJobTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_job_template, request, IoTDeleteJobTemplateResponse)

    async def delete_mitigation_action(
        self,
        request: IoTDeleteMitigationActionRequest,
    ) -> IoTDeleteMitigationActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_mitigation_action, request, IoTDeleteMitigationActionResponse)

    async def delete_ota_update(
        self,
        request: IoTDeleteOTAUpdateRequest,
    ) -> IoTDeleteOTAUpdateResponse:
        client = self._require_client()
        return await self._execute(client.delete_ota_update, request, IoTDeleteOTAUpdateResponse)

    async def delete_package(
        self,
        request: IoTDeletePackageRequest,
    ) -> IoTDeletePackageResponse:
        client = self._require_client()
        return await self._execute(client.delete_package, request, IoTDeletePackageResponse)

    async def delete_package_version(
        self,
        request: IoTDeletePackageVersionRequest,
    ) -> IoTDeletePackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_package_version, request, IoTDeletePackageVersionResponse)

    async def delete_policy(
        self,
        request: IoTDeletePolicyRequest,
    ) -> IoTDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy, request, IoTDeletePolicyResponse)

    async def delete_policy_version(
        self,
        request: IoTDeletePolicyVersionRequest,
    ) -> IoTDeletePolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy_version, request, IoTDeletePolicyVersionResponse)

    async def delete_provisioning_template(
        self,
        request: IoTDeleteProvisioningTemplateRequest,
    ) -> IoTDeleteProvisioningTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioning_template, request, IoTDeleteProvisioningTemplateResponse)

    async def delete_provisioning_template_version(
        self,
        request: IoTDeleteProvisioningTemplateVersionRequest,
    ) -> IoTDeleteProvisioningTemplateVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioning_template_version, request, IoTDeleteProvisioningTemplateVersionResponse)

    async def delete_registration_code(
        self,
        request: IoTDeleteRegistrationCodeRequest | None = None,
    ) -> IoTDeleteRegistrationCodeResponse:
        client = self._require_client()
        return await self._execute(client.delete_registration_code, request, IoTDeleteRegistrationCodeResponse)

    async def delete_role_alias(
        self,
        request: IoTDeleteRoleAliasRequest,
    ) -> IoTDeleteRoleAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_role_alias, request, IoTDeleteRoleAliasResponse)

    async def delete_scheduled_audit(
        self,
        request: IoTDeleteScheduledAuditRequest,
    ) -> IoTDeleteScheduledAuditResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduled_audit, request, IoTDeleteScheduledAuditResponse)

    async def delete_security_profile(
        self,
        request: IoTDeleteSecurityProfileRequest,
    ) -> IoTDeleteSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_profile, request, IoTDeleteSecurityProfileResponse)

    async def delete_stream(
        self,
        request: IoTDeleteStreamRequest,
    ) -> IoTDeleteStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_stream, request, IoTDeleteStreamResponse)

    async def delete_thing(
        self,
        request: IoTDeleteThingRequest,
    ) -> IoTDeleteThingResponse:
        client = self._require_client()
        return await self._execute(client.delete_thing, request, IoTDeleteThingResponse)

    async def delete_thing_group(
        self,
        request: IoTDeleteThingGroupRequest,
    ) -> IoTDeleteThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_thing_group, request, IoTDeleteThingGroupResponse)

    async def delete_thing_type(
        self,
        request: IoTDeleteThingTypeRequest,
    ) -> IoTDeleteThingTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_thing_type, request, IoTDeleteThingTypeResponse)

    async def delete_topic_rule(
        self,
        request: IoTDeleteTopicRuleRequest,
    ) -> IoTDeleteTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic_rule, request, IoTDeleteTopicRuleResponse)

    async def delete_topic_rule_destination(
        self,
        request: IoTDeleteTopicRuleDestinationRequest,
    ) -> IoTDeleteTopicRuleDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic_rule_destination, request, IoTDeleteTopicRuleDestinationResponse)

    async def delete_v2_logging_level(
        self,
        request: IoTDeleteV2LoggingLevelRequest,
    ) -> IoTDeleteV2LoggingLevelResponse:
        client = self._require_client()
        return await self._execute(client.delete_v2_logging_level, request, IoTDeleteV2LoggingLevelResponse)

    async def deprecate_thing_type(
        self,
        request: IoTDeprecateThingTypeRequest,
    ) -> IoTDeprecateThingTypeResponse:
        client = self._require_client()
        return await self._execute(client.deprecate_thing_type, request, IoTDeprecateThingTypeResponse)

    async def describe_account_audit_configuration(
        self,
        request: IoTDescribeAccountAuditConfigurationRequest | None = None,
    ) -> IoTDescribeAccountAuditConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_audit_configuration, request, IoTDescribeAccountAuditConfigurationResponse)

    async def describe_audit_finding(
        self,
        request: IoTDescribeAuditFindingRequest,
    ) -> IoTDescribeAuditFindingResponse:
        client = self._require_client()
        return await self._execute(client.describe_audit_finding, request, IoTDescribeAuditFindingResponse)

    async def describe_audit_mitigation_actions_task(
        self,
        request: IoTDescribeAuditMitigationActionsTaskRequest,
    ) -> IoTDescribeAuditMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_audit_mitigation_actions_task, request, IoTDescribeAuditMitigationActionsTaskResponse)

    async def describe_audit_suppression(
        self,
        request: IoTDescribeAuditSuppressionRequest,
    ) -> IoTDescribeAuditSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.describe_audit_suppression, request, IoTDescribeAuditSuppressionResponse)

    async def describe_audit_task(
        self,
        request: IoTDescribeAuditTaskRequest,
    ) -> IoTDescribeAuditTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_audit_task, request, IoTDescribeAuditTaskResponse)

    async def describe_authorizer(
        self,
        request: IoTDescribeAuthorizerRequest,
    ) -> IoTDescribeAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.describe_authorizer, request, IoTDescribeAuthorizerResponse)

    async def describe_billing_group(
        self,
        request: IoTDescribeBillingGroupRequest,
    ) -> IoTDescribeBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_billing_group, request, IoTDescribeBillingGroupResponse)

    async def describe_ca_certificate(
        self,
        request: IoTDescribeCACertificateRequest,
    ) -> IoTDescribeCACertificateResponse:
        client = self._require_client()
        return await self._execute(client.describe_ca_certificate, request, IoTDescribeCACertificateResponse)

    async def describe_certificate(
        self,
        request: IoTDescribeCertificateRequest,
    ) -> IoTDescribeCertificateResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate, request, IoTDescribeCertificateResponse)

    async def describe_certificate_provider(
        self,
        request: IoTDescribeCertificateProviderRequest,
    ) -> IoTDescribeCertificateProviderResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate_provider, request, IoTDescribeCertificateProviderResponse)

    async def describe_custom_metric(
        self,
        request: IoTDescribeCustomMetricRequest,
    ) -> IoTDescribeCustomMetricResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_metric, request, IoTDescribeCustomMetricResponse)

    async def describe_default_authorizer(
        self,
        request: IoTDescribeDefaultAuthorizerRequest | None = None,
    ) -> IoTDescribeDefaultAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.describe_default_authorizer, request, IoTDescribeDefaultAuthorizerResponse)

    async def describe_detect_mitigation_actions_task(
        self,
        request: IoTDescribeDetectMitigationActionsTaskRequest,
    ) -> IoTDescribeDetectMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_detect_mitigation_actions_task, request, IoTDescribeDetectMitigationActionsTaskResponse)

    async def describe_dimension(
        self,
        request: IoTDescribeDimensionRequest,
    ) -> IoTDescribeDimensionResponse:
        client = self._require_client()
        return await self._execute(client.describe_dimension, request, IoTDescribeDimensionResponse)

    async def describe_domain_configuration(
        self,
        request: IoTDescribeDomainConfigurationRequest,
    ) -> IoTDescribeDomainConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_configuration, request, IoTDescribeDomainConfigurationResponse)

    async def describe_encryption_configuration(
        self,
        request: IoTDescribeEncryptionConfigurationRequest | None = None,
    ) -> IoTDescribeEncryptionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_encryption_configuration, request, IoTDescribeEncryptionConfigurationResponse)

    async def describe_endpoint(
        self,
        request: IoTDescribeEndpointRequest | None = None,
    ) -> IoTDescribeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint, request, IoTDescribeEndpointResponse)

    async def describe_event_configurations(
        self,
        request: IoTDescribeEventConfigurationsRequest | None = None,
    ) -> IoTDescribeEventConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_configurations, request, IoTDescribeEventConfigurationsResponse)

    async def describe_fleet_metric(
        self,
        request: IoTDescribeFleetMetricRequest,
    ) -> IoTDescribeFleetMetricResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_metric, request, IoTDescribeFleetMetricResponse)

    async def describe_index(
        self,
        request: IoTDescribeIndexRequest,
    ) -> IoTDescribeIndexResponse:
        client = self._require_client()
        return await self._execute(client.describe_index, request, IoTDescribeIndexResponse)

    async def describe_job(
        self,
        request: IoTDescribeJobRequest,
    ) -> IoTDescribeJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_job, request, IoTDescribeJobResponse)

    async def describe_job_execution(
        self,
        request: IoTDescribeJobExecutionRequest,
    ) -> IoTDescribeJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_execution, request, IoTDescribeJobExecutionResponse)

    async def describe_job_template(
        self,
        request: IoTDescribeJobTemplateRequest,
    ) -> IoTDescribeJobTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_template, request, IoTDescribeJobTemplateResponse)

    async def describe_managed_job_template(
        self,
        request: IoTDescribeManagedJobTemplateRequest,
    ) -> IoTDescribeManagedJobTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_job_template, request, IoTDescribeManagedJobTemplateResponse)

    async def describe_mitigation_action(
        self,
        request: IoTDescribeMitigationActionRequest,
    ) -> IoTDescribeMitigationActionResponse:
        client = self._require_client()
        return await self._execute(client.describe_mitigation_action, request, IoTDescribeMitigationActionResponse)

    async def describe_provisioning_template(
        self,
        request: IoTDescribeProvisioningTemplateRequest,
    ) -> IoTDescribeProvisioningTemplateResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioning_template, request, IoTDescribeProvisioningTemplateResponse)

    async def describe_provisioning_template_version(
        self,
        request: IoTDescribeProvisioningTemplateVersionRequest,
    ) -> IoTDescribeProvisioningTemplateVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioning_template_version, request, IoTDescribeProvisioningTemplateVersionResponse)

    async def describe_role_alias(
        self,
        request: IoTDescribeRoleAliasRequest,
    ) -> IoTDescribeRoleAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_role_alias, request, IoTDescribeRoleAliasResponse)

    async def describe_scheduled_audit(
        self,
        request: IoTDescribeScheduledAuditRequest,
    ) -> IoTDescribeScheduledAuditResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_audit, request, IoTDescribeScheduledAuditResponse)

    async def describe_security_profile(
        self,
        request: IoTDescribeSecurityProfileRequest,
    ) -> IoTDescribeSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_profile, request, IoTDescribeSecurityProfileResponse)

    async def describe_stream(
        self,
        request: IoTDescribeStreamRequest,
    ) -> IoTDescribeStreamResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream, request, IoTDescribeStreamResponse)

    async def describe_thing(
        self,
        request: IoTDescribeThingRequest,
    ) -> IoTDescribeThingResponse:
        client = self._require_client()
        return await self._execute(client.describe_thing, request, IoTDescribeThingResponse)

    async def describe_thing_group(
        self,
        request: IoTDescribeThingGroupRequest,
    ) -> IoTDescribeThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_thing_group, request, IoTDescribeThingGroupResponse)

    async def describe_thing_registration_task(
        self,
        request: IoTDescribeThingRegistrationTaskRequest,
    ) -> IoTDescribeThingRegistrationTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_thing_registration_task, request, IoTDescribeThingRegistrationTaskResponse)

    async def describe_thing_type(
        self,
        request: IoTDescribeThingTypeRequest,
    ) -> IoTDescribeThingTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_thing_type, request, IoTDescribeThingTypeResponse)

    async def detach_policy(
        self,
        request: IoTDetachPolicyRequest,
    ) -> IoTDetachPolicyResponse:
        client = self._require_client()
        return await self._execute(client.detach_policy, request, IoTDetachPolicyResponse)

    async def detach_principal_policy(
        self,
        request: IoTDetachPrincipalPolicyRequest,
    ) -> IoTDetachPrincipalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.detach_principal_policy, request, IoTDetachPrincipalPolicyResponse)

    async def detach_security_profile(
        self,
        request: IoTDetachSecurityProfileRequest,
    ) -> IoTDetachSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.detach_security_profile, request, IoTDetachSecurityProfileResponse)

    async def detach_thing_principal(
        self,
        request: IoTDetachThingPrincipalRequest,
    ) -> IoTDetachThingPrincipalResponse:
        client = self._require_client()
        return await self._execute(client.detach_thing_principal, request, IoTDetachThingPrincipalResponse)

    async def disable_topic_rule(
        self,
        request: IoTDisableTopicRuleRequest,
    ) -> IoTDisableTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.disable_topic_rule, request, IoTDisableTopicRuleResponse)

    async def disassociate_sbom_from_package_version(
        self,
        request: IoTDisassociateSbomFromPackageVersionRequest,
    ) -> IoTDisassociateSbomFromPackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_sbom_from_package_version, request, IoTDisassociateSbomFromPackageVersionResponse)

    async def enable_topic_rule(
        self,
        request: IoTEnableTopicRuleRequest,
    ) -> IoTEnableTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.enable_topic_rule, request, IoTEnableTopicRuleResponse)

    async def get_behavior_model_training_summaries(
        self,
        request: IoTGetBehaviorModelTrainingSummariesRequest | None = None,
    ) -> IoTGetBehaviorModelTrainingSummariesResponse:
        client = self._require_client()
        return await self._execute(client.get_behavior_model_training_summaries, request, IoTGetBehaviorModelTrainingSummariesResponse)

    async def get_behavior_model_training_summaries_paginated(
        self,
        request: IoTGetBehaviorModelTrainingSummariesRequest | None = None,
    ) -> list[IoTGetBehaviorModelTrainingSummariesResponse]:
        return await self._paginate('get_behavior_model_training_summaries', request, IoTGetBehaviorModelTrainingSummariesResponse)

    async def get_buckets_aggregation(
        self,
        request: IoTGetBucketsAggregationRequest,
    ) -> IoTGetBucketsAggregationResponse:
        client = self._require_client()
        return await self._execute(client.get_buckets_aggregation, request, IoTGetBucketsAggregationResponse)

    async def get_cardinality(
        self,
        request: IoTGetCardinalityRequest,
    ) -> IoTGetCardinalityResponse:
        client = self._require_client()
        return await self._execute(client.get_cardinality, request, IoTGetCardinalityResponse)

    async def get_command(
        self,
        request: IoTGetCommandRequest,
    ) -> IoTGetCommandResponse:
        client = self._require_client()
        return await self._execute(client.get_command, request, IoTGetCommandResponse)

    async def get_command_execution(
        self,
        request: IoTGetCommandExecutionRequest,
    ) -> IoTGetCommandExecutionResponse:
        client = self._require_client()
        return await self._execute(client.get_command_execution, request, IoTGetCommandExecutionResponse)

    async def get_effective_policies(
        self,
        request: IoTGetEffectivePoliciesRequest | None = None,
    ) -> IoTGetEffectivePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.get_effective_policies, request, IoTGetEffectivePoliciesResponse)

    async def get_indexing_configuration(
        self,
        request: IoTGetIndexingConfigurationRequest | None = None,
    ) -> IoTGetIndexingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_indexing_configuration, request, IoTGetIndexingConfigurationResponse)

    async def get_job_document(
        self,
        request: IoTGetJobDocumentRequest,
    ) -> IoTGetJobDocumentResponse:
        client = self._require_client()
        return await self._execute(client.get_job_document, request, IoTGetJobDocumentResponse)

    async def get_logging_options(
        self,
        request: IoTGetLoggingOptionsRequest | None = None,
    ) -> IoTGetLoggingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_logging_options, request, IoTGetLoggingOptionsResponse)

    async def get_ota_update(
        self,
        request: IoTGetOTAUpdateRequest,
    ) -> IoTGetOTAUpdateResponse:
        client = self._require_client()
        return await self._execute(client.get_ota_update, request, IoTGetOTAUpdateResponse)

    async def get_package(
        self,
        request: IoTGetPackageRequest,
    ) -> IoTGetPackageResponse:
        client = self._require_client()
        return await self._execute(client.get_package, request, IoTGetPackageResponse)

    async def get_package_configuration(
        self,
        request: IoTGetPackageConfigurationRequest | None = None,
    ) -> IoTGetPackageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_package_configuration, request, IoTGetPackageConfigurationResponse)

    async def get_package_version(
        self,
        request: IoTGetPackageVersionRequest,
    ) -> IoTGetPackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_package_version, request, IoTGetPackageVersionResponse)

    async def get_percentiles(
        self,
        request: IoTGetPercentilesRequest,
    ) -> IoTGetPercentilesResponse:
        client = self._require_client()
        return await self._execute(client.get_percentiles, request, IoTGetPercentilesResponse)

    async def get_policy(
        self,
        request: IoTGetPolicyRequest,
    ) -> IoTGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_policy, request, IoTGetPolicyResponse)

    async def get_policy_version(
        self,
        request: IoTGetPolicyVersionRequest,
    ) -> IoTGetPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_policy_version, request, IoTGetPolicyVersionResponse)

    async def get_registration_code(
        self,
        request: IoTGetRegistrationCodeRequest | None = None,
    ) -> IoTGetRegistrationCodeResponse:
        client = self._require_client()
        return await self._execute(client.get_registration_code, request, IoTGetRegistrationCodeResponse)

    async def get_statistics(
        self,
        request: IoTGetStatisticsRequest,
    ) -> IoTGetStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_statistics, request, IoTGetStatisticsResponse)

    async def get_thing_connectivity_data(
        self,
        request: IoTGetThingConnectivityDataRequest,
    ) -> IoTGetThingConnectivityDataResponse:
        client = self._require_client()
        return await self._execute(client.get_thing_connectivity_data, request, IoTGetThingConnectivityDataResponse)

    async def get_topic_rule(
        self,
        request: IoTGetTopicRuleRequest,
    ) -> IoTGetTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_topic_rule, request, IoTGetTopicRuleResponse)

    async def get_topic_rule_destination(
        self,
        request: IoTGetTopicRuleDestinationRequest,
    ) -> IoTGetTopicRuleDestinationResponse:
        client = self._require_client()
        return await self._execute(client.get_topic_rule_destination, request, IoTGetTopicRuleDestinationResponse)

    async def get_v2_logging_options(
        self,
        request: IoTGetV2LoggingOptionsRequest | None = None,
    ) -> IoTGetV2LoggingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_v2_logging_options, request, IoTGetV2LoggingOptionsResponse)

    async def list_active_violations(
        self,
        request: IoTListActiveViolationsRequest | None = None,
    ) -> IoTListActiveViolationsResponse:
        client = self._require_client()
        return await self._execute(client.list_active_violations, request, IoTListActiveViolationsResponse)

    async def list_active_violations_paginated(
        self,
        request: IoTListActiveViolationsRequest | None = None,
    ) -> list[IoTListActiveViolationsResponse]:
        return await self._paginate('list_active_violations', request, IoTListActiveViolationsResponse)

    async def list_attached_policies(
        self,
        request: IoTListAttachedPoliciesRequest,
    ) -> IoTListAttachedPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_attached_policies, request, IoTListAttachedPoliciesResponse)

    async def list_attached_policies_paginated(
        self,
        request: IoTListAttachedPoliciesRequest,
    ) -> list[IoTListAttachedPoliciesResponse]:
        return await self._paginate('list_attached_policies', request, IoTListAttachedPoliciesResponse)

    async def list_audit_findings(
        self,
        request: IoTListAuditFindingsRequest | None = None,
    ) -> IoTListAuditFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_audit_findings, request, IoTListAuditFindingsResponse)

    async def list_audit_findings_paginated(
        self,
        request: IoTListAuditFindingsRequest | None = None,
    ) -> list[IoTListAuditFindingsResponse]:
        return await self._paginate('list_audit_findings', request, IoTListAuditFindingsResponse)

    async def list_audit_mitigation_actions_executions(
        self,
        request: IoTListAuditMitigationActionsExecutionsRequest,
    ) -> IoTListAuditMitigationActionsExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_audit_mitigation_actions_executions, request, IoTListAuditMitigationActionsExecutionsResponse)

    async def list_audit_mitigation_actions_executions_paginated(
        self,
        request: IoTListAuditMitigationActionsExecutionsRequest,
    ) -> list[IoTListAuditMitigationActionsExecutionsResponse]:
        return await self._paginate('list_audit_mitigation_actions_executions', request, IoTListAuditMitigationActionsExecutionsResponse)

    async def list_audit_mitigation_actions_tasks(
        self,
        request: IoTListAuditMitigationActionsTasksRequest,
    ) -> IoTListAuditMitigationActionsTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_audit_mitigation_actions_tasks, request, IoTListAuditMitigationActionsTasksResponse)

    async def list_audit_mitigation_actions_tasks_paginated(
        self,
        request: IoTListAuditMitigationActionsTasksRequest,
    ) -> list[IoTListAuditMitigationActionsTasksResponse]:
        return await self._paginate('list_audit_mitigation_actions_tasks', request, IoTListAuditMitigationActionsTasksResponse)

    async def list_audit_suppressions(
        self,
        request: IoTListAuditSuppressionsRequest | None = None,
    ) -> IoTListAuditSuppressionsResponse:
        client = self._require_client()
        return await self._execute(client.list_audit_suppressions, request, IoTListAuditSuppressionsResponse)

    async def list_audit_suppressions_paginated(
        self,
        request: IoTListAuditSuppressionsRequest | None = None,
    ) -> list[IoTListAuditSuppressionsResponse]:
        return await self._paginate('list_audit_suppressions', request, IoTListAuditSuppressionsResponse)

    async def list_audit_tasks(
        self,
        request: IoTListAuditTasksRequest,
    ) -> IoTListAuditTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_audit_tasks, request, IoTListAuditTasksResponse)

    async def list_audit_tasks_paginated(
        self,
        request: IoTListAuditTasksRequest,
    ) -> list[IoTListAuditTasksResponse]:
        return await self._paginate('list_audit_tasks', request, IoTListAuditTasksResponse)

    async def list_authorizers(
        self,
        request: IoTListAuthorizersRequest | None = None,
    ) -> IoTListAuthorizersResponse:
        client = self._require_client()
        return await self._execute(client.list_authorizers, request, IoTListAuthorizersResponse)

    async def list_authorizers_paginated(
        self,
        request: IoTListAuthorizersRequest | None = None,
    ) -> list[IoTListAuthorizersResponse]:
        return await self._paginate('list_authorizers', request, IoTListAuthorizersResponse)

    async def list_billing_groups(
        self,
        request: IoTListBillingGroupsRequest | None = None,
    ) -> IoTListBillingGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_billing_groups, request, IoTListBillingGroupsResponse)

    async def list_billing_groups_paginated(
        self,
        request: IoTListBillingGroupsRequest | None = None,
    ) -> list[IoTListBillingGroupsResponse]:
        return await self._paginate('list_billing_groups', request, IoTListBillingGroupsResponse)

    async def list_ca_certificates(
        self,
        request: IoTListCACertificatesRequest | None = None,
    ) -> IoTListCACertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_ca_certificates, request, IoTListCACertificatesResponse)

    async def list_ca_certificates_paginated(
        self,
        request: IoTListCACertificatesRequest | None = None,
    ) -> list[IoTListCACertificatesResponse]:
        return await self._paginate('list_ca_certificates', request, IoTListCACertificatesResponse)

    async def list_certificate_providers(
        self,
        request: IoTListCertificateProvidersRequest | None = None,
    ) -> IoTListCertificateProvidersResponse:
        client = self._require_client()
        return await self._execute(client.list_certificate_providers, request, IoTListCertificateProvidersResponse)

    async def list_certificates(
        self,
        request: IoTListCertificatesRequest | None = None,
    ) -> IoTListCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_certificates, request, IoTListCertificatesResponse)

    async def list_certificates_paginated(
        self,
        request: IoTListCertificatesRequest | None = None,
    ) -> list[IoTListCertificatesResponse]:
        return await self._paginate('list_certificates', request, IoTListCertificatesResponse)

    async def list_certificates_by_ca(
        self,
        request: IoTListCertificatesByCARequest,
    ) -> IoTListCertificatesByCAResponse:
        client = self._require_client()
        return await self._execute(client.list_certificates_by_ca, request, IoTListCertificatesByCAResponse)

    async def list_certificates_by_ca_paginated(
        self,
        request: IoTListCertificatesByCARequest,
    ) -> list[IoTListCertificatesByCAResponse]:
        return await self._paginate('list_certificates_by_ca', request, IoTListCertificatesByCAResponse)

    async def list_command_executions(
        self,
        request: IoTListCommandExecutionsRequest | None = None,
    ) -> IoTListCommandExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_command_executions, request, IoTListCommandExecutionsResponse)

    async def list_command_executions_paginated(
        self,
        request: IoTListCommandExecutionsRequest | None = None,
    ) -> list[IoTListCommandExecutionsResponse]:
        return await self._paginate('list_command_executions', request, IoTListCommandExecutionsResponse)

    async def list_commands(
        self,
        request: IoTListCommandsRequest | None = None,
    ) -> IoTListCommandsResponse:
        client = self._require_client()
        return await self._execute(client.list_commands, request, IoTListCommandsResponse)

    async def list_commands_paginated(
        self,
        request: IoTListCommandsRequest | None = None,
    ) -> list[IoTListCommandsResponse]:
        return await self._paginate('list_commands', request, IoTListCommandsResponse)

    async def list_custom_metrics(
        self,
        request: IoTListCustomMetricsRequest | None = None,
    ) -> IoTListCustomMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_metrics, request, IoTListCustomMetricsResponse)

    async def list_custom_metrics_paginated(
        self,
        request: IoTListCustomMetricsRequest | None = None,
    ) -> list[IoTListCustomMetricsResponse]:
        return await self._paginate('list_custom_metrics', request, IoTListCustomMetricsResponse)

    async def list_detect_mitigation_actions_executions(
        self,
        request: IoTListDetectMitigationActionsExecutionsRequest | None = None,
    ) -> IoTListDetectMitigationActionsExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_detect_mitigation_actions_executions, request, IoTListDetectMitigationActionsExecutionsResponse)

    async def list_detect_mitigation_actions_executions_paginated(
        self,
        request: IoTListDetectMitigationActionsExecutionsRequest | None = None,
    ) -> list[IoTListDetectMitigationActionsExecutionsResponse]:
        return await self._paginate('list_detect_mitigation_actions_executions', request, IoTListDetectMitigationActionsExecutionsResponse)

    async def list_detect_mitigation_actions_tasks(
        self,
        request: IoTListDetectMitigationActionsTasksRequest,
    ) -> IoTListDetectMitigationActionsTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_detect_mitigation_actions_tasks, request, IoTListDetectMitigationActionsTasksResponse)

    async def list_detect_mitigation_actions_tasks_paginated(
        self,
        request: IoTListDetectMitigationActionsTasksRequest,
    ) -> list[IoTListDetectMitigationActionsTasksResponse]:
        return await self._paginate('list_detect_mitigation_actions_tasks', request, IoTListDetectMitigationActionsTasksResponse)

    async def list_dimensions(
        self,
        request: IoTListDimensionsRequest | None = None,
    ) -> IoTListDimensionsResponse:
        client = self._require_client()
        return await self._execute(client.list_dimensions, request, IoTListDimensionsResponse)

    async def list_dimensions_paginated(
        self,
        request: IoTListDimensionsRequest | None = None,
    ) -> list[IoTListDimensionsResponse]:
        return await self._paginate('list_dimensions', request, IoTListDimensionsResponse)

    async def list_domain_configurations(
        self,
        request: IoTListDomainConfigurationsRequest | None = None,
    ) -> IoTListDomainConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_configurations, request, IoTListDomainConfigurationsResponse)

    async def list_domain_configurations_paginated(
        self,
        request: IoTListDomainConfigurationsRequest | None = None,
    ) -> list[IoTListDomainConfigurationsResponse]:
        return await self._paginate('list_domain_configurations', request, IoTListDomainConfigurationsResponse)

    async def list_fleet_metrics(
        self,
        request: IoTListFleetMetricsRequest | None = None,
    ) -> IoTListFleetMetricsResponse:
        client = self._require_client()
        return await self._execute(client.list_fleet_metrics, request, IoTListFleetMetricsResponse)

    async def list_fleet_metrics_paginated(
        self,
        request: IoTListFleetMetricsRequest | None = None,
    ) -> list[IoTListFleetMetricsResponse]:
        return await self._paginate('list_fleet_metrics', request, IoTListFleetMetricsResponse)

    async def list_indices(
        self,
        request: IoTListIndicesRequest | None = None,
    ) -> IoTListIndicesResponse:
        client = self._require_client()
        return await self._execute(client.list_indices, request, IoTListIndicesResponse)

    async def list_indices_paginated(
        self,
        request: IoTListIndicesRequest | None = None,
    ) -> list[IoTListIndicesResponse]:
        return await self._paginate('list_indices', request, IoTListIndicesResponse)

    async def list_job_executions_for_job(
        self,
        request: IoTListJobExecutionsForJobRequest,
    ) -> IoTListJobExecutionsForJobResponse:
        client = self._require_client()
        return await self._execute(client.list_job_executions_for_job, request, IoTListJobExecutionsForJobResponse)

    async def list_job_executions_for_job_paginated(
        self,
        request: IoTListJobExecutionsForJobRequest,
    ) -> list[IoTListJobExecutionsForJobResponse]:
        return await self._paginate('list_job_executions_for_job', request, IoTListJobExecutionsForJobResponse)

    async def list_job_executions_for_thing(
        self,
        request: IoTListJobExecutionsForThingRequest,
    ) -> IoTListJobExecutionsForThingResponse:
        client = self._require_client()
        return await self._execute(client.list_job_executions_for_thing, request, IoTListJobExecutionsForThingResponse)

    async def list_job_executions_for_thing_paginated(
        self,
        request: IoTListJobExecutionsForThingRequest,
    ) -> list[IoTListJobExecutionsForThingResponse]:
        return await self._paginate('list_job_executions_for_thing', request, IoTListJobExecutionsForThingResponse)

    async def list_job_templates(
        self,
        request: IoTListJobTemplatesRequest | None = None,
    ) -> IoTListJobTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_job_templates, request, IoTListJobTemplatesResponse)

    async def list_job_templates_paginated(
        self,
        request: IoTListJobTemplatesRequest | None = None,
    ) -> list[IoTListJobTemplatesResponse]:
        return await self._paginate('list_job_templates', request, IoTListJobTemplatesResponse)

    async def list_jobs(
        self,
        request: IoTListJobsRequest | None = None,
    ) -> IoTListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, IoTListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: IoTListJobsRequest | None = None,
    ) -> list[IoTListJobsResponse]:
        return await self._paginate('list_jobs', request, IoTListJobsResponse)

    async def list_managed_job_templates(
        self,
        request: IoTListManagedJobTemplatesRequest | None = None,
    ) -> IoTListManagedJobTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_managed_job_templates, request, IoTListManagedJobTemplatesResponse)

    async def list_managed_job_templates_paginated(
        self,
        request: IoTListManagedJobTemplatesRequest | None = None,
    ) -> list[IoTListManagedJobTemplatesResponse]:
        return await self._paginate('list_managed_job_templates', request, IoTListManagedJobTemplatesResponse)

    async def list_metric_values(
        self,
        request: IoTListMetricValuesRequest,
    ) -> IoTListMetricValuesResponse:
        client = self._require_client()
        return await self._execute(client.list_metric_values, request, IoTListMetricValuesResponse)

    async def list_metric_values_paginated(
        self,
        request: IoTListMetricValuesRequest,
    ) -> list[IoTListMetricValuesResponse]:
        return await self._paginate('list_metric_values', request, IoTListMetricValuesResponse)

    async def list_mitigation_actions(
        self,
        request: IoTListMitigationActionsRequest | None = None,
    ) -> IoTListMitigationActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_mitigation_actions, request, IoTListMitigationActionsResponse)

    async def list_mitigation_actions_paginated(
        self,
        request: IoTListMitigationActionsRequest | None = None,
    ) -> list[IoTListMitigationActionsResponse]:
        return await self._paginate('list_mitigation_actions', request, IoTListMitigationActionsResponse)

    async def list_ota_updates(
        self,
        request: IoTListOTAUpdatesRequest | None = None,
    ) -> IoTListOTAUpdatesResponse:
        client = self._require_client()
        return await self._execute(client.list_ota_updates, request, IoTListOTAUpdatesResponse)

    async def list_ota_updates_paginated(
        self,
        request: IoTListOTAUpdatesRequest | None = None,
    ) -> list[IoTListOTAUpdatesResponse]:
        return await self._paginate('list_ota_updates', request, IoTListOTAUpdatesResponse)

    async def list_outgoing_certificates(
        self,
        request: IoTListOutgoingCertificatesRequest | None = None,
    ) -> IoTListOutgoingCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_outgoing_certificates, request, IoTListOutgoingCertificatesResponse)

    async def list_outgoing_certificates_paginated(
        self,
        request: IoTListOutgoingCertificatesRequest | None = None,
    ) -> list[IoTListOutgoingCertificatesResponse]:
        return await self._paginate('list_outgoing_certificates', request, IoTListOutgoingCertificatesResponse)

    async def list_package_versions(
        self,
        request: IoTListPackageVersionsRequest,
    ) -> IoTListPackageVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_package_versions, request, IoTListPackageVersionsResponse)

    async def list_package_versions_paginated(
        self,
        request: IoTListPackageVersionsRequest,
    ) -> list[IoTListPackageVersionsResponse]:
        return await self._paginate('list_package_versions', request, IoTListPackageVersionsResponse)

    async def list_packages(
        self,
        request: IoTListPackagesRequest | None = None,
    ) -> IoTListPackagesResponse:
        client = self._require_client()
        return await self._execute(client.list_packages, request, IoTListPackagesResponse)

    async def list_packages_paginated(
        self,
        request: IoTListPackagesRequest | None = None,
    ) -> list[IoTListPackagesResponse]:
        return await self._paginate('list_packages', request, IoTListPackagesResponse)

    async def list_policies(
        self,
        request: IoTListPoliciesRequest | None = None,
    ) -> IoTListPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_policies, request, IoTListPoliciesResponse)

    async def list_policies_paginated(
        self,
        request: IoTListPoliciesRequest | None = None,
    ) -> list[IoTListPoliciesResponse]:
        return await self._paginate('list_policies', request, IoTListPoliciesResponse)

    async def list_policy_principals(
        self,
        request: IoTListPolicyPrincipalsRequest,
    ) -> IoTListPolicyPrincipalsResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_principals, request, IoTListPolicyPrincipalsResponse)

    async def list_policy_principals_paginated(
        self,
        request: IoTListPolicyPrincipalsRequest,
    ) -> list[IoTListPolicyPrincipalsResponse]:
        return await self._paginate('list_policy_principals', request, IoTListPolicyPrincipalsResponse)

    async def list_policy_versions(
        self,
        request: IoTListPolicyVersionsRequest,
    ) -> IoTListPolicyVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_versions, request, IoTListPolicyVersionsResponse)

    async def list_principal_policies(
        self,
        request: IoTListPrincipalPoliciesRequest,
    ) -> IoTListPrincipalPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_principal_policies, request, IoTListPrincipalPoliciesResponse)

    async def list_principal_policies_paginated(
        self,
        request: IoTListPrincipalPoliciesRequest,
    ) -> list[IoTListPrincipalPoliciesResponse]:
        return await self._paginate('list_principal_policies', request, IoTListPrincipalPoliciesResponse)

    async def list_principal_things(
        self,
        request: IoTListPrincipalThingsRequest,
    ) -> IoTListPrincipalThingsResponse:
        client = self._require_client()
        return await self._execute(client.list_principal_things, request, IoTListPrincipalThingsResponse)

    async def list_principal_things_paginated(
        self,
        request: IoTListPrincipalThingsRequest,
    ) -> list[IoTListPrincipalThingsResponse]:
        return await self._paginate('list_principal_things', request, IoTListPrincipalThingsResponse)

    async def list_principal_things_v2(
        self,
        request: IoTListPrincipalThingsV2Request,
    ) -> IoTListPrincipalThingsV2Response:
        client = self._require_client()
        return await self._execute(client.list_principal_things_v2, request, IoTListPrincipalThingsV2Response)

    async def list_principal_things_v2_paginated(
        self,
        request: IoTListPrincipalThingsV2Request,
    ) -> list[IoTListPrincipalThingsV2Response]:
        return await self._paginate('list_principal_things_v2', request, IoTListPrincipalThingsV2Response)

    async def list_provisioning_template_versions(
        self,
        request: IoTListProvisioningTemplateVersionsRequest,
    ) -> IoTListProvisioningTemplateVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioning_template_versions, request, IoTListProvisioningTemplateVersionsResponse)

    async def list_provisioning_template_versions_paginated(
        self,
        request: IoTListProvisioningTemplateVersionsRequest,
    ) -> list[IoTListProvisioningTemplateVersionsResponse]:
        return await self._paginate('list_provisioning_template_versions', request, IoTListProvisioningTemplateVersionsResponse)

    async def list_provisioning_templates(
        self,
        request: IoTListProvisioningTemplatesRequest | None = None,
    ) -> IoTListProvisioningTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioning_templates, request, IoTListProvisioningTemplatesResponse)

    async def list_provisioning_templates_paginated(
        self,
        request: IoTListProvisioningTemplatesRequest | None = None,
    ) -> list[IoTListProvisioningTemplatesResponse]:
        return await self._paginate('list_provisioning_templates', request, IoTListProvisioningTemplatesResponse)

    async def list_related_resources_for_audit_finding(
        self,
        request: IoTListRelatedResourcesForAuditFindingRequest,
    ) -> IoTListRelatedResourcesForAuditFindingResponse:
        client = self._require_client()
        return await self._execute(client.list_related_resources_for_audit_finding, request, IoTListRelatedResourcesForAuditFindingResponse)

    async def list_related_resources_for_audit_finding_paginated(
        self,
        request: IoTListRelatedResourcesForAuditFindingRequest,
    ) -> list[IoTListRelatedResourcesForAuditFindingResponse]:
        return await self._paginate('list_related_resources_for_audit_finding', request, IoTListRelatedResourcesForAuditFindingResponse)

    async def list_role_aliases(
        self,
        request: IoTListRoleAliasesRequest | None = None,
    ) -> IoTListRoleAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_role_aliases, request, IoTListRoleAliasesResponse)

    async def list_role_aliases_paginated(
        self,
        request: IoTListRoleAliasesRequest | None = None,
    ) -> list[IoTListRoleAliasesResponse]:
        return await self._paginate('list_role_aliases', request, IoTListRoleAliasesResponse)

    async def list_sbom_validation_results(
        self,
        request: IoTListSbomValidationResultsRequest,
    ) -> IoTListSbomValidationResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_sbom_validation_results, request, IoTListSbomValidationResultsResponse)

    async def list_sbom_validation_results_paginated(
        self,
        request: IoTListSbomValidationResultsRequest,
    ) -> list[IoTListSbomValidationResultsResponse]:
        return await self._paginate('list_sbom_validation_results', request, IoTListSbomValidationResultsResponse)

    async def list_scheduled_audits(
        self,
        request: IoTListScheduledAuditsRequest | None = None,
    ) -> IoTListScheduledAuditsResponse:
        client = self._require_client()
        return await self._execute(client.list_scheduled_audits, request, IoTListScheduledAuditsResponse)

    async def list_scheduled_audits_paginated(
        self,
        request: IoTListScheduledAuditsRequest | None = None,
    ) -> list[IoTListScheduledAuditsResponse]:
        return await self._paginate('list_scheduled_audits', request, IoTListScheduledAuditsResponse)

    async def list_security_profiles(
        self,
        request: IoTListSecurityProfilesRequest | None = None,
    ) -> IoTListSecurityProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profiles, request, IoTListSecurityProfilesResponse)

    async def list_security_profiles_paginated(
        self,
        request: IoTListSecurityProfilesRequest | None = None,
    ) -> list[IoTListSecurityProfilesResponse]:
        return await self._paginate('list_security_profiles', request, IoTListSecurityProfilesResponse)

    async def list_security_profiles_for_target(
        self,
        request: IoTListSecurityProfilesForTargetRequest,
    ) -> IoTListSecurityProfilesForTargetResponse:
        client = self._require_client()
        return await self._execute(client.list_security_profiles_for_target, request, IoTListSecurityProfilesForTargetResponse)

    async def list_security_profiles_for_target_paginated(
        self,
        request: IoTListSecurityProfilesForTargetRequest,
    ) -> list[IoTListSecurityProfilesForTargetResponse]:
        return await self._paginate('list_security_profiles_for_target', request, IoTListSecurityProfilesForTargetResponse)

    async def list_streams(
        self,
        request: IoTListStreamsRequest | None = None,
    ) -> IoTListStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_streams, request, IoTListStreamsResponse)

    async def list_streams_paginated(
        self,
        request: IoTListStreamsRequest | None = None,
    ) -> list[IoTListStreamsResponse]:
        return await self._paginate('list_streams', request, IoTListStreamsResponse)

    async def list_tags_for_resource(
        self,
        request: IoTListTagsForResourceRequest,
    ) -> IoTListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, IoTListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: IoTListTagsForResourceRequest,
    ) -> list[IoTListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, IoTListTagsForResourceResponse)

    async def list_targets_for_policy(
        self,
        request: IoTListTargetsForPolicyRequest,
    ) -> IoTListTargetsForPolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_targets_for_policy, request, IoTListTargetsForPolicyResponse)

    async def list_targets_for_policy_paginated(
        self,
        request: IoTListTargetsForPolicyRequest,
    ) -> list[IoTListTargetsForPolicyResponse]:
        return await self._paginate('list_targets_for_policy', request, IoTListTargetsForPolicyResponse)

    async def list_targets_for_security_profile(
        self,
        request: IoTListTargetsForSecurityProfileRequest,
    ) -> IoTListTargetsForSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.list_targets_for_security_profile, request, IoTListTargetsForSecurityProfileResponse)

    async def list_targets_for_security_profile_paginated(
        self,
        request: IoTListTargetsForSecurityProfileRequest,
    ) -> list[IoTListTargetsForSecurityProfileResponse]:
        return await self._paginate('list_targets_for_security_profile', request, IoTListTargetsForSecurityProfileResponse)

    async def list_thing_groups(
        self,
        request: IoTListThingGroupsRequest | None = None,
    ) -> IoTListThingGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_groups, request, IoTListThingGroupsResponse)

    async def list_thing_groups_paginated(
        self,
        request: IoTListThingGroupsRequest | None = None,
    ) -> list[IoTListThingGroupsResponse]:
        return await self._paginate('list_thing_groups', request, IoTListThingGroupsResponse)

    async def list_thing_groups_for_thing(
        self,
        request: IoTListThingGroupsForThingRequest,
    ) -> IoTListThingGroupsForThingResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_groups_for_thing, request, IoTListThingGroupsForThingResponse)

    async def list_thing_groups_for_thing_paginated(
        self,
        request: IoTListThingGroupsForThingRequest,
    ) -> list[IoTListThingGroupsForThingResponse]:
        return await self._paginate('list_thing_groups_for_thing', request, IoTListThingGroupsForThingResponse)

    async def list_thing_principals(
        self,
        request: IoTListThingPrincipalsRequest,
    ) -> IoTListThingPrincipalsResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_principals, request, IoTListThingPrincipalsResponse)

    async def list_thing_principals_paginated(
        self,
        request: IoTListThingPrincipalsRequest,
    ) -> list[IoTListThingPrincipalsResponse]:
        return await self._paginate('list_thing_principals', request, IoTListThingPrincipalsResponse)

    async def list_thing_principals_v2(
        self,
        request: IoTListThingPrincipalsV2Request,
    ) -> IoTListThingPrincipalsV2Response:
        client = self._require_client()
        return await self._execute(client.list_thing_principals_v2, request, IoTListThingPrincipalsV2Response)

    async def list_thing_principals_v2_paginated(
        self,
        request: IoTListThingPrincipalsV2Request,
    ) -> list[IoTListThingPrincipalsV2Response]:
        return await self._paginate('list_thing_principals_v2', request, IoTListThingPrincipalsV2Response)

    async def list_thing_registration_task_reports(
        self,
        request: IoTListThingRegistrationTaskReportsRequest,
    ) -> IoTListThingRegistrationTaskReportsResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_registration_task_reports, request, IoTListThingRegistrationTaskReportsResponse)

    async def list_thing_registration_task_reports_paginated(
        self,
        request: IoTListThingRegistrationTaskReportsRequest,
    ) -> list[IoTListThingRegistrationTaskReportsResponse]:
        return await self._paginate('list_thing_registration_task_reports', request, IoTListThingRegistrationTaskReportsResponse)

    async def list_thing_registration_tasks(
        self,
        request: IoTListThingRegistrationTasksRequest | None = None,
    ) -> IoTListThingRegistrationTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_registration_tasks, request, IoTListThingRegistrationTasksResponse)

    async def list_thing_registration_tasks_paginated(
        self,
        request: IoTListThingRegistrationTasksRequest | None = None,
    ) -> list[IoTListThingRegistrationTasksResponse]:
        return await self._paginate('list_thing_registration_tasks', request, IoTListThingRegistrationTasksResponse)

    async def list_thing_types(
        self,
        request: IoTListThingTypesRequest | None = None,
    ) -> IoTListThingTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_thing_types, request, IoTListThingTypesResponse)

    async def list_thing_types_paginated(
        self,
        request: IoTListThingTypesRequest | None = None,
    ) -> list[IoTListThingTypesResponse]:
        return await self._paginate('list_thing_types', request, IoTListThingTypesResponse)

    async def list_things(
        self,
        request: IoTListThingsRequest | None = None,
    ) -> IoTListThingsResponse:
        client = self._require_client()
        return await self._execute(client.list_things, request, IoTListThingsResponse)

    async def list_things_paginated(
        self,
        request: IoTListThingsRequest | None = None,
    ) -> list[IoTListThingsResponse]:
        return await self._paginate('list_things', request, IoTListThingsResponse)

    async def list_things_in_billing_group(
        self,
        request: IoTListThingsInBillingGroupRequest,
    ) -> IoTListThingsInBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_things_in_billing_group, request, IoTListThingsInBillingGroupResponse)

    async def list_things_in_billing_group_paginated(
        self,
        request: IoTListThingsInBillingGroupRequest,
    ) -> list[IoTListThingsInBillingGroupResponse]:
        return await self._paginate('list_things_in_billing_group', request, IoTListThingsInBillingGroupResponse)

    async def list_things_in_thing_group(
        self,
        request: IoTListThingsInThingGroupRequest,
    ) -> IoTListThingsInThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_things_in_thing_group, request, IoTListThingsInThingGroupResponse)

    async def list_things_in_thing_group_paginated(
        self,
        request: IoTListThingsInThingGroupRequest,
    ) -> list[IoTListThingsInThingGroupResponse]:
        return await self._paginate('list_things_in_thing_group', request, IoTListThingsInThingGroupResponse)

    async def list_topic_rule_destinations(
        self,
        request: IoTListTopicRuleDestinationsRequest | None = None,
    ) -> IoTListTopicRuleDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.list_topic_rule_destinations, request, IoTListTopicRuleDestinationsResponse)

    async def list_topic_rule_destinations_paginated(
        self,
        request: IoTListTopicRuleDestinationsRequest | None = None,
    ) -> list[IoTListTopicRuleDestinationsResponse]:
        return await self._paginate('list_topic_rule_destinations', request, IoTListTopicRuleDestinationsResponse)

    async def list_topic_rules(
        self,
        request: IoTListTopicRulesRequest | None = None,
    ) -> IoTListTopicRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_topic_rules, request, IoTListTopicRulesResponse)

    async def list_topic_rules_paginated(
        self,
        request: IoTListTopicRulesRequest | None = None,
    ) -> list[IoTListTopicRulesResponse]:
        return await self._paginate('list_topic_rules', request, IoTListTopicRulesResponse)

    async def list_v2_logging_levels(
        self,
        request: IoTListV2LoggingLevelsRequest | None = None,
    ) -> IoTListV2LoggingLevelsResponse:
        client = self._require_client()
        return await self._execute(client.list_v2_logging_levels, request, IoTListV2LoggingLevelsResponse)

    async def list_v2_logging_levels_paginated(
        self,
        request: IoTListV2LoggingLevelsRequest | None = None,
    ) -> list[IoTListV2LoggingLevelsResponse]:
        return await self._paginate('list_v2_logging_levels', request, IoTListV2LoggingLevelsResponse)

    async def list_violation_events(
        self,
        request: IoTListViolationEventsRequest,
    ) -> IoTListViolationEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_violation_events, request, IoTListViolationEventsResponse)

    async def list_violation_events_paginated(
        self,
        request: IoTListViolationEventsRequest,
    ) -> list[IoTListViolationEventsResponse]:
        return await self._paginate('list_violation_events', request, IoTListViolationEventsResponse)

    async def put_verification_state_on_violation(
        self,
        request: IoTPutVerificationStateOnViolationRequest,
    ) -> IoTPutVerificationStateOnViolationResponse:
        client = self._require_client()
        return await self._execute(client.put_verification_state_on_violation, request, IoTPutVerificationStateOnViolationResponse)

    async def register_ca_certificate(
        self,
        request: IoTRegisterCACertificateRequest,
    ) -> IoTRegisterCACertificateResponse:
        client = self._require_client()
        return await self._execute(client.register_ca_certificate, request, IoTRegisterCACertificateResponse)

    async def register_certificate(
        self,
        request: IoTRegisterCertificateRequest,
    ) -> IoTRegisterCertificateResponse:
        client = self._require_client()
        return await self._execute(client.register_certificate, request, IoTRegisterCertificateResponse)

    async def register_certificate_without_ca(
        self,
        request: IoTRegisterCertificateWithoutCARequest,
    ) -> IoTRegisterCertificateWithoutCAResponse:
        client = self._require_client()
        return await self._execute(client.register_certificate_without_ca, request, IoTRegisterCertificateWithoutCAResponse)

    async def register_thing(
        self,
        request: IoTRegisterThingRequest,
    ) -> IoTRegisterThingResponse:
        client = self._require_client()
        return await self._execute(client.register_thing, request, IoTRegisterThingResponse)

    async def reject_certificate_transfer(
        self,
        request: IoTRejectCertificateTransferRequest,
    ) -> IoTRejectCertificateTransferResponse:
        client = self._require_client()
        return await self._execute(client.reject_certificate_transfer, request, IoTRejectCertificateTransferResponse)

    async def remove_thing_from_billing_group(
        self,
        request: IoTRemoveThingFromBillingGroupRequest | None = None,
    ) -> IoTRemoveThingFromBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.remove_thing_from_billing_group, request, IoTRemoveThingFromBillingGroupResponse)

    async def remove_thing_from_thing_group(
        self,
        request: IoTRemoveThingFromThingGroupRequest | None = None,
    ) -> IoTRemoveThingFromThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.remove_thing_from_thing_group, request, IoTRemoveThingFromThingGroupResponse)

    async def replace_topic_rule(
        self,
        request: IoTReplaceTopicRuleRequest,
    ) -> IoTReplaceTopicRuleResponse:
        client = self._require_client()
        return await self._execute(client.replace_topic_rule, request, IoTReplaceTopicRuleResponse)

    async def search_index(
        self,
        request: IoTSearchIndexRequest,
    ) -> IoTSearchIndexResponse:
        client = self._require_client()
        return await self._execute(client.search_index, request, IoTSearchIndexResponse)

    async def set_default_authorizer(
        self,
        request: IoTSetDefaultAuthorizerRequest,
    ) -> IoTSetDefaultAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.set_default_authorizer, request, IoTSetDefaultAuthorizerResponse)

    async def set_default_policy_version(
        self,
        request: IoTSetDefaultPolicyVersionRequest,
    ) -> IoTSetDefaultPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.set_default_policy_version, request, IoTSetDefaultPolicyVersionResponse)

    async def set_logging_options(
        self,
        request: IoTSetLoggingOptionsRequest,
    ) -> IoTSetLoggingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.set_logging_options, request, IoTSetLoggingOptionsResponse)

    async def set_v2_logging_level(
        self,
        request: IoTSetV2LoggingLevelRequest,
    ) -> IoTSetV2LoggingLevelResponse:
        client = self._require_client()
        return await self._execute(client.set_v2_logging_level, request, IoTSetV2LoggingLevelResponse)

    async def set_v2_logging_options(
        self,
        request: IoTSetV2LoggingOptionsRequest | None = None,
    ) -> IoTSetV2LoggingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.set_v2_logging_options, request, IoTSetV2LoggingOptionsResponse)

    async def start_audit_mitigation_actions_task(
        self,
        request: IoTStartAuditMitigationActionsTaskRequest,
    ) -> IoTStartAuditMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_audit_mitigation_actions_task, request, IoTStartAuditMitigationActionsTaskResponse)

    async def start_detect_mitigation_actions_task(
        self,
        request: IoTStartDetectMitigationActionsTaskRequest,
    ) -> IoTStartDetectMitigationActionsTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_detect_mitigation_actions_task, request, IoTStartDetectMitigationActionsTaskResponse)

    async def start_on_demand_audit_task(
        self,
        request: IoTStartOnDemandAuditTaskRequest,
    ) -> IoTStartOnDemandAuditTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_on_demand_audit_task, request, IoTStartOnDemandAuditTaskResponse)

    async def start_thing_registration_task(
        self,
        request: IoTStartThingRegistrationTaskRequest,
    ) -> IoTStartThingRegistrationTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_thing_registration_task, request, IoTStartThingRegistrationTaskResponse)

    async def stop_thing_registration_task(
        self,
        request: IoTStopThingRegistrationTaskRequest,
    ) -> IoTStopThingRegistrationTaskResponse:
        client = self._require_client()
        return await self._execute(client.stop_thing_registration_task, request, IoTStopThingRegistrationTaskResponse)

    async def tag_resource(
        self,
        request: IoTTagResourceRequest,
    ) -> IoTTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, IoTTagResourceResponse)

    async def test_authorization(
        self,
        request: IoTTestAuthorizationRequest,
    ) -> IoTTestAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.test_authorization, request, IoTTestAuthorizationResponse)

    async def test_invoke_authorizer(
        self,
        request: IoTTestInvokeAuthorizerRequest,
    ) -> IoTTestInvokeAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.test_invoke_authorizer, request, IoTTestInvokeAuthorizerResponse)

    async def transfer_certificate(
        self,
        request: IoTTransferCertificateRequest,
    ) -> IoTTransferCertificateResponse:
        client = self._require_client()
        return await self._execute(client.transfer_certificate, request, IoTTransferCertificateResponse)

    async def untag_resource(
        self,
        request: IoTUntagResourceRequest,
    ) -> IoTUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, IoTUntagResourceResponse)

    async def update_account_audit_configuration(
        self,
        request: IoTUpdateAccountAuditConfigurationRequest | None = None,
    ) -> IoTUpdateAccountAuditConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_account_audit_configuration, request, IoTUpdateAccountAuditConfigurationResponse)

    async def update_audit_suppression(
        self,
        request: IoTUpdateAuditSuppressionRequest,
    ) -> IoTUpdateAuditSuppressionResponse:
        client = self._require_client()
        return await self._execute(client.update_audit_suppression, request, IoTUpdateAuditSuppressionResponse)

    async def update_authorizer(
        self,
        request: IoTUpdateAuthorizerRequest,
    ) -> IoTUpdateAuthorizerResponse:
        client = self._require_client()
        return await self._execute(client.update_authorizer, request, IoTUpdateAuthorizerResponse)

    async def update_billing_group(
        self,
        request: IoTUpdateBillingGroupRequest,
    ) -> IoTUpdateBillingGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_billing_group, request, IoTUpdateBillingGroupResponse)

    async def update_ca_certificate(
        self,
        request: IoTUpdateCACertificateRequest,
    ) -> IoTUpdateCACertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_ca_certificate, request, IoTUpdateCACertificateResponse)

    async def update_certificate(
        self,
        request: IoTUpdateCertificateRequest,
    ) -> IoTUpdateCertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_certificate, request, IoTUpdateCertificateResponse)

    async def update_certificate_provider(
        self,
        request: IoTUpdateCertificateProviderRequest,
    ) -> IoTUpdateCertificateProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_certificate_provider, request, IoTUpdateCertificateProviderResponse)

    async def update_command(
        self,
        request: IoTUpdateCommandRequest,
    ) -> IoTUpdateCommandResponse:
        client = self._require_client()
        return await self._execute(client.update_command, request, IoTUpdateCommandResponse)

    async def update_custom_metric(
        self,
        request: IoTUpdateCustomMetricRequest,
    ) -> IoTUpdateCustomMetricResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_metric, request, IoTUpdateCustomMetricResponse)

    async def update_dimension(
        self,
        request: IoTUpdateDimensionRequest,
    ) -> IoTUpdateDimensionResponse:
        client = self._require_client()
        return await self._execute(client.update_dimension, request, IoTUpdateDimensionResponse)

    async def update_domain_configuration(
        self,
        request: IoTUpdateDomainConfigurationRequest,
    ) -> IoTUpdateDomainConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_configuration, request, IoTUpdateDomainConfigurationResponse)

    async def update_dynamic_thing_group(
        self,
        request: IoTUpdateDynamicThingGroupRequest,
    ) -> IoTUpdateDynamicThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_dynamic_thing_group, request, IoTUpdateDynamicThingGroupResponse)

    async def update_encryption_configuration(
        self,
        request: IoTUpdateEncryptionConfigurationRequest,
    ) -> IoTUpdateEncryptionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_encryption_configuration, request, IoTUpdateEncryptionConfigurationResponse)

    async def update_event_configurations(
        self,
        request: IoTUpdateEventConfigurationsRequest | None = None,
    ) -> IoTUpdateEventConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.update_event_configurations, request, IoTUpdateEventConfigurationsResponse)

    async def update_fleet_metric(
        self,
        request: IoTUpdateFleetMetricRequest,
    ) -> IoTUpdateFleetMetricResponse:
        client = self._require_client()
        return await self._execute(client.update_fleet_metric, request, IoTUpdateFleetMetricResponse)

    async def update_indexing_configuration(
        self,
        request: IoTUpdateIndexingConfigurationRequest | None = None,
    ) -> IoTUpdateIndexingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_indexing_configuration, request, IoTUpdateIndexingConfigurationResponse)

    async def update_job(
        self,
        request: IoTUpdateJobRequest,
    ) -> IoTUpdateJobResponse:
        client = self._require_client()
        return await self._execute(client.update_job, request, IoTUpdateJobResponse)

    async def update_mitigation_action(
        self,
        request: IoTUpdateMitigationActionRequest,
    ) -> IoTUpdateMitigationActionResponse:
        client = self._require_client()
        return await self._execute(client.update_mitigation_action, request, IoTUpdateMitigationActionResponse)

    async def update_package(
        self,
        request: IoTUpdatePackageRequest,
    ) -> IoTUpdatePackageResponse:
        client = self._require_client()
        return await self._execute(client.update_package, request, IoTUpdatePackageResponse)

    async def update_package_configuration(
        self,
        request: IoTUpdatePackageConfigurationRequest | None = None,
    ) -> IoTUpdatePackageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_package_configuration, request, IoTUpdatePackageConfigurationResponse)

    async def update_package_version(
        self,
        request: IoTUpdatePackageVersionRequest,
    ) -> IoTUpdatePackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_package_version, request, IoTUpdatePackageVersionResponse)

    async def update_provisioning_template(
        self,
        request: IoTUpdateProvisioningTemplateRequest,
    ) -> IoTUpdateProvisioningTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioning_template, request, IoTUpdateProvisioningTemplateResponse)

    async def update_role_alias(
        self,
        request: IoTUpdateRoleAliasRequest,
    ) -> IoTUpdateRoleAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_role_alias, request, IoTUpdateRoleAliasResponse)

    async def update_scheduled_audit(
        self,
        request: IoTUpdateScheduledAuditRequest,
    ) -> IoTUpdateScheduledAuditResponse:
        client = self._require_client()
        return await self._execute(client.update_scheduled_audit, request, IoTUpdateScheduledAuditResponse)

    async def update_security_profile(
        self,
        request: IoTUpdateSecurityProfileRequest,
    ) -> IoTUpdateSecurityProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_security_profile, request, IoTUpdateSecurityProfileResponse)

    async def update_stream(
        self,
        request: IoTUpdateStreamRequest,
    ) -> IoTUpdateStreamResponse:
        client = self._require_client()
        return await self._execute(client.update_stream, request, IoTUpdateStreamResponse)

    async def update_thing(
        self,
        request: IoTUpdateThingRequest,
    ) -> IoTUpdateThingResponse:
        client = self._require_client()
        return await self._execute(client.update_thing, request, IoTUpdateThingResponse)

    async def update_thing_group(
        self,
        request: IoTUpdateThingGroupRequest,
    ) -> IoTUpdateThingGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_thing_group, request, IoTUpdateThingGroupResponse)

    async def update_thing_groups_for_thing(
        self,
        request: IoTUpdateThingGroupsForThingRequest | None = None,
    ) -> IoTUpdateThingGroupsForThingResponse:
        client = self._require_client()
        return await self._execute(client.update_thing_groups_for_thing, request, IoTUpdateThingGroupsForThingResponse)

    async def update_thing_type(
        self,
        request: IoTUpdateThingTypeRequest,
    ) -> IoTUpdateThingTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_thing_type, request, IoTUpdateThingTypeResponse)

    async def update_topic_rule_destination(
        self,
        request: IoTUpdateTopicRuleDestinationRequest,
    ) -> IoTUpdateTopicRuleDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_topic_rule_destination, request, IoTUpdateTopicRuleDestinationResponse)

    async def validate_security_profile_behaviors(
        self,
        request: IoTValidateSecurityProfileBehaviorsRequest,
    ) -> IoTValidateSecurityProfileBehaviorsResponse:
        client = self._require_client()
        return await self._execute(client.validate_security_profile_behaviors, request, IoTValidateSecurityProfileBehaviorsResponse)
