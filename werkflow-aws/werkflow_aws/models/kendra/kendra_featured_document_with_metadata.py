from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraFeaturedDocumentWithMetadata(BaseModel):
    Id: StrictStr | None = None
    Title: StrictStr | None = None
    URI: StrictStr | None = None
