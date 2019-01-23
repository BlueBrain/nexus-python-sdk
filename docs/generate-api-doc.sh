python ./md-doc.py > doc.md

cd api
pydoc -w nexussdk
pydoc -w nexussdk.acls
pydoc -w nexussdk.config
pydoc -w nexussdk.files
pydoc -w nexussdk.identities
pydoc -w nexussdk.organizations
pydoc -w nexussdk.permissions
pydoc -w nexussdk.projects
pydoc -w nexussdk.realms
pydoc -w nexussdk.resources
pydoc -w nexussdk.schemas
pydoc -w nexussdk.views
pydoc -w nexussdk.utils
cd ..
