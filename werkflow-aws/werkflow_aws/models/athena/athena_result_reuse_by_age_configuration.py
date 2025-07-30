from pydantic import (
    BaseModel,
    StrictBool,
    StrictInt
)


class AthenaResultReuseByAgeConfiguration(BaseModel):
    Enabled: StrictBool = False
    MaxAgeInMinutes: StrictInt