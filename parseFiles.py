import time
import tracemalloc
import csv
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Function to measure time and memory usage
def measure_performance(func, *args):
    start_time = time.time()
    tracemalloc.start()

    func(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time: {end_time - start_time:.6f} seconds, Memory: {peak / 1024:.2f} KB")

# Parsing CSV
def parse_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            pass

# Parsing JSON
def parse_json(filename):
    with open(filename, mode='r') as file:
        data = json.load(file)

# Parsing XML
def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

# Parsing HTML
def parse_html(filename):
    with open(filename, mode='r') as file:
        soup = BeautifulSoup(file, 'html.parser')

# Performance testing
if __name__ == "__main__":
    # Assume these files contain respective formatted data
    print("Parsing CSV File:")
    measure_performance(parse_csv, 'data.csv')

    print("\nParsing JSON File:")
    measure_performance(parse_json, 'data.json')

    print("\nParsing XML File:")
    measure_performance(parse_xml, 'data.xml')

    print("\nParsing HTML File:")
    measure_performance(parse_html, 'data.html')
