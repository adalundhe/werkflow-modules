from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_input_description import KinesisAnalyticsInputDescription


class KinesisAnalyticsAddApplicationInputResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    InputDescriptions: list[KinesisAnalyticsInputDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
