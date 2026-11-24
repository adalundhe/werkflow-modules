from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, StrictBool, StrictInt, StrictStr


class ActorValidator(BaseModel):
    login: StrictStr
    id: StrictInt
    node_id: StrictStr
    avatar_url: AnyHttpUrl
    gravatar_id: Optional[StrictStr] = None
    url: AnyHttpUrl
    html_url: AnyHttpUrl
    followers_url: Optional[AnyHttpUrl] = None
    following_url: Optional[StrictStr] = None
    gists_url: Optional[StrictStr] = None
    starred_url: Optional[StrictStr] = None
    subscriptions_url: Optional[AnyHttpUrl] = None
    organizations_url: Optional[AnyHttpUrl] = None
    repos_url: Optional[AnyHttpUrl] = None
    events_url: Optional[StrictStr] = None
    received_events_url: Optional[AnyHttpUrl] = None
    type: StrictStr
    site_admin: StrictBool
