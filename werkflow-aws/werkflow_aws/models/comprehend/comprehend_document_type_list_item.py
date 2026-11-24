from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendDocumentTypeListItem(BaseModel):
    Page: StrictInt | None = None
    Type: StrictStr | None = None
