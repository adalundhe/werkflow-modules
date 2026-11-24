from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_allowed_publishers import LambdaAllowedPublishers
from .lambda_code_signing_policies import LambdaCodeSigningPolicies


class LambdaCreateCodeSigningConfigRequest(BaseModel):
    AllowedPublishers: LambdaAllowedPublishers
    Description: StrictStr | None = None
    CodeSigningPolicies: LambdaCodeSigningPolicies | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
