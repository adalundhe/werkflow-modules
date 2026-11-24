from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTCertificate(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    status: StrictStr | None = None
    certificateMode: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
