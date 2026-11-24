from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class FSxDeleteDataRepositoryAssociationResponse(BaseModel):
    AssociationId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    DeleteDataInFileSystem: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
