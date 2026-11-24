from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3RedirectAllRequestsTo(BaseModel):
    HostName: StrictStr | None = None
    Protocol: Literal['http', 'https'] | None = None
