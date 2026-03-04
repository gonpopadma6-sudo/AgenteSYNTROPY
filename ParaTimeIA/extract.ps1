param(
    [string]$docxPath,
    [string]$outPath
)

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($docxPath)
$entry = $zip.GetEntry("word/document.xml")
$reader = New-Object System.IO.StreamReader($entry.Open())
$xmlString = $reader.ReadToEnd()
$reader.Close()
$zip.Dispose()

$xml = [xml]$xmlString
$ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
$ns.AddNamespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")
$nodes = $xml.SelectNodes("//w:t", $ns)
$text = ($nodes | ForEach-Object { $_.InnerText }) -join "`n"
Set-Content -Path $outPath -Value $text -Encoding UTF8
