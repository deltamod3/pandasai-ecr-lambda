# PandasAI Lambda Function Project

## Development
1. Install Python 3.8 or higher.
2. Create a new virtual environment: `python -m venv venv`.
3. Activate the created environment: `source venv/bin/activate`.
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the Flask app from the app directory: `flask run`.
6. Send GET or POST queries with JSON body to `localhost:5000/`.


## Deployment
We use the Serverless Framework to deploy the Docker container to Amazon Elastic Container Registry (ECR) and connect it to AWS Lambda.

### Prerequisites
1. Install Serverless Framework
2. Install AWS CLI
3. Configure AWS credential

### Update serverless.yml file
Before deploying, you need to update the serverless.yml file with your desired configuration. Make sure to specify the deployment stage, region, and other settings as needed.

```bash
provider:
  name: aws
  stage: dev
  region: eu-north-1
```

### Deploy with Serverless Framework

To deploy your API, use the following command:

```bash
sls deploy
```
This command will package your application, create an AWS Lambda function, and configure it to run the Docker container from the ECR repository.

Once the deployment is successful, you will receive the API endpoint URL that you can use to access your HTTP API endpoints.

### Reference
[- Deploy Python Lambda functions with container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)
[- Deploy Containerized Serverless Flask to AWS Lambda](https://medium.com/hoonio/deploy-containerized-serverless-flask-to-aws-lambda-c0eb87c1404d)