from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlQueryFieldEntityProperty(BaseModel):
    entity: StrictStr | None = None
    key: StrictStr | None = None
    path: StrictStr | None = None
    type: StrictStr | None = None
