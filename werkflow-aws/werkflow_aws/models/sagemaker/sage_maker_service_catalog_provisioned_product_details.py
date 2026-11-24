from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerServiceCatalogProvisionedProductDetails(BaseModel):
    ProvisionedProductId: StrictStr | None = None
    ProvisionedProductStatusMessage: StrictStr | None = None
