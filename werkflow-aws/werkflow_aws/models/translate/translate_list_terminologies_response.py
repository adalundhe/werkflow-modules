from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .translate_terminology_properties import TranslateTerminologyProperties


class TranslateListTerminologiesResponse(BaseModel):
    TerminologyPropertiesList: list[TranslateTerminologyProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
