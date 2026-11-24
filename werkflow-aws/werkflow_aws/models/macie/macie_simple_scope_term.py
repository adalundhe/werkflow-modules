from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieSimpleScopeTerm(BaseModel):
    comparator: StrictStr | None = None
    key: StrictStr | None = None
    values: list[StrictStr] | None = None
