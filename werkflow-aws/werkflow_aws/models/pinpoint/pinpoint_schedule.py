from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_campaign_event_filter import PinpointCampaignEventFilter
from .pinpoint_quiet_time import PinpointQuietTime


class PinpointSchedule(BaseModel):
    EndTime: StrictStr | None = None
    EventFilter: PinpointCampaignEventFilter | None = None
    Frequency: StrictStr | None = None
    IsLocalTime: StrictBool | None = None
    QuietTime: PinpointQuietTime | None = None
    StartTime: StrictStr | None = None
    Timezone: StrictStr | None = None
