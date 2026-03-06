# hao-backprop-test

A simple Express.js-based Node.js server that serves two HTTP endpoints. This project demonstrates basic routing with Express.js, returning plain-text responses.

## Prerequisites

- [Node.js](https://nodejs.org/) version 18 or higher
- npm (included with Node.js)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd hao-backprop-test
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

## Usage

Start the server using either command:

```bash
npm start
```

or

```bash
node server.js
```

The server will start at **http://127.0.0.1:3000/**.

## API Endpoints

| Method | Path       | Response          | Content-Type | Status |
|--------|------------|-------------------|--------------|--------|
| GET    | `/`        | `Hello, World!\n` | `text/plain` | 200    |
| GET    | `/evening` | `Good evening`    | `text/plain` | 200    |

## License

MIT
