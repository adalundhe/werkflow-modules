from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_session_mapping_detail import EMRSessionMappingDetail


class EMRGetStudioSessionMappingResponse(BaseModel):
    SessionMapping: EMRSessionMappingDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
