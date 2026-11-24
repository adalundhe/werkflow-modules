from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_custom_delivery_configuration import PinpointCustomDeliveryConfiguration
from .pinpoint_message_configuration import PinpointMessageConfiguration
from .pinpoint_schedule import PinpointSchedule
from .pinpoint_template_configuration import PinpointTemplateConfiguration


class PinpointWriteTreatmentResource(BaseModel):
    SizePercent: StrictInt
    CustomDeliveryConfiguration: PinpointCustomDeliveryConfiguration | None = None
    MessageConfiguration: PinpointMessageConfiguration | None = None
    Schedule: PinpointSchedule | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TreatmentDescription: StrictStr | None = None
    TreatmentName: StrictStr | None = None
