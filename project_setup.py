import mlrun

def setup(project: mlrun.projects.MlrunProject) -> mlrun.projects.MlrunProject:
    
    project.set_source(source="git://github.com/EdmondIguazio/remote-project.git", pull_at_runtime=False)

    project.set_function(func="./src/func.py",
                        name="func",
                        kind="job",
                        image="mlrun/mlrun")
    
    project.set_workflow(
        name="workflow", workflow_path="./src/workflow.py", image="mlrun/mlrun"
    )

    project.save()
    
    return project