from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlowModuleAliasSummary(BaseModel):
    Arn: StrictStr | None = None
    AliasId: StrictStr | None = None
    Version: StrictInt | None = None
    AliasName: StrictStr | None = None
    AliasDescription: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
