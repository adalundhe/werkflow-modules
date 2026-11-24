from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class OpenSearchNodeConfig(BaseModel):
    Enabled: StrictBool | None = None
    Type: StrictStr | None = None
    Count: StrictInt | None = None
