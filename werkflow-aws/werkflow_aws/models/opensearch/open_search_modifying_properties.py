from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchModifyingProperties(BaseModel):
    Name: StrictStr | None = None
    ActiveValue: StrictStr | None = None
    PendingValue: StrictStr | None = None
    ValueType: StrictStr | None = None
