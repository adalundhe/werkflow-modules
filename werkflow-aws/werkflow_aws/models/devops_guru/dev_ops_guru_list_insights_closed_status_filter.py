from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .dev_ops_guru_end_time_range import DevOpsGuruEndTimeRange


class DevOpsGuruListInsightsClosedStatusFilter(BaseModel):
    Type: Literal['REACTIVE', 'PROACTIVE']
    EndTimeRange: DevOpsGuruEndTimeRange
