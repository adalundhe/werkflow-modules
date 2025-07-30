from pydantic import (
    BaseModel,
    StrictBool,
)

class AthenaResultReuseInformation(BaseModel):
    ReusedPreviousResult: StrictBool = False