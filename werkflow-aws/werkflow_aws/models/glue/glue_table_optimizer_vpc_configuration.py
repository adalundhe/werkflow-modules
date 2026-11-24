from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTableOptimizerVpcConfiguration(BaseModel):
    glueConnectionName: StrictStr | None = None
