# Use an official Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory to ${LAMBDA_TASK_ROOT}
WORKDIR ${LAMBDA_TASK_ROOT}

# Required to read the model files
RUN yum update -y && \
    yum install -y gcc g++ libgomp && \
    yum clean all

# Copy the current directory contents into the container at ${LAMBDA_TASK_ROOT}
COPY . ${LAMBDA_TASK_ROOT}

# Copy the requirements.txt file into the container at ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the CMD to run your Flask app
CMD ["app.handler"]