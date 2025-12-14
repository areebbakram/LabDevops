# # Stop & remove old containers
# docker stop node-exporter, prometheus, grafana -ErrorAction SilentlyContinue
# docker rm node-exporter, prometheus, grafana -f -ErrorAction SilentlyContinue

# # Create a user-defined network
# docker network inspect monitoring -ErrorAction SilentlyContinue
# if ($LASTEXITCODE -ne 0) {
#     docker network create monitoring
# }

# # Start Node Exporter
# docker run -d --name node-exporter --network monitoring -p 9100:9100 prom/node-exporter

# # Start Prometheus
# $pwdEscaped = ${PWD}.Path -replace '\\','\\'
# docker run -d --name prometheus --network monitoring -p 9090:9090 `
#   -v "$pwdEscaped\monitoring\prometheus.yml:/etc/prometheus/prometheus.yml" `
#   prom/prometheus

# # Start Grafana
# docker run -d --name grafana --network monitoring -p 3000:3000 grafana/grafana


# Check if network exists
docker network inspect monitoring
if ($LASTEXITCODE -ne 0) {
    Write-Output "Creating Docker network 'monitoring'..."
    docker network create monitoring
}

# Start Node Exporter
docker run -d --name node-exporter --network monitoring -p 9100:9100 prom/node-exporter

# Start Prometheus
$pwdEscaped = ${PWD}.Path -replace '\\','\\'
docker run -d --name prometheus --network monitoring -p 9090:9090 `
  -v "$pwdEscaped\monitoring\prometheus.yml:/etc/prometheus/prometheus.yml" prom/prometheus

# Start Grafana
docker run -d --name grafana --network monitoring -p 3000:3000 grafana/grafana
