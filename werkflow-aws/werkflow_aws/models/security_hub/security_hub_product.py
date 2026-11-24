from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubProduct(BaseModel):
    ProductArn: StrictStr | None = None
    ProductName: StrictStr | None = None
    CompanyName: StrictStr | None = None
    Description: StrictStr | None = None
    Categories: list[StrictStr] | None = None
    IntegrationTypes: list[StrictStr] | None = None
    MarketplaceUrl: StrictStr | None = None
    ActivationUrl: StrictStr | None = None
    ProductSubscriptionResourcePolicy: StrictStr | None = None
