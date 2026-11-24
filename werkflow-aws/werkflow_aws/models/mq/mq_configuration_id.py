from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MQConfigurationId(BaseModel):
    Id: StrictStr | None = None
    Revision: StrictInt | None = None
