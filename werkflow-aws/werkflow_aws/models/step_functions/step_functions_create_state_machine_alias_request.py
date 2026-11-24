from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_routing_configuration_list_item import StepFunctionsRoutingConfigurationListItem


class StepFunctionsCreateStateMachineAliasRequest(BaseModel):
    name: StrictStr
    routingConfiguration: list[StepFunctionsRoutingConfigurationListItem]
    description: StrictStr | None = None
