from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FMSGetThirdPartyFirewallAssociationStatusResponse(BaseModel):
    ThirdPartyFirewallStatus: StrictStr | None = None
    MarketplaceOnboardingStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
