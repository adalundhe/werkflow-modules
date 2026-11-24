from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerAssociateTrialComponentResponse(BaseModel):
    TrialComponentArn: StrictStr | None = None
    TrialArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
