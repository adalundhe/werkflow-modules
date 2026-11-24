from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_workforce import SageMakerWorkforce


class SageMakerUpdateWorkforceResponse(BaseModel):
    Workforce: SageMakerWorkforce | None = None
    ResponseMetadata: dict[str, Any] | None = None
