#!/bin/bash

# Step 1: Generate a unique tag
TIMESTAMP=$(date +%s)

# Step 2: Build the Docker image
echo "Building Docker image with tag: $TIMESTAMP"
docker build -t pyaephyo28/my-app:$TIMESTAMP ./app

# Step 3: Push the Docker image
echo "Pushing Docker image to Docker Hub"
docker push pyaephyo28/my-app:$TIMESTAMP

# Step 4: Update deployment.yaml with the new tag
echo "Updating deployment.yaml with the new image tag"
sed -i "s|image: pyaephyo28/my-app:.*|image: pyaephyo28/my-app:$TIMESTAMP|" manifests/deployment.yaml

# Step 5: Commit and push changes to Git
echo "Committing and pushing changes to Git"
git add manifests/deployment.yaml
git commit -m "Update image tag to $TIMESTAMP"
git push origin main

# Step 6: Reconcile FluxCD
echo "Reconciling FluxCD"
flux reconcile kustomization flux-system

echo "Deployment update completed successfully!"
