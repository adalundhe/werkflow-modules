from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    StrictBool,
    AnyHttpUrl
)
from typing import Optional, Any, List, Dict, Literal
from .user_validator import UserValidator


class RepoValidator(BaseModel):
    id: StrictInt
    node_id: StrictStr
    name: StrictStr
    full_name: StrictStr
    owner: UserValidator
    private: StrictBool
    html_url: AnyHttpUrl
    description: Optional[StrictStr]=None
    fork: StrictBool
    url: AnyHttpUrl
    archive_url: AnyHttpUrl
    assignees_url: AnyHttpUrl
    blobs_url: AnyHttpUrl
    branches_url: AnyHttpUrl
    collaborators_url: AnyHttpUrl
    comments_url: AnyHttpUrl
    commits_url: AnyHttpUrl
    compare_url: AnyHttpUrl
    contents_url: AnyHttpUrl
    contributors_url: AnyHttpUrl
    deployments_url: AnyHttpUrl
    downloads_url: AnyHttpUrl
    events_url: AnyHttpUrl
    forks_url: AnyHttpUrl
    git_commits_url: AnyHttpUrl
    git_refs_url: AnyHttpUrl
    git_tags_url: AnyHttpUrl
    git_url: StrictStr
    issue_comment_url: AnyHttpUrl
    issue_events_url: AnyHttpUrl
    issues_url: AnyHttpUrl
    keys_url: AnyHttpUrl
    labels_url: AnyHttpUrl
    languages_url: AnyHttpUrl
    merges_url: AnyHttpUrl
    milestones_url: AnyHttpUrl
    notifications_url: AnyHttpUrl
    pulls_url: AnyHttpUrl
    releases_url: AnyHttpUrl
    ssh_url: StrictStr
    stargazers_url: AnyHttpUrl
    statuses_url: AnyHttpUrl
    subscribers_url: AnyHttpUrl
    subscription_url: AnyHttpUrl
    tags_url: AnyHttpUrl
    teams_url: AnyHttpUrl
    trees_url: AnyHttpUrl
    clone_url: AnyHttpUrl
    mirror_url: Optional[AnyHttpUrl]=None
    hooks_url: AnyHttpUrl
    svn_url: AnyHttpUrl
    homepage: Optional[AnyHttpUrl | StrictStr]=None
    language: Optional[Any]=None
    forks_count: StrictInt
    stargazers_count: StrictInt
    is_template: StrictBool
    topics: List[StrictStr]
    has_issues: StrictBool
    has_projects: StrictBool
    has_wiki: StrictBool
    has_pages: StrictBool
    has_downloads: StrictBool
    has_discussions: StrictBool
    archived: StrictBool
    disabled: StrictBool
    visibility: StrictStr
    pushed_at: StrictStr
    created_at: StrictStr
    updated_at: StrictStr
    permissions: Dict[StrictStr, StrictBool]
    security_and_analysis: Dict[
        StrictStr, 
        Dict[
            StrictStr, 
            Literal["enabled", "disabled"]
        ]
    ]
    
    