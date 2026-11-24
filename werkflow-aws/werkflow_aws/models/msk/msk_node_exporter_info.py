from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKNodeExporterInfo(BaseModel):
    EnabledInBroker: StrictBool | None = None
