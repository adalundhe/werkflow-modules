from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_extraction_definition_not_found_behavior import ConnectExtractionDefinitionNotFoundBehavior


class ConnectExtractionConfiguration(BaseModel):
    PromptHint: StrictStr | None = None
    NotFoundBehavior: ConnectExtractionDefinitionNotFoundBehavior | None = None
