from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESExportDestination(BaseModel):
    DataFormat: StrictStr | None = None
    S3Url: StrictStr | None = None
