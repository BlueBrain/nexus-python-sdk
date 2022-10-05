import pytest


@pytest.mark.asyncio
async def test_create_and_fetch(env):
    print(f"{env.org}/{env.prj}")

    ids = []

    def cb(task):
        index, status, json = task.result()
        nonlocal ids
        if status < 400:
            ids.append(json["@id"])
        else:
            raise Exception(f"Error: index={index} status={status} output={json}")

    resources = []
    for i in range(10):
        resources.append({
            "firstname": f"Johnny {i}",
            "lastname": "Bravo"
        })
    result = await env.client.resources.bulk_create(env.org, env.prj, resources, callback=cb)
    assert len(result) == 10
    assert len(ids) == 10
    print(ids)

    fetched = []

    def cb2(task):
        index, status, json = task.result()
        nonlocal fetched
        print(f"Error: index={index} status={status} output={json}")
        if status < 400:
            fetched.append(json["@id"])
        else:
            raise Exception(f"Error: index={index} status={status} output={json}")

    result = await env.client.resources.bulk_fetch(env.org, env.prj, ids, callback=cb2)
    assert len(result) == 10
    assert len(fetched) == 10
