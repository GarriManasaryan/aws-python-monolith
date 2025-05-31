import importlib
import pkgutil
from fastapi import APIRouter

router = APIRouter(prefix="/api")

# Dynamically import all modules and include their `router`
for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    if hasattr(module, "router"):
        router.include_router(module.router)
