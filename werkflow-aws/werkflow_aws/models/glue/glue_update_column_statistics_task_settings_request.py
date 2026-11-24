from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueUpdateColumnStatisticsTaskSettingsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    Role: StrictStr | None = None
    Schedule: StrictStr | None = None
    ColumnNameList: list[StrictStr] | None = None
    SampleSize: StrictFloat | StrictInt | None = None
    CatalogID: StrictStr | None = None
    SecurityConfiguration: StrictStr | None = None
