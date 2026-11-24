from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_cancel_steps_info import EMRCancelStepsInfo


class EMRCancelStepsResponse(BaseModel):
    CancelStepsInfoList: list[EMRCancelStepsInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
