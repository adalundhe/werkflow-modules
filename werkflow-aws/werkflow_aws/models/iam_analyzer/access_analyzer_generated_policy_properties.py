from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .access_analyzer_cloud_trail_properties import AccessAnalyzerCloudTrailProperties


class AccessAnalyzerGeneratedPolicyProperties(BaseModel):
    isComplete: StrictBool | None = None
    principalArn: StrictStr | None = None
    cloudTrailProperties: AccessAnalyzerCloudTrailProperties | None = None
