from config.app import ConnectionFromPool, db_cursor_context


def transactional(func):
    def wrapper_func(*args, **kwargs):
        with ConnectionFromPool() as cursor:
            # set cursor to global (but thread local) ContextVar dict
            db_cursor_context.set(cursor)
            result = func(*args, **kwargs)
            # nullify ContextVar
            db_cursor_context.set(None)
            return result

    return wrapper_func
