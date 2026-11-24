from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateXMLClassifierRequest(BaseModel):
    Classification: StrictStr
    Name: StrictStr
    RowTag: StrictStr | None = None
