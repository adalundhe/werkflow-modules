from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessFailedDocument(BaseModel):
    id: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    dataSourceId: StrictStr | None = None
