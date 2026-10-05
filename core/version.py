from importlib.metadata import PackageNotFoundError, version

try:
    VERSION = version("Abyss")
except PackageNotFoundError:
    VERSION = "dev"
