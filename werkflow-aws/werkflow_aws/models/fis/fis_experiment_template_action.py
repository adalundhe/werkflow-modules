from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateAction(BaseModel):
    actionId: StrictStr | None = None
    description: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    targets: dict[StrictStr, StrictStr] | None = None
    startAfter: list[StrictStr] | None = None
