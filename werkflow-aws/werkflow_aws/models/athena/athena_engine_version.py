from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaEngineVersion(BaseModel):
    SelectedEngineVersion: StrictStr
    EffectiveEngineVersion: StrictStr