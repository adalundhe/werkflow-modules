from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_multi_measure_attribute_mapping import TimestreamQueryMultiMeasureAttributeMapping


class TimestreamQueryMixedMeasureMapping(BaseModel):
    MeasureName: StrictStr | None = None
    SourceColumn: StrictStr | None = None
    TargetMeasureName: StrictStr | None = None
    MeasureValueType: StrictStr | None = None
    MultiMeasureAttributeMappings: list[TimestreamQueryMultiMeasureAttributeMapping] | None = None
