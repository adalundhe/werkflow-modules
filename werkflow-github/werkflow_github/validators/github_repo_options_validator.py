from pydantic import BaseModel, StrictStr, StrictBool
from typing import Optional


class GithubRepoOptions(BaseModel):
    name: StrictStr
    description: StrictStr
    homepage: StrictStr
    private: StrictBool=True
    visibility: StrictStr='private'
    has_issues: StrictBool=True
    has_projects: StrictBool=True
    has_wiki: StrictBool=True
    team_id: Optional[StrictStr]