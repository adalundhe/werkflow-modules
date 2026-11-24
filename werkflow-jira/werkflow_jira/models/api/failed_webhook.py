from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FailedWebhook(BaseModel):
    body: StrictStr | None = None
    failureTime: StrictInt | None = None
    id: StrictStr | None = None
    url: StrictStr | None = None
