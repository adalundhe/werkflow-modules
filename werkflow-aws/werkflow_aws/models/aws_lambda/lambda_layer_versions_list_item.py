from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_architecture import LambdaArchitecture
from .lambda_runtime import LambdaRuntime


class LambdaLayerVersionsListItem(BaseModel):
    LayerVersionArn: StrictStr | None = None
    Version: StrictInt | None = None
    Description: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    CompatibleArchitectures: list[LambdaArchitecture] | None = None
    CompatibleRuntimes: list[LambdaRuntime] | None = None
    LicenseInfo: StrictStr | None = None
