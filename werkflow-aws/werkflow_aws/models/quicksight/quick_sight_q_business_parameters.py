from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQBusinessParameters(BaseModel):
    ApplicationArn: StrictStr | None = None
