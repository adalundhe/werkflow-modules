from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .translate_parallel_data_data_location import TranslateParallelDataDataLocation
from .translate_parallel_data_properties import TranslateParallelDataProperties


class TranslateGetParallelDataResponse(BaseModel):
    ParallelDataProperties: TranslateParallelDataProperties | None = None
    DataLocation: TranslateParallelDataDataLocation | None = None
    AuxiliaryDataLocation: TranslateParallelDataDataLocation | None = None
    LatestUpdateAttemptAuxiliaryDataLocation: TranslateParallelDataDataLocation | None = None
    ResponseMetadata: dict[str, Any] | None = None
