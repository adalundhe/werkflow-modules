from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKNodeExporterModel(BaseModel):
    EnabledInBroker: StrictBool | None = None
