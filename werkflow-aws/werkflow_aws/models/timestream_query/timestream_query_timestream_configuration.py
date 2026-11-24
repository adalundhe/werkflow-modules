from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_dimension_mapping import TimestreamQueryDimensionMapping
from .timestream_query_mixed_measure_mapping import TimestreamQueryMixedMeasureMapping
from .timestream_query_multi_measure_mappings import TimestreamQueryMultiMeasureMappings


class TimestreamQueryTimestreamConfiguration(BaseModel):
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    TimeColumn: StrictStr | None = None
    DimensionMappings: list[TimestreamQueryDimensionMapping] | None = None
    MultiMeasureMappings: TimestreamQueryMultiMeasureMappings | None = None
    MixedMeasureMappings: list[TimestreamQueryMixedMeasureMapping] | None = None
    MeasureNameColumn: StrictStr | None = None
