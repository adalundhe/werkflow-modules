from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_iceberg_destination_update import MSKIcebergDestinationUpdate
from .msks3_destination_update import MSKS3DestinationUpdate


class MSKUpdateChannelRequest(BaseModel):
    ChannelArn: StrictStr
    ClusterArn: StrictStr
    IcebergDestinationUpdate: MSKIcebergDestinationUpdate | None = None
    S3DestinationUpdate: MSKS3DestinationUpdate | None = None
