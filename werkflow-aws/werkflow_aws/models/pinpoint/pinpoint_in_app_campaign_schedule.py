from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_campaign_event_filter import PinpointCampaignEventFilter
from .pinpoint_quiet_time import PinpointQuietTime


class PinpointInAppCampaignSchedule(BaseModel):
    EndDate: StrictStr | None = None
    EventFilter: PinpointCampaignEventFilter | None = None
    QuietTime: PinpointQuietTime | None = None
