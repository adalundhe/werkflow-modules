from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_batch_describe_data_table_value_failure_result import ConnectBatchDescribeDataTableValueFailureResult
from .connect_batch_describe_data_table_value_success_result import ConnectBatchDescribeDataTableValueSuccessResult


class ConnectBatchDescribeDataTableValueResponse(BaseModel):
    Successful: list[ConnectBatchDescribeDataTableValueSuccessResult] | None = None
    Failed: list[ConnectBatchDescribeDataTableValueFailureResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
