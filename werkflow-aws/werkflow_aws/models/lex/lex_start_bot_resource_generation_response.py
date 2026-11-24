from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexStartBotResourceGenerationResponse(BaseModel):
    generationInputPrompt: StrictStr | None = None
    generationId: StrictStr | None = None
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    generationStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
