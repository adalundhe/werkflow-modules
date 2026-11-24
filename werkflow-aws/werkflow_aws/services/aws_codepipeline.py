from werkflow_aws.models.codepipeline import (
    CodePipelineAcknowledgeJobRequest,
    CodePipelineAcknowledgeJobResponse,
    CodePipelineAcknowledgeThirdPartyJobRequest,
    CodePipelineAcknowledgeThirdPartyJobResponse,
    CodePipelineCreateCustomActionTypeRequest,
    CodePipelineCreateCustomActionTypeResponse,
    CodePipelineCreatePipelineRequest,
    CodePipelineCreatePipelineResponse,
    CodePipelineDeleteCustomActionTypeRequest,
    CodePipelineDeleteCustomActionTypeResponse,
    CodePipelineDeletePipelineRequest,
    CodePipelineDeletePipelineResponse,
    CodePipelineDeleteWebhookRequest,
    CodePipelineDeleteWebhookResponse,
    CodePipelineDeregisterWebhookWithThirdPartyRequest,
    CodePipelineDeregisterWebhookWithThirdPartyResponse,
    CodePipelineDisableStageTransitionRequest,
    CodePipelineDisableStageTransitionResponse,
    CodePipelineEnableStageTransitionRequest,
    CodePipelineEnableStageTransitionResponse,
    CodePipelineGetActionTypeRequest,
    CodePipelineGetActionTypeResponse,
    CodePipelineGetJobDetailsRequest,
    CodePipelineGetJobDetailsResponse,
    CodePipelineGetPipelineExecutionRequest,
    CodePipelineGetPipelineExecutionResponse,
    CodePipelineGetPipelineRequest,
    CodePipelineGetPipelineResponse,
    CodePipelineGetPipelineStateRequest,
    CodePipelineGetPipelineStateResponse,
    CodePipelineGetThirdPartyJobDetailsRequest,
    CodePipelineGetThirdPartyJobDetailsResponse,
    CodePipelineListActionExecutionsRequest,
    CodePipelineListActionExecutionsResponse,
    CodePipelineListActionTypesRequest,
    CodePipelineListActionTypesResponse,
    CodePipelineListDeployActionExecutionTargetsRequest,
    CodePipelineListDeployActionExecutionTargetsResponse,
    CodePipelineListPipelineExecutionsRequest,
    CodePipelineListPipelineExecutionsResponse,
    CodePipelineListPipelinesRequest,
    CodePipelineListPipelinesResponse,
    CodePipelineListRuleExecutionsRequest,
    CodePipelineListRuleExecutionsResponse,
    CodePipelineListRuleTypesRequest,
    CodePipelineListRuleTypesResponse,
    CodePipelineListTagsForResourceRequest,
    CodePipelineListTagsForResourceResponse,
    CodePipelineListWebhooksRequest,
    CodePipelineListWebhooksResponse,
    CodePipelineOverrideStageConditionRequest,
    CodePipelineOverrideStageConditionResponse,
    CodePipelinePollForJobsRequest,
    CodePipelinePollForJobsResponse,
    CodePipelinePollForThirdPartyJobsRequest,
    CodePipelinePollForThirdPartyJobsResponse,
    CodePipelinePutActionRevisionRequest,
    CodePipelinePutActionRevisionResponse,
    CodePipelinePutApprovalResultRequest,
    CodePipelinePutApprovalResultResponse,
    CodePipelinePutJobFailureResultRequest,
    CodePipelinePutJobFailureResultResponse,
    CodePipelinePutJobSuccessResultRequest,
    CodePipelinePutJobSuccessResultResponse,
    CodePipelinePutThirdPartyJobFailureResultRequest,
    CodePipelinePutThirdPartyJobFailureResultResponse,
    CodePipelinePutThirdPartyJobSuccessResultRequest,
    CodePipelinePutThirdPartyJobSuccessResultResponse,
    CodePipelinePutWebhookRequest,
    CodePipelinePutWebhookResponse,
    CodePipelineRegisterWebhookWithThirdPartyRequest,
    CodePipelineRegisterWebhookWithThirdPartyResponse,
    CodePipelineRetryStageExecutionRequest,
    CodePipelineRetryStageExecutionResponse,
    CodePipelineRollbackStageRequest,
    CodePipelineRollbackStageResponse,
    CodePipelineStartPipelineExecutionRequest,
    CodePipelineStartPipelineExecutionResponse,
    CodePipelineStopPipelineExecutionRequest,
    CodePipelineStopPipelineExecutionResponse,
    CodePipelineTagResourceRequest,
    CodePipelineTagResourceResponse,
    CodePipelineUntagResourceRequest,
    CodePipelineUntagResourceResponse,
    CodePipelineUpdateActionTypeRequest,
    CodePipelineUpdateActionTypeResponse,
    CodePipelineUpdatePipelineRequest,
    CodePipelineUpdatePipelineResponse,
)
from werkflow_aws.types.codepipeline_client import CodePipelineClient
from .base import AWSBaseService


class AWSCodePipeline(AWSBaseService[CodePipelineClient]):
    service_name = 'codepipeline'
    boto3_service_name = 'codepipeline'

    def __init__(self) -> None:
        super().__init__(service_name='codepipeline', boto3_service_name='codepipeline')

    async def acknowledge_job(
        self,
        request: CodePipelineAcknowledgeJobRequest,
    ) -> CodePipelineAcknowledgeJobResponse:
        client = self._require_client()
        return await self._execute(client.acknowledge_job, request, CodePipelineAcknowledgeJobResponse)

    async def acknowledge_third_party_job(
        self,
        request: CodePipelineAcknowledgeThirdPartyJobRequest,
    ) -> CodePipelineAcknowledgeThirdPartyJobResponse:
        client = self._require_client()
        return await self._execute(client.acknowledge_third_party_job, request, CodePipelineAcknowledgeThirdPartyJobResponse)

    async def create_custom_action_type(
        self,
        request: CodePipelineCreateCustomActionTypeRequest,
    ) -> CodePipelineCreateCustomActionTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_action_type, request, CodePipelineCreateCustomActionTypeResponse)

    async def create_pipeline(
        self,
        request: CodePipelineCreatePipelineRequest,
    ) -> CodePipelineCreatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.create_pipeline, request, CodePipelineCreatePipelineResponse)

    async def delete_custom_action_type(
        self,
        request: CodePipelineDeleteCustomActionTypeRequest,
    ) -> CodePipelineDeleteCustomActionTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_action_type, request, CodePipelineDeleteCustomActionTypeResponse)

    async def delete_pipeline(
        self,
        request: CodePipelineDeletePipelineRequest,
    ) -> CodePipelineDeletePipelineResponse:
        client = self._require_client()
        return await self._execute(client.delete_pipeline, request, CodePipelineDeletePipelineResponse)

    async def delete_webhook(
        self,
        request: CodePipelineDeleteWebhookRequest,
    ) -> CodePipelineDeleteWebhookResponse:
        client = self._require_client()
        return await self._execute(client.delete_webhook, request, CodePipelineDeleteWebhookResponse)

    async def deregister_webhook_with_third_party(
        self,
        request: CodePipelineDeregisterWebhookWithThirdPartyRequest | None = None,
    ) -> CodePipelineDeregisterWebhookWithThirdPartyResponse:
        client = self._require_client()
        return await self._execute(client.deregister_webhook_with_third_party, request, CodePipelineDeregisterWebhookWithThirdPartyResponse)

    async def disable_stage_transition(
        self,
        request: CodePipelineDisableStageTransitionRequest,
    ) -> CodePipelineDisableStageTransitionResponse:
        client = self._require_client()
        return await self._execute(client.disable_stage_transition, request, CodePipelineDisableStageTransitionResponse)

    async def enable_stage_transition(
        self,
        request: CodePipelineEnableStageTransitionRequest,
    ) -> CodePipelineEnableStageTransitionResponse:
        client = self._require_client()
        return await self._execute(client.enable_stage_transition, request, CodePipelineEnableStageTransitionResponse)

    async def get_action_type(
        self,
        request: CodePipelineGetActionTypeRequest,
    ) -> CodePipelineGetActionTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_action_type, request, CodePipelineGetActionTypeResponse)

    async def get_job_details(
        self,
        request: CodePipelineGetJobDetailsRequest,
    ) -> CodePipelineGetJobDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_job_details, request, CodePipelineGetJobDetailsResponse)

    async def get_pipeline(
        self,
        request: CodePipelineGetPipelineRequest,
    ) -> CodePipelineGetPipelineResponse:
        client = self._require_client()
        return await self._execute(client.get_pipeline, request, CodePipelineGetPipelineResponse)

    async def get_pipeline_execution(
        self,
        request: CodePipelineGetPipelineExecutionRequest,
    ) -> CodePipelineGetPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.get_pipeline_execution, request, CodePipelineGetPipelineExecutionResponse)

    async def get_pipeline_state(
        self,
        request: CodePipelineGetPipelineStateRequest,
    ) -> CodePipelineGetPipelineStateResponse:
        client = self._require_client()
        return await self._execute(client.get_pipeline_state, request, CodePipelineGetPipelineStateResponse)

    async def get_third_party_job_details(
        self,
        request: CodePipelineGetThirdPartyJobDetailsRequest,
    ) -> CodePipelineGetThirdPartyJobDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_third_party_job_details, request, CodePipelineGetThirdPartyJobDetailsResponse)

    async def list_action_executions(
        self,
        request: CodePipelineListActionExecutionsRequest,
    ) -> CodePipelineListActionExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_action_executions, request, CodePipelineListActionExecutionsResponse)

    async def list_action_executions_paginated(
        self,
        request: CodePipelineListActionExecutionsRequest,
    ) -> list[CodePipelineListActionExecutionsResponse]:
        return await self._paginate('list_action_executions', request, CodePipelineListActionExecutionsResponse)

    async def list_action_types(
        self,
        request: CodePipelineListActionTypesRequest | None = None,
    ) -> CodePipelineListActionTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_action_types, request, CodePipelineListActionTypesResponse)

    async def list_action_types_paginated(
        self,
        request: CodePipelineListActionTypesRequest | None = None,
    ) -> list[CodePipelineListActionTypesResponse]:
        return await self._paginate('list_action_types', request, CodePipelineListActionTypesResponse)

    async def list_deploy_action_execution_targets(
        self,
        request: CodePipelineListDeployActionExecutionTargetsRequest,
    ) -> CodePipelineListDeployActionExecutionTargetsResponse:
        client = self._require_client()
        return await self._execute(client.list_deploy_action_execution_targets, request, CodePipelineListDeployActionExecutionTargetsResponse)

    async def list_deploy_action_execution_targets_paginated(
        self,
        request: CodePipelineListDeployActionExecutionTargetsRequest,
    ) -> list[CodePipelineListDeployActionExecutionTargetsResponse]:
        return await self._paginate('list_deploy_action_execution_targets', request, CodePipelineListDeployActionExecutionTargetsResponse)

    async def list_pipeline_executions(
        self,
        request: CodePipelineListPipelineExecutionsRequest,
    ) -> CodePipelineListPipelineExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_pipeline_executions, request, CodePipelineListPipelineExecutionsResponse)

    async def list_pipeline_executions_paginated(
        self,
        request: CodePipelineListPipelineExecutionsRequest,
    ) -> list[CodePipelineListPipelineExecutionsResponse]:
        return await self._paginate('list_pipeline_executions', request, CodePipelineListPipelineExecutionsResponse)

    async def list_pipelines(
        self,
        request: CodePipelineListPipelinesRequest | None = None,
    ) -> CodePipelineListPipelinesResponse:
        client = self._require_client()
        return await self._execute(client.list_pipelines, request, CodePipelineListPipelinesResponse)

    async def list_pipelines_paginated(
        self,
        request: CodePipelineListPipelinesRequest | None = None,
    ) -> list[CodePipelineListPipelinesResponse]:
        return await self._paginate('list_pipelines', request, CodePipelineListPipelinesResponse)

    async def list_rule_executions(
        self,
        request: CodePipelineListRuleExecutionsRequest,
    ) -> CodePipelineListRuleExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_rule_executions, request, CodePipelineListRuleExecutionsResponse)

    async def list_rule_executions_paginated(
        self,
        request: CodePipelineListRuleExecutionsRequest,
    ) -> list[CodePipelineListRuleExecutionsResponse]:
        return await self._paginate('list_rule_executions', request, CodePipelineListRuleExecutionsResponse)

    async def list_rule_types(
        self,
        request: CodePipelineListRuleTypesRequest | None = None,
    ) -> CodePipelineListRuleTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_rule_types, request, CodePipelineListRuleTypesResponse)

    async def list_tags_for_resource(
        self,
        request: CodePipelineListTagsForResourceRequest,
    ) -> CodePipelineListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CodePipelineListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: CodePipelineListTagsForResourceRequest,
    ) -> list[CodePipelineListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, CodePipelineListTagsForResourceResponse)

    async def list_webhooks(
        self,
        request: CodePipelineListWebhooksRequest | None = None,
    ) -> CodePipelineListWebhooksResponse:
        client = self._require_client()
        return await self._execute(client.list_webhooks, request, CodePipelineListWebhooksResponse)

    async def list_webhooks_paginated(
        self,
        request: CodePipelineListWebhooksRequest | None = None,
    ) -> list[CodePipelineListWebhooksResponse]:
        return await self._paginate('list_webhooks', request, CodePipelineListWebhooksResponse)

    async def override_stage_condition(
        self,
        request: CodePipelineOverrideStageConditionRequest,
    ) -> CodePipelineOverrideStageConditionResponse:
        client = self._require_client()
        return await self._execute(client.override_stage_condition, request, CodePipelineOverrideStageConditionResponse)

    async def poll_for_jobs(
        self,
        request: CodePipelinePollForJobsRequest,
    ) -> CodePipelinePollForJobsResponse:
        client = self._require_client()
        return await self._execute(client.poll_for_jobs, request, CodePipelinePollForJobsResponse)

    async def poll_for_third_party_jobs(
        self,
        request: CodePipelinePollForThirdPartyJobsRequest,
    ) -> CodePipelinePollForThirdPartyJobsResponse:
        client = self._require_client()
        return await self._execute(client.poll_for_third_party_jobs, request, CodePipelinePollForThirdPartyJobsResponse)

    async def put_action_revision(
        self,
        request: CodePipelinePutActionRevisionRequest,
    ) -> CodePipelinePutActionRevisionResponse:
        client = self._require_client()
        return await self._execute(client.put_action_revision, request, CodePipelinePutActionRevisionResponse)

    async def put_approval_result(
        self,
        request: CodePipelinePutApprovalResultRequest,
    ) -> CodePipelinePutApprovalResultResponse:
        client = self._require_client()
        return await self._execute(client.put_approval_result, request, CodePipelinePutApprovalResultResponse)

    async def put_job_failure_result(
        self,
        request: CodePipelinePutJobFailureResultRequest,
    ) -> CodePipelinePutJobFailureResultResponse:
        client = self._require_client()
        return await self._execute(client.put_job_failure_result, request, CodePipelinePutJobFailureResultResponse)

    async def put_job_success_result(
        self,
        request: CodePipelinePutJobSuccessResultRequest,
    ) -> CodePipelinePutJobSuccessResultResponse:
        client = self._require_client()
        return await self._execute(client.put_job_success_result, request, CodePipelinePutJobSuccessResultResponse)

    async def put_third_party_job_failure_result(
        self,
        request: CodePipelinePutThirdPartyJobFailureResultRequest,
    ) -> CodePipelinePutThirdPartyJobFailureResultResponse:
        client = self._require_client()
        return await self._execute(client.put_third_party_job_failure_result, request, CodePipelinePutThirdPartyJobFailureResultResponse)

    async def put_third_party_job_success_result(
        self,
        request: CodePipelinePutThirdPartyJobSuccessResultRequest,
    ) -> CodePipelinePutThirdPartyJobSuccessResultResponse:
        client = self._require_client()
        return await self._execute(client.put_third_party_job_success_result, request, CodePipelinePutThirdPartyJobSuccessResultResponse)

    async def put_webhook(
        self,
        request: CodePipelinePutWebhookRequest,
    ) -> CodePipelinePutWebhookResponse:
        client = self._require_client()
        return await self._execute(client.put_webhook, request, CodePipelinePutWebhookResponse)

    async def register_webhook_with_third_party(
        self,
        request: CodePipelineRegisterWebhookWithThirdPartyRequest | None = None,
    ) -> CodePipelineRegisterWebhookWithThirdPartyResponse:
        client = self._require_client()
        return await self._execute(client.register_webhook_with_third_party, request, CodePipelineRegisterWebhookWithThirdPartyResponse)

    async def retry_stage_execution(
        self,
        request: CodePipelineRetryStageExecutionRequest,
    ) -> CodePipelineRetryStageExecutionResponse:
        client = self._require_client()
        return await self._execute(client.retry_stage_execution, request, CodePipelineRetryStageExecutionResponse)

    async def rollback_stage(
        self,
        request: CodePipelineRollbackStageRequest,
    ) -> CodePipelineRollbackStageResponse:
        client = self._require_client()
        return await self._execute(client.rollback_stage, request, CodePipelineRollbackStageResponse)

    async def start_pipeline_execution(
        self,
        request: CodePipelineStartPipelineExecutionRequest,
    ) -> CodePipelineStartPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_pipeline_execution, request, CodePipelineStartPipelineExecutionResponse)

    async def stop_pipeline_execution(
        self,
        request: CodePipelineStopPipelineExecutionRequest,
    ) -> CodePipelineStopPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_pipeline_execution, request, CodePipelineStopPipelineExecutionResponse)

    async def tag_resource(
        self,
        request: CodePipelineTagResourceRequest,
    ) -> CodePipelineTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CodePipelineTagResourceResponse)

    async def untag_resource(
        self,
        request: CodePipelineUntagResourceRequest,
    ) -> CodePipelineUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CodePipelineUntagResourceResponse)

    async def update_action_type(
        self,
        request: CodePipelineUpdateActionTypeRequest,
    ) -> CodePipelineUpdateActionTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_action_type, request, CodePipelineUpdateActionTypeResponse)

    async def update_pipeline(
        self,
        request: CodePipelineUpdatePipelineRequest,
    ) -> CodePipelineUpdatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.update_pipeline, request, CodePipelineUpdatePipelineResponse)
