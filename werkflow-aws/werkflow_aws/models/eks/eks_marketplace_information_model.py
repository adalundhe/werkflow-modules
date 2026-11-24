from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSMarketplaceInformationModel(BaseModel):
    productId: StrictStr | None = None
    productUrl: StrictStr | None = None
