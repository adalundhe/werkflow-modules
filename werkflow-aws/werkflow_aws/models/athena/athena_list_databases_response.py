from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_database import AthenaDatabase


class AthenaListDatabasesResponse(BaseModel):
    DatabaseList: list[AthenaDatabase]
    NextToken: StrictStr | None = None