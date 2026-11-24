from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_serverless_v2_platform_version_info import RDSServerlessV2PlatformVersionInfo


class RDSDescribeServerlessV2PlatformVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ServerlessV2PlatformVersions: list[RDSServerlessV2PlatformVersionInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
