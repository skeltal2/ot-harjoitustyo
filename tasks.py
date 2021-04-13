from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def coverage_report(ctx):
    ctx.run("coverage html")