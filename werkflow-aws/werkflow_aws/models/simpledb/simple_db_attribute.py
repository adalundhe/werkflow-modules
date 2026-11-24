from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SimpleDBAttribute(BaseModel):
    Name: StrictStr | None = None
    AlternateNameEncoding: StrictStr | None = None
    Value: StrictStr | None = None
    AlternateValueEncoding: StrictStr | None = None
