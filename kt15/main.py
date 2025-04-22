import click

@click.command()
@click.argument("name")
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
