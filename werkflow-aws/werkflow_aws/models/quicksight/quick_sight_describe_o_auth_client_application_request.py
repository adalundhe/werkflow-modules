from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeOAuthClientApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    OAuthClientApplicationId: StrictStr
