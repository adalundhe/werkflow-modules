from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSourceTableConfig(BaseModel):
    Fields: list[StrictStr] | None = None
    FilterPredicate: StrictStr | None = None
    PrimaryKey: list[StrictStr] | None = None
    RecordUpdateField: StrictStr | None = None
