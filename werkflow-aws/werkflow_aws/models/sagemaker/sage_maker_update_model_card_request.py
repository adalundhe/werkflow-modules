from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerUpdateModelCardRequest(BaseModel):
    ModelCardName: StrictStr
    Content: StrictStr | None = None
    ModelCardStatus: Literal['Draft', 'PendingReview', 'Approved', 'Archived'] | None = None
