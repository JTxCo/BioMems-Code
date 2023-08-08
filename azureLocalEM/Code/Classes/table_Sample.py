from table_BASE import BaseTable


class Sample(BaseTable):
    def __init__(self, test_ID) -> None:
        super().__init__()
        # if None in (test_ID):
        #     raise ValueError("All attributes must be non-null.")
        # if not isinstance(test_ID, int):
        #     raise ValueError("test_ID must be an integer.")
        # self.test_ID = test_ID
        