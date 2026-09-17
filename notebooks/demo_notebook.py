# Databricks notebook source

print("Starting CI/CD demo notebook")

values = [1, 2, 3, 4]
total = sum(values)
print(f"Calculated total: {total}")

if total != 10:
    raise ValueError("Validation failed: expected total to equal 10")

print("Notebook validation passed")
