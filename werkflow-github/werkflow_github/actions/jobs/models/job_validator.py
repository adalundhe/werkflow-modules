import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    AnyHttpUrl
)
from typing import List
from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status
from werkflow_github.actions.steps.models.step import Step


class JobValidator(BaseModel):
    id: StrictInt
    run_id: StrictInt
    run_url: AnyHttpUrl
    node_id: StrictStr
    head_sha: StrictStr
    name: StrictStr
    url: AnyHttpUrl
    html_url: AnyHttpUrl
    status: Status
    conclusion: Conclusion
    started_at: datetime.datetime
    completed_at: datetime.datetime
    steps: List[Step]
    check_run_url: AnyHttpUrl
    labels: List[StrictStr]
    runner_id: StrictInt
    runner_name: StrictStr
    runner_group_id: StrictInt
    runner_group_name: StrictStr
    workflow_name: StrictStr
    head_branch: StrictStr

    class Config:
        allow_arbitrary_types=True