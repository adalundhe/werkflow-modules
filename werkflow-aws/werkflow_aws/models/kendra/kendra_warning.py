from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraWarning(BaseModel):
    Message: StrictStr | None = None
    Code: StrictStr | None = None
