from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaVersion(BaseModel):
    Version: StrictStr | None = None
    Status: StrictStr | None = None
