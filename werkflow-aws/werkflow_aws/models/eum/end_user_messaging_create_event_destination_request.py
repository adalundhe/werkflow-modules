from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_cloud_watch_logs_destination import EndUserMessagingCloudWatchLogsDestination
from .end_user_messaging_kinesis_firehose_destination import EndUserMessagingKinesisFirehoseDestination
from .end_user_messaging_sns_destination import EndUserMessagingSnsDestination


class EndUserMessagingCreateEventDestinationRequest(BaseModel):
    ConfigurationSetName: StrictStr
    EventDestinationName: StrictStr
    MatchingEventTypes: list[StrictStr]
    CloudWatchLogsDestination: EndUserMessagingCloudWatchLogsDestination | None = None
    KinesisFirehoseDestination: EndUserMessagingKinesisFirehoseDestination | None = None
    SnsDestination: EndUserMessagingSnsDestination | None = None
    ClientToken: StrictStr | None = None
