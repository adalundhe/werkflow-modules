from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_input_parallelism import KinesisAnalyticsInputParallelism
from .kinesis_analytics_input_processing_configuration_description import KinesisAnalyticsInputProcessingConfigurationDescription
from .kinesis_analytics_input_starting_position_configuration import KinesisAnalyticsInputStartingPositionConfiguration
from .kinesis_analytics_kinesis_firehose_input_description import KinesisAnalyticsKinesisFirehoseInputDescription
from .kinesis_analytics_kinesis_streams_input_description import KinesisAnalyticsKinesisStreamsInputDescription
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsInputDescription(BaseModel):
    InputId: StrictStr | None = None
    NamePrefix: StrictStr | None = None
    InAppStreamNames: list[StrictStr] | None = None
    InputProcessingConfigurationDescription: KinesisAnalyticsInputProcessingConfigurationDescription | None = None
    KinesisStreamsInputDescription: KinesisAnalyticsKinesisStreamsInputDescription | None = None
    KinesisFirehoseInputDescription: KinesisAnalyticsKinesisFirehoseInputDescription | None = None
    InputSchema: KinesisAnalyticsSourceSchema | None = None
    InputParallelism: KinesisAnalyticsInputParallelism | None = None
    InputStartingPositionConfiguration: KinesisAnalyticsInputStartingPositionConfiguration | None = None
