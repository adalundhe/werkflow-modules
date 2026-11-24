from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_batch_update_data_table_value_failure_result import ConnectBatchUpdateDataTableValueFailureResult
from .connect_batch_update_data_table_value_success_result import ConnectBatchUpdateDataTableValueSuccessResult


class ConnectBatchUpdateDataTableValueResponse(BaseModel):
    Successful: list[ConnectBatchUpdateDataTableValueSuccessResult] | None = None
    Failed: list[ConnectBatchUpdateDataTableValueFailureResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
