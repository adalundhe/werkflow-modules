from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_multi_measure_attribute_mapping import TimestreamWriteMultiMeasureAttributeMapping


class TimestreamWriteMixedMeasureMapping(BaseModel):
    MeasureName: StrictStr | None = None
    SourceColumn: StrictStr | None = None
    TargetMeasureName: StrictStr | None = None
    MeasureValueType: StrictStr | None = None
    MultiMeasureAttributeMappings: list[TimestreamWriteMultiMeasureAttributeMapping] | None = None
