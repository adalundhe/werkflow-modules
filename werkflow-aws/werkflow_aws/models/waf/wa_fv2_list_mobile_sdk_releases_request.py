from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ListMobileSdkReleasesRequest(BaseModel):
    Platform: Literal['IOS', 'ANDROID']
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
