from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .fis_experiment_action_state import FISExperimentActionState


class FISExperimentAction(BaseModel):
    actionId: StrictStr | None = None
    description: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    targets: dict[StrictStr, StrictStr] | None = None
    startAfter: list[StrictStr] | None = None
    state: FISExperimentActionState | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
