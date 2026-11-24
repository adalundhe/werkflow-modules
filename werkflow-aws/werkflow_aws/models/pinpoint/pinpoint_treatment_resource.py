from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_campaign_state import PinpointCampaignState
from .pinpoint_custom_delivery_configuration import PinpointCustomDeliveryConfiguration
from .pinpoint_message_configuration import PinpointMessageConfiguration
from .pinpoint_schedule import PinpointSchedule
from .pinpoint_template_configuration import PinpointTemplateConfiguration


class PinpointTreatmentResource(BaseModel):
    CustomDeliveryConfiguration: PinpointCustomDeliveryConfiguration | None = None
    Id: StrictStr | None = None
    MessageConfiguration: PinpointMessageConfiguration | None = None
    Schedule: PinpointSchedule | None = None
    SizePercent: StrictInt | None = None
    State: PinpointCampaignState | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TreatmentDescription: StrictStr | None = None
    TreatmentName: StrictStr | None = None
