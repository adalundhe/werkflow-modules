from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_partner_info import LightsailPartnerInfo


class LightsailGetProfileResponse(BaseModel):
    profileType: StrictStr | None = None
    partner: LightsailPartnerInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
