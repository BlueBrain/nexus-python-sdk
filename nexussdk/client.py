from typing import Optional

from nexussdk.acls import Acls
from nexussdk.files import Files
from nexussdk.identities import Identities
from nexussdk.organizations import Organizations
from nexussdk.permissions import Permissions
from nexussdk.projects import Projects
from nexussdk.realms import Realms
from nexussdk.resources import Resources
from nexussdk.resolvers import Resolvers
from nexussdk.schemas import Schemas
from nexussdk.storages import Storages
from nexussdk.utils.http import Http
from nexussdk.views import Views


class NexusClient:
    def __init__(self, environment: str, token: Optional[str] = None):
        self._http = Http(environment, token)
        self.acls = Acls(self._http)
        self.files = Files(self._http)
        self.identities = Identities(self._http)
        self.organizations = Organizations(self._http)
        self.permissions = Permissions(self._http)
        self.projects = Projects(self._http)
        self.realms = Realms(self._http)
        self.resolvers = Resolvers(self._http)
        self.resources = Resources(self._http)
        self.schemas = Schemas(self._http)
        self.storages = Storages(self._http)
        self.views = Views(self._http)
