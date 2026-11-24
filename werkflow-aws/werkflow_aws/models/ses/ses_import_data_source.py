from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESImportDataSource(BaseModel):
    S3Url: StrictStr | None = None
    DataFormat: StrictStr | None = None
