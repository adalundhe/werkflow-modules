from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lambda_code_signing_config import LambdaCodeSigningConfig


class LambdaUpdateCodeSigningConfigResponse(BaseModel):
    CodeSigningConfig: LambdaCodeSigningConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
