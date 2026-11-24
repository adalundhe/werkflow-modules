from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class StepFunctionsCreateStateMachineAliasResponse(BaseModel):
    stateMachineAliasArn: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
