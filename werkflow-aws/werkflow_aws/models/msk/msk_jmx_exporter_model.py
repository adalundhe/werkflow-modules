from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKJmxExporterModel(BaseModel):
    EnabledInBroker: StrictBool | None = None
