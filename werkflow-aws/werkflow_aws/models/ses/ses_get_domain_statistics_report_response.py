from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_daily_volume import SESDailyVolume
from .ses_overall_volume import SESOverallVolume


class SESGetDomainStatisticsReportResponse(BaseModel):
    OverallVolume: SESOverallVolume | None = None
    DailyVolumes: list[SESDailyVolume] | None = None
    ResponseMetadata: dict[str, Any] | None = None
