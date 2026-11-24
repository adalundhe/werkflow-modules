from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .pinpoint_campaign_hook import PinpointCampaignHook
from .pinpoint_campaign_limits import PinpointCampaignLimits
from .pinpoint_campaign_state import PinpointCampaignState
from .pinpoint_custom_delivery_configuration import PinpointCustomDeliveryConfiguration
from .pinpoint_message_configuration import PinpointMessageConfiguration
from .pinpoint_schedule import PinpointSchedule
from .pinpoint_template_configuration import PinpointTemplateConfiguration
from .pinpoint_treatment_resource import PinpointTreatmentResource


class PinpointCampaignResponse(BaseModel):
    AdditionalTreatments: list[PinpointTreatmentResource] | None = None
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreationDate: StrictStr | None = None
    CustomDeliveryConfiguration: PinpointCustomDeliveryConfiguration | None = None
    DefaultState: PinpointCampaignState | None = None
    Description: StrictStr | None = None
    HoldoutPercent: StrictInt | None = None
    Hook: PinpointCampaignHook | None = None
    Id: StrictStr | None = None
    IsPaused: StrictBool | None = None
    LastModifiedDate: StrictStr | None = None
    Limits: PinpointCampaignLimits | None = None
    MessageConfiguration: PinpointMessageConfiguration | None = None
    Name: StrictStr | None = None
    Schedule: PinpointSchedule | None = None
    SegmentId: StrictStr | None = None
    SegmentVersion: StrictInt | None = None
    State: PinpointCampaignState | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateConfiguration: PinpointTemplateConfiguration | None = None
    TreatmentDescription: StrictStr | None = None
    TreatmentName: StrictStr | None = None
    Version: StrictInt | None = None
    Priority: StrictInt | None = None
