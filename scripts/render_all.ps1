param(
    [ValidateSet("l", "m", "h", "p", "k")]
    [string]$Quality = "l"
)

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$scenes = @(
    @("src/module0_hook.py", "OpeningClinicalNotes"),
    @("src/module0_hook.py", "RoadMap"),
    @("src/module1_erm.py", "ERMAccuracyIllusion"),
    @("src/module1_erm.py", "ERMAnatomy"),
    @("src/module1_erm.py", "SpuriousDefinition"),
    @("src/module1_erm.py", "FormalizingXYE"),
    @("src/module1_erm.py", "OODShiftBreaks"),
    @("src/module1_erm.py", "DistributionSetFamily"),
    @("src/module2_framework.py", "FormalizingVariables"),
    @("src/module2_framework.py", "IDOODDistributions"),
    @("src/module2_framework.py", "EnvironmentFormalization"),
    @("src/module2_framework.py", "DistributionSet"),
    @("src/module1_erm.py", "GeometryInductiveBias"),
    @("src/module1_erm.py", "GeometricSkewMaxMargin"),
    @("src/module2_framework.py", "RiskAggregation"),
    @("src/module2_framework.py", "RiskAggregationFamilies"),
    @("src/module2_framework.py", "GroupStructure"),
    @("src/module2_framework.py", "WorstGroupAccuracy"),
    @("src/module2_framework.py", "DistributionShiftTypes"),
    @("src/module3_causality.py", "StructuralCausalModel"),
    @("src/module3_causality.py", "ShiftBreaksSpuriousLink"),
    @("src/module3_causality.py", "CausalVsSpuriousTest"),
    @("src/module4_irm.py", "ImportanceWeightingInterpolation"),
    @("src/module4_irm.py", "InvariancePrinciple"),
    @("src/module4_irm.py", "IRMInvariantIdea"),
    @("src/module4_irm.py", "IRMRepresentationSpace"),
    @("src/module4_irm.py", "IRMFormula"),
    @("src/module4_irm.py", "IRMGradientVectors"),
    @("src/module4_irm.py", "IRMLimitations"),
    @("src/module4_irm.py", "NuRD"),
    @("src/module4_irm.py", "NuRDDivergencePenalty"),
    @("src/module4_irm.py", "AvoidingInterpolation"),
    @("src/module5_dro.py", "GroupDRO"),
    @("src/module6_jtt.py", "SemanticCorruptions"),
    @("src/module6_jtt.py", "JTT"),
    @("src/module7_foundation.py", "ScaleDoesNotSolve"),
    @("src/module7_foundation.py", "CLIPSpuriousWeb"),
    @("src/module7_foundation.py", "ICLShortcuts"),
    @("src/module7_foundation.py", "ReverseScaling"),
    @("src/module7_foundation.py", "PromptingForRobustness"),
    @("src/module7_foundation.py", "CATO"),
    @("src/module8_benchmarks.py", "BenchmarksReality"),
    @("src/module8_benchmarks.py", "ModelSelectionParadox"),
    @("src/module8_benchmarks.py", "BestPractices"),
    @("src/module9_outro.py", "JourneySummaryRemastered"),
    @("src/module9_outro.py", "BigTriangleConclusion"),
    @("src/module9_outro.py", "OpenProblemsCredits")
)

foreach ($scene in $scenes) {
    Write-Host "Rendering $($scene[1])"
    manim "-q$Quality" $scene[0] $scene[1]
}
