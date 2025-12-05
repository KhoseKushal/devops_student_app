# DevOps Student App - Complete Repo

This repository contains a complete end-to-end DevOps project for a **Student Form App** (HTML + Python Flask) deployed to **Azure AKS** with **Terraform**, **Docker**, **ACR**, and **GitHub Actions** (CI/CD).

## What is included
- `app/` — Flask application (templates + app.py)
- `Dockerfile` — Build the app image
- `k8s/` — Kubernetes manifests (Deployment + Service)
- `terraform/` — Terraform files to provision Azure resources (ACR, AKS, MySQL)
- `.github/workflows/` — GitHub Actions CI (build & push) and CD (deploy)
- `README.md` — this file
- `.gitignore`

> **IMPORTANT:** Replace placeholder names and secrets before running Terraform or CI. ACR name must be globally unique.

## Architecture (simple diagram)

Developer -> GitHub (repo)
  └─> GitHub Actions CI -> Build Docker image -> Push to ACR
  └─> GitHub Actions CD -> Connect to AKS -> kubectl apply -> AKS pulls image from ACR -> Kubernetes (Pods/Services) -> Users

## Quick start (local test)
1. Create a Python virtualenv and install packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
```
2. Set environment variables (example for local MySQL):
```bash
export DB_HOST=localhost
export DB_USER=root
export DB_PASSWORD=pass
export DB_NAME=studentdb
```
3. Run the app:
```bash
python app/app.py
# Open http://localhost:5000
```

## Terraform / Azure / GitHub
- Edit `terraform/variables.tf` to set names and passwords.
- Use `az login`, then:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
- Push the repo to GitHub and configure GitHub Secrets:
  - `AZURE_CREDENTIALS` (for azure/login action)
  - `ACR_NAME`
  - `AKS_RESOURCE_GROUP`
  - `AKS_CLUSTER_NAME`
  - `MYSQL_PASSWORD` (or use KeyVault)

## Files to inspect for customization
- `k8s/deployment.yaml` — set image path `<<ACR_NAME>>.azurecr.io/student-app:<<TAG>>`
- `terraform/main.tf` — contains resource names (change to match your naming)
- `.github/workflows/ci.yml` — set ACR name and image tag
- `.github/workflows/cd.yml` — set resource group and cluster name

--- 
Happy deploying!  
