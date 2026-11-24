from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSMarketplaceInformation(BaseModel):
    productId: StrictStr | None = None
    productUrl: StrictStr | None = None
