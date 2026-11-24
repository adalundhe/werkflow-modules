from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .open_search_cloned_blue_green_scheduled_action import OpenSearchClonedBlueGreenScheduledAction
from .open_search_traffic_percents import OpenSearchTrafficPercents


class OpenSearchClonedBlueGreenUpgradeDetails(BaseModel):
    TrafficSplit: OpenSearchTrafficPercents | None = None
    ScheduledAction: OpenSearchClonedBlueGreenScheduledAction | None = None
    RetentionInHours: StrictInt | None = None
