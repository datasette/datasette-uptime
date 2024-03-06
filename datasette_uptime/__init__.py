from datasette import hookimpl, Response
import time


@hookimpl
def startup(datasette):
    datasette._uptime_started = time.monotonic()


async def uptime(datasette):
    return Response.json(
        {
            "started": datasette._uptime_started,
            "now": time.monotonic(),
            "uptime_seconds": time.monotonic() - datasette._uptime_started,
            "uptime_hours": (time.monotonic() - datasette._uptime_started) / 3600,
        }
    )


@hookimpl
def register_routes():
    return [
        (r"^/-/uptime$", uptime),
    ]
