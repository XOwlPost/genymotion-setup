from fabric import task

@task
def lint(c):
    """Run Python linters (flake8 and black)."""
    c.run("echo 'Running Python linters...'")
    c.run("flake8 .")
    c.run("black --check .")
    c.run("echo 'Linting completed.'")
