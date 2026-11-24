from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubProductV2(BaseModel):
    ProductV2Name: StrictStr | None = None
    CompanyName: StrictStr | None = None
    Description: StrictStr | None = None
    Categories: list[StrictStr] | None = None
    IntegrationV2Types: list[StrictStr] | None = None
    MarketplaceUrl: StrictStr | None = None
    ActivationUrl: StrictStr | None = None
    MarketplaceProductId: StrictStr | None = None
