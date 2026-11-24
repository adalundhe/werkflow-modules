from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlowModuleAliasInfo(BaseModel):
    ContactFlowModuleId: StrictStr | None = None
    ContactFlowModuleArn: StrictStr | None = None
    AliasId: StrictStr | None = None
    Version: StrictInt | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
