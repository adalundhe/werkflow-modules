from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexDialogAction(BaseModel):
    type: StrictStr | None = None
    slotToElicit: StrictStr | None = None
    suppressNextMessage: StrictBool | None = None
