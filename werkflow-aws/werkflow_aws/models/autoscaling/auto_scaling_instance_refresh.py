from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_desired_configuration import AutoScalingDesiredConfiguration
from .auto_scaling_instance_refresh_progress_details import AutoScalingInstanceRefreshProgressDetails
from .auto_scaling_refresh_preferences import AutoScalingRefreshPreferences
from .auto_scaling_rollback_details import AutoScalingRollbackDetails


class AutoScalingInstanceRefresh(BaseModel):
    InstanceRefreshId: StrictStr | None = None
    AutoScalingGroupName: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    PercentageComplete: StrictInt | None = None
    InstancesToUpdate: StrictInt | None = None
    ProgressDetails: AutoScalingInstanceRefreshProgressDetails | None = None
    Preferences: AutoScalingRefreshPreferences | None = None
    DesiredConfiguration: AutoScalingDesiredConfiguration | None = None
    RollbackDetails: AutoScalingRollbackDetails | None = None
    Strategy: StrictStr | None = None
