from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectGatewayAttachment(BaseModel):
    directConnectGatewayId: StrictStr | None = None
    virtualInterfaceId: StrictStr | None = None
    virtualInterfaceRegion: StrictStr | None = None
    virtualInterfaceOwnerAccount: StrictStr | None = None
    attachmentState: StrictStr | None = None
    attachmentType: StrictStr | None = None
    stateChangeError: StrictStr | None = None
