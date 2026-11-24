from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_allowed_publishers import LambdaAllowedPublishers
from .lambda_code_signing_policies import LambdaCodeSigningPolicies


class LambdaUpdateCodeSigningConfigRequest(BaseModel):
    CodeSigningConfigArn: StrictStr
    Description: StrictStr | None = None
    AllowedPublishers: LambdaAllowedPublishers | None = None
    CodeSigningPolicies: LambdaCodeSigningPolicies | None = None
