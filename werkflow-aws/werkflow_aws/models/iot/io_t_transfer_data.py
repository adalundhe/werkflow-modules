from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTTransferData(BaseModel):
    transferMessage: StrictStr | None = None
    rejectReason: StrictStr | None = None
    transferDate: datetime.datetime | StrictStr | None = None
    acceptDate: datetime.datetime | StrictStr | None = None
    rejectDate: datetime.datetime | StrictStr | None = None
