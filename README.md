# 🌦 Weather SDK Service (Python)

## 📌 Overview

This project implements a simple **SDK-like service layer** for interacting with a public weather API.
It demonstrates clean architecture principles, abstraction layers, and code quality enforcement using strict linting.

The application allows users to:

* Fetch current weather data
* Fetch weather forecast
* Store and retrieve data using a storage layer
* Interact via a CLI interface

---

## 🧱 Architecture

The project follows a layered architecture:

```
Client (API Connector)
        ↓
Service Layer
        ↓
Storage Layer
        ↓
CLI (User Interface)
```

### 🔹 Components

#### 1. API Connector Layer

* Abstract interface: `ApiConnector`
* Implementation: `WeatherApiConnector`
* Handles HTTP communication with external API

#### 2. Service Layer

* `WeatherService`
* Contains business logic
* Uses connector + storage

#### 3. Storage Layer

* Abstract interface: `Storage`
* Implementations:

  * `InMemoryStorage`
  * `MockStorage`
  * (Optional) `PostgresStorage`
* Provides CRUD operations

#### 4. CLI Layer

* Interactive menu
* Uses input/output abstractions
* Allows user to:

  * Get current weather
  * Get forecast
  * Access cached data
  * Delete cached data

#### 5. Config Layer

* Uses `pydantic-settings`
* Loads configuration from `.env`

---

## 🚀 Installation

### 1. Clone repository

```bash
git clone <your-repo-url>
cd weather-sdk
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in project root:

```env
WEATHER_API_KEY=your_api_key_here
```

You can obtain an API key from https://openweathermap.org/

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

### Example interaction:

```
Choose an action:
1 - Get current weather
2 - Get forecast
3 - Get cached data
4 - Delete cached data
0 - Exit

Enter option: 1
Enter city: Lviv

Current weather in Lviv:
Temperature: 18°C
Cloudiness: 40%
Rain (1h): 0 mm
```

---

## 🧪 Testing

Mock connector allows testing without real API calls:

* `MockApiConnector`
* `MockStorage`

These can be used to simulate API responses and isolate logic.

---

## 🧹 Code Quality

Project uses strict linting rules:

### Run linter:

```bash
flake8 . --select=WPS
```

### Type checking:

```bash
mypy .
```

---

## 📁 Project Structure

```
connectors/
services/
storages/
utils/
config/
models/
main.py
```

---

## 🧠 Design Principles

* **Dependency Inversion Principle**
* **Single Responsibility Principle**
* **Separation of Concerns**
* **Testability via abstraction**
* **Extensibility (plug different storage/API)**

---

## 🔮 Possible Improvements

* Add async support (`aiohttp`)
* Implement persistent DB (PostgreSQL fully)
* Add unit tests (`pytest`)
* Improve CLI (argparse / TUI)
* Add logging layer
* Add caching expiration (TTL)
