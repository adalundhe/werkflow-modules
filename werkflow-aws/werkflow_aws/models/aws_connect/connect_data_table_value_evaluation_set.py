from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_primary_value import ConnectPrimaryValue


class ConnectDataTableValueEvaluationSet(BaseModel):
    AttributeNames: list[StrictStr]
    PrimaryValues: list[ConnectPrimaryValue] | None = None
