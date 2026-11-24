from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_statistic_model_result import GlueStatisticModelResult


class GlueGetDataQualityModelResultResponse(BaseModel):
    CompletedOn: datetime.datetime | StrictStr | None = None
    Model: list[GlueStatisticModelResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
