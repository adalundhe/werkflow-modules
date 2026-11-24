from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_primary_value import ConnectPrimaryValue


class ConnectBatchDeleteDataTableValueFailureResult(BaseModel):
    PrimaryValues: list[ConnectPrimaryValue] | None = None
    AttributeName: StrictStr | None = None
    Message: StrictStr | None = None
