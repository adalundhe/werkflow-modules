from typing import Any, Dict, List, Literal, Optional

from pydantic import AnyHttpUrl, BaseModel, Field, StrictBool, StrictInt, StrictStr

from .user_validator import UserValidator


class RepoValidator(BaseModel):
    id: StrictInt
    node_id: StrictStr
    name: StrictStr
    full_name: StrictStr
    owner: UserValidator
    private: StrictBool
    html_url: AnyHttpUrl
    description: Optional[StrictStr] = None
    fork: StrictBool
    url: AnyHttpUrl
    archive_url: Optional[StrictStr] = None
    assignees_url: Optional[StrictStr] = None
    blobs_url: Optional[StrictStr] = None
    branches_url: Optional[StrictStr] = None
    collaborators_url: Optional[StrictStr] = None
    comments_url: Optional[StrictStr] = None
    commits_url: Optional[StrictStr] = None
    compare_url: Optional[StrictStr] = None
    contents_url: Optional[StrictStr] = None
    contributors_url: Optional[StrictStr] = None
    deployments_url: Optional[StrictStr] = None
    downloads_url: Optional[StrictStr] = None
    events_url: Optional[StrictStr] = None
    forks_url: Optional[StrictStr] = None
    git_commits_url: Optional[StrictStr] = None
    git_refs_url: Optional[StrictStr] = None
    git_tags_url: Optional[StrictStr] = None
    git_url: Optional[StrictStr] = None
    issue_comment_url: Optional[StrictStr] = None
    issue_events_url: Optional[StrictStr] = None
    issues_url: Optional[StrictStr] = None
    keys_url: Optional[StrictStr] = None
    labels_url: Optional[StrictStr] = None
    languages_url: Optional[StrictStr] = None
    merges_url: Optional[StrictStr] = None
    milestones_url: Optional[StrictStr] = None
    notifications_url: Optional[StrictStr] = None
    pulls_url: Optional[StrictStr] = None
    releases_url: Optional[StrictStr] = None
    ssh_url: Optional[StrictStr] = None
    stargazers_url: Optional[StrictStr] = None
    statuses_url: Optional[StrictStr] = None
    subscribers_url: Optional[StrictStr] = None
    subscription_url: Optional[StrictStr] = None
    tags_url: Optional[StrictStr] = None
    teams_url: Optional[StrictStr] = None
    trees_url: Optional[StrictStr] = None
    clone_url: Optional[AnyHttpUrl] = None
    mirror_url: Optional[StrictStr] = None
    hooks_url: Optional[AnyHttpUrl] = None
    svn_url: Optional[AnyHttpUrl] = None
    homepage: Optional[AnyHttpUrl | StrictStr] = None
    language: Optional[Any] = None
    forks_count: Optional[StrictInt] = None
    stargazers_count: Optional[StrictInt] = None
    is_template: Optional[StrictBool] = None
    topics: List[StrictStr] = Field(default_factory=list)
    has_issues: Optional[StrictBool] = None
    has_projects: Optional[StrictBool] = None
    has_wiki: Optional[StrictBool] = None
    has_pages: Optional[StrictBool] = None
    has_downloads: Optional[StrictBool] = None
    has_discussions: Optional[StrictBool] = None
    archived: Optional[StrictBool] = None
    disabled: Optional[StrictBool] = None
    visibility: Optional[StrictStr] = None
    pushed_at: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    permissions: Optional[Dict[StrictStr, StrictBool]] = None
    security_and_analysis: Optional[
        Dict[
            StrictStr,
            Dict[
                StrictStr,
                Literal['enabled', 'disabled'],
            ],
        ]
    ] = None
