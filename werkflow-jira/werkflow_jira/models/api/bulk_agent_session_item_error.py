from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BulkAgentSessionItemError(BaseModel):
    message: StrictStr | None = None
    statusCode: StrictInt | None = None
    type: StrictStr | None = None
