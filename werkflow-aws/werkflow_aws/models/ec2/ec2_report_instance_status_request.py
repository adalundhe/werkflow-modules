from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReportInstanceStatusRequest(BaseModel):
    Instances: list[StrictStr]
    Status: Literal['ok', 'impaired']
    ReasonCodes: list[Literal['instance-stuck-in-state', 'unresponsive', 'not-accepting-credentials', 'password-not-available', 'performance-network', 'performance-instance-store', 'performance-ebs-volume', 'performance-other', 'other']]
    DryRun: StrictBool | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
