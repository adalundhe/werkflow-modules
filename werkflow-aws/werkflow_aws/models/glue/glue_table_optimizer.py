from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_table_optimizer_configuration import GlueTableOptimizerConfiguration
from .glue_table_optimizer_run import GlueTableOptimizerRun


class GlueTableOptimizer(BaseModel):
    type: StrictStr | None = None
    configuration: GlueTableOptimizerConfiguration | None = None
    lastRun: GlueTableOptimizerRun | None = None
    configurationSource: StrictStr | None = None
