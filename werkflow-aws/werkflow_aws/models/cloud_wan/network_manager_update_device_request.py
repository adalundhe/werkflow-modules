from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_aws_location import NetworkManagerAWSLocation
from .network_manager_location import NetworkManagerLocation


class NetworkManagerUpdateDeviceRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr
    AWSLocation: NetworkManagerAWSLocation | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    Vendor: StrictStr | None = None
    Model: StrictStr | None = None
    SerialNumber: StrictStr | None = None
    Location: NetworkManagerLocation | None = None
    SiteId: StrictStr | None = None
