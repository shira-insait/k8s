#!/bin/bash

# Define the yaml files
declare -a files=("secrets.yaml" 
                  "backend-deployment.yaml" 
                  "backend-service.yaml" 
                  "frontend-deployment.yaml" 
                  "frontend-service.yaml" 
                  "nginx-deployment.yaml" 
                  "nginx-service.yaml" 
                  "nginx-configmap.yaml")

# Loop through the yaml files and apply them
for file in "${files[@]}"; do
    echo "Applying $file..."
    kubectl apply -f $file
    if [ $? -eq 0 ]; then
        echo "$file applied successfully."
    else
        echo "Failed to apply $file. Exiting script."
        exit 1
    fi
    echo ""
done

echo "All files applied successfully."
