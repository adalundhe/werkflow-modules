from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_starting_event_batch_condition import GlueStartingEventBatchCondition
from .glue_workflow_graph import GlueWorkflowGraph
from .glue_workflow_run_statistics import GlueWorkflowRunStatistics


class GlueWorkflowRun(BaseModel):
    Name: StrictStr | None = None
    WorkflowRunId: StrictStr | None = None
    PreviousRunId: StrictStr | None = None
    WorkflowRunProperties: dict[StrictStr, StrictStr] | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    Statistics: GlueWorkflowRunStatistics | None = None
    Graph: GlueWorkflowGraph | None = None
    StartingEventBatchCondition: GlueStartingEventBatchCondition | None = None
