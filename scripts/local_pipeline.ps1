
$ErrorActionPreference = "Stop"

# Move to the project root
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$InfraPath = Join-Path $ProjectRoot "infra"

Write-Host "`n=== AI381 Lab 4: Local Pipeline ===" -ForegroundColor Cyan

# Step 1: Terraform format check
Write-Host "`n[1/5] Checking Terraform formatting..."
terraform -chdir="$InfraPath" fmt -check -recursive
if ($LASTEXITCODE -ne 0) { throw "Terraform format check failed." }

# Step 2: Terraform validation
Write-Host "`n[2/5] Validating Terraform..."
terraform -chdir="$InfraPath" validate
if ($LASTEXITCODE -ne 0) { throw "Terraform validation failed." }

# Step 3: Terraform plan
Write-Host "`n[3/5] Creating Terraform plan..."
terraform -chdir="$InfraPath" plan -out=tfplan
if ($LASTEXITCODE -ne 0) { throw "Terraform plan failed." }

# Step 4: Apply the plan
Write-Host "`n[4/5] Applying Terraform plan..."
terraform -chdir="$InfraPath" apply -auto-approve tfplan
if ($LASTEXITCODE -ne 0) { throw "Terraform apply failed." }

# Step 5: API smoke test
Write-Host "`n[5/5] Testing API health..."
$ApiUrl = terraform -chdir="$InfraPath" output -raw api_url
if ($LASTEXITCODE -ne 0) { throw "Could not read API URL." }

$Health = Invoke-RestMethod "$ApiUrl/health"
if ($Health.status -ne "ok") {
    throw "API health check failed."
}

Write-Host "`nPipeline completed successfully!" -ForegroundColor Green
$Health | Format-List
