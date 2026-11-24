from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRContainersConfig(BaseModel):
    JobRunId: StrictStr | None = None
