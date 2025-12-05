variable "resource_group_name" {
  type    = string
  default = "devops-rg"
}
variable "location" {
  type    = string
  default = "eastus"
}
variable "acr_name" {
  type    = string
  default = "studentacr123" # must be globally unique - change this
}
variable "aks_name" {
  type    = string
  default = "student-aks"
}
variable "dns_prefix" {
  type    = string
  default = "studentapp"
}
variable "mysql_name" {
  type    = string
  default = "studentmysqlserver"
}
variable "mysql_admin" {
  type    = string
  default = "adminuser"
}
variable "mysql_password" {
  type    = string
  default = "Admin@12345" # change before production
}
variable "mysql_database" {
  type    = string
  default = "studentdb"
}
