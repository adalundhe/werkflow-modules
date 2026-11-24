from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessDocumentDetails(BaseModel):
    documentId: StrictStr | None = None
    status: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
