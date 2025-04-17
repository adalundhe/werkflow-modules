import asyncio
import configparser
import functools
import pathlib
from concurrent.futures import ThreadPoolExecutor
from werkflow_system import System
from werkflow_aws.models.parsing import AWSConfigRole


class AWSConfigParser:

    def __init__(self):
        self._loop: asyncio.AbstractEventLoop | None = None
        self._system = System()
        self._parser = configparser.ConfigParser()

        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._matching_roles: dict[str, AWSConfigRole] = {}
        self._roles: list[AWSConfigRole] = []
        self._active_role_idx = 0

    def __iter__(self):
        for role in self._matching_roles.values():
            yield role

    def __next__(self):

        if len(self._roles) < 1:
            raise StopIteration('No roles found! Did you call load() first?')
        
        role = self._roles[self._active_role_idx]
        self._active_role_idx = (self._active_role_idx + 1) % len(self._matching_roles)
        return role

    def __getitem__(self, role_name: str):
        return self._matching_roles[role_name]
    
    def first(self):
        if len(self._roles) < 1:
            raise StopIteration('No roles found! Did you call load() first?')

        return self._roles[0]

    def next(self):
        return self.__next__()
    
    def get(self, role_name: str):
        return self._matching_roles.get(role_name)

    async def load(
        self,
        path: str,
        account: str,
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        path: pathlib.Path = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                pathlib.Path,
                path
            )
        )

        absolute_path = await self._loop.run_in_executor(
            self._executor,
            path.absolute
        )

        resolved_path = await self._loop.run_in_executor(
            self._executor,
            absolute_path.resolve
        )

        await self._loop.run_in_executor(
            self._executor,
            self._parser.read,
            str(resolved_path)
        )

        self._matching_roles.clear()
        self._roles.clear()
        
        for section in self._parser.sections():
            section_line: str = section
            if section_line.startswith(f"profile {account}"):
                role_name = section_line.split()[1]  # Extract the role name from the section header

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
    
    async def close(self):
        await self._system.close()

    def abort(self):
        self._system.abort()