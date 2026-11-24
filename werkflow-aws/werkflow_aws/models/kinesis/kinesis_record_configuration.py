from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisRecordConfiguration(BaseModel):
    RecordFormatType: StrictStr | None = None
    GSRSchemaARN: StrictStr | None = None
