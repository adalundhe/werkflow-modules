from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSConnectorConfigResponseModel(BaseModel):
    activationId: StrictStr | None = None
    activationCode: StrictStr | None = None
    activationExpiry: datetime.datetime | StrictStr | None = None
    provider: StrictStr | None = None
    roleArn: StrictStr | None = None
