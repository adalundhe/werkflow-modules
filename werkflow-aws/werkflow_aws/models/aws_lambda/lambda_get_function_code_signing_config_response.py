from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionCodeSigningConfigResponse(BaseModel):
    CodeSigningConfigArn: StrictStr | None = None
    FunctionName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
