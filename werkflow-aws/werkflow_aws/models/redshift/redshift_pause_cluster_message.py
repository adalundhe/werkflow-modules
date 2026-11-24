from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftPauseClusterMessage(BaseModel):
    ClusterIdentifier: StrictStr | None = None
