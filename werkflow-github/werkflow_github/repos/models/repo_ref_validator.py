from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    AnyHttpUrl
)


class RepoRefValidator(BaseModel):
    id: StrictInt
    url: AnyHttpUrl
    name: StrictStr



