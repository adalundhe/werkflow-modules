from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesImageSourceIdentifier(BaseModel):
    Ec2ImportTaskId: StrictStr | None = None
    ImageBuildVersionArn: StrictStr | None = None
    Ec2ImageId: StrictStr | None = None
