from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessErrorDetail(BaseModel):
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
