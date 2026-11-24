from __future__ import annotations
from pydantic import BaseModel
from .lightsail_container_service_ecr_image_puller_role import LightsailContainerServiceECRImagePullerRole


class LightsailPrivateRegistryAccess(BaseModel):
    ecrImagePullerRole: LightsailContainerServiceECRImagePullerRole | None = None
