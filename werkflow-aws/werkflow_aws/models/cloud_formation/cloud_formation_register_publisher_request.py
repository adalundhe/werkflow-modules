from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationRegisterPublisherRequest(BaseModel):
    AcceptTermsAndConditions: StrictBool | None = None
    ConnectionArn: StrictStr | None = None
