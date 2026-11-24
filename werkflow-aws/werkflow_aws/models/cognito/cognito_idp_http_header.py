from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPHttpHeader(BaseModel):
    headerName: StrictStr | None = None
    headerValue: StrictStr | None = None
