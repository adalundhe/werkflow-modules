import asyncio
import configparser
import functools
import pathlib
from concurrent.futures import ThreadPoolExecutor
from typing import Iterator
from werkflow_system import System
from werkflow_aws.models.parsing import AWSConfigRole


class AWSConfigParser:

    def __init__(self) -> None:
        self._loop: asyncio.AbstractEventLoop | None = None
        self._system = System()
        self._parser = configparser.ConfigParser()

        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._matching_roles: dict[str, AWSConfigRole] = {}
        self._roles: list[AWSConfigRole] = []
        self._active_role_idx: int = 0

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    def __iter__(self) -> Iterator[AWSConfigRole]:
        yield from self._roles

    def __next__(self) -> AWSConfigRole:
        if len(self._roles) < 1:
            raise StopIteration('No roles found! Did you call load() first?')

        if self._active_role_idx >= len(self._roles):
            self._active_role_idx = 0
            raise StopIteration()

        role = self._roles[self._active_role_idx]
        self._active_role_idx += 1
        return role

    def __getitem__(self, role_name: str) -> AWSConfigRole:
        return self._matching_roles[role_name]

    def first(self) -> AWSConfigRole:
        if len(self._roles) < 1:
            raise StopIteration('No roles found! Did you call load() first?')

        return self._roles[0]

    def next(self) -> AWSConfigRole:
        return self.__next__()

    def get(self, role_name: str) -> AWSConfigRole | None:
        return self._matching_roles.get(role_name)

    async def load(
        self,
        path: str,
        account: str,
    ) -> list[AWSConfigRole]:
        loop = self._get_loop()

        config_path = await loop.run_in_executor(
            self._executor,
            functools.partial(pathlib.Path, path),
        )
        resolved_path = await loop.run_in_executor(
            self._executor,
            config_path.resolve,
        )

        self._parser = configparser.ConfigParser()
        await loop.run_in_executor(
            self._executor,
            self._parser.read,
            str(resolved_path),
        )

        self._matching_roles.clear()
        self._roles.clear()
        self._active_role_idx = 0

        for section in self._parser.sections():
            if section.startswith(f'profile {account}'):
                parts = section.split(maxsplit=1)
                role_name = parts[1] if len(parts) > 1 else section

                role = AWSConfigRole(
                    role_name=role_name,
                    region=self._parser.get(section, 'region', fallback='N/A'),
                    source_profile=self._parser.get(section, 'source_profile', fallback='N/A'),
                    external_id=self._parser.get(section, 'external_id', fallback='N/A'),
                    role_arn=self._parser.get(section, 'role_arn', fallback='N/A'),
                )

                self._roles.append(role)
                self._matching_roles[role_name] = role

        return list(self._roles)

    async def close(self) -> None:
        await self._system.close()
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        self._system.abort()
        self._executor.shutdown(wait=False, cancel_futures=True)
