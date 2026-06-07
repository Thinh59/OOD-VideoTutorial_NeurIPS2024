param(
    [string]$QualityDir = "480p15"
)

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$pairs = @(
    @("module0_hook", "OpeningClinicalNotes", "scene_0_1_OpeningClinicalNotes"),
    @("module0_hook", "RoadMap", "scene_0_2_RoadMap"),
    @("module1_erm", "ERMAccuracyIllusion", "scene_1_1_ERMAccuracyIllusion"),
    @("module1_erm", "ERMAnatomy", "scene_1_2_ERMAnatomy"),
    @("module1_erm", "SpuriousDefinition", "scene_1_3_SpuriousDefinition"),
    @("module1_erm", "FormalizingXYE", "scene_1_3A_FormalizingXYE"),
    @("module1_erm", "OODShiftBreaks", "scene_1_3B_OODShiftBreaks"),
    @("module1_erm", "DistributionSetFamily", "scene_1_3C_DistributionSetFamily"),
    @("module2_framework", "FormalizingVariables", "scene_1_31_FormalizingVariables"),
    @("module2_framework", "IDOODDistributions", "scene_1_32_IDOODDistributions"),
    @("module2_framework", "EnvironmentFormalization", "scene_1_33_EnvironmentFormalization"),
    @("module2_framework", "DistributionSet", "scene_1_34_DistributionSet"),
    @("module1_erm", "GeometryInductiveBias", "scene_1_4_GeometryInductiveBias"),
    @("module1_erm", "GeometricSkewMaxMargin", "scene_1_4B_GeometricSkewMaxMargin"),
    @("module2_framework", "RiskAggregation", "scene_2_0_RiskAggregation"),
    @("module2_framework", "RiskAggregationFamilies", "scene_R4_RiskAggregationFamilies"),
    @("module2_framework", "GroupStructure", "scene_2_1_GroupStructure"),
    @("module2_framework", "WorstGroupAccuracy", "scene_2_2_WorstGroupAccuracy"),
    @("module2_framework", "DistributionShiftTypes", "scene_2_3_DistributionShiftTypes"),
    @("module3_causality", "StructuralCausalModel", "scene_3_1_StructuralCausalModel"),
    @("module3_causality", "ShiftBreaksSpuriousLink", "scene_3_2_ShiftBreaksSpuriousLink"),
    @("module3_causality", "CausalVsSpuriousTest", "scene_3_3_CausalVsSpuriousTest"),
    @("module4_irm", "ImportanceWeightingInterpolation", "scene_4_0_ImportanceWeightingInterpolation"),
    @("module4_irm", "InvariancePrinciple", "scene_4_1A_InvariancePrinciple"),
    @("module4_irm", "IRMInvariantIdea", "scene_4_1_IRMInvariantIdea"),
    @("module4_irm", "IRMRepresentationSpace", "scene_4_1B_IRMRepresentationSpace"),
    @("module4_irm", "IRMFormula", "scene_4_2_IRMFormula"),
    @("module4_irm", "IRMGradientVectors", "scene_4_3_IRMGradientVectors"),
    @("module4_irm", "IRMLimitations", "scene_4_4_IRMLimitations"),
    @("module4_irm", "NuRD", "scene_4_5_NuRD"),
    @("module4_irm", "NuRDDivergencePenalty", "scene_N1_5_NuRDDivergencePenalty"),
    @("module4_irm", "AvoidingInterpolation", "scene_RW4_AvoidingInterpolation"),
    @("module5_dro", "GroupDRO", "scene_5_1_GroupDRO"),
    @("module6_jtt", "SemanticCorruptions", "scene_6_0_SemanticCorruptions"),
    @("module6_jtt", "JTT", "scene_6_1_JTT"),
    @("module7_foundation", "ScaleDoesNotSolve", "scene_7_1_ScaleDoesNotSolve"),
    @("module7_foundation", "CLIPSpuriousWeb", "scene_7_2_CLIPSpuriousWeb"),
    @("module7_foundation", "ICLShortcuts", "scene_7_3_ICLShortcuts"),
    @("module7_foundation", "ReverseScaling", "scene_7_4_ReverseScaling"),
    @("module7_foundation", "PromptingForRobustness", "scene_7_5_PromptingForRobustness"),
    @("module7_foundation", "CATO", "scene_7_6_CATO"),
    @("module8_benchmarks", "BenchmarksReality", "scene_8_1_BenchmarksReality"),
    @("module8_benchmarks", "ModelSelectionParadox", "scene_8_2_ModelSelectionParadox"),
    @("module8_benchmarks", "BestPractices", "scene_8_3_BestPractices"),
    @("module9_outro", "JourneySummaryRemastered", "scene_9_1_JourneySummaryRemastered"),
    @("module9_outro", "BigTriangleConclusion", "scene_9_1B_BigTriangleConclusion"),
    @("module9_outro", "OpenProblemsCredits", "scene_9_2_OpenProblemsCredits")
)

foreach ($p in $pairs) {
    $module = $p[0]
    $scene = $p[1]
    $audio = $p[2]
    $video = "media\videos\$module\$QualityDir\$scene.mp4"
    $wav = "assets\narration_en\$audio.wav"
    $out = "media\videos\$module\$QualityDir\${scene}_vo48.mp4"
    
    if (-not (Test-Path $video)) { Write-Host "SKIP $scene (no video)"; continue }
    if (-not (Test-Path $wav)) { Write-Host "SKIP $scene (no audio)"; continue }
    
    Write-Host "Merging $scene..."
    ffmpeg -y -i $video -i $wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 160k -ar 48000 -ac 2 -shortest $out 2>$null
    
    $vdur = ffprobe -v error -show_entries format=duration -of csv=p=0 $video 2>$null
    $adur = ffprobe -v error -show_entries format=duration -of csv=p=0 $wav 2>$null
    $odur = ffprobe -v error -show_entries format=duration -of csv=p=0 $out 2>$null
    $delta = [math]::Round([double]$vdur - [double]$adur, 1)
    $status = if ([double]$vdur -ge [double]$adur) { "OK" } else { "AUDIO_CUT" }
    Write-Host "  video=${vdur}s audio=${adur}s output=${odur}s delta=${delta}s [$status]"
}
