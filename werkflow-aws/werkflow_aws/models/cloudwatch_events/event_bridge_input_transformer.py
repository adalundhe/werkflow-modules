from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeInputTransformer(BaseModel):
    InputPathsMap: dict[StrictStr, StrictStr] | None = None
    InputTemplate: StrictStr | None = None
