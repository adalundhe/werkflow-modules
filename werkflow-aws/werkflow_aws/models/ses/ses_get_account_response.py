from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_account_details import SESAccountDetails
from .ses_delivery_attributes import SESDeliveryAttributes
from .ses_pricing_attributes import SESPricingAttributes
from .ses_send_quota import SESSendQuota
from .ses_suppression_attributes import SESSuppressionAttributes
from .ses_vdm_attributes import SESVdmAttributes


class SESGetAccountResponse(BaseModel):
    DedicatedIpAutoWarmupEnabled: StrictBool | None = None
    EnforcementStatus: StrictStr | None = None
    ProductionAccessEnabled: StrictBool | None = None
    SendQuota: SESSendQuota | None = None
    SendingEnabled: StrictBool | None = None
    SuppressionAttributes: SESSuppressionAttributes | None = None
    Details: SESAccountDetails | None = None
    VdmAttributes: SESVdmAttributes | None = None
    PricingAttributes: SESPricingAttributes | None = None
    DeliveryAttributes: SESDeliveryAttributes | None = None
    ResponseMetadata: dict[str, Any] | None = None
