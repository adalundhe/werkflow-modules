from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppRunnerListServicesForAutoScalingConfigurationResponse(BaseModel):
    ServiceArnList: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
