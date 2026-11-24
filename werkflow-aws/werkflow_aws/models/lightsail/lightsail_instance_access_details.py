from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_host_key_attributes import LightsailHostKeyAttributes
from .lightsail_password_data import LightsailPasswordData


class LightsailInstanceAccessDetails(BaseModel):
    certKey: StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
    ipAddress: StrictStr | None = None
    ipv6Addresses: list[StrictStr] | None = None
    password: StrictStr | None = None
    passwordData: LightsailPasswordData | None = None
    privateKey: StrictStr | None = None
    protocol: StrictStr | None = None
    instanceName: StrictStr | None = None
    username: StrictStr | None = None
    hostKeys: list[LightsailHostKeyAttributes] | None = None
