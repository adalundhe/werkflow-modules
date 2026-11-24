from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class BatchClient(ABC):

    @abstractmethod
    def cancel_job(
        self,
        *,
        jobId: str,
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_jobs(
        self,
        *,
        jobs: list[str],
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_compute_environment(
        self,
        *,
        computeEnvironmentName: str,
        type: str,
        state: str | None = None,
        unmanagedvCpus: int | None = None,
        computeResources: dict[str, Any] | None = None,
        serviceRole: str | None = None,
        tags: dict[str, str] | None = None,
        eksConfiguration: dict[str, Any] | None = None,
        context: str | None = None,
        ecsSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_consumable_resource(
        self,
        *,
        consumableResourceName: str,
        totalQuantity: int | None = None,
        resourceType: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_job_queue(
        self,
        *,
        jobQueueName: str,
        priority: int,
        state: str | None = None,
        schedulingPolicyArn: str | None = None,
        computeEnvironmentOrder: list[dict[str, Any]] | None = None,
        serviceEnvironmentOrder: list[dict[str, Any]] | None = None,
        jobQueueType: str | None = None,
        tags: dict[str, str] | None = None,
        jobStateTimeLimitActions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_quota_share(
        self,
        *,
        quotaShareName: str,
        jobQueue: str,
        capacityLimits: list[dict[str, Any]],
        resourceSharingConfiguration: dict[str, Any],
        preemptionConfiguration: dict[str, Any],
        state: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_scheduling_policy(
        self,
        *,
        name: str,
        quotaSharePolicy: dict[str, Any] | None = None,
        fairsharePolicy: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service_environment(
        self,
        *,
        serviceEnvironmentName: str,
        serviceEnvironmentType: str,
        capacityLimits: list[dict[str, Any]],
        state: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_compute_environment(
        self,
        *,
        computeEnvironment: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_consumable_resource(
        self,
        *,
        consumableResource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job_queue(
        self,
        *,
        jobQueue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_quota_share(
        self,
        *,
        quotaShareArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduling_policy(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_environment(
        self,
        *,
        serviceEnvironment: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_job_definition(
        self,
        *,
        jobDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_compute_environments(
        self,
        *,
        computeEnvironments: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_consumable_resource(
        self,
        *,
        consumableResource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_definitions(
        self,
        *,
        jobDefinitions: list[str] | None = None,
        maxResults: int | None = None,
        jobDefinitionName: str | None = None,
        status: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_queues(
        self,
        *,
        jobQueues: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_jobs(
        self,
        *,
        jobs: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_quota_share(
        self,
        *,
        quotaShareArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduling_policies(
        self,
        *,
        arns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_environments(
        self,
        *,
        serviceEnvironments: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_job(
        self,
        *,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_queue_snapshot(
        self,
        *,
        jobQueue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_consumable_resources(
        self,
        *,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        jobQueue: str | None = None,
        arrayJobId: str | None = None,
        multiNodeJobId: str | None = None,
        jobStatus: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs_by_consumable_resource(
        self,
        *,
        consumableResource: str,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_quota_shares(
        self,
        *,
        jobQueue: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scheduling_policies(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_service_jobs(
        self,
        *,
        jobQueue: str | None = None,
        jobStatus: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_job_definition(
        self,
        *,
        jobDefinitionName: str,
        type: str,
        parameters: dict[str, str] | None = None,
        schedulingPriority: int | None = None,
        containerProperties: dict[str, Any] | None = None,
        nodeProperties: dict[str, Any] | None = None,
        retryStrategy: dict[str, Any] | None = None,
        propagateTags: bool | None = None,
        timeout: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
        platformCapabilities: list[str] | None = None,
        eksProperties: dict[str, Any] | None = None,
        ecsProperties: dict[str, Any] | None = None,
        consumableResourceProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_job(
        self,
        *,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        shareIdentifier: str | None = None,
        schedulingPriorityOverride: int | None = None,
        arrayProperties: dict[str, Any] | None = None,
        dependsOn: list[dict[str, Any]] | None = None,
        parameters: dict[str, str] | None = None,
        containerOverrides: dict[str, Any] | None = None,
        nodeOverrides: dict[str, Any] | None = None,
        retryStrategy: dict[str, Any] | None = None,
        propagateTags: bool | None = None,
        timeout: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
        eksPropertiesOverride: dict[str, Any] | None = None,
        ecsPropertiesOverride: dict[str, Any] | None = None,
        consumableResourcePropertiesOverride: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_service_job(
        self,
        *,
        jobName: str,
        jobQueue: str,
        serviceRequestPayload: str,
        serviceJobType: str,
        retryStrategy: dict[str, Any] | None = None,
        schedulingPriority: int | None = None,
        shareIdentifier: str | None = None,
        quotaShareName: str | None = None,
        preemptionConfiguration: dict[str, Any] | None = None,
        timeoutConfig: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_job(
        self,
        *,
        jobId: str,
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_jobs(
        self,
        *,
        jobs: list[str],
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_service_job(
        self,
        *,
        jobId: str,
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_service_jobs(
        self,
        *,
        jobs: list[str],
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_compute_environment(
        self,
        *,
        computeEnvironment: str,
        state: str | None = None,
        unmanagedvCpus: int | None = None,
        computeResources: dict[str, Any] | None = None,
        serviceRole: str | None = None,
        updatePolicy: dict[str, Any] | None = None,
        context: str | None = None,
        ecsSettings: dict[str, Any] | None = None,
        eksConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_consumable_resource(
        self,
        *,
        consumableResource: str,
        operation: str | None = None,
        quantity: int | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_job_queue(
        self,
        *,
        jobQueue: str,
        state: str | None = None,
        schedulingPolicyArn: str | None = None,
        priority: int | None = None,
        computeEnvironmentOrder: list[dict[str, Any]] | None = None,
        serviceEnvironmentOrder: list[dict[str, Any]] | None = None,
        jobStateTimeLimitActions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_quota_share(
        self,
        *,
        quotaShareArn: str,
        capacityLimits: list[dict[str, Any]] | None = None,
        resourceSharingConfiguration: dict[str, Any] | None = None,
        preemptionConfiguration: dict[str, Any] | None = None,
        state: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scheduling_policy(
        self,
        *,
        arn: str,
        quotaSharePolicy: dict[str, Any] | None = None,
        fairsharePolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_environment(
        self,
        *,
        serviceEnvironment: str,
        state: str | None = None,
        capacityLimits: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_job(
        self,
        *,
        jobId: str,
        schedulingPriority: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
