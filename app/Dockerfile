# ===== Stage 1: Build Go app =====
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY app/go.mod app/go.sum ./
RUN go mod download
COPY app/ .
RUN go build -o cpu-ram-monitoring

# ===== Stage 2: Final image =====
FROM python:3.12-alpine
WORKDIR /app

# Skopiuj Go binary
COPY --from=builder /app/cpu-ram-monitoring .

# Skopiuj frontend
COPY frontend/ ./frontend

# Skopiuj Python app
COPY python_app/ ./python_app
COPY requirements.txt .

# Zainstaluj Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Start command (np. Go app)
CMD ["./cpu-ram-monitoring"]

