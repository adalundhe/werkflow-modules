from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueViewValidation(BaseModel):
    Dialect: StrictStr | None = None
    DialectVersion: StrictStr | None = None
    ViewValidationText: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Error: GlueErrorDetail | None = None
