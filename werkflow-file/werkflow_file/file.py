import asyncio
import functools
import pathlib
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Literal, Optional, TypeVar, overload

from werkflow_core import Module
from werkflow_shell import Shell
from werkflow_system import System

T = TypeVar('T')
FileTransformString = Callable[[T], str]
FileTransformBytes = Callable[[T], bytes | bytearray]

FileReadMode = Literal['r', 'rb']
FileWriteMode = Literal['w', 'wb', 'a', 'ab']


class File(Module):
    dependencies = ['werkflow-shell', 'werkflow-system']

    def __init__(self) -> None:
        super().__init__()

        self._system = System()
        self._shell = Shell()

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    @staticmethod
    def _find_matching_files(
        search_path: pathlib.Path,
        pattern: str,
    ) -> List[str]:
        return [
            str(result)
            for result in search_path.rglob(pattern)
            if result.is_file()
        ]

    async def list_matching_files(
        self,
        path: str,
        pattern: str,
    ) -> List[str]:
        loop = self._get_loop()
        absolute_path = await self._shell.to_absolute_path(path)
        search_path = pathlib.Path(absolute_path)

        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                self._find_matching_files,
                search_path,
                pattern,
            ),
        )

    @overload
    async def read(
        self,
        path: str,
        mode: Literal['r'] = 'r',
        encoding: str = 'utf-8',
    ) -> str: ...

    @overload
    async def read(
        self,
        path: str,
        mode: Literal['rb'],
        encoding: str = 'utf-8',
    ) -> bytes: ...

    @overload
    async def read(
        self,
        path: str,
        mode: FileReadMode = 'r',
        encoding: str = 'utf-8',
    ) -> str | bytes: ...

    async def read(
        self,
        path: str,
        mode: FileReadMode = 'r',
        encoding: str = 'utf-8',
    ) -> str | bytes:
        loop = self._get_loop()
        absolute_path = await self._shell.to_absolute_path(path)
        return await loop.run_in_executor(
            self._executor,
            functools.partial(
                self._read,
                pathlib.Path(absolute_path),
                mode=mode,
                encoding=encoding,
            ),
        )

    async def write(
        self,
        path: str,
        data: T,
        transform: (
            FileTransformString[T]
            | FileTransformBytes[T]
            | None
        ) = None,
        mode: FileWriteMode = 'w',
        encoding: str = 'utf-8',
    ) -> None:
        loop = self._get_loop()
        absolute_path = await self._shell.to_absolute_path(path)
        await loop.run_in_executor(
            self._executor,
            functools.partial(
                self._write,
                pathlib.Path(absolute_path),
                data,
                transform=transform,
                mode=mode,
                encoding=encoding,
            ),
        )

    def _read(
        self,
        path: pathlib.Path,
        mode: FileReadMode = 'r',
        encoding: str = 'utf-8',
    ) -> str | bytes:
        if mode == 'rb':
            with open(path, mode) as file:
                return file.read()
        with open(path, mode, encoding=encoding) as file:
            return file.read()

    def _write(
        self,
        path: pathlib.Path,
        data: T,
        transform: (
            FileTransformString[T]
            | FileTransformBytes[T]
            | None
        ) = None,
        mode: FileWriteMode = 'w',
        encoding: str = 'utf-8',
    ) -> None:
        writeable_data: str | bytes | bytearray
        if transform is not None:
            writeable_data = transform(data)
        elif isinstance(data, (str, bytes, bytearray)):
            writeable_data = data
        else:
            raise TypeError(
                f"Data of type {type(data).__name__!r} requires a transform function."
            )

        if mode in ('wb', 'ab'):
            binary_data: bytes | bytearray = (
                writeable_data.encode(encoding)
                if isinstance(writeable_data, str)
                else writeable_data
            )
            with open(path, mode) as file:
                file.write(binary_data)
        else:
            text_data: str = (
                writeable_data.decode(encoding)
                if isinstance(writeable_data, (bytes, bytearray))
                else writeable_data
            )
            with open(path, mode, encoding=encoding) as file:
                file.write(text_data)

    async def close(self) -> None:
        await self._shell.close()
        await self._system.close()
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown(wait=False, cancel_futures=True)
