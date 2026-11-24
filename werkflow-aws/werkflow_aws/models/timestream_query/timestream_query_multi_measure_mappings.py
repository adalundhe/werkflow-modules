from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_multi_measure_attribute_mapping import TimestreamQueryMultiMeasureAttributeMapping


class TimestreamQueryMultiMeasureMappings(BaseModel):
    TargetMultiMeasureName: StrictStr | None = None
    MultiMeasureAttributeMappings: list[TimestreamQueryMultiMeasureAttributeMapping] | None = None
