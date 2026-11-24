from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRollingDateConfiguration(BaseModel):
    DataSetIdentifier: StrictStr | None = None
    Expression: StrictStr | None = None
