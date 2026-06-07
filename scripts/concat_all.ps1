param(
    [string]$QualityDir = "480p15",
    [string]$OutFile = "OOD_Generalization_Full.mp4"
)

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$pairs = @(
    @("module0_hook", "OpeningClinicalNotes"),
    @("module0_hook", "RoadMap"),
    @("module1_erm", "ERMAccuracyIllusion"),
    @("module1_erm", "ERMAnatomy"),
    @("module1_erm", "SpuriousDefinition"),
    @("module1_erm", "FormalizingXYE"),
    @("module1_erm", "OODShiftBreaks"),
    @("module1_erm", "DistributionSetFamily"),
    @("module2_framework", "FormalizingVariables"),
    @("module2_framework", "IDOODDistributions"),
    @("module2_framework", "EnvironmentFormalization"),
    @("module2_framework", "DistributionSet"),
    @("module1_erm", "GeometryInductiveBias"),
    @("module1_erm", "GeometricSkewMaxMargin"),
    @("module2_framework", "RiskAggregation"),
    @("module2_framework", "RiskAggregationFamilies"),
    @("module2_framework", "GroupStructure"),
    @("module2_framework", "WorstGroupAccuracy"),
    @("module2_framework", "DistributionShiftTypes"),
    @("module3_causality", "StructuralCausalModel"),
    @("module3_causality", "ShiftBreaksSpuriousLink"),
    @("module3_causality", "CausalVsSpuriousTest"),
    @("module4_irm", "ImportanceWeightingInterpolation"),
    @("module4_irm", "InvariancePrinciple"),
    @("module4_irm", "IRMInvariantIdea"),
    @("module4_irm", "IRMRepresentationSpace"),
    @("module4_irm", "IRMFormula"),
    @("module4_irm", "IRMGradientVectors"),
    @("module4_irm", "IRMLimitations"),
    @("module4_irm", "NuRD"),
    @("module4_irm", "NuRDDivergencePenalty"),
    @("module4_irm", "AvoidingInterpolation"),
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
    @("module9_outro", "JourneySummaryRemastered"),
    @("module9_outro", "BigTriangleConclusion"),
    @("module9_outro", "OpenProblemsCredits")
)

$listFile = "media/videos/concat_list.txt"

$lines = @()
$count = 0
foreach ($p in $pairs) {
    $module = $p[0]
    $scene = $p[1]
    $videoPath = "media/videos/$module/$QualityDir/${scene}_vo48.mp4"
    if (Test-Path $videoPath) {
        $absPath = (Get-Item $videoPath).FullName.Replace("\", "/")
        $lines += "file '$absPath'"
        $count++
    } else {
        Write-Warning "Missing video: $videoPath"
    }
}

if ($count -eq 0) {
    Write-Warning "No files found to concatenate."
    exit
}

New-Item -ItemType Directory -Force -Path (Split-Path $listFile) | Out-Null
[IO.File]::WriteAllLines((Join-Path $PWD $listFile), $lines)

Write-Host "Starting concatenation of $count files..."
ffmpeg -y -f concat -safe 0 -i $listFile -c copy $OutFile

if ($?) {
    Write-Host "Successfully created OOD_Generalization_Full.mp4" -ForegroundColor Green
} else {
    Write-Error "Concatenation failed"
}
