$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$pairs = @(
    @("module0_hook", "OpeningClinicalNotes"),
    @("module0_hook", "RoadMap"),
    @("module1_erm", "ERMAccuracyIllusion"),
    @("module1_erm", "ERMAnatomy"),
    @("module1_erm", "SpuriousDefinition"),
    @("module2_framework", "FormalizingVariables"),
    @("module2_framework", "IDOODDistributions"),
    @("module2_framework", "EnvironmentFormalization"),
    @("module2_framework", "DistributionSet"),
    @("module1_erm", "GeometryInductiveBias"),
    @("module2_framework", "RiskAggregation"),
    @("module2_framework", "GroupStructure"),
    @("module2_framework", "WorstGroupAccuracy"),
    @("module2_framework", "DistributionShiftTypes"),
    @("module3_causality", "StructuralCausalModel"),
    @("module3_causality", "ShiftBreaksSpuriousLink"),
    @("module4_irm", "ImportanceWeightingInterpolation"),
    @("module4_irm", "IRMInvariantIdea"),
    @("module4_irm", "IRMFormula"),
    @("module4_irm", "IRMGradientVectors"),
    @("module4_irm", "IRMLimitations"),
    @("module4_irm", "NuRD"),
    @("module5_dro", "GroupDRO"),
    @("module6_jtt", "SemanticCorruptions"),
    @("module6_jtt", "JTT"),
    @("module7_foundation", "ScaleDoesNotSolve"),
    @("module7_foundation", "CLIPSpuriousWeb"),
    @("module7_foundation", "ICLShortcuts"),
    @("module7_foundation", "ReverseScaling"),
    @("module7_foundation", "PromptingForRobustness"),
    @("module7_foundation", "CATO"),
    @("module8_benchmarks", "BenchmarksReality"),
    @("module8_benchmarks", "ModelSelectionParadox"),
    @("module8_benchmarks", "BestPractices"),
    @("module9_outro", "JourneySummary"),
    @("module9_outro", "OpenProblemsCredits")
)

$listFile = "media/videos/concat_list.txt"

$lines = @()
$count = 0
foreach ($p in $pairs) {
    $module = $p[0]
    $scene = $p[1]
    $videoPath = "media/videos/$module/480p15/${scene}_vo48.mp4"
    if (Test-Path $videoPath) {
        $absPath = (Get-Item $videoPath).FullName.Replace("\", "/")
        $lines += "file '$absPath'"
        $count++
    } else {
        Write-Warning "Missing video: $videoPath"
    }
}

if ($count -eq 0) {
    Write-Error "No merged video files found to concatenate!"
    exit 1
}

[System.IO.File]::WriteAllLines("$root/$listFile", $lines)

Write-Host "Found $count video files to concatenate."
$outputVideo = "media/videos/OOD_Final_Lecture_480p15.mp4"
if (Test-Path $outputVideo) { Remove-Item $outputVideo }

Write-Host "Concatenating videos using FFmpeg concat demuxer..."
ffmpeg -y -f concat -safe 0 -i $listFile -c copy $outputVideo 2>$null

if (Test-Path $outputVideo) {
    $size = (Get-Item $outputVideo).Length / 1MB
    Write-Host "Successfully concatenated final video!" -ForegroundColor Green
    Write-Host "Output saved to: $outputVideo"
    Write-Host "File size: $([math]::Round($size, 2)) MB"
} else {
    Write-Error "Failed to generate final concatenated video."
}
