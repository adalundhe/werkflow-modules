from werkflow_aws.models.timestream_query import (
    TimestreamQueryCancelQueryRequest,
    TimestreamQueryCancelQueryResponse,
    TimestreamQueryCreateScheduledQueryRequest,
    TimestreamQueryCreateScheduledQueryResponse,
    TimestreamQueryDeleteScheduledQueryRequest,
    TimestreamQueryDeleteScheduledQueryResponse,
    TimestreamQueryDescribeAccountSettingsRequest,
    TimestreamQueryDescribeAccountSettingsResponse,
    TimestreamQueryDescribeEndpointsRequest,
    TimestreamQueryDescribeEndpointsResponse,
    TimestreamQueryDescribeScheduledQueryRequest,
    TimestreamQueryDescribeScheduledQueryResponse,
    TimestreamQueryExecuteScheduledQueryRequest,
    TimestreamQueryExecuteScheduledQueryResponse,
    TimestreamQueryListScheduledQueriesRequest,
    TimestreamQueryListScheduledQueriesResponse,
    TimestreamQueryListTagsForResourceRequest,
    TimestreamQueryListTagsForResourceResponse,
    TimestreamQueryPrepareQueryRequest,
    TimestreamQueryPrepareQueryResponse,
    TimestreamQueryQueryRequest,
    TimestreamQueryQueryResponse,
    TimestreamQueryTagResourceRequest,
    TimestreamQueryTagResourceResponse,
    TimestreamQueryUntagResourceRequest,
    TimestreamQueryUntagResourceResponse,
    TimestreamQueryUpdateAccountSettingsRequest,
    TimestreamQueryUpdateAccountSettingsResponse,
    TimestreamQueryUpdateScheduledQueryRequest,
    TimestreamQueryUpdateScheduledQueryResponse,
)
from werkflow_aws.types.timestream_query_client import TimestreamQueryClient
from .base import AWSBaseService


class AWSTimestreamQuery(AWSBaseService[TimestreamQueryClient]):
    service_name = 'timestream-query'
    boto3_service_name = 'timestream-query'

    def __init__(self) -> None:
        super().__init__(service_name='timestream-query', boto3_service_name='timestream-query')

    async def cancel_query(
        self,
        request: TimestreamQueryCancelQueryRequest,
    ) -> TimestreamQueryCancelQueryResponse:
        client = self._require_client()
        return await self._execute(client.cancel_query, request, TimestreamQueryCancelQueryResponse)

    async def create_scheduled_query(
        self,
        request: TimestreamQueryCreateScheduledQueryRequest,
    ) -> TimestreamQueryCreateScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.create_scheduled_query, request, TimestreamQueryCreateScheduledQueryResponse)

    async def delete_scheduled_query(
        self,
        request: TimestreamQueryDeleteScheduledQueryRequest,
    ) -> TimestreamQueryDeleteScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduled_query, request, TimestreamQueryDeleteScheduledQueryResponse)

    async def describe_account_settings(
        self,
        request: TimestreamQueryDescribeAccountSettingsRequest | None = None,
    ) -> TimestreamQueryDescribeAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_settings, request, TimestreamQueryDescribeAccountSettingsResponse)

    async def describe_endpoints(
        self,
        request: TimestreamQueryDescribeEndpointsRequest | None = None,
    ) -> TimestreamQueryDescribeEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoints, request, TimestreamQueryDescribeEndpointsResponse)

    async def describe_scheduled_query(
        self,
        request: TimestreamQueryDescribeScheduledQueryRequest,
    ) -> TimestreamQueryDescribeScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduled_query, request, TimestreamQueryDescribeScheduledQueryResponse)

    async def execute_scheduled_query(
        self,
        request: TimestreamQueryExecuteScheduledQueryRequest,
    ) -> TimestreamQueryExecuteScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.execute_scheduled_query, request, TimestreamQueryExecuteScheduledQueryResponse)

    async def list_scheduled_queries(
        self,
        request: TimestreamQueryListScheduledQueriesRequest | None = None,
    ) -> TimestreamQueryListScheduledQueriesResponse:
        client = self._require_client()
        return await self._execute(client.list_scheduled_queries, request, TimestreamQueryListScheduledQueriesResponse)

    async def list_scheduled_queries_paginated(
        self,
        request: TimestreamQueryListScheduledQueriesRequest | None = None,
    ) -> list[TimestreamQueryListScheduledQueriesResponse]:
        return await self._paginate('list_scheduled_queries', request, TimestreamQueryListScheduledQueriesResponse)

    async def list_tags_for_resource(
        self,
        request: TimestreamQueryListTagsForResourceRequest,
    ) -> TimestreamQueryListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TimestreamQueryListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: TimestreamQueryListTagsForResourceRequest,
    ) -> list[TimestreamQueryListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, TimestreamQueryListTagsForResourceResponse)

    async def prepare_query(
        self,
        request: TimestreamQueryPrepareQueryRequest,
    ) -> TimestreamQueryPrepareQueryResponse:
        client = self._require_client()
        return await self._execute(client.prepare_query, request, TimestreamQueryPrepareQueryResponse)

    async def query(
        self,
        request: TimestreamQueryQueryRequest,
    ) -> TimestreamQueryQueryResponse:
        client = self._require_client()
        return await self._execute(client.query, request, TimestreamQueryQueryResponse)

    async def query_paginated(
        self,
        request: TimestreamQueryQueryRequest,
    ) -> list[TimestreamQueryQueryResponse]:
        return await self._paginate('query', request, TimestreamQueryQueryResponse)

    async def tag_resource(
        self,
        request: TimestreamQueryTagResourceRequest,
    ) -> TimestreamQueryTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TimestreamQueryTagResourceResponse)

    async def untag_resource(
        self,
        request: TimestreamQueryUntagResourceRequest,
    ) -> TimestreamQueryUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TimestreamQueryUntagResourceResponse)

    async def update_account_settings(
        self,
        request: TimestreamQueryUpdateAccountSettingsRequest | None = None,
    ) -> TimestreamQueryUpdateAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_account_settings, request, TimestreamQueryUpdateAccountSettingsResponse)

    async def update_scheduled_query(
        self,
        request: TimestreamQueryUpdateScheduledQueryRequest,
    ) -> TimestreamQueryUpdateScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.update_scheduled_query, request, TimestreamQueryUpdateScheduledQueryResponse)
