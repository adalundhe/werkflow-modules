from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_parallel_data_config import TranslateParallelDataConfig


class TranslateUpdateParallelDataRequest(BaseModel):
    Name: StrictStr
    ParallelDataConfig: TranslateParallelDataConfig
    ClientToken: StrictStr
    Description: StrictStr | None = None
