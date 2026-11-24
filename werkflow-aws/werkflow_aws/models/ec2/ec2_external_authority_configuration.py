from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2ExternalAuthorityConfiguration(BaseModel):
    Type: Literal['infoblox'] | None = None
    ExternalResourceIdentifier: StrictStr | None = None
