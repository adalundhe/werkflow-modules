from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FSxDeleteDataRepositoryAssociationRequest(BaseModel):
    AssociationId: StrictStr
    ClientRequestToken: StrictStr | None = None
    DeleteDataInFileSystem: StrictBool | None = None
