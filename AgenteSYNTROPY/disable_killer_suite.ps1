# Requer privilégios de Administrador
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell.exe -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

Write-Host "Neutralizando serviços do Killer Performance Suite..."

# Parar serviços
Stop-Service -Name "KillerAnalyticsService" -Force -ErrorAction SilentlyContinue
Stop-Service -Name "KillerNetworkService" -Force -ErrorAction SilentlyContinue
Stop-Service -Name "KillerProviderDataHelperService" -Force -ErrorAction SilentlyContinue

# Desabilitar serviços
Set-Service -Name "KillerAnalyticsService" -StartupType Disabled -ErrorAction SilentlyContinue
Set-Service -Name "KillerNetworkService" -StartupType Disabled -ErrorAction SilentlyContinue
Set-Service -Name "KillerProviderDataHelperService" -StartupType Disabled -ErrorAction SilentlyContinue

# Matar processos em andamento do Killer Control Center
Stop-Process -Name "KillerControlCenter" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "KCC" -Force -ErrorAction SilentlyContinue

Write-Host "O Killer Performance Suite foi neutralizado."
Write-Host "Apenas os drivers de rede (Wi-Fi/Ethernet) continuarão operando normalmente."
Write-Host "Pressione qualquer tecla para sair..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
