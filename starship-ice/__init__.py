
from typing import Iterable, TypedDict
import requests


class Status(TypedDict):
    connection: bool
    serviceLevel: str
    gpsStatus: str
    internet: str
    latitude: float
    longitude: float
    tileY: int
    tileX: int
    series: str
    serverTime: int
    speed: float
    trainType: str
    tzn: str
    wagonClass: str
    connectivity: TypedDict
    bapInstalled: bool


def get_status() -> Status:
    """
        {
            'connection': True,
            'serviceLevel': 'AVAILABLE_SERVICE',
            'gpsStatus': 'VALID',
            'internet': 'HIGH',
            'latitude': 49.50447666666667,
            'longitude': 10.982958,
            'tileY': -56,
            'tileX': 98,
            'series': '803',
            'serverTime': 1632417358363,
            'speed': 135.0,
            'trainType': 'ICE',
            'tzn': 'Tz189',
            'wagonClass': 'SECOND',
            'connectivity': {'currentState': 'HIGH', 'nextState': 'UNSTABLE', 'remainingTimeSeconds': 1786},
            'bapInstalled': True
        }
    """

    resp = requests.get("https://iceportal.de/api1/rs/status")

    return resp.json()


class Station(TypedDict):
    name: str


class TimeTable(TypedDict):
    actualArrivalTime: str


class StopInfo(TypedDict):
    passed: bool


class Stop(TypedDict):
    station: Station
    info: StopInfo
    timetable: TimeTable


class Trip(TypedDict):
    tripDate: str
    trainType: str
    vzn: str
    stops: list[Stop]


def get_trip() -> Trip:
    """
    {
        'trip': {
            'tripDate': '2021-09-23',
            'trainType': 'ICE',
            'vzn': '702',
            'actualPosition': 180477,
            'distanceFromLastStop': 17492,
            'totalDistance': 592403,
            'stopInfo': {
                'scheduledNext': '8010101_00',
                'actualNext': '8010101_00',
                'actualLast': '8000284_00',
                'actualLastStarted': '8010101',
                'finalStationName': 'Berlin Gesundbrunnen',
                'finalStationEvaNr': '8011102_00'
            },
            'stops': [
                {
                    'station': {'evaNr': '8000261_00', 'name': 'München Hbf', 'code': None, 'geocoordinates': {'latitude': 48.140232, 'longitude': 11.558335}},
                    'timetable': {
                        'scheduledArrivalTime': None,
                        'actualArrivalTime': None,
                        'showActualArrivalTime': None,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632409500000,
                        'actualDepartureTime': 1632409560000,
                        'showActualDepartureTime': True,
                        'departureDelay': '+1'
                    },
                    'track': {'scheduled': '14', 'actual': '14'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'passed', 'distance': 0, 'distanceFromStart': 0},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8004158_00', 'name': 'München-Pasing', 'code': None, 'geocoordinates': {'latitude': 48.149852, 'longitude': 11.461872}},
                    'timetable': {
                        'scheduledArrivalTime': 1632409920000,
                        'actualArrivalTime': 1632409980000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '+1',
                        'scheduledDepartureTime': 1632410040000,
                        'actualDepartureTime': 1632410040000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '10', 'actual': '10'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'passed', 'distance': 7239, 'distanceFromStart': 7239},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8000013_00', 'name': 'Augsburg Hbf', 'code': None, 'geocoordinates': {'latitude': 48.365441, 'longitude': 10.88557}},
                    'timetable': {
                        'scheduledArrivalTime': 1632411420000,
                        'actualArrivalTime': 1632411420000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632411540000,
                        'actualDepartureTime': 1632411540000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '5', 'actual': '5'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'passed', 'distance': 48952, 'distanceFromStart': 56191},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8000078_00', 'name': 'Donauwörth', 'code': None, 'geocoordinates': {'latitude': 48.714026, 'longitude': 10.771443}},
                    'timetable': {
                        'scheduledArrivalTime': 1632412920000,
                        'actualArrivalTime': 1632412920000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632413040000,
                        'actualDepartureTime': 1632413040000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '3', 'actual': '3'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'passed', 'distance': 39672, 'distanceFromStart': 95863},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8000122_00', 'name': 'Treuchtlingen', 'code': None, 'geocoordinates': {'latitude': 48.961267, 'longitude': 10.908159}},
                    'timetable': {
                        'scheduledArrivalTime': 1632414180000,
                        'actualArrivalTime': 1632414420000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '+4',
                        'scheduledDepartureTime': 1632414300000,
                        'actualDepartureTime': 1632414420000,
                        'showActualDepartureTime': True,
                        'departureDelay': '+2'
                    },
                    'track': {'scheduled': '4', 'actual': '4'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'passed', 'distance': 29264, 'distanceFromStart': 125127},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8000284_00', 'name': 'Nürnberg Hbf', 'code': None, 'geocoordinates': {'latitude': 49.445616, 'longitude': 11.082989}},
                    'timetable': {
                        'scheduledArrivalTime': 1632416340000,
                        'actualArrivalTime': 1632416520000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '+3',
                        'scheduledDepartureTime': 1632416760000,
                        'actualDepartureTime': 1632416820000,
                        'showActualDepartureTime': True,
                        'departureDelay': '+1'
                    },
                    'track': {'scheduled': '7', 'actual': '7'},
                    'info': {'status': 0, 'passed': True, 'positionStatus': 'departed', 'distance': 55350, 'distanceFromStart': 180477},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8010101_00', 'name': 'Erfurt Hbf', 'code': None, 'geocoordinates': {'latitude': 50.972551, 'longitude': 11.038499}},
                    'timetable': {
                        'scheduledArrivalTime': 1632421440000,
                        'actualArrivalTime': 1632421440000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632421920000,
                        'actualDepartureTime': 1632421920000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '9', 'actual': '9'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 169865, 'distanceFromStart': 350342},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8010159_00', 'name': 'Halle (Saale) Hbf', 'code': None, 'geocoordinates': {'latitude': 51.477509, 'longitude': 11.987085}},
                    'timetable': {
                        'scheduledArrivalTime': 1632423840000,
                        'actualArrivalTime': 1632423840000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632423960000,
                        'actualDepartureTime': 1632423960000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '8', 'actual': '8'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 86719, 'distanceFromStart': 437061},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8010050_00', 'name': 'Bitterfeld', 'code': None, 'geocoordinates': {'latitude': 51.622861, 'longitude': 12.31685}},
                    'timetable': {
                        'scheduledArrivalTime': 1632424920000,
                        'actualArrivalTime': 1632424920000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632425040000,
                        'actualDepartureTime': 1632425040000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '2', 'actual': '2'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 27956, 'distanceFromStart': 465017},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8011113_00', 'name': 'Berlin Südkreuz', 'code': None, 'geocoordinates': {'latitude': 52.475047, 'longitude': 13.365319}},
                    'timetable': {
                        'scheduledArrivalTime': 1632428220000,
                        'actualArrivalTime': 1632428220000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632428340000,
                        'actualDepartureTime': 1632428340000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '8', 'actual': '8'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 118858, 'distanceFromStart': 583875},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8098160_00', 'name': 'Berlin Hbf (tief)', 'code': None, 'geocoordinates': {'latitude': 52.525592, 'longitude': 13.369545}},
                    'timetable': {
                        'scheduledArrivalTime': 1632428640000,
                        'actualArrivalTime': 1632428640000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': 1632428940000,
                        'actualDepartureTime': 1632428940000,
                        'showActualDepartureTime': True,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '6', 'actual': '6'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 5629, 'distanceFromStart': 589504},
                    'delayReasons': None
                },
                {
                    'station': {'evaNr': '8011102_00', 'name': 'Berlin Gesundbrunnen', 'code': None, 'geocoordinates': {'latitude': 52.548963, 'longitude': 13.388513}},
                    'timetable': {
                        'scheduledArrivalTime': 1632429180000,
                        'actualArrivalTime': 1632429180000,
                        'showActualArrivalTime': True,
                        'arrivalDelay': '',
                        'scheduledDepartureTime': None,
                        'actualDepartureTime': None,
                        'showActualDepartureTime': None,
                        'departureDelay': ''
                    },
                    'track': {'scheduled': '8', 'actual': '8'},
                    'info': {'status': 0, 'passed': False, 'positionStatus': 'future', 'distance': 2899, 'distanceFromStart': 592403},
                    'delayReasons': None
                }
            ]
        },
        'connection': None,
        'selectedRoute': {'conflictInfo': {'status': 'NO_CONFLICT', 'text': None}, 'mobility': None},
        'active': None
    }
    """

    resp = requests.get("https://iceportal.de/api1/rs/tripInfo/trip")

    return resp.json().get('trip')


def next_stop(stops: Iterable[Stop]) -> Stop:
    for stop in stops:
        if stop["info"]["passed"] == False:
            return stop
    return None
