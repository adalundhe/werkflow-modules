from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .cloud_front_session_stickiness_config import CloudFrontSessionStickinessConfig


class CloudFrontContinuousDeploymentSingleWeightConfig(BaseModel):
    Weight: StrictFloat | StrictInt | None = None
    SessionStickinessConfig: CloudFrontSessionStickinessConfig | None = None
