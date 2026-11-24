from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_alias_operations import SageMakerAliasOperations


class SageMakerUpdatePipelineVersionRequest(BaseModel):
    PipelineArn: StrictStr
    PipelineVersionId: StrictInt
    PipelineVersionDisplayName: StrictStr | None = None
    PipelineVersionDescription: StrictStr | None = None
    PipelineVersionAliasOperations: SageMakerAliasOperations | None = None
