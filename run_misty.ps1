param(
    [string]$ip = "192.168.0.41",
    [string]$condaEnv = "cs531_py311"
)

# Try to activate conda environment and run the GUI. If conda isn't available, fall back to .venv if present.
Write-Host "Starting Misty WoZ GUI for IP: $ip"

# Prefer using `conda run` (works even if conda isn't initialized in this shell).
$condaCmd = Get-Command conda -ErrorAction SilentlyContinue
if ($condaCmd) {
    Write-Host "Running via: conda run -n $condaEnv python main.py $ip"
    Set-Location -Path (Join-Path $PSScriptRoot "Misty WoZ")
    conda run -n $condaEnv python main.py $ip
    exit $LASTEXITCODE
} else {
    Write-Host "conda not found in PATH. Trying project .venv..."
    $venvPy = Join-Path $PSScriptRoot "Misty WoZ\.venv\Scripts\python.exe"
    if (Test-Path $venvPy) {
        & $venvPy (Join-Path $PSScriptRoot "Misty WoZ\main.py") $ip
        exit $LASTEXITCODE
    } else {
        Write-Host "No conda and no .venv python found. Please activate your desired environment and run: python main.py $ip"
        exit 1
    }
}
