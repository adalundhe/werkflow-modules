from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3RedirectAllRequestsToInput(BaseModel):
    HostName: StrictStr
    Protocol: Literal['http', 'https'] | None = None
