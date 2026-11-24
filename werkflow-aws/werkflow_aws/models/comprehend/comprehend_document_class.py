from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendDocumentClass(BaseModel):
    Name: StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
    Page: StrictInt | None = None
