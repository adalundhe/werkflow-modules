from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchKeyValuesPair(BaseModel):
    name: StrictStr | None = None
    values: list[StrictStr] | None = None
