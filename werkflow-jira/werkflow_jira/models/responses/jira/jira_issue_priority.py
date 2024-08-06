from pydantic import AnyHttpUrl, BaseModel, StrictStr


class JiraIssuePriority(BaseModel):
    description: StrictStr
    iconUrl: StrictStr
    id: StrictStr
    name: StrictStr
    self: AnyHttpUrl
    statusColor: StrictStr
