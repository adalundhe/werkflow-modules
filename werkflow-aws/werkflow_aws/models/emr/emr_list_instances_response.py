from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_instance import EMRInstance


class EMRListInstancesResponse(BaseModel):
    Instances: list[EMRInstance] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
