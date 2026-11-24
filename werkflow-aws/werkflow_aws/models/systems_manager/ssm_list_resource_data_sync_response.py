from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_item import SSMResourceDataSyncItem


class SSMListResourceDataSyncResponse(BaseModel):
    ResourceDataSyncItems: list[SSMResourceDataSyncItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
