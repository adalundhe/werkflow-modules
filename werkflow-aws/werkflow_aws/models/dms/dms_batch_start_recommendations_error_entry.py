from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSBatchStartRecommendationsErrorEntry(BaseModel):
    DatabaseId: StrictStr | None = None
    Message: StrictStr | None = None
    Code: StrictStr | None = None
