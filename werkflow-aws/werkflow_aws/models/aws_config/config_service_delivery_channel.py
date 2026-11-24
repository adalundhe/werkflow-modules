from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_config_snapshot_delivery_properties import ConfigServiceConfigSnapshotDeliveryProperties


class ConfigServiceDeliveryChannel(BaseModel):
    name: StrictStr | None = None
    s3BucketName: StrictStr | None = None
    s3KeyPrefix: StrictStr | None = None
    s3KmsKeyArn: StrictStr | None = None
    snsTopicARN: StrictStr | None = None
    configSnapshotDeliveryProperties: ConfigServiceConfigSnapshotDeliveryProperties | None = None
