@echo off
color 0B
echo =======================================================
echo          NEUTRALIZANDO KILLER PERFORMANCE SUITE
echo =======================================================
echo.
echo Parando os servicos...
net stop "KillerAnalyticsService" /y 2>nul
net stop "KillerNetworkService" /y 2>nul
net stop "KillerProviderDataHelperService" /y 2>nul
echo.
echo Desabilitando a reinicializacao automatica...
sc config "KillerAnalyticsService" start= disabled
sc config "KillerNetworkService" start= disabled
sc config "KillerProviderDataHelperService" start= disabled
echo.
echo Encerrando Control Center em execucao...
taskkill /F /IM KillerControlCenter.exe /T 2>nul
taskkill /F /IM KCC.exe /T 2>nul
echo.
echo =======================================================
echo O Killer Performance Suite foi neutralizado com sucesso!
echo =======================================================
echo Os drivers de conexao (Wi-Fi/Ethernet) estao intocados.
echo Pressione qualquer tecla para sair desta janela...
pause >nul
