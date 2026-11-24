from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_mobile_sdk_release import WAFv2MobileSdkRelease


class WAFv2GetMobileSdkReleaseResponse(BaseModel):
    MobileSdkRelease: WAFv2MobileSdkRelease | None = None
    ResponseMetadata: dict[str, Any] | None = None
