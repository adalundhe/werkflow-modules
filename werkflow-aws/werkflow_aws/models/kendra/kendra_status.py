from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraStatus(BaseModel):
    DocumentId: StrictStr | None = None
    DocumentStatus: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureReason: StrictStr | None = None
