from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_fleet_state_change_reason import EMRInstanceFleetStateChangeReason
from .emr_instance_fleet_timeline import EMRInstanceFleetTimeline


class EMRInstanceFleetStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRInstanceFleetStateChangeReason | None = None
    Timeline: EMRInstanceFleetTimeline | None = None
