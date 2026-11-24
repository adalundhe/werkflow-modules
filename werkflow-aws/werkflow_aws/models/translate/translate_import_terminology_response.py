from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .translate_terminology_data_location import TranslateTerminologyDataLocation
from .translate_terminology_properties import TranslateTerminologyProperties


class TranslateImportTerminologyResponse(BaseModel):
    TerminologyProperties: TranslateTerminologyProperties | None = None
    AuxiliaryDataLocation: TranslateTerminologyDataLocation | None = None
    ResponseMetadata: dict[str, Any] | None = None
