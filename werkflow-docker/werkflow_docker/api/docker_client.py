import asyncio
import docker
import pathlib
import functools
from concurrent.futures import ThreadPoolExecutor
from docker.models.images import Image as DockerImage
from werkflow.env import TimeParser
from werkflow_shell import Shell
from werkflow_system import System
from werkflow_docker.cli import BuildOptions
from werkflow_docker.images import Image
from typing import (
    Union,
    Optional,
    Dict,
    Any,
    List
)


class DockerClient:

    def __init__(self) -> None:
        super().__init__()

        self._shell = Shell()
        self._system = System()

        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )
        self._loop: Union[asyncio.AbstractEventLoop, None] = None
        self._client = docker.DockerClient(
            max_pool_size=self._system.configuration.cores.physical
        )

        self._error: Union[Exception, None] = None

    async def login(
        self,
        registry_url: str,
        registry_user: str,
        registry_password: str,
        reauthorize: bool=True
    ) -> Dict[str, Any]:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.api.login,
                registry_user,
                password=registry_password,
                registry=registry_url,
                reauth=reauthorize
            )
        )
    
    async def build_image_from_file(
        self,
        path: str,
        image: str,
        tag: str='latest',
        target: Optional[str]=None,
        options: Optional[BuildOptions]=None,
        timeout: Optional[str]=None,
        env: Dict[str, str]={}
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if timeout:
            timeout = TimeParser(timeout).time

        image_path = pathlib.Path(path)
        image_absolute_path = await self._shell.to_absolute_path(
            str(image_path)
        )

        command = f'docker build -t {image}:{tag} -f {image_absolute_path}'

        if options is None:
            options = BuildOptions()

        options_string = options.to_string()
        command = f'{command} {options_string}'

        if target:
            command = f'{command} --target {target}'

        command = f'{command} .'

        return await self._shell.run(
            command,
            env=env,
            as_shell=True,
            silent=True
        )

    async def build_image(
        self,
        image: Image,
        force_image_removal: bool=True,
        build_args: Dict[str, str]={},
        no_cache: bool=False,
        no_intermediate_containers: bool=False,
        squash_layers: bool=False,
        platform: Optional[str]=None,
        target: Optional[str]=None,
        labels: Dict[str, str]=None,
        update_base_images: bool=False,
        timeout: Optional[str]=None
    ) -> DockerImage:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            self._executor,
            image.to_file
        )

        current_directory = await self._shell.get_current_directory()


        if timeout:
            timeout = TimeParser(timeout).time

        completed_image, _ = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.build,
                path=current_directory,
                dockerfile=image.filename,
                tag=image.full_name,
                nocache=no_cache,
                rm=no_intermediate_containers,
                timeout=timeout,
                pull=update_base_images,
                labels=labels,
                target=target,
                squash=squash_layers,
                platform=platform,
                buildargs=build_args,
                forcerm=force_image_removal
            )
        )

        return completed_image
    
    async def pull(
        self,
        repository: str,
        image: str,
        tag: str='latest'
    ) -> DockerImage:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        image_fullname = f'{repository}/{image}'
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.pull,
                image_fullname,
                tag=tag
            )
        )
    
    async def tag_image(
        self,
        repository: str,
        image: str,
        tag: str,
        env: Dict[str, str]={}
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        image_fullname = f'{repository}/{image}'

        command = f'docker tag {image_fullname} {tag}'
        return await self._shell.run(
            command,
            env=env,
            as_shell=True,
            silent=True
        )

    async def prune_all_images(
        self,
        env: Dict[str, str]={}
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._shell.run(
            'docker system prune -a -f',
            env=env,
            as_shell=True,
            silent=True
        )

    async def prune_dangling_image(self):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.prune,
                filters={
                    'dangling': True
                }
            )
        )

    async def remove_image(
        self,
        image: str,
        tag: str='latest',
        force: bool=True,
        delete_parents: bool=True
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        image_fullname = f'{image}:{tag}'

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.remove,
                image_fullname,
                force=force,
                noprune=not delete_parents
            )
        )

    async def get_image(
        self,
        image: str,
        tag: str='latest'
    ) -> DockerImage:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        image_fullname = f'{image}:{tag}'

        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.get,
                image_fullname
            )
        )

    async def list_images(
        self,
        repository: Optional[str]=None,
        show_intermediate_layers: bool=False,
        show_dangling: bool=False
    ) -> List[DockerImage]:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.list,
                name=repository,
                all=show_intermediate_layers,
                filters={
                    'dangling': show_dangling
                }
            )
        )

    async def push(
        self,
        repository: str,
        image: str,
        tag: str='latest'
    ):    
        image_fullname = f'{repository}/{image}'
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.images.push,
                image_fullname,
                tag=tag
            )
        )
    
    async def close(self):
        await self._loop.run_in_executor(
            None,
            self._client.close
        )

        self._executor.shutdown()
        await self._shell.close()
        await self._system.close()

    def abort(self):
        self._client.close()
        self._executor.shutdown()
        self._shell.abort()
        self._system.abort()