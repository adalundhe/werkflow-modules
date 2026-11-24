from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListPhoneNumbersOptedOutRequest(BaseModel):
    nextToken: StrictStr | None = None
