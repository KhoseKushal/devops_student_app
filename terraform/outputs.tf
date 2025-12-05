output "resource_group" {
  value = azurerm_resource_group.rg.name
}
output "aks_name" {
  value = azurerm_kubernetes_cluster.aks.name
}
output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}
output "mysql_server" {
  value = azurerm_mysql_flexible_server.mysql.name
}
