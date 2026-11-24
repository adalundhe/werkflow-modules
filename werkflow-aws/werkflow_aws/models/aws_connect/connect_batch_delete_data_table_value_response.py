from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_batch_delete_data_table_value_failure_result import ConnectBatchDeleteDataTableValueFailureResult
from .connect_batch_delete_data_table_value_success_result import ConnectBatchDeleteDataTableValueSuccessResult


class ConnectBatchDeleteDataTableValueResponse(BaseModel):
    Successful: list[ConnectBatchDeleteDataTableValueSuccessResult] | None = None
    Failed: list[ConnectBatchDeleteDataTableValueFailureResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
