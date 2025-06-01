import heapq
from os import path
from typing import List, Dict
import json

class Station:

    def __init__(self, name: str, line: 'Line', connecting_lines: List['Line'], stations: Dict['Station', int]) -> None:
        self.name = name
        self.connecting_lines = connecting_lines
        self.stations = stations
        self.line = line.color

class Line:

    def __init__(self, color: str, stations: List['Station']) -> None:
        self.color = color
        self.stations = stations

class Network:

    def __init__(self) -> None:
        self.lines: List[Line] = []
        self.station_map: Dict[str, 'Station'] = {}

    def load_from_json(self, filepath: str) -> None:
        with open(filepath) as f:
            raw_data = json.load(f)

        line_map: Dict[str, Line] = {}

        # Step 1: Create stations
        for entry in raw_data:
            for line_name in entry["lines"]:
                if line_name not in line_map:
                    line_map[line_name] = Line(line_name, [])

            primary_line = line_map[entry["lines"][0]]
            station = Station(entry["name"], primary_line, [], {})
            self.station_map[entry["name"]] = station

            for line_name in entry["lines"]:
                line_map[line_name].stations.append(station)

        # Step 2: Add connections
        for entry in raw_data:
            current_station = self.station_map[entry["name"]]
            current_station.connecting_lines = [
                line_map[line_name] for line_name in entry["lines"]
            ]
            for neighbor_name, dist in entry["connecting"].items():
                if neighbor_name in self.station_map:
                    neighbor_station = self.station_map[neighbor_name]
                    current_station.stations[neighbor_station] = dist

        # Step 3: Add lines to self.lines
        self.lines = list(line_map.values())

    def calculate_fare(self, source: str, destination: str) -> int:
        if source not in self.station_map or destination not in self.station_map:
            raise ValueError("Invalid station name")

        start = self.station_map[source]
        end = self.station_map[destination]

        # Dijkstra setup
        distances = {station: float('inf') for station in self.station_map.values()}
        distances[start] = 0
        pq = [(0, start)]  # (distance, station)

        while pq:
            curr_dist, curr_station = heapq.heappop(pq)
            if curr_station == end:
                break

            for neighbor, dist in curr_station.stations.items():
                new_dist = curr_dist + dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        total_distance = distances[end]
        return self.dmrc_fare_rules(total_distance)

    @staticmethod
    def dmrc_fare_rules(distance: float) -> int:
        if distance <= 2:
            return 10
        elif distance <= 5:
            return 20
        elif distance <= 12:
            return 30
        elif distance <= 21:
            return 40
        elif distance <= 32:
            return 50
        else:
            return 60


network = Network()
base_dir = path.dirname(path.dirname(path.abspath(__file__)))
json_path = path.join(base_dir, 'json', 'delhi_metro.json')
network.load_from_json(json_path)
fare = network.calculate_fare("Rajiv Chowk", "Barakhamba Road")
print(f"Fare from Rajiv Chowk to Barakhamba Road: ₹{fare}")

for name, station in network.station_map.items():
    print(f"{name} → Line: {station.line}, Connections: {[s.name for s in station.stations]}")





