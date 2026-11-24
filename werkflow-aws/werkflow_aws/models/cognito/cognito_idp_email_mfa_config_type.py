from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPEmailMfaConfigType(BaseModel):
    Message: StrictStr | None = None
    Subject: StrictStr | None = None
