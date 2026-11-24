from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_input_parallelism_update import KinesisAnalyticsInputParallelismUpdate
from .kinesis_analytics_input_processing_configuration_update import KinesisAnalyticsInputProcessingConfigurationUpdate
from .kinesis_analytics_input_schema_update import KinesisAnalyticsInputSchemaUpdate
from .kinesis_analytics_kinesis_firehose_input_update import KinesisAnalyticsKinesisFirehoseInputUpdate
from .kinesis_analytics_kinesis_streams_input_update import KinesisAnalyticsKinesisStreamsInputUpdate


class KinesisAnalyticsInputUpdate(BaseModel):
    InputId: StrictStr
    NamePrefixUpdate: StrictStr | None = None
    InputProcessingConfigurationUpdate: KinesisAnalyticsInputProcessingConfigurationUpdate | None = None
    KinesisStreamsInputUpdate: KinesisAnalyticsKinesisStreamsInputUpdate | None = None
    KinesisFirehoseInputUpdate: KinesisAnalyticsKinesisFirehoseInputUpdate | None = None
    InputSchemaUpdate: KinesisAnalyticsInputSchemaUpdate | None = None
    InputParallelismUpdate: KinesisAnalyticsInputParallelismUpdate | None = None
