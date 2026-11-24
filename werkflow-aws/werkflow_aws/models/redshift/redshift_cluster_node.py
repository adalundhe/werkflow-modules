from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterNode(BaseModel):
    NodeRole: StrictStr | None = None
    PrivateIPAddress: StrictStr | None = None
    PublicIPAddress: StrictStr | None = None
