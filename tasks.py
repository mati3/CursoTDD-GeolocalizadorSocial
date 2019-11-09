from invoke import task

@task
def test(c):
    c.run("pytest -q tests/test_Post.py")

@task
def cov(c):
	c.run("pytest --cov=./")
