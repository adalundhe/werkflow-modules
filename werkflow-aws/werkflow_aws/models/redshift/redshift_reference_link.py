from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftReferenceLink(BaseModel):
    Text: StrictStr | None = None
    Link: StrictStr | None = None
