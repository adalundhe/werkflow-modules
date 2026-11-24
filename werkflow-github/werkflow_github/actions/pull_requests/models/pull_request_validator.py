from pydantic import AnyHttpUrl, BaseModel, ConfigDict, StrictInt

from .pull_request_ref import PullRequestRef


class PullRequestValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: StrictInt
    number: StrictInt
    url: AnyHttpUrl
    head: PullRequestRef
    base: PullRequestRef
