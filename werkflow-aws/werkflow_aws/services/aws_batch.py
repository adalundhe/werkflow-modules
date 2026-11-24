from werkflow_aws.models.batch import (
    BatchCancelJobRequest,
    BatchCancelJobResponse,
    BatchCancelJobsRequest,
    BatchCancelJobsResponse,
    BatchCreateComputeEnvironmentRequest,
    BatchCreateComputeEnvironmentResponse,
    BatchCreateConsumableResourceRequest,
    BatchCreateConsumableResourceResponse,
    BatchCreateJobQueueRequest,
    BatchCreateJobQueueResponse,
    BatchCreateQuotaShareRequest,
    BatchCreateQuotaShareResponse,
    BatchCreateSchedulingPolicyRequest,
    BatchCreateSchedulingPolicyResponse,
    BatchCreateServiceEnvironmentRequest,
    BatchCreateServiceEnvironmentResponse,
    BatchDeleteComputeEnvironmentRequest,
    BatchDeleteComputeEnvironmentResponse,
    BatchDeleteConsumableResourceRequest,
    BatchDeleteConsumableResourceResponse,
    BatchDeleteJobQueueRequest,
    BatchDeleteJobQueueResponse,
    BatchDeleteQuotaShareRequest,
    BatchDeleteQuotaShareResponse,
    BatchDeleteSchedulingPolicyRequest,
    BatchDeleteSchedulingPolicyResponse,
    BatchDeleteServiceEnvironmentRequest,
    BatchDeleteServiceEnvironmentResponse,
    BatchDeregisterJobDefinitionRequest,
    BatchDeregisterJobDefinitionResponse,
    BatchDescribeComputeEnvironmentsRequest,
    BatchDescribeComputeEnvironmentsResponse,
    BatchDescribeConsumableResourceRequest,
    BatchDescribeConsumableResourceResponse,
    BatchDescribeJobDefinitionsRequest,
    BatchDescribeJobDefinitionsResponse,
    BatchDescribeJobQueuesRequest,
    BatchDescribeJobQueuesResponse,
    BatchDescribeJobsRequest,
    BatchDescribeJobsResponse,
    BatchDescribeQuotaShareRequest,
    BatchDescribeQuotaShareResponse,
    BatchDescribeSchedulingPoliciesRequest,
    BatchDescribeSchedulingPoliciesResponse,
    BatchDescribeServiceEnvironmentsRequest,
    BatchDescribeServiceEnvironmentsResponse,
    BatchDescribeServiceJobRequest,
    BatchDescribeServiceJobResponse,
    BatchGetJobQueueSnapshotRequest,
    BatchGetJobQueueSnapshotResponse,
    BatchListConsumableResourcesRequest,
    BatchListConsumableResourcesResponse,
    BatchListJobsByConsumableResourceRequest,
    BatchListJobsByConsumableResourceResponse,
    BatchListJobsRequest,
    BatchListJobsResponse,
    BatchListQuotaSharesRequest,
    BatchListQuotaSharesResponse,
    BatchListSchedulingPoliciesRequest,
    BatchListSchedulingPoliciesResponse,
    BatchListServiceJobsRequest,
    BatchListServiceJobsResponse,
    BatchListTagsForResourceRequest,
    BatchListTagsForResourceResponse,
    BatchRegisterJobDefinitionRequest,
    BatchRegisterJobDefinitionResponse,
    BatchSubmitJobRequest,
    BatchSubmitJobResponse,
    BatchSubmitServiceJobRequest,
    BatchSubmitServiceJobResponse,
    BatchTagResourceRequest,
    BatchTagResourceResponse,
    BatchTerminateJobRequest,
    BatchTerminateJobResponse,
    BatchTerminateJobsRequest,
    BatchTerminateJobsResponse,
    BatchTerminateServiceJobRequest,
    BatchTerminateServiceJobResponse,
    BatchTerminateServiceJobsRequest,
    BatchTerminateServiceJobsResponse,
    BatchUntagResourceRequest,
    BatchUntagResourceResponse,
    BatchUpdateComputeEnvironmentRequest,
    BatchUpdateComputeEnvironmentResponse,
    BatchUpdateConsumableResourceRequest,
    BatchUpdateConsumableResourceResponse,
    BatchUpdateJobQueueRequest,
    BatchUpdateJobQueueResponse,
    BatchUpdateQuotaShareRequest,
    BatchUpdateQuotaShareResponse,
    BatchUpdateSchedulingPolicyRequest,
    BatchUpdateSchedulingPolicyResponse,
    BatchUpdateServiceEnvironmentRequest,
    BatchUpdateServiceEnvironmentResponse,
    BatchUpdateServiceJobRequest,
    BatchUpdateServiceJobResponse,
)
from werkflow_aws.types.batch_client import BatchClient
from .base import AWSBaseService


class AWSBatch(AWSBaseService[BatchClient]):
    service_name = 'batch'
    boto3_service_name = 'batch'

    def __init__(self) -> None:
        super().__init__(service_name='batch', boto3_service_name='batch')

    async def cancel_job(
        self,
        request: BatchCancelJobRequest,
    ) -> BatchCancelJobResponse:
        client = self._require_client()
        return await self._execute(client.cancel_job, request, BatchCancelJobResponse)

    async def cancel_jobs(
        self,
        request: BatchCancelJobsRequest,
    ) -> BatchCancelJobsResponse:
        client = self._require_client()
        return await self._execute(client.cancel_jobs, request, BatchCancelJobsResponse)

    async def create_compute_environment(
        self,
        request: BatchCreateComputeEnvironmentRequest,
    ) -> BatchCreateComputeEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_compute_environment, request, BatchCreateComputeEnvironmentResponse)

    async def create_consumable_resource(
        self,
        request: BatchCreateConsumableResourceRequest,
    ) -> BatchCreateConsumableResourceResponse:
        client = self._require_client()
        return await self._execute(client.create_consumable_resource, request, BatchCreateConsumableResourceResponse)

    async def create_job_queue(
        self,
        request: BatchCreateJobQueueRequest,
    ) -> BatchCreateJobQueueResponse:
        client = self._require_client()
        return await self._execute(client.create_job_queue, request, BatchCreateJobQueueResponse)

    async def create_quota_share(
        self,
        request: BatchCreateQuotaShareRequest,
    ) -> BatchCreateQuotaShareResponse:
        client = self._require_client()
        return await self._execute(client.create_quota_share, request, BatchCreateQuotaShareResponse)

    async def create_scheduling_policy(
        self,
        request: BatchCreateSchedulingPolicyRequest,
    ) -> BatchCreateSchedulingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_scheduling_policy, request, BatchCreateSchedulingPolicyResponse)

    async def create_service_environment(
        self,
        request: BatchCreateServiceEnvironmentRequest,
    ) -> BatchCreateServiceEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_service_environment, request, BatchCreateServiceEnvironmentResponse)

    async def delete_compute_environment(
        self,
        request: BatchDeleteComputeEnvironmentRequest,
    ) -> BatchDeleteComputeEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_compute_environment, request, BatchDeleteComputeEnvironmentResponse)

    async def delete_consumable_resource(
        self,
        request: BatchDeleteConsumableResourceRequest,
    ) -> BatchDeleteConsumableResourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_consumable_resource, request, BatchDeleteConsumableResourceResponse)

    async def delete_job_queue(
        self,
        request: BatchDeleteJobQueueRequest,
    ) -> BatchDeleteJobQueueResponse:
        client = self._require_client()
        return await self._execute(client.delete_job_queue, request, BatchDeleteJobQueueResponse)

    async def delete_quota_share(
        self,
        request: BatchDeleteQuotaShareRequest,
    ) -> BatchDeleteQuotaShareResponse:
        client = self._require_client()
        return await self._execute(client.delete_quota_share, request, BatchDeleteQuotaShareResponse)

    async def delete_scheduling_policy(
        self,
        request: BatchDeleteSchedulingPolicyRequest,
    ) -> BatchDeleteSchedulingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduling_policy, request, BatchDeleteSchedulingPolicyResponse)

    async def delete_service_environment(
        self,
        request: BatchDeleteServiceEnvironmentRequest,
    ) -> BatchDeleteServiceEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_environment, request, BatchDeleteServiceEnvironmentResponse)

    async def deregister_job_definition(
        self,
        request: BatchDeregisterJobDefinitionRequest,
    ) -> BatchDeregisterJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.deregister_job_definition, request, BatchDeregisterJobDefinitionResponse)

    async def describe_compute_environments(
        self,
        request: BatchDescribeComputeEnvironmentsRequest | None = None,
    ) -> BatchDescribeComputeEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_compute_environments, request, BatchDescribeComputeEnvironmentsResponse)

    async def describe_compute_environments_paginated(
        self,
        request: BatchDescribeComputeEnvironmentsRequest | None = None,
    ) -> list[BatchDescribeComputeEnvironmentsResponse]:
        return await self._paginate('describe_compute_environments', request, BatchDescribeComputeEnvironmentsResponse)

    async def describe_consumable_resource(
        self,
        request: BatchDescribeConsumableResourceRequest,
    ) -> BatchDescribeConsumableResourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_consumable_resource, request, BatchDescribeConsumableResourceResponse)

    async def describe_job_definitions(
        self,
        request: BatchDescribeJobDefinitionsRequest | None = None,
    ) -> BatchDescribeJobDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_definitions, request, BatchDescribeJobDefinitionsResponse)

    async def describe_job_definitions_paginated(
        self,
        request: BatchDescribeJobDefinitionsRequest | None = None,
    ) -> list[BatchDescribeJobDefinitionsResponse]:
        return await self._paginate('describe_job_definitions', request, BatchDescribeJobDefinitionsResponse)

    async def describe_job_queues(
        self,
        request: BatchDescribeJobQueuesRequest | None = None,
    ) -> BatchDescribeJobQueuesResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_queues, request, BatchDescribeJobQueuesResponse)

    async def describe_job_queues_paginated(
        self,
        request: BatchDescribeJobQueuesRequest | None = None,
    ) -> list[BatchDescribeJobQueuesResponse]:
        return await self._paginate('describe_job_queues', request, BatchDescribeJobQueuesResponse)

    async def describe_jobs(
        self,
        request: BatchDescribeJobsRequest,
    ) -> BatchDescribeJobsResponse:
        client = self._require_client()
        return await self._execute(client.describe_jobs, request, BatchDescribeJobsResponse)

    async def describe_quota_share(
        self,
        request: BatchDescribeQuotaShareRequest,
    ) -> BatchDescribeQuotaShareResponse:
        client = self._require_client()
        return await self._execute(client.describe_quota_share, request, BatchDescribeQuotaShareResponse)

    async def describe_scheduling_policies(
        self,
        request: BatchDescribeSchedulingPoliciesRequest,
    ) -> BatchDescribeSchedulingPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_scheduling_policies, request, BatchDescribeSchedulingPoliciesResponse)

    async def describe_service_environments(
        self,
        request: BatchDescribeServiceEnvironmentsRequest | None = None,
    ) -> BatchDescribeServiceEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_environments, request, BatchDescribeServiceEnvironmentsResponse)

    async def describe_service_environments_paginated(
        self,
        request: BatchDescribeServiceEnvironmentsRequest | None = None,
    ) -> list[BatchDescribeServiceEnvironmentsResponse]:
        return await self._paginate('describe_service_environments', request, BatchDescribeServiceEnvironmentsResponse)

    async def describe_service_job(
        self,
        request: BatchDescribeServiceJobRequest,
    ) -> BatchDescribeServiceJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_job, request, BatchDescribeServiceJobResponse)

    async def get_job_queue_snapshot(
        self,
        request: BatchGetJobQueueSnapshotRequest,
    ) -> BatchGetJobQueueSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.get_job_queue_snapshot, request, BatchGetJobQueueSnapshotResponse)

    async def list_consumable_resources(
        self,
        request: BatchListConsumableResourcesRequest | None = None,
    ) -> BatchListConsumableResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_consumable_resources, request, BatchListConsumableResourcesResponse)

    async def list_consumable_resources_paginated(
        self,
        request: BatchListConsumableResourcesRequest | None = None,
    ) -> list[BatchListConsumableResourcesResponse]:
        return await self._paginate('list_consumable_resources', request, BatchListConsumableResourcesResponse)

    async def list_jobs(
        self,
        request: BatchListJobsRequest | None = None,
    ) -> BatchListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, BatchListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: BatchListJobsRequest | None = None,
    ) -> list[BatchListJobsResponse]:
        return await self._paginate('list_jobs', request, BatchListJobsResponse)

    async def list_jobs_by_consumable_resource(
        self,
        request: BatchListJobsByConsumableResourceRequest,
    ) -> BatchListJobsByConsumableResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs_by_consumable_resource, request, BatchListJobsByConsumableResourceResponse)

    async def list_jobs_by_consumable_resource_paginated(
        self,
        request: BatchListJobsByConsumableResourceRequest,
    ) -> list[BatchListJobsByConsumableResourceResponse]:
        return await self._paginate('list_jobs_by_consumable_resource', request, BatchListJobsByConsumableResourceResponse)

    async def list_quota_shares(
        self,
        request: BatchListQuotaSharesRequest,
    ) -> BatchListQuotaSharesResponse:
        client = self._require_client()
        return await self._execute(client.list_quota_shares, request, BatchListQuotaSharesResponse)

    async def list_quota_shares_paginated(
        self,
        request: BatchListQuotaSharesRequest,
    ) -> list[BatchListQuotaSharesResponse]:
        return await self._paginate('list_quota_shares', request, BatchListQuotaSharesResponse)

    async def list_scheduling_policies(
        self,
        request: BatchListSchedulingPoliciesRequest | None = None,
    ) -> BatchListSchedulingPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_scheduling_policies, request, BatchListSchedulingPoliciesResponse)

    async def list_scheduling_policies_paginated(
        self,
        request: BatchListSchedulingPoliciesRequest | None = None,
    ) -> list[BatchListSchedulingPoliciesResponse]:
        return await self._paginate('list_scheduling_policies', request, BatchListSchedulingPoliciesResponse)

    async def list_service_jobs(
        self,
        request: BatchListServiceJobsRequest | None = None,
    ) -> BatchListServiceJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_service_jobs, request, BatchListServiceJobsResponse)

    async def list_service_jobs_paginated(
        self,
        request: BatchListServiceJobsRequest | None = None,
    ) -> list[BatchListServiceJobsResponse]:
        return await self._paginate('list_service_jobs', request, BatchListServiceJobsResponse)

    async def list_tags_for_resource(
        self,
        request: BatchListTagsForResourceRequest,
    ) -> BatchListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, BatchListTagsForResourceResponse)

    async def register_job_definition(
        self,
        request: BatchRegisterJobDefinitionRequest,
    ) -> BatchRegisterJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.register_job_definition, request, BatchRegisterJobDefinitionResponse)

    async def submit_job(
        self,
        request: BatchSubmitJobRequest,
    ) -> BatchSubmitJobResponse:
        client = self._require_client()
        return await self._execute(client.submit_job, request, BatchSubmitJobResponse)

    async def submit_service_job(
        self,
        request: BatchSubmitServiceJobRequest,
    ) -> BatchSubmitServiceJobResponse:
        client = self._require_client()
        return await self._execute(client.submit_service_job, request, BatchSubmitServiceJobResponse)

    async def tag_resource(
        self,
        request: BatchTagResourceRequest,
    ) -> BatchTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, BatchTagResourceResponse)

    async def terminate_job(
        self,
        request: BatchTerminateJobRequest,
    ) -> BatchTerminateJobResponse:
        client = self._require_client()
        return await self._execute(client.terminate_job, request, BatchTerminateJobResponse)

    async def terminate_jobs(
        self,
        request: BatchTerminateJobsRequest,
    ) -> BatchTerminateJobsResponse:
        client = self._require_client()
        return await self._execute(client.terminate_jobs, request, BatchTerminateJobsResponse)

    async def terminate_service_job(
        self,
        request: BatchTerminateServiceJobRequest,
    ) -> BatchTerminateServiceJobResponse:
        client = self._require_client()
        return await self._execute(client.terminate_service_job, request, BatchTerminateServiceJobResponse)

    async def terminate_service_jobs(
        self,
        request: BatchTerminateServiceJobsRequest,
    ) -> BatchTerminateServiceJobsResponse:
        client = self._require_client()
        return await self._execute(client.terminate_service_jobs, request, BatchTerminateServiceJobsResponse)

    async def untag_resource(
        self,
        request: BatchUntagResourceRequest,
    ) -> BatchUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, BatchUntagResourceResponse)

    async def update_compute_environment(
        self,
        request: BatchUpdateComputeEnvironmentRequest,
    ) -> BatchUpdateComputeEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_compute_environment, request, BatchUpdateComputeEnvironmentResponse)

    async def update_consumable_resource(
        self,
        request: BatchUpdateConsumableResourceRequest,
    ) -> BatchUpdateConsumableResourceResponse:
        client = self._require_client()
        return await self._execute(client.update_consumable_resource, request, BatchUpdateConsumableResourceResponse)

    async def update_job_queue(
        self,
        request: BatchUpdateJobQueueRequest,
    ) -> BatchUpdateJobQueueResponse:
        client = self._require_client()
        return await self._execute(client.update_job_queue, request, BatchUpdateJobQueueResponse)

    async def update_quota_share(
        self,
        request: BatchUpdateQuotaShareRequest,
    ) -> BatchUpdateQuotaShareResponse:
        client = self._require_client()
        return await self._execute(client.update_quota_share, request, BatchUpdateQuotaShareResponse)

    async def update_scheduling_policy(
        self,
        request: BatchUpdateSchedulingPolicyRequest,
    ) -> BatchUpdateSchedulingPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_scheduling_policy, request, BatchUpdateSchedulingPolicyResponse)

    async def update_service_environment(
        self,
        request: BatchUpdateServiceEnvironmentRequest,
    ) -> BatchUpdateServiceEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_service_environment, request, BatchUpdateServiceEnvironmentResponse)

    async def update_service_job(
        self,
        request: BatchUpdateServiceJobRequest,
    ) -> BatchUpdateServiceJobResponse:
        client = self._require_client()
        return await self._execute(client.update_service_job, request, BatchUpdateServiceJobResponse)
