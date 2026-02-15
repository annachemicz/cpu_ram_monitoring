\# ===== Stage 1: Build Go app =====
FROM golang:1.21-alpine AS builder
WORKDIR /app

# Skopiuj go.mod z prawidłowej lokalizacji
COPY apka/go.mod ./

# Pobierz zależności (go.sum nie jest wymagany)
RUN go mod download

# Skopiuj cały kod Go
COPY apka/ ./apka

# Zbuduj binarkę
RUN go build -o cpu-ram-monitoring ./apka

# ===== Stage 2: Final image =====
FROM python:3.12-alpine
WORKDIR /app

# Skopiuj Go binary
COPY --from=builder /app/cpu-ram-monitoring .

# Skopiuj frontend
COPY frontend/ ./frontend

# Skopiuj Python app
COPY python_app/ ./python_app

# Skopiuj requirements.txt
COPY python_app/requirements.txt .

# Zainstaluj Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Start command (np. Go app)
CMD ["./cpu-ram-monitoring"]