from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_input_processing_configuration import KinesisAnalyticsInputProcessingConfiguration


class KinesisAnalyticsAddApplicationInputProcessingConfigurationRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    InputId: StrictStr
    InputProcessingConfiguration: KinesisAnalyticsInputProcessingConfiguration
