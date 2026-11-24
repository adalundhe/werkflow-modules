from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESListEmailIdentityCertificatesRequest(BaseModel):
    EmailIdentity: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
