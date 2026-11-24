from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTHttpContext(BaseModel):
    headers: dict[StrictStr, StrictStr] | None = None
    queryString: StrictStr | None = None
