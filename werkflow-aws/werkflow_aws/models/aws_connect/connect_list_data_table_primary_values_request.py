from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_primary_attribute_value_filter import ConnectPrimaryAttributeValueFilter


class ConnectListDataTablePrimaryValuesRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    RecordIds: list[StrictStr] | None = None
    PrimaryAttributeValues: list[ConnectPrimaryAttributeValueFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
