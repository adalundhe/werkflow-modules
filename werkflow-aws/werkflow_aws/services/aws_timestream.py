from werkflow_aws.models.timestream import (
    TimestreamWriteCreateBatchLoadTaskRequest,
    TimestreamWriteCreateBatchLoadTaskResponse,
    TimestreamWriteCreateDatabaseRequest,
    TimestreamWriteCreateDatabaseResponse,
    TimestreamWriteCreateTableRequest,
    TimestreamWriteCreateTableResponse,
    TimestreamWriteDeleteDatabaseRequest,
    TimestreamWriteDeleteDatabaseResponse,
    TimestreamWriteDeleteTableRequest,
    TimestreamWriteDeleteTableResponse,
    TimestreamWriteDescribeBatchLoadTaskRequest,
    TimestreamWriteDescribeBatchLoadTaskResponse,
    TimestreamWriteDescribeDatabaseRequest,
    TimestreamWriteDescribeDatabaseResponse,
    TimestreamWriteDescribeEndpointsRequest,
    TimestreamWriteDescribeEndpointsResponse,
    TimestreamWriteDescribeTableRequest,
    TimestreamWriteDescribeTableResponse,
    TimestreamWriteListBatchLoadTasksRequest,
    TimestreamWriteListBatchLoadTasksResponse,
    TimestreamWriteListDatabasesRequest,
    TimestreamWriteListDatabasesResponse,
    TimestreamWriteListTablesRequest,
    TimestreamWriteListTablesResponse,
    TimestreamWriteListTagsForResourceRequest,
    TimestreamWriteListTagsForResourceResponse,
    TimestreamWriteResumeBatchLoadTaskRequest,
    TimestreamWriteResumeBatchLoadTaskResponse,
    TimestreamWriteTagResourceRequest,
    TimestreamWriteTagResourceResponse,
    TimestreamWriteUntagResourceRequest,
    TimestreamWriteUntagResourceResponse,
    TimestreamWriteUpdateDatabaseRequest,
    TimestreamWriteUpdateDatabaseResponse,
    TimestreamWriteUpdateTableRequest,
    TimestreamWriteUpdateTableResponse,
    TimestreamWriteWriteRecordsRequest,
    TimestreamWriteWriteRecordsResponse,
)
from werkflow_aws.types.timestream_client import TimestreamWriteClient
from .base import AWSBaseService


class AWSTimestreamWrite(AWSBaseService[TimestreamWriteClient]):
    service_name = 'timestream'
    boto3_service_name = 'timestream-write'

    def __init__(self) -> None:
        super().__init__(service_name='timestream', boto3_service_name='timestream-write')

    async def create_batch_load_task(
        self,
        request: TimestreamWriteCreateBatchLoadTaskRequest,
    ) -> TimestreamWriteCreateBatchLoadTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_batch_load_task, request, TimestreamWriteCreateBatchLoadTaskResponse)

    async def create_database(
        self,
        request: TimestreamWriteCreateDatabaseRequest,
    ) -> TimestreamWriteCreateDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.create_database, request, TimestreamWriteCreateDatabaseResponse)

    async def create_table(
        self,
        request: TimestreamWriteCreateTableRequest,
    ) -> TimestreamWriteCreateTableResponse:
        client = self._require_client()
        return await self._execute(client.create_table, request, TimestreamWriteCreateTableResponse)

    async def delete_database(
        self,
        request: TimestreamWriteDeleteDatabaseRequest,
    ) -> TimestreamWriteDeleteDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_database, request, TimestreamWriteDeleteDatabaseResponse)

    async def delete_table(
        self,
        request: TimestreamWriteDeleteTableRequest,
    ) -> TimestreamWriteDeleteTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_table, request, TimestreamWriteDeleteTableResponse)

    async def describe_batch_load_task(
        self,
        request: TimestreamWriteDescribeBatchLoadTaskRequest,
    ) -> TimestreamWriteDescribeBatchLoadTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_batch_load_task, request, TimestreamWriteDescribeBatchLoadTaskResponse)

    async def describe_database(
        self,
        request: TimestreamWriteDescribeDatabaseRequest,
    ) -> TimestreamWriteDescribeDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.describe_database, request, TimestreamWriteDescribeDatabaseResponse)

    async def describe_endpoints(
        self,
        request: TimestreamWriteDescribeEndpointsRequest | None = None,
    ) -> TimestreamWriteDescribeEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoints, request, TimestreamWriteDescribeEndpointsResponse)

    async def describe_table(
        self,
        request: TimestreamWriteDescribeTableRequest,
    ) -> TimestreamWriteDescribeTableResponse:
        client = self._require_client()
        return await self._execute(client.describe_table, request, TimestreamWriteDescribeTableResponse)

    async def list_batch_load_tasks(
        self,
        request: TimestreamWriteListBatchLoadTasksRequest | None = None,
    ) -> TimestreamWriteListBatchLoadTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_batch_load_tasks, request, TimestreamWriteListBatchLoadTasksResponse)

    async def list_databases(
        self,
        request: TimestreamWriteListDatabasesRequest | None = None,
    ) -> TimestreamWriteListDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.list_databases, request, TimestreamWriteListDatabasesResponse)

    async def list_tables(
        self,
        request: TimestreamWriteListTablesRequest | None = None,
    ) -> TimestreamWriteListTablesResponse:
        client = self._require_client()
        return await self._execute(client.list_tables, request, TimestreamWriteListTablesResponse)

    async def list_tags_for_resource(
        self,
        request: TimestreamWriteListTagsForResourceRequest,
    ) -> TimestreamWriteListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TimestreamWriteListTagsForResourceResponse)

    async def resume_batch_load_task(
        self,
        request: TimestreamWriteResumeBatchLoadTaskRequest,
    ) -> TimestreamWriteResumeBatchLoadTaskResponse:
        client = self._require_client()
        return await self._execute(client.resume_batch_load_task, request, TimestreamWriteResumeBatchLoadTaskResponse)

    async def tag_resource(
        self,
        request: TimestreamWriteTagResourceRequest,
    ) -> TimestreamWriteTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TimestreamWriteTagResourceResponse)

    async def untag_resource(
        self,
        request: TimestreamWriteUntagResourceRequest,
    ) -> TimestreamWriteUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TimestreamWriteUntagResourceResponse)

    async def update_database(
        self,
        request: TimestreamWriteUpdateDatabaseRequest,
    ) -> TimestreamWriteUpdateDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.update_database, request, TimestreamWriteUpdateDatabaseResponse)

    async def update_table(
        self,
        request: TimestreamWriteUpdateTableRequest,
    ) -> TimestreamWriteUpdateTableResponse:
        client = self._require_client()
        return await self._execute(client.update_table, request, TimestreamWriteUpdateTableResponse)

    async def write_records(
        self,
        request: TimestreamWriteWriteRecordsRequest,
    ) -> TimestreamWriteWriteRecordsResponse:
        client = self._require_client()
        return await self._execute(client.write_records, request, TimestreamWriteWriteRecordsResponse)
