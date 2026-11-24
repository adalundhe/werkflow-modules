from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_in_app_campaign_schedule import PinpointInAppCampaignSchedule
from .pinpoint_in_app_message import PinpointInAppMessage


class PinpointInAppMessageCampaign(BaseModel):
    CampaignId: StrictStr | None = None
    DailyCap: StrictInt | None = None
    InAppMessage: PinpointInAppMessage | None = None
    Priority: StrictInt | None = None
    Schedule: PinpointInAppCampaignSchedule | None = None
    SessionCap: StrictInt | None = None
    TotalCap: StrictInt | None = None
    TreatmentId: StrictStr | None = None
