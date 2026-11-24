from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail
from .glue_status_details import GlueStatusDetails


class GlueTableStatus(BaseModel):
    RequestedBy: StrictStr | None = None
    UpdatedBy: StrictStr | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    Action: StrictStr | None = None
    State: StrictStr | None = None
    Error: GlueErrorDetail | None = None
    Details: GlueStatusDetails | None = None
