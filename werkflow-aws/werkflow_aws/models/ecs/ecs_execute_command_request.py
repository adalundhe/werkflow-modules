from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSExecuteCommandRequest(BaseModel):
    command: StrictStr
    interactive: StrictBool
    task: StrictStr
    cluster: StrictStr | None = None
    container: StrictStr | None = None
