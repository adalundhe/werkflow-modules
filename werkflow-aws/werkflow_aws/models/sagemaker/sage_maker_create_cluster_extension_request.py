from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateClusterExtensionRequest(BaseModel):
    ClusterArn: StrictStr
    ExtensionName: StrictStr
    ExtensionVersion: StrictStr | None = None
    ConfigurationValues: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ClientToken: StrictStr | None = None
