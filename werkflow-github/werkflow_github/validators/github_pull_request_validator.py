from pydantic import BaseModel, StrictStr


class GithubPullRequest(BaseModel):
    title: StrictStr
    body: StrictStr
    head: StrictStr
    base: StrictStr