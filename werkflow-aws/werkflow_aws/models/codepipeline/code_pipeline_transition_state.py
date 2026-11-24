from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class CodePipelineTransitionState(BaseModel):
    enabled: StrictBool | None = None
    lastChangedBy: StrictStr | None = None
    lastChangedAt: datetime.datetime | StrictStr | None = None
    disabledReason: StrictStr | None = None
