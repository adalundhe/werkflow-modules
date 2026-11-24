from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesConnectionAliasAssociation(BaseModel):
    AssociationStatus: StrictStr | None = None
    AssociatedAccountId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ConnectionIdentifier: StrictStr | None = None
