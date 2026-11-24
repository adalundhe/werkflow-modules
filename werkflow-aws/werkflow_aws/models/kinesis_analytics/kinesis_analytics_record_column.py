from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsRecordColumn(BaseModel):
    Name: StrictStr | None = None
    Mapping: StrictStr | None = None
    SqlType: StrictStr | None = None
