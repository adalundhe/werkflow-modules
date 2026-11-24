from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftCancelResizeRequest(BaseModel):
    ClusterIdentifier: StrictStr
