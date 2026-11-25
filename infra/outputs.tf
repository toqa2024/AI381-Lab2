
output "container_name" {
  description = "Name of the deployed API container"
  value       = docker_container.api.name
}

output "container_id" {
  description = "ID of the deployed API container"
  value       = docker_container.api.id
}

output "api_url" {
  description = "URL of the local API"
  value       = "http://localhost:${var.external_port}"
}
