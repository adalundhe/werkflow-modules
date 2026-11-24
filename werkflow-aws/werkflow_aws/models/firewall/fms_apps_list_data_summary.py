from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_app import FMSApp


class FMSAppsListDataSummary(BaseModel):
    ListArn: StrictStr | None = None
    ListId: StrictStr | None = None
    ListName: StrictStr | None = None
    AppsList: list[FMSApp] | None = None
