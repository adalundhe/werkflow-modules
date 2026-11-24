from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAnnotationConsolidationConfig(BaseModel):
    AnnotationConsolidationLambdaArn: StrictStr | None = None
