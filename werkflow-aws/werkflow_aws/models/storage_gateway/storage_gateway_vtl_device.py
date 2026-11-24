from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_devicei_scsi_attributes import StorageGatewayDeviceiSCSIAttributes


class StorageGatewayVTLDevice(BaseModel):
    VTLDeviceARN: StrictStr | None = None
    VTLDeviceType: StrictStr | None = None
    VTLDeviceVendor: StrictStr | None = None
    VTLDeviceProductIdentifier: StrictStr | None = None
    DeviceiSCSIAttributes: StorageGatewayDeviceiSCSIAttributes | None = None
