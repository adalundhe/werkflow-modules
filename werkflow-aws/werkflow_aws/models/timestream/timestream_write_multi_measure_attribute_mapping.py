from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteMultiMeasureAttributeMapping(BaseModel):
    SourceColumn: StrictStr | None = None
    TargetMultiMeasureAttributeName: StrictStr | None = None
    MeasureValueType: StrictStr | None = None
