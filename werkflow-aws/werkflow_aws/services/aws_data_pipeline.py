from werkflow_aws.models.data_pipeline import (
    DataPipelineActivatePipelineRequest,
    DataPipelineActivatePipelineResponse,
    DataPipelineAddTagsRequest,
    DataPipelineAddTagsResponse,
    DataPipelineCreatePipelineRequest,
    DataPipelineCreatePipelineResponse,
    DataPipelineDeactivatePipelineRequest,
    DataPipelineDeactivatePipelineResponse,
    DataPipelineDeletePipelineRequest,
    DataPipelineDeletePipelineResponse,
    DataPipelineDescribeObjectsRequest,
    DataPipelineDescribeObjectsResponse,
    DataPipelineDescribePipelinesRequest,
    DataPipelineDescribePipelinesResponse,
    DataPipelineEvaluateExpressionRequest,
    DataPipelineEvaluateExpressionResponse,
    DataPipelineGetPipelineDefinitionRequest,
    DataPipelineGetPipelineDefinitionResponse,
    DataPipelineListPipelinesRequest,
    DataPipelineListPipelinesResponse,
    DataPipelinePollForTaskRequest,
    DataPipelinePollForTaskResponse,
    DataPipelinePutPipelineDefinitionRequest,
    DataPipelinePutPipelineDefinitionResponse,
    DataPipelineQueryObjectsRequest,
    DataPipelineQueryObjectsResponse,
    DataPipelineRemoveTagsRequest,
    DataPipelineRemoveTagsResponse,
    DataPipelineReportTaskProgressRequest,
    DataPipelineReportTaskProgressResponse,
    DataPipelineReportTaskRunnerHeartbeatRequest,
    DataPipelineReportTaskRunnerHeartbeatResponse,
    DataPipelineSetStatusRequest,
    DataPipelineSetStatusResponse,
    DataPipelineSetTaskStatusRequest,
    DataPipelineSetTaskStatusResponse,
    DataPipelineValidatePipelineDefinitionRequest,
    DataPipelineValidatePipelineDefinitionResponse,
)
from werkflow_aws.types.data_pipeline_client import DataPipelineClient
from .base import AWSBaseService


class AWSDataPipeline(AWSBaseService[DataPipelineClient]):
    service_name = 'data-pipeline'
    boto3_service_name = 'datapipeline'

    def __init__(self) -> None:
        super().__init__(service_name='data-pipeline', boto3_service_name='datapipeline')

    async def activate_pipeline(
        self,
        request: DataPipelineActivatePipelineRequest,
    ) -> DataPipelineActivatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.activate_pipeline, request, DataPipelineActivatePipelineResponse)

    async def add_tags(
        self,
        request: DataPipelineAddTagsRequest,
    ) -> DataPipelineAddTagsResponse:
        client = self._require_client()
        return await self._execute(client.add_tags, request, DataPipelineAddTagsResponse)

    async def create_pipeline(
        self,
        request: DataPipelineCreatePipelineRequest,
    ) -> DataPipelineCreatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.create_pipeline, request, DataPipelineCreatePipelineResponse)

    async def deactivate_pipeline(
        self,
        request: DataPipelineDeactivatePipelineRequest,
    ) -> DataPipelineDeactivatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_pipeline, request, DataPipelineDeactivatePipelineResponse)

    async def delete_pipeline(
        self,
        request: DataPipelineDeletePipelineRequest,
    ) -> DataPipelineDeletePipelineResponse:
        client = self._require_client()
        return await self._execute(client.delete_pipeline, request, DataPipelineDeletePipelineResponse)

    async def describe_objects(
        self,
        request: DataPipelineDescribeObjectsRequest,
    ) -> DataPipelineDescribeObjectsResponse:
        client = self._require_client()
        return await self._execute(client.describe_objects, request, DataPipelineDescribeObjectsResponse)

    async def describe_objects_paginated(
        self,
        request: DataPipelineDescribeObjectsRequest,
    ) -> list[DataPipelineDescribeObjectsResponse]:
        return await self._paginate('describe_objects', request, DataPipelineDescribeObjectsResponse)

    async def describe_pipelines(
        self,
        request: DataPipelineDescribePipelinesRequest,
    ) -> DataPipelineDescribePipelinesResponse:
        client = self._require_client()
        return await self._execute(client.describe_pipelines, request, DataPipelineDescribePipelinesResponse)

    async def evaluate_expression(
        self,
        request: DataPipelineEvaluateExpressionRequest,
    ) -> DataPipelineEvaluateExpressionResponse:
        client = self._require_client()
        return await self._execute(client.evaluate_expression, request, DataPipelineEvaluateExpressionResponse)

    async def get_pipeline_definition(
        self,
        request: DataPipelineGetPipelineDefinitionRequest,
    ) -> DataPipelineGetPipelineDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.get_pipeline_definition, request, DataPipelineGetPipelineDefinitionResponse)

    async def list_pipelines(
        self,
        request: DataPipelineListPipelinesRequest | None = None,
    ) -> DataPipelineListPipelinesResponse:
        client = self._require_client()
        return await self._execute(client.list_pipelines, request, DataPipelineListPipelinesResponse)

    async def list_pipelines_paginated(
        self,
        request: DataPipelineListPipelinesRequest | None = None,
    ) -> list[DataPipelineListPipelinesResponse]:
        return await self._paginate('list_pipelines', request, DataPipelineListPipelinesResponse)

    async def poll_for_task(
        self,
        request: DataPipelinePollForTaskRequest,
    ) -> DataPipelinePollForTaskResponse:
        client = self._require_client()
        return await self._execute(client.poll_for_task, request, DataPipelinePollForTaskResponse)

    async def put_pipeline_definition(
        self,
        request: DataPipelinePutPipelineDefinitionRequest,
    ) -> DataPipelinePutPipelineDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.put_pipeline_definition, request, DataPipelinePutPipelineDefinitionResponse)

    async def query_objects(
        self,
        request: DataPipelineQueryObjectsRequest,
    ) -> DataPipelineQueryObjectsResponse:
        client = self._require_client()
        return await self._execute(client.query_objects, request, DataPipelineQueryObjectsResponse)

    async def query_objects_paginated(
        self,
        request: DataPipelineQueryObjectsRequest,
    ) -> list[DataPipelineQueryObjectsResponse]:
        return await self._paginate('query_objects', request, DataPipelineQueryObjectsResponse)

    async def remove_tags(
        self,
        request: DataPipelineRemoveTagsRequest,
    ) -> DataPipelineRemoveTagsResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags, request, DataPipelineRemoveTagsResponse)

    async def report_task_progress(
        self,
        request: DataPipelineReportTaskProgressRequest,
    ) -> DataPipelineReportTaskProgressResponse:
        client = self._require_client()
        return await self._execute(client.report_task_progress, request, DataPipelineReportTaskProgressResponse)

    async def report_task_runner_heartbeat(
        self,
        request: DataPipelineReportTaskRunnerHeartbeatRequest,
    ) -> DataPipelineReportTaskRunnerHeartbeatResponse:
        client = self._require_client()
        return await self._execute(client.report_task_runner_heartbeat, request, DataPipelineReportTaskRunnerHeartbeatResponse)

    async def set_status(
        self,
        request: DataPipelineSetStatusRequest,
    ) -> DataPipelineSetStatusResponse:
        client = self._require_client()
        return await self._execute(client.set_status, request, DataPipelineSetStatusResponse)

    async def set_task_status(
        self,
        request: DataPipelineSetTaskStatusRequest,
    ) -> DataPipelineSetTaskStatusResponse:
        client = self._require_client()
        return await self._execute(client.set_task_status, request, DataPipelineSetTaskStatusResponse)

    async def validate_pipeline_definition(
        self,
        request: DataPipelineValidatePipelineDefinitionRequest,
    ) -> DataPipelineValidatePipelineDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.validate_pipeline_definition, request, DataPipelineValidatePipelineDefinitionResponse)
