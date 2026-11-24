from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAuthorizerConfig(BaseModel):
    defaultAuthorizerName: StrictStr | None = None
    allowAuthorizerOverride: StrictBool | None = None
