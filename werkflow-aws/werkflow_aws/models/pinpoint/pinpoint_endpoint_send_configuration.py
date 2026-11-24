from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointEndpointSendConfiguration(BaseModel):
    BodyOverride: StrictStr | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    RawContent: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    TitleOverride: StrictStr | None = None
