from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingSubmitRegistrationVersionRequest(BaseModel):
    RegistrationId: StrictStr
    AwsReview: StrictBool | None = None
