from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .wa_fv2_bot_statistics import WAFv2BotStatistics
from .wa_fv2_filter_source import WAFv2FilterSource


class WAFv2PathStatistics(BaseModel):
    Source: WAFv2FilterSource | None = None
    Path: StrictStr | None = None
    RequestCount: StrictInt | None = None
    Percentage: StrictFloat | StrictInt | None = None
    TopBots: list[WAFv2BotStatistics] | None = None
