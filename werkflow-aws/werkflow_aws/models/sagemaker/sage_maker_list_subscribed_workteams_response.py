from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_subscribed_workteam import SageMakerSubscribedWorkteam


class SageMakerListSubscribedWorkteamsResponse(BaseModel):
    SubscribedWorkteams: list[SageMakerSubscribedWorkteam] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
