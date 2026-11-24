from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_hidden_sage_maker_image import SageMakerHiddenSageMakerImage


class SageMakerStudioWebPortalSettings(BaseModel):
    HiddenMlTools: list[StrictStr] | None = None
    HiddenAppTypes: list[StrictStr] | None = None
    HiddenInstanceTypes: list[StrictStr] | None = None
    HiddenSageMakerImageVersionAliases: list[SageMakerHiddenSageMakerImage] | None = None
    ExecutionRoleSessionNameMode: StrictStr | None = None
