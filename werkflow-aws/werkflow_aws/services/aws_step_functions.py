from werkflow_aws.models.step_functions import (
    StepFunctionsCreateActivityRequest,
    StepFunctionsCreateActivityResponse,
    StepFunctionsCreateStateMachineAliasRequest,
    StepFunctionsCreateStateMachineAliasResponse,
    StepFunctionsCreateStateMachineRequest,
    StepFunctionsCreateStateMachineResponse,
    StepFunctionsDeleteActivityRequest,
    StepFunctionsDeleteActivityResponse,
    StepFunctionsDeleteStateMachineAliasRequest,
    StepFunctionsDeleteStateMachineAliasResponse,
    StepFunctionsDeleteStateMachineRequest,
    StepFunctionsDeleteStateMachineResponse,
    StepFunctionsDeleteStateMachineVersionRequest,
    StepFunctionsDeleteStateMachineVersionResponse,
    StepFunctionsDescribeActivityRequest,
    StepFunctionsDescribeActivityResponse,
    StepFunctionsDescribeExecutionRequest,
    StepFunctionsDescribeExecutionResponse,
    StepFunctionsDescribeMapRunRequest,
    StepFunctionsDescribeMapRunResponse,
    StepFunctionsDescribeStateMachineAliasRequest,
    StepFunctionsDescribeStateMachineAliasResponse,
    StepFunctionsDescribeStateMachineForExecutionRequest,
    StepFunctionsDescribeStateMachineForExecutionResponse,
    StepFunctionsDescribeStateMachineRequest,
    StepFunctionsDescribeStateMachineResponse,
    StepFunctionsGetActivityTaskRequest,
    StepFunctionsGetActivityTaskResponse,
    StepFunctionsGetExecutionHistoryRequest,
    StepFunctionsGetExecutionHistoryResponse,
    StepFunctionsListActivitiesRequest,
    StepFunctionsListActivitiesResponse,
    StepFunctionsListExecutionsRequest,
    StepFunctionsListExecutionsResponse,
    StepFunctionsListMapRunsRequest,
    StepFunctionsListMapRunsResponse,
    StepFunctionsListStateMachineAliasesRequest,
    StepFunctionsListStateMachineAliasesResponse,
    StepFunctionsListStateMachineVersionsRequest,
    StepFunctionsListStateMachineVersionsResponse,
    StepFunctionsListStateMachinesRequest,
    StepFunctionsListStateMachinesResponse,
    StepFunctionsListTagsForResourceRequest,
    StepFunctionsListTagsForResourceResponse,
    StepFunctionsPublishStateMachineVersionRequest,
    StepFunctionsPublishStateMachineVersionResponse,
    StepFunctionsRedriveExecutionRequest,
    StepFunctionsRedriveExecutionResponse,
    StepFunctionsSendTaskFailureRequest,
    StepFunctionsSendTaskFailureResponse,
    StepFunctionsSendTaskHeartbeatRequest,
    StepFunctionsSendTaskHeartbeatResponse,
    StepFunctionsSendTaskSuccessRequest,
    StepFunctionsSendTaskSuccessResponse,
    StepFunctionsStartExecutionRequest,
    StepFunctionsStartExecutionResponse,
    StepFunctionsStartSyncExecutionRequest,
    StepFunctionsStartSyncExecutionResponse,
    StepFunctionsStopExecutionRequest,
    StepFunctionsStopExecutionResponse,
    StepFunctionsTagResourceRequest,
    StepFunctionsTagResourceResponse,
    StepFunctionsTestStateRequest,
    StepFunctionsTestStateResponse,
    StepFunctionsUntagResourceRequest,
    StepFunctionsUntagResourceResponse,
    StepFunctionsUpdateMapRunRequest,
    StepFunctionsUpdateMapRunResponse,
    StepFunctionsUpdateStateMachineAliasRequest,
    StepFunctionsUpdateStateMachineAliasResponse,
    StepFunctionsUpdateStateMachineRequest,
    StepFunctionsUpdateStateMachineResponse,
    StepFunctionsValidateStateMachineDefinitionRequest,
    StepFunctionsValidateStateMachineDefinitionResponse,
)
from werkflow_aws.types.step_functions_client import StepFunctionsClient
from .base import AWSBaseService


class AWSStepFunctions(AWSBaseService[StepFunctionsClient]):
    service_name = 'step-functions'
    boto3_service_name = 'stepfunctions'

    def __init__(self) -> None:
        super().__init__(service_name='step-functions', boto3_service_name='stepfunctions')

    async def create_activity(
        self,
        request: StepFunctionsCreateActivityRequest,
    ) -> StepFunctionsCreateActivityResponse:
        client = self._require_client()
        return await self._execute(client.create_activity, request, StepFunctionsCreateActivityResponse)

    async def create_state_machine(
        self,
        request: StepFunctionsCreateStateMachineRequest,
    ) -> StepFunctionsCreateStateMachineResponse:
        client = self._require_client()
        return await self._execute(client.create_state_machine, request, StepFunctionsCreateStateMachineResponse)

    async def create_state_machine_alias(
        self,
        request: StepFunctionsCreateStateMachineAliasRequest,
    ) -> StepFunctionsCreateStateMachineAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_state_machine_alias, request, StepFunctionsCreateStateMachineAliasResponse)

    async def delete_activity(
        self,
        request: StepFunctionsDeleteActivityRequest,
    ) -> StepFunctionsDeleteActivityResponse:
        client = self._require_client()
        return await self._execute(client.delete_activity, request, StepFunctionsDeleteActivityResponse)

    async def delete_state_machine(
        self,
        request: StepFunctionsDeleteStateMachineRequest,
    ) -> StepFunctionsDeleteStateMachineResponse:
        client = self._require_client()
        return await self._execute(client.delete_state_machine, request, StepFunctionsDeleteStateMachineResponse)

    async def delete_state_machine_alias(
        self,
        request: StepFunctionsDeleteStateMachineAliasRequest,
    ) -> StepFunctionsDeleteStateMachineAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_state_machine_alias, request, StepFunctionsDeleteStateMachineAliasResponse)

    async def delete_state_machine_version(
        self,
        request: StepFunctionsDeleteStateMachineVersionRequest,
    ) -> StepFunctionsDeleteStateMachineVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_state_machine_version, request, StepFunctionsDeleteStateMachineVersionResponse)

    async def describe_activity(
        self,
        request: StepFunctionsDescribeActivityRequest,
    ) -> StepFunctionsDescribeActivityResponse:
        client = self._require_client()
        return await self._execute(client.describe_activity, request, StepFunctionsDescribeActivityResponse)

    async def describe_execution(
        self,
        request: StepFunctionsDescribeExecutionRequest,
    ) -> StepFunctionsDescribeExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_execution, request, StepFunctionsDescribeExecutionResponse)

    async def describe_map_run(
        self,
        request: StepFunctionsDescribeMapRunRequest,
    ) -> StepFunctionsDescribeMapRunResponse:
        client = self._require_client()
        return await self._execute(client.describe_map_run, request, StepFunctionsDescribeMapRunResponse)

    async def describe_state_machine(
        self,
        request: StepFunctionsDescribeStateMachineRequest,
    ) -> StepFunctionsDescribeStateMachineResponse:
        client = self._require_client()
        return await self._execute(client.describe_state_machine, request, StepFunctionsDescribeStateMachineResponse)

    async def describe_state_machine_alias(
        self,
        request: StepFunctionsDescribeStateMachineAliasRequest,
    ) -> StepFunctionsDescribeStateMachineAliasResponse:
        client = self._require_client()
        return await self._execute(client.describe_state_machine_alias, request, StepFunctionsDescribeStateMachineAliasResponse)

    async def describe_state_machine_for_execution(
        self,
        request: StepFunctionsDescribeStateMachineForExecutionRequest,
    ) -> StepFunctionsDescribeStateMachineForExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_state_machine_for_execution, request, StepFunctionsDescribeStateMachineForExecutionResponse)

    async def get_activity_task(
        self,
        request: StepFunctionsGetActivityTaskRequest,
    ) -> StepFunctionsGetActivityTaskResponse:
        client = self._require_client()
        return await self._execute(client.get_activity_task, request, StepFunctionsGetActivityTaskResponse)

    async def get_execution_history(
        self,
        request: StepFunctionsGetExecutionHistoryRequest,
    ) -> StepFunctionsGetExecutionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_execution_history, request, StepFunctionsGetExecutionHistoryResponse)

    async def get_execution_history_paginated(
        self,
        request: StepFunctionsGetExecutionHistoryRequest,
    ) -> list[StepFunctionsGetExecutionHistoryResponse]:
        return await self._paginate('get_execution_history', request, StepFunctionsGetExecutionHistoryResponse)

    async def list_activities(
        self,
        request: StepFunctionsListActivitiesRequest | None = None,
    ) -> StepFunctionsListActivitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_activities, request, StepFunctionsListActivitiesResponse)

    async def list_activities_paginated(
        self,
        request: StepFunctionsListActivitiesRequest | None = None,
    ) -> list[StepFunctionsListActivitiesResponse]:
        return await self._paginate('list_activities', request, StepFunctionsListActivitiesResponse)

    async def list_executions(
        self,
        request: StepFunctionsListExecutionsRequest | None = None,
    ) -> StepFunctionsListExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_executions, request, StepFunctionsListExecutionsResponse)

    async def list_executions_paginated(
        self,
        request: StepFunctionsListExecutionsRequest | None = None,
    ) -> list[StepFunctionsListExecutionsResponse]:
        return await self._paginate('list_executions', request, StepFunctionsListExecutionsResponse)

    async def list_map_runs(
        self,
        request: StepFunctionsListMapRunsRequest,
    ) -> StepFunctionsListMapRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_map_runs, request, StepFunctionsListMapRunsResponse)

    async def list_map_runs_paginated(
        self,
        request: StepFunctionsListMapRunsRequest,
    ) -> list[StepFunctionsListMapRunsResponse]:
        return await self._paginate('list_map_runs', request, StepFunctionsListMapRunsResponse)

    async def list_state_machine_aliases(
        self,
        request: StepFunctionsListStateMachineAliasesRequest,
    ) -> StepFunctionsListStateMachineAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_state_machine_aliases, request, StepFunctionsListStateMachineAliasesResponse)

    async def list_state_machine_versions(
        self,
        request: StepFunctionsListStateMachineVersionsRequest,
    ) -> StepFunctionsListStateMachineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_state_machine_versions, request, StepFunctionsListStateMachineVersionsResponse)

    async def list_state_machines(
        self,
        request: StepFunctionsListStateMachinesRequest | None = None,
    ) -> StepFunctionsListStateMachinesResponse:
        client = self._require_client()
        return await self._execute(client.list_state_machines, request, StepFunctionsListStateMachinesResponse)

    async def list_state_machines_paginated(
        self,
        request: StepFunctionsListStateMachinesRequest | None = None,
    ) -> list[StepFunctionsListStateMachinesResponse]:
        return await self._paginate('list_state_machines', request, StepFunctionsListStateMachinesResponse)

    async def list_tags_for_resource(
        self,
        request: StepFunctionsListTagsForResourceRequest,
    ) -> StepFunctionsListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, StepFunctionsListTagsForResourceResponse)

    async def publish_state_machine_version(
        self,
        request: StepFunctionsPublishStateMachineVersionRequest,
    ) -> StepFunctionsPublishStateMachineVersionResponse:
        client = self._require_client()
        return await self._execute(client.publish_state_machine_version, request, StepFunctionsPublishStateMachineVersionResponse)

    async def redrive_execution(
        self,
        request: StepFunctionsRedriveExecutionRequest,
    ) -> StepFunctionsRedriveExecutionResponse:
        client = self._require_client()
        return await self._execute(client.redrive_execution, request, StepFunctionsRedriveExecutionResponse)

    async def send_task_failure(
        self,
        request: StepFunctionsSendTaskFailureRequest,
    ) -> StepFunctionsSendTaskFailureResponse:
        client = self._require_client()
        return await self._execute(client.send_task_failure, request, StepFunctionsSendTaskFailureResponse)

    async def send_task_heartbeat(
        self,
        request: StepFunctionsSendTaskHeartbeatRequest,
    ) -> StepFunctionsSendTaskHeartbeatResponse:
        client = self._require_client()
        return await self._execute(client.send_task_heartbeat, request, StepFunctionsSendTaskHeartbeatResponse)

    async def send_task_success(
        self,
        request: StepFunctionsSendTaskSuccessRequest,
    ) -> StepFunctionsSendTaskSuccessResponse:
        client = self._require_client()
        return await self._execute(client.send_task_success, request, StepFunctionsSendTaskSuccessResponse)

    async def start_execution(
        self,
        request: StepFunctionsStartExecutionRequest,
    ) -> StepFunctionsStartExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_execution, request, StepFunctionsStartExecutionResponse)

    async def start_sync_execution(
        self,
        request: StepFunctionsStartSyncExecutionRequest,
    ) -> StepFunctionsStartSyncExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_sync_execution, request, StepFunctionsStartSyncExecutionResponse)

    async def stop_execution(
        self,
        request: StepFunctionsStopExecutionRequest,
    ) -> StepFunctionsStopExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_execution, request, StepFunctionsStopExecutionResponse)

    async def tag_resource(
        self,
        request: StepFunctionsTagResourceRequest,
    ) -> StepFunctionsTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, StepFunctionsTagResourceResponse)

    async def test_state(
        self,
        request: StepFunctionsTestStateRequest,
    ) -> StepFunctionsTestStateResponse:
        client = self._require_client()
        return await self._execute(client.test_state, request, StepFunctionsTestStateResponse)

    async def untag_resource(
        self,
        request: StepFunctionsUntagResourceRequest,
    ) -> StepFunctionsUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, StepFunctionsUntagResourceResponse)

    async def update_map_run(
        self,
        request: StepFunctionsUpdateMapRunRequest,
    ) -> StepFunctionsUpdateMapRunResponse:
        client = self._require_client()
        return await self._execute(client.update_map_run, request, StepFunctionsUpdateMapRunResponse)

    async def update_state_machine(
        self,
        request: StepFunctionsUpdateStateMachineRequest,
    ) -> StepFunctionsUpdateStateMachineResponse:
        client = self._require_client()
        return await self._execute(client.update_state_machine, request, StepFunctionsUpdateStateMachineResponse)

    async def update_state_machine_alias(
        self,
        request: StepFunctionsUpdateStateMachineAliasRequest,
    ) -> StepFunctionsUpdateStateMachineAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_state_machine_alias, request, StepFunctionsUpdateStateMachineAliasResponse)

    async def validate_state_machine_definition(
        self,
        request: StepFunctionsValidateStateMachineDefinitionRequest,
    ) -> StepFunctionsValidateStateMachineDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.validate_state_machine_definition, request, StepFunctionsValidateStateMachineDefinitionResponse)
