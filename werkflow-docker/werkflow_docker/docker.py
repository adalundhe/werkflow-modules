from werkflow.modules.base import Module
from werkflow.modules import Shell
from typing import Dict, Optional
from .api import DockerClient
from .images import Image


class Docker(Module):

    def __init__(self) -> None:
        super().__init__()

        self._shell = Shell()

        self.client = DockerClient()
        self.images: Dict[str, Image] = {}

    async def load_image(
        self,
        path: str,
        image_name: Optional[str]=None,
        image_tag: Optional[str]='latest'
    ):
        if image_tag is None:
            image_tag = 'latest'


        if image_name is None:
            image_data = await self._shell.read_file(
                path,
                silent=True
            )

            return Image.generate_from_string(
                image_data,
                output_path=path
            )

        else:
            image = Image(
                image_name,
                tag=image_tag,
                path=path
            )
            
            image_data = await self._shell.read_file(
                path,
                silent=True
            )

            image.from_string(image_data)
            self.images[image_name] = image

            return image

    async def close(self):
        await self.client.close()
        await self._shell.close()

    def abort(self):
        self.client.abort()
        self._shell.abort()