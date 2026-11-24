from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueMapping(BaseModel):
    ToKey: StrictStr | None = None
    FromPath: list[StrictStr] | None = None
    FromType: StrictStr | None = None
    ToType: StrictStr | None = None
    Dropped: StrictBool | None = None
    Children: list[GlueMapping] | None = None
