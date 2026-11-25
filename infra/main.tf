resource "docker_container" "api" {
  name  = var.container_name
  image = var.image_name

  ports {
    internal = var.internal_port
    external = var.external_port
  }

  restart = "unless-stopped"

  labels {
    label = "owner"
    value = var.owner
  }

  labels {
    label = "course"
    value = "AI381"
  }

  labels {
    label = "lab"
    value = "Lab4"
  }
}