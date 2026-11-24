from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAmazonOpenSearchParameters(BaseModel):
    Domain: StrictStr | None = None
