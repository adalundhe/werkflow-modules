from __future__ import annotations
from pydantic import BaseModel
from .lambda_image_config import LambdaImageConfig
from .lambda_image_config_error import LambdaImageConfigError


class LambdaImageConfigResponse(BaseModel):
    ImageConfig: LambdaImageConfig | None = None
    Error: LambdaImageConfigError | None = None
