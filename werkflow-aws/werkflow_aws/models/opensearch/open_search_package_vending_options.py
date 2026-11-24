from __future__ import annotations
from pydantic import BaseModel, StrictBool


class OpenSearchPackageVendingOptions(BaseModel):
    VendingEnabled: StrictBool | None = None
