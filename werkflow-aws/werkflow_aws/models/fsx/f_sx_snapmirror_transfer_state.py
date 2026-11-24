from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class FSxSnapmirrorTransferState(BaseModel):
    State: StrictStr | None = None
    Type: StrictStr | None = None
    BytesTransferred: StrictInt | None = None
    Duration: StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
