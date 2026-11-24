from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESPutEmailIdentityMailFromAttributesRequest(BaseModel):
    EmailIdentity: StrictStr
    MailFromDomain: StrictStr | None = None
    BehaviorOnMxFailure: Literal['USE_DEFAULT_VALUE', 'REJECT_MESSAGE'] | None = None
