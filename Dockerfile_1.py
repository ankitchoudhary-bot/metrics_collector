# Use official PyTorch image
FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir \
    torch \
    torchvision \
    tqdm \
    kubernetes\
    kubeflow-katib

# Copy training script
COPY objective_fn.py .
COPY run.py .


# Default command for Katib trial execution
ENTRYPOINT ["python", "run.py"]