import asyncio
import functools
import io
import pathlib
from typing import Callable, TypeVar, Literal
from concurrent.futures import ThreadPoolExecutor
from werkflow_core import Module
from werkflow_shell import Shell
from werkflow_system import System
from typing import List

T = TypeVar('T')
FileTransformString = Callable[[T], str]
FileTransformBytes = Callable[[T], bytes | bytearray]

FileReadMode = Literal['r', 'rb']
FileWriteMode = Literal['w', 'wb', 'a', 'ab']



class File(Module):

    def __init__(self) -> None:
        super().__init__()

        self._system = System()
        self._shell = Shell()

        self._loop: asyncio.AbstractEventLoop = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

    async def list_matching_files(
        self,
        path: str,
        pattern: str
    ) -> List[str]:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        absolute_path = await self._shell.to_absolute_path(path)

        search_path = pathlib.Path(absolute_path)
        
        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                search_path.rglob,
                pattern
            )
        )

        return [
            str(result) for result in results
        ]
        
    async def read(
        self,
        path: str,
        mode: FileReadMode = 'r',
    ):
        absolute_path = await self._shell.to_absolute_path(path)
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._read,
                pathlib.Path(absolute_path),
                mode=mode,
            )
        )
    
    async def write(
        self,
        path: str,
        data: T,
        transform: (
            FileTransformString[T]
            | FileTransformBytes[T]
            | None
        ),
        mode: FileWriteMode = 'w',
    ) -> None:
        absolute_path = await self._shell.to_absolute_path(path)
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._write,
                pathlib.Path(absolute_path),
                data,
                mode=mode,
                transform=transform,
            )
        )

    def _read(
        self,
        path: pathlib.Path,
        mode: FileReadMode = 'r',
    ) -> str | bytes:
        with open(path, mode) as file:
            return file.read()
        
    def _write(
        self,
        path: pathlib.Path,
        data: T,
        transform: (
            FileTransformString[T]
            | FileTransformBytes[T]
            | None
        ),
        mode: FileWriteMode = 'w',
    ) -> None:
        
        writeable_data: str | bytes | bytearray = data
        if transform:
            writeable_data = transform(data)

        with open(path, mode) as file:
            file.write(writeable_data)

    async def close(self):
        await self._shell.close()
        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown()