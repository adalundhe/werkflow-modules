from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueTableVersionError(BaseModel):
    TableName: StrictStr | None = None
    VersionId: StrictStr | None = None
    ErrorDetail: GlueErrorDetail | None = None
