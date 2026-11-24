from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteOAuthClientApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    OAuthClientApplicationId: StrictStr
