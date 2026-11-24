import asyncio
import functools
import os
import pathlib
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Union

import docker
from docker.errors import DockerException
from docker.models.images import Image as DockerImage
from werkflow_shell import Shell
from werkflow_system import System

from werkflow_docker.cli import BuildOptions
from werkflow_docker.images import Image

try:
    from werkflow.env import TimeParser as _TimeParser
except ImportError:
    _TimeParser = None

_DURATION_PART_PATTERN = re.compile(r'(\d+(?:\.\d+)?)(ms|s|m|h|d)')
_DURATION_MULTIPLIERS: Dict[str, float] = {
    'ms': 0.001,
    's': 1.0,
    'm': 60.0,
    'h': 3600.0,
    'd': 86400.0,
}


def parse_duration(timeout: Optional[Union[str, int, float]]) -> Optional[float]:
    if timeout is None:
        return None

    if isinstance(timeout, bool):
        raise ValueError(f'Invalid timeout duration: {timeout!r}')

    if isinstance(timeout, (int, float)):
        return float(timeout)

    raw = timeout.strip().lower()
    if not raw:
        raise ValueError(f'Invalid timeout duration: {timeout!r}')

    if re.fullmatch(r'\d+(?:\.\d+)?', raw):
        return float(raw)

    total = 0.0
    pos = 0
    for match in _DURATION_PART_PATTERN.finditer(raw):
        if match.start() != pos:
            pos = -1
            break
        value = float(match.group(1))
        unit = match.group(2)
        total += value * _DURATION_MULTIPLIERS[unit]
        pos = match.end()

    if pos == len(raw) and pos > 0:
        return total

    if _TimeParser is not None:
        try:
            parsed = _TimeParser(timeout).time
            if isinstance(parsed, (int, float)):
                return float(parsed)
        except Exception:
            pass

    raise ValueError(f'Invalid timeout duration: {timeout!r}')


class DockerClient:

    def __init__(self) -> None:
        super().__init__()

        self._shell = Shell()
        self._system = System()

        max_workers = max(1, self._system.configuration.cores.physical or 1)
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._client: Optional[docker.DockerClient] = None
        self._error: Optional[Exception] = None

        try:
            self._client = self._create_client()
        except Exception as err:
            self._error = err

    def _create_client(self) -> docker.DockerClient:
        max_pool_size = max(1, self._system.configuration.cores.physical or 1)
        if os.environ.get('DOCKER_HOST'):
            return docker.from_env(max_pool_size=max_pool_size)

        try:
            return docker.from_env(max_pool_size=max_pool_size)
        except DockerException:
            return docker.DockerClient(max_pool_size=max_pool_size)

    def _get_client(self) -> docker.DockerClient:
        if self._client is None:
            self._client = self._create_client()
            self._error = None
        return self._client

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_running_loop()
        return self._loop

    async def login(
        self,
        registry_url: str,
        registry_user: str,
        registry_password: str,
        reauthorize: bool = True,
    ) -> Dict[str, Any]:
        loop = self._get_loop()
        client = self._get_client()

        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.api.login,
                registry_user,
                password=registry_password,
                registry=registry_url,
                reauth=reauthorize,
            ),
        )

    async def build_image_from_file(
        self,
        path: str,
        image: str,
        tag: str = 'latest',
        target: Optional[str] = None,
        options: Optional[BuildOptions] = None,
        timeout: Optional[Union[str, int, float]] = None,
        env: Optional[Dict[str, str]] = None,
    ) -> subprocess.CompletedProcess[str]:
        self._get_loop()

        parsed_timeout = parse_duration(timeout)

        image_path = pathlib.Path(path)
        image_absolute_path = await self._shell.to_absolute_path(
            str(image_path)
        )

        command = f'docker build -t {image}:{tag} -f {image_absolute_path}'

        if options is None:
            options = BuildOptions()

        options_string = options.to_string().strip()
        if options_string:
            command = f'{command} {options_string}'

        if target:
            command = f'{command} --target {target}'

        command = f'{command} .'

        return await self._shell.run(
            command,
            env=env,
            as_shell=True,
            silent=True,
            timeout=parsed_timeout,
        )

    async def build_image(
        self,
        image: Image,
        force_image_removal: bool = True,
        build_args: Optional[Dict[str, str]] = None,
        no_cache: bool = False,
        no_intermediate_containers: bool = False,
        squash_layers: bool = False,
        platform: Optional[str] = None,
        target: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        update_base_images: bool = False,
        timeout: Optional[Union[str, int, float]] = None,
    ) -> DockerImage:
        loop = self._get_loop()
        client = self._get_client()

        await loop.run_in_executor(
            self._executor,
            image.to_file,
        )

        current_directory = await self._shell.get_current_directory()

        parsed_timeout = parse_duration(timeout)
        docker_timeout: Optional[int] = (
            int(parsed_timeout) if parsed_timeout is not None else None
        )

        completed_image, _ = await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.build,
                path=current_directory,
                dockerfile=image.filename,
                tag=image.full_name,
                nocache=no_cache,
                rm=no_intermediate_containers,
                timeout=docker_timeout,
                pull=update_base_images,
                labels=labels,
                target=target,
                squash=squash_layers,
                platform=platform,
                buildargs=build_args or {},
                forcerm=force_image_removal,
            ),
        )

        return completed_image

    async def pull(
        self,
        repository: str,
        image: str,
        tag: str = 'latest',
    ) -> DockerImage:
        loop = self._get_loop()
        client = self._get_client()

        image_fullname = f'{repository}/{image}'
        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.pull,
                image_fullname,
                tag=tag,
            ),
        )

    async def tag_image(
        self,
        repository: str,
        image: str,
        tag: str,
        env: Optional[Dict[str, str]] = None,
    ) -> subprocess.CompletedProcess[str]:
        self._get_loop()

        image_fullname = f'{repository}/{image}'

        command = f'docker tag {image_fullname} {tag}'
        return await self._shell.run(
            command,
            env=env,
            as_shell=True,
            silent=True,
        )

    async def prune_all_images(
        self,
        env: Optional[Dict[str, str]] = None,
    ) -> None:
        self._get_loop()

        await self._shell.run(
            'docker system prune -a -f',
            env=env,
            as_shell=True,
            silent=True,
        )

    async def prune_dangling_image(self) -> None:
        loop = self._get_loop()
        client = self._get_client()

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.prune,
                filters={'dangling': True},
            ),
        )

    async def remove_image(
        self,
        image: str,
        tag: str = 'latest',
        force: bool = True,
        delete_parents: bool = True,
    ) -> None:
        loop = self._get_loop()
        client = self._get_client()

        image_fullname = f'{image}:{tag}'

        await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.remove,
                image_fullname,
                force=force,
                noprune=not delete_parents,
            ),
        )

    async def get_image(
        self,
        image: str,
        tag: str = 'latest',
    ) -> DockerImage:
        loop = self._get_loop()
        client = self._get_client()

        image_fullname = f'{image}:{tag}'

        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.get,
                image_fullname,
            ),
        )

    async def list_images(
        self,
        repository: Optional[str] = None,
        show_intermediate_layers: bool = False,
        show_dangling: bool = False,
    ) -> List[DockerImage]:
        loop = self._get_loop()
        client = self._get_client()

        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.list,
                name=repository,
                all=show_intermediate_layers,
                filters={'dangling': show_dangling},
            ),
        )

    async def push(
        self,
        repository: str,
        image: str,
        tag: str = 'latest',
    ) -> Any:
        loop = self._get_loop()
        client = self._get_client()

        image_fullname = f'{repository}/{image}'
        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.images.push,
                image_fullname,
                tag=tag,
            ),
        )

    async def close(self) -> None:
        if self._client is not None:
            loop = self._get_loop()
            await loop.run_in_executor(
                None,
                self._client.close,
            )
            self._client = None

        self._executor.shutdown()
        await self._shell.close()
        await self._system.close()

    def abort(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None
        self._executor.shutdown()
        self._shell.abort()
        self._system.abort()
