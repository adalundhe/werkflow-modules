from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeCopyProductStatusRequest(BaseModel):
    CopyProductToken: StrictStr
    AcceptLanguage: StrictStr | None = None
