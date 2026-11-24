from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTaskTemplateContactHooks(BaseModel):
    WrapUpFlowId: StrictStr | None = None
