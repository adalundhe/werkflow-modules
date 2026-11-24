from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .dev_ops_guru_start_time_range import DevOpsGuruStartTimeRange


class DevOpsGuruListInsightsAnyStatusFilter(BaseModel):
    Type: Literal['REACTIVE', 'PROACTIVE']
    StartTimeRange: DevOpsGuruStartTimeRange
