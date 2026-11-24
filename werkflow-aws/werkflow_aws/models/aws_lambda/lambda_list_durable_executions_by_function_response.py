from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_execution import LambdaExecution


class LambdaListDurableExecutionsByFunctionResponse(BaseModel):
    DurableExecutions: list[LambdaExecution] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
