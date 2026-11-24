from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogUpdateProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    AcceptLanguage: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Active: StrictBool | None = None
    Guidance: Literal['DEFAULT', 'DEPRECATED'] | None = None
