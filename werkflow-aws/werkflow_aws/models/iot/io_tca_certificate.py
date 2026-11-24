from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTCACertificate(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    status: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
