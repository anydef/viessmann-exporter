variable "namespace" {
  type = string
}

variable "name" {
  type = string
  default = "viessmann-exporter"
}

variable "port" {
  type = string
  default = 5000
}

variable "viessmann_api_key" {
  type = string
}

variable "viessmann_email" {
  type = string
}

variable "viessmann_password" {
  type = string
}

variable "viessmann_polling_interval" {
  type = string
}

variable "viessmann_exporter_image" {
  type = string
}

variable "github_container_registry_secret_name" {
  type = string
}

