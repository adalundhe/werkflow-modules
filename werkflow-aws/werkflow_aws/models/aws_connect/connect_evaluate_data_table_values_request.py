from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_data_table_value_evaluation_set import ConnectDataTableValueEvaluationSet


class ConnectEvaluateDataTableValuesRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    Values: list[ConnectDataTableValueEvaluationSet]
    TimeZone: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
