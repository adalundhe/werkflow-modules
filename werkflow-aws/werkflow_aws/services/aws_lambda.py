from werkflow_aws.models.aws_lambda import (
    LambdaCreateAliasRequest,
    LambdaCreateAliasResponse,
    LambdaCreateEventSourceMappingRequest,
    LambdaCreateEventSourceMappingResponse,
    LambdaCreateFunctionRequest,
    LambdaCreateFunctionResponse,
    LambdaDeleteAliasRequest,
    LambdaDeleteAliasResponse,
    LambdaDeleteEventSourceMappingRequest,
    LambdaDeleteEventSourceMappingResponse,
    LambdaDeleteFunctionRequest,
    LambdaDeleteFunctionResponse,
    LambdaGetAliasRequest,
    LambdaGetAliasResponse,
    LambdaGetFunctionConfigurationRequest,
    LambdaGetFunctionConfigurationResponse,
    LambdaGetFunctionRequest,
    LambdaGetFunctionResponse,
    LambdaInvokeRequest,
    LambdaInvokeResponse,
    LambdaListAliasesRequest,
    LambdaListAliasesResponse,
    LambdaListEventSourceMappingsRequest,
    LambdaListEventSourceMappingsResponse,
    LambdaListFunctionsRequest,
    LambdaListFunctionsResponse,
    LambdaListLayersRequest,
    LambdaListLayersResponse,
    LambdaListTagsRequest,
    LambdaListTagsResponse,
    LambdaListVersionsByFunctionRequest,
    LambdaListVersionsByFunctionResponse,
    LambdaPublishVersionRequest,
    LambdaPublishVersionResponse,
    LambdaTagResourceRequest,
    LambdaTagResourceResponse,
    LambdaUntagResourceRequest,
    LambdaUntagResourceResponse,
    LambdaUpdateAliasRequest,
    LambdaUpdateAliasResponse,
    LambdaUpdateFunctionCodeRequest,
    LambdaUpdateFunctionCodeResponse,
    LambdaUpdateFunctionConfigurationRequest,
    LambdaUpdateFunctionConfigurationResponse,
)
from werkflow_aws.types.lambda_client import LambdaClient
from .base import AWSBaseService
from werkflow_aws.models.aws_lambda import (
    LambdaAddLayerVersionPermissionRequest,
    LambdaAddLayerVersionPermissionResponse,
    LambdaAddPermissionRequest,
    LambdaAddPermissionResponse,
    LambdaCheckpointDurableExecutionRequest,
    LambdaCheckpointDurableExecutionResponse,
    LambdaCreateCapacityProviderRequest,
    LambdaCreateCapacityProviderResponse,
    LambdaCreateCodeSigningConfigRequest,
    LambdaCreateCodeSigningConfigResponse,
    LambdaCreateFunctionUrlConfigRequest,
    LambdaCreateFunctionUrlConfigResponse,
    LambdaDeleteCapacityProviderRequest,
    LambdaDeleteCapacityProviderResponse,
    LambdaDeleteCodeSigningConfigRequest,
    LambdaDeleteCodeSigningConfigResponse,
    LambdaDeleteDurableExecutionRequest,
    LambdaDeleteDurableExecutionResponse,
    LambdaDeleteFunctionCodeSigningConfigRequest,
    LambdaDeleteFunctionCodeSigningConfigResponse,
    LambdaDeleteFunctionConcurrencyRequest,
    LambdaDeleteFunctionConcurrencyResponse,
    LambdaDeleteFunctionEventInvokeConfigRequest,
    LambdaDeleteFunctionEventInvokeConfigResponse,
    LambdaDeleteFunctionUrlConfigRequest,
    LambdaDeleteFunctionUrlConfigResponse,
    LambdaDeleteLayerVersionRequest,
    LambdaDeleteLayerVersionResponse,
    LambdaDeleteProvisionedConcurrencyConfigRequest,
    LambdaDeleteProvisionedConcurrencyConfigResponse,
    LambdaDeleteResourcePolicyRequest,
    LambdaDeleteResourcePolicyResponse,
    LambdaGetAccountSettingsRequest,
    LambdaGetAccountSettingsResponse,
    LambdaGetCapacityProviderRequest,
    LambdaGetCapacityProviderResponse,
    LambdaGetCodeSigningConfigRequest,
    LambdaGetCodeSigningConfigResponse,
    LambdaGetDurableExecutionHistoryRequest,
    LambdaGetDurableExecutionHistoryResponse,
    LambdaGetDurableExecutionRequest,
    LambdaGetDurableExecutionResponse,
    LambdaGetDurableExecutionStateRequest,
    LambdaGetDurableExecutionStateResponse,
    LambdaGetEventSourceMappingRequest,
    LambdaGetEventSourceMappingResponse,
    LambdaGetFunctionCodeSigningConfigRequest,
    LambdaGetFunctionCodeSigningConfigResponse,
    LambdaGetFunctionConcurrencyRequest,
    LambdaGetFunctionConcurrencyResponse,
    LambdaGetFunctionEventInvokeConfigRequest,
    LambdaGetFunctionEventInvokeConfigResponse,
    LambdaGetFunctionRecursionConfigRequest,
    LambdaGetFunctionRecursionConfigResponse,
    LambdaGetFunctionScalingConfigRequest,
    LambdaGetFunctionScalingConfigResponse,
    LambdaGetFunctionUrlConfigRequest,
    LambdaGetFunctionUrlConfigResponse,
    LambdaGetLayerVersionByArnRequest,
    LambdaGetLayerVersionByArnResponse,
    LambdaGetLayerVersionPolicyRequest,
    LambdaGetLayerVersionPolicyResponse,
    LambdaGetLayerVersionRequest,
    LambdaGetLayerVersionResponse,
    LambdaGetPolicyRequest,
    LambdaGetPolicyResponse,
    LambdaGetProvisionedConcurrencyConfigRequest,
    LambdaGetProvisionedConcurrencyConfigResponse,
    LambdaGetResourcePolicyRequest,
    LambdaGetResourcePolicyResponse,
    LambdaGetRuntimeManagementConfigRequest,
    LambdaGetRuntimeManagementConfigResponse,
    LambdaInvokeAsyncRequest,
    LambdaInvokeAsyncResponse,
    LambdaInvokeWithResponseStreamRequest,
    LambdaInvokeWithResponseStreamResponse,
    LambdaListCapacityProvidersRequest,
    LambdaListCapacityProvidersResponse,
    LambdaListCodeSigningConfigsRequest,
    LambdaListCodeSigningConfigsResponse,
    LambdaListDurableExecutionsByFunctionRequest,
    LambdaListDurableExecutionsByFunctionResponse,
    LambdaListFunctionEventInvokeConfigsRequest,
    LambdaListFunctionEventInvokeConfigsResponse,
    LambdaListFunctionUrlConfigsRequest,
    LambdaListFunctionUrlConfigsResponse,
    LambdaListFunctionVersionsByCapacityProviderRequest,
    LambdaListFunctionVersionsByCapacityProviderResponse,
    LambdaListFunctionsByCodeSigningConfigRequest,
    LambdaListFunctionsByCodeSigningConfigResponse,
    LambdaListLayerVersionsRequest,
    LambdaListLayerVersionsResponse,
    LambdaListProvisionedConcurrencyConfigsRequest,
    LambdaListProvisionedConcurrencyConfigsResponse,
    LambdaPauseDurableExecutionRequest,
    LambdaPauseDurableExecutionResponse,
    LambdaPublishLayerVersionRequest,
    LambdaPublishLayerVersionResponse,
    LambdaPutFunctionCodeSigningConfigRequest,
    LambdaPutFunctionCodeSigningConfigResponse,
    LambdaPutFunctionConcurrencyRequest,
    LambdaPutFunctionConcurrencyResponse,
    LambdaPutFunctionEventInvokeConfigRequest,
    LambdaPutFunctionEventInvokeConfigResponse,
    LambdaPutFunctionRecursionConfigRequest,
    LambdaPutFunctionRecursionConfigResponse,
    LambdaPutFunctionScalingConfigRequest,
    LambdaPutFunctionScalingConfigResponse,
    LambdaPutProvisionedConcurrencyConfigRequest,
    LambdaPutProvisionedConcurrencyConfigResponse,
    LambdaPutResourcePolicyRequest,
    LambdaPutResourcePolicyResponse,
    LambdaPutRuntimeManagementConfigRequest,
    LambdaPutRuntimeManagementConfigResponse,
    LambdaRemoveLayerVersionPermissionRequest,
    LambdaRemoveLayerVersionPermissionResponse,
    LambdaRemovePermissionRequest,
    LambdaRemovePermissionResponse,
    LambdaResumeDurableExecutionRequest,
    LambdaResumeDurableExecutionResponse,
    LambdaSendDurableExecutionCallbackFailureRequest,
    LambdaSendDurableExecutionCallbackFailureResponse,
    LambdaSendDurableExecutionCallbackHeartbeatRequest,
    LambdaSendDurableExecutionCallbackHeartbeatResponse,
    LambdaSendDurableExecutionCallbackSuccessRequest,
    LambdaSendDurableExecutionCallbackSuccessResponse,
    LambdaStopDurableExecutionRequest,
    LambdaStopDurableExecutionResponse,
    LambdaUpdateCapacityProviderRequest,
    LambdaUpdateCapacityProviderResponse,
    LambdaUpdateCodeSigningConfigRequest,
    LambdaUpdateCodeSigningConfigResponse,
    LambdaUpdateEventSourceMappingRequest,
    LambdaUpdateEventSourceMappingResponse,
    LambdaUpdateFunctionEventInvokeConfigRequest,
    LambdaUpdateFunctionEventInvokeConfigResponse,
    LambdaUpdateFunctionUrlConfigRequest,
    LambdaUpdateFunctionUrlConfigResponse,
)


class AWSLambda(AWSBaseService[LambdaClient]):
    service_name = 'Lambda'
    boto3_service_name = 'lambda'

    def __init__(self) -> None:
        super().__init__(
            service_name='Lambda',
            boto3_service_name='lambda',
        )

    async def list_functions(
        self,
        request: LambdaListFunctionsRequest | None = None,
    ) -> LambdaListFunctionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_functions,
            request or LambdaListFunctionsRequest(),
            LambdaListFunctionsResponse,
        )

    async def list_functions_paginated(
        self,
        request: LambdaListFunctionsRequest | None = None,
    ) -> list[LambdaListFunctionsResponse]:
        return await self._paginate(
            'list_functions',
            request or LambdaListFunctionsRequest(),
            LambdaListFunctionsResponse,
        )

    async def get_function(
        self,
        request: LambdaGetFunctionRequest,
    ) -> LambdaGetFunctionResponse:
        client = self._require_client()
        return await self._execute(
            client.get_function,
            request,
            LambdaGetFunctionResponse,
        )

    async def get_function_configuration(
        self,
        request: LambdaGetFunctionConfigurationRequest,
    ) -> LambdaGetFunctionConfigurationResponse:
        client = self._require_client()
        return await self._execute(
            client.get_function_configuration,
            request,
            LambdaGetFunctionConfigurationResponse,
        )

    async def create_function(
        self,
        request: LambdaCreateFunctionRequest,
    ) -> LambdaCreateFunctionResponse:
        client = self._require_client()
        return await self._execute(
            client.create_function,
            request,
            LambdaCreateFunctionResponse,
        )

    async def delete_function(
        self,
        request: LambdaDeleteFunctionRequest,
    ) -> LambdaDeleteFunctionResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_function,
            request,
            LambdaDeleteFunctionResponse,
        )

    async def update_function_code(
        self,
        request: LambdaUpdateFunctionCodeRequest,
    ) -> LambdaUpdateFunctionCodeResponse:
        client = self._require_client()
        return await self._execute(
            client.update_function_code,
            request,
            LambdaUpdateFunctionCodeResponse,
        )

    async def update_function_configuration(
        self,
        request: LambdaUpdateFunctionConfigurationRequest,
    ) -> LambdaUpdateFunctionConfigurationResponse:
        client = self._require_client()
        return await self._execute(
            client.update_function_configuration,
            request,
            LambdaUpdateFunctionConfigurationResponse,
        )

    async def invoke(
        self,
        request: LambdaInvokeRequest,
    ) -> LambdaInvokeResponse:
        client = self._require_client()
        return await self._execute(
            client.invoke,
            request,
            LambdaInvokeResponse,
        )

    async def publish_version(
        self,
        request: LambdaPublishVersionRequest,
    ) -> LambdaPublishVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.publish_version,
            request,
            LambdaPublishVersionResponse,
        )

    async def list_versions_by_function(
        self,
        request: LambdaListVersionsByFunctionRequest,
    ) -> LambdaListVersionsByFunctionResponse:
        client = self._require_client()
        return await self._execute(
            client.list_versions_by_function,
            request,
            LambdaListVersionsByFunctionResponse,
        )

    async def list_versions_by_function_paginated(
        self,
        request: LambdaListVersionsByFunctionRequest,
    ) -> list[LambdaListVersionsByFunctionResponse]:
        return await self._paginate(
            'list_versions_by_function',
            request,
            LambdaListVersionsByFunctionResponse,
        )

    async def create_alias(
        self,
        request: LambdaCreateAliasRequest,
    ) -> LambdaCreateAliasResponse:
        client = self._require_client()
        return await self._execute(
            client.create_alias,
            request,
            LambdaCreateAliasResponse,
        )

    async def get_alias(
        self,
        request: LambdaGetAliasRequest,
    ) -> LambdaGetAliasResponse:
        client = self._require_client()
        return await self._execute(
            client.get_alias,
            request,
            LambdaGetAliasResponse,
        )

    async def update_alias(
        self,
        request: LambdaUpdateAliasRequest,
    ) -> LambdaUpdateAliasResponse:
        client = self._require_client()
        return await self._execute(
            client.update_alias,
            request,
            LambdaUpdateAliasResponse,
        )

    async def delete_alias(
        self,
        request: LambdaDeleteAliasRequest,
    ) -> LambdaDeleteAliasResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_alias,
            request,
            LambdaDeleteAliasResponse,
        )

    async def list_aliases(
        self,
        request: LambdaListAliasesRequest,
    ) -> LambdaListAliasesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_aliases,
            request,
            LambdaListAliasesResponse,
        )

    async def list_aliases_paginated(
        self,
        request: LambdaListAliasesRequest,
    ) -> list[LambdaListAliasesResponse]:
        return await self._paginate(
            'list_aliases',
            request,
            LambdaListAliasesResponse,
        )

    async def list_layers(
        self,
        request: LambdaListLayersRequest | None = None,
    ) -> LambdaListLayersResponse:
        client = self._require_client()
        return await self._execute(
            client.list_layers,
            request or LambdaListLayersRequest(),
            LambdaListLayersResponse,
        )

    async def list_layers_paginated(
        self,
        request: LambdaListLayersRequest | None = None,
    ) -> list[LambdaListLayersResponse]:
        return await self._paginate(
            'list_layers',
            request or LambdaListLayersRequest(),
            LambdaListLayersResponse,
        )

    async def list_event_source_mappings(
        self,
        request: LambdaListEventSourceMappingsRequest | None = None,
    ) -> LambdaListEventSourceMappingsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_event_source_mappings,
            request or LambdaListEventSourceMappingsRequest(),
            LambdaListEventSourceMappingsResponse,
        )

    async def list_event_source_mappings_paginated(
        self,
        request: LambdaListEventSourceMappingsRequest | None = None,
    ) -> list[LambdaListEventSourceMappingsResponse]:
        return await self._paginate(
            'list_event_source_mappings',
            request or LambdaListEventSourceMappingsRequest(),
            LambdaListEventSourceMappingsResponse,
        )

    async def create_event_source_mapping(
        self,
        request: LambdaCreateEventSourceMappingRequest,
    ) -> LambdaCreateEventSourceMappingResponse:
        client = self._require_client()
        return await self._execute(
            client.create_event_source_mapping,
            request,
            LambdaCreateEventSourceMappingResponse,
        )

    async def delete_event_source_mapping(
        self,
        request: LambdaDeleteEventSourceMappingRequest,
    ) -> LambdaDeleteEventSourceMappingResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_event_source_mapping,
            request,
            LambdaDeleteEventSourceMappingResponse,
        )

    async def list_tags(
        self,
        request: LambdaListTagsRequest,
    ) -> LambdaListTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags,
            request,
            LambdaListTagsResponse,
        )

    async def tag_resource(
        self,
        request: LambdaTagResourceRequest,
    ) -> LambdaTagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            LambdaTagResourceResponse,
        )

    async def untag_resource(
        self,
        request: LambdaUntagResourceRequest,
    ) -> LambdaUntagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            LambdaUntagResourceResponse,
        )

    async def add_layer_version_permission(
        self,
        request: LambdaAddLayerVersionPermissionRequest,
    ) -> LambdaAddLayerVersionPermissionResponse:
        client = self._require_client()
        return await self._execute(client.add_layer_version_permission, request, LambdaAddLayerVersionPermissionResponse)

    async def add_permission(
        self,
        request: LambdaAddPermissionRequest,
    ) -> LambdaAddPermissionResponse:
        client = self._require_client()
        return await self._execute(client.add_permission, request, LambdaAddPermissionResponse)

    async def checkpoint_durable_execution(
        self,
        request: LambdaCheckpointDurableExecutionRequest,
    ) -> LambdaCheckpointDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.checkpoint_durable_execution, request, LambdaCheckpointDurableExecutionResponse)

    async def create_capacity_provider(
        self,
        request: LambdaCreateCapacityProviderRequest,
    ) -> LambdaCreateCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_provider, request, LambdaCreateCapacityProviderResponse)

    async def create_code_signing_config(
        self,
        request: LambdaCreateCodeSigningConfigRequest,
    ) -> LambdaCreateCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_code_signing_config, request, LambdaCreateCodeSigningConfigResponse)

    async def create_function_url_config(
        self,
        request: LambdaCreateFunctionUrlConfigRequest,
    ) -> LambdaCreateFunctionUrlConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_function_url_config, request, LambdaCreateFunctionUrlConfigResponse)

    async def delete_capacity_provider(
        self,
        request: LambdaDeleteCapacityProviderRequest,
    ) -> LambdaDeleteCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_capacity_provider, request, LambdaDeleteCapacityProviderResponse)

    async def delete_code_signing_config(
        self,
        request: LambdaDeleteCodeSigningConfigRequest,
    ) -> LambdaDeleteCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_code_signing_config, request, LambdaDeleteCodeSigningConfigResponse)

    async def delete_durable_execution(
        self,
        request: LambdaDeleteDurableExecutionRequest,
    ) -> LambdaDeleteDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.delete_durable_execution, request, LambdaDeleteDurableExecutionResponse)

    async def delete_function_code_signing_config(
        self,
        request: LambdaDeleteFunctionCodeSigningConfigRequest,
    ) -> LambdaDeleteFunctionCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_function_code_signing_config, request, LambdaDeleteFunctionCodeSigningConfigResponse)

    async def delete_function_concurrency(
        self,
        request: LambdaDeleteFunctionConcurrencyRequest,
    ) -> LambdaDeleteFunctionConcurrencyResponse:
        client = self._require_client()
        return await self._execute(client.delete_function_concurrency, request, LambdaDeleteFunctionConcurrencyResponse)

    async def delete_function_event_invoke_config(
        self,
        request: LambdaDeleteFunctionEventInvokeConfigRequest,
    ) -> LambdaDeleteFunctionEventInvokeConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_function_event_invoke_config, request, LambdaDeleteFunctionEventInvokeConfigResponse)

    async def delete_function_url_config(
        self,
        request: LambdaDeleteFunctionUrlConfigRequest,
    ) -> LambdaDeleteFunctionUrlConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_function_url_config, request, LambdaDeleteFunctionUrlConfigResponse)

    async def delete_layer_version(
        self,
        request: LambdaDeleteLayerVersionRequest,
    ) -> LambdaDeleteLayerVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_layer_version, request, LambdaDeleteLayerVersionResponse)

    async def delete_provisioned_concurrency_config(
        self,
        request: LambdaDeleteProvisionedConcurrencyConfigRequest,
    ) -> LambdaDeleteProvisionedConcurrencyConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioned_concurrency_config, request, LambdaDeleteProvisionedConcurrencyConfigResponse)

    async def delete_resource_policy(
        self,
        request: LambdaDeleteResourcePolicyRequest,
    ) -> LambdaDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, LambdaDeleteResourcePolicyResponse)

    async def get_account_settings(
        self,
        request: LambdaGetAccountSettingsRequest | None = None,
    ) -> LambdaGetAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_account_settings, request, LambdaGetAccountSettingsResponse)

    async def get_capacity_provider(
        self,
        request: LambdaGetCapacityProviderRequest,
    ) -> LambdaGetCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_provider, request, LambdaGetCapacityProviderResponse)

    async def get_code_signing_config(
        self,
        request: LambdaGetCodeSigningConfigRequest,
    ) -> LambdaGetCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_code_signing_config, request, LambdaGetCodeSigningConfigResponse)

    async def get_durable_execution(
        self,
        request: LambdaGetDurableExecutionRequest,
    ) -> LambdaGetDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.get_durable_execution, request, LambdaGetDurableExecutionResponse)

    async def get_durable_execution_history(
        self,
        request: LambdaGetDurableExecutionHistoryRequest,
    ) -> LambdaGetDurableExecutionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_durable_execution_history, request, LambdaGetDurableExecutionHistoryResponse)

    async def get_durable_execution_history_paginated(
        self,
        request: LambdaGetDurableExecutionHistoryRequest,
    ) -> list[LambdaGetDurableExecutionHistoryResponse]:
        return await self._paginate('get_durable_execution_history', request, LambdaGetDurableExecutionHistoryResponse)

    async def get_durable_execution_state(
        self,
        request: LambdaGetDurableExecutionStateRequest,
    ) -> LambdaGetDurableExecutionStateResponse:
        client = self._require_client()
        return await self._execute(client.get_durable_execution_state, request, LambdaGetDurableExecutionStateResponse)

    async def get_durable_execution_state_paginated(
        self,
        request: LambdaGetDurableExecutionStateRequest,
    ) -> list[LambdaGetDurableExecutionStateResponse]:
        return await self._paginate('get_durable_execution_state', request, LambdaGetDurableExecutionStateResponse)

    async def get_event_source_mapping(
        self,
        request: LambdaGetEventSourceMappingRequest,
    ) -> LambdaGetEventSourceMappingResponse:
        client = self._require_client()
        return await self._execute(client.get_event_source_mapping, request, LambdaGetEventSourceMappingResponse)

    async def get_function_code_signing_config(
        self,
        request: LambdaGetFunctionCodeSigningConfigRequest,
    ) -> LambdaGetFunctionCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_function_code_signing_config, request, LambdaGetFunctionCodeSigningConfigResponse)

    async def get_function_concurrency(
        self,
        request: LambdaGetFunctionConcurrencyRequest,
    ) -> LambdaGetFunctionConcurrencyResponse:
        client = self._require_client()
        return await self._execute(client.get_function_concurrency, request, LambdaGetFunctionConcurrencyResponse)

    async def get_function_event_invoke_config(
        self,
        request: LambdaGetFunctionEventInvokeConfigRequest,
    ) -> LambdaGetFunctionEventInvokeConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_function_event_invoke_config, request, LambdaGetFunctionEventInvokeConfigResponse)

    async def get_function_recursion_config(
        self,
        request: LambdaGetFunctionRecursionConfigRequest,
    ) -> LambdaGetFunctionRecursionConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_function_recursion_config, request, LambdaGetFunctionRecursionConfigResponse)

    async def get_function_scaling_config(
        self,
        request: LambdaGetFunctionScalingConfigRequest,
    ) -> LambdaGetFunctionScalingConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_function_scaling_config, request, LambdaGetFunctionScalingConfigResponse)

    async def get_function_url_config(
        self,
        request: LambdaGetFunctionUrlConfigRequest,
    ) -> LambdaGetFunctionUrlConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_function_url_config, request, LambdaGetFunctionUrlConfigResponse)

    async def get_layer_version(
        self,
        request: LambdaGetLayerVersionRequest,
    ) -> LambdaGetLayerVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_layer_version, request, LambdaGetLayerVersionResponse)

    async def get_layer_version_by_arn(
        self,
        request: LambdaGetLayerVersionByArnRequest,
    ) -> LambdaGetLayerVersionByArnResponse:
        client = self._require_client()
        return await self._execute(client.get_layer_version_by_arn, request, LambdaGetLayerVersionByArnResponse)

    async def get_layer_version_policy(
        self,
        request: LambdaGetLayerVersionPolicyRequest,
    ) -> LambdaGetLayerVersionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_layer_version_policy, request, LambdaGetLayerVersionPolicyResponse)

    async def get_policy(
        self,
        request: LambdaGetPolicyRequest,
    ) -> LambdaGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_policy, request, LambdaGetPolicyResponse)

    async def get_provisioned_concurrency_config(
        self,
        request: LambdaGetProvisionedConcurrencyConfigRequest,
    ) -> LambdaGetProvisionedConcurrencyConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_provisioned_concurrency_config, request, LambdaGetProvisionedConcurrencyConfigResponse)

    async def get_resource_policy(
        self,
        request: LambdaGetResourcePolicyRequest,
    ) -> LambdaGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, LambdaGetResourcePolicyResponse)

    async def get_runtime_management_config(
        self,
        request: LambdaGetRuntimeManagementConfigRequest,
    ) -> LambdaGetRuntimeManagementConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_runtime_management_config, request, LambdaGetRuntimeManagementConfigResponse)

    async def invoke_async(
        self,
        request: LambdaInvokeAsyncRequest,
    ) -> LambdaInvokeAsyncResponse:
        client = self._require_client()
        return await self._execute(client.invoke_async, request, LambdaInvokeAsyncResponse)

    async def invoke_with_response_stream(
        self,
        request: LambdaInvokeWithResponseStreamRequest,
    ) -> LambdaInvokeWithResponseStreamResponse:
        client = self._require_client()
        return await self._execute(client.invoke_with_response_stream, request, LambdaInvokeWithResponseStreamResponse)

    async def list_capacity_providers(
        self,
        request: LambdaListCapacityProvidersRequest | None = None,
    ) -> LambdaListCapacityProvidersResponse:
        client = self._require_client()
        return await self._execute(client.list_capacity_providers, request, LambdaListCapacityProvidersResponse)

    async def list_capacity_providers_paginated(
        self,
        request: LambdaListCapacityProvidersRequest | None = None,
    ) -> list[LambdaListCapacityProvidersResponse]:
        return await self._paginate('list_capacity_providers', request, LambdaListCapacityProvidersResponse)

    async def list_code_signing_configs(
        self,
        request: LambdaListCodeSigningConfigsRequest | None = None,
    ) -> LambdaListCodeSigningConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_code_signing_configs, request, LambdaListCodeSigningConfigsResponse)

    async def list_code_signing_configs_paginated(
        self,
        request: LambdaListCodeSigningConfigsRequest | None = None,
    ) -> list[LambdaListCodeSigningConfigsResponse]:
        return await self._paginate('list_code_signing_configs', request, LambdaListCodeSigningConfigsResponse)

    async def list_durable_executions_by_function(
        self,
        request: LambdaListDurableExecutionsByFunctionRequest,
    ) -> LambdaListDurableExecutionsByFunctionResponse:
        client = self._require_client()
        return await self._execute(client.list_durable_executions_by_function, request, LambdaListDurableExecutionsByFunctionResponse)

    async def list_durable_executions_by_function_paginated(
        self,
        request: LambdaListDurableExecutionsByFunctionRequest,
    ) -> list[LambdaListDurableExecutionsByFunctionResponse]:
        return await self._paginate('list_durable_executions_by_function', request, LambdaListDurableExecutionsByFunctionResponse)

    async def list_function_event_invoke_configs(
        self,
        request: LambdaListFunctionEventInvokeConfigsRequest,
    ) -> LambdaListFunctionEventInvokeConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_function_event_invoke_configs, request, LambdaListFunctionEventInvokeConfigsResponse)

    async def list_function_event_invoke_configs_paginated(
        self,
        request: LambdaListFunctionEventInvokeConfigsRequest,
    ) -> list[LambdaListFunctionEventInvokeConfigsResponse]:
        return await self._paginate('list_function_event_invoke_configs', request, LambdaListFunctionEventInvokeConfigsResponse)

    async def list_function_url_configs(
        self,
        request: LambdaListFunctionUrlConfigsRequest,
    ) -> LambdaListFunctionUrlConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_function_url_configs, request, LambdaListFunctionUrlConfigsResponse)

    async def list_function_url_configs_paginated(
        self,
        request: LambdaListFunctionUrlConfigsRequest,
    ) -> list[LambdaListFunctionUrlConfigsResponse]:
        return await self._paginate('list_function_url_configs', request, LambdaListFunctionUrlConfigsResponse)

    async def list_function_versions_by_capacity_provider(
        self,
        request: LambdaListFunctionVersionsByCapacityProviderRequest,
    ) -> LambdaListFunctionVersionsByCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.list_function_versions_by_capacity_provider, request, LambdaListFunctionVersionsByCapacityProviderResponse)

    async def list_function_versions_by_capacity_provider_paginated(
        self,
        request: LambdaListFunctionVersionsByCapacityProviderRequest,
    ) -> list[LambdaListFunctionVersionsByCapacityProviderResponse]:
        return await self._paginate('list_function_versions_by_capacity_provider', request, LambdaListFunctionVersionsByCapacityProviderResponse)

    async def list_functions_by_code_signing_config(
        self,
        request: LambdaListFunctionsByCodeSigningConfigRequest,
    ) -> LambdaListFunctionsByCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.list_functions_by_code_signing_config, request, LambdaListFunctionsByCodeSigningConfigResponse)

    async def list_functions_by_code_signing_config_paginated(
        self,
        request: LambdaListFunctionsByCodeSigningConfigRequest,
    ) -> list[LambdaListFunctionsByCodeSigningConfigResponse]:
        return await self._paginate('list_functions_by_code_signing_config', request, LambdaListFunctionsByCodeSigningConfigResponse)

    async def list_layer_versions(
        self,
        request: LambdaListLayerVersionsRequest,
    ) -> LambdaListLayerVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_layer_versions, request, LambdaListLayerVersionsResponse)

    async def list_layer_versions_paginated(
        self,
        request: LambdaListLayerVersionsRequest,
    ) -> list[LambdaListLayerVersionsResponse]:
        return await self._paginate('list_layer_versions', request, LambdaListLayerVersionsResponse)

    async def list_provisioned_concurrency_configs(
        self,
        request: LambdaListProvisionedConcurrencyConfigsRequest,
    ) -> LambdaListProvisionedConcurrencyConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioned_concurrency_configs, request, LambdaListProvisionedConcurrencyConfigsResponse)

    async def list_provisioned_concurrency_configs_paginated(
        self,
        request: LambdaListProvisionedConcurrencyConfigsRequest,
    ) -> list[LambdaListProvisionedConcurrencyConfigsResponse]:
        return await self._paginate('list_provisioned_concurrency_configs', request, LambdaListProvisionedConcurrencyConfigsResponse)

    async def pause_durable_execution(
        self,
        request: LambdaPauseDurableExecutionRequest,
    ) -> LambdaPauseDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.pause_durable_execution, request, LambdaPauseDurableExecutionResponse)

    async def publish_layer_version(
        self,
        request: LambdaPublishLayerVersionRequest,
    ) -> LambdaPublishLayerVersionResponse:
        client = self._require_client()
        return await self._execute(client.publish_layer_version, request, LambdaPublishLayerVersionResponse)

    async def put_function_code_signing_config(
        self,
        request: LambdaPutFunctionCodeSigningConfigRequest,
    ) -> LambdaPutFunctionCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_function_code_signing_config, request, LambdaPutFunctionCodeSigningConfigResponse)

    async def put_function_concurrency(
        self,
        request: LambdaPutFunctionConcurrencyRequest,
    ) -> LambdaPutFunctionConcurrencyResponse:
        client = self._require_client()
        return await self._execute(client.put_function_concurrency, request, LambdaPutFunctionConcurrencyResponse)

    async def put_function_event_invoke_config(
        self,
        request: LambdaPutFunctionEventInvokeConfigRequest,
    ) -> LambdaPutFunctionEventInvokeConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_function_event_invoke_config, request, LambdaPutFunctionEventInvokeConfigResponse)

    async def put_function_recursion_config(
        self,
        request: LambdaPutFunctionRecursionConfigRequest,
    ) -> LambdaPutFunctionRecursionConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_function_recursion_config, request, LambdaPutFunctionRecursionConfigResponse)

    async def put_function_scaling_config(
        self,
        request: LambdaPutFunctionScalingConfigRequest,
    ) -> LambdaPutFunctionScalingConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_function_scaling_config, request, LambdaPutFunctionScalingConfigResponse)

    async def put_provisioned_concurrency_config(
        self,
        request: LambdaPutProvisionedConcurrencyConfigRequest,
    ) -> LambdaPutProvisionedConcurrencyConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_provisioned_concurrency_config, request, LambdaPutProvisionedConcurrencyConfigResponse)

    async def put_resource_policy(
        self,
        request: LambdaPutResourcePolicyRequest,
    ) -> LambdaPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, LambdaPutResourcePolicyResponse)

    async def put_runtime_management_config(
        self,
        request: LambdaPutRuntimeManagementConfigRequest,
    ) -> LambdaPutRuntimeManagementConfigResponse:
        client = self._require_client()
        return await self._execute(client.put_runtime_management_config, request, LambdaPutRuntimeManagementConfigResponse)

    async def remove_layer_version_permission(
        self,
        request: LambdaRemoveLayerVersionPermissionRequest,
    ) -> LambdaRemoveLayerVersionPermissionResponse:
        client = self._require_client()
        return await self._execute(client.remove_layer_version_permission, request, LambdaRemoveLayerVersionPermissionResponse)

    async def remove_permission(
        self,
        request: LambdaRemovePermissionRequest,
    ) -> LambdaRemovePermissionResponse:
        client = self._require_client()
        return await self._execute(client.remove_permission, request, LambdaRemovePermissionResponse)

    async def resume_durable_execution(
        self,
        request: LambdaResumeDurableExecutionRequest,
    ) -> LambdaResumeDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.resume_durable_execution, request, LambdaResumeDurableExecutionResponse)

    async def send_durable_execution_callback_failure(
        self,
        request: LambdaSendDurableExecutionCallbackFailureRequest,
    ) -> LambdaSendDurableExecutionCallbackFailureResponse:
        client = self._require_client()
        return await self._execute(client.send_durable_execution_callback_failure, request, LambdaSendDurableExecutionCallbackFailureResponse)

    async def send_durable_execution_callback_heartbeat(
        self,
        request: LambdaSendDurableExecutionCallbackHeartbeatRequest,
    ) -> LambdaSendDurableExecutionCallbackHeartbeatResponse:
        client = self._require_client()
        return await self._execute(client.send_durable_execution_callback_heartbeat, request, LambdaSendDurableExecutionCallbackHeartbeatResponse)

    async def send_durable_execution_callback_success(
        self,
        request: LambdaSendDurableExecutionCallbackSuccessRequest,
    ) -> LambdaSendDurableExecutionCallbackSuccessResponse:
        client = self._require_client()
        return await self._execute(client.send_durable_execution_callback_success, request, LambdaSendDurableExecutionCallbackSuccessResponse)

    async def stop_durable_execution(
        self,
        request: LambdaStopDurableExecutionRequest,
    ) -> LambdaStopDurableExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_durable_execution, request, LambdaStopDurableExecutionResponse)

    async def update_capacity_provider(
        self,
        request: LambdaUpdateCapacityProviderRequest,
    ) -> LambdaUpdateCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_capacity_provider, request, LambdaUpdateCapacityProviderResponse)

    async def update_code_signing_config(
        self,
        request: LambdaUpdateCodeSigningConfigRequest,
    ) -> LambdaUpdateCodeSigningConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_code_signing_config, request, LambdaUpdateCodeSigningConfigResponse)

    async def update_event_source_mapping(
        self,
        request: LambdaUpdateEventSourceMappingRequest,
    ) -> LambdaUpdateEventSourceMappingResponse:
        client = self._require_client()
        return await self._execute(client.update_event_source_mapping, request, LambdaUpdateEventSourceMappingResponse)

    async def update_function_event_invoke_config(
        self,
        request: LambdaUpdateFunctionEventInvokeConfigRequest,
    ) -> LambdaUpdateFunctionEventInvokeConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_function_event_invoke_config, request, LambdaUpdateFunctionEventInvokeConfigResponse)

    async def update_function_url_config(
        self,
        request: LambdaUpdateFunctionUrlConfigRequest,
    ) -> LambdaUpdateFunctionUrlConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_function_url_config, request, LambdaUpdateFunctionUrlConfigResponse)

