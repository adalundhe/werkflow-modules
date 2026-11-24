from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightRedshiftIAMParameters(BaseModel):
    RoleArn: StrictStr | None = None
    DatabaseUser: StrictStr | None = None
    DatabaseGroups: list[StrictStr] | None = None
    AutoCreateDatabaseUser: StrictBool | None = None
