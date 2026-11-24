from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_cloud_watch_logs_destination import EndUserMessagingCloudWatchLogsDestination
from .end_user_messaging_kinesis_firehose_destination import EndUserMessagingKinesisFirehoseDestination
from .end_user_messaging_sns_destination import EndUserMessagingSnsDestination


class EndUserMessagingEventDestination(BaseModel):
    EventDestinationName: StrictStr | None = None
    Enabled: StrictBool | None = None
    MatchingEventTypes: list[StrictStr] | None = None
    CloudWatchLogsDestination: EndUserMessagingCloudWatchLogsDestination | None = None
    KinesisFirehoseDestination: EndUserMessagingKinesisFirehoseDestination | None = None
    SnsDestination: EndUserMessagingSnsDestination | None = None
