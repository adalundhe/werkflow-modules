from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_cloud_watch_destination import SESCloudWatchDestination
from .ses_event_bridge_destination import SESEventBridgeDestination
from .ses_kinesis_firehose_destination import SESKinesisFirehoseDestination
from .ses_pinpoint_destination import SESPinpointDestination
from .ses_sns_destination import SESSnsDestination


class SESEventDestination(BaseModel):
    Name: StrictStr | None = None
    Enabled: StrictBool | None = None
    MatchingEventTypes: list[StrictStr] | None = None
    KinesisFirehoseDestination: SESKinesisFirehoseDestination | None = None
    CloudWatchDestination: SESCloudWatchDestination | None = None
    SnsDestination: SESSnsDestination | None = None
    EventBridgeDestination: SESEventBridgeDestination | None = None
    PinpointDestination: SESPinpointDestination | None = None
