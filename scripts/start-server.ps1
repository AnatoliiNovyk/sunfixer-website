# Simple local server launcher for testing PWA/SW
param(
    [int]$Port = 8080
)

$publicPath = Join-Path (Split-Path -Parent $PSCommandPath) "..\public"
$publicPath = (Resolve-Path $publicPath).Path
Write-Host "Serving $publicPath on http://localhost:$Port/"

function TryPython {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd) {
        Write-Host "Using Python at" $cmd.Source
        python -m http.server $Port --directory $publicPath
        return $true
    }
    return $false
}

function TryNpxServe {
    $cmd = Get-Command npx -ErrorAction SilentlyContinue
    if ($cmd) {
        Write-Host "Using npx serve (if installed)"
        npx serve $publicPath -l $Port
        return $true
    }
    return $false
}

if (-not (TryPython)) {
    if (-not (TryNpxServe)) {
        Write-Error "Neither python nor npx serve is available. Install Python 3 or npm (serve)."
    }
}
