from typing import List, Dict
from os import path
import heapq
import json

class Station:

    def __init__(self, name: str, line: 'Line', connecting_lines: List['Line'], stations: Dict['Station', int]) -> None:
        self.name = name
        self.connecting_lines = connecting_lines
        self.stations = stations
        self.line = line.color
        print(f"Station created: {self.name} on line {self.line}")

    def __lt__(self, other):
        return self.name < other.name

class Line:

    def __init__(self, color: str, stations: List['Station']) -> None:
        self.color = color
        self.stations = stations
        print(f"Line created: {self.color}")

class Network:

    def __init__(self) -> None:
        self.lines: List[Line] = []
        self.station_map: Dict[str, 'Station'] = {}
        print("Network initialized")

    def load_from_json(self, filepath: str) -> None:
        print(f"Loading data from JSON: {filepath}")
        with open(filepath) as f:
            raw_data = json.load(f)
        print(f"Raw data loaded: {len(raw_data)} stations found")

        line_map: Dict[str, Line] = {}

        # Step 1: Create stations
        for entry in raw_data:
            for line_name in entry["lines"]:
                if line_name not in line_map:
                    line_map[line_name] = Line(line_name, [])
                    print(f"New line added: {line_name}")

            primary_line = line_map[entry["lines"][0]]
            station = Station(entry["name"], primary_line, [], {})
            self.station_map[entry["name"]] = station
            print(f"Station added to network: {station.name}")

            for line_name in entry["lines"]:
                line_map[line_name].stations.append(station)
                print(f"Station {station.name} added to line {line_name}")

        # Step 2: Add connections (assuming connecting is a list of neighbor names)
        for entry in raw_data:
            current_station = self.station_map[entry["name"]]
            current_station.connecting_lines = [
                line_map[line_name] for line_name in entry["lines"]
            ]
            print(f"Setting connections for station: {current_station.name}")
            for neighbor_name in entry.get("connecting", []):
                if neighbor_name in self.station_map:
                    neighbor_station = self.station_map[neighbor_name]
                    # Assuming fixed distance 1.5 for all connections as per your latest format
                    current_station.stations[neighbor_station] = 1.5
                    print(f"Connected {current_station.name} to {neighbor_station.name} with distance 1.5")

        # Step 3: Add lines to self.lines
        self.lines = list(line_map.values())
        print(f"Total lines loaded: {len(self.lines)}")

    def calculate_fare(self, source: str, destination: str) -> int:
        print(f"Calculating fare from '{source}' to '{destination}'")
        if source not in self.station_map or destination not in self.station_map:
            error_msg = f"Invalid station name(s): {source} or {destination}"
            print(error_msg)
            raise ValueError(error_msg)

        start = self.station_map[source]
        end = self.station_map[destination]

        # Dijkstra setup
        distances = {station: float('inf') for station in self.station_map.values()}
        distances[start] = 0
        pq = [(0, start)]  # (distance, station)

        while pq:
            curr_dist, curr_station = heapq.heappop(pq)
            # print current processing station for debugging
            print(f"Processing station: {curr_station.name}, current distance: {curr_dist}")

            if curr_station == end:
                print(f"Destination {end.name} reached with distance {curr_dist}")
                break

            for neighbor, dist in curr_station.stations.items():
                new_dist = curr_dist + dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
                    print(f"Updated distance for {neighbor.name} to {new_dist}")

        total_distance = distances[end]
        print(f"Total distance: {total_distance}")
        fare = self.dmrc_fare_rules(total_distance)
        print(f"Fare calculated: {fare}")
        return fare

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

# Example test print
fare = network.calculate_fare("Rajiv Chowk", "Barakhamba Road")
print(f"Fare from Rajiv Chowk to Barakhamba Road: ₹{fare}")
