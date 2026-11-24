from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .firehose_delivery_stream_encryption_configuration import FirehoseDeliveryStreamEncryptionConfiguration
from .firehose_destination_description import FirehoseDestinationDescription
from .firehose_failure_description import FirehoseFailureDescription
from .firehose_source_description import FirehoseSourceDescription


class FirehoseDeliveryStreamDescription(BaseModel):
    DeliveryStreamName: StrictStr | None = None
    DeliveryStreamARN: StrictStr | None = None
    DeliveryStreamStatus: StrictStr | None = None
    FailureDescription: FirehoseFailureDescription | None = None
    DeliveryStreamEncryptionConfiguration: FirehoseDeliveryStreamEncryptionConfiguration | None = None
    DeliveryStreamType: StrictStr | None = None
    VersionId: StrictStr | None = None
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    Source: FirehoseSourceDescription | None = None
    Destinations: list[FirehoseDestinationDescription] | None = None
    HasMoreDestinations: StrictBool | None = None
