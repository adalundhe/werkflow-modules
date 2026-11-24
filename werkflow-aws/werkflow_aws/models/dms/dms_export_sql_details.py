from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSExportSqlDetails(BaseModel):
    S3ObjectKey: StrictStr | None = None
    ObjectURL: StrictStr | None = None
