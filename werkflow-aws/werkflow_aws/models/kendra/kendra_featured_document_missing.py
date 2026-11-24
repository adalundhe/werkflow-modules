from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraFeaturedDocumentMissing(BaseModel):
    Id: StrictStr | None = None
