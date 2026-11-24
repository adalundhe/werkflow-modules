from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LambdaListFunctionsByCodeSigningConfigResponse(BaseModel):
    NextMarker: StrictStr | None = None
    FunctionArns: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
