from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_dimension_mapping import TimestreamWriteDimensionMapping
from .timestream_write_mixed_measure_mapping import TimestreamWriteMixedMeasureMapping
from .timestream_write_multi_measure_mappings import TimestreamWriteMultiMeasureMappings


class TimestreamWriteDataModel(BaseModel):
    TimeColumn: StrictStr | None = None
    TimeUnit: StrictStr | None = None
    DimensionMappings: list[TimestreamWriteDimensionMapping] | None = None
    MultiMeasureMappings: TimestreamWriteMultiMeasureMappings | None = None
    MixedMeasureMappings: list[TimestreamWriteMixedMeasureMapping] | None = None
    MeasureNameColumn: StrictStr | None = None
