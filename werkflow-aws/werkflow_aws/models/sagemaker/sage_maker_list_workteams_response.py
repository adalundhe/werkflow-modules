from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_workteam import SageMakerWorkteam


class SageMakerListWorkteamsResponse(BaseModel):
    Workteams: list[SageMakerWorkteam] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
