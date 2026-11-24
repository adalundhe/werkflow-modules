from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_api_schema import QBusinessAPISchema


class QBusinessCustomPluginConfiguration(BaseModel):
    description: StrictStr | None = None
    apiSchemaType: StrictStr | None = None
    apiSchema: QBusinessAPISchema | None = None
