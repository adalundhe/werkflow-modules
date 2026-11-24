from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaPropagateTags(BaseModel):
    Mode: StrictStr | None = None
    ExplicitTags: dict[StrictStr, StrictStr] | None = None
