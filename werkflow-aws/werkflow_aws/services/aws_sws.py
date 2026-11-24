from werkflow_aws.models.sws import (
    SWFCountClosedWorkflowExecutionsRequest,
    SWFCountClosedWorkflowExecutionsResponse,
    SWFCountOpenWorkflowExecutionsRequest,
    SWFCountOpenWorkflowExecutionsResponse,
    SWFCountPendingActivityTasksRequest,
    SWFCountPendingActivityTasksResponse,
    SWFCountPendingDecisionTasksRequest,
    SWFCountPendingDecisionTasksResponse,
    SWFDeleteActivityTypeRequest,
    SWFDeleteActivityTypeResponse,
    SWFDeleteWorkflowTypeRequest,
    SWFDeleteWorkflowTypeResponse,
    SWFDeprecateActivityTypeRequest,
    SWFDeprecateActivityTypeResponse,
    SWFDeprecateDomainRequest,
    SWFDeprecateDomainResponse,
    SWFDeprecateWorkflowTypeRequest,
    SWFDeprecateWorkflowTypeResponse,
    SWFDescribeActivityTypeRequest,
    SWFDescribeActivityTypeResponse,
    SWFDescribeDomainRequest,
    SWFDescribeDomainResponse,
    SWFDescribeWorkflowExecutionRequest,
    SWFDescribeWorkflowExecutionResponse,
    SWFDescribeWorkflowTypeRequest,
    SWFDescribeWorkflowTypeResponse,
    SWFGetWorkflowExecutionHistoryRequest,
    SWFGetWorkflowExecutionHistoryResponse,
    SWFListActivityTypesRequest,
    SWFListActivityTypesResponse,
    SWFListClosedWorkflowExecutionsRequest,
    SWFListClosedWorkflowExecutionsResponse,
    SWFListDomainsRequest,
    SWFListDomainsResponse,
    SWFListOpenWorkflowExecutionsRequest,
    SWFListOpenWorkflowExecutionsResponse,
    SWFListTagsForResourceRequest,
    SWFListTagsForResourceResponse,
    SWFListWorkflowTypesRequest,
    SWFListWorkflowTypesResponse,
    SWFPollForActivityTaskRequest,
    SWFPollForActivityTaskResponse,
    SWFPollForDecisionTaskRequest,
    SWFPollForDecisionTaskResponse,
    SWFRecordActivityTaskHeartbeatRequest,
    SWFRecordActivityTaskHeartbeatResponse,
    SWFRegisterActivityTypeRequest,
    SWFRegisterActivityTypeResponse,
    SWFRegisterDomainRequest,
    SWFRegisterDomainResponse,
    SWFRegisterWorkflowTypeRequest,
    SWFRegisterWorkflowTypeResponse,
    SWFRequestCancelWorkflowExecutionRequest,
    SWFRequestCancelWorkflowExecutionResponse,
    SWFRespondActivityTaskCanceledRequest,
    SWFRespondActivityTaskCanceledResponse,
    SWFRespondActivityTaskCompletedRequest,
    SWFRespondActivityTaskCompletedResponse,
    SWFRespondActivityTaskFailedRequest,
    SWFRespondActivityTaskFailedResponse,
    SWFRespondDecisionTaskCompletedRequest,
    SWFRespondDecisionTaskCompletedResponse,
    SWFSignalWorkflowExecutionRequest,
    SWFSignalWorkflowExecutionResponse,
    SWFStartWorkflowExecutionRequest,
    SWFStartWorkflowExecutionResponse,
    SWFTagResourceRequest,
    SWFTagResourceResponse,
    SWFTerminateWorkflowExecutionRequest,
    SWFTerminateWorkflowExecutionResponse,
    SWFUndeprecateActivityTypeRequest,
    SWFUndeprecateActivityTypeResponse,
    SWFUndeprecateDomainRequest,
    SWFUndeprecateDomainResponse,
    SWFUndeprecateWorkflowTypeRequest,
    SWFUndeprecateWorkflowTypeResponse,
    SWFUntagResourceRequest,
    SWFUntagResourceResponse,
)
from werkflow_aws.types.sws_client import SWFClient
from .base import AWSBaseService


class AWSSWF(AWSBaseService[SWFClient]):
    service_name = 'sws'
    boto3_service_name = 'swf'

    def __init__(self) -> None:
        super().__init__(service_name='sws', boto3_service_name='swf')

    async def count_closed_workflow_executions(
        self,
        request: SWFCountClosedWorkflowExecutionsRequest,
    ) -> SWFCountClosedWorkflowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.count_closed_workflow_executions, request, SWFCountClosedWorkflowExecutionsResponse)

    async def count_open_workflow_executions(
        self,
        request: SWFCountOpenWorkflowExecutionsRequest,
    ) -> SWFCountOpenWorkflowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.count_open_workflow_executions, request, SWFCountOpenWorkflowExecutionsResponse)

    async def count_pending_activity_tasks(
        self,
        request: SWFCountPendingActivityTasksRequest,
    ) -> SWFCountPendingActivityTasksResponse:
        client = self._require_client()
        return await self._execute(client.count_pending_activity_tasks, request, SWFCountPendingActivityTasksResponse)

    async def count_pending_decision_tasks(
        self,
        request: SWFCountPendingDecisionTasksRequest,
    ) -> SWFCountPendingDecisionTasksResponse:
        client = self._require_client()
        return await self._execute(client.count_pending_decision_tasks, request, SWFCountPendingDecisionTasksResponse)

    async def delete_activity_type(
        self,
        request: SWFDeleteActivityTypeRequest,
    ) -> SWFDeleteActivityTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_activity_type, request, SWFDeleteActivityTypeResponse)

    async def delete_workflow_type(
        self,
        request: SWFDeleteWorkflowTypeRequest,
    ) -> SWFDeleteWorkflowTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_workflow_type, request, SWFDeleteWorkflowTypeResponse)

    async def deprecate_activity_type(
        self,
        request: SWFDeprecateActivityTypeRequest,
    ) -> SWFDeprecateActivityTypeResponse:
        client = self._require_client()
        return await self._execute(client.deprecate_activity_type, request, SWFDeprecateActivityTypeResponse)

    async def deprecate_domain(
        self,
        request: SWFDeprecateDomainRequest,
    ) -> SWFDeprecateDomainResponse:
        client = self._require_client()
        return await self._execute(client.deprecate_domain, request, SWFDeprecateDomainResponse)

    async def deprecate_workflow_type(
        self,
        request: SWFDeprecateWorkflowTypeRequest,
    ) -> SWFDeprecateWorkflowTypeResponse:
        client = self._require_client()
        return await self._execute(client.deprecate_workflow_type, request, SWFDeprecateWorkflowTypeResponse)

    async def describe_activity_type(
        self,
        request: SWFDescribeActivityTypeRequest,
    ) -> SWFDescribeActivityTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_activity_type, request, SWFDescribeActivityTypeResponse)

    async def describe_domain(
        self,
        request: SWFDescribeDomainRequest,
    ) -> SWFDescribeDomainResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain, request, SWFDescribeDomainResponse)

    async def describe_workflow_execution(
        self,
        request: SWFDescribeWorkflowExecutionRequest,
    ) -> SWFDescribeWorkflowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_workflow_execution, request, SWFDescribeWorkflowExecutionResponse)

    async def describe_workflow_type(
        self,
        request: SWFDescribeWorkflowTypeRequest,
    ) -> SWFDescribeWorkflowTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_workflow_type, request, SWFDescribeWorkflowTypeResponse)

    async def get_workflow_execution_history(
        self,
        request: SWFGetWorkflowExecutionHistoryRequest,
    ) -> SWFGetWorkflowExecutionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow_execution_history, request, SWFGetWorkflowExecutionHistoryResponse)

    async def get_workflow_execution_history_paginated(
        self,
        request: SWFGetWorkflowExecutionHistoryRequest,
    ) -> list[SWFGetWorkflowExecutionHistoryResponse]:
        return await self._paginate('get_workflow_execution_history', request, SWFGetWorkflowExecutionHistoryResponse)

    async def list_activity_types(
        self,
        request: SWFListActivityTypesRequest,
    ) -> SWFListActivityTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_activity_types, request, SWFListActivityTypesResponse)

    async def list_activity_types_paginated(
        self,
        request: SWFListActivityTypesRequest,
    ) -> list[SWFListActivityTypesResponse]:
        return await self._paginate('list_activity_types', request, SWFListActivityTypesResponse)

    async def list_closed_workflow_executions(
        self,
        request: SWFListClosedWorkflowExecutionsRequest,
    ) -> SWFListClosedWorkflowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_closed_workflow_executions, request, SWFListClosedWorkflowExecutionsResponse)

    async def list_closed_workflow_executions_paginated(
        self,
        request: SWFListClosedWorkflowExecutionsRequest,
    ) -> list[SWFListClosedWorkflowExecutionsResponse]:
        return await self._paginate('list_closed_workflow_executions', request, SWFListClosedWorkflowExecutionsResponse)

    async def list_domains(
        self,
        request: SWFListDomainsRequest,
    ) -> SWFListDomainsResponse:
        client = self._require_client()
        return await self._execute(client.list_domains, request, SWFListDomainsResponse)

    async def list_domains_paginated(
        self,
        request: SWFListDomainsRequest,
    ) -> list[SWFListDomainsResponse]:
        return await self._paginate('list_domains', request, SWFListDomainsResponse)

    async def list_open_workflow_executions(
        self,
        request: SWFListOpenWorkflowExecutionsRequest,
    ) -> SWFListOpenWorkflowExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_open_workflow_executions, request, SWFListOpenWorkflowExecutionsResponse)

    async def list_open_workflow_executions_paginated(
        self,
        request: SWFListOpenWorkflowExecutionsRequest,
    ) -> list[SWFListOpenWorkflowExecutionsResponse]:
        return await self._paginate('list_open_workflow_executions', request, SWFListOpenWorkflowExecutionsResponse)

    async def list_tags_for_resource(
        self,
        request: SWFListTagsForResourceRequest,
    ) -> SWFListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SWFListTagsForResourceResponse)

    async def list_workflow_types(
        self,
        request: SWFListWorkflowTypesRequest,
    ) -> SWFListWorkflowTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_workflow_types, request, SWFListWorkflowTypesResponse)

    async def list_workflow_types_paginated(
        self,
        request: SWFListWorkflowTypesRequest,
    ) -> list[SWFListWorkflowTypesResponse]:
        return await self._paginate('list_workflow_types', request, SWFListWorkflowTypesResponse)

    async def poll_for_activity_task(
        self,
        request: SWFPollForActivityTaskRequest,
    ) -> SWFPollForActivityTaskResponse:
        client = self._require_client()
        return await self._execute(client.poll_for_activity_task, request, SWFPollForActivityTaskResponse)

    async def poll_for_decision_task(
        self,
        request: SWFPollForDecisionTaskRequest,
    ) -> SWFPollForDecisionTaskResponse:
        client = self._require_client()
        return await self._execute(client.poll_for_decision_task, request, SWFPollForDecisionTaskResponse)

    async def poll_for_decision_task_paginated(
        self,
        request: SWFPollForDecisionTaskRequest,
    ) -> list[SWFPollForDecisionTaskResponse]:
        return await self._paginate('poll_for_decision_task', request, SWFPollForDecisionTaskResponse)

    async def record_activity_task_heartbeat(
        self,
        request: SWFRecordActivityTaskHeartbeatRequest,
    ) -> SWFRecordActivityTaskHeartbeatResponse:
        client = self._require_client()
        return await self._execute(client.record_activity_task_heartbeat, request, SWFRecordActivityTaskHeartbeatResponse)

    async def register_activity_type(
        self,
        request: SWFRegisterActivityTypeRequest,
    ) -> SWFRegisterActivityTypeResponse:
        client = self._require_client()
        return await self._execute(client.register_activity_type, request, SWFRegisterActivityTypeResponse)

    async def register_domain(
        self,
        request: SWFRegisterDomainRequest,
    ) -> SWFRegisterDomainResponse:
        client = self._require_client()
        return await self._execute(client.register_domain, request, SWFRegisterDomainResponse)

    async def register_workflow_type(
        self,
        request: SWFRegisterWorkflowTypeRequest,
    ) -> SWFRegisterWorkflowTypeResponse:
        client = self._require_client()
        return await self._execute(client.register_workflow_type, request, SWFRegisterWorkflowTypeResponse)

    async def request_cancel_workflow_execution(
        self,
        request: SWFRequestCancelWorkflowExecutionRequest,
    ) -> SWFRequestCancelWorkflowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.request_cancel_workflow_execution, request, SWFRequestCancelWorkflowExecutionResponse)

    async def respond_activity_task_canceled(
        self,
        request: SWFRespondActivityTaskCanceledRequest,
    ) -> SWFRespondActivityTaskCanceledResponse:
        client = self._require_client()
        return await self._execute(client.respond_activity_task_canceled, request, SWFRespondActivityTaskCanceledResponse)

    async def respond_activity_task_completed(
        self,
        request: SWFRespondActivityTaskCompletedRequest,
    ) -> SWFRespondActivityTaskCompletedResponse:
        client = self._require_client()
        return await self._execute(client.respond_activity_task_completed, request, SWFRespondActivityTaskCompletedResponse)

    async def respond_activity_task_failed(
        self,
        request: SWFRespondActivityTaskFailedRequest,
    ) -> SWFRespondActivityTaskFailedResponse:
        client = self._require_client()
        return await self._execute(client.respond_activity_task_failed, request, SWFRespondActivityTaskFailedResponse)

    async def respond_decision_task_completed(
        self,
        request: SWFRespondDecisionTaskCompletedRequest,
    ) -> SWFRespondDecisionTaskCompletedResponse:
        client = self._require_client()
        return await self._execute(client.respond_decision_task_completed, request, SWFRespondDecisionTaskCompletedResponse)

    async def signal_workflow_execution(
        self,
        request: SWFSignalWorkflowExecutionRequest,
    ) -> SWFSignalWorkflowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.signal_workflow_execution, request, SWFSignalWorkflowExecutionResponse)

    async def start_workflow_execution(
        self,
        request: SWFStartWorkflowExecutionRequest,
    ) -> SWFStartWorkflowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_workflow_execution, request, SWFStartWorkflowExecutionResponse)

    async def tag_resource(
        self,
        request: SWFTagResourceRequest,
    ) -> SWFTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SWFTagResourceResponse)

    async def terminate_workflow_execution(
        self,
        request: SWFTerminateWorkflowExecutionRequest,
    ) -> SWFTerminateWorkflowExecutionResponse:
        client = self._require_client()
        return await self._execute(client.terminate_workflow_execution, request, SWFTerminateWorkflowExecutionResponse)

    async def undeprecate_activity_type(
        self,
        request: SWFUndeprecateActivityTypeRequest,
    ) -> SWFUndeprecateActivityTypeResponse:
        client = self._require_client()
        return await self._execute(client.undeprecate_activity_type, request, SWFUndeprecateActivityTypeResponse)

    async def undeprecate_domain(
        self,
        request: SWFUndeprecateDomainRequest,
    ) -> SWFUndeprecateDomainResponse:
        client = self._require_client()
        return await self._execute(client.undeprecate_domain, request, SWFUndeprecateDomainResponse)

    async def undeprecate_workflow_type(
        self,
        request: SWFUndeprecateWorkflowTypeRequest,
    ) -> SWFUndeprecateWorkflowTypeResponse:
        client = self._require_client()
        return await self._execute(client.undeprecate_workflow_type, request, SWFUndeprecateWorkflowTypeResponse)

    async def untag_resource(
        self,
        request: SWFUntagResourceRequest,
    ) -> SWFUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SWFUntagResourceResponse)
