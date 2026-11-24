from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListRoleAliasesRequest(BaseModel):
    pageSize: StrictInt | None = None
    marker: StrictStr | None = None
    ascendingOrder: StrictBool | None = None
