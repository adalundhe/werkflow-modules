from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    StrictBool,
    AnyHttpUrl
)


class UserValidator(BaseModel):
    login: StrictStr
    id: StrictInt
    node_id: StrictStr
    avatar_url: AnyHttpUrl
    gravatar_id: StrictStr
    url: AnyHttpUrl
    html_url: AnyHttpUrl
    followers_url: AnyHttpUrl
    following_url: AnyHttpUrl
    gists_url: AnyHttpUrl
    starred_url: AnyHttpUrl
    subscriptions_url: AnyHttpUrl
    organizations_url: AnyHttpUrl
    repos_url: AnyHttpUrl
    events_url: AnyHttpUrl
    type: StrictStr
    site_admin: StrictBool