from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaCalculationConfiguration(BaseModel):
    CodeBlock: StrictStr