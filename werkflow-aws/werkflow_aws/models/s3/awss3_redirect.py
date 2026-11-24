from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3Redirect(BaseModel):
    HostName: StrictStr | None = None
    HttpRedirectCode: StrictStr | None = None
    Protocol: Literal['http', 'https'] | None = None
    ReplaceKeyPrefixWith: StrictStr | None = None
    ReplaceKeyWith: StrictStr | None = None
