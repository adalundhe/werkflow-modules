from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectConnectDescribeInterconnectLoaRequest(BaseModel):
    interconnectId: StrictStr
    providerName: StrictStr | None = None
    loaContentType: Literal['application/pdf'] | None = None
