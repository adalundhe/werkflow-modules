from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FMSProtocolsListData(BaseModel):
    ListId: StrictStr | None = None
    ListName: StrictStr | None = None
    ListUpdateToken: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    ProtocolsList: list[StrictStr] | None = None
    PreviousProtocolsList: dict[StrictStr, list[StrictStr]] | None = None
