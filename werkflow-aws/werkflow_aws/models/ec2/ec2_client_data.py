from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EC2ClientData(BaseModel):
    Comment: StrictStr | None = None
    UploadEnd: datetime.datetime | StrictStr | None = None
    UploadSize: StrictFloat | StrictInt | None = None
    UploadStart: datetime.datetime | StrictStr | None = None
