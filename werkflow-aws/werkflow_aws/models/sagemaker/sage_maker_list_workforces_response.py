from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_workforce import SageMakerWorkforce


class SageMakerListWorkforcesResponse(BaseModel):
    Workforces: list[SageMakerWorkforce] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
