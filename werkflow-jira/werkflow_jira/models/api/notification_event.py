from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NotificationEvent(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    templateEvent: NotificationEvent | None = None
