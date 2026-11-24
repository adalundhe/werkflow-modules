from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchTmpfs(BaseModel):
    containerPath: StrictStr | None = None
    size: StrictInt | None = None
    mountOptions: list[StrictStr] | None = None
