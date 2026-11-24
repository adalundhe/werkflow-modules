from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lambda_layer_version_content_input import LambdaLayerVersionContentInput


class LambdaPublishLayerVersionRequest(BaseModel):
    LayerName: StrictStr
    Content: LambdaLayerVersionContentInput
    Description: StrictStr | None = None
    CompatibleArchitectures: list[Literal['x86_64', 'arm64']] | None = None
    CompatibleRuntimes: list[StrictStr] | None = None
    LicenseInfo: StrictStr | None = None
