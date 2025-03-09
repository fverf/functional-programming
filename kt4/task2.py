#функция gen-resource-builder
#создаёт функцию, принимающую resource и возвращающую функцию, которая принимает id в качестве аргумента.

def gen_resource_builder(host, api_key):
    return lambda resource: lambda id: f"{host}/{resource}/{id}?token={api_key}"

resource_builder = gen_resource_builder("https://github.com/fverf/functional-programming", "mySecureToken")
repo_url = resource_builder("issues")
print(repo_url("42"))