from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
)


class MSKCloudWatchLogs(BaseModel):
    Enabled: StrictBool = False
    LogGroup: StrictStr | None = None