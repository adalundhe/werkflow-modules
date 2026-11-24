from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeAwsLogSourceResource(BaseModel):
    sourceName: StrictStr | None = None
    sourceVersion: StrictStr | None = None
