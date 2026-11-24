from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTOutgoingCertificate(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    transferredTo: StrictStr | None = None
    transferDate: datetime.datetime | StrictStr | None = None
    transferMessage: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
