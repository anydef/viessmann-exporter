resource "kubernetes_manifest" "viessmann-exporter-servicemonitor_monitoring" {
  manifest = {
    "apiVersion" = "monitoring.coreos.com/v1"
    "kind"       = "ServiceMonitor"
    "metadata"   = {
      "labels" = {
        "app.kubernetes.io/name" = var.name
        "app"                    = var.name
        "name"                   = var.name
      }
      "name"      = var.name
      "namespace" = var.namespace
    }
    "spec" = {
      "endpoints" = [
        {
          "interval"          = "15s"
          "port"              = "http"
          "relabelings"       = []
          "metricRelabelings" = []
          "honorLabels"       = true
          "path"              = "/metrics"
        },
      ]
      "jobLabel" = "app.kubernetes.io/name"
      "selector" = {
        "matchLabels" = {
          "app.kubernetes.io/name" = var.name
        }
      }
    }
  }
}
