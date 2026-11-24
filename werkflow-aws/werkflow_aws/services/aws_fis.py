from werkflow_aws.models.fis import (
    FISCreateExperimentTemplateRequest,
    FISCreateExperimentTemplateResponse,
    FISCreateTargetAccountConfigurationRequest,
    FISCreateTargetAccountConfigurationResponse,
    FISDeleteExperimentTemplateRequest,
    FISDeleteExperimentTemplateResponse,
    FISDeleteTargetAccountConfigurationRequest,
    FISDeleteTargetAccountConfigurationResponse,
    FISGetActionRequest,
    FISGetActionResponse,
    FISGetExperimentRequest,
    FISGetExperimentResponse,
    FISGetExperimentTargetAccountConfigurationRequest,
    FISGetExperimentTargetAccountConfigurationResponse,
    FISGetExperimentTemplateRequest,
    FISGetExperimentTemplateResponse,
    FISGetSafetyLeverRequest,
    FISGetSafetyLeverResponse,
    FISGetTargetAccountConfigurationRequest,
    FISGetTargetAccountConfigurationResponse,
    FISGetTargetResourceTypeRequest,
    FISGetTargetResourceTypeResponse,
    FISListActionsRequest,
    FISListActionsResponse,
    FISListExperimentResolvedTargetsRequest,
    FISListExperimentResolvedTargetsResponse,
    FISListExperimentTargetAccountConfigurationsRequest,
    FISListExperimentTargetAccountConfigurationsResponse,
    FISListExperimentTemplatesRequest,
    FISListExperimentTemplatesResponse,
    FISListExperimentsRequest,
    FISListExperimentsResponse,
    FISListTagsForResourceRequest,
    FISListTagsForResourceResponse,
    FISListTargetAccountConfigurationsRequest,
    FISListTargetAccountConfigurationsResponse,
    FISListTargetResourceTypesRequest,
    FISListTargetResourceTypesResponse,
    FISStartExperimentRequest,
    FISStartExperimentResponse,
    FISStopExperimentRequest,
    FISStopExperimentResponse,
    FISTagResourceRequest,
    FISTagResourceResponse,
    FISUntagResourceRequest,
    FISUntagResourceResponse,
    FISUpdateExperimentTemplateRequest,
    FISUpdateExperimentTemplateResponse,
    FISUpdateSafetyLeverStateRequest,
    FISUpdateSafetyLeverStateResponse,
    FISUpdateTargetAccountConfigurationRequest,
    FISUpdateTargetAccountConfigurationResponse,
)
from werkflow_aws.types.fis_client import FISClient
from .base import AWSBaseService


class AWSFIS(AWSBaseService[FISClient]):
    service_name = 'fis'
    boto3_service_name = 'fis'

    def __init__(self) -> None:
        super().__init__(service_name='fis', boto3_service_name='fis')

    async def create_experiment_template(
        self,
        request: FISCreateExperimentTemplateRequest,
    ) -> FISCreateExperimentTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_experiment_template, request, FISCreateExperimentTemplateResponse)

    async def create_target_account_configuration(
        self,
        request: FISCreateTargetAccountConfigurationRequest,
    ) -> FISCreateTargetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_target_account_configuration, request, FISCreateTargetAccountConfigurationResponse)

    async def delete_experiment_template(
        self,
        request: FISDeleteExperimentTemplateRequest,
    ) -> FISDeleteExperimentTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_experiment_template, request, FISDeleteExperimentTemplateResponse)

    async def delete_target_account_configuration(
        self,
        request: FISDeleteTargetAccountConfigurationRequest,
    ) -> FISDeleteTargetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_target_account_configuration, request, FISDeleteTargetAccountConfigurationResponse)

    async def get_action(
        self,
        request: FISGetActionRequest,
    ) -> FISGetActionResponse:
        client = self._require_client()
        return await self._execute(client.get_action, request, FISGetActionResponse)

    async def get_experiment(
        self,
        request: FISGetExperimentRequest,
    ) -> FISGetExperimentResponse:
        client = self._require_client()
        return await self._execute(client.get_experiment, request, FISGetExperimentResponse)

    async def get_experiment_target_account_configuration(
        self,
        request: FISGetExperimentTargetAccountConfigurationRequest,
    ) -> FISGetExperimentTargetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_experiment_target_account_configuration, request, FISGetExperimentTargetAccountConfigurationResponse)

    async def get_experiment_template(
        self,
        request: FISGetExperimentTemplateRequest,
    ) -> FISGetExperimentTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_experiment_template, request, FISGetExperimentTemplateResponse)

    async def get_safety_lever(
        self,
        request: FISGetSafetyLeverRequest,
    ) -> FISGetSafetyLeverResponse:
        client = self._require_client()
        return await self._execute(client.get_safety_lever, request, FISGetSafetyLeverResponse)

    async def get_target_account_configuration(
        self,
        request: FISGetTargetAccountConfigurationRequest,
    ) -> FISGetTargetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_target_account_configuration, request, FISGetTargetAccountConfigurationResponse)

    async def get_target_resource_type(
        self,
        request: FISGetTargetResourceTypeRequest,
    ) -> FISGetTargetResourceTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_target_resource_type, request, FISGetTargetResourceTypeResponse)

    async def list_actions(
        self,
        request: FISListActionsRequest | None = None,
    ) -> FISListActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_actions, request, FISListActionsResponse)

    async def list_actions_paginated(
        self,
        request: FISListActionsRequest | None = None,
    ) -> list[FISListActionsResponse]:
        return await self._paginate('list_actions', request, FISListActionsResponse)

    async def list_experiment_resolved_targets(
        self,
        request: FISListExperimentResolvedTargetsRequest,
    ) -> FISListExperimentResolvedTargetsResponse:
        client = self._require_client()
        return await self._execute(client.list_experiment_resolved_targets, request, FISListExperimentResolvedTargetsResponse)

    async def list_experiment_resolved_targets_paginated(
        self,
        request: FISListExperimentResolvedTargetsRequest,
    ) -> list[FISListExperimentResolvedTargetsResponse]:
        return await self._paginate('list_experiment_resolved_targets', request, FISListExperimentResolvedTargetsResponse)

    async def list_experiment_target_account_configurations(
        self,
        request: FISListExperimentTargetAccountConfigurationsRequest,
    ) -> FISListExperimentTargetAccountConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_experiment_target_account_configurations, request, FISListExperimentTargetAccountConfigurationsResponse)

    async def list_experiment_templates(
        self,
        request: FISListExperimentTemplatesRequest | None = None,
    ) -> FISListExperimentTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_experiment_templates, request, FISListExperimentTemplatesResponse)

    async def list_experiment_templates_paginated(
        self,
        request: FISListExperimentTemplatesRequest | None = None,
    ) -> list[FISListExperimentTemplatesResponse]:
        return await self._paginate('list_experiment_templates', request, FISListExperimentTemplatesResponse)

    async def list_experiments(
        self,
        request: FISListExperimentsRequest | None = None,
    ) -> FISListExperimentsResponse:
        client = self._require_client()
        return await self._execute(client.list_experiments, request, FISListExperimentsResponse)

    async def list_experiments_paginated(
        self,
        request: FISListExperimentsRequest | None = None,
    ) -> list[FISListExperimentsResponse]:
        return await self._paginate('list_experiments', request, FISListExperimentsResponse)

    async def list_tags_for_resource(
        self,
        request: FISListTagsForResourceRequest,
    ) -> FISListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, FISListTagsForResourceResponse)

    async def list_target_account_configurations(
        self,
        request: FISListTargetAccountConfigurationsRequest,
    ) -> FISListTargetAccountConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_target_account_configurations, request, FISListTargetAccountConfigurationsResponse)

    async def list_target_account_configurations_paginated(
        self,
        request: FISListTargetAccountConfigurationsRequest,
    ) -> list[FISListTargetAccountConfigurationsResponse]:
        return await self._paginate('list_target_account_configurations', request, FISListTargetAccountConfigurationsResponse)

    async def list_target_resource_types(
        self,
        request: FISListTargetResourceTypesRequest | None = None,
    ) -> FISListTargetResourceTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_target_resource_types, request, FISListTargetResourceTypesResponse)

    async def list_target_resource_types_paginated(
        self,
        request: FISListTargetResourceTypesRequest | None = None,
    ) -> list[FISListTargetResourceTypesResponse]:
        return await self._paginate('list_target_resource_types', request, FISListTargetResourceTypesResponse)

    async def start_experiment(
        self,
        request: FISStartExperimentRequest,
    ) -> FISStartExperimentResponse:
        client = self._require_client()
        return await self._execute(client.start_experiment, request, FISStartExperimentResponse)

    async def stop_experiment(
        self,
        request: FISStopExperimentRequest,
    ) -> FISStopExperimentResponse:
        client = self._require_client()
        return await self._execute(client.stop_experiment, request, FISStopExperimentResponse)

    async def tag_resource(
        self,
        request: FISTagResourceRequest,
    ) -> FISTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, FISTagResourceResponse)

    async def untag_resource(
        self,
        request: FISUntagResourceRequest,
    ) -> FISUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, FISUntagResourceResponse)

    async def update_experiment_template(
        self,
        request: FISUpdateExperimentTemplateRequest,
    ) -> FISUpdateExperimentTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_experiment_template, request, FISUpdateExperimentTemplateResponse)

    async def update_safety_lever_state(
        self,
        request: FISUpdateSafetyLeverStateRequest,
    ) -> FISUpdateSafetyLeverStateResponse:
        client = self._require_client()
        return await self._execute(client.update_safety_lever_state, request, FISUpdateSafetyLeverStateResponse)

    async def update_target_account_configuration(
        self,
        request: FISUpdateTargetAccountConfigurationRequest,
    ) -> FISUpdateTargetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_target_account_configuration, request, FISUpdateTargetAccountConfigurationResponse)
