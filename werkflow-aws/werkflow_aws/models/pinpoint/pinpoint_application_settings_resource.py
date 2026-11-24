from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_application_settings_journey_limits import PinpointApplicationSettingsJourneyLimits
from .pinpoint_campaign_hook import PinpointCampaignHook
from .pinpoint_campaign_limits import PinpointCampaignLimits
from .pinpoint_quiet_time import PinpointQuietTime


class PinpointApplicationSettingsResource(BaseModel):
    ApplicationId: StrictStr | None = None
    CampaignHook: PinpointCampaignHook | None = None
    LastModifiedDate: StrictStr | None = None
    Limits: PinpointCampaignLimits | None = None
    QuietTime: PinpointQuietTime | None = None
    JourneyLimits: PinpointApplicationSettingsJourneyLimits | None = None
