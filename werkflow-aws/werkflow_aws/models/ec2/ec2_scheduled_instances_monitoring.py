from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2ScheduledInstancesMonitoring(BaseModel):
    Enabled: StrictBool | None = None
