from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StepFunctionsGetActivityTaskResponse(BaseModel):
    taskToken: StrictStr | None = None
    input: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
