from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .fms_app import FMSApp


class FMSAppsListData(BaseModel):
    ListId: StrictStr | None = None
    ListName: StrictStr | None = None
    ListUpdateToken: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    AppsList: list[FMSApp] | None = None
    PreviousAppsList: dict[StrictStr, list[FMSApp]] | None = None
