from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBFailureException(BaseModel):
    ExceptionName: StrictStr | None = None
    ExceptionDescription: StrictStr | None = None
