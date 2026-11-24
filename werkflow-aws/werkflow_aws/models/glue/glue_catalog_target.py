from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCatalogTarget(BaseModel):
    DatabaseName: StrictStr | None = None
    Tables: list[StrictStr] | None = None
    ConnectionName: StrictStr | None = None
    EventQueueArn: StrictStr | None = None
    DlqEventQueueArn: StrictStr | None = None
