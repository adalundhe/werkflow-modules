from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueCreateColumnStatisticsTaskSettingsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    Role: StrictStr
    Schedule: StrictStr | None = None
    ColumnNameList: list[StrictStr] | None = None
    SampleSize: StrictFloat | StrictInt | None = None
    CatalogID: StrictStr | None = None
    SecurityConfiguration: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
