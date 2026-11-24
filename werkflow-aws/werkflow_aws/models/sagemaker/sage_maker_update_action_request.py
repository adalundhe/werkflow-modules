from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerUpdateActionRequest(BaseModel):
    ActionName: StrictStr
    Description: StrictStr | None = None
    Status: Literal['Unknown', 'InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped'] | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    PropertiesToRemove: list[StrictStr] | None = None
