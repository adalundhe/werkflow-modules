from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_use_case import ConnectUseCase


class ConnectListUseCasesResponse(BaseModel):
    UseCaseSummaryList: list[ConnectUseCase] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
