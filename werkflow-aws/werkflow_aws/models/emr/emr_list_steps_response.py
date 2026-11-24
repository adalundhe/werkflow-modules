from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_step_summary import EMRStepSummary


class EMRListStepsResponse(BaseModel):
    Steps: list[EMRStepSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
