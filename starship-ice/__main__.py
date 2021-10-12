
import sys
from typing import Iterable, List
from rich import print
from rich.console import Console
from datetime import datetime
from . import Status, Trip, get_status, get_trip, next_stop

DEFAULT_FORMAT = "[green]{trainType} {vzn}[/green] @ [red]{speed} km/h[/red] (next: [yellow]{next[station][name]}[/yellow] at {next[timetable][actualArrivalTime]:%H:%M})"

cons = Console(color_system='standard')


def make_prompt(status: Status, trip: Trip) -> Iterable[str]:
    if train_type := status.get('trainType'):
        yield f"[green]{train_type}[/green]"

    if vzn := trip.get('vzn'):
        yield f"[green]{vzn}[/green]"

    if speed := status.get('speed'):
        yield f"[red]{speed} km/h[/red]"

    if stops := trip.get('stops'):
        next = next_stop(stops)
        arrival_time = datetime.fromtimestamp(next['timetable']['actualArrivalTime']/1000)

        yield f"next: [yellow]{next['station']['name']}[/yellow] at {arrival_time:%H:%M}"


def main():

    try:
        status = get_status()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    # print(status)

    try:
        trip = get_trip()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    # print(trip)

    # if stops := trip.get('stops'):
    #     next = next_stop(stops)

    # else:
    #     next = None

    # data = dict(**status, vzn=trip['vzn'])

    # for k, v in next.items():
    #     data["next."+k] = v

    # data['next.name'] = next['station']['name']
    # data['next.arrival'] = next_arrival
    cons.print(' '.join(make_prompt(status, trip)))


if __name__ == "__main__":
    main()
