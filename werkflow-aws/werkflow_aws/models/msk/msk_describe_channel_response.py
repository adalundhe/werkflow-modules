from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_channel_logging_info import MSKChannelLoggingInfo
from .msk_channel_state_info import MSKChannelStateInfo
from .msk_encryption_configuration import MSKEncryptionConfiguration
from .msk_iceberg_destination_configuration import MSKIcebergDestinationConfiguration
from .msks3_destination_configuration import MSKS3DestinationConfiguration
from .msk_topic_configuration import MSKTopicConfiguration


class MSKDescribeChannelResponse(BaseModel):
    ChannelArn: StrictStr | None = None
    ChannelName: StrictStr | None = None
    EncryptionConfiguration: MSKEncryptionConfiguration | None = None
    IcebergDestinationConfiguration: MSKIcebergDestinationConfiguration | None = None
    S3DestinationConfiguration: MSKS3DestinationConfiguration | None = None
    Status: StrictStr | None = None
    DestinationType: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TopicConfigurationList: list[MSKTopicConfiguration] | None = None
    LoggingInfo: MSKChannelLoggingInfo | None = None
    StateInfo: MSKChannelStateInfo | None = None
    ClusterOperationArn: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
