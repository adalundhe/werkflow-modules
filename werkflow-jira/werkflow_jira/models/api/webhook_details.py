from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WebhookDetails(BaseModel):
    events: list[StrictStr] | None = None
    fieldIdsFilter: list[StrictStr] | None = None
    issuePropertyKeysFilter: list[StrictStr] | None = None
    jqlFilter: StrictStr | None = None
