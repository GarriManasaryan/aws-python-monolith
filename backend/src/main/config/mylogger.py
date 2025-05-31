import logging

logging.basicConfig(
    level=logging.DEBUG,  # Or INFO/WARNING depending on need
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)