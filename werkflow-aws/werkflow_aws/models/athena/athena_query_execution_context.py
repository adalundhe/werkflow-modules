from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaQueryExecutionContext(BaseModel):
    Database: StrictStr
    Catalog: StrictStr