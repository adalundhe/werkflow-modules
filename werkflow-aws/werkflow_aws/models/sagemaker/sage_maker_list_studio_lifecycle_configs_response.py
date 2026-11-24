from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_studio_lifecycle_config_details import SageMakerStudioLifecycleConfigDetails


class SageMakerListStudioLifecycleConfigsResponse(BaseModel):
    NextToken: StrictStr | None = None
    StudioLifecycleConfigs: list[SageMakerStudioLifecycleConfigDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
