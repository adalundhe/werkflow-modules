from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLoadingAnimation(BaseModel):
    Visibility: StrictStr | None = None
