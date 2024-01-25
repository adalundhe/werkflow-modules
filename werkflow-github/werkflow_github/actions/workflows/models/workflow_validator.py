import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    AnyHttpUrl
)
from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status
from werkflow_github.actions.pull_requests.models.pull_request_validator import PullRequest
from typing import Optional, List


class WorkflowValidator(BaseModel):
    id: StrictInt
    name: StrictStr
    node_id: StrictStr
    check_suite_id: StrictInt
    check_suite_node_id: StrictStr
    head_branch: StrictStr
    headh_sha: StrictStr
    path: StrictStr
    run_number: StrictInt
    event: StrictStr
    display_title: StrictStr
    status: Status
    conclusion: Optional[Conclusion]=None
    workflow_id: StrictInt
    url: AnyHttpUrl
    html_url: AnyHttpUrl
    pull_requests: List[PullRequest]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    