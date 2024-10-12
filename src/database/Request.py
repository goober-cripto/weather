import asyncpg


class Request:
    """
    Сласс с методами для работы с БД
    """
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector


