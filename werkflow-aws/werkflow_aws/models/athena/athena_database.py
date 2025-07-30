from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaDatabase(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None