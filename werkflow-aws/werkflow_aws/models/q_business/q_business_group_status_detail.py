from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessGroupStatusDetail(BaseModel):
    status: StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    errorDetail: QBusinessErrorDetail | None = None
