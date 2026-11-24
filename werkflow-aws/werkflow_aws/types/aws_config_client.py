from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ConfigServiceClient(ABC):

    @abstractmethod
    def associate_resource_types(
        self,
        *,
        ConfigurationRecorderArn: str,
        ResourceTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_aggregate_resource_config(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceIdentifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_resource_config(
        self,
        *,
        resourceKeys: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_aggregation_authorization(
        self,
        *,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_config_rule(
        self,
        *,
        ConfigRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_aggregator(
        self,
        *,
        ConfigurationAggregatorName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_recorder(
        self,
        *,
        ConfigurationRecorderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_conformance_pack(
        self,
        *,
        ConformancePackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connector(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery_channel(
        self,
        *,
        DeliveryChannelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_evaluation_results(
        self,
        *,
        ConfigRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_organization_config_rule(
        self,
        *,
        OrganizationConfigRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_organization_conformance_pack(
        self,
        *,
        OrganizationConformancePackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pending_aggregation_request(
        self,
        *,
        RequesterAccountId: str,
        RequesterAwsRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_remediation_configuration(
        self,
        *,
        ConfigRuleName: str,
        ResourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_remediation_exceptions(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_config(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_retention_configuration(
        self,
        *,
        RetentionConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_linked_configuration_recorder(
        self,
        *,
        ServicePrincipal: str | None = None,
        Arn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stored_query(
        self,
        *,
        QueryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deliver_config_snapshot(
        self,
        *,
        deliveryChannelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_aggregate_compliance_by_config_rules(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_aggregate_compliance_by_conformance_packs(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_aggregation_authorizations(
        self,
        *,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_compliance_by_config_rule(
        self,
        *,
        ConfigRuleNames: list[str] | None = None,
        ComplianceTypes: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_compliance_by_resource(
        self,
        *,
        ResourceType: str | None = None,
        ResourceId: str | None = None,
        ComplianceTypes: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_config_rule_evaluation_status(
        self,
        *,
        ConfigRuleNames: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_config_rules(
        self,
        *,
        ConfigRuleNames: list[str] | None = None,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_aggregator_sources_status(
        self,
        *,
        ConfigurationAggregatorName: str,
        UpdateStatus: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_aggregators(
        self,
        *,
        ConfigurationAggregatorNames: list[str] | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_recorder_status(
        self,
        *,
        ConfigurationRecorderNames: list[str] | None = None,
        ServicePrincipal: str | None = None,
        Arn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_recorders(
        self,
        *,
        ConfigurationRecorderNames: list[str] | None = None,
        ServicePrincipal: str | None = None,
        Arn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conformance_pack_compliance(
        self,
        *,
        ConformancePackName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conformance_pack_status(
        self,
        *,
        ConformancePackNames: list[str] | None = None,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conformance_packs(
        self,
        *,
        ConformancePackNames: list[str] | None = None,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_delivery_channel_status(
        self,
        *,
        DeliveryChannelNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_delivery_channels(
        self,
        *,
        DeliveryChannelNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_config_rule_statuses(
        self,
        *,
        OrganizationConfigRuleNames: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_config_rules(
        self,
        *,
        OrganizationConfigRuleNames: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_conformance_pack_statuses(
        self,
        *,
        OrganizationConformancePackNames: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_conformance_packs(
        self,
        *,
        OrganizationConformancePackNames: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pending_aggregation_requests(
        self,
        *,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_remediation_configurations(
        self,
        *,
        ConfigRuleNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_remediation_exceptions(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_remediation_execution_status(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: list[dict[str, Any]] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_retention_configurations(
        self,
        *,
        RetentionConfigurationNames: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_resource_types(
        self,
        *,
        ConfigurationRecorderArn: str,
        ResourceTypes: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregate_compliance_details_by_config_rule(
        self,
        *,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregate_config_rule_compliance_summary(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: dict[str, Any] | None = None,
        GroupByKey: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregate_conformance_pack_compliance_summary(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: dict[str, Any] | None = None,
        GroupByKey: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregate_discovered_resource_counts(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: dict[str, Any] | None = None,
        GroupByKey: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregate_resource_config(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceIdentifier: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compliance_details_by_config_rule(
        self,
        *,
        ConfigRuleName: str,
        ComplianceTypes: list[str] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compliance_details_by_resource(
        self,
        *,
        ResourceType: str | None = None,
        ResourceId: str | None = None,
        ComplianceTypes: list[str] | None = None,
        NextToken: str | None = None,
        ResourceEvaluationId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compliance_summary_by_config_rule(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compliance_summary_by_resource_type(
        self,
        *,
        ResourceTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_conformance_pack_compliance_details(
        self,
        *,
        ConformancePackName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_conformance_pack_compliance_summary(
        self,
        *,
        ConformancePackNames: list[str],
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connector(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_rule_policy(
        self,
        *,
        ConfigRuleName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_discovered_resource_counts(
        self,
        *,
        resourceTypes: list[str] | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_config_rule_detailed_status(
        self,
        *,
        OrganizationConfigRuleName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_conformance_pack_detailed_status(
        self,
        *,
        OrganizationConformancePackName: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_custom_rule_policy(
        self,
        *,
        OrganizationConfigRuleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_config_history(
        self,
        *,
        resourceType: str,
        resourceId: str,
        laterTime: datetime.datetime | str | None = None,
        earlierTime: datetime.datetime | str | None = None,
        chronologicalOrder: str | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_evaluation_summary(
        self,
        *,
        ResourceEvaluationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stored_query(
        self,
        *,
        QueryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aggregate_discovered_resources(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceType: str,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_recorders(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_conformance_pack_compliance_scores(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connectors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_discovered_resources(
        self,
        *,
        resourceType: str,
        resourceIds: list[str] | None = None,
        resourceName: str | None = None,
        limit: int | None = None,
        includeDeletedResources: bool | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_evaluations(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stored_queries(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_aggregation_authorization(
        self,
        *,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_config_rule(
        self,
        *,
        ConfigRule: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_aggregator(
        self,
        *,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: list[dict[str, Any]] | None = None,
        OrganizationAggregationSource: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AggregatorFilters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_recorder(
        self,
        *,
        ConfigurationRecorder: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_conformance_pack(
        self,
        *,
        ConformancePackName: str,
        TemplateS3Uri: str | None = None,
        TemplateBody: str | None = None,
        DeliveryS3Bucket: str | None = None,
        DeliveryS3KeyPrefix: str | None = None,
        ConformancePackInputParameters: list[dict[str, Any]] | None = None,
        TemplateSSMDocumentDetails: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Source: dict[str, Any] | None = None,
        Scope: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_connector(
        self,
        *,
        ConnectorConfiguration: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_delivery_channel(
        self,
        *,
        DeliveryChannel: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_evaluations(
        self,
        *,
        ResultToken: str,
        Evaluations: list[dict[str, Any]] | None = None,
        TestMode: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_external_evaluation(
        self,
        *,
        ConfigRuleName: str,
        ExternalEvaluation: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_organization_config_rule(
        self,
        *,
        OrganizationConfigRuleName: str,
        OrganizationManagedRuleMetadata: dict[str, Any] | None = None,
        OrganizationCustomRuleMetadata: dict[str, Any] | None = None,
        ExcludedAccounts: list[str] | None = None,
        OrganizationCustomPolicyRuleMetadata: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_organization_conformance_pack(
        self,
        *,
        OrganizationConformancePackName: str,
        TemplateS3Uri: str | None = None,
        TemplateBody: str | None = None,
        DeliveryS3Bucket: str | None = None,
        DeliveryS3KeyPrefix: str | None = None,
        ConformancePackInputParameters: list[dict[str, Any]] | None = None,
        ExcludedAccounts: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_remediation_configurations(
        self,
        *,
        RemediationConfigurations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_remediation_exceptions(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: list[dict[str, Any]],
        Message: str | None = None,
        ExpirationTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_config(
        self,
        *,
        ResourceType: str,
        SchemaVersionId: str,
        ResourceId: str,
        Configuration: str,
        ResourceName: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_retention_configuration(
        self,
        *,
        RetentionPeriodInDays: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_service_linked_configuration_recorder(
        self,
        *,
        ServicePrincipal: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_stored_query(
        self,
        *,
        StoredQuery: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_third_party_service_linked_configuration_recorder(
        self,
        *,
        ServicePrincipal: str,
        ConnectorArn: str,
        ScopeConfiguration: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def select_aggregate_resource_config(
        self,
        *,
        Expression: str,
        ConfigurationAggregatorName: str,
        Limit: int | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def select_resource_config(
        self,
        *,
        Expression: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_config_rules_evaluation(
        self,
        *,
        ConfigRuleNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_configuration_recorder(
        self,
        *,
        ConfigurationRecorderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_remediation_execution(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_resource_evaluation(
        self,
        *,
        ResourceDetails: dict[str, Any],
        EvaluationMode: str,
        EvaluationContext: dict[str, Any] | None = None,
        EvaluationTimeout: int | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_configuration_recorder(
        self,
        *,
        ConfigurationRecorderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
