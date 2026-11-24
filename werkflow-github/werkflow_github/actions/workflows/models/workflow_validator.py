import datetime
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, BaseModel, ConfigDict, Field, StrictInt, StrictStr

from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status
from werkflow_github.actions.pull_requests.models import PullRequest

from .actor_validator import ActorValidator


class WorkflowValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: StrictInt
    name: StrictStr
    node_id: StrictStr
    check_suite_id: Optional[StrictInt] = None
    check_suite_node_id: Optional[StrictStr] = None
    head_branch: Optional[StrictStr] = None
    head_sha: StrictStr
    path: Optional[StrictStr] = None
    run_number: StrictInt
    event: StrictStr
    display_title: Optional[StrictStr] = None
    status: Status
    conclusion: Optional[Conclusion] = None
    workflow_id: StrictInt
    url: AnyHttpUrl
    html_url: Optional[AnyHttpUrl] = None
    pull_requests: List[PullRequest] = Field(default_factory=list)
    created_at: datetime.datetime
    updated_at: datetime.datetime
    actor: Optional[ActorValidator] = None
    triggering_actor: Optional[ActorValidator] = None
    run_attempt: Optional[StrictInt] = None
    referenced_workflows: Optional[List[Dict[str, Any]]] = None
    run_started_at: Optional[datetime.datetime] = None
    jobs_url: Optional[AnyHttpUrl] = None
    logs_url: Optional[AnyHttpUrl] = None
    check_suite_url: Optional[AnyHttpUrl] = None
    artifacts_url: Optional[AnyHttpUrl] = None
    cancel_url: Optional[AnyHttpUrl] = None
    rerun_url: Optional[AnyHttpUrl] = None
    previous_attempt_url: Optional[AnyHttpUrl] = None
    workflow_url: Optional[AnyHttpUrl] = None
    head_commit: Optional[Dict[str, Any]] = None
    repository: Optional[Dict[str, Any]] = None
    head_repository: Optional[Dict[str, Any]] = None
