from __future__ import annotations
from pydantic import BaseModel
from .x_ray_annotation_value import XRayAnnotationValue
from .x_ray_service_id import XRayServiceId


class XRayValueWithServiceIds(BaseModel):
    AnnotationValue: XRayAnnotationValue | None = None
    ServiceIds: list[XRayServiceId] | None = None
