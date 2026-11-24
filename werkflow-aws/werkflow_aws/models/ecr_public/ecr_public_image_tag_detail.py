from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecr_public_referenced_image_detail import ECRPublicReferencedImageDetail


class ECRPublicImageTagDetail(BaseModel):
    imageTag: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    imageDetail: ECRPublicReferencedImageDetail | None = None
