from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CodePipelineClient(ABC):

    @abstractmethod
    def acknowledge_job(
        self,
        *,
        jobId: str,
        nonce: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def acknowledge_third_party_job(
        self,
        *,
        jobId: str,
        nonce: str,
        clientToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_action_type(
        self,
        *,
        category: str,
        provider: str,
        version: str,
        inputArtifactDetails: dict[str, Any],
        outputArtifactDetails: dict[str, Any],
        settings: dict[str, Any] | None = None,
        configurationProperties: list[dict[str, Any]] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pipeline(
        self,
        *,
        pipeline: dict[str, Any],
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_action_type(
        self,
        *,
        category: str,
        provider: str,
        version: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pipeline(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_webhook(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_webhook_with_third_party(
        self,
        *,
        webhookName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_stage_transition(
        self,
        *,
        pipelineName: str,
        stageName: str,
        transitionType: str,
        reason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_stage_transition(
        self,
        *,
        pipelineName: str,
        stageName: str,
        transitionType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_action_type(
        self,
        *,
        category: str,
        owner: str,
        provider: str,
        version: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_details(
        self,
        *,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pipeline(
        self,
        *,
        name: str,
        version: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pipeline_execution(
        self,
        *,
        pipelineName: str,
        pipelineExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_pipeline_state(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_third_party_job_details(
        self,
        *,
        jobId: str,
        clientToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_action_executions(
        self,
        *,
        pipelineName: str,
        filter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_action_types(
        self,
        *,
        actionOwnerFilter: str | None = None,
        nextToken: str | None = None,
        regionFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_deploy_action_execution_targets(
        self,
        *,
        actionExecutionId: str,
        pipelineName: str | None = None,
        filters: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipeline_executions(
        self,
        *,
        pipelineName: str,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipelines(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rule_executions(
        self,
        *,
        pipelineName: str,
        filter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rule_types(
        self,
        *,
        ruleOwnerFilter: str | None = None,
        regionFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_webhooks(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def override_stage_condition(
        self,
        *,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        conditionType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def poll_for_jobs(
        self,
        *,
        actionTypeId: dict[str, Any],
        maxBatchSize: int | None = None,
        queryParam: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def poll_for_third_party_jobs(
        self,
        *,
        actionTypeId: dict[str, Any],
        maxBatchSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_action_revision(
        self,
        *,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_approval_result(
        self,
        *,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: dict[str, Any],
        token: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_job_failure_result(
        self,
        *,
        jobId: str,
        failureDetails: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_job_success_result(
        self,
        *,
        jobId: str,
        currentRevision: dict[str, Any] | None = None,
        continuationToken: str | None = None,
        executionDetails: dict[str, Any] | None = None,
        outputVariables: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_third_party_job_failure_result(
        self,
        *,
        jobId: str,
        clientToken: str,
        failureDetails: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_third_party_job_success_result(
        self,
        *,
        jobId: str,
        clientToken: str,
        currentRevision: dict[str, Any] | None = None,
        continuationToken: str | None = None,
        executionDetails: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_webhook(
        self,
        *,
        webhook: dict[str, Any],
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_webhook_with_third_party(
        self,
        *,
        webhookName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retry_stage_execution(
        self,
        *,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        retryMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rollback_stage(
        self,
        *,
        pipelineName: str,
        stageName: str,
        targetPipelineExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_pipeline_execution(
        self,
        *,
        name: str,
        variables: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
        sourceRevisions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_pipeline_execution(
        self,
        *,
        pipelineName: str,
        pipelineExecutionId: str,
        abandon: bool | None = None,
        reason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
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
    def update_action_type(
        self,
        *,
        actionType: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pipeline(
        self,
        *,
        pipeline: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
