
variable "container_name" {
  description = "Name of the local Docker container"
  type        = string
  default     = "ai381-lab4-api-github"
}

variable "image_name" {
  description = "Local Docker image used by the API"
  type        = string
  default     = "churn-api:local"
}

variable "external_port" {
  description = "Port exposed on the host machine"
  type        = number
  default     = 8002
}

variable "internal_port" {
  description = "Port used by the API inside the container"
  type        = number
  default     = 8000
}
variable "owner" {
  description = "Owner of the lab resources"
  type        = string
  default     = "student"
}

variable "docker_host" {
  description = "Docker daemon connection endpoint"
  type        = string
  default     = "npipe:////./pipe/docker_engine"
}