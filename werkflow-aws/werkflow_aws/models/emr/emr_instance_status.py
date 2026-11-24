from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_state_change_reason import EMRInstanceStateChangeReason
from .emr_instance_timeline import EMRInstanceTimeline


class EMRInstanceStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRInstanceStateChangeReason | None = None
    Timeline: EMRInstanceTimeline | None = None
