from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDestinationSchema(BaseModel):
    RecordFormatType: StrictStr | None = None
