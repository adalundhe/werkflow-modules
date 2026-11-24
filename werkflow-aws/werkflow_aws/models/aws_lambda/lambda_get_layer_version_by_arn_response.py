from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_layer_version_content_output import LambdaLayerVersionContentOutput


class LambdaGetLayerVersionByArnResponse(BaseModel):
    Content: LambdaLayerVersionContentOutput | None = None
    LayerArn: StrictStr | None = None
    LayerVersionArn: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    Version: StrictInt | None = None
    CompatibleArchitectures: list[StrictStr] | None = None
    CompatibleRuntimes: list[StrictStr] | None = None
    LicenseInfo: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
