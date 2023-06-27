# don't run this unless you understand what it does!
# it WILL delete files on your computer without asking you first!
$folder = "C:\path\to\folder"
$filesToKeep = 25
$filesToDelete = Get-ChildItem -Path $folder -Filter "*.json" -File |
Sort-Object -Property LastWriteTime | Select-Object -SkipLast $filesToKeep
$filesToDelete | Remove-Item -Force