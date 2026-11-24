from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTRetryCriteria(BaseModel):
    failureType: StrictStr | None = None
    numberOfRetries: StrictInt | None = None
