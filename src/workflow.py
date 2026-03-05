import kfp
import mlrun
from kfp import dsl

@kfp.dsl.pipeline()
def pipeline():
    
    project = mlrun.get_current_project()
    
    func = project.run_function("func", handler="handler")

    project.run_function("func2", handler="handler").after(func)


