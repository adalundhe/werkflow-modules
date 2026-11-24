from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_input_processing_configuration_description import KinesisAnalyticsInputProcessingConfigurationDescription


class KinesisAnalyticsAddApplicationInputProcessingConfigurationResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    InputId: StrictStr | None = None
    InputProcessingConfigurationDescription: KinesisAnalyticsInputProcessingConfigurationDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
