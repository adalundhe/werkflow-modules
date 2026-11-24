from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectConnectDescribeConnectionLoaRequest(BaseModel):
    connectionId: StrictStr
    providerName: StrictStr | None = None
    loaContentType: Literal['application/pdf'] | None = None
