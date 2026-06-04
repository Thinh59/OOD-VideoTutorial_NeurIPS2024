$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

python scripts/write_english_assets.py

$narration = Join-Path $root "assets\narration_en"
$voice = New-Object -ComObject SAPI.SpVoice
$voice.Rate = 0
$voice.Volume = 100

$streamType = 22
$format = New-Object -ComObject SAPI.SpAudioFormat
$format.Type = $streamType

Get-ChildItem $narration -Filter "scene_*.txt" | Sort-Object Name | ForEach-Object {
    $wav = Join-Path $narration ($_.BaseName + ".wav")
    Write-Host "Generating $wav"
    $stream = New-Object -ComObject SAPI.SpFileStream
    $stream.Format = $format
    $stream.Open($wav, 3, $false)
    $voice.AudioOutputStream = $stream
    $text = Get-Content $_.FullName -Raw -Encoding UTF8
    $xmlText = "<speak>" + $text + "</speak>"
    [void]$voice.Speak($xmlText, 8)
    $stream.Close()
}

Write-Host "Voiceover WAV files are in $narration"
