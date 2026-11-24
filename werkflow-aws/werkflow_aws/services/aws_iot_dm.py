from werkflow_aws.models.iot_dm import (
    IoTJobsDataDescribeJobExecutionRequest,
    IoTJobsDataDescribeJobExecutionResponse,
    IoTJobsDataGetPendingJobExecutionsRequest,
    IoTJobsDataGetPendingJobExecutionsResponse,
    IoTJobsDataStartCommandExecutionRequest,
    IoTJobsDataStartCommandExecutionResponse,
    IoTJobsDataStartNextPendingJobExecutionRequest,
    IoTJobsDataStartNextPendingJobExecutionResponse,
    IoTJobsDataUpdateJobExecutionRequest,
    IoTJobsDataUpdateJobExecutionResponse,
)
from werkflow_aws.types.iot_dm_client import IoTJobsDataClient
from .base import AWSBaseService


class AWSIoTJobsData(AWSBaseService[IoTJobsDataClient]):
    service_name = 'iot-dm'
    boto3_service_name = 'iot-jobs-data'

    def __init__(self) -> None:
        super().__init__(service_name='iot-dm', boto3_service_name='iot-jobs-data')

    async def describe_job_execution(
        self,
        request: IoTJobsDataDescribeJobExecutionRequest,
    ) -> IoTJobsDataDescribeJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_execution, request, IoTJobsDataDescribeJobExecutionResponse)

    async def get_pending_job_executions(
        self,
        request: IoTJobsDataGetPendingJobExecutionsRequest,
    ) -> IoTJobsDataGetPendingJobExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.get_pending_job_executions, request, IoTJobsDataGetPendingJobExecutionsResponse)

    async def start_command_execution(
        self,
        request: IoTJobsDataStartCommandExecutionRequest,
    ) -> IoTJobsDataStartCommandExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_command_execution, request, IoTJobsDataStartCommandExecutionResponse)

    async def start_next_pending_job_execution(
        self,
        request: IoTJobsDataStartNextPendingJobExecutionRequest,
    ) -> IoTJobsDataStartNextPendingJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_next_pending_job_execution, request, IoTJobsDataStartNextPendingJobExecutionResponse)

    async def update_job_execution(
        self,
        request: IoTJobsDataUpdateJobExecutionRequest,
    ) -> IoTJobsDataUpdateJobExecutionResponse:
        client = self._require_client()
        return await self._execute(client.update_job_execution, request, IoTJobsDataUpdateJobExecutionResponse)
