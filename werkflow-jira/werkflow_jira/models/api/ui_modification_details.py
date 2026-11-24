from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ui_modification_context_details import UiModificationContextDetails


class UiModificationDetails(BaseModel):
    contexts: list[UiModificationContextDetails] | None = None
    data: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
