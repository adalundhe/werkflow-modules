from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_output_description import KinesisAnalyticsOutputDescription


class KinesisAnalyticsAddApplicationOutputResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    OutputDescriptions: list[KinesisAnalyticsOutputDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
