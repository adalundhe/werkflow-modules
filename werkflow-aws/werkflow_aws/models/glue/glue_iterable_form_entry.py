from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIterableFormEntry(BaseModel):
    FormTypeId: StrictStr | None = None
