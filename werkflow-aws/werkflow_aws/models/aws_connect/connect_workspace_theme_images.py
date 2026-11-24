from __future__ import annotations
from pydantic import BaseModel
from .connect_images_logo import ConnectImagesLogo


class ConnectWorkspaceThemeImages(BaseModel):
    Logo: ConnectImagesLogo | None = None
