from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_data_table_delete_value_identifier import ConnectDataTableDeleteValueIdentifier


class ConnectBatchDeleteDataTableValueRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    Values: list[ConnectDataTableDeleteValueIdentifier]
