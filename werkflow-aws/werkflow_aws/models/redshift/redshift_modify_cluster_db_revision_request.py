from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyClusterDbRevisionRequest(BaseModel):
    ClusterIdentifier: StrictStr
    RevisionTarget: StrictStr
