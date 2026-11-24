from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMModifyDocumentPermissionRequest(BaseModel):
    Name: StrictStr
    PermissionType: Literal['Share']
    AccountIdsToAdd: list[StrictStr] | None = None
    AccountIdsToRemove: list[StrictStr] | None = None
    SharedDocumentVersion: StrictStr | None = None
