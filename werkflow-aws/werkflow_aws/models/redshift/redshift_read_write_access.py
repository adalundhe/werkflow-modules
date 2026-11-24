from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftReadWriteAccess(BaseModel):
    Authorization: StrictStr | None = None
