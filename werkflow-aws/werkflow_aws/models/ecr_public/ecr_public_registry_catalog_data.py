from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicRegistryCatalogData(BaseModel):
    displayName: StrictStr | None = None
