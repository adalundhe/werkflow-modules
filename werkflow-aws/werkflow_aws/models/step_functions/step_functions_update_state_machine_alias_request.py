from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_routing_configuration_list_item import StepFunctionsRoutingConfigurationListItem


class StepFunctionsUpdateStateMachineAliasRequest(BaseModel):
    stateMachineAliasArn: StrictStr
    description: StrictStr | None = None
    routingConfiguration: list[StepFunctionsRoutingConfigurationListItem] | None = None
