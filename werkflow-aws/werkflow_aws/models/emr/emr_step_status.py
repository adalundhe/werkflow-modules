from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_failure_details import EMRFailureDetails
from .emr_step_state_change_reason import EMRStepStateChangeReason
from .emr_step_timeline import EMRStepTimeline


class EMRStepStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRStepStateChangeReason | None = None
    FailureDetails: EMRFailureDetails | None = None
    Timeline: EMRStepTimeline | None = None
