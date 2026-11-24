from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDescribeBotResourceGenerationResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    generationId: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    generationStatus: StrictStr | None = None
    generationInputPrompt: StrictStr | None = None
    generatedBotLocaleUrl: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    modelArn: StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
