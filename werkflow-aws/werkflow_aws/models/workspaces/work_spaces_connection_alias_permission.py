from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkSpacesConnectionAliasPermission(BaseModel):
    SharedAccountId: StrictStr | None = None
    AllowAssociation: StrictBool | None = None
