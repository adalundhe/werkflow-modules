from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_bundle import LightsailBundle


class LightsailGetBundlesResponse(BaseModel):
    bundles: list[LightsailBundle] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
