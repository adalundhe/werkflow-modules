from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_workteam import SageMakerWorkteam


class SageMakerDescribeWorkteamResponse(BaseModel):
    Workteam: SageMakerWorkteam | None = None
    ResponseMetadata: dict[str, Any] | None = None
