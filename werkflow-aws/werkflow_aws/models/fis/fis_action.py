from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_action_parameter import FISActionParameter
from .fis_action_target import FISActionTarget


class FISAction(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    parameters: dict[StrictStr, FISActionParameter] | None = None
    targets: dict[StrictStr, FISActionTarget] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
