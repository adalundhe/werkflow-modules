from pydantic import (
    BaseModel,
    StrictStr,
)


class MSKStateInfo(BaseModel):
    Code: StrictStr
    Message: StrictStr