from __future__ import annotations
from pydantic import BaseModel
from .connect_device_info import ConnectDeviceInfo
from .connect_participant_capabilities import ConnectParticipantCapabilities


class ConnectCustomer(BaseModel):
    DeviceInfo: ConnectDeviceInfo | None = None
    Capabilities: ConnectParticipantCapabilities | None = None
