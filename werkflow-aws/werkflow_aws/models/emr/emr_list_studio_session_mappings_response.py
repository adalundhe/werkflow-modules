from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_session_mapping_summary import EMRSessionMappingSummary


class EMRListStudioSessionMappingsResponse(BaseModel):
    SessionMappings: list[EMRSessionMappingSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
