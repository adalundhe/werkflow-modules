from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .pinpoint_campaign_hook import PinpointCampaignHook
from .pinpoint_campaign_limits import PinpointCampaignLimits
from .pinpoint_custom_delivery_configuration import PinpointCustomDeliveryConfiguration
from .pinpoint_message_configuration import PinpointMessageConfiguration
from .pinpoint_schedule import PinpointSchedule
from .pinpoint_template_configuration import PinpointTemplateConfiguration
from .pinpoint_write_treatment_resource import PinpointWriteTreatmentResource


class PinpointWriteCampaignRequest(BaseModel):
    AdditionalTreatments: list[PinpointWriteTreatmentResource] | None = None
    CustomDeliveryConfiguration: PinpointCustomDeliveryConfiguration | None = None
    Description: StrictStr | None = None
    HoldoutPercent: StrictInt | None = None
    Hook: PinpointCampaignHook | None = None
    IsPaused: StrictBool | None = None
    Limits: PinpointCampaignLimits | None = None
    MessageConfiguration: PinpointMessageConfiguration | None = None
    Name: StrictStr | None = None
    Schedule: PinpointSchedule | None = None
    SegmentId: StrictStr | None = None
    SegmentVersion: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TreatmentDescription: StrictStr | None = None
    TreatmentName: StrictStr | None = None
    Priority: StrictInt | None = None
