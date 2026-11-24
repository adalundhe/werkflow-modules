from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_blueprint_details import GlueBlueprintDetails
from .glue_workflow_graph import GlueWorkflowGraph
from .glue_workflow_run import GlueWorkflowRun


class GlueWorkflow(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultRunProperties: dict[StrictStr, StrictStr] | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    LastRun: GlueWorkflowRun | None = None
    Graph: GlueWorkflowGraph | None = None
    MaxConcurrentRuns: StrictInt | None = None
    BlueprintDetails: GlueBlueprintDetails | None = None
