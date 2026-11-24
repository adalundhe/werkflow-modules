from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_input_parallelism import KinesisAnalyticsInputParallelism
from .kinesis_analytics_input_processing_configuration import KinesisAnalyticsInputProcessingConfiguration
from .kinesis_analytics_kinesis_firehose_input import KinesisAnalyticsKinesisFirehoseInput
from .kinesis_analytics_kinesis_streams_input import KinesisAnalyticsKinesisStreamsInput
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsInput(BaseModel):
    NamePrefix: StrictStr
    InputSchema: KinesisAnalyticsSourceSchema
    InputProcessingConfiguration: KinesisAnalyticsInputProcessingConfiguration | None = None
    KinesisStreamsInput: KinesisAnalyticsKinesisStreamsInput | None = None
    KinesisFirehoseInput: KinesisAnalyticsKinesisFirehoseInput | None = None
    InputParallelism: KinesisAnalyticsInputParallelism | None = None
