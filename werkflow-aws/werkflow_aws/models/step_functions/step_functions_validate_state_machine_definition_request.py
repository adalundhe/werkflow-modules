from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsValidateStateMachineDefinitionRequest(BaseModel):
    definition: StrictStr
    type: Literal['STANDARD', 'EXPRESS'] | None = None
    severity: Literal['ERROR', 'WARNING'] | None = None
    maxResults: StrictInt | None = None
