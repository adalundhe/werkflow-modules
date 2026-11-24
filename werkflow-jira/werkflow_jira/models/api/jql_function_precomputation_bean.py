from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlFunctionPrecomputationBean(BaseModel):
    arguments: list[StrictStr] | None = None
    created: StrictStr | None = None
    error: StrictStr | None = None
    field: StrictStr | None = None
    functionKey: StrictStr | None = None
    functionName: StrictStr | None = None
    id: StrictStr | None = None
    operator: StrictStr | None = None
    updated: StrictStr | None = None
    used: StrictStr | None = None
    value: StrictStr | None = None
