from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSConnectorConfigResponse(BaseModel):
    activationId: StrictStr | None = None
    activationCode: StrictStr | None = None
    activationExpiry: datetime.datetime | None = None
    provider: StrictStr | None = None
    roleArn: StrictStr | None = None
