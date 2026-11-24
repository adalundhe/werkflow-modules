from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_app_details import SageMakerAppDetails


class SageMakerListAppsResponse(BaseModel):
    Apps: list[SageMakerAppDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
