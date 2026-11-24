from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraFeaturedDocument(BaseModel):
    Id: StrictStr | None = None
