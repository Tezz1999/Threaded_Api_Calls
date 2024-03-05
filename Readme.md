# Efficient API Calls with Multithreading

## Overview

This project demonstrates the significant benefits of utilizing multithreading for making concurrent API calls. Through a simple Flask application that interacts with a MySQL database to fetch geospatial data, we highlight how multithreading can reduce the total time required to process multiple requests.

## Objective

The primary objective is to showcase the efficiency gains from employing multithreading in the context of making API requests. We compare the time it takes to make sequential API calls versus concurrent calls using Python's `threading` module. This comparison illustrates the effectiveness of multithreading in reducing overall request time, thereby improving the performance of applications reliant on external API calls.

## Implementation

- A Flask web service exposes an endpoint `/getByPoint` that accepts geospatial coordinates (latitude and longitude) and queries a MySQL database for nearby data points.
- The endpoint calculates distances using geospatial functions and returns the closest data points, including their attributes and distances from the input coordinates.
- Python scripts demonstrate both sequential and multithreaded approaches to making requests to the Flask endpoint, using a list of predefined geospatial points.

## Results

Employing multithreading for making concurrent API requests resulted in a significant reduction in total processing time compared to sequential requests. This efficiency gain is attributed to the ability of multithreading to perform I/O operations in parallel, minimizing the idle time associated with waiting for each request to complete.

## Importance of Multithreading in API Calls

Multithreading allows an application to remain responsive and efficiently handle multiple tasks simultaneously. In the context of API calls, which often involve waiting for network responses, multithreading ensures that the waiting time for one request does not block the processing of others. This is especially critical for applications that require data from multiple sources or need to query an API multiple times with different parameters.

## Conclusion

The use of multithreading in making API calls is a powerful technique for improving the performance of applications that rely on external data sources. By executing requests concurrently, applications can achieve better resource utilization, reduce overall execution time, and provide a more responsive user experience.

## Running the Project

1. Ensure Python and Flask are installed.
2. Start the Flask application:
    ```bash
    python main.py
    ```
3. Execute the request script:
    ```bash
    python client.py
    ```
4. Execute the multi threaded request script:
    ```bash
    python client_threaded.py
    ```


