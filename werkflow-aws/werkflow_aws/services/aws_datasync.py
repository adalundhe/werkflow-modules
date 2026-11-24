from werkflow_aws.models.datasync import (
    DataSyncCancelTaskExecutionRequest,
    DataSyncCancelTaskExecutionResponse,
    DataSyncCreateAgentRequest,
    DataSyncCreateAgentResponse,
    DataSyncCreateLocationAzureBlobRequest,
    DataSyncCreateLocationAzureBlobResponse,
    DataSyncCreateLocationEfsRequest,
    DataSyncCreateLocationEfsResponse,
    DataSyncCreateLocationFsxLustreRequest,
    DataSyncCreateLocationFsxLustreResponse,
    DataSyncCreateLocationFsxOntapRequest,
    DataSyncCreateLocationFsxOntapResponse,
    DataSyncCreateLocationFsxOpenZfsRequest,
    DataSyncCreateLocationFsxOpenZfsResponse,
    DataSyncCreateLocationFsxWindowsRequest,
    DataSyncCreateLocationFsxWindowsResponse,
    DataSyncCreateLocationHdfsRequest,
    DataSyncCreateLocationHdfsResponse,
    DataSyncCreateLocationNfsRequest,
    DataSyncCreateLocationNfsResponse,
    DataSyncCreateLocationObjectStorageRequest,
    DataSyncCreateLocationObjectStorageResponse,
    DataSyncCreateLocationS3Request,
    DataSyncCreateLocationS3Response,
    DataSyncCreateLocationSmbRequest,
    DataSyncCreateLocationSmbResponse,
    DataSyncCreateTaskRequest,
    DataSyncCreateTaskResponse,
    DataSyncDeleteAgentRequest,
    DataSyncDeleteAgentResponse,
    DataSyncDeleteLocationRequest,
    DataSyncDeleteLocationResponse,
    DataSyncDeleteTaskRequest,
    DataSyncDeleteTaskResponse,
    DataSyncDescribeAgentRequest,
    DataSyncDescribeAgentResponse,
    DataSyncDescribeLocationAzureBlobRequest,
    DataSyncDescribeLocationAzureBlobResponse,
    DataSyncDescribeLocationEfsRequest,
    DataSyncDescribeLocationEfsResponse,
    DataSyncDescribeLocationFsxLustreRequest,
    DataSyncDescribeLocationFsxLustreResponse,
    DataSyncDescribeLocationFsxOntapRequest,
    DataSyncDescribeLocationFsxOntapResponse,
    DataSyncDescribeLocationFsxOpenZfsRequest,
    DataSyncDescribeLocationFsxOpenZfsResponse,
    DataSyncDescribeLocationFsxWindowsRequest,
    DataSyncDescribeLocationFsxWindowsResponse,
    DataSyncDescribeLocationHdfsRequest,
    DataSyncDescribeLocationHdfsResponse,
    DataSyncDescribeLocationNfsRequest,
    DataSyncDescribeLocationNfsResponse,
    DataSyncDescribeLocationObjectStorageRequest,
    DataSyncDescribeLocationObjectStorageResponse,
    DataSyncDescribeLocationS3Request,
    DataSyncDescribeLocationS3Response,
    DataSyncDescribeLocationSmbRequest,
    DataSyncDescribeLocationSmbResponse,
    DataSyncDescribeTaskExecutionRequest,
    DataSyncDescribeTaskExecutionResponse,
    DataSyncDescribeTaskRequest,
    DataSyncDescribeTaskResponse,
    DataSyncListAgentsRequest,
    DataSyncListAgentsResponse,
    DataSyncListLocationsRequest,
    DataSyncListLocationsResponse,
    DataSyncListTagsForResourceRequest,
    DataSyncListTagsForResourceResponse,
    DataSyncListTaskExecutionsRequest,
    DataSyncListTaskExecutionsResponse,
    DataSyncListTasksRequest,
    DataSyncListTasksResponse,
    DataSyncStartTaskExecutionRequest,
    DataSyncStartTaskExecutionResponse,
    DataSyncTagResourceRequest,
    DataSyncTagResourceResponse,
    DataSyncUntagResourceRequest,
    DataSyncUntagResourceResponse,
    DataSyncUpdateAgentRequest,
    DataSyncUpdateAgentResponse,
    DataSyncUpdateLocationAzureBlobRequest,
    DataSyncUpdateLocationAzureBlobResponse,
    DataSyncUpdateLocationEfsRequest,
    DataSyncUpdateLocationEfsResponse,
    DataSyncUpdateLocationFsxLustreRequest,
    DataSyncUpdateLocationFsxLustreResponse,
    DataSyncUpdateLocationFsxOntapRequest,
    DataSyncUpdateLocationFsxOntapResponse,
    DataSyncUpdateLocationFsxOpenZfsRequest,
    DataSyncUpdateLocationFsxOpenZfsResponse,
    DataSyncUpdateLocationFsxWindowsRequest,
    DataSyncUpdateLocationFsxWindowsResponse,
    DataSyncUpdateLocationHdfsRequest,
    DataSyncUpdateLocationHdfsResponse,
    DataSyncUpdateLocationNfsRequest,
    DataSyncUpdateLocationNfsResponse,
    DataSyncUpdateLocationObjectStorageRequest,
    DataSyncUpdateLocationObjectStorageResponse,
    DataSyncUpdateLocationS3Request,
    DataSyncUpdateLocationS3Response,
    DataSyncUpdateLocationSmbRequest,
    DataSyncUpdateLocationSmbResponse,
    DataSyncUpdateTaskExecutionRequest,
    DataSyncUpdateTaskExecutionResponse,
    DataSyncUpdateTaskRequest,
    DataSyncUpdateTaskResponse,
)
from werkflow_aws.types.datasync_client import DataSyncClient
from .base import AWSBaseService


class AWSDataSync(AWSBaseService[DataSyncClient]):
    service_name = 'datasync'
    boto3_service_name = 'datasync'

    def __init__(self) -> None:
        super().__init__(service_name='datasync', boto3_service_name='datasync')

    async def cancel_task_execution(
        self,
        request: DataSyncCancelTaskExecutionRequest,
    ) -> DataSyncCancelTaskExecutionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_task_execution, request, DataSyncCancelTaskExecutionResponse)

    async def create_agent(
        self,
        request: DataSyncCreateAgentRequest,
    ) -> DataSyncCreateAgentResponse:
        client = self._require_client()
        return await self._execute(client.create_agent, request, DataSyncCreateAgentResponse)

    async def create_location_azure_blob(
        self,
        request: DataSyncCreateLocationAzureBlobRequest,
    ) -> DataSyncCreateLocationAzureBlobResponse:
        client = self._require_client()
        return await self._execute(client.create_location_azure_blob, request, DataSyncCreateLocationAzureBlobResponse)

    async def create_location_efs(
        self,
        request: DataSyncCreateLocationEfsRequest,
    ) -> DataSyncCreateLocationEfsResponse:
        client = self._require_client()
        return await self._execute(client.create_location_efs, request, DataSyncCreateLocationEfsResponse)

    async def create_location_fsx_lustre(
        self,
        request: DataSyncCreateLocationFsxLustreRequest,
    ) -> DataSyncCreateLocationFsxLustreResponse:
        client = self._require_client()
        return await self._execute(client.create_location_fsx_lustre, request, DataSyncCreateLocationFsxLustreResponse)

    async def create_location_fsx_ontap(
        self,
        request: DataSyncCreateLocationFsxOntapRequest,
    ) -> DataSyncCreateLocationFsxOntapResponse:
        client = self._require_client()
        return await self._execute(client.create_location_fsx_ontap, request, DataSyncCreateLocationFsxOntapResponse)

    async def create_location_fsx_open_zfs(
        self,
        request: DataSyncCreateLocationFsxOpenZfsRequest,
    ) -> DataSyncCreateLocationFsxOpenZfsResponse:
        client = self._require_client()
        return await self._execute(client.create_location_fsx_open_zfs, request, DataSyncCreateLocationFsxOpenZfsResponse)

    async def create_location_fsx_windows(
        self,
        request: DataSyncCreateLocationFsxWindowsRequest,
    ) -> DataSyncCreateLocationFsxWindowsResponse:
        client = self._require_client()
        return await self._execute(client.create_location_fsx_windows, request, DataSyncCreateLocationFsxWindowsResponse)

    async def create_location_hdfs(
        self,
        request: DataSyncCreateLocationHdfsRequest,
    ) -> DataSyncCreateLocationHdfsResponse:
        client = self._require_client()
        return await self._execute(client.create_location_hdfs, request, DataSyncCreateLocationHdfsResponse)

    async def create_location_nfs(
        self,
        request: DataSyncCreateLocationNfsRequest,
    ) -> DataSyncCreateLocationNfsResponse:
        client = self._require_client()
        return await self._execute(client.create_location_nfs, request, DataSyncCreateLocationNfsResponse)

    async def create_location_object_storage(
        self,
        request: DataSyncCreateLocationObjectStorageRequest,
    ) -> DataSyncCreateLocationObjectStorageResponse:
        client = self._require_client()
        return await self._execute(client.create_location_object_storage, request, DataSyncCreateLocationObjectStorageResponse)

    async def create_location_s3(
        self,
        request: DataSyncCreateLocationS3Request,
    ) -> DataSyncCreateLocationS3Response:
        client = self._require_client()
        return await self._execute(client.create_location_s3, request, DataSyncCreateLocationS3Response)

    async def create_location_smb(
        self,
        request: DataSyncCreateLocationSmbRequest,
    ) -> DataSyncCreateLocationSmbResponse:
        client = self._require_client()
        return await self._execute(client.create_location_smb, request, DataSyncCreateLocationSmbResponse)

    async def create_task(
        self,
        request: DataSyncCreateTaskRequest,
    ) -> DataSyncCreateTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_task, request, DataSyncCreateTaskResponse)

    async def delete_agent(
        self,
        request: DataSyncDeleteAgentRequest,
    ) -> DataSyncDeleteAgentResponse:
        client = self._require_client()
        return await self._execute(client.delete_agent, request, DataSyncDeleteAgentResponse)

    async def delete_location(
        self,
        request: DataSyncDeleteLocationRequest,
    ) -> DataSyncDeleteLocationResponse:
        client = self._require_client()
        return await self._execute(client.delete_location, request, DataSyncDeleteLocationResponse)

    async def delete_task(
        self,
        request: DataSyncDeleteTaskRequest,
    ) -> DataSyncDeleteTaskResponse:
        client = self._require_client()
        return await self._execute(client.delete_task, request, DataSyncDeleteTaskResponse)

    async def describe_agent(
        self,
        request: DataSyncDescribeAgentRequest,
    ) -> DataSyncDescribeAgentResponse:
        client = self._require_client()
        return await self._execute(client.describe_agent, request, DataSyncDescribeAgentResponse)

    async def describe_location_azure_blob(
        self,
        request: DataSyncDescribeLocationAzureBlobRequest,
    ) -> DataSyncDescribeLocationAzureBlobResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_azure_blob, request, DataSyncDescribeLocationAzureBlobResponse)

    async def describe_location_efs(
        self,
        request: DataSyncDescribeLocationEfsRequest,
    ) -> DataSyncDescribeLocationEfsResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_efs, request, DataSyncDescribeLocationEfsResponse)

    async def describe_location_fsx_lustre(
        self,
        request: DataSyncDescribeLocationFsxLustreRequest,
    ) -> DataSyncDescribeLocationFsxLustreResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_fsx_lustre, request, DataSyncDescribeLocationFsxLustreResponse)

    async def describe_location_fsx_ontap(
        self,
        request: DataSyncDescribeLocationFsxOntapRequest,
    ) -> DataSyncDescribeLocationFsxOntapResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_fsx_ontap, request, DataSyncDescribeLocationFsxOntapResponse)

    async def describe_location_fsx_open_zfs(
        self,
        request: DataSyncDescribeLocationFsxOpenZfsRequest,
    ) -> DataSyncDescribeLocationFsxOpenZfsResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_fsx_open_zfs, request, DataSyncDescribeLocationFsxOpenZfsResponse)

    async def describe_location_fsx_windows(
        self,
        request: DataSyncDescribeLocationFsxWindowsRequest,
    ) -> DataSyncDescribeLocationFsxWindowsResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_fsx_windows, request, DataSyncDescribeLocationFsxWindowsResponse)

    async def describe_location_hdfs(
        self,
        request: DataSyncDescribeLocationHdfsRequest,
    ) -> DataSyncDescribeLocationHdfsResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_hdfs, request, DataSyncDescribeLocationHdfsResponse)

    async def describe_location_nfs(
        self,
        request: DataSyncDescribeLocationNfsRequest,
    ) -> DataSyncDescribeLocationNfsResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_nfs, request, DataSyncDescribeLocationNfsResponse)

    async def describe_location_object_storage(
        self,
        request: DataSyncDescribeLocationObjectStorageRequest,
    ) -> DataSyncDescribeLocationObjectStorageResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_object_storage, request, DataSyncDescribeLocationObjectStorageResponse)

    async def describe_location_s3(
        self,
        request: DataSyncDescribeLocationS3Request,
    ) -> DataSyncDescribeLocationS3Response:
        client = self._require_client()
        return await self._execute(client.describe_location_s3, request, DataSyncDescribeLocationS3Response)

    async def describe_location_smb(
        self,
        request: DataSyncDescribeLocationSmbRequest,
    ) -> DataSyncDescribeLocationSmbResponse:
        client = self._require_client()
        return await self._execute(client.describe_location_smb, request, DataSyncDescribeLocationSmbResponse)

    async def describe_task(
        self,
        request: DataSyncDescribeTaskRequest,
    ) -> DataSyncDescribeTaskResponse:
        client = self._require_client()
        return await self._execute(client.describe_task, request, DataSyncDescribeTaskResponse)

    async def describe_task_execution(
        self,
        request: DataSyncDescribeTaskExecutionRequest,
    ) -> DataSyncDescribeTaskExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_task_execution, request, DataSyncDescribeTaskExecutionResponse)

    async def list_agents(
        self,
        request: DataSyncListAgentsRequest | None = None,
    ) -> DataSyncListAgentsResponse:
        client = self._require_client()
        return await self._execute(client.list_agents, request, DataSyncListAgentsResponse)

    async def list_agents_paginated(
        self,
        request: DataSyncListAgentsRequest | None = None,
    ) -> list[DataSyncListAgentsResponse]:
        return await self._paginate('list_agents', request, DataSyncListAgentsResponse)

    async def list_locations(
        self,
        request: DataSyncListLocationsRequest | None = None,
    ) -> DataSyncListLocationsResponse:
        client = self._require_client()
        return await self._execute(client.list_locations, request, DataSyncListLocationsResponse)

    async def list_locations_paginated(
        self,
        request: DataSyncListLocationsRequest | None = None,
    ) -> list[DataSyncListLocationsResponse]:
        return await self._paginate('list_locations', request, DataSyncListLocationsResponse)

    async def list_tags_for_resource(
        self,
        request: DataSyncListTagsForResourceRequest,
    ) -> DataSyncListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DataSyncListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: DataSyncListTagsForResourceRequest,
    ) -> list[DataSyncListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, DataSyncListTagsForResourceResponse)

    async def list_task_executions(
        self,
        request: DataSyncListTaskExecutionsRequest | None = None,
    ) -> DataSyncListTaskExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_task_executions, request, DataSyncListTaskExecutionsResponse)

    async def list_task_executions_paginated(
        self,
        request: DataSyncListTaskExecutionsRequest | None = None,
    ) -> list[DataSyncListTaskExecutionsResponse]:
        return await self._paginate('list_task_executions', request, DataSyncListTaskExecutionsResponse)

    async def list_tasks(
        self,
        request: DataSyncListTasksRequest | None = None,
    ) -> DataSyncListTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_tasks, request, DataSyncListTasksResponse)

    async def list_tasks_paginated(
        self,
        request: DataSyncListTasksRequest | None = None,
    ) -> list[DataSyncListTasksResponse]:
        return await self._paginate('list_tasks', request, DataSyncListTasksResponse)

    async def start_task_execution(
        self,
        request: DataSyncStartTaskExecutionRequest,
    ) -> DataSyncStartTaskExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_task_execution, request, DataSyncStartTaskExecutionResponse)

    async def tag_resource(
        self,
        request: DataSyncTagResourceRequest,
    ) -> DataSyncTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, DataSyncTagResourceResponse)

    async def untag_resource(
        self,
        request: DataSyncUntagResourceRequest,
    ) -> DataSyncUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, DataSyncUntagResourceResponse)

    async def update_agent(
        self,
        request: DataSyncUpdateAgentRequest,
    ) -> DataSyncUpdateAgentResponse:
        client = self._require_client()
        return await self._execute(client.update_agent, request, DataSyncUpdateAgentResponse)

    async def update_location_azure_blob(
        self,
        request: DataSyncUpdateLocationAzureBlobRequest,
    ) -> DataSyncUpdateLocationAzureBlobResponse:
        client = self._require_client()
        return await self._execute(client.update_location_azure_blob, request, DataSyncUpdateLocationAzureBlobResponse)

    async def update_location_efs(
        self,
        request: DataSyncUpdateLocationEfsRequest,
    ) -> DataSyncUpdateLocationEfsResponse:
        client = self._require_client()
        return await self._execute(client.update_location_efs, request, DataSyncUpdateLocationEfsResponse)

    async def update_location_fsx_lustre(
        self,
        request: DataSyncUpdateLocationFsxLustreRequest,
    ) -> DataSyncUpdateLocationFsxLustreResponse:
        client = self._require_client()
        return await self._execute(client.update_location_fsx_lustre, request, DataSyncUpdateLocationFsxLustreResponse)

    async def update_location_fsx_ontap(
        self,
        request: DataSyncUpdateLocationFsxOntapRequest,
    ) -> DataSyncUpdateLocationFsxOntapResponse:
        client = self._require_client()
        return await self._execute(client.update_location_fsx_ontap, request, DataSyncUpdateLocationFsxOntapResponse)

    async def update_location_fsx_open_zfs(
        self,
        request: DataSyncUpdateLocationFsxOpenZfsRequest,
    ) -> DataSyncUpdateLocationFsxOpenZfsResponse:
        client = self._require_client()
        return await self._execute(client.update_location_fsx_open_zfs, request, DataSyncUpdateLocationFsxOpenZfsResponse)

    async def update_location_fsx_windows(
        self,
        request: DataSyncUpdateLocationFsxWindowsRequest,
    ) -> DataSyncUpdateLocationFsxWindowsResponse:
        client = self._require_client()
        return await self._execute(client.update_location_fsx_windows, request, DataSyncUpdateLocationFsxWindowsResponse)

    async def update_location_hdfs(
        self,
        request: DataSyncUpdateLocationHdfsRequest,
    ) -> DataSyncUpdateLocationHdfsResponse:
        client = self._require_client()
        return await self._execute(client.update_location_hdfs, request, DataSyncUpdateLocationHdfsResponse)

    async def update_location_nfs(
        self,
        request: DataSyncUpdateLocationNfsRequest,
    ) -> DataSyncUpdateLocationNfsResponse:
        client = self._require_client()
        return await self._execute(client.update_location_nfs, request, DataSyncUpdateLocationNfsResponse)

    async def update_location_object_storage(
        self,
        request: DataSyncUpdateLocationObjectStorageRequest,
    ) -> DataSyncUpdateLocationObjectStorageResponse:
        client = self._require_client()
        return await self._execute(client.update_location_object_storage, request, DataSyncUpdateLocationObjectStorageResponse)

    async def update_location_s3(
        self,
        request: DataSyncUpdateLocationS3Request,
    ) -> DataSyncUpdateLocationS3Response:
        client = self._require_client()
        return await self._execute(client.update_location_s3, request, DataSyncUpdateLocationS3Response)

    async def update_location_smb(
        self,
        request: DataSyncUpdateLocationSmbRequest,
    ) -> DataSyncUpdateLocationSmbResponse:
        client = self._require_client()
        return await self._execute(client.update_location_smb, request, DataSyncUpdateLocationSmbResponse)

    async def update_task(
        self,
        request: DataSyncUpdateTaskRequest,
    ) -> DataSyncUpdateTaskResponse:
        client = self._require_client()
        return await self._execute(client.update_task, request, DataSyncUpdateTaskResponse)

    async def update_task_execution(
        self,
        request: DataSyncUpdateTaskExecutionRequest,
    ) -> DataSyncUpdateTaskExecutionResponse:
        client = self._require_client()
        return await self._execute(client.update_task_execution, request, DataSyncUpdateTaskExecutionResponse)
