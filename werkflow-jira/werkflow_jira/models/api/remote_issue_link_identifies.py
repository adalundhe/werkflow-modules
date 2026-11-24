from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RemoteIssueLinkIdentifies(BaseModel):
    id: StrictInt | None = None
    self: StrictStr | None = None
