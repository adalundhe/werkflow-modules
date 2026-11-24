from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_studio_summary import EMRStudioSummary


class EMRListStudiosResponse(BaseModel):
    Studios: list[EMRStudioSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
