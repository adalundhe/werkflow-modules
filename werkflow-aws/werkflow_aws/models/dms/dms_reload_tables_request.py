from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dms_table_to_reload import DMSTableToReload


class DMSReloadTablesRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    TablesToReload: list[DMSTableToReload]
    ReloadOption: Literal['data-reload', 'validate-only'] | None = None
