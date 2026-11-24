from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_serverless_v2_platform_version_info import NeptuneServerlessV2PlatformVersionInfo


class NeptuneDescribeServerlessV2PlatformVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ServerlessV2PlatformVersions: list[NeptuneServerlessV2PlatformVersionInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
