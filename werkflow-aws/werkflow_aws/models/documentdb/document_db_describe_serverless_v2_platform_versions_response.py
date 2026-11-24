from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_serverless_v2_platform_version_info import DocumentDBServerlessV2PlatformVersionInfo


class DocumentDBDescribeServerlessV2PlatformVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ServerlessV2PlatformVersions: list[DocumentDBServerlessV2PlatformVersionInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
