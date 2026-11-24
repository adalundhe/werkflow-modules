from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESContactListDestination(BaseModel):
    ContactListName: StrictStr | None = None
    ContactListImportAction: StrictStr | None = None
