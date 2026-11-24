from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerLinkAssociation(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    DeviceId: StrictStr | None = None
    LinkId: StrictStr | None = None
    LinkAssociationState: StrictStr | None = None
