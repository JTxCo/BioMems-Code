from table_BASE import BaseTable


class Sample(BaseTable):
    def __init__(self, well_reference_list) -> None:
        super().__init__()
        self.well_refernce_list = well_reference_list
        
        