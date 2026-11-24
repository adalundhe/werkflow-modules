from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaKafkaSchemaValidationConfigModel(BaseModel):
    Attribute: StrictStr | None = None
