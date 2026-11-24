from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_sync_event_config import AppSyncEventConfig


class AppSyncApi(BaseModel):
    apiId: StrictStr | None = None
    name: StrictStr | None = None
    ownerContact: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    dns: dict[StrictStr, StrictStr] | None = None
    apiArn: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    xrayEnabled: StrictBool | None = None
    wafWebAclArn: StrictStr | None = None
    eventConfig: AppSyncEventConfig | None = None
