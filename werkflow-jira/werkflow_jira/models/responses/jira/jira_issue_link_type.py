from pydantic import AnyHttpUrl, BaseModel, StrictStr


class JiraIssueLinkType(BaseModel):
    id: StrictStr
    inward: StrictStr
    name: StrictStr
    outward: StrictStr
    self: AnyHttpUrl | None = None
