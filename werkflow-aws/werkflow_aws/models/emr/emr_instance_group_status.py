from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_group_state_change_reason import EMRInstanceGroupStateChangeReason
from .emr_instance_group_timeline import EMRInstanceGroupTimeline


class EMRInstanceGroupStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRInstanceGroupStateChangeReason | None = None
    Timeline: EMRInstanceGroupTimeline | None = None
