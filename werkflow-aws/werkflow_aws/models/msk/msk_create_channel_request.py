from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_channel_logging_info import MSKChannelLoggingInfo
from .msk_encryption_configuration import MSKEncryptionConfiguration
from .msk_iceberg_destination_configuration import MSKIcebergDestinationConfiguration
from .msks3_destination_configuration import MSKS3DestinationConfiguration
from .msk_topic_configuration import MSKTopicConfiguration


class MSKCreateChannelRequest(BaseModel):
    ChannelName: StrictStr
    ClusterArn: StrictStr
    TopicConfigurationList: list[MSKTopicConfiguration]
    EncryptionConfiguration: MSKEncryptionConfiguration | None = None
    IcebergDestinationConfiguration: MSKIcebergDestinationConfiguration | None = None
    S3DestinationConfiguration: MSKS3DestinationConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LoggingInfo: MSKChannelLoggingInfo | None = None
