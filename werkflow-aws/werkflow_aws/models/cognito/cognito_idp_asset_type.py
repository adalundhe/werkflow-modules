from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CognitoIDPAssetType(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Category: StrictStr | None = None
    ColorMode: StrictStr | None = None
    Extension: StrictStr | None = None
    Bytes: StrictBytes | Any | None = None
    ResourceId: StrictStr | None = None
