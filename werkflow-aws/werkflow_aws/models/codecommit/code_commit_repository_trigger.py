from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitRepositoryTrigger(BaseModel):
    name: StrictStr | None = None
    destinationArn: StrictStr | None = None
    customData: StrictStr | None = None
    branches: list[StrictStr] | None = None
    events: list[StrictStr] | None = None
