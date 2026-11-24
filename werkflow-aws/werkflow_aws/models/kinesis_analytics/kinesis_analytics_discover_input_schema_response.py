from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsDiscoverInputSchemaResponse(BaseModel):
    InputSchema: KinesisAnalyticsSourceSchema | None = None
    ParsedInputRecords: list[list[StrictStr]] | None = None
    ProcessedInputRecords: list[StrictStr] | None = None
    RawInputRecords: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
