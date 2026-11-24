from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_destination_schema import KinesisAnalyticsDestinationSchema
from .kinesis_analytics_kinesis_firehose_output import KinesisAnalyticsKinesisFirehoseOutput
from .kinesis_analytics_kinesis_streams_output import KinesisAnalyticsKinesisStreamsOutput
from .kinesis_analytics_lambda_output import KinesisAnalyticsLambdaOutput


class KinesisAnalyticsOutput(BaseModel):
    Name: StrictStr
    DestinationSchema: KinesisAnalyticsDestinationSchema
    KinesisStreamsOutput: KinesisAnalyticsKinesisStreamsOutput | None = None
    KinesisFirehoseOutput: KinesisAnalyticsKinesisFirehoseOutput | None = None
    LambdaOutput: KinesisAnalyticsLambdaOutput | None = None
