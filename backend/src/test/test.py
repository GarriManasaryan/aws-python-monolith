from dotenv import load_dotenv
from port.persistence.pg_executer import select, update, get_cursor

load_dotenv()
import os

print('\n\nAAAAA\n\n')
print(os.getenv("PYTHONPATH"))
print('\n\nAAAAA\n\n')