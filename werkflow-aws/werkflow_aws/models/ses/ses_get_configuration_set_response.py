from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_archiving_options import SESArchivingOptions
from .ses_delivery_options import SESDeliveryOptions
from .ses_message_security_options import SESMessageSecurityOptions
from .ses_reputation_options import SESReputationOptions
from .ses_sending_options import SESSendingOptions
from .ses_suppression_options import SESSuppressionOptions
from .ses_tag import SESTag
from .ses_tracking_options import SESTrackingOptions
from .ses_vdm_options import SESVdmOptions


class SESGetConfigurationSetResponse(BaseModel):
    ConfigurationSetName: StrictStr | None = None
    TrackingOptions: SESTrackingOptions | None = None
    DeliveryOptions: SESDeliveryOptions | None = None
    ReputationOptions: SESReputationOptions | None = None
    SendingOptions: SESSendingOptions | None = None
    Tags: list[SESTag] | None = None
    SuppressionOptions: SESSuppressionOptions | None = None
    VdmOptions: SESVdmOptions | None = None
    ArchivingOptions: SESArchivingOptions | None = None
    MessageSecurityOptions: SESMessageSecurityOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
