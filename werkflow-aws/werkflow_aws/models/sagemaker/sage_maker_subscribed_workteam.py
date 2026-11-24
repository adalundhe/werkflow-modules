from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSubscribedWorkteam(BaseModel):
    WorkteamArn: StrictStr | None = None
    MarketplaceTitle: StrictStr | None = None
    SellerName: StrictStr | None = None
    MarketplaceDescription: StrictStr | None = None
    ListingId: StrictStr | None = None
