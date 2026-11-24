from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VerifiedAccessInstanceOpenVpnClientConfigurationRoute(BaseModel):
    Cidr: StrictStr | None = None
