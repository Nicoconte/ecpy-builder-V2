from .insert_builder import InsertBuilder
from .select_builder import SelectBuilder
from .delete_builder import DeleteBuilder
from .update_builder import UpdateBuilder

class EcpyBuilder(InsertBuilder, SelectBuilder, DeleteBuilder, UpdateBuilder):
    
    def __init__(self, db_params):
        InsertBuilder.__init__(self, db_params)
        SelectBuilder.__init__(self, db_params)
        DeleteBuilder.__init__(self, db_params)
        UpdateBuilder.__init__(self, db_params)

        
    

            
