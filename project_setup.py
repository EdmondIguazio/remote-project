import mlrun

def setup(project: mlrun.projects.MlrunProject) -> mlrun.projects.MlrunProject:
    
    project.set_source(source="git://github.com/EdmondIguazio/remote-project.git", pull_at_runtime=False)

    project.set_function(func="./src/func.py",
                        name="func",
                        kind="job",
                        image="mlrun/mlrun")

    project.set_function(func="./src/func.py",
                        name="func2",
                        kind="job",
                        image="mlrun/mlrun")

    sj = project.set_function(kind="spark", 
                              func="./src/func-spark.py", 
                              name="sparktest")

    sj.with_driver_limits(cpu="1300m")
    sj.with_driver_requests(cpu=1, mem="512m")

    sj.with_executor_limits(cpu="1400m")
    sj.with_executor_requests(cpu=1, mem="512m")

    sj.with_igz_spark()
    
    project.set_workflow(
        name="workflow", workflow_path="./src/workflow.py", image="mlrun/mlrun-kfp"
    )

    project.save()
    
    return project
