from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_code_signing_config import LambdaCodeSigningConfig


class LambdaListCodeSigningConfigsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    CodeSigningConfigs: list[LambdaCodeSigningConfig] | None = None
    ResponseMetadata: dict[str, Any] | None = None
