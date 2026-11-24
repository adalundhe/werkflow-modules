from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_instance_refresh_progress_details import AutoScalingInstanceRefreshProgressDetails


class AutoScalingRollbackDetails(BaseModel):
    RollbackReason: StrictStr | None = None
    RollbackStartTime: datetime.datetime | StrictStr | None = None
    PercentageCompleteOnRollback: StrictInt | None = None
    InstancesToUpdateOnRollback: StrictInt | None = None
    ProgressDetailsOnRollback: AutoScalingInstanceRefreshProgressDetails | None = None
