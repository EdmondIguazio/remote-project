import kfp
import mlrun
from kfp import dsl

@kfp.dsl.pipeline()
def pipeline():
    
    project = mlrun.get_current_project()
    
    func = project.run_function("func", handler="handler")

    func2 = project.run_function("func2", handler="handler").after(func)

    # build_spark = project.build_function(function="sparktest", requirements=["mlrun==1.10.2"], with_mlrun=False).after(func2)

    func_spark = project.run_function("sparktest", handler="handler").after(func2)


