from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_studio import EMRStudio


class EMRDescribeStudioResponse(BaseModel):
    Studio: EMRStudio | None = None
    ResponseMetadata: dict[str, Any] | None = None
