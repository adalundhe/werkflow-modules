from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_instance_fleet import EMRInstanceFleet


class EMRListInstanceFleetsResponse(BaseModel):
    InstanceFleets: list[EMRInstanceFleet] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
