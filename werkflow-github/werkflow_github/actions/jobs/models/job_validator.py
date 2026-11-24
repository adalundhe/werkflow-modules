import datetime
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseModel, ConfigDict, Field, StrictInt, StrictStr

from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status
from werkflow_github.actions.steps.models.step import Step


class JobValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: StrictInt
    run_id: StrictInt
    run_url: AnyHttpUrl
    node_id: StrictStr
    head_sha: StrictStr
    name: StrictStr
    url: AnyHttpUrl
    html_url: AnyHttpUrl
    status: Status
    conclusion: Optional[Conclusion] = None
    started_at: Optional[datetime.datetime] = None
    completed_at: Optional[datetime.datetime] = None
    steps: List[Step] = Field(default_factory=list)
    check_run_url: AnyHttpUrl
    labels: List[StrictStr] = Field(default_factory=list)
    runner_id: Optional[StrictInt] = None
    runner_name: Optional[StrictStr] = None
    runner_group_id: Optional[StrictInt] = None
    runner_group_name: Optional[StrictStr] = None
    workflow_name: Optional[StrictStr] = None
    head_branch: Optional[StrictStr] = None
