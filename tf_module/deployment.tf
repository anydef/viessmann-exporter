resource "kubernetes_deployment_v1" "viessmann-exporter" {
  metadata {
    name = var.name
    namespace = var.namespace
    labels = {
      app: var.name
      name: var.name
    }
  }
  spec {
    replicas = "1"
    selector {
      match_labels = {
        app: var.name
      }
    }
    template {
      metadata {
        name   = var.name
        labels = {
          "app.kubernetes.io/name" = var.name
          app                      = var.name
          name                     = var.name
        }
      }
      spec {
        container {
          name = var.name
          image = var.viessmann_exporter_image
          port {
            container_port = var.port
          }
          env {
            name = "VIESSMANN_API_KEY"
            value = var.viessmann_api_key
          }
          env {
            name = "VIESSMANN_EMAIL"
            value = var.viessmann_email
          }
          env {
            name = "VIESSMANN_PASSWORD"
            value = var.viessmann_password
          }
          env {
            name = "VIESSMANN_POLLING_INTERVAL"
            value = var.viessmann_polling_interval
          }
        }
        image_pull_secrets {
          name = var.github_container_registry_secret_name
        }
      }
    }
  }
}