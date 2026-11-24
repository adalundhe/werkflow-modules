from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsRoutingConfigurationListItem(BaseModel):
    stateMachineVersionArn: StrictStr | None = None
    weight: StrictInt | None = None
