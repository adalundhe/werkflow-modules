from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .translate_parallel_data_properties import TranslateParallelDataProperties


class TranslateListParallelDataResponse(BaseModel):
    ParallelDataPropertiesList: list[TranslateParallelDataProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
