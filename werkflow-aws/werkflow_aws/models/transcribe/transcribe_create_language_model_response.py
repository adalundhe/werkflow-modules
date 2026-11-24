from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_input_data_config import TranscribeInputDataConfig


class TranscribeCreateLanguageModelResponse(BaseModel):
    LanguageCode: StrictStr | None = None
    BaseModelName: StrictStr | None = None
    ModelName: StrictStr | None = None
    InputDataConfig: TranscribeInputDataConfig | None = None
    ModelStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
