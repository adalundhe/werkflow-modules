from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBCsvOptions(BaseModel):
    Delimiter: StrictStr | None = None
    HeaderList: list[StrictStr] | None = None
