from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueJDBCConnectorOptions(BaseModel):
    FilterPredicate: StrictStr | None = None
    PartitionColumn: StrictStr | None = None
    LowerBound: StrictInt | None = None
    UpperBound: StrictInt | None = None
    NumPartitions: StrictInt | None = None
    JobBookmarkKeys: list[StrictStr] | None = None
    JobBookmarkKeysSortOrder: StrictStr | None = None
    DataTypeMapping: dict[StrictStr, StrictStr] | None = None
