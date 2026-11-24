from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_batch_create_data_table_value_failure_result import ConnectBatchCreateDataTableValueFailureResult
from .connect_batch_create_data_table_value_success_result import ConnectBatchCreateDataTableValueSuccessResult


class ConnectBatchCreateDataTableValueResponse(BaseModel):
    Successful: list[ConnectBatchCreateDataTableValueSuccessResult] | None = None
    Failed: list[ConnectBatchCreateDataTableValueFailureResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
