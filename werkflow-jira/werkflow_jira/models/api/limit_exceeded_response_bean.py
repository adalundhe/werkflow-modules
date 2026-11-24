from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LimitExceededResponseBean(BaseModel):
    current_count: StrictInt | None = None
    entity_type: StrictStr | None = None
    error_code: StrictStr | None = None
    limit_type: StrictStr | None = None
    max_allowed_limit: StrictInt | None = None
    message: StrictStr | None = None
    scope_id: StrictStr | None = None
