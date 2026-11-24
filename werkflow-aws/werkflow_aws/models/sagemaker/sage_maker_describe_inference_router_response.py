from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_routing_target import SageMakerRoutingTarget


class SageMakerDescribeInferenceRouterResponse(BaseModel):
    InferenceRouterName: StrictStr | None = None
    InferenceRouterArn: StrictStr | None = None
    RoutingTargets: list[SageMakerRoutingTarget] | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
