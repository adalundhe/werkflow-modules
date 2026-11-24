from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_edit_action_error import BulkEditActionError


class BulkEditShareableEntityResponse(BaseModel):
    action: StrictStr | None = None
    entityErrors: dict[StrictStr, BulkEditActionError] | None = None
