from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_subscribed_workteam import SageMakerSubscribedWorkteam


class SageMakerDescribeSubscribedWorkteamResponse(BaseModel):
    SubscribedWorkteam: SageMakerSubscribedWorkteam | None = None
    ResponseMetadata: dict[str, Any] | None = None
