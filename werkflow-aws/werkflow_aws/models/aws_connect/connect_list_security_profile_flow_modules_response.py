from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_flow_module import ConnectFlowModule


class ConnectListSecurityProfileFlowModulesResponse(BaseModel):
    AllowedFlowModules: list[ConnectFlowModule] | None = None
    NextToken: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
