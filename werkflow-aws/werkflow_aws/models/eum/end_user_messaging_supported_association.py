from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSupportedAssociation(BaseModel):
    ResourceType: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    AssociationBehavior: StrictStr | None = None
    DisassociationBehavior: StrictStr | None = None
