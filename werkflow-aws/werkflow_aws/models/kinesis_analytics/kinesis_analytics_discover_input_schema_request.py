from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_input_processing_configuration import KinesisAnalyticsInputProcessingConfiguration
from .kinesis_analytics_input_starting_position_configuration import KinesisAnalyticsInputStartingPositionConfiguration
from .kinesis_analytics_s3_configuration import KinesisAnalyticsS3Configuration


class KinesisAnalyticsDiscoverInputSchemaRequest(BaseModel):
    ServiceExecutionRole: StrictStr
    ResourceARN: StrictStr | None = None
    InputStartingPositionConfiguration: KinesisAnalyticsInputStartingPositionConfiguration | None = None
    S3Configuration: KinesisAnalyticsS3Configuration | None = None
    InputProcessingConfiguration: KinesisAnalyticsInputProcessingConfiguration | None = None
