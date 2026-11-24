from werkflow_aws.models.xray import (
    XRayBatchGetTracesRequest,
    XRayBatchGetTracesResponse,
    XRayCancelTraceRetrievalRequest,
    XRayCancelTraceRetrievalResponse,
    XRayCreateGroupRequest,
    XRayCreateGroupResponse,
    XRayCreateSamplingRuleRequest,
    XRayCreateSamplingRuleResponse,
    XRayDeleteGroupRequest,
    XRayDeleteGroupResponse,
    XRayDeleteResourcePolicyRequest,
    XRayDeleteResourcePolicyResponse,
    XRayDeleteSamplingRuleRequest,
    XRayDeleteSamplingRuleResponse,
    XRayGetEncryptionConfigRequest,
    XRayGetEncryptionConfigResponse,
    XRayGetGroupRequest,
    XRayGetGroupResponse,
    XRayGetGroupsRequest,
    XRayGetGroupsResponse,
    XRayGetIndexingRulesRequest,
    XRayGetIndexingRulesResponse,
    XRayGetInsightEventsRequest,
    XRayGetInsightEventsResponse,
    XRayGetInsightImpactGraphRequest,
    XRayGetInsightImpactGraphResponse,
    XRayGetInsightRequest,
    XRayGetInsightResponse,
    XRayGetInsightSummariesRequest,
    XRayGetInsightSummariesResponse,
    XRayGetRetrievedTracesGraphRequest,
    XRayGetRetrievedTracesGraphResponse,
    XRayGetSamplingRulesRequest,
    XRayGetSamplingRulesResponse,
    XRayGetSamplingStatisticSummariesRequest,
    XRayGetSamplingStatisticSummariesResponse,
    XRayGetSamplingTargetsRequest,
    XRayGetSamplingTargetsResponse,
    XRayGetServiceGraphRequest,
    XRayGetServiceGraphResponse,
    XRayGetTimeSeriesServiceStatisticsRequest,
    XRayGetTimeSeriesServiceStatisticsResponse,
    XRayGetTraceGraphRequest,
    XRayGetTraceGraphResponse,
    XRayGetTraceSegmentDestinationRequest,
    XRayGetTraceSegmentDestinationResponse,
    XRayGetTraceSummariesRequest,
    XRayGetTraceSummariesResponse,
    XRayListResourcePoliciesRequest,
    XRayListResourcePoliciesResponse,
    XRayListRetrievedTracesRequest,
    XRayListRetrievedTracesResponse,
    XRayListTagsForResourceRequest,
    XRayListTagsForResourceResponse,
    XRayPutEncryptionConfigRequest,
    XRayPutEncryptionConfigResponse,
    XRayPutResourcePolicyRequest,
    XRayPutResourcePolicyResponse,
    XRayPutTelemetryRecordsRequest,
    XRayPutTelemetryRecordsResponse,
    XRayPutTraceSegmentsRequest,
    XRayPutTraceSegmentsResponse,
    XRayStartTraceRetrievalRequest,
    XRayStartTraceRetrievalResponse,
    XRayTagResourceRequest,
    XRayTagResourceResponse,
    XRayUntagResourceRequest,
    XRayUntagResourceResponse,
    XRayUpdateGroupRequest,
    XRayUpdateGroupResponse,
    XRayUpdateIndexingRuleRequest,
    XRayUpdateIndexingRuleResponse,
    XRayUpdateSamplingRuleRequest,
    XRayUpdateSamplingRuleResponse,
    XRayUpdateTraceSegmentDestinationRequest,
    XRayUpdateTraceSegmentDestinationResponse,
)
from werkflow_aws.types.xray_client import XRayClient
from .base import AWSBaseService


class AWSXRay(AWSBaseService[XRayClient]):
    service_name = 'xray'
    boto3_service_name = 'xray'

    def __init__(self) -> None:
        super().__init__(service_name='xray', boto3_service_name='xray')

    async def batch_get_traces(
        self,
        request: XRayBatchGetTracesRequest,
    ) -> XRayBatchGetTracesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_traces, request, XRayBatchGetTracesResponse)

    async def batch_get_traces_paginated(
        self,
        request: XRayBatchGetTracesRequest,
    ) -> list[XRayBatchGetTracesResponse]:
        return await self._paginate('batch_get_traces', request, XRayBatchGetTracesResponse)

    async def cancel_trace_retrieval(
        self,
        request: XRayCancelTraceRetrievalRequest,
    ) -> XRayCancelTraceRetrievalResponse:
        client = self._require_client()
        return await self._execute(client.cancel_trace_retrieval, request, XRayCancelTraceRetrievalResponse)

    async def create_group(
        self,
        request: XRayCreateGroupRequest,
    ) -> XRayCreateGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_group, request, XRayCreateGroupResponse)

    async def create_sampling_rule(
        self,
        request: XRayCreateSamplingRuleRequest,
    ) -> XRayCreateSamplingRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_sampling_rule, request, XRayCreateSamplingRuleResponse)

    async def delete_group(
        self,
        request: XRayDeleteGroupRequest | None = None,
    ) -> XRayDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_group, request, XRayDeleteGroupResponse)

    async def delete_resource_policy(
        self,
        request: XRayDeleteResourcePolicyRequest,
    ) -> XRayDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, XRayDeleteResourcePolicyResponse)

    async def delete_sampling_rule(
        self,
        request: XRayDeleteSamplingRuleRequest | None = None,
    ) -> XRayDeleteSamplingRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_sampling_rule, request, XRayDeleteSamplingRuleResponse)

    async def get_encryption_config(
        self,
        request: XRayGetEncryptionConfigRequest | None = None,
    ) -> XRayGetEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_encryption_config, request, XRayGetEncryptionConfigResponse)

    async def get_group(
        self,
        request: XRayGetGroupRequest | None = None,
    ) -> XRayGetGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_group, request, XRayGetGroupResponse)

    async def get_groups(
        self,
        request: XRayGetGroupsRequest | None = None,
    ) -> XRayGetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.get_groups, request, XRayGetGroupsResponse)

    async def get_groups_paginated(
        self,
        request: XRayGetGroupsRequest | None = None,
    ) -> list[XRayGetGroupsResponse]:
        return await self._paginate('get_groups', request, XRayGetGroupsResponse)

    async def get_indexing_rules(
        self,
        request: XRayGetIndexingRulesRequest | None = None,
    ) -> XRayGetIndexingRulesResponse:
        client = self._require_client()
        return await self._execute(client.get_indexing_rules, request, XRayGetIndexingRulesResponse)

    async def get_insight(
        self,
        request: XRayGetInsightRequest,
    ) -> XRayGetInsightResponse:
        client = self._require_client()
        return await self._execute(client.get_insight, request, XRayGetInsightResponse)

    async def get_insight_events(
        self,
        request: XRayGetInsightEventsRequest,
    ) -> XRayGetInsightEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_events, request, XRayGetInsightEventsResponse)

    async def get_insight_impact_graph(
        self,
        request: XRayGetInsightImpactGraphRequest,
    ) -> XRayGetInsightImpactGraphResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_impact_graph, request, XRayGetInsightImpactGraphResponse)

    async def get_insight_summaries(
        self,
        request: XRayGetInsightSummariesRequest,
    ) -> XRayGetInsightSummariesResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_summaries, request, XRayGetInsightSummariesResponse)

    async def get_retrieved_traces_graph(
        self,
        request: XRayGetRetrievedTracesGraphRequest,
    ) -> XRayGetRetrievedTracesGraphResponse:
        client = self._require_client()
        return await self._execute(client.get_retrieved_traces_graph, request, XRayGetRetrievedTracesGraphResponse)

    async def get_sampling_rules(
        self,
        request: XRayGetSamplingRulesRequest | None = None,
    ) -> XRayGetSamplingRulesResponse:
        client = self._require_client()
        return await self._execute(client.get_sampling_rules, request, XRayGetSamplingRulesResponse)

    async def get_sampling_rules_paginated(
        self,
        request: XRayGetSamplingRulesRequest | None = None,
    ) -> list[XRayGetSamplingRulesResponse]:
        return await self._paginate('get_sampling_rules', request, XRayGetSamplingRulesResponse)

    async def get_sampling_statistic_summaries(
        self,
        request: XRayGetSamplingStatisticSummariesRequest | None = None,
    ) -> XRayGetSamplingStatisticSummariesResponse:
        client = self._require_client()
        return await self._execute(client.get_sampling_statistic_summaries, request, XRayGetSamplingStatisticSummariesResponse)

    async def get_sampling_statistic_summaries_paginated(
        self,
        request: XRayGetSamplingStatisticSummariesRequest | None = None,
    ) -> list[XRayGetSamplingStatisticSummariesResponse]:
        return await self._paginate('get_sampling_statistic_summaries', request, XRayGetSamplingStatisticSummariesResponse)

    async def get_sampling_targets(
        self,
        request: XRayGetSamplingTargetsRequest,
    ) -> XRayGetSamplingTargetsResponse:
        client = self._require_client()
        return await self._execute(client.get_sampling_targets, request, XRayGetSamplingTargetsResponse)

    async def get_service_graph(
        self,
        request: XRayGetServiceGraphRequest,
    ) -> XRayGetServiceGraphResponse:
        client = self._require_client()
        return await self._execute(client.get_service_graph, request, XRayGetServiceGraphResponse)

    async def get_service_graph_paginated(
        self,
        request: XRayGetServiceGraphRequest,
    ) -> list[XRayGetServiceGraphResponse]:
        return await self._paginate('get_service_graph', request, XRayGetServiceGraphResponse)

    async def get_time_series_service_statistics(
        self,
        request: XRayGetTimeSeriesServiceStatisticsRequest,
    ) -> XRayGetTimeSeriesServiceStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_time_series_service_statistics, request, XRayGetTimeSeriesServiceStatisticsResponse)

    async def get_time_series_service_statistics_paginated(
        self,
        request: XRayGetTimeSeriesServiceStatisticsRequest,
    ) -> list[XRayGetTimeSeriesServiceStatisticsResponse]:
        return await self._paginate('get_time_series_service_statistics', request, XRayGetTimeSeriesServiceStatisticsResponse)

    async def get_trace_graph(
        self,
        request: XRayGetTraceGraphRequest,
    ) -> XRayGetTraceGraphResponse:
        client = self._require_client()
        return await self._execute(client.get_trace_graph, request, XRayGetTraceGraphResponse)

    async def get_trace_graph_paginated(
        self,
        request: XRayGetTraceGraphRequest,
    ) -> list[XRayGetTraceGraphResponse]:
        return await self._paginate('get_trace_graph', request, XRayGetTraceGraphResponse)

    async def get_trace_segment_destination(
        self,
        request: XRayGetTraceSegmentDestinationRequest | None = None,
    ) -> XRayGetTraceSegmentDestinationResponse:
        client = self._require_client()
        return await self._execute(client.get_trace_segment_destination, request, XRayGetTraceSegmentDestinationResponse)

    async def get_trace_summaries(
        self,
        request: XRayGetTraceSummariesRequest,
    ) -> XRayGetTraceSummariesResponse:
        client = self._require_client()
        return await self._execute(client.get_trace_summaries, request, XRayGetTraceSummariesResponse)

    async def get_trace_summaries_paginated(
        self,
        request: XRayGetTraceSummariesRequest,
    ) -> list[XRayGetTraceSummariesResponse]:
        return await self._paginate('get_trace_summaries', request, XRayGetTraceSummariesResponse)

    async def list_resource_policies(
        self,
        request: XRayListResourcePoliciesRequest | None = None,
    ) -> XRayListResourcePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_policies, request, XRayListResourcePoliciesResponse)

    async def list_resource_policies_paginated(
        self,
        request: XRayListResourcePoliciesRequest | None = None,
    ) -> list[XRayListResourcePoliciesResponse]:
        return await self._paginate('list_resource_policies', request, XRayListResourcePoliciesResponse)

    async def list_retrieved_traces(
        self,
        request: XRayListRetrievedTracesRequest,
    ) -> XRayListRetrievedTracesResponse:
        client = self._require_client()
        return await self._execute(client.list_retrieved_traces, request, XRayListRetrievedTracesResponse)

    async def list_tags_for_resource(
        self,
        request: XRayListTagsForResourceRequest,
    ) -> XRayListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, XRayListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: XRayListTagsForResourceRequest,
    ) -> list[XRayListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, XRayListTagsForResourceResponse)

    async def put_encryption_config(
        self,
        request: XRayPutEncryptionConfigRequest,
    ) -> XRayPutEncryptionConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_encryption_config, request, XRayPutEncryptionConfigResponse)

    async def put_resource_policy(
        self,
        request: XRayPutResourcePolicyRequest,
    ) -> XRayPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, XRayPutResourcePolicyResponse)

    async def put_telemetry_records(
        self,
        request: XRayPutTelemetryRecordsRequest,
    ) -> XRayPutTelemetryRecordsResponse:
        client = self._require_client()
        return await self._execute(client.put_telemetry_records, request, XRayPutTelemetryRecordsResponse)

    async def put_trace_segments(
        self,
        request: XRayPutTraceSegmentsRequest,
    ) -> XRayPutTraceSegmentsResponse:
        client = self._require_client()
        return await self._execute(client.put_trace_segments, request, XRayPutTraceSegmentsResponse)

    async def start_trace_retrieval(
        self,
        request: XRayStartTraceRetrievalRequest,
    ) -> XRayStartTraceRetrievalResponse:
        client = self._require_client()
        return await self._execute(client.start_trace_retrieval, request, XRayStartTraceRetrievalResponse)

    async def tag_resource(
        self,
        request: XRayTagResourceRequest,
    ) -> XRayTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, XRayTagResourceResponse)

    async def untag_resource(
        self,
        request: XRayUntagResourceRequest,
    ) -> XRayUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, XRayUntagResourceResponse)

    async def update_group(
        self,
        request: XRayUpdateGroupRequest | None = None,
    ) -> XRayUpdateGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_group, request, XRayUpdateGroupResponse)

    async def update_indexing_rule(
        self,
        request: XRayUpdateIndexingRuleRequest,
    ) -> XRayUpdateIndexingRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_indexing_rule, request, XRayUpdateIndexingRuleResponse)

    async def update_sampling_rule(
        self,
        request: XRayUpdateSamplingRuleRequest,
    ) -> XRayUpdateSamplingRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_sampling_rule, request, XRayUpdateSamplingRuleResponse)

    async def update_trace_segment_destination(
        self,
        request: XRayUpdateTraceSegmentDestinationRequest | None = None,
    ) -> XRayUpdateTraceSegmentDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_trace_segment_destination, request, XRayUpdateTraceSegmentDestinationResponse)
