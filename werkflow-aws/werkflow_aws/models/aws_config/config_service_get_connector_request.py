from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGetConnectorRequest(BaseModel):
    Arn: StrictStr
