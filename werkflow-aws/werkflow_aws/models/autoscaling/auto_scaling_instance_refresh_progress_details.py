from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_instance_refresh_live_pool_progress import AutoScalingInstanceRefreshLivePoolProgress
from .auto_scaling_instance_refresh_warm_pool_progress import AutoScalingInstanceRefreshWarmPoolProgress


class AutoScalingInstanceRefreshProgressDetails(BaseModel):
    LivePoolProgress: AutoScalingInstanceRefreshLivePoolProgress | None = None
    WarmPoolProgress: AutoScalingInstanceRefreshWarmPoolProgress | None = None
