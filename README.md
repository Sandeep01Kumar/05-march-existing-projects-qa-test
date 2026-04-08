# hao-backprop-test

A minimal Python 3 Flask HTTP server for backprop integration testing. Do not touch!

## Description

This project implements a lightweight HTTP server using Python 3 and [Flask](https://flask.palletsprojects.com/). The server responds to every HTTP request (any method, any path) with:

- **Status:** 200 OK
- **Content-Type:** `text/plain`
- **Body:** `Hello, World!`

The server binds to `127.0.0.1` on port `3000`.

## Prerequisites

- Python 3.9 or newer (Python 3.12 recommended)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

The server will start and print a confirmation message:

```
Server running at http://127.0.0.1:3000/
```

## License

MIT
