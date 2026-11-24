from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCancelledChangeProperty(BaseModel):
    PropertyName: StrictStr | None = None
    CancelledValue: StrictStr | None = None
    ActiveValue: StrictStr | None = None
