from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CloudTrailPublicKey(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Value: StrictBytes | Any | None = None
    ValidityStartTime: datetime.datetime | StrictStr | None = None
    ValidityEndTime: datetime.datetime | StrictStr | None = None
    Fingerprint: StrictStr | None = None
