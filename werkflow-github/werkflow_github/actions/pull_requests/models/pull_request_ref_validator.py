from pydantic import BaseModel, ConfigDict, StrictStr

from werkflow_github.repos.models import RepoRef


class PullRequestRefValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    ref: StrictStr
    sha: StrictStr
    repo: RepoRef
