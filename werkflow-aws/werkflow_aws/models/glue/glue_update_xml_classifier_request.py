from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateXMLClassifierRequest(BaseModel):
    Name: StrictStr
    Classification: StrictStr | None = None
    RowTag: StrictStr | None = None
