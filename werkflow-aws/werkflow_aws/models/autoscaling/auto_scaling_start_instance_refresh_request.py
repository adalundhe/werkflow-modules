from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .auto_scaling_desired_configuration import AutoScalingDesiredConfiguration
from .auto_scaling_refresh_preferences import AutoScalingRefreshPreferences


class AutoScalingStartInstanceRefreshRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    Strategy: Literal['Rolling', 'ReplaceRootVolume'] | None = None
    DesiredConfiguration: AutoScalingDesiredConfiguration | None = None
    Preferences: AutoScalingRefreshPreferences | None = None
