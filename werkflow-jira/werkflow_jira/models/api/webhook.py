from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Webhook(BaseModel):
    events: list[StrictStr] | None = None
    expirationDate: StrictInt | None = None
    fieldIdsFilter: list[StrictStr] | None = None
    id: StrictInt | None = None
    issuePropertyKeysFilter: list[StrictStr] | None = None
    jqlFilter: StrictStr | None = None
    url: StrictStr | None = None
