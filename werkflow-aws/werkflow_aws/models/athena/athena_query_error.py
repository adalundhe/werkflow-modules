from pydantic import (
    BaseModel,
    StrictInt,
    StrictBool,
    StrictStr,
)

class AthenaQueryError(BaseModel):
    ErrorCategory: StrictInt
    ErrorType: StrictInt
    Retryable: StrictBool = False
    ErrorMessage: StrictStr