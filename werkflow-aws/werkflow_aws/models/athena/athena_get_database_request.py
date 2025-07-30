from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetDatabaseRequest(BaseModel):
    CatalogName: StrictStr
    DatabaseName: StrictStr
    WorkGroup: StrictStr | None = None