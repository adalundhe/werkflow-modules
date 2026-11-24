from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchEksAttemptContainerDetail(BaseModel):
    name: StrictStr | None = None
    containerID: StrictStr | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
