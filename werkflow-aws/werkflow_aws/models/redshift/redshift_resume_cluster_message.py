from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftResumeClusterMessage(BaseModel):
    ClusterIdentifier: StrictStr | None = None
