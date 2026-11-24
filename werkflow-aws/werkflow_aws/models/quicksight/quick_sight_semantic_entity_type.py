from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSemanticEntityType(BaseModel):
    TypeName: StrictStr | None = None
    SubTypeName: StrictStr | None = None
    TypeParameters: dict[StrictStr, StrictStr] | None = None
