# Yuno QA Automation Assessment

## Overview
This repository contains API automation tests for Yuno payment flows using
Python and Behave (BDD).

## Tech Stack
- Python
- Behave
- Requests

## Covered APIs
- Create Payment (Single-step & Authorization)
- Capture Authorization
- Cancel Payment
- Refund Payment
- Verify Payment
- Create Customer
- Enroll Payment Method

## Test Data
This project uses Yuno Test Payment Gateway sandbox cards to deterministically
simulate all transaction outcomes (SUCCEEDED, INSUFFICIENT_FUNDS, etc.).

## Execution
export PUBLIC_API_KEY=xxx
export PRIVATE_SECRET_KEY=xxx
export ACCOUNT_ID=xxx

pip install -r requirements.txt
behave
