from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMFailureDetails(BaseModel):
    FailureStage: StrictStr | None = None
    FailureType: StrictStr | None = None
    Details: dict[StrictStr, list[StrictStr]] | None = None
