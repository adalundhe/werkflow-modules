from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaLayerVersionsListItemModel(BaseModel):
    LayerVersionArn: StrictStr | None = None
    Version: StrictInt | None = None
    Description: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    CompatibleArchitectures: list[StrictStr] | None = None
    CompatibleRuntimes: list[StrictStr] | None = None
    LicenseInfo: StrictStr | None = None
