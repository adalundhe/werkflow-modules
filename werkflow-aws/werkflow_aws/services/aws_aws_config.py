from werkflow_aws.models.aws_config import (
    ConfigServiceAssociateResourceTypesRequest,
    ConfigServiceAssociateResourceTypesResponse,
    ConfigServiceBatchGetAggregateResourceConfigRequest,
    ConfigServiceBatchGetAggregateResourceConfigResponse,
    ConfigServiceBatchGetResourceConfigRequest,
    ConfigServiceBatchGetResourceConfigResponse,
    ConfigServiceDeleteAggregationAuthorizationRequest,
    ConfigServiceDeleteAggregationAuthorizationResponse,
    ConfigServiceDeleteConfigRuleRequest,
    ConfigServiceDeleteConfigRuleResponse,
    ConfigServiceDeleteConfigurationAggregatorRequest,
    ConfigServiceDeleteConfigurationAggregatorResponse,
    ConfigServiceDeleteConfigurationRecorderRequest,
    ConfigServiceDeleteConfigurationRecorderResponse,
    ConfigServiceDeleteConformancePackRequest,
    ConfigServiceDeleteConformancePackResponse,
    ConfigServiceDeleteConnectorRequest,
    ConfigServiceDeleteConnectorResponse,
    ConfigServiceDeleteDeliveryChannelRequest,
    ConfigServiceDeleteDeliveryChannelResponse,
    ConfigServiceDeleteEvaluationResultsRequest,
    ConfigServiceDeleteEvaluationResultsResponse,
    ConfigServiceDeleteOrganizationConfigRuleRequest,
    ConfigServiceDeleteOrganizationConfigRuleResponse,
    ConfigServiceDeleteOrganizationConformancePackRequest,
    ConfigServiceDeleteOrganizationConformancePackResponse,
    ConfigServiceDeletePendingAggregationRequestRequest,
    ConfigServiceDeletePendingAggregationRequestResponse,
    ConfigServiceDeleteRemediationConfigurationRequest,
    ConfigServiceDeleteRemediationConfigurationResponse,
    ConfigServiceDeleteRemediationExceptionsRequest,
    ConfigServiceDeleteRemediationExceptionsResponse,
    ConfigServiceDeleteResourceConfigRequest,
    ConfigServiceDeleteResourceConfigResponse,
    ConfigServiceDeleteRetentionConfigurationRequest,
    ConfigServiceDeleteRetentionConfigurationResponse,
    ConfigServiceDeleteServiceLinkedConfigurationRecorderRequest,
    ConfigServiceDeleteServiceLinkedConfigurationRecorderResponse,
    ConfigServiceDeleteStoredQueryRequest,
    ConfigServiceDeleteStoredQueryResponse,
    ConfigServiceDeliverConfigSnapshotRequest,
    ConfigServiceDeliverConfigSnapshotResponse,
    ConfigServiceDescribeAggregateComplianceByConfigRulesRequest,
    ConfigServiceDescribeAggregateComplianceByConfigRulesResponse,
    ConfigServiceDescribeAggregateComplianceByConformancePacksRequest,
    ConfigServiceDescribeAggregateComplianceByConformancePacksResponse,
    ConfigServiceDescribeAggregationAuthorizationsRequest,
    ConfigServiceDescribeAggregationAuthorizationsResponse,
    ConfigServiceDescribeComplianceByConfigRuleRequest,
    ConfigServiceDescribeComplianceByConfigRuleResponse,
    ConfigServiceDescribeComplianceByResourceRequest,
    ConfigServiceDescribeComplianceByResourceResponse,
    ConfigServiceDescribeConfigRuleEvaluationStatusRequest,
    ConfigServiceDescribeConfigRuleEvaluationStatusResponse,
    ConfigServiceDescribeConfigRulesRequest,
    ConfigServiceDescribeConfigRulesResponse,
    ConfigServiceDescribeConfigurationAggregatorSourcesStatusRequest,
    ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse,
    ConfigServiceDescribeConfigurationAggregatorsRequest,
    ConfigServiceDescribeConfigurationAggregatorsResponse,
    ConfigServiceDescribeConfigurationRecorderStatusRequest,
    ConfigServiceDescribeConfigurationRecorderStatusResponse,
    ConfigServiceDescribeConfigurationRecordersRequest,
    ConfigServiceDescribeConfigurationRecordersResponse,
    ConfigServiceDescribeConformancePackComplianceRequest,
    ConfigServiceDescribeConformancePackComplianceResponse,
    ConfigServiceDescribeConformancePackStatusRequest,
    ConfigServiceDescribeConformancePackStatusResponse,
    ConfigServiceDescribeConformancePacksRequest,
    ConfigServiceDescribeConformancePacksResponse,
    ConfigServiceDescribeDeliveryChannelStatusRequest,
    ConfigServiceDescribeDeliveryChannelStatusResponse,
    ConfigServiceDescribeDeliveryChannelsRequest,
    ConfigServiceDescribeDeliveryChannelsResponse,
    ConfigServiceDescribeOrganizationConfigRuleStatusesRequest,
    ConfigServiceDescribeOrganizationConfigRuleStatusesResponse,
    ConfigServiceDescribeOrganizationConfigRulesRequest,
    ConfigServiceDescribeOrganizationConfigRulesResponse,
    ConfigServiceDescribeOrganizationConformancePackStatusesRequest,
    ConfigServiceDescribeOrganizationConformancePackStatusesResponse,
    ConfigServiceDescribeOrganizationConformancePacksRequest,
    ConfigServiceDescribeOrganizationConformancePacksResponse,
    ConfigServiceDescribePendingAggregationRequestsRequest,
    ConfigServiceDescribePendingAggregationRequestsResponse,
    ConfigServiceDescribeRemediationConfigurationsRequest,
    ConfigServiceDescribeRemediationConfigurationsResponse,
    ConfigServiceDescribeRemediationExceptionsRequest,
    ConfigServiceDescribeRemediationExceptionsResponse,
    ConfigServiceDescribeRemediationExecutionStatusRequest,
    ConfigServiceDescribeRemediationExecutionStatusResponse,
    ConfigServiceDescribeRetentionConfigurationsRequest,
    ConfigServiceDescribeRetentionConfigurationsResponse,
    ConfigServiceDisassociateResourceTypesRequest,
    ConfigServiceDisassociateResourceTypesResponse,
    ConfigServiceGetAggregateComplianceDetailsByConfigRuleRequest,
    ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse,
    ConfigServiceGetAggregateConfigRuleComplianceSummaryRequest,
    ConfigServiceGetAggregateConfigRuleComplianceSummaryResponse,
    ConfigServiceGetAggregateConformancePackComplianceSummaryRequest,
    ConfigServiceGetAggregateConformancePackComplianceSummaryResponse,
    ConfigServiceGetAggregateDiscoveredResourceCountsRequest,
    ConfigServiceGetAggregateDiscoveredResourceCountsResponse,
    ConfigServiceGetAggregateResourceConfigRequest,
    ConfigServiceGetAggregateResourceConfigResponse,
    ConfigServiceGetComplianceDetailsByConfigRuleRequest,
    ConfigServiceGetComplianceDetailsByConfigRuleResponse,
    ConfigServiceGetComplianceDetailsByResourceRequest,
    ConfigServiceGetComplianceDetailsByResourceResponse,
    ConfigServiceGetComplianceSummaryByConfigRuleRequest,
    ConfigServiceGetComplianceSummaryByConfigRuleResponse,
    ConfigServiceGetComplianceSummaryByResourceTypeRequest,
    ConfigServiceGetComplianceSummaryByResourceTypeResponse,
    ConfigServiceGetConformancePackComplianceDetailsRequest,
    ConfigServiceGetConformancePackComplianceDetailsResponse,
    ConfigServiceGetConformancePackComplianceSummaryRequest,
    ConfigServiceGetConformancePackComplianceSummaryResponse,
    ConfigServiceGetConnectorRequest,
    ConfigServiceGetConnectorResponse,
    ConfigServiceGetCustomRulePolicyRequest,
    ConfigServiceGetCustomRulePolicyResponse,
    ConfigServiceGetDiscoveredResourceCountsRequest,
    ConfigServiceGetDiscoveredResourceCountsResponse,
    ConfigServiceGetOrganizationConfigRuleDetailedStatusRequest,
    ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse,
    ConfigServiceGetOrganizationConformancePackDetailedStatusRequest,
    ConfigServiceGetOrganizationConformancePackDetailedStatusResponse,
    ConfigServiceGetOrganizationCustomRulePolicyRequest,
    ConfigServiceGetOrganizationCustomRulePolicyResponse,
    ConfigServiceGetResourceConfigHistoryRequest,
    ConfigServiceGetResourceConfigHistoryResponse,
    ConfigServiceGetResourceEvaluationSummaryRequest,
    ConfigServiceGetResourceEvaluationSummaryResponse,
    ConfigServiceGetStoredQueryRequest,
    ConfigServiceGetStoredQueryResponse,
    ConfigServiceListAggregateDiscoveredResourcesRequest,
    ConfigServiceListAggregateDiscoveredResourcesResponse,
    ConfigServiceListConfigurationRecordersRequest,
    ConfigServiceListConfigurationRecordersResponse,
    ConfigServiceListConformancePackComplianceScoresRequest,
    ConfigServiceListConformancePackComplianceScoresResponse,
    ConfigServiceListConnectorsRequest,
    ConfigServiceListConnectorsResponse,
    ConfigServiceListDiscoveredResourcesRequest,
    ConfigServiceListDiscoveredResourcesResponse,
    ConfigServiceListResourceEvaluationsRequest,
    ConfigServiceListResourceEvaluationsResponse,
    ConfigServiceListStoredQueriesRequest,
    ConfigServiceListStoredQueriesResponse,
    ConfigServiceListTagsForResourceRequest,
    ConfigServiceListTagsForResourceResponse,
    ConfigServicePutAggregationAuthorizationRequest,
    ConfigServicePutAggregationAuthorizationResponse,
    ConfigServicePutConfigRuleRequest,
    ConfigServicePutConfigRuleResponse,
    ConfigServicePutConfigurationAggregatorRequest,
    ConfigServicePutConfigurationAggregatorResponse,
    ConfigServicePutConfigurationRecorderRequest,
    ConfigServicePutConfigurationRecorderResponse,
    ConfigServicePutConformancePackRequest,
    ConfigServicePutConformancePackResponse,
    ConfigServicePutConnectorRequest,
    ConfigServicePutConnectorResponse,
    ConfigServicePutDeliveryChannelRequest,
    ConfigServicePutDeliveryChannelResponse,
    ConfigServicePutEvaluationsRequest,
    ConfigServicePutEvaluationsResponse,
    ConfigServicePutExternalEvaluationRequest,
    ConfigServicePutExternalEvaluationResponse,
    ConfigServicePutOrganizationConfigRuleRequest,
    ConfigServicePutOrganizationConfigRuleResponse,
    ConfigServicePutOrganizationConformancePackRequest,
    ConfigServicePutOrganizationConformancePackResponse,
    ConfigServicePutRemediationConfigurationsRequest,
    ConfigServicePutRemediationConfigurationsResponse,
    ConfigServicePutRemediationExceptionsRequest,
    ConfigServicePutRemediationExceptionsResponse,
    ConfigServicePutResourceConfigRequest,
    ConfigServicePutResourceConfigResponse,
    ConfigServicePutRetentionConfigurationRequest,
    ConfigServicePutRetentionConfigurationResponse,
    ConfigServicePutServiceLinkedConfigurationRecorderRequest,
    ConfigServicePutServiceLinkedConfigurationRecorderResponse,
    ConfigServicePutStoredQueryRequest,
    ConfigServicePutStoredQueryResponse,
    ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderRequest,
    ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderResponse,
    ConfigServiceSelectAggregateResourceConfigRequest,
    ConfigServiceSelectAggregateResourceConfigResponse,
    ConfigServiceSelectResourceConfigRequest,
    ConfigServiceSelectResourceConfigResponse,
    ConfigServiceStartConfigRulesEvaluationRequest,
    ConfigServiceStartConfigRulesEvaluationResponse,
    ConfigServiceStartConfigurationRecorderRequest,
    ConfigServiceStartConfigurationRecorderResponse,
    ConfigServiceStartRemediationExecutionRequest,
    ConfigServiceStartRemediationExecutionResponse,
    ConfigServiceStartResourceEvaluationRequest,
    ConfigServiceStartResourceEvaluationResponse,
    ConfigServiceStopConfigurationRecorderRequest,
    ConfigServiceStopConfigurationRecorderResponse,
    ConfigServiceTagResourceRequest,
    ConfigServiceTagResourceResponse,
    ConfigServiceUntagResourceRequest,
    ConfigServiceUntagResourceResponse,
)
from werkflow_aws.types.aws_config_client import ConfigServiceClient
from .base import AWSBaseService


class AWSConfigService(AWSBaseService[ConfigServiceClient]):
    service_name = 'config'
    boto3_service_name = 'config'

    def __init__(self) -> None:
        super().__init__(service_name='config', boto3_service_name='config')

    async def associate_resource_types(
        self,
        request: ConfigServiceAssociateResourceTypesRequest,
    ) -> ConfigServiceAssociateResourceTypesResponse:
        client = self._require_client()
        return await self._execute(client.associate_resource_types, request, ConfigServiceAssociateResourceTypesResponse)

    async def batch_get_aggregate_resource_config(
        self,
        request: ConfigServiceBatchGetAggregateResourceConfigRequest,
    ) -> ConfigServiceBatchGetAggregateResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_aggregate_resource_config, request, ConfigServiceBatchGetAggregateResourceConfigResponse)

    async def batch_get_resource_config(
        self,
        request: ConfigServiceBatchGetResourceConfigRequest,
    ) -> ConfigServiceBatchGetResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_resource_config, request, ConfigServiceBatchGetResourceConfigResponse)

    async def delete_aggregation_authorization(
        self,
        request: ConfigServiceDeleteAggregationAuthorizationRequest,
    ) -> ConfigServiceDeleteAggregationAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.delete_aggregation_authorization, request, ConfigServiceDeleteAggregationAuthorizationResponse)

    async def delete_config_rule(
        self,
        request: ConfigServiceDeleteConfigRuleRequest,
    ) -> ConfigServiceDeleteConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_config_rule, request, ConfigServiceDeleteConfigRuleResponse)

    async def delete_configuration_aggregator(
        self,
        request: ConfigServiceDeleteConfigurationAggregatorRequest,
    ) -> ConfigServiceDeleteConfigurationAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_aggregator, request, ConfigServiceDeleteConfigurationAggregatorResponse)

    async def delete_configuration_recorder(
        self,
        request: ConfigServiceDeleteConfigurationRecorderRequest,
    ) -> ConfigServiceDeleteConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_recorder, request, ConfigServiceDeleteConfigurationRecorderResponse)

    async def delete_conformance_pack(
        self,
        request: ConfigServiceDeleteConformancePackRequest,
    ) -> ConfigServiceDeleteConformancePackResponse:
        client = self._require_client()
        return await self._execute(client.delete_conformance_pack, request, ConfigServiceDeleteConformancePackResponse)

    async def delete_connector(
        self,
        request: ConfigServiceDeleteConnectorRequest,
    ) -> ConfigServiceDeleteConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_connector, request, ConfigServiceDeleteConnectorResponse)

    async def delete_delivery_channel(
        self,
        request: ConfigServiceDeleteDeliveryChannelRequest,
    ) -> ConfigServiceDeleteDeliveryChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery_channel, request, ConfigServiceDeleteDeliveryChannelResponse)

    async def delete_evaluation_results(
        self,
        request: ConfigServiceDeleteEvaluationResultsRequest,
    ) -> ConfigServiceDeleteEvaluationResultsResponse:
        client = self._require_client()
        return await self._execute(client.delete_evaluation_results, request, ConfigServiceDeleteEvaluationResultsResponse)

    async def delete_organization_config_rule(
        self,
        request: ConfigServiceDeleteOrganizationConfigRuleRequest,
    ) -> ConfigServiceDeleteOrganizationConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_organization_config_rule, request, ConfigServiceDeleteOrganizationConfigRuleResponse)

    async def delete_organization_conformance_pack(
        self,
        request: ConfigServiceDeleteOrganizationConformancePackRequest,
    ) -> ConfigServiceDeleteOrganizationConformancePackResponse:
        client = self._require_client()
        return await self._execute(client.delete_organization_conformance_pack, request, ConfigServiceDeleteOrganizationConformancePackResponse)

    async def delete_pending_aggregation_request(
        self,
        request: ConfigServiceDeletePendingAggregationRequestRequest,
    ) -> ConfigServiceDeletePendingAggregationRequestResponse:
        client = self._require_client()
        return await self._execute(client.delete_pending_aggregation_request, request, ConfigServiceDeletePendingAggregationRequestResponse)

    async def delete_remediation_configuration(
        self,
        request: ConfigServiceDeleteRemediationConfigurationRequest,
    ) -> ConfigServiceDeleteRemediationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_remediation_configuration, request, ConfigServiceDeleteRemediationConfigurationResponse)

    async def delete_remediation_exceptions(
        self,
        request: ConfigServiceDeleteRemediationExceptionsRequest,
    ) -> ConfigServiceDeleteRemediationExceptionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_remediation_exceptions, request, ConfigServiceDeleteRemediationExceptionsResponse)

    async def delete_resource_config(
        self,
        request: ConfigServiceDeleteResourceConfigRequest,
    ) -> ConfigServiceDeleteResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_config, request, ConfigServiceDeleteResourceConfigResponse)

    async def delete_retention_configuration(
        self,
        request: ConfigServiceDeleteRetentionConfigurationRequest,
    ) -> ConfigServiceDeleteRetentionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_retention_configuration, request, ConfigServiceDeleteRetentionConfigurationResponse)

    async def delete_service_linked_configuration_recorder(
        self,
        request: ConfigServiceDeleteServiceLinkedConfigurationRecorderRequest | None = None,
    ) -> ConfigServiceDeleteServiceLinkedConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_linked_configuration_recorder, request, ConfigServiceDeleteServiceLinkedConfigurationRecorderResponse)

    async def delete_stored_query(
        self,
        request: ConfigServiceDeleteStoredQueryRequest,
    ) -> ConfigServiceDeleteStoredQueryResponse:
        client = self._require_client()
        return await self._execute(client.delete_stored_query, request, ConfigServiceDeleteStoredQueryResponse)

    async def deliver_config_snapshot(
        self,
        request: ConfigServiceDeliverConfigSnapshotRequest,
    ) -> ConfigServiceDeliverConfigSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.deliver_config_snapshot, request, ConfigServiceDeliverConfigSnapshotResponse)

    async def describe_aggregate_compliance_by_config_rules(
        self,
        request: ConfigServiceDescribeAggregateComplianceByConfigRulesRequest,
    ) -> ConfigServiceDescribeAggregateComplianceByConfigRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_aggregate_compliance_by_config_rules, request, ConfigServiceDescribeAggregateComplianceByConfigRulesResponse)

    async def describe_aggregate_compliance_by_config_rules_paginated(
        self,
        request: ConfigServiceDescribeAggregateComplianceByConfigRulesRequest,
    ) -> list[ConfigServiceDescribeAggregateComplianceByConfigRulesResponse]:
        return await self._paginate('describe_aggregate_compliance_by_config_rules', request, ConfigServiceDescribeAggregateComplianceByConfigRulesResponse)

    async def describe_aggregate_compliance_by_conformance_packs(
        self,
        request: ConfigServiceDescribeAggregateComplianceByConformancePacksRequest,
    ) -> ConfigServiceDescribeAggregateComplianceByConformancePacksResponse:
        client = self._require_client()
        return await self._execute(client.describe_aggregate_compliance_by_conformance_packs, request, ConfigServiceDescribeAggregateComplianceByConformancePacksResponse)

    async def describe_aggregate_compliance_by_conformance_packs_paginated(
        self,
        request: ConfigServiceDescribeAggregateComplianceByConformancePacksRequest,
    ) -> list[ConfigServiceDescribeAggregateComplianceByConformancePacksResponse]:
        return await self._paginate('describe_aggregate_compliance_by_conformance_packs', request, ConfigServiceDescribeAggregateComplianceByConformancePacksResponse)

    async def describe_aggregation_authorizations(
        self,
        request: ConfigServiceDescribeAggregationAuthorizationsRequest | None = None,
    ) -> ConfigServiceDescribeAggregationAuthorizationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_aggregation_authorizations, request, ConfigServiceDescribeAggregationAuthorizationsResponse)

    async def describe_aggregation_authorizations_paginated(
        self,
        request: ConfigServiceDescribeAggregationAuthorizationsRequest | None = None,
    ) -> list[ConfigServiceDescribeAggregationAuthorizationsResponse]:
        return await self._paginate('describe_aggregation_authorizations', request, ConfigServiceDescribeAggregationAuthorizationsResponse)

    async def describe_compliance_by_config_rule(
        self,
        request: ConfigServiceDescribeComplianceByConfigRuleRequest | None = None,
    ) -> ConfigServiceDescribeComplianceByConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.describe_compliance_by_config_rule, request, ConfigServiceDescribeComplianceByConfigRuleResponse)

    async def describe_compliance_by_config_rule_paginated(
        self,
        request: ConfigServiceDescribeComplianceByConfigRuleRequest | None = None,
    ) -> list[ConfigServiceDescribeComplianceByConfigRuleResponse]:
        return await self._paginate('describe_compliance_by_config_rule', request, ConfigServiceDescribeComplianceByConfigRuleResponse)

    async def describe_compliance_by_resource(
        self,
        request: ConfigServiceDescribeComplianceByResourceRequest | None = None,
    ) -> ConfigServiceDescribeComplianceByResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_compliance_by_resource, request, ConfigServiceDescribeComplianceByResourceResponse)

    async def describe_compliance_by_resource_paginated(
        self,
        request: ConfigServiceDescribeComplianceByResourceRequest | None = None,
    ) -> list[ConfigServiceDescribeComplianceByResourceResponse]:
        return await self._paginate('describe_compliance_by_resource', request, ConfigServiceDescribeComplianceByResourceResponse)

    async def describe_config_rule_evaluation_status(
        self,
        request: ConfigServiceDescribeConfigRuleEvaluationStatusRequest | None = None,
    ) -> ConfigServiceDescribeConfigRuleEvaluationStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_config_rule_evaluation_status, request, ConfigServiceDescribeConfigRuleEvaluationStatusResponse)

    async def describe_config_rule_evaluation_status_paginated(
        self,
        request: ConfigServiceDescribeConfigRuleEvaluationStatusRequest | None = None,
    ) -> list[ConfigServiceDescribeConfigRuleEvaluationStatusResponse]:
        return await self._paginate('describe_config_rule_evaluation_status', request, ConfigServiceDescribeConfigRuleEvaluationStatusResponse)

    async def describe_config_rules(
        self,
        request: ConfigServiceDescribeConfigRulesRequest | None = None,
    ) -> ConfigServiceDescribeConfigRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_config_rules, request, ConfigServiceDescribeConfigRulesResponse)

    async def describe_config_rules_paginated(
        self,
        request: ConfigServiceDescribeConfigRulesRequest | None = None,
    ) -> list[ConfigServiceDescribeConfigRulesResponse]:
        return await self._paginate('describe_config_rules', request, ConfigServiceDescribeConfigRulesResponse)

    async def describe_configuration_aggregator_sources_status(
        self,
        request: ConfigServiceDescribeConfigurationAggregatorSourcesStatusRequest,
    ) -> ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_aggregator_sources_status, request, ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse)

    async def describe_configuration_aggregator_sources_status_paginated(
        self,
        request: ConfigServiceDescribeConfigurationAggregatorSourcesStatusRequest,
    ) -> list[ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse]:
        return await self._paginate('describe_configuration_aggregator_sources_status', request, ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse)

    async def describe_configuration_aggregators(
        self,
        request: ConfigServiceDescribeConfigurationAggregatorsRequest | None = None,
    ) -> ConfigServiceDescribeConfigurationAggregatorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_aggregators, request, ConfigServiceDescribeConfigurationAggregatorsResponse)

    async def describe_configuration_aggregators_paginated(
        self,
        request: ConfigServiceDescribeConfigurationAggregatorsRequest | None = None,
    ) -> list[ConfigServiceDescribeConfigurationAggregatorsResponse]:
        return await self._paginate('describe_configuration_aggregators', request, ConfigServiceDescribeConfigurationAggregatorsResponse)

    async def describe_configuration_recorder_status(
        self,
        request: ConfigServiceDescribeConfigurationRecorderStatusRequest | None = None,
    ) -> ConfigServiceDescribeConfigurationRecorderStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_recorder_status, request, ConfigServiceDescribeConfigurationRecorderStatusResponse)

    async def describe_configuration_recorders(
        self,
        request: ConfigServiceDescribeConfigurationRecordersRequest | None = None,
    ) -> ConfigServiceDescribeConfigurationRecordersResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_recorders, request, ConfigServiceDescribeConfigurationRecordersResponse)

    async def describe_conformance_pack_compliance(
        self,
        request: ConfigServiceDescribeConformancePackComplianceRequest,
    ) -> ConfigServiceDescribeConformancePackComplianceResponse:
        client = self._require_client()
        return await self._execute(client.describe_conformance_pack_compliance, request, ConfigServiceDescribeConformancePackComplianceResponse)

    async def describe_conformance_pack_compliance_paginated(
        self,
        request: ConfigServiceDescribeConformancePackComplianceRequest,
    ) -> list[ConfigServiceDescribeConformancePackComplianceResponse]:
        return await self._paginate('describe_conformance_pack_compliance', request, ConfigServiceDescribeConformancePackComplianceResponse)

    async def describe_conformance_pack_status(
        self,
        request: ConfigServiceDescribeConformancePackStatusRequest | None = None,
    ) -> ConfigServiceDescribeConformancePackStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_conformance_pack_status, request, ConfigServiceDescribeConformancePackStatusResponse)

    async def describe_conformance_pack_status_paginated(
        self,
        request: ConfigServiceDescribeConformancePackStatusRequest | None = None,
    ) -> list[ConfigServiceDescribeConformancePackStatusResponse]:
        return await self._paginate('describe_conformance_pack_status', request, ConfigServiceDescribeConformancePackStatusResponse)

    async def describe_conformance_packs(
        self,
        request: ConfigServiceDescribeConformancePacksRequest | None = None,
    ) -> ConfigServiceDescribeConformancePacksResponse:
        client = self._require_client()
        return await self._execute(client.describe_conformance_packs, request, ConfigServiceDescribeConformancePacksResponse)

    async def describe_conformance_packs_paginated(
        self,
        request: ConfigServiceDescribeConformancePacksRequest | None = None,
    ) -> list[ConfigServiceDescribeConformancePacksResponse]:
        return await self._paginate('describe_conformance_packs', request, ConfigServiceDescribeConformancePacksResponse)

    async def describe_delivery_channel_status(
        self,
        request: ConfigServiceDescribeDeliveryChannelStatusRequest | None = None,
    ) -> ConfigServiceDescribeDeliveryChannelStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_delivery_channel_status, request, ConfigServiceDescribeDeliveryChannelStatusResponse)

    async def describe_delivery_channels(
        self,
        request: ConfigServiceDescribeDeliveryChannelsRequest | None = None,
    ) -> ConfigServiceDescribeDeliveryChannelsResponse:
        client = self._require_client()
        return await self._execute(client.describe_delivery_channels, request, ConfigServiceDescribeDeliveryChannelsResponse)

    async def describe_organization_config_rule_statuses(
        self,
        request: ConfigServiceDescribeOrganizationConfigRuleStatusesRequest | None = None,
    ) -> ConfigServiceDescribeOrganizationConfigRuleStatusesResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_config_rule_statuses, request, ConfigServiceDescribeOrganizationConfigRuleStatusesResponse)

    async def describe_organization_config_rule_statuses_paginated(
        self,
        request: ConfigServiceDescribeOrganizationConfigRuleStatusesRequest | None = None,
    ) -> list[ConfigServiceDescribeOrganizationConfigRuleStatusesResponse]:
        return await self._paginate('describe_organization_config_rule_statuses', request, ConfigServiceDescribeOrganizationConfigRuleStatusesResponse)

    async def describe_organization_config_rules(
        self,
        request: ConfigServiceDescribeOrganizationConfigRulesRequest | None = None,
    ) -> ConfigServiceDescribeOrganizationConfigRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_config_rules, request, ConfigServiceDescribeOrganizationConfigRulesResponse)

    async def describe_organization_config_rules_paginated(
        self,
        request: ConfigServiceDescribeOrganizationConfigRulesRequest | None = None,
    ) -> list[ConfigServiceDescribeOrganizationConfigRulesResponse]:
        return await self._paginate('describe_organization_config_rules', request, ConfigServiceDescribeOrganizationConfigRulesResponse)

    async def describe_organization_conformance_pack_statuses(
        self,
        request: ConfigServiceDescribeOrganizationConformancePackStatusesRequest | None = None,
    ) -> ConfigServiceDescribeOrganizationConformancePackStatusesResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_conformance_pack_statuses, request, ConfigServiceDescribeOrganizationConformancePackStatusesResponse)

    async def describe_organization_conformance_pack_statuses_paginated(
        self,
        request: ConfigServiceDescribeOrganizationConformancePackStatusesRequest | None = None,
    ) -> list[ConfigServiceDescribeOrganizationConformancePackStatusesResponse]:
        return await self._paginate('describe_organization_conformance_pack_statuses', request, ConfigServiceDescribeOrganizationConformancePackStatusesResponse)

    async def describe_organization_conformance_packs(
        self,
        request: ConfigServiceDescribeOrganizationConformancePacksRequest | None = None,
    ) -> ConfigServiceDescribeOrganizationConformancePacksResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_conformance_packs, request, ConfigServiceDescribeOrganizationConformancePacksResponse)

    async def describe_organization_conformance_packs_paginated(
        self,
        request: ConfigServiceDescribeOrganizationConformancePacksRequest | None = None,
    ) -> list[ConfigServiceDescribeOrganizationConformancePacksResponse]:
        return await self._paginate('describe_organization_conformance_packs', request, ConfigServiceDescribeOrganizationConformancePacksResponse)

    async def describe_pending_aggregation_requests(
        self,
        request: ConfigServiceDescribePendingAggregationRequestsRequest | None = None,
    ) -> ConfigServiceDescribePendingAggregationRequestsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pending_aggregation_requests, request, ConfigServiceDescribePendingAggregationRequestsResponse)

    async def describe_pending_aggregation_requests_paginated(
        self,
        request: ConfigServiceDescribePendingAggregationRequestsRequest | None = None,
    ) -> list[ConfigServiceDescribePendingAggregationRequestsResponse]:
        return await self._paginate('describe_pending_aggregation_requests', request, ConfigServiceDescribePendingAggregationRequestsResponse)

    async def describe_remediation_configurations(
        self,
        request: ConfigServiceDescribeRemediationConfigurationsRequest,
    ) -> ConfigServiceDescribeRemediationConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_remediation_configurations, request, ConfigServiceDescribeRemediationConfigurationsResponse)

    async def describe_remediation_exceptions(
        self,
        request: ConfigServiceDescribeRemediationExceptionsRequest,
    ) -> ConfigServiceDescribeRemediationExceptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_remediation_exceptions, request, ConfigServiceDescribeRemediationExceptionsResponse)

    async def describe_remediation_execution_status(
        self,
        request: ConfigServiceDescribeRemediationExecutionStatusRequest,
    ) -> ConfigServiceDescribeRemediationExecutionStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_remediation_execution_status, request, ConfigServiceDescribeRemediationExecutionStatusResponse)

    async def describe_remediation_execution_status_paginated(
        self,
        request: ConfigServiceDescribeRemediationExecutionStatusRequest,
    ) -> list[ConfigServiceDescribeRemediationExecutionStatusResponse]:
        return await self._paginate('describe_remediation_execution_status', request, ConfigServiceDescribeRemediationExecutionStatusResponse)

    async def describe_retention_configurations(
        self,
        request: ConfigServiceDescribeRetentionConfigurationsRequest | None = None,
    ) -> ConfigServiceDescribeRetentionConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_retention_configurations, request, ConfigServiceDescribeRetentionConfigurationsResponse)

    async def describe_retention_configurations_paginated(
        self,
        request: ConfigServiceDescribeRetentionConfigurationsRequest | None = None,
    ) -> list[ConfigServiceDescribeRetentionConfigurationsResponse]:
        return await self._paginate('describe_retention_configurations', request, ConfigServiceDescribeRetentionConfigurationsResponse)

    async def disassociate_resource_types(
        self,
        request: ConfigServiceDisassociateResourceTypesRequest,
    ) -> ConfigServiceDisassociateResourceTypesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_resource_types, request, ConfigServiceDisassociateResourceTypesResponse)

    async def get_aggregate_compliance_details_by_config_rule(
        self,
        request: ConfigServiceGetAggregateComplianceDetailsByConfigRuleRequest,
    ) -> ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_aggregate_compliance_details_by_config_rule, request, ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse)

    async def get_aggregate_compliance_details_by_config_rule_paginated(
        self,
        request: ConfigServiceGetAggregateComplianceDetailsByConfigRuleRequest,
    ) -> list[ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse]:
        return await self._paginate('get_aggregate_compliance_details_by_config_rule', request, ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse)

    async def get_aggregate_config_rule_compliance_summary(
        self,
        request: ConfigServiceGetAggregateConfigRuleComplianceSummaryRequest,
    ) -> ConfigServiceGetAggregateConfigRuleComplianceSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_aggregate_config_rule_compliance_summary, request, ConfigServiceGetAggregateConfigRuleComplianceSummaryResponse)

    async def get_aggregate_conformance_pack_compliance_summary(
        self,
        request: ConfigServiceGetAggregateConformancePackComplianceSummaryRequest,
    ) -> ConfigServiceGetAggregateConformancePackComplianceSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_aggregate_conformance_pack_compliance_summary, request, ConfigServiceGetAggregateConformancePackComplianceSummaryResponse)

    async def get_aggregate_discovered_resource_counts(
        self,
        request: ConfigServiceGetAggregateDiscoveredResourceCountsRequest,
    ) -> ConfigServiceGetAggregateDiscoveredResourceCountsResponse:
        client = self._require_client()
        return await self._execute(client.get_aggregate_discovered_resource_counts, request, ConfigServiceGetAggregateDiscoveredResourceCountsResponse)

    async def get_aggregate_resource_config(
        self,
        request: ConfigServiceGetAggregateResourceConfigRequest,
    ) -> ConfigServiceGetAggregateResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_aggregate_resource_config, request, ConfigServiceGetAggregateResourceConfigResponse)

    async def get_compliance_details_by_config_rule(
        self,
        request: ConfigServiceGetComplianceDetailsByConfigRuleRequest,
    ) -> ConfigServiceGetComplianceDetailsByConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_compliance_details_by_config_rule, request, ConfigServiceGetComplianceDetailsByConfigRuleResponse)

    async def get_compliance_details_by_config_rule_paginated(
        self,
        request: ConfigServiceGetComplianceDetailsByConfigRuleRequest,
    ) -> list[ConfigServiceGetComplianceDetailsByConfigRuleResponse]:
        return await self._paginate('get_compliance_details_by_config_rule', request, ConfigServiceGetComplianceDetailsByConfigRuleResponse)

    async def get_compliance_details_by_resource(
        self,
        request: ConfigServiceGetComplianceDetailsByResourceRequest | None = None,
    ) -> ConfigServiceGetComplianceDetailsByResourceResponse:
        client = self._require_client()
        return await self._execute(client.get_compliance_details_by_resource, request, ConfigServiceGetComplianceDetailsByResourceResponse)

    async def get_compliance_details_by_resource_paginated(
        self,
        request: ConfigServiceGetComplianceDetailsByResourceRequest | None = None,
    ) -> list[ConfigServiceGetComplianceDetailsByResourceResponse]:
        return await self._paginate('get_compliance_details_by_resource', request, ConfigServiceGetComplianceDetailsByResourceResponse)

    async def get_compliance_summary_by_config_rule(
        self,
        request: ConfigServiceGetComplianceSummaryByConfigRuleRequest | None = None,
    ) -> ConfigServiceGetComplianceSummaryByConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_compliance_summary_by_config_rule, request, ConfigServiceGetComplianceSummaryByConfigRuleResponse)

    async def get_compliance_summary_by_resource_type(
        self,
        request: ConfigServiceGetComplianceSummaryByResourceTypeRequest | None = None,
    ) -> ConfigServiceGetComplianceSummaryByResourceTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_compliance_summary_by_resource_type, request, ConfigServiceGetComplianceSummaryByResourceTypeResponse)

    async def get_conformance_pack_compliance_details(
        self,
        request: ConfigServiceGetConformancePackComplianceDetailsRequest,
    ) -> ConfigServiceGetConformancePackComplianceDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_conformance_pack_compliance_details, request, ConfigServiceGetConformancePackComplianceDetailsResponse)

    async def get_conformance_pack_compliance_summary(
        self,
        request: ConfigServiceGetConformancePackComplianceSummaryRequest,
    ) -> ConfigServiceGetConformancePackComplianceSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_conformance_pack_compliance_summary, request, ConfigServiceGetConformancePackComplianceSummaryResponse)

    async def get_conformance_pack_compliance_summary_paginated(
        self,
        request: ConfigServiceGetConformancePackComplianceSummaryRequest,
    ) -> list[ConfigServiceGetConformancePackComplianceSummaryResponse]:
        return await self._paginate('get_conformance_pack_compliance_summary', request, ConfigServiceGetConformancePackComplianceSummaryResponse)

    async def get_connector(
        self,
        request: ConfigServiceGetConnectorRequest,
    ) -> ConfigServiceGetConnectorResponse:
        client = self._require_client()
        return await self._execute(client.get_connector, request, ConfigServiceGetConnectorResponse)

    async def get_custom_rule_policy(
        self,
        request: ConfigServiceGetCustomRulePolicyRequest | None = None,
    ) -> ConfigServiceGetCustomRulePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_rule_policy, request, ConfigServiceGetCustomRulePolicyResponse)

    async def get_discovered_resource_counts(
        self,
        request: ConfigServiceGetDiscoveredResourceCountsRequest | None = None,
    ) -> ConfigServiceGetDiscoveredResourceCountsResponse:
        client = self._require_client()
        return await self._execute(client.get_discovered_resource_counts, request, ConfigServiceGetDiscoveredResourceCountsResponse)

    async def get_organization_config_rule_detailed_status(
        self,
        request: ConfigServiceGetOrganizationConfigRuleDetailedStatusRequest,
    ) -> ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_config_rule_detailed_status, request, ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse)

    async def get_organization_config_rule_detailed_status_paginated(
        self,
        request: ConfigServiceGetOrganizationConfigRuleDetailedStatusRequest,
    ) -> list[ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse]:
        return await self._paginate('get_organization_config_rule_detailed_status', request, ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse)

    async def get_organization_conformance_pack_detailed_status(
        self,
        request: ConfigServiceGetOrganizationConformancePackDetailedStatusRequest,
    ) -> ConfigServiceGetOrganizationConformancePackDetailedStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_conformance_pack_detailed_status, request, ConfigServiceGetOrganizationConformancePackDetailedStatusResponse)

    async def get_organization_conformance_pack_detailed_status_paginated(
        self,
        request: ConfigServiceGetOrganizationConformancePackDetailedStatusRequest,
    ) -> list[ConfigServiceGetOrganizationConformancePackDetailedStatusResponse]:
        return await self._paginate('get_organization_conformance_pack_detailed_status', request, ConfigServiceGetOrganizationConformancePackDetailedStatusResponse)

    async def get_organization_custom_rule_policy(
        self,
        request: ConfigServiceGetOrganizationCustomRulePolicyRequest,
    ) -> ConfigServiceGetOrganizationCustomRulePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_custom_rule_policy, request, ConfigServiceGetOrganizationCustomRulePolicyResponse)

    async def get_resource_config_history(
        self,
        request: ConfigServiceGetResourceConfigHistoryRequest,
    ) -> ConfigServiceGetResourceConfigHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_config_history, request, ConfigServiceGetResourceConfigHistoryResponse)

    async def get_resource_config_history_paginated(
        self,
        request: ConfigServiceGetResourceConfigHistoryRequest,
    ) -> list[ConfigServiceGetResourceConfigHistoryResponse]:
        return await self._paginate('get_resource_config_history', request, ConfigServiceGetResourceConfigHistoryResponse)

    async def get_resource_evaluation_summary(
        self,
        request: ConfigServiceGetResourceEvaluationSummaryRequest,
    ) -> ConfigServiceGetResourceEvaluationSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_evaluation_summary, request, ConfigServiceGetResourceEvaluationSummaryResponse)

    async def get_stored_query(
        self,
        request: ConfigServiceGetStoredQueryRequest,
    ) -> ConfigServiceGetStoredQueryResponse:
        client = self._require_client()
        return await self._execute(client.get_stored_query, request, ConfigServiceGetStoredQueryResponse)

    async def list_aggregate_discovered_resources(
        self,
        request: ConfigServiceListAggregateDiscoveredResourcesRequest,
    ) -> ConfigServiceListAggregateDiscoveredResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_aggregate_discovered_resources, request, ConfigServiceListAggregateDiscoveredResourcesResponse)

    async def list_aggregate_discovered_resources_paginated(
        self,
        request: ConfigServiceListAggregateDiscoveredResourcesRequest,
    ) -> list[ConfigServiceListAggregateDiscoveredResourcesResponse]:
        return await self._paginate('list_aggregate_discovered_resources', request, ConfigServiceListAggregateDiscoveredResourcesResponse)

    async def list_configuration_recorders(
        self,
        request: ConfigServiceListConfigurationRecordersRequest | None = None,
    ) -> ConfigServiceListConfigurationRecordersResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_recorders, request, ConfigServiceListConfigurationRecordersResponse)

    async def list_configuration_recorders_paginated(
        self,
        request: ConfigServiceListConfigurationRecordersRequest | None = None,
    ) -> list[ConfigServiceListConfigurationRecordersResponse]:
        return await self._paginate('list_configuration_recorders', request, ConfigServiceListConfigurationRecordersResponse)

    async def list_conformance_pack_compliance_scores(
        self,
        request: ConfigServiceListConformancePackComplianceScoresRequest | None = None,
    ) -> ConfigServiceListConformancePackComplianceScoresResponse:
        client = self._require_client()
        return await self._execute(client.list_conformance_pack_compliance_scores, request, ConfigServiceListConformancePackComplianceScoresResponse)

    async def list_connectors(
        self,
        request: ConfigServiceListConnectorsRequest | None = None,
    ) -> ConfigServiceListConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_connectors, request, ConfigServiceListConnectorsResponse)

    async def list_connectors_paginated(
        self,
        request: ConfigServiceListConnectorsRequest | None = None,
    ) -> list[ConfigServiceListConnectorsResponse]:
        return await self._paginate('list_connectors', request, ConfigServiceListConnectorsResponse)

    async def list_discovered_resources(
        self,
        request: ConfigServiceListDiscoveredResourcesRequest,
    ) -> ConfigServiceListDiscoveredResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_discovered_resources, request, ConfigServiceListDiscoveredResourcesResponse)

    async def list_discovered_resources_paginated(
        self,
        request: ConfigServiceListDiscoveredResourcesRequest,
    ) -> list[ConfigServiceListDiscoveredResourcesResponse]:
        return await self._paginate('list_discovered_resources', request, ConfigServiceListDiscoveredResourcesResponse)

    async def list_resource_evaluations(
        self,
        request: ConfigServiceListResourceEvaluationsRequest | None = None,
    ) -> ConfigServiceListResourceEvaluationsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_evaluations, request, ConfigServiceListResourceEvaluationsResponse)

    async def list_resource_evaluations_paginated(
        self,
        request: ConfigServiceListResourceEvaluationsRequest | None = None,
    ) -> list[ConfigServiceListResourceEvaluationsResponse]:
        return await self._paginate('list_resource_evaluations', request, ConfigServiceListResourceEvaluationsResponse)

    async def list_stored_queries(
        self,
        request: ConfigServiceListStoredQueriesRequest | None = None,
    ) -> ConfigServiceListStoredQueriesResponse:
        client = self._require_client()
        return await self._execute(client.list_stored_queries, request, ConfigServiceListStoredQueriesResponse)

    async def list_tags_for_resource(
        self,
        request: ConfigServiceListTagsForResourceRequest,
    ) -> ConfigServiceListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ConfigServiceListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: ConfigServiceListTagsForResourceRequest,
    ) -> list[ConfigServiceListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, ConfigServiceListTagsForResourceResponse)

    async def put_aggregation_authorization(
        self,
        request: ConfigServicePutAggregationAuthorizationRequest,
    ) -> ConfigServicePutAggregationAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.put_aggregation_authorization, request, ConfigServicePutAggregationAuthorizationResponse)

    async def put_config_rule(
        self,
        request: ConfigServicePutConfigRuleRequest,
    ) -> ConfigServicePutConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_config_rule, request, ConfigServicePutConfigRuleResponse)

    async def put_configuration_aggregator(
        self,
        request: ConfigServicePutConfigurationAggregatorRequest,
    ) -> ConfigServicePutConfigurationAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_aggregator, request, ConfigServicePutConfigurationAggregatorResponse)

    async def put_configuration_recorder(
        self,
        request: ConfigServicePutConfigurationRecorderRequest,
    ) -> ConfigServicePutConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_recorder, request, ConfigServicePutConfigurationRecorderResponse)

    async def put_conformance_pack(
        self,
        request: ConfigServicePutConformancePackRequest,
    ) -> ConfigServicePutConformancePackResponse:
        client = self._require_client()
        return await self._execute(client.put_conformance_pack, request, ConfigServicePutConformancePackResponse)

    async def put_connector(
        self,
        request: ConfigServicePutConnectorRequest,
    ) -> ConfigServicePutConnectorResponse:
        client = self._require_client()
        return await self._execute(client.put_connector, request, ConfigServicePutConnectorResponse)

    async def put_delivery_channel(
        self,
        request: ConfigServicePutDeliveryChannelRequest,
    ) -> ConfigServicePutDeliveryChannelResponse:
        client = self._require_client()
        return await self._execute(client.put_delivery_channel, request, ConfigServicePutDeliveryChannelResponse)

    async def put_evaluations(
        self,
        request: ConfigServicePutEvaluationsRequest,
    ) -> ConfigServicePutEvaluationsResponse:
        client = self._require_client()
        return await self._execute(client.put_evaluations, request, ConfigServicePutEvaluationsResponse)

    async def put_external_evaluation(
        self,
        request: ConfigServicePutExternalEvaluationRequest,
    ) -> ConfigServicePutExternalEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.put_external_evaluation, request, ConfigServicePutExternalEvaluationResponse)

    async def put_organization_config_rule(
        self,
        request: ConfigServicePutOrganizationConfigRuleRequest,
    ) -> ConfigServicePutOrganizationConfigRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_organization_config_rule, request, ConfigServicePutOrganizationConfigRuleResponse)

    async def put_organization_conformance_pack(
        self,
        request: ConfigServicePutOrganizationConformancePackRequest,
    ) -> ConfigServicePutOrganizationConformancePackResponse:
        client = self._require_client()
        return await self._execute(client.put_organization_conformance_pack, request, ConfigServicePutOrganizationConformancePackResponse)

    async def put_remediation_configurations(
        self,
        request: ConfigServicePutRemediationConfigurationsRequest,
    ) -> ConfigServicePutRemediationConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.put_remediation_configurations, request, ConfigServicePutRemediationConfigurationsResponse)

    async def put_remediation_exceptions(
        self,
        request: ConfigServicePutRemediationExceptionsRequest,
    ) -> ConfigServicePutRemediationExceptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_remediation_exceptions, request, ConfigServicePutRemediationExceptionsResponse)

    async def put_resource_config(
        self,
        request: ConfigServicePutResourceConfigRequest,
    ) -> ConfigServicePutResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_config, request, ConfigServicePutResourceConfigResponse)

    async def put_retention_configuration(
        self,
        request: ConfigServicePutRetentionConfigurationRequest,
    ) -> ConfigServicePutRetentionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_retention_configuration, request, ConfigServicePutRetentionConfigurationResponse)

    async def put_service_linked_configuration_recorder(
        self,
        request: ConfigServicePutServiceLinkedConfigurationRecorderRequest,
    ) -> ConfigServicePutServiceLinkedConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.put_service_linked_configuration_recorder, request, ConfigServicePutServiceLinkedConfigurationRecorderResponse)

    async def put_stored_query(
        self,
        request: ConfigServicePutStoredQueryRequest,
    ) -> ConfigServicePutStoredQueryResponse:
        client = self._require_client()
        return await self._execute(client.put_stored_query, request, ConfigServicePutStoredQueryResponse)

    async def put_third_party_service_linked_configuration_recorder(
        self,
        request: ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderRequest,
    ) -> ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.put_third_party_service_linked_configuration_recorder, request, ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderResponse)

    async def select_aggregate_resource_config(
        self,
        request: ConfigServiceSelectAggregateResourceConfigRequest,
    ) -> ConfigServiceSelectAggregateResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.select_aggregate_resource_config, request, ConfigServiceSelectAggregateResourceConfigResponse)

    async def select_aggregate_resource_config_paginated(
        self,
        request: ConfigServiceSelectAggregateResourceConfigRequest,
    ) -> list[ConfigServiceSelectAggregateResourceConfigResponse]:
        return await self._paginate('select_aggregate_resource_config', request, ConfigServiceSelectAggregateResourceConfigResponse)

    async def select_resource_config(
        self,
        request: ConfigServiceSelectResourceConfigRequest,
    ) -> ConfigServiceSelectResourceConfigResponse:
        client = self._require_client()
        return await self._execute(client.select_resource_config, request, ConfigServiceSelectResourceConfigResponse)

    async def select_resource_config_paginated(
        self,
        request: ConfigServiceSelectResourceConfigRequest,
    ) -> list[ConfigServiceSelectResourceConfigResponse]:
        return await self._paginate('select_resource_config', request, ConfigServiceSelectResourceConfigResponse)

    async def start_config_rules_evaluation(
        self,
        request: ConfigServiceStartConfigRulesEvaluationRequest | None = None,
    ) -> ConfigServiceStartConfigRulesEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.start_config_rules_evaluation, request, ConfigServiceStartConfigRulesEvaluationResponse)

    async def start_configuration_recorder(
        self,
        request: ConfigServiceStartConfigurationRecorderRequest,
    ) -> ConfigServiceStartConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.start_configuration_recorder, request, ConfigServiceStartConfigurationRecorderResponse)

    async def start_remediation_execution(
        self,
        request: ConfigServiceStartRemediationExecutionRequest,
    ) -> ConfigServiceStartRemediationExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_remediation_execution, request, ConfigServiceStartRemediationExecutionResponse)

    async def start_resource_evaluation(
        self,
        request: ConfigServiceStartResourceEvaluationRequest,
    ) -> ConfigServiceStartResourceEvaluationResponse:
        client = self._require_client()
        return await self._execute(client.start_resource_evaluation, request, ConfigServiceStartResourceEvaluationResponse)

    async def stop_configuration_recorder(
        self,
        request: ConfigServiceStopConfigurationRecorderRequest,
    ) -> ConfigServiceStopConfigurationRecorderResponse:
        client = self._require_client()
        return await self._execute(client.stop_configuration_recorder, request, ConfigServiceStopConfigurationRecorderResponse)

    async def tag_resource(
        self,
        request: ConfigServiceTagResourceRequest,
    ) -> ConfigServiceTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ConfigServiceTagResourceResponse)

    async def untag_resource(
        self,
        request: ConfigServiceUntagResourceRequest,
    ) -> ConfigServiceUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ConfigServiceUntagResourceResponse)
