import kfp
import mlrun
from kfp import dsl

@kfp.dsl.pipeline()
def pipeline():
    
    project = mlrun.get_current_project()
    
    project.run_function("func", handler="handler")

