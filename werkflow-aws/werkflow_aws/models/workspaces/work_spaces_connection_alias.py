from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_connection_alias_association import WorkSpacesConnectionAliasAssociation


class WorkSpacesConnectionAlias(BaseModel):
    ConnectionString: StrictStr | None = None
    AliasId: StrictStr | None = None
    State: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    Associations: list[WorkSpacesConnectionAliasAssociation] | None = None
