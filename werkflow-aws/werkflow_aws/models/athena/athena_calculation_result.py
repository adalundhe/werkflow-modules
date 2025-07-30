from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaCalculationResult(BaseModel):
    StdOutS3Uri: StrictStr
    StdErrorS3Uri: StrictStr
    ResultS3Uri: StrictStr
    ResultType: StrictStr