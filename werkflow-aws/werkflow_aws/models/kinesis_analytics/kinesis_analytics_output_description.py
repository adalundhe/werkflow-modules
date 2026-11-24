from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_destination_schema import KinesisAnalyticsDestinationSchema
from .kinesis_analytics_kinesis_firehose_output_description import KinesisAnalyticsKinesisFirehoseOutputDescription
from .kinesis_analytics_kinesis_streams_output_description import KinesisAnalyticsKinesisStreamsOutputDescription
from .kinesis_analytics_lambda_output_description import KinesisAnalyticsLambdaOutputDescription


class KinesisAnalyticsOutputDescription(BaseModel):
    OutputId: StrictStr | None = None
    Name: StrictStr | None = None
    KinesisStreamsOutputDescription: KinesisAnalyticsKinesisStreamsOutputDescription | None = None
    KinesisFirehoseOutputDescription: KinesisAnalyticsKinesisFirehoseOutputDescription | None = None
    LambdaOutputDescription: KinesisAnalyticsLambdaOutputDescription | None = None
    DestinationSchema: KinesisAnalyticsDestinationSchema | None = None
