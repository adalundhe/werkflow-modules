from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_key_value_pair import ECSKeyValuePair


class ECSProxyConfiguration(BaseModel):
    type: StrictStr | None = None
    containerName: StrictStr | None = None
    properties: list[ECSKeyValuePair] | None = None
