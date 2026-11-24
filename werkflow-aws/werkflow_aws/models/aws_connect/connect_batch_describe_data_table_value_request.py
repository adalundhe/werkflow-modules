from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_data_table_value_identifier import ConnectDataTableValueIdentifier


class ConnectBatchDescribeDataTableValueRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    Values: list[ConnectDataTableValueIdentifier]
