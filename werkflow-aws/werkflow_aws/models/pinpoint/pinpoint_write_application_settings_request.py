from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .pinpoint_application_settings_journey_limits import PinpointApplicationSettingsJourneyLimits
from .pinpoint_campaign_hook import PinpointCampaignHook
from .pinpoint_campaign_limits import PinpointCampaignLimits
from .pinpoint_quiet_time import PinpointQuietTime


class PinpointWriteApplicationSettingsRequest(BaseModel):
    CampaignHook: PinpointCampaignHook | None = None
    CloudWatchMetricsEnabled: StrictBool | None = None
    EventTaggingEnabled: StrictBool | None = None
    Limits: PinpointCampaignLimits | None = None
    QuietTime: PinpointQuietTime | None = None
    JourneyLimits: PinpointApplicationSettingsJourneyLimits | None = None
