from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_destination_schema import KinesisAnalyticsDestinationSchema
from .kinesis_analytics_kinesis_firehose_output_update import KinesisAnalyticsKinesisFirehoseOutputUpdate
from .kinesis_analytics_kinesis_streams_output_update import KinesisAnalyticsKinesisStreamsOutputUpdate
from .kinesis_analytics_lambda_output_update import KinesisAnalyticsLambdaOutputUpdate


class KinesisAnalyticsOutputUpdate(BaseModel):
    OutputId: StrictStr
    NameUpdate: StrictStr | None = None
    KinesisStreamsOutputUpdate: KinesisAnalyticsKinesisStreamsOutputUpdate | None = None
    KinesisFirehoseOutputUpdate: KinesisAnalyticsKinesisFirehoseOutputUpdate | None = None
    LambdaOutputUpdate: KinesisAnalyticsLambdaOutputUpdate | None = None
    DestinationSchemaUpdate: KinesisAnalyticsDestinationSchema | None = None
