from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mq_engine_version import MQEngineVersion


class MQBrokerEngineType(BaseModel):
    EngineType: StrictStr | None = None
    EngineVersions: list[MQEngineVersion] | None = None
