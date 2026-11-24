from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_data_table_value import ConnectDataTableValue


class ConnectBatchUpdateDataTableValueRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    Values: list[ConnectDataTableValue]
