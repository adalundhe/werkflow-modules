from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DeviceFarmUpload(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    url: StrictStr | None = None
    metadata: StrictStr | None = None
    contentType: StrictStr | None = None
    message: StrictStr | None = None
    category: StrictStr | None = None
