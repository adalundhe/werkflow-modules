from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicPutRegistryCatalogDataRequest(BaseModel):
    displayName: StrictStr | None = None
