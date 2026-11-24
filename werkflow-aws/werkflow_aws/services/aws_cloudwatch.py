from werkflow_aws.models.cloudwatch import (
    CloudWatchDeleteAlarmsRequest,
    CloudWatchDescribeAlarmsRequest,
    CloudWatchDescribeAlarmsResponse,
    CloudWatchEmptyResponse,
    CloudWatchGetMetricDataRequest,
    CloudWatchGetMetricDataResponse,
    CloudWatchGetMetricStatisticsRequest,
    CloudWatchGetMetricStatisticsResponse,
    CloudWatchListMetricsRequest,
    CloudWatchListMetricsResponse,
    CloudWatchPutMetricAlarmRequest,
    CloudWatchPutMetricDataRequest,
)
from werkflow_aws.types import CloudWatchClient
from .base import AWSBaseService
from werkflow_aws.models.cloudwatch import (
    CloudWatchAssociateDatasetKmsKeyRequest,
    CloudWatchAssociateDatasetKmsKeyResponse,
    CloudWatchCreateResourceMetricsConfigurationRequest,
    CloudWatchCreateResourceMetricsConfigurationResponse,
    CloudWatchDeleteAlarmMuteRuleRequest,
    CloudWatchDeleteAlarmMuteRuleResponse,
    CloudWatchDeleteAnomalyDetectorRequest,
    CloudWatchDeleteAnomalyDetectorResponse,
    CloudWatchDeleteDashboardsRequest,
    CloudWatchDeleteDashboardsResponse,
    CloudWatchDeleteInsightRulesRequest,
    CloudWatchDeleteInsightRulesResponse,
    CloudWatchDeleteMetricDataQueryDefinitionRequest,
    CloudWatchDeleteMetricDataQueryDefinitionResponse,
    CloudWatchDeleteMetricStreamRequest,
    CloudWatchDeleteMetricStreamResponse,
    CloudWatchDeleteResourceMetricsConfigurationRequest,
    CloudWatchDeleteResourceMetricsConfigurationResponse,
    CloudWatchDescribeAlarmContributorsRequest,
    CloudWatchDescribeAlarmContributorsResponse,
    CloudWatchDescribeAlarmHistoryRequest,
    CloudWatchDescribeAlarmHistoryResponse,
    CloudWatchDescribeAlarmsForMetricRequest,
    CloudWatchDescribeAlarmsForMetricResponse,
    CloudWatchDescribeAnomalyDetectorsRequest,
    CloudWatchDescribeAnomalyDetectorsResponse,
    CloudWatchDescribeInsightRulesRequest,
    CloudWatchDescribeInsightRulesResponse,
    CloudWatchDisableAlarmActionsRequest,
    CloudWatchDisableAlarmActionsResponse,
    CloudWatchDisableInsightRulesRequest,
    CloudWatchDisableInsightRulesResponse,
    CloudWatchDisassociateDatasetKmsKeyRequest,
    CloudWatchDisassociateDatasetKmsKeyResponse,
    CloudWatchEnableAlarmActionsRequest,
    CloudWatchEnableAlarmActionsResponse,
    CloudWatchEnableInsightRulesRequest,
    CloudWatchEnableInsightRulesResponse,
    CloudWatchGetAlarmMuteRuleRequest,
    CloudWatchGetAlarmMuteRuleResponse,
    CloudWatchGetDashboardRequest,
    CloudWatchGetDashboardResponse,
    CloudWatchGetDatasetRequest,
    CloudWatchGetDatasetResponse,
    CloudWatchGetInsightRuleReportRequest,
    CloudWatchGetInsightRuleReportResponse,
    CloudWatchGetMetricDataQueryDefinitionRequest,
    CloudWatchGetMetricDataQueryDefinitionResponse,
    CloudWatchGetMetricStreamRequest,
    CloudWatchGetMetricStreamResponse,
    CloudWatchGetMetricWidgetImageRequest,
    CloudWatchGetMetricWidgetImageResponse,
    CloudWatchGetOTelEnrichmentRequest,
    CloudWatchGetOTelEnrichmentResponse,
    CloudWatchGetResourceMetricsConfigurationRequest,
    CloudWatchGetResourceMetricsConfigurationResponse,
    CloudWatchListAlarmMuteRulesRequest,
    CloudWatchListAlarmMuteRulesResponse,
    CloudWatchListDashboardsRequest,
    CloudWatchListDashboardsResponse,
    CloudWatchListManagedInsightRulesRequest,
    CloudWatchListManagedInsightRulesResponse,
    CloudWatchListMetricDataQueryDefinitionsRequest,
    CloudWatchListMetricDataQueryDefinitionsResponse,
    CloudWatchListMetricStreamsRequest,
    CloudWatchListMetricStreamsResponse,
    CloudWatchListTagsForResourceRequest,
    CloudWatchListTagsForResourceResponse,
    CloudWatchPutAlarmMuteRuleRequest,
    CloudWatchPutAlarmMuteRuleResponse,
    CloudWatchPutAnomalyDetectorRequest,
    CloudWatchPutAnomalyDetectorResponse,
    CloudWatchPutCompositeAlarmRequest,
    CloudWatchPutCompositeAlarmResponse,
    CloudWatchPutDashboardRequest,
    CloudWatchPutDashboardResponse,
    CloudWatchPutInsightRuleRequest,
    CloudWatchPutInsightRuleResponse,
    CloudWatchPutLogAlarmRequest,
    CloudWatchPutLogAlarmResponse,
    CloudWatchPutManagedInsightRulesRequest,
    CloudWatchPutManagedInsightRulesResponse,
    CloudWatchPutMetricDataQueryDefinitionRequest,
    CloudWatchPutMetricDataQueryDefinitionResponse,
    CloudWatchPutMetricStreamRequest,
    CloudWatchPutMetricStreamResponse,
    CloudWatchSetAlarmStateRequest,
    CloudWatchSetAlarmStateResponse,
    CloudWatchStartMetricStreamsRequest,
    CloudWatchStartMetricStreamsResponse,
    CloudWatchStartOTelEnrichmentRequest,
    CloudWatchStartOTelEnrichmentResponse,
    CloudWatchStopMetricStreamsRequest,
    CloudWatchStopMetricStreamsResponse,
    CloudWatchStopOTelEnrichmentRequest,
    CloudWatchStopOTelEnrichmentResponse,
    CloudWatchTagResourceRequest,
    CloudWatchTagResourceResponse,
    CloudWatchUntagResourceRequest,
    CloudWatchUntagResourceResponse,
    CloudWatchUpdateOTelEnrichmentRequest,
    CloudWatchUpdateOTelEnrichmentResponse,
    CloudWatchUpdateResourceMetricsConfigurationRequest,
    CloudWatchUpdateResourceMetricsConfigurationResponse,
)


class AWSCloudwatch(AWSBaseService[CloudWatchClient]):
    service_name = 'CloudWatch'
    boto3_service_name = 'cloudwatch'

    def __init__(self) -> None:
        super().__init__(
            service_name='CloudWatch',
            boto3_service_name='cloudwatch',
        )

    async def get_metric_data(
        self,
        request: CloudWatchGetMetricDataRequest,
    ) -> CloudWatchGetMetricDataResponse:
        client = self._require_client()
        return await self._execute(
            client.get_metric_data,
            request,
            CloudWatchGetMetricDataResponse,
        )

    async def get_metric_data_paginated(
        self,
        request: CloudWatchGetMetricDataRequest,
    ) -> list[CloudWatchGetMetricDataResponse]:
        return await self._paginate(
            'get_metric_data',
            request,
            CloudWatchGetMetricDataResponse,
        )

    async def get_metric_statistics(
        self,
        request: CloudWatchGetMetricStatisticsRequest,
    ) -> CloudWatchGetMetricStatisticsResponse:
        client = self._require_client()
        return await self._execute(
            client.get_metric_statistics,
            request,
            CloudWatchGetMetricStatisticsResponse,
        )

    async def list_metrics(
        self,
        request: CloudWatchListMetricsRequest | None = None,
    ) -> CloudWatchListMetricsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_metrics,
            request or CloudWatchListMetricsRequest(),
            CloudWatchListMetricsResponse,
        )

    async def list_metrics_paginated(
        self,
        request: CloudWatchListMetricsRequest | None = None,
    ) -> list[CloudWatchListMetricsResponse]:
        return await self._paginate(
            'list_metrics',
            request or CloudWatchListMetricsRequest(),
            CloudWatchListMetricsResponse,
        )

    async def put_metric_data(
        self,
        request: CloudWatchPutMetricDataRequest,
    ) -> CloudWatchEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.put_metric_data,
            request,
            CloudWatchEmptyResponse,
        )

    async def describe_alarms(
        self,
        request: CloudWatchDescribeAlarmsRequest | None = None,
    ) -> CloudWatchDescribeAlarmsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_alarms,
            request or CloudWatchDescribeAlarmsRequest(),
            CloudWatchDescribeAlarmsResponse,
        )

    async def describe_alarms_paginated(
        self,
        request: CloudWatchDescribeAlarmsRequest | None = None,
    ) -> list[CloudWatchDescribeAlarmsResponse]:
        return await self._paginate(
            'describe_alarms',
            request or CloudWatchDescribeAlarmsRequest(),
            CloudWatchDescribeAlarmsResponse,
        )

    async def put_metric_alarm(
        self,
        request: CloudWatchPutMetricAlarmRequest,
    ) -> CloudWatchEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.put_metric_alarm,
            request,
            CloudWatchEmptyResponse,
        )

    async def delete_alarms(
        self,
        request: CloudWatchDeleteAlarmsRequest,
    ) -> CloudWatchEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_alarms,
            request,
            CloudWatchEmptyResponse,
        )

    async def associate_dataset_kms_key(
        self,
        request: CloudWatchAssociateDatasetKmsKeyRequest,
    ) -> CloudWatchAssociateDatasetKmsKeyResponse:
        client = self._require_client()
        return await self._execute(client.associate_dataset_kms_key, request, CloudWatchAssociateDatasetKmsKeyResponse)

    async def create_resource_metrics_configuration(
        self,
        request: CloudWatchCreateResourceMetricsConfigurationRequest,
    ) -> CloudWatchCreateResourceMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_metrics_configuration, request, CloudWatchCreateResourceMetricsConfigurationResponse)

    async def delete_alarm_mute_rule(
        self,
        request: CloudWatchDeleteAlarmMuteRuleRequest,
    ) -> CloudWatchDeleteAlarmMuteRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_alarm_mute_rule, request, CloudWatchDeleteAlarmMuteRuleResponse)

    async def delete_anomaly_detector(
        self,
        request: CloudWatchDeleteAnomalyDetectorRequest | None = None,
    ) -> CloudWatchDeleteAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_anomaly_detector, request, CloudWatchDeleteAnomalyDetectorResponse)

    async def delete_dashboards(
        self,
        request: CloudWatchDeleteDashboardsRequest,
    ) -> CloudWatchDeleteDashboardsResponse:
        client = self._require_client()
        return await self._execute(client.delete_dashboards, request, CloudWatchDeleteDashboardsResponse)

    async def delete_insight_rules(
        self,
        request: CloudWatchDeleteInsightRulesRequest,
    ) -> CloudWatchDeleteInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.delete_insight_rules, request, CloudWatchDeleteInsightRulesResponse)

    async def delete_metric_data_query_definition(
        self,
        request: CloudWatchDeleteMetricDataQueryDefinitionRequest,
    ) -> CloudWatchDeleteMetricDataQueryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_data_query_definition, request, CloudWatchDeleteMetricDataQueryDefinitionResponse)

    async def delete_metric_stream(
        self,
        request: CloudWatchDeleteMetricStreamRequest,
    ) -> CloudWatchDeleteMetricStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_stream, request, CloudWatchDeleteMetricStreamResponse)

    async def delete_resource_metrics_configuration(
        self,
        request: CloudWatchDeleteResourceMetricsConfigurationRequest,
    ) -> CloudWatchDeleteResourceMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_metrics_configuration, request, CloudWatchDeleteResourceMetricsConfigurationResponse)

    async def describe_alarm_contributors(
        self,
        request: CloudWatchDescribeAlarmContributorsRequest,
    ) -> CloudWatchDescribeAlarmContributorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_alarm_contributors, request, CloudWatchDescribeAlarmContributorsResponse)

    async def describe_alarm_history(
        self,
        request: CloudWatchDescribeAlarmHistoryRequest | None = None,
    ) -> CloudWatchDescribeAlarmHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_alarm_history, request, CloudWatchDescribeAlarmHistoryResponse)

    async def describe_alarm_history_paginated(
        self,
        request: CloudWatchDescribeAlarmHistoryRequest | None = None,
    ) -> list[CloudWatchDescribeAlarmHistoryResponse]:
        return await self._paginate('describe_alarm_history', request, CloudWatchDescribeAlarmHistoryResponse)

    async def describe_alarms_for_metric(
        self,
        request: CloudWatchDescribeAlarmsForMetricRequest,
    ) -> CloudWatchDescribeAlarmsForMetricResponse:
        client = self._require_client()
        return await self._execute(client.describe_alarms_for_metric, request, CloudWatchDescribeAlarmsForMetricResponse)

    async def describe_anomaly_detectors(
        self,
        request: CloudWatchDescribeAnomalyDetectorsRequest | None = None,
    ) -> CloudWatchDescribeAnomalyDetectorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_anomaly_detectors, request, CloudWatchDescribeAnomalyDetectorsResponse)

    async def describe_anomaly_detectors_paginated(
        self,
        request: CloudWatchDescribeAnomalyDetectorsRequest | None = None,
    ) -> list[CloudWatchDescribeAnomalyDetectorsResponse]:
        return await self._paginate('describe_anomaly_detectors', request, CloudWatchDescribeAnomalyDetectorsResponse)

    async def describe_insight_rules(
        self,
        request: CloudWatchDescribeInsightRulesRequest | None = None,
    ) -> CloudWatchDescribeInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_insight_rules, request, CloudWatchDescribeInsightRulesResponse)

    async def disable_alarm_actions(
        self,
        request: CloudWatchDisableAlarmActionsRequest,
    ) -> CloudWatchDisableAlarmActionsResponse:
        client = self._require_client()
        return await self._execute(client.disable_alarm_actions, request, CloudWatchDisableAlarmActionsResponse)

    async def disable_insight_rules(
        self,
        request: CloudWatchDisableInsightRulesRequest,
    ) -> CloudWatchDisableInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.disable_insight_rules, request, CloudWatchDisableInsightRulesResponse)

    async def disassociate_dataset_kms_key(
        self,
        request: CloudWatchDisassociateDatasetKmsKeyRequest,
    ) -> CloudWatchDisassociateDatasetKmsKeyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_dataset_kms_key, request, CloudWatchDisassociateDatasetKmsKeyResponse)

    async def enable_alarm_actions(
        self,
        request: CloudWatchEnableAlarmActionsRequest,
    ) -> CloudWatchEnableAlarmActionsResponse:
        client = self._require_client()
        return await self._execute(client.enable_alarm_actions, request, CloudWatchEnableAlarmActionsResponse)

    async def enable_insight_rules(
        self,
        request: CloudWatchEnableInsightRulesRequest,
    ) -> CloudWatchEnableInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.enable_insight_rules, request, CloudWatchEnableInsightRulesResponse)

    async def get_alarm_mute_rule(
        self,
        request: CloudWatchGetAlarmMuteRuleRequest,
    ) -> CloudWatchGetAlarmMuteRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_alarm_mute_rule, request, CloudWatchGetAlarmMuteRuleResponse)

    async def get_dashboard(
        self,
        request: CloudWatchGetDashboardRequest,
    ) -> CloudWatchGetDashboardResponse:
        client = self._require_client()
        return await self._execute(client.get_dashboard, request, CloudWatchGetDashboardResponse)

    async def get_dataset(
        self,
        request: CloudWatchGetDatasetRequest,
    ) -> CloudWatchGetDatasetResponse:
        client = self._require_client()
        return await self._execute(client.get_dataset, request, CloudWatchGetDatasetResponse)

    async def get_insight_rule_report(
        self,
        request: CloudWatchGetInsightRuleReportRequest,
    ) -> CloudWatchGetInsightRuleReportResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_rule_report, request, CloudWatchGetInsightRuleReportResponse)

    async def get_metric_data_query_definition(
        self,
        request: CloudWatchGetMetricDataQueryDefinitionRequest,
    ) -> CloudWatchGetMetricDataQueryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.get_metric_data_query_definition, request, CloudWatchGetMetricDataQueryDefinitionResponse)

    async def get_metric_stream(
        self,
        request: CloudWatchGetMetricStreamRequest,
    ) -> CloudWatchGetMetricStreamResponse:
        client = self._require_client()
        return await self._execute(client.get_metric_stream, request, CloudWatchGetMetricStreamResponse)

    async def get_metric_widget_image(
        self,
        request: CloudWatchGetMetricWidgetImageRequest,
    ) -> CloudWatchGetMetricWidgetImageResponse:
        client = self._require_client()
        return await self._execute(client.get_metric_widget_image, request, CloudWatchGetMetricWidgetImageResponse)

    async def get_otel_enrichment(
        self,
        request: CloudWatchGetOTelEnrichmentRequest | None = None,
    ) -> CloudWatchGetOTelEnrichmentResponse:
        client = self._require_client()
        return await self._execute(client.get_otel_enrichment, request, CloudWatchGetOTelEnrichmentResponse)

    async def get_resource_metrics_configuration(
        self,
        request: CloudWatchGetResourceMetricsConfigurationRequest,
    ) -> CloudWatchGetResourceMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_metrics_configuration, request, CloudWatchGetResourceMetricsConfigurationResponse)

    async def list_alarm_mute_rules(
        self,
        request: CloudWatchListAlarmMuteRulesRequest | None = None,
    ) -> CloudWatchListAlarmMuteRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_alarm_mute_rules, request, CloudWatchListAlarmMuteRulesResponse)

    async def list_alarm_mute_rules_paginated(
        self,
        request: CloudWatchListAlarmMuteRulesRequest | None = None,
    ) -> list[CloudWatchListAlarmMuteRulesResponse]:
        return await self._paginate('list_alarm_mute_rules', request, CloudWatchListAlarmMuteRulesResponse)

    async def list_dashboards(
        self,
        request: CloudWatchListDashboardsRequest | None = None,
    ) -> CloudWatchListDashboardsResponse:
        client = self._require_client()
        return await self._execute(client.list_dashboards, request, CloudWatchListDashboardsResponse)

    async def list_dashboards_paginated(
        self,
        request: CloudWatchListDashboardsRequest | None = None,
    ) -> list[CloudWatchListDashboardsResponse]:
        return await self._paginate('list_dashboards', request, CloudWatchListDashboardsResponse)

    async def list_managed_insight_rules(
        self,
        request: CloudWatchListManagedInsightRulesRequest,
    ) -> CloudWatchListManagedInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_managed_insight_rules, request, CloudWatchListManagedInsightRulesResponse)

    async def list_metric_data_query_definitions(
        self,
        request: CloudWatchListMetricDataQueryDefinitionsRequest | None = None,
    ) -> CloudWatchListMetricDataQueryDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_metric_data_query_definitions, request, CloudWatchListMetricDataQueryDefinitionsResponse)

    async def list_metric_data_query_definitions_paginated(
        self,
        request: CloudWatchListMetricDataQueryDefinitionsRequest | None = None,
    ) -> list[CloudWatchListMetricDataQueryDefinitionsResponse]:
        return await self._paginate('list_metric_data_query_definitions', request, CloudWatchListMetricDataQueryDefinitionsResponse)

    async def list_metric_streams(
        self,
        request: CloudWatchListMetricStreamsRequest | None = None,
    ) -> CloudWatchListMetricStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_metric_streams, request, CloudWatchListMetricStreamsResponse)

    async def list_tags_for_resource(
        self,
        request: CloudWatchListTagsForResourceRequest,
    ) -> CloudWatchListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CloudWatchListTagsForResourceResponse)

    async def put_alarm_mute_rule(
        self,
        request: CloudWatchPutAlarmMuteRuleRequest,
    ) -> CloudWatchPutAlarmMuteRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_alarm_mute_rule, request, CloudWatchPutAlarmMuteRuleResponse)

    async def put_anomaly_detector(
        self,
        request: CloudWatchPutAnomalyDetectorRequest | None = None,
    ) -> CloudWatchPutAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.put_anomaly_detector, request, CloudWatchPutAnomalyDetectorResponse)

    async def put_composite_alarm(
        self,
        request: CloudWatchPutCompositeAlarmRequest,
    ) -> CloudWatchPutCompositeAlarmResponse:
        client = self._require_client()
        return await self._execute(client.put_composite_alarm, request, CloudWatchPutCompositeAlarmResponse)

    async def put_dashboard(
        self,
        request: CloudWatchPutDashboardRequest,
    ) -> CloudWatchPutDashboardResponse:
        client = self._require_client()
        return await self._execute(client.put_dashboard, request, CloudWatchPutDashboardResponse)

    async def put_insight_rule(
        self,
        request: CloudWatchPutInsightRuleRequest,
    ) -> CloudWatchPutInsightRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_insight_rule, request, CloudWatchPutInsightRuleResponse)

    async def put_log_alarm(
        self,
        request: CloudWatchPutLogAlarmRequest,
    ) -> CloudWatchPutLogAlarmResponse:
        client = self._require_client()
        return await self._execute(client.put_log_alarm, request, CloudWatchPutLogAlarmResponse)

    async def put_managed_insight_rules(
        self,
        request: CloudWatchPutManagedInsightRulesRequest,
    ) -> CloudWatchPutManagedInsightRulesResponse:
        client = self._require_client()
        return await self._execute(client.put_managed_insight_rules, request, CloudWatchPutManagedInsightRulesResponse)

    async def put_metric_data_query_definition(
        self,
        request: CloudWatchPutMetricDataQueryDefinitionRequest,
    ) -> CloudWatchPutMetricDataQueryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.put_metric_data_query_definition, request, CloudWatchPutMetricDataQueryDefinitionResponse)

    async def put_metric_stream(
        self,
        request: CloudWatchPutMetricStreamRequest,
    ) -> CloudWatchPutMetricStreamResponse:
        client = self._require_client()
        return await self._execute(client.put_metric_stream, request, CloudWatchPutMetricStreamResponse)

    async def set_alarm_state(
        self,
        request: CloudWatchSetAlarmStateRequest,
    ) -> CloudWatchSetAlarmStateResponse:
        client = self._require_client()
        return await self._execute(client.set_alarm_state, request, CloudWatchSetAlarmStateResponse)

    async def start_metric_streams(
        self,
        request: CloudWatchStartMetricStreamsRequest,
    ) -> CloudWatchStartMetricStreamsResponse:
        client = self._require_client()
        return await self._execute(client.start_metric_streams, request, CloudWatchStartMetricStreamsResponse)

    async def start_otel_enrichment(
        self,
        request: CloudWatchStartOTelEnrichmentRequest | None = None,
    ) -> CloudWatchStartOTelEnrichmentResponse:
        client = self._require_client()
        return await self._execute(client.start_otel_enrichment, request, CloudWatchStartOTelEnrichmentResponse)

    async def stop_metric_streams(
        self,
        request: CloudWatchStopMetricStreamsRequest,
    ) -> CloudWatchStopMetricStreamsResponse:
        client = self._require_client()
        return await self._execute(client.stop_metric_streams, request, CloudWatchStopMetricStreamsResponse)

    async def stop_otel_enrichment(
        self,
        request: CloudWatchStopOTelEnrichmentRequest | None = None,
    ) -> CloudWatchStopOTelEnrichmentResponse:
        client = self._require_client()
        return await self._execute(client.stop_otel_enrichment, request, CloudWatchStopOTelEnrichmentResponse)

    async def tag_resource(
        self,
        request: CloudWatchTagResourceRequest,
    ) -> CloudWatchTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CloudWatchTagResourceResponse)

    async def untag_resource(
        self,
        request: CloudWatchUntagResourceRequest,
    ) -> CloudWatchUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CloudWatchUntagResourceResponse)

    async def update_otel_enrichment(
        self,
        request: CloudWatchUpdateOTelEnrichmentRequest | None = None,
    ) -> CloudWatchUpdateOTelEnrichmentResponse:
        client = self._require_client()
        return await self._execute(client.update_otel_enrichment, request, CloudWatchUpdateOTelEnrichmentResponse)

    async def update_resource_metrics_configuration(
        self,
        request: CloudWatchUpdateResourceMetricsConfigurationRequest,
    ) -> CloudWatchUpdateResourceMetricsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_metrics_configuration, request, CloudWatchUpdateResourceMetricsConfigurationResponse)

