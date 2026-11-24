from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class StepFunctionsUpdateStateMachineResponse(BaseModel):
    updateDate: datetime.datetime | StrictStr | None = None
    revisionId: StrictStr | None = None
    stateMachineVersionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
