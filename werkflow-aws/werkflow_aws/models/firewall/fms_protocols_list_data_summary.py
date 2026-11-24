from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSProtocolsListDataSummary(BaseModel):
    ListArn: StrictStr | None = None
    ListId: StrictStr | None = None
    ListName: StrictStr | None = None
    ProtocolsList: list[StrictStr] | None = None
