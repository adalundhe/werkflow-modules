from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_routing_configuration_list_item import StepFunctionsRoutingConfigurationListItem


class StepFunctionsDescribeStateMachineAliasResponse(BaseModel):
    stateMachineAliasArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    routingConfiguration: list[StepFunctionsRoutingConfigurationListItem] | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    updateDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
