from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_cloud_trail_details import AccessAnalyzerCloudTrailDetails
from .access_analyzer_policy_generation_details import AccessAnalyzerPolicyGenerationDetails


class AccessAnalyzerStartPolicyGenerationRequest(BaseModel):
    policyGenerationDetails: AccessAnalyzerPolicyGenerationDetails
    cloudTrailDetails: AccessAnalyzerCloudTrailDetails | None = None
    clientToken: StrictStr | None = None
