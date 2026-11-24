from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LambdaGetRuntimeManagementConfigResponse(BaseModel):
    UpdateRuntimeOn: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    RuntimeVersionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
