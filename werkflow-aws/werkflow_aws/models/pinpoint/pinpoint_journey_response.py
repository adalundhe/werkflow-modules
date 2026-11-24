from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_activity import PinpointActivity
from .pinpoint_closed_days import PinpointClosedDays
from .pinpoint_journey_channel_settings import PinpointJourneyChannelSettings
from .pinpoint_journey_limits import PinpointJourneyLimits
from .pinpoint_journey_schedule import PinpointJourneySchedule
from .pinpoint_open_hours import PinpointOpenHours
from .pinpoint_quiet_time import PinpointQuietTime
from .pinpoint_start_condition import PinpointStartCondition


class PinpointJourneyResponse(BaseModel):
    Activities: dict[StrictStr, PinpointActivity] | None = None
    ApplicationId: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Id: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    Limits: PinpointJourneyLimits | None = None
    LocalTime: StrictBool | None = None
    Name: StrictStr | None = None
    QuietTime: PinpointQuietTime | None = None
    RefreshFrequency: StrictStr | None = None
    Schedule: PinpointJourneySchedule | None = None
    StartActivity: StrictStr | None = None
    StartCondition: PinpointStartCondition | None = None
    State: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    WaitForQuietTime: StrictBool | None = None
    RefreshOnSegmentUpdate: StrictBool | None = None
    JourneyChannelSettings: PinpointJourneyChannelSettings | None = None
    SendingSchedule: StrictBool | None = None
    OpenHours: PinpointOpenHours | None = None
    ClosedDays: PinpointClosedDays | None = None
    TimezoneEstimationMethods: list[StrictStr] | None = None
