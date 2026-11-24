from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_destination_data_sharing import SSMResourceDataSyncDestinationDataSharing


class SSMResourceDataSyncS3Destination(BaseModel):
    BucketName: StrictStr | None = None
    Prefix: StrictStr | None = None
    SyncFormat: StrictStr | None = None
    Region: StrictStr | None = None
    AWSKMSKeyARN: StrictStr | None = None
    DestinationDataSharing: SSMResourceDataSyncDestinationDataSharing | None = None
