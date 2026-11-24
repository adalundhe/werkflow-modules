from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectSignInDistribution(BaseModel):
    Region: StrictStr | None = None
    Enabled: StrictBool | None = None
