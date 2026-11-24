from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsCSVMappingParameters(BaseModel):
    RecordRowDelimiter: StrictStr | None = None
    RecordColumnDelimiter: StrictStr | None = None
