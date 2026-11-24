from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_activity import PinpointActivity
from .pinpoint_closed_days import PinpointClosedDays
from .pinpoint_journey_channel_settings import PinpointJourneyChannelSettings
from .pinpoint_journey_limits import PinpointJourneyLimits
from .pinpoint_journey_schedule import PinpointJourneySchedule
from .pinpoint_open_hours import PinpointOpenHours
from .pinpoint_quiet_time import PinpointQuietTime
from .pinpoint_start_condition import PinpointStartCondition


class PinpointWriteJourneyRequest(BaseModel):
    Name: StrictStr
    Activities: dict[StrictStr, PinpointActivity] | None = None
    CreationDate: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    Limits: PinpointJourneyLimits | None = None
    LocalTime: StrictBool | None = None
    QuietTime: PinpointQuietTime | None = None
    RefreshFrequency: StrictStr | None = None
    Schedule: PinpointJourneySchedule | None = None
    StartActivity: StrictStr | None = None
    StartCondition: PinpointStartCondition | None = None
    State: Literal['DRAFT', 'ACTIVE', 'COMPLETED', 'CANCELLED', 'CLOSED', 'PAUSED'] | None = None
    WaitForQuietTime: StrictBool | None = None
    RefreshOnSegmentUpdate: StrictBool | None = None
    JourneyChannelSettings: PinpointJourneyChannelSettings | None = None
    SendingSchedule: StrictBool | None = None
    OpenHours: PinpointOpenHours | None = None
    ClosedDays: PinpointClosedDays | None = None
    TimezoneEstimationMethods: list[Literal['PHONE_NUMBER', 'POSTAL_CODE']] | None = None
