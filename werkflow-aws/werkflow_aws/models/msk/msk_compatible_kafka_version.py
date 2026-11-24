from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKCompatibleKafkaVersion(BaseModel):
    SourceVersion: StrictStr | None = None
    TargetVersions: list[StrictStr] | None = None
