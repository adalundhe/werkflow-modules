from pydantic import (
    BaseModel,
    StrictStr
)
from werkflow_github.actions.repo.models import RepoRef


class PullRequestRefValidator(BaseModel):
    ref: StrictStr
    sha: StrictStr
    repo: RepoRef


