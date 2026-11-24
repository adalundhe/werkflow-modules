from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKJmxExporterInfo(BaseModel):
    EnabledInBroker: StrictBool | None = None
