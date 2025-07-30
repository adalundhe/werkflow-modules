from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaVarCharValue(BaseModel):
    VarCharValue: StrictStr