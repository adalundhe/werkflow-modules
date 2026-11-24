from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_multi_measure_attribute_mapping import TimestreamWriteMultiMeasureAttributeMapping


class TimestreamWriteMultiMeasureMappings(BaseModel):
    TargetMultiMeasureName: StrictStr | None = None
    MultiMeasureAttributeMappings: list[TimestreamWriteMultiMeasureAttributeMapping] | None = None
